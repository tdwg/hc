# Script to build Markdown pages that provide term metadata for complex vocabularies
# Steve Baskauf 2020-06-28 CC0
# Modified for use with Humboldt Extension 2022-05-29
# This script merges static Markdown header and footer documents with term information tables (in Markdown) generated from data in the rs.tdwg.org repo from the TDWG Github site

import re
import requests   # best library to manage HTTP transactions
import csv        # library to read/write/parse CSV files
import json       # library to convert JSON to Python data structures
import pandas as pd
import yaml

# -----------------
# Configuration section
# -----------------

github_branch = 'eco_final' # "main" for production, something else for development

# This is the base URL for raw files from the branch of the repo that has been pushed to GitHub
githubBaseUri = 'https://raw.githubusercontent.com/tdwg/rs.tdwg.org/' + github_branch + '/'

headerFileName = 'termlist-header.md'
footerFileName = 'termlist-footer.md'
outFileName = '../docs/list/index.md'

# This is a Python list of the database names of the term lists to be included in the document.
termLists = ['humboldt']

# If this list of terms is for terms in a single namespace, set the value of has_namespace to True. The value
# of has_namespace should be False for a list of terms that contains multiple namespaces.
has_namespace = True

# NOTE! There may be problems unless every term list is of the same vocabulary type since the number of columns will differ
# However, there probably aren't any circumstances where mixed types will be used to generate the same page.
vocab_type = 1 # 1 is simple vocabulary, 2 is simple controlled vocabulary, 3 is c.v. with broader hierarchy

# Terms in large vocabularies like Darwin and Audubon Cores may be organized into categories using tdwgutility_organizedInClass
# If so, those categories can be used to group terms in the generated term list document.
organized_in_categories = True

# If organized in categories, the display_order list must contain the IRIs that are values of tdwgutility_organizedInClass
# If not organized into categories, the value is irrelevant. There just needs to be one item in the list.
display_order = [ 'http://rs.tdwg.org/dwc/terms/Event']
display_label = ['Humboldt Extension Event terms']
display_comments = ['','']
display_id = ['event']

# ---------------
# Load header data
# ---------------

config_file_path = 'process/document_metadata_processing/dwc_doc_eco/'
contributors_yaml_file = 'authors_configuration.yaml'
document_configuration_yaml_file = 'document_configuration.yaml'

if has_namespace:
    # Load the configuration file used in the metadata creation process.
    metadata_config_text = requests.get(githubBaseUri + 'process/config.yaml').text
    metadata_config = yaml.load(metadata_config_text, Loader=yaml.FullLoader)
    namespace_uri = metadata_config['namespaces'][0]['namespace_uri']
    pref_namespace_prefix = metadata_config['namespaces'][0]['pref_namespace_prefix']

# Load the contributors YAML file from its GitHub URL
contributors_yaml_url = githubBaseUri + config_file_path + contributors_yaml_file
contributors_yaml = requests.get(contributors_yaml_url).text
if contributors_yaml == '404: Not Found':
    print('Contributors YAML file not found. Check the URL.')
    print(contributors_yaml_url)
    exit()
contributors_yaml = yaml.load(contributors_yaml, Loader=yaml.FullLoader)

# Load the document configuration YAML file from its GitHub URL
document_configuration_yaml_url = githubBaseUri + config_file_path + document_configuration_yaml_file
document_configuration_yaml = requests.get(document_configuration_yaml_url).text
document_configuration_yaml = yaml.load(document_configuration_yaml, Loader=yaml.FullLoader)

# ---------------
# Function definitions
# ---------------

# replace URL with link
#
def createLinks(text):
    def repl(match):
        if match.group(1)[-1] == '.':
            return '<a href="' + match.group(1)[:-1] + '">' + match.group(1)[:-1] + '</a>.'
        return '<a href="' + match.group(1) + '">' + match.group(1) + '</a>'

    pattern = '(https?://[^\s,;\)"]*)'
    result = re.sub(pattern, repl, text)
    return result

