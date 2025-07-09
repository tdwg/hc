#
# S. Van Hoey, John Wieczorek
#
# Build script for document handling
# Based on https://github.com/tdwg/dwc/blob/master/build/build.py
#

import io
import os
import re
import csv
import sys
import codecs

from urllib import request
from jinja2 import FileSystemLoader, Environment

NAMESPACES = {
    'http://rs.tdwg.org/eco/iri/' : 'ecoiri',
    'http://rs.tdwg.org/eco/terms/' : 'eco',
    'http://rs.tdwg.org/dwc/terms/attributes/' : 'tdwgutility'}

class DwcNamespaceError(Exception):
    """Namespace link is not available in the currently provided links"""
    pass

class DwcBuildReader():

    def __init__(self, dwc_build_file):
        """Custom Reader switching between raw Github or local file"""
        self.dwc_build_file = dwc_build_file

    def __enter__(self):
        if "https://raw.github" in self.dwc_build_file:
            self.open_dwc_term = request.urlopen(self.dwc_build_file)
        else:
            self.open_dwc_term = open(self.dwc_build_file, 'rb')
        return self.open_dwc_term

    def __exit__(self, *args):
        self.open_dwc_term.close()

class DwcDigester(object):

    def __init__(self, term_versions, qrg_term_versions):
        """Digest the term and qrg documents of Darwin Core to support automatic
        generation of derivatives

        Parameters
        -----------
        term_versions : str
            Either a relative path and filename of the normative Dwc document
            or a URL link to the raw Github version of the file
        qrg_term_versions : str
            Either a relative path and filename of the Quick Reference Guide term order 
            document or a URL link to the raw Github version of the file

        Notes
        -----
        Remark that the sequence of the term versions entries is
        essential for the automatic generation of the individual documents
        (mainly the index.html)
        """
        self.term_versions = term_versions
        self.qrg_term_versions = qrg_term_versions

        self.term_versions_data = {}
        self._store_versions()

        # create the defined data-object for the different outputs
        self.template_data = self.process_terms()
        self.properties = self.properties_list()

    def versions(self):
        """Iterator providing the terms as represented in the normative term
        versions file
        """
        with DwcBuildReader(self.term_versions) as versions:
            for vterm in csv.DictReader(io.TextIOWrapper(versions), delimiter=','):
                if vterm["status"] == "recommended":
                    yield vterm

    def _store_versions(self):
        """Collect all the versions data in a dictionary as the
        term_versions_data attribute
        """
        for term in self.versions():
            self.term_versions_data[term["term_iri"]] = term

    def _select_versions_term(self, term_iri):
        """Select a specific term of the versions data, using term_iri match
        """
        return self.term_versions_data[term_iri]

    @staticmethod
    def split_iri(term_iri):
        """Split an iri field into the namespace url and the local name
        of the term
        """
        prog = re.compile("(.*/)([^/]*$)")
        namespace, local_name = prog.findall(term_iri)[0]
        return namespace, local_name

    @staticmethod
    def resolve_namespace_abbrev(namespace):
        """Using the NAMESPACE constant, get the namespace abbreviation by
        providing the namespace link

        Parameters
        -----------
        namespace : str
            valid key of the NAMESPACES variable
        """
        if namespace not in NAMESPACES.keys():
            print("namespace url: %s", namespace)
            raise DwcNamespaceError("The namespace url is currently not supported in NAMESPACES")
        return NAMESPACES[namespace]

    def get_term_definition(self, term_iri):
        """Extract the required information from the terms table to show on
        the webpage of a single term by using the term_iri as the identifier

        Notes
        ------
        Due to the current implementation, make sure to provide the same keys
        represented in the record-level specific version `process_terms`
        method (room for improvement)
        """
        vs_term = self._select_versions_term(term_iri)

        term_data = {}
        term_data["label"] = vs_term['term_localName'] # See https://github.com/tdwg/dwc/issues/253#issuecomment-670098202
        term_data["iri"] = term_iri
        term_data["class"] = vs_term['organized_in']
        term_data["definition"] = self.convert_link(vs_term['definition'])
        term_data["comments"] = self.convert_link(self.convert_code(vs_term['comments']))
        term_data["examples"] = self.convert_link(self.convert_code(vs_term['examples']))
        term_data["rdf_type"] = vs_term['rdf_type']
        namespace_url, _ = self.split_iri(term_iri)
        term_data["namespace"] = self.resolve_namespace_abbrev(namespace_url)
        return term_data

    @staticmethod
    def convert_code(text_with_backticks):
        """Takes all back-quoted sections in a text field and converts it to
        the html tagged version of code blocks <code>...</code>
        """
        return re.sub(r'`([^`]*)`', r'<code>\1</code>', text_with_backticks)

    @staticmethod
    def convert_link(text_with_urls):
        """Takes all links in a text field and converts it to the html tagged
        version of the link
        """
        def _handle_matched(inputstring):
            """quick hack version of url handling on the current prime versions data"""
            url = inputstring.group()
            return "<a href=\"{}\">{}</a>".format(url, url)

        regx = r"(http[s]?://[\w\d:#@%/;$()~_?\+-;=\\\.&]*)(?<![\)\.])"
        return re.sub(regx, _handle_matched, text_with_urls)

    def process_terms(self):
        """Parse the config terms (sequence matters!)

        Collect all required data from both the normative versions file and
        the config file and return the template ready data.

        Returns
        -------
        Data object that can be digested by the html-template file. Contains
        the term data formatted to create the indidivual outputs, each list
        element is a dictionary representing a class group. Hence, the data
        object is structured as follows:

            [
                {'name' : class_group_name_1, 'label': xxxx,...,
                    'terms':
                        [
                            {'name' : term_1, 'label': xxxx,...},
                            {'name' : term_2, 'label': xxxx,...},
                            ...
                        ]}
                {'name' : class_group_name_2,...
                ...},
                ...
            ]
        """
        termdict = {}
        for term in self.versions(): # sequence of the terms file used as order
            term_data = self.get_term_definition(term['term_iri'])
            termdict[term['term_iri']] = term_data

        template_data = []
        class_group = {}

        with DwcBuildReader(self.qrg_term_versions) as versions:
            for vterm in csv.DictReader(io.TextIOWrapper(versions), delimiter=','):
                iri = vterm['recommended_term_iri']
                if iri.find('group:') == 0:
                    # Row is a group indicator starting with the string "group:"
                    # Make a class group to put terms in
                    class_group = {}
                    group_name = iri.rpartition(':')[-1].strip()
                    class_group["label"] = group_name
                    class_group["iri"] = None
                    class_group["class"] = None
                    class_group["definition"] = None
                    class_group["comments"] = None
                    class_group["rdf_type"] = None
                    class_group["namespace"] = None
                    class_group["terms"] = []
                    template_data.append(class_group)
                else:
                    # Row is a term to be listed with the most recent class_group
                    # Add the term, getting the details from the dictionary created from
                    # the term_versions.csv rather than the qrg_list.csv
                    term_data = termdict.get(iri)
                    class_group['terms'].append(term_data)
        return template_data

    def create_html(self, html_template="terms.tmpl",
                    html_output="../docs/terms/index.md"):
        """build html with the processed term info, by filling in the
        tmpl-template

        Parameters
        -----------
        html_template : str
            relative path and filename to the Jinja2 compatible
            template
        html_output : str
            relative path and filename to write the resulting index.html
        """

        data = {}
        data["class_groups"] = self.template_data

        env = Environment(
            loader = FileSystemLoader(os.path.dirname(html_template)),
            trim_blocks = True
        )
        template = env.get_template(os.path.basename(html_template))
        html = template.render(data)

        index_page = open(html_output, "w")
        index_page.write(str(html))
        index_page.close()

    def properties_list(self):
        """Make a list of all properties in the qrg-list
        """
        properties = []
        for group in self.template_data:
            for term in group['terms']:
                properties.append(term.get('label'))
        return properties

    def create_dwc_list(self, file_output="../dist/simple_eco_vertical.csv"):
        """Build a list of simple dwc terms and write it to file

        Parameters
        -----------
        file_output : str
            relative path and filename to write the resulting list
        """
        with codecs.open(file_output, 'w', 'utf-8') as dwc_list_file:
            for term in self.properties:
                dwc_list_file.write(term + "\n")

    def create_dwc_header(self, file_output="../dist/simple_eco_horizontal.csv"):
        """Build a header of simple dwc terms and write it to file

        Parameters
        -----------
        file_output : str
            relative path and filename to write the resulting list
        """
        with codecs.open(file_output, 'w', 'utf-8') as dwc_header_file:
            dwc_header_file.write(",".join(self.properties))
            dwc_header_file.write("\n")

def main():
    """Building up the quick reference html and derivatives"""

    term_versions_file = "../vocabulary/term_versions.csv"
    qrg_term_versions_file = "./qrg-list.csv"

    print("Running build process:")
    my_dwc = DwcDigester(term_versions_file, qrg_term_versions_file)
    print("Building quick reference guide")
    my_dwc.create_html()
    print("Building simple CSV files")
    my_dwc.create_dwc_list()
    my_dwc.create_dwc_header()
    print("Done!")


if __name__ == "__main__":
    sys.exit(main())
