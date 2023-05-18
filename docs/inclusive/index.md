# isLeastSpecificTargetCategoryQuantityInclusive Guidelines

**Title:** isLeastSpecificTargetCategoryQuantityInclusive Guidelines

**Date version issued:** 2023-xx-xx

**Date created:** 2023-xx-xx

**Part of TDWG Standard:** http://www.tdwg.org/standards/450

**This version:** http://rs.tdwg.org/eco/doc/inclusive/2023-xx-xx

**Latest version:** http://rs.tdwg.org/eco/doc/inclusive/

**Abstract:** The Humboldt Extension mints the term isLeastSpecificTargetCategoryQuantityInclusive to describe how to treat counts of organisms when records from a single Event include multiple target categories. This document describes how to use that term.

**Contributors:** Yi Ming Gan, Wesley Hochachka, John Wieczorek, Yanina Sica

**Creator:** TDWG Humboldt Core Task Group

**Bibliographic citation:** Humboldt Core Task Group. 2023. isLeastSpecificTargetCategoryQuantityInclusive Guidelines. Biodiversity Information Standards (TDWG). http://rs.tdwg.org/eco/doc/inclusive/2023-xx-xx

## 1 Introduction (non-normative)

This document elaborates upon the meaning and use of the term `eco:isLeastSpecificTargetCategoryQuantityInclusive`.  Use of this term is necessary in order to describe how to treat counts of organisms (or any other organisms quantity)  when records from a single `dwc:Event` (<http://rs.tdwg.org/dwc/terms/Event>) include multiple target categories (e.g., taxonomic ranks within a higher rank or different life stages for the same species). For example, a statement whether the least specific target category quantity is inclusive should be reported when an `dwc:Event` includes records with  quantities that are associated with subcategories (e.g., subspecies) and other records reporting quantities  for a more general category (e.g., the full species).  In this example the species is the least specific category, because it is more general than the subspecies category nested below it.  Species and subspecies are just one example of a pair of category and subcategory.  Other examples of subcategories are life stages (e.g., “adult”, “larva”, “egg”), and sexes.

### 1.1 Status of the content of this document

Sections 3 of this document is normative. The other sections are non-normative.  


### 1.2 RFC 2119 key words
The key words "MUST", "MUST NOT", "REQUIRED", "SHALL", "SHALL NOT", "SHOULD", "SHOULD NOT", "RECOMMENDED", "MAY", and "OPTIONAL" in this document are to be interpreted as described in [RFC 2119](https://tools.ietf.org/html/rfc2119).

### 1.3 Namespaces and terminology

The namespace `eco:` abbreviates `http://rs.tdwg.org/eco/terms/` and is used with terms minted for the Humboldt Extension. `dwc:` abbreviates `http://rs.tdwg.org/dwc/terms/`, terms in the main Darwin Core vocabulary namespace. Words in `code markup` are term IRIs or literal values. The word "organisms" is used colloquially and is not used in the techincal sense of the `dwc:Organism` class.

## 2 Rationale (non-normative)

The term `eco:isLeastSpecificTargetCategoryQuantityInclusive` was introduced into the Humboldt Extension for ecological inventories late in development, after testing it with real-world cases ([Sica et al., 2022](#ref2)). Testing revealed that the quantities of organisms stored in two major biodiversity databases — OBIS (<a href="#ref1">OBIS, 2023</a>) and eBird (<a href="#ref3">Sullivan et al., 2014</a>) — need to be treated differently in order to calculate the total quantity of organisms in the least specific category.  In the specific case of data in the OBIS database, the information for a single `dwc:Event` can contain multiple records for a species, with one record for a species listing the quantity of individual organisms for the species without specifying any subcategory of life stage, and other records for the same species in the same `dwc:Event` listing quantities for separate life stages (e.g., one record for adults and another record for juveniles).  In this example the single `dwc:Event` will contain 3 records: one for the species without any life stage specified, one for adults of the species, and one for juveniles of the species.  For the OBIS data, the quantity in the record for which no life stage is specified is the sum of three quantities: the number of juveniles, the number of adults, and the number of individuals that were not recorded as belonging to any specific life stage.  In other words, when using OBIS data, the total quantity of individuals recorded for a species, across all life stages combined, has been pre-calculated and stored in the database; unless the quantities of individuals within specific life stages are of interest, the information in the life-stage subcategories can be ignored. The value of the term `eco:isLeastSpecificTargetCategoryQuantityInclusive` in this case would be `true` - the least specific category (species only) already includes the counts of the more specific subcategories.

eBird stores information about quantities of organisms differently.  For the example of a `dwc:Event` that contains separate records for subspecies and their parent species, the total number of individuals of the species needs to be calculated by the end user, where this total quantity is the sum of the number reported for the full species plus the numbers reported for the one or more subspecies.  In other words, the total quantity of organisms of each species has not been pre-calculated and must be derived by the end user. The value of the term `eco:isLeastSpecificTargetCategoryQuantityInclusive` in this case would be `false` - the least specific category (species only) does not include the counts of the more specific subcategories (subspecies).

In summary, the term `eco:isLeastSpecificTargetCategoryQuantityInclusive` is required to inform the end user of whether they will need to derive the total quantity of organisms for the least specific category (e.g., for a species), or whether this total quantity has already been calculated prior to the data being entered into the database.  Interestingly, if a data set contains only simple targets that have no subcategories, the result of the term `eco:isLeastSpecificTargetCategoryQuantityInclusive` being `true` or `false` is exactly the same - the count is the total in either case. Only in this circumstance does the term not strictly need to be populated. However, given that data records acquire a "life of their own" separate from their associated metadata when aggregated from multiple data sets, best practice would suggest that the term `eco:isLeastSpecificTargetCategoryQuantityInclusive` always be included and populated.

## 3 Usage guidelines (normative)

The term `eco:isLeastSpecificTargetCategoryQuantityInclusive` is defined as "The total detected quantity of organisms for a `dwc:Taxon` (including subsets thereof) in a `dwc:Event` is given explicitly in a single record (`dwc:organismQuantity` value) for that `dwc:Taxon`."

Values MUST be `true` and `false`. If `true`, the `dwc:organismQuantity` values for a taxon in a event is inclusive of all organisms of the taxon (including more specific scopes such as different life stages or lower taxonomic ranks) and the total detected quantity of organisms for that taxon in the event MUST NOT be determined by summing the dwc:organismQuantity values for all records of the taxon in the event. Instead, the total detected quantity of organisms for the taxon in an event MUST be reported in a single record for the taxon in the event, with this record having no further specific scopes. In this case the sum of `dwc:organismQuantity` values for the reported subsets of the taxon MUST NOT exceed the value of `dwc:organismQuantity` for the single record for the taxon without subsets (i.e., the total).  If `false`, the `dwc:organismQuantity` values for a taxon in an event MUST be added to get the total detected quantity of organisms for that taxon in the event. 

## 4 Examples (non-normative)

### 4.1 Single taxon example

As an example of the difference between `true` and `false` values for `eco:isLeastSpecificTargetCategoryQuantityInclusive`, suppose there are three records (see Table 1) with `dwc:organismQuantity` for a taxon (taxon_01) for an event (event_01). One record is for adults of the taxon with `dwc:organismQuantity` = `1` and `dwc:organismQuantityType` = `individuals`, one record is for juveniles of the Taxon with `dwc:organismQuantity` = `2` and `dwc:organismQuantityType` = `individuals`, and one record is for the taxon without specifying the life stage and with `dwc:organismQuantity` = `4` and `dwc:organismQuantityType` = `individuals`. 

If `eco:isLeastSpecificTargetCategoryQuantityInclusive` is `true` for event_01, then the total number of individuals of taxon_01 for the event is 4 (the least specific taxon record — the one with no more specific scopes — includes all individuals of the taxon). This means there was 1 adult, 2 juveniles and 1 individual of taxon_01 whose life stage was not recorded. 

If `eco:isLeastSpecificTargetCategoryQuantityInclusive` is `false` for event_01, then the total number of individuals of taxon_01 for the event is 7 (the least specific taxon record - the one with no more specific scopes - does not include all individuals of the taxon, rather, it is a separate category that must also be added to get the total). This means there was 1 adult, 2 juveniles and 4 individuals of taxon_01 whose life stage was not recorded.

**Table 1. Organism quantities in occurrence records**

| occurrenceID | eventID | taxonID | lifeStage | organismQuantity | organismQuantityType |
| ------------ | ------- | ------- | --------- | ---------------- | -------------------- |
| occ_01 | event_01 | taxon_01 | adult | 1 | individual |
| occ_02 | event_01 | taxon_01 | juvenile | 2 | individual |
| occ_03 | event_01 | taxon_01 |  | 4 | individual |

### 4.2 Nested taxa example

Suppose there are three records (see Table 2) with `dwc:organismQuantity` for three taxa (*Hirundo rustica* and two subspecies) for an event (event_01). The record for the species has `dwc:organismQuantity` = `3` and `dwc:organismQuantityType` = `individuals`. The record is for *H. r. rustica* has `dwc:organismQuantity` = `2` and `dwc:organismQuantityType` = `individuals`. The record for *H. r. gutturalis* has `dwc:organismQuantity` = `4` and `dwc:organismQuantityType` = `individuals`.

If `eco:isLeastSpecificTargetCategoryQuantityInclusive` is `true` for event_01, then the total number of individuals of for the species *H. rustica* for the Event is 3 (the least specific taxon record includes all individuals of the Taxon). This means there were 2 *H. r. rustica*, 1 *H. r. gutturalis*, and no other *H. rustica* of any kind detected.

If `eco:isLeastSpecificTargetCategoryQuantityInclusive` is `false` for event_01, then the total number of individuals of for the species *H. rustica* for the event is 6 (the least specific taxon record does not include all individuals of the taxon). This means there were 2 *H. r. rustica*, 1 *H. r. gutturalis*, and 3 other *H. rustica* detected that were not identified to subspecies. 

**Table 2. Organism quantities in event records**

| eventID | scientificName | organismQuantity | organismQuantityType |
| ------- | -------------- | ---------------- | -------------------- |
| event_01 | Hirundo rustica | 3 | individual |
| event_01 | Hirundo rustica rustica | 2 | individual |
| event_01 | Hirundo rustica gutturalis | 1 | individual |

# 5 References

<a id="ref1"></a>OBIS (2023) Ocean Biodiversity Information System. Intergovernmental Oceanographic Commission of UNESCO. <https://www.obis.org/>.

<a id="ref2"></a>Sica Y. V., K. Ingenloff, Y-M GAN, Z. Kachian, S. J. Baskauf, J. Wieczorek, P. F. Zermoglio, R. D. Stevenson (2022). Application of Humboldt Extension to Real-world Cases. *Biodiversity Information Science and Standards* 6: e91502. <https://doi.org/10.3897/biss.6.91502>

<a id="ref3"></a>Sullivan, B. L., J. L. Aycrigg, J. H. Barry, R. E. Bonney, N. Bruns, C. B. Cooper, T. Damoulas, A. A. Dhondt, T. Dietterich, A. Farnsworth, D. Fink, et al. (2014). The eBird enterprise: an integrated approach to development and application of citizen science. *Biological Conservation* 169:31-40. <https://10.1016/j.biocon.2013.11.003>