# 2021-08-06 Replace the createLinks() function with functions copied from the QRG build script written by S. Van Hoey
def convert_code(text_with_backticks):
    """Takes all back-quoted sections in a text field and converts it to
    the html tagged version of code blocks <code>...</code>
    """
    return re.sub(r'`([^`]*)`', r'<code>\1</code>', text_with_backticks)

def convert_link(text_with_urls):
    """Takes all links in a text field and converts it to the html tagged
    version of the link
    """
    def _handle_matched(inputstring):
        """quick hack version of url handling on the current prime versions data"""
        url = inputstring.group()
        return "<a href=\"{}\">{}</a>".format(url, url)

    regx = "(http[s]?://[\w\d:#@%/;$()~_?\+-;=\\\.&]*)(?<![\)\.,])"
    return re.sub(regx, _handle_matched, text_with_urls)

# Hack the code taken from the terms.tmpl template to insert the HTML necessary to make the semicolon-separated
# lists of examples into an HTML list.
# {% set examples = term.examples.split("; ") %}
# {% if examples | length == 1 %}{{ examples | first }}{% else %}<ul class="list-group list-group-flush">{% for example in examples %}<li class="list-group-item">{{ example }}</li>{% endfor %}</ul>{% endif %}
def convert_examples(text_with_list_of_examples: str) -> str:
    examples_list = text_with_list_of_examples.split('; ')
    if len(examples_list) == 1:
        return examples_list[0]
    else:
        output = '<ul class="list-group list-group-flush">\n'
        for example in examples_list:
            output += '  <li class="list-group-item">' + example + '</li>\n'
        output += '</ul>'
        return output

print('Retrieving term list metadata from GitHub')
term_lists_info = []

frame = pd.read_csv(githubBaseUri + 'term-lists/term-lists.csv', na_filter=False)
for termList in termLists:
    term_list_dict = {'list_iri': termList}
    term_list_dict = {'database': termList}
    for index,row in frame.iterrows():
        if row['database'] == termList:
            term_list_dict['pref_ns_prefix'] = row['vann_preferredNamespacePrefix']
            term_list_dict['pref_ns_uri'] = row['vann_preferredNamespaceUri']
            term_list_dict['list_iri'] = row['list']
    term_lists_info.append(term_list_dict)
#print(term_lists_info)

# Create column list
column_list = ['pref_ns_prefix', 'pref_ns_uri', 'term_localName', 'label', 'rdfs_comment', 'dcterms_description', 'examples', 'term_modified', 'term_deprecated', 'rdf_type', 'tdwgutility_abcdEquivalence', 'replaces_term', 'replaces1_term']
if vocab_type == 2:
    column_list += ['controlled_value_string']
elif vocab_type == 3:
    column_list += ['controlled_value_string', 'skos_broader']
if organized_in_categories:
    column_list.append('tdwgutility_organizedInClass')
column_list.append('version_iri')

