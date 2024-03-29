# {document_title}

Title
: {document_title}

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

## 1 Introduction

This document contains all former and current terms in the {ratification_date} version of the Humboldt Extension for Ecological Inventories vocabulary (<http://rs.tdwg.org/version/eco/{ratification_date}>). The vocabulary uses the namespace abbreviation `eco:` for `http://rs.tdwg.org/eco/terms/` and `ecoiri:` for `http://rs.tdwg.org/eco/iri/`. 

For a simplified list that contains only the currently recommended terms, see the Humboldt Extension Quick Reference Guide (<https://eco.tdwg.org/terms/>).

### 1.1 Status of the content of this document

In Section 4, the values of the `Term IRI`, and `Definition` are normative. The values of `Term Name` are non-normative, although one can expect that the namespace abbreviation prefix is one commonly used for the term namespace.  `Label` and the values of all other properties (such as `Notes` and `Examples`) are non-normative.

### 1.2 RFC 2119 key words
The key words "MUST", "MUST NOT", "REQUIRED", "SHALL", "SHALL NOT", "SHOULD", "SHOULD NOT", "RECOMMENDED", "MAY", and "OPTIONAL" in this document are to be interpreted as described in [BCP 14](https://www.rfc-editor.org/info/bcp14) [\[RFC 2119\]](https://datatracker.ietf.org/doc/html/rfc2119) and [\[RFC 8174\]](https://datatracker.ietf.org/doc/html/rfc8174) when, and only when, they appear in all capitals, as shown here.

## 2 Use of Terms

The terms in this extension are meant to provide stable definitions that can be used in a variety of biodiversity inventory contexts but were envisioned principally to function together as an extension to Darwin Core. This vocabulary allows the reporting of detailed information about the inventory process such as i\) a general description of the survey, ii\) where an inventory takes place and the habitat characteristics and environmental conditions of survey sites, iii\) when an inventory takes place, iv\) the target taxonomic group, life stages, growth forms, and degrees of establishment of the organisms sampled, v\) the methodology implemented (inventory type performed, protocol(s) used, absence reported, material samples or vouchers collected, non-target taxa reported), and vi\) the completeness of the inventory and the sampling effort applied. 

This extension allows the representation of complex, highly nested survey designs. An ancillary document explaining how dwc:Event hierarchies for ecological inventories should be structured and providing guidance on the use of the terms in the context of parent and child dwc:Event(s) can be found at [http://rs.tdwg.org/dwc/doc/hierarchy/](https://tdwg.github.io/hc/hierarchy/). 

To assist in the interpretation of the term eco:isLeastSpecificTargetCategoryQuantityInclusive a detailed description of its use is provided at [http://rs.tdwg.org/dwc/doc/inclusive/](https://tdwg.github.io/hc/inclusive/).

Terms that are expected to have Booleans as values should use controlled value strings from the TDWG Boolean Controlled Vocabulary at [http://rs.tdwg.org/tag/doc/boolean/](https://tag.tdwg.org/boolean/) when those values are serialized in text form. See also the [Best practices for serializing booleans](https://tag.tdwg.org/guides/boolean/) and the [Boolean Values Best Practices Reference](https://tag.tdwg.org/reference/boolean/).

## 3 Term index

