# {document_title}

Title
: {document_title}

Namespace IRI
: {namespace_uri}

Preferred namespace abbreviation
: {pref_namespace_prefix}:

Date version issued
: {ratification_date}

Date created
: {created_date}

Part of TDWG Standard
: <{standard_iri}>

This version
: <{current_iri}{ratification_date}>

Latest version
: <{current_iri}>

{previous_version_slot}

Abstract
: {abstract}

Contributors
: {contributors}

Creator
: {creator}

Bibliographic citation
: {creator}. {year}. {document_title}. {publisher}. <{current_iri}{ratification_date}>

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

## 2 Use of Terms (normative)

Due to the requirements of [Section 1.4.3 of the Darwin Core RDF Guide](http://rs.tdwg.org/dwc/terms/guides/rdf/#143-use-of-darwin-core-terms-in-rdf-normative), term IRIs MUST be used as values of `ecoiri:taxonCompletenessReported`. Controlled value strings MUST be used as values of `eco:taxonCompletenessReported`.