print('Retrieving metadata about terms from all namespaces from GitHub')
# Create list of lists metadata table
table_list = []
for term_list in term_lists_info:
    # retrieve versions metadata for term list
    versions_url = githubBaseUri + term_list['database'] + '-versions/' + term_list['database'] + '-versions.csv'
    versions_df = pd.read_csv(versions_url, na_filter=False)
    
    # retrieve current term metadata for term list
    data_url = githubBaseUri + term_list['database'] + '/' + term_list['database'] + '.csv'
    frame = pd.read_csv(data_url, na_filter=False)
    for index,row in frame.iterrows():
        row_list = [term_list['pref_ns_prefix'], term_list['pref_ns_uri'], row['term_localName'], row['label'], row['rdfs_comment'], row['dcterms_description'], row['examples'], row['term_modified'], row['term_deprecated'], row['rdf_type'], row['tdwgutility_abcdEquivalence'], row['replaces_term'], row['replaces1_term']]
        #row_list = [term_list['pref_ns_prefix'], term_list['pref_ns_uri'], row['term_localName'], row['label'], row['definition'], row['usage'], row['notes'], row['term_modified'], row['term_deprecated'], row['type']]
        if vocab_type == 2:
            row_list += [row['controlled_value_string']]
        elif vocab_type == 3:
            if row['skos_broader'] =='':
                row_list += [row['controlled_value_string'], '']
            else:
                row_list += [row['controlled_value_string'], term_list['pref_ns_prefix'] + ':' + row['skos_broader']]
        if organized_in_categories:
            row_list.append(row['tdwgutility_organizedInClass'])

        # Borrowed terms really don't have implemented versions. They may be lacking values for version_status.
        # In their case, their version IRI will be omitted.
        found = False
        for vindex, vrow in versions_df.iterrows():
            if vrow['term_localName']==row['term_localName'] and vrow['version_status']=='recommended':
                found = True
                version_iri = vrow['version']
                # NOTE: the current hack for non-TDWG terms without a version is to append # to the end of the term IRI
                if version_iri[len(version_iri)-1] == '#':
                    version_iri = ''
        if not found:
            version_iri = ''
        row_list.append(version_iri)

        table_list.append(row_list)

print('processing data')
# Turn list of lists into dataframe
terms_df = pd.DataFrame(table_list, columns = column_list)

terms_sorted_by_label = terms_df.sort_values(by='label')
#terms_sorted_by_localname = terms_df.sort_values(by='term_localName')

# This makes sort case insensitive
terms_sorted_by_localname = terms_df.iloc[terms_df.term_localName.str.lower().argsort()]
#terms_sorted_by_localname
print('done retrieving')
print()

print('Generating term index by CURIE')
text = '### 3.1 Index By Term Name\n\n'
text += '(See also [3.2 Index By Label](#32-index-by-label))\n\n'

text += '**Classes**\n'
text += '\n'
for row_index,row in terms_sorted_by_localname.iterrows():
    if row['rdf_type'] == 'http://www.w3.org/2000/01/rdf-schema#Class':
        curie = row['pref_ns_prefix'] + ":" + row['term_localName']
        curie_anchor = curie.replace(':','_')
        text += '[' + curie + '](#' + curie_anchor + ') |\n'
text = text[:len(text)-2] # remove final trailing vertical bar and newline
text += '\n\n' # put back removed newline

for category in range(0,len(display_order)):
    text += '**' + display_label[category] + '**\n'
    text += '\n'
    if organized_in_categories:
        filtered_table = terms_sorted_by_localname[terms_sorted_by_localname['tdwgutility_organizedInClass']==display_order[category]]
        filtered_table.reset_index(drop=True, inplace=True)
    else:
        filtered_table = terms_sorted_by_localname
        
    for row_index,row in filtered_table.iterrows():
        if row['rdf_type'] != 'http://www.w3.org/2000/01/rdf-schema#Class':
            curie = row['pref_ns_prefix'] + ":" + row['term_localName']
            curie_anchor = curie.replace(':','_')
            text += '[' + curie + '](#' + curie_anchor + ') |\n'
    text = text[:len(text)-2] # remove final trailing vertical bar and newline
    text += '\n\n' # put back removed newline

index_by_name = text

#print(index_by_name)

print('Generating term index by label')
text = '\n\n'

# Comment out the following two lines if there is no index by local names
text = '### 3.2 Index By Label\n\n'
text += '(See also [3.1 Index By Term Name](#31-index-by-term-name))\n\n'

text += '**Classes**\n'
text += '\n'
for row_index,row in terms_sorted_by_label.iterrows():
    if row['rdf_type'] == 'http://www.w3.org/2000/01/rdf-schema#Class':
        curie_anchor = row['pref_ns_prefix'] + "_" + row['term_localName']
        text += '[' + row['label'] + '](#' + curie_anchor + ') |\n'
text = text[:len(text)-2] # remove final trailing vertical bar and newline
text += '\n\n' # put back removed newline

