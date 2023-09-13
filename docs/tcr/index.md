# Taxon Completeness Reported Controlled Vocabulary List of Terms

Title
: Taxon Completeness Reported Controlled Vocabulary List of Terms

Date version issued
: 2023-09-13

Date created
: 2023-09-13

Part of TDWG Standard
: <http://www.tdwg.org/standards/450>

This version
: <http://rs.tdwg.org/dwc/doc/tcr/2023-09-13>

Latest version
: <http://rs.tdwg.org/dwc/doc/tcr/>

Abstract
: The Humboldt Extension for Ecological Inventories mints the term `taxonCompletenessReported` to alert users that the inventory was conducted in such a way that all of the target taxa should have been detectable if they were present during the dwc:Event. This vocabulary provides terms that should be used as values for `eco:taxonCompletenessReported` and `ecoiri:taxonCompletenessReported`.

Contributors
: [Yanina V. Sica](https://orcid.org/0000-0002-1720-0127) ([Yale University](http://www.wikidata.org/entity/Q49112)), [Wesley M. Hochachka](https://orcid.org/0000-0002-0595-7827) ([Cornell Lab of Ornithology](http://www.wikidata.org/entity/Q2997535)), [Steven J. Baskauf](https://orcid.org/0000-0003-4365-3135) ([Vanderbilt University Libraries](http://www.wikidata.org/entity/Q16849893))

Creator
: TDWG Humboldt Extension Task Group

Bibliographic citation
: TDWG Humboldt Extension Task Group. 2023. Taxon Completeness Reported Controlled Vocabulary List of Terms. Biodiversity Information Standards (TDWG). <http://rs.tdwg.org/dwc/doc/tcr/2023-09-13>

## 1 Introduction (non-normative)

This document includes terms intended to be used as a controlled value for the Humboldt Extension terms with the local name `taxonCompletenessReported`. 

### 1.1 Status of the content of this document

Sections 1 and 3 are non-normative. Section 2 is normative. In Section 4, the values of the `Term IRI`, `Definition`, and `Controlled value` are normative. The value of `Usage` (if it exists for a given term) is normative. The values of `Term Name` are non-normative, although one can expect that the namespace abbreviation prefix is one commonly used for the term namespace. `Label` and the values of all other properties (such as `Notes`) are non-normative.

### 1.2 RFC 2119 key words
The key words "MUST", "MUST NOT", "REQUIRED", "SHALL", "SHALL NOT", "SHOULD", 
"SHOULD NOT", "RECOMMENDED", "MAY", and "OPTIONAL" in this document are to 
be interpreted as described in [BCP 14](https://datatracker.ietf.org/doc/html/bcp14)
[[RFC2119]](https://datatracker.ietf.org/doc/html/rfc2119)
[[RFC8174]](https://datatracker.ietf.org/doc/html/rfc8174)
when, and only when, they are written in capitals (as shown here).

### 1.3 Namespaces

The namespace `eco:` abbreviates `http://rs.tdwg.org/eco/terms/` and the namespace `ecoiri:` abbreviates `http://rs.tdwg.org/eco/iri/`. Both namespaces are used with terms minted for the Humboldt Extension for Ecological Inventories. `ecotcr:` abbreviates `http://rs.tdwg.org/ecotcr/values/`, and is used with terms in this vocabulary.

## 2 Use of Terms (normnative)

Due to the requirements of [Section 1.4.3 of the Darwin Core RDF Guide](http://rs.tdwg.org/dwc/terms/guides/rdf/#143-use-of-darwin-core-terms-in-rdf-normative), term IRIs MUST be used as values of `ecoiri:taxonCompletenessReported`. Controlled value strings MUST be used as values of `eco:taxonCompletenessReported`.

## 3 Term Index 

[not reported](#ecotcr_tcr00) |
[reported complete](#ecotcr_tcr01) |
[reported incomplete](#ecotcr_tcr02) |
[taxon completeness reported concept scheme](#ecotcr_tcr)

## 4 Vocabulary
<table>
	<thead>
		<tr>
			<th colspan="2"><a id="ecotcr_tcr"></a>Term Name  ecotcr:tcr</th>
		</tr>
	</thead>
	<tbody>
		<tr>
			<td>Term IRI</td>
			<td><a href="http://rs.tdwg.org/ecotcr/values/tcr">http://rs.tdwg.org/ecotcr/values/tcr</a></td>
		</tr>
		<tr>
			<td>Modified</td>
			<td>2023-09-13</td>
		</tr>
		<tr>
			<td>Term version IRI</td>
			<td><a href="http://rs.tdwg.org/ecotcr/values/version/tcr-2023-09-13">http://rs.tdwg.org/ecotcr/values/version/tcr-2023-09-13</a></td>
		</tr>
		<tr>
			<td>Label</td>
			<td>taxon completeness reported concept scheme</td>
		</tr>
		<tr>
			<td>Definition</td>
			<td>a SKOS concept scheme for categorizing taxon completeness reporting</td>
		</tr>
		<tr>
			<td>Type</td>
			<td>http://www.w3.org/2004/02/skos/core#ConceptScheme</td>
		</tr>
	</tbody>
</table>

<table>
	<thead>
		<tr>
			<th colspan="2"><a id="ecotcr_tcr00"></a>Term Name  ecotcr:tcr00</th>
		</tr>
	</thead>
	<tbody>
		<tr>
			<td>Term IRI</td>
			<td><a href="http://rs.tdwg.org/ecotcr/values/tcr00">http://rs.tdwg.org/ecotcr/values/tcr00</a></td>
		</tr>
		<tr>
			<td>Modified</td>
			<td>2023-09-13</td>
		</tr>
		<tr>
			<td>Term version IRI</td>
			<td><a href="http://rs.tdwg.org/ecotcr/values/version/tcr00-2023-09-13">http://rs.tdwg.org/ecotcr/values/version/tcr00-2023-09-13</a></td>
		</tr>
		<tr>
			<td>Label</td>
			<td>not reported</td>
		</tr>
		<tr>
			<td>Definition</td>
			<td>Taxonomic completeness was not assessed or reported for the dwc:Event.</td>
		</tr>
		<tr>
			<td>Controlled value</td>
			<td>notReported</td>
		</tr>
		<tr>
			<td>Type</td>
			<td>Concept</td>
		</tr>
	</tbody>
</table>

<table>
	<thead>
		<tr>
			<th colspan="2"><a id="ecotcr_tcr01"></a>Term Name  ecotcr:tcr01</th>
		</tr>
	</thead>
	<tbody>
		<tr>
			<td>Term IRI</td>
			<td><a href="http://rs.tdwg.org/ecotcr/values/tcr01">http://rs.tdwg.org/ecotcr/values/tcr01</a></td>
		</tr>
		<tr>
			<td>Modified</td>
			<td>2023-09-13</td>
		</tr>
		<tr>
			<td>Term version IRI</td>
			<td><a href="http://rs.tdwg.org/ecotcr/values/version/tcr01-2023-09-13">http://rs.tdwg.org/ecotcr/values/version/tcr01-2023-09-13</a></td>
		</tr>
		<tr>
			<td>Label</td>
			<td>reported complete</td>
		</tr>
		<tr>
			<td>Definition</td>
			<td>Taxonomic completeness was assessed for the dwc:Event, and it was determined to be complete.</td>
		</tr>
		<tr>
			<td>Controlled value</td>
			<td>reportedComplete</td>
		</tr>
		<tr>
			<td>Type</td>
			<td>Concept</td>
		</tr>
	</tbody>
</table>

<table>
	<thead>
		<tr>
			<th colspan="2"><a id="ecotcr_tcr02"></a>Term Name  ecotcr:tcr02</th>
		</tr>
	</thead>
	<tbody>
		<tr>
			<td>Term IRI</td>
			<td><a href="http://rs.tdwg.org/ecotcr/values/tcr02">http://rs.tdwg.org/ecotcr/values/tcr02</a></td>
		</tr>
		<tr>
			<td>Modified</td>
			<td>2023-09-13</td>
		</tr>
		<tr>
			<td>Term version IRI</td>
			<td><a href="http://rs.tdwg.org/ecotcr/values/version/tcr02-2023-09-13">http://rs.tdwg.org/ecotcr/values/version/tcr02-2023-09-13</a></td>
		</tr>
		<tr>
			<td>Label</td>
			<td>reported incomplete</td>
		</tr>
		<tr>
			<td>Definition</td>
			<td>Taxonomic completeness was assessed for the dwc:Event, and it was determined to be incomplete.</td>
		</tr>
		<tr>
			<td>Controlled value</td>
			<td>reportedIncomplete</td>
		</tr>
		<tr>
			<td>Type</td>
			<td>Concept</td>
		</tr>
	</tbody>
</table>