for category in range(0,len(display_order)):
    if organized_in_categories:
        text += '**' + display_label[category] + '**\n'
        text += '\n'
        filtered_table = terms_sorted_by_label[terms_sorted_by_label['tdwgutility_organizedInClass']==display_order[category]]
        filtered_table.reset_index(drop=True, inplace=True)
    else:
        filtered_table = terms_sorted_by_label
        
    for row_index,row in filtered_table.iterrows():
        if row_index == 0 or (row_index != 0 and row['label'] != filtered_table.iloc[row_index - 1].loc['label']): # this is a hack to prevent duplicate labels
            if row['rdf_type'] != 'http://www.w3.org/2000/01/rdf-schema#Class':
                curie_anchor = row['pref_ns_prefix'] + "_" + row['term_localName']
                text += '[' + row['label'] + '](#' + curie_anchor + ') |\n'
    text = text[:len(text)-2] # remove final trailing vertical bar and newline
    text += '\n\n' # put back removed newline

index_by_label = text

#print(index_by_label)

decisions_df = pd.read_csv('https://raw.githubusercontent.com/tdwg/rs.tdwg.org/master/decisions/decisions-links.csv', na_filter=False)

# ---------------
# generate a table for each term, with terms grouped by category
# ---------------

print('Generating terms table')
# generate the Markdown for the terms table
text = '## 4 Vocabulary\n'
if True:
    filtered_table = terms_sorted_by_localname

#for category in range(0,len(display_order)):
#    if organized_in_categories:
#        text += '### 4.' + str(category + 1) + ' ' + display_label[category] + '\n'
#        text += '\n'
#        text += display_comments[category] # insert the comments for the category, if any.
#        filtered_table = terms_sorted_by_localname[terms_sorted_by_localname['tdwgutility_organizedInClass']==display_order[category]]
#        filtered_table.reset_index(drop=True, inplace=True)
#    else:
#        filtered_table = terms_sorted_by_localname

    for row_index,row in filtered_table.iterrows():
        text += '<table>\n'
        curie = row['pref_ns_prefix'] + ":" + row['term_localName']
        curieAnchor = curie.replace(':','_')
        text += '\t<thead>\n'
        text += '\t\t<tr>\n'
        text += '\t\t\t<th colspan="2"><a id="' + curieAnchor + '"></a>Term Name  ' + curie + '</th>\n'
        text += '\t\t</tr>\n'
        text += '\t</thead>\n'
        text += '\t<tbody>\n'
        text += '\t\t<tr>\n'
        text += '\t\t\t<td>Term IRI</td>\n'
        uri = row['pref_ns_uri'] + row['term_localName']
        text += '\t\t\t<td><a href="' + uri + '">' + uri + '</a></td>\n'
        text += '\t\t</tr>\n'
        text += '\t\t<tr>\n'
        text += '\t\t\t<td>Modified</td>\n'
        text += '\t\t\t<td>' + row['term_modified'] + '</td>\n'
        text += '\t\t</tr>\n'

        if row['version_iri'] != '':
            text += '\t\t<tr>\n'
            text += '\t\t\t<td>Term version IRI</td>\n'
            text += '\t\t\t<td><a href="' + row['version_iri'] + '">' + row['version_iri'] + '</a></td>\n'
            text += '\t\t</tr>\n'

        text += '\t\t<tr>\n'
        text += '\t\t\t<td>Label</td>\n'
        text += '\t\t\t<td>' + row['label'] + '</td>\n'
        text += '\t\t</tr>\n'

        if row['term_deprecated'] != '':
            text += '\t\t<tr>\n'
            text += '\t\t\t<td></td>\n'
            text += '\t\t\t<td><strong>This term is deprecated and should no longer be used.</strong></td>\n'
            text += '\t\t</tr>\n'

            for dep_index,dep_row in filtered_table.iterrows():
                if dep_row['replaces_term'] == uri:
                    text += '\t\t<tr>\n'
                    text += '\t\t\t<td>Is replaced by</td>\n'
                    text += '\t\t\t<td><a href="#' + dep_row['pref_ns_prefix'] + "_" + dep_row['term_localName'] + '">' + dep_row['pref_ns_uri'] + dep_row['term_localName'] + '</a></td>\n'
                    text += '\t\t</tr>\n'
                if dep_row['replaces1_term'] == uri:
                    text += '\t\t<tr>\n'
                    text += '\t\t\t<td>Is replaced by</td>\n'
                    text += '\t\t\t<td><a href="#' + dep_row['pref_ns_prefix'] + "_" + dep_row['term_localName'] + '">' + dep_row['pref_ns_uri'] + dep_row['term_localName'] + '</a></td>\n'
                    text += '\t\t</tr>\n'

        text += '\t\t<tr>\n'
        text += '\t\t\t<td>Definition</td>\n'
        text += '\t\t\t<td>' + row['rdfs_comment'] + '</td>\n'
        #text += '\t\t\t<td>' + row['definition'] + '</td>\n'
        text += '\t\t</tr>\n'

        if row['dcterms_description'] != '':
        #if row['notes'] != '':
            text += '\t\t<tr>\n'
            text += '\t\t\t<td>Notes</td>\n'
            text += '\t\t\t<td>' + convert_link(convert_code(row['dcterms_description'])) + '</td>\n'
            #text += '\t\t\t<td>' + createLinks(row['notes']) + '</td>\n'
            text += '\t\t</tr>\n'

        if row['examples'] != '':
        #if row['usage'] != '':
            text += '\t\t<tr>\n'
            text += '\t\t\t<td>Examples</td>\n'
            text += '\t\t\t<td>' + convert_examples(convert_link(convert_code(row['examples']))) + '</td>\n'
            #text += '\t\t\t<td>' + createLinks(row['usage']) + '</td>\n'
            text += '\t\t</tr>\n'

        if row['tdwgutility_abcdEquivalence'] != '':
        #if row['usage'] != '':
            text += '\t\t<tr>\n'
            text += '\t\t\t<td>ABCD equivalence</td>\n'
            text += '\t\t\t<td>' + convert_link(convert_code(row['tdwgutility_abcdEquivalence'])) + '</td>\n'
            text += '\t\t</tr>\n'

        if vocab_type == 2 or vocab_type ==3: # controlled vocabulary
            text += '\t\t<tr>\n'
            text += '\t\t\t<td>Controlled value</td>\n'
            text += '\t\t\t<td>' + row['controlled_value_string'] + '</td>\n'
            text += '\t\t</tr>\n'

        if vocab_type == 3 and row['skos_broader'] != '': # controlled vocabulary with skos:broader relationships
            text += '\t\t<tr>\n'
            text += '\t\t\t<td>Has broader concept</td>\n'
            curieAnchor = row['skos_broader'].replace(':','_')
            text += '\t\t\t<td><a href="#' + curieAnchor + '">' + row['skos_broader'] + '</a></td>\n'
            text += '\t\t</tr>\n'

        text += '\t\t<tr>\n'
        text += '\t\t\t<td>Type</td>\n'
        if row['rdf_type'] == 'http://www.w3.org/1999/02/22-rdf-syntax-ns#Property':
        #if row['type'] == 'http://www.w3.org/1999/02/22-rdf-syntax-ns#Property':
            text += '\t\t\t<td>Property</td>\n'
        elif row['rdf_type'] == 'http://www.w3.org/2000/01/rdf-schema#Class':
        #elif row['type'] == 'http://www.w3.org/2000/01/rdf-schema#Class':
            text += '\t\t\t<td>Class</td>\n'
        elif row['rdf_type'] == 'http://www.w3.org/2004/02/skos/core#Concept':
        #elif row['type'] == 'http://www.w3.org/2004/02/skos/core#Concept':
            text += '\t\t\t<td>Concept</td>\n'
        else:
            text += '\t\t\t<td>' + row['rdf_type'] + '</td>\n' # this should rarely happen
            #text += '\t\t\t<td>' + row['type'] + '</td>\n' # this should rarely happen
        text += '\t\t</tr>\n'

        # Look up decisions related to this term
        for drow_index,drow in decisions_df.iterrows():
            if drow['linked_affected_resource'] == uri:
                text += '\t\t<tr>\n'
                text += '\t\t\t<td>Executive Committee decision</td>\n'
                text += '\t\t\t<td><a href="http://rs.tdwg.org/decisions/' + drow['decision_localName'] + '">http://rs.tdwg.org/decisions/' + drow['decision_localName'] + '</a></td>\n'
                text += '\t\t</tr>\n'                        

        text += '\t</tbody>\n'
        text += '</table>\n'
        text += '\n'
    text += '\n'
term_table = text
print('done generating')
print()

#print(term_table)

print('Merging term table with header and footer and saving file')
#text = index_by_label + term_table
text = index_by_name + index_by_label + term_table

# read in header and footer, merge with terms table, and output

headerObject = open(headerFileName, 'rt', encoding='utf-8')
header = headerObject.read()
headerObject.close()

# Build the Markdown for the contributors list
contributors = ''
for contributor in contributors_yaml:
    contributors += '[' + contributor['contributor_literal'] + '](' + contributor['contributor_iri'] + ') '
    contributors += '([' + contributor['affiliation'] + '](' + contributor['affiliation_uri'] + ')), '
contributors = contributors[:-2] # Remove the last comma and space

# Substitute values of ratification_date and contributors into the header template
header = header.replace('{document_title}', document_configuration_yaml['documentTitle'])
header = header.replace('{ratification_date}', document_configuration_yaml['doc_modified'])
header = header.replace('{created_date}', document_configuration_yaml['doc_created'])
header = header.replace('{contributors}', contributors)
header = header.replace('{standard_iri}', document_configuration_yaml['dcterms_isPartOf'])
header = header.replace('{current_iri}', document_configuration_yaml['current_iri'])
header = header.replace('{abstract}', document_configuration_yaml['abstract'])
header = header.replace('{creator}', document_configuration_yaml['creator'])
header = header.replace('{publisher}', document_configuration_yaml['publisher'])
year = document_configuration_yaml['doc_modified'].split('-')[0]
header = header.replace('{year}', year)
if has_namespace:
    header = header.replace('{namespace_uri}', namespace_uri)
    header = header.replace('{pref_namespace_prefix}', pref_namespace_prefix)

# Determine whether there was a previous version of the document.
if document_configuration_yaml['doc_created'] != document_configuration_yaml['doc_modified']:
    # Load versions list from document versions data in the rs.tdwg.org repo and find most recent version.
    versions_data_url = githubBaseUri + 'docs/docs-versions.csv'
    versions_list_df = pd.read_csv(versions_data_url, na_filter=False)
    # Slice all rows for versions of this document.
    matching_versions = versions_list_df[versions_list_df['current_iri']==document_configuration_yaml['current_iri']]
    # Sort the matching versions by version IRI in descending order so that the most recent version is first.
    matching_versions = matching_versions.sort_values(by=['version_iri'], ascending=[False])
    # The previous version is the second row in the dataframe (row 1).
    # The version IRI is in the second column (column 1).
    most_recent_version_iri = matching_versions.iat[1, 1]
    #print(most_recent_version_iri)

    # Insert the previous version information into the header
    previous_version_metadata_string = '''Previous version
: <''' + most_recent_version_iri + '''>

'''
    # Insert the previous version information into the designated slot.
    header = header.replace('{previous_version_slot}\n\n', previous_version_metadata_string)
else:
    # If there was no previous version, remove the slot from the header.
    header = header.replace('{previous_version_slot}\n\n', '')

footerObject = open(footerFileName, 'rt', encoding='utf-8')
footer = footerObject.read()
footerObject.close()

output = header + text + footer
outputObject = open(outFileName, 'wt', encoding='utf-8')
outputObject.write(output)
outputObject.close()
    
print('done')
