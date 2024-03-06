---
container: fluid
---

# Humboldt Extension quick reference guide

This document is intended to be an easy-to-read reference the currently recommended terms that extend the [Darwin Core standard](https://www.tdwg.org/standards/dwc/) with vocabulary to describe biological inventories. This document is not part of the standard. It draws on the [term names and definitions](../list/) from the normative part of the standard and combines them with comments and examples that are not normative, but that are meant to help people to use the terms consistently. The category to which all of the terms in this extension correspond is the Darwin Core Event (dwc:Event) class. Comprehensive metadata for current and obsolete terms in human readable form are found in a [list of terms document](../list/). CSV files with the [full history](https://github.com/tdwg/hc/blob/master/vocabulary/term_versions.csv) of the terms, with [horizontal and vertical lists](https://github.com/tdwg/hc/tree/master/dist) of these terms and the schema for the [Darwin Core Archive extension](https://github.com/tdwg/hc/tree/master/dist) can be found in the [Humboldt Extension repository](https://github.com/tdwg/hc).


## Site

<div class="my-4">
        <a class="btn btn-sm btn-outline-secondary m-1" href="#eco:siteCount">siteCount</a>
        <a class="btn btn-sm btn-outline-secondary m-1" href="#eco:siteNestingDescription">siteNestingDescription</a>
        <a class="btn btn-sm btn-outline-secondary m-1" href="#eco:verbatimSiteDescriptions">verbatimSiteDescriptions</a>
        <a class="btn btn-sm btn-outline-secondary m-1" href="#eco:verbatimSiteNames">verbatimSiteNames</a>
        <a class="btn btn-sm btn-outline-secondary m-1" href="#eco:geospatialScopeAreaValue">geospatialScopeAreaValue</a>
        <a class="btn btn-sm btn-outline-secondary m-1" href="#eco:geospatialScopeAreaUnit">geospatialScopeAreaUnit</a>
        <a class="btn btn-sm btn-outline-secondary m-1" href="#eco:totalAreaSampledValue">totalAreaSampledValue</a>
        <a class="btn btn-sm btn-outline-secondary m-1" href="#eco:totalAreaSampledUnit">totalAreaSampledUnit</a>
        <a class="btn btn-sm btn-outline-secondary m-1" href="#eco:reportedWeather">reportedWeather</a>
        <a class="btn btn-sm btn-outline-secondary m-1" href="#eco:reportedExtremeConditions">reportedExtremeConditions</a>
    </div>


<p class="invisible">
    <a id="eco:siteCount"></a><a id="siteCount"></a></p>
<table class="table table-sm table-bordered">
    <tbody>
        <tr class="table-secondary"><th colspan="2">siteCount <span class="badge badge-secondary float-right">Property</span></th></tr>
        <tr><td class="theme-label">Identifier</td><td><a href="http://rs.tdwg.org/eco/terms/siteCount">http://rs.tdwg.org/eco/terms/siteCount</a></td></tr>
        <tr><td class="theme-label">Definition</td><td>Total number of individual sites surveyed during the dwc:Event.</td></tr>
        <tr><td class="theme-label">Comments</td><td>Site refers to the location at which observations are made or samples/measurements are taken. The site can be at any level of hierarchy.</td></tr>
        <tr><td class="theme-label">Examples</td><td><ul class="list-group list-group-flush"><li class="list-group-item"><code>1</code></li><li class="list-group-item"><code>15</code></li></ul></td></tr>
    </tbody>
</table>
<p class="invisible">
    <a id="eco:siteNestingDescription"></a><a id="siteNestingDescription"></a></p>
<table class="table table-sm table-bordered">
    <tbody>
        <tr class="table-secondary"><th colspan="2">siteNestingDescription <span class="badge badge-secondary float-right">Property</span></th></tr>
        <tr><td class="theme-label">Identifier</td><td><a href="http://rs.tdwg.org/eco/terms/siteNestingDescription">http://rs.tdwg.org/eco/terms/siteNestingDescription</a></td></tr>
        <tr><td class="theme-label">Definition</td><td>Textual description of the hierarchical sampling design.</td></tr>
        <tr><td class="theme-label">Comments</td><td>Site refers to the location at which observations are made or samples/measurements are taken. The site can be at any level of hierarchy.</td></tr>
        <tr><td class="theme-label">Examples</td><td><code>5 sampling sites of 3-5 plots each</code></td></tr>
    </tbody>
</table>
<p class="invisible">
    <a id="eco:verbatimSiteDescriptions"></a><a id="verbatimSiteDescriptions"></a></p>
<table class="table table-sm table-bordered">
    <tbody>
        <tr class="table-secondary"><th colspan="2">verbatimSiteDescriptions <span class="badge badge-secondary float-right">Property</span></th></tr>
        <tr><td class="theme-label">Identifier</td><td><a href="http://rs.tdwg.org/eco/terms/verbatimSiteDescriptions">http://rs.tdwg.org/eco/terms/verbatimSiteDescriptions</a></td></tr>
        <tr><td class="theme-label">Definition</td><td>Original textual description of the site(s).</td></tr>
        <tr><td class="theme-label">Comments</td><td>Site refers to the location at which observations are made or samples/measurements are taken. The site can be at any level of hierarchy. Recommended best practice is to separate multiple values in a list with space vertical bar space ( | ).</td></tr>
        <tr><td class="theme-label">Examples</td><td><code>Wet flatwoods | Wet depression surrounded by mesic longleaf pine flatwoods | Ground cover of thick Andropogon spp., Sporobolus floridanus, Vaccinium spp, Rhynchospora spp., Centella erecta, Panicum rigidulum.</code></td></tr>
    </tbody>
</table>
<p class="invisible">
    <a id="eco:verbatimSiteNames"></a><a id="verbatimSiteNames"></a></p>
<table class="table table-sm table-bordered">
    <tbody>
        <tr class="table-secondary"><th colspan="2">verbatimSiteNames <span class="badge badge-secondary float-right">Property</span></th></tr>
        <tr><td class="theme-label">Identifier</td><td><a href="http://rs.tdwg.org/eco/terms/verbatimSiteNames">http://rs.tdwg.org/eco/terms/verbatimSiteNames</a></td></tr>
        <tr><td class="theme-label">Definition</td><td>A list (concatenated and separated) of original site names.</td></tr>
        <tr><td class="theme-label">Comments</td><td>Site refers to the location at which observations are made or samples/measurements are taken. The site can be at any level of hierarchy. Recommended best practice is to separate multiple values in a list with space vertical bar space ( | ).</td></tr>
        <tr><td class="theme-label">Examples</td><td><ul class="list-group list-group-flush"><li class="list-group-item"><code>East Coastal Fringe | St. Marks Wildlife Management Area</code></li><li class="list-group-item"><code>S1 | S2 | C1 | C2 | R14 | R22 | W1</code></li></ul></td></tr>
    </tbody>
</table>
<p class="invisible">
    <a id="eco:geospatialScopeAreaValue"></a><a id="geospatialScopeAreaValue"></a></p>
<table class="table table-sm table-bordered">
    <tbody>
        <tr class="table-secondary"><th colspan="2">geospatialScopeAreaValue <span class="badge badge-secondary float-right">Property</span></th></tr>
        <tr><td class="theme-label">Identifier</td><td><a href="http://rs.tdwg.org/eco/terms/geospatialScopeAreaValue">http://rs.tdwg.org/eco/terms/geospatialScopeAreaValue</a></td></tr>
        <tr><td class="theme-label">Definition</td><td>The numeric value for the total area of the geospatial scope of the dwc:Event.</td></tr>
        <tr><td class="theme-label">Comments</td><td>Geospatial scope refers to the dwc:Event location reported using the terms organized in Darwin Core under dcterms:Location. This area is always greater than or equal to the eco:totalAreaSampledValue. An eco:geospatialScopeAreaValue must have a corresponding eco:geospatialScopeAreaUnit.</td></tr>
        <tr><td class="theme-label">Examples</td><td><code>25</code></td></tr>
    </tbody>
</table>
<p class="invisible">
    <a id="eco:geospatialScopeAreaUnit"></a><a id="geospatialScopeAreaUnit"></a></p>
<table class="table table-sm table-bordered">
    <tbody>
        <tr class="table-secondary"><th colspan="2">geospatialScopeAreaUnit <span class="badge badge-secondary float-right">Property</span></th></tr>
        <tr><td class="theme-label">Identifier</td><td><a href="http://rs.tdwg.org/eco/terms/geospatialScopeAreaUnit">http://rs.tdwg.org/eco/terms/geospatialScopeAreaUnit</a></td></tr>
        <tr><td class="theme-label">Definition</td><td>The units associated with eco:geospatialScopeAreaValue</td></tr>
        <tr><td class="theme-label">Comments</td><td>Recommended best practice is to use a controlled vocabulary. For units containing exponents, use characters from the Unicode Latin-1 Supplement character set (hex 00B2 for squared and 00B3 for cubed).</td></tr>
        <tr><td class="theme-label">Examples</td><td><code>km²</code></td></tr>
    </tbody>
</table>
<p class="invisible">
    <a id="eco:totalAreaSampledValue"></a><a id="totalAreaSampledValue"></a></p>
<table class="table table-sm table-bordered">
    <tbody>
        <tr class="table-secondary"><th colspan="2">totalAreaSampledValue <span class="badge badge-secondary float-right">Property</span></th></tr>
        <tr><td class="theme-label">Identifier</td><td><a href="http://rs.tdwg.org/eco/terms/totalAreaSampledValue">http://rs.tdwg.org/eco/terms/totalAreaSampledValue</a></td></tr>
        <tr><td class="theme-label">Definition</td><td>The numeric value for the total area surveyed during the dwc:Event.</td></tr>
        <tr><td class="theme-label">Comments</td><td>This area is always less than or equal to the eco:geospatialScopeAreaValue. An eco:totalAreaSampledValue must have a corresponding eco:totalAreaSampledUnit.</td></tr>
        <tr><td class="theme-label">Examples</td><td><code>0.8</code></td></tr>
    </tbody>
</table>
<p class="invisible">
    <a id="eco:totalAreaSampledUnit"></a><a id="totalAreaSampledUnit"></a></p>
<table class="table table-sm table-bordered">
    <tbody>
        <tr class="table-secondary"><th colspan="2">totalAreaSampledUnit <span class="badge badge-secondary float-right">Property</span></th></tr>
        <tr><td class="theme-label">Identifier</td><td><a href="http://rs.tdwg.org/eco/terms/totalAreaSampledUnit">http://rs.tdwg.org/eco/terms/totalAreaSampledUnit</a></td></tr>
        <tr><td class="theme-label">Definition</td><td>The units associated with eco:totalAreaSampledValue</td></tr>
        <tr><td class="theme-label">Comments</td><td>Recommended best practice is to use a controlled vocabulary. For units containing exponents, use characters from the Unicode Latin-1 Supplement character set (hex 00B2 for squared and 00B3 for cubed).</td></tr>
        <tr><td class="theme-label">Examples</td><td><code>km²</code></td></tr>
    </tbody>
</table>
<p class="invisible">
    <a id="eco:reportedWeather"></a><a id="reportedWeather"></a></p>
<table class="table table-sm table-bordered">
    <tbody>
        <tr class="table-secondary"><th colspan="2">reportedWeather <span class="badge badge-secondary float-right">Property</span></th></tr>
        <tr><td class="theme-label">Identifier</td><td><a href="http://rs.tdwg.org/eco/terms/reportedWeather">http://rs.tdwg.org/eco/terms/reportedWeather</a></td></tr>
        <tr><td class="theme-label">Definition</td><td>A list of weather or climatic conditions present during the dwc:Event.</td></tr>
        <tr><td class="theme-label">Comments</td><td>Recommended best practice is to use a key:value encoding schema for a data interchange format such as JSON.</td></tr>
        <tr><td class="theme-label">Examples</td><td><code>{"minimumTemperatureInDegreesFahrenheit": 18, "maximumTemperatureInDegreesFahrenheit": 32}</code></td></tr>
    </tbody>
</table>
<p class="invisible">
    <a id="eco:reportedExtremeConditions"></a><a id="reportedExtremeConditions"></a></p>
<table class="table table-sm table-bordered">
    <tbody>
        <tr class="table-secondary"><th colspan="2">reportedExtremeConditions <span class="badge badge-secondary float-right">Property</span></th></tr>
        <tr><td class="theme-label">Identifier</td><td><a href="http://rs.tdwg.org/eco/terms/reportedExtremeConditions">http://rs.tdwg.org/eco/terms/reportedExtremeConditions</a></td></tr>
        <tr><td class="theme-label">Definition</td><td>A description of any extreme weather or environmental conditions that may have affected the dwc:Event.</td></tr>
        <tr><td class="theme-label">Comments</td><td></td></tr>
        <tr><td class="theme-label">Examples</td><td><ul class="list-group list-group-flush"><li class="list-group-item"><code>flooding during week 3 of surveys</code></li><li class="list-group-item"><code>rockslide at site 2</code></li></ul></td></tr>
    </tbody>
</table>


## Habitat Scope

<div class="my-4">
        <a class="btn btn-sm btn-outline-secondary m-1" href="#eco:targetHabitatScope">targetHabitatScope</a>
        <a class="btn btn-sm btn-outline-secondary m-1" href="#eco:excludedHabitatScope">excludedHabitatScope</a>
    </div>


<p class="invisible">
    <a id="eco:targetHabitatScope"></a><a id="targetHabitatScope"></a></p>
<table class="table table-sm table-bordered">
    <tbody>
        <tr class="table-secondary"><th colspan="2">targetHabitatScope <span class="badge badge-secondary float-right">Property</span></th></tr>
        <tr><td class="theme-label">Identifier</td><td><a href="http://rs.tdwg.org/eco/terms/targetHabitatScope">http://rs.tdwg.org/eco/terms/targetHabitatScope</a></td></tr>
        <tr><td class="theme-label">Definition</td><td>The habitats targeted for sampling during the dwc:Event.</td></tr>
        <tr><td class="theme-label">Comments</td><td>Recommended best practice is to use a controlled vocabulary and separate the values in a list with space vertical bar space ( | ).</td></tr>
        <tr><td class="theme-label">Examples</td><td><ul class="list-group list-group-flush"><li class="list-group-item"><code>dunes</code></li><li class="list-group-item"><code>pineForest</code></li><li class="list-group-item"><code>riparian</code></li><li class="list-group-item"><code>scrub | grassland</code></li></ul></td></tr>
    </tbody>
</table>
<p class="invisible">
    <a id="eco:excludedHabitatScope"></a><a id="excludedHabitatScope"></a></p>
<table class="table table-sm table-bordered">
    <tbody>
        <tr class="table-secondary"><th colspan="2">excludedHabitatScope <span class="badge badge-secondary float-right">Property</span></th></tr>
        <tr><td class="theme-label">Identifier</td><td><a href="http://rs.tdwg.org/eco/terms/excludedHabitatScope">http://rs.tdwg.org/eco/terms/excludedHabitatScope</a></td></tr>
        <tr><td class="theme-label">Definition</td><td>The habitats explicitly excluded from sampling during the dwc:Event.</td></tr>
        <tr><td class="theme-label">Comments</td><td>Recommended best practice is to use a controlled vocabulary and separate multiple values in a list with space vertical bar space ( | ).</td></tr>
        <tr><td class="theme-label">Examples</td><td><ul class="list-group list-group-flush"><li class="list-group-item"><code>wetFlatwoods</code></li><li class="list-group-item"><code>swamp | estuary</code></li></ul></td></tr>
    </tbody>
</table>


## Temporal Scope

<div class="my-4">
        <a class="btn btn-sm btn-outline-secondary m-1" href="#eco:eventDurationValue">eventDurationValue</a>
        <a class="btn btn-sm btn-outline-secondary m-1" href="#eco:eventDurationUnit">eventDurationUnit</a>
    </div>


<p class="invisible">
    <a id="eco:eventDurationValue"></a><a id="eventDurationValue"></a></p>
<table class="table table-sm table-bordered">
    <tbody>
        <tr class="table-secondary"><th colspan="2">eventDurationValue <span class="badge badge-secondary float-right">Property</span></th></tr>
        <tr><td class="theme-label">Identifier</td><td><a href="http://rs.tdwg.org/eco/terms/eventDurationValue">http://rs.tdwg.org/eco/terms/eventDurationValue</a></td></tr>
        <tr><td class="theme-label">Definition</td><td>The numeric value for the duration of the dwc:Event.</td></tr>
        <tr><td class="theme-label">Comments</td><td>An eco:eventDurationValue must have a corresponding eco:eventDurationUnit.</td></tr>
        <tr><td class="theme-label">Examples</td><td><ul class="list-group list-group-flush"><li class="list-group-item"><code>1</code></li><li class="list-group-item"><code>30</code></li></ul></td></tr>
    </tbody>
</table>
<p class="invisible">
    <a id="eco:eventDurationUnit"></a><a id="eventDurationUnit"></a></p>
<table class="table table-sm table-bordered">
    <tbody>
        <tr class="table-secondary"><th colspan="2">eventDurationUnit <span class="badge badge-secondary float-right">Property</span></th></tr>
        <tr><td class="theme-label">Identifier</td><td><a href="http://rs.tdwg.org/eco/terms/eventDurationUnit">http://rs.tdwg.org/eco/terms/eventDurationUnit</a></td></tr>
        <tr><td class="theme-label">Definition</td><td>The units associated with the eco:eventDurationValue.</td></tr>
        <tr><td class="theme-label">Comments</td><td>Recommended best practice is to use a controlled vocabulary.</td></tr>
        <tr><td class="theme-label">Examples</td><td><ul class="list-group list-group-flush"><li class="list-group-item"><code>minutes</code></li><li class="list-group-item"><code>hours</code></li><li class="list-group-item"><code>days</code></li><li class="list-group-item"><code>months</code></li><li class="list-group-item"><code>years</code></li></ul></td></tr>
    </tbody>
</table>


## Taxonomic Scope

<div class="my-4">
        <a class="btn btn-sm btn-outline-secondary m-1" href="#eco:targetTaxonomicScope">targetTaxonomicScope</a>
        <a class="btn btn-sm btn-outline-secondary m-1" href="#eco:excludedTaxonomicScope">excludedTaxonomicScope</a>
        <a class="btn btn-sm btn-outline-secondary m-1" href="#eco:taxonCompletenessReported">taxonCompletenessReported</a>
        <a class="btn btn-sm btn-outline-secondary m-1" href="#eco:taxonCompletenessProtocols">taxonCompletenessProtocols</a>
        <a class="btn btn-sm btn-outline-secondary m-1" href="#eco:isTaxonomicScopeFullyReported">isTaxonomicScopeFullyReported</a>
        <a class="btn btn-sm btn-outline-secondary m-1" href="#eco:isAbsenceReported">isAbsenceReported</a>
        <a class="btn btn-sm btn-outline-secondary m-1" href="#eco:absentTaxa">absentTaxa</a>
        <a class="btn btn-sm btn-outline-secondary m-1" href="#eco:hasNonTargetTaxa">hasNonTargetTaxa</a>
        <a class="btn btn-sm btn-outline-secondary m-1" href="#eco:nonTargetTaxa">nonTargetTaxa</a>
        <a class="btn btn-sm btn-outline-secondary m-1" href="#eco:areNonTargetTaxaFullyReported">areNonTargetTaxaFullyReported</a>
    </div>


<p class="invisible">
    <a id="eco:targetTaxonomicScope"></a><a id="targetTaxonomicScope"></a></p>
<table class="table table-sm table-bordered">
    <tbody>
        <tr class="table-secondary"><th colspan="2">targetTaxonomicScope <span class="badge badge-secondary float-right">Property</span></th></tr>
        <tr><td class="theme-label">Identifier</td><td><a href="http://rs.tdwg.org/eco/terms/targetTaxonomicScope">http://rs.tdwg.org/eco/terms/targetTaxonomicScope</a></td></tr>
        <tr><td class="theme-label">Definition</td><td>The taxonomic group(s) targeted for sampling during the dwc:Event.</td></tr>
        <tr><td class="theme-label">Comments</td><td>The dwc:Event to which the eco:targetTaxonomicScope refers could be at any level of hierarchy. In the case of a higher level (parent) dwc:Event, include all taxonomic groups surveyed in the child dwc:Events that contributed to the parent dwc:Event. Recommended best practice is to separate multiple values in a list with space vertical bar space ( | ).</td></tr>
        <tr><td class="theme-label">Examples</td><td><ul class="list-group list-group-flush"><li class="list-group-item"><code>Aves</code></li><li class="list-group-item"><code>Aves | Mammalia</code></li><li class="list-group-item"><code>Procellariformes</code></li></ul></td></tr>
    </tbody>
</table>
<p class="invisible">
    <a id="eco:excludedTaxonomicScope"></a><a id="excludedTaxonomicScope"></a></p>
<table class="table table-sm table-bordered">
    <tbody>
        <tr class="table-secondary"><th colspan="2">excludedTaxonomicScope <span class="badge badge-secondary float-right">Property</span></th></tr>
        <tr><td class="theme-label">Identifier</td><td><a href="http://rs.tdwg.org/eco/terms/excludedTaxonomicScope">http://rs.tdwg.org/eco/terms/excludedTaxonomicScope</a></td></tr>
        <tr><td class="theme-label">Definition</td><td>The taxonomic group(s) explicitly excluded from sampling during the dwc:Event.</td></tr>
        <tr><td class="theme-label">Comments</td><td>The dwc:Event to which the eco:excludedTaxonomicScope refers could be at any level of hierarchy. In the case of a higher level (parent) dwc:Event, include all the taxonomic groups explicitly excluded from the child dwc:Events that contributed to the parent dwc:Event. Recommended best practice is to separate multiple values in a list with space vertical bar space ( | ).</td></tr>
        <tr><td class="theme-label">Examples</td><td><ul class="list-group list-group-flush"><li class="list-group-item"><code>Aves</code></li><li class="list-group-item"><code>Quercus | Acer</code></li></ul></td></tr>
    </tbody>
</table>
<p class="invisible">
    <a id="eco:taxonCompletenessReported"></a><a id="taxonCompletenessReported"></a></p>
<table class="table table-sm table-bordered">
    <tbody>
        <tr class="table-secondary"><th colspan="2">taxonCompletenessReported <span class="badge badge-secondary float-right">Property</span></th></tr>
        <tr><td class="theme-label">Identifier</td><td><a href="http://rs.tdwg.org/eco/terms/taxonCompletenessReported">http://rs.tdwg.org/eco/terms/taxonCompletenessReported</a></td></tr>
        <tr><td class="theme-label">Definition</td><td>Statement about whether the taxonomic completeness of the dwc:Event was assessed.</td></tr>
        <tr><td class="theme-label">Comments</td><td>This term is meant to alert users that the inventory was conducted in such a way that all of the target taxa (the combination of eco:targetTaxonomicScope and eco:excludedTaxonomicScope) should have been detectable if they were present during the dwc:Event. This term can provide data users with a qualitative measure of how comprehensively an area has been surveyed, which assists in interpreting species populations, areas of occupancy, inferring species absences, etc. This term is only relevant if the dwc:Event used restricted search or open search methods. If taxonomic completeness was assessed, the methods used or an explanation of the basis of the completeness should be stated in eco: taxonCompletenessProtocols. Recommended best practice is to use controlled value strings from the controlled vocabulary designated for use with this term, listed at <a href="http://rs.tdwg.org/dwc/doc/tcr/">http://rs.tdwg.org/dwc/doc/tcr/</a>.</td></tr>
        <tr><td class="theme-label">Examples</td><td><ul class="list-group list-group-flush"><li class="list-group-item"><code>notReported</code></li><li class="list-group-item"><code>reportedComplete</code></li><li class="list-group-item"><code>reportedIncomplete</code></li></ul></td></tr>
    </tbody>
</table>
<p class="invisible">
    <a id="eco:taxonCompletenessProtocols"></a><a id="taxonCompletenessProtocols"></a></p>
<table class="table table-sm table-bordered">
    <tbody>
        <tr class="table-secondary"><th colspan="2">taxonCompletenessProtocols <span class="badge badge-secondary float-right">Property</span></th></tr>
        <tr><td class="theme-label">Identifier</td><td><a href="http://rs.tdwg.org/eco/terms/taxonCompletenessProtocols">http://rs.tdwg.org/eco/terms/taxonCompletenessProtocols</a></td></tr>
        <tr><td class="theme-label">Definition</td><td>A description of or reference (publication, URL) to the methods used to determine eco:taxonCompletenessReported.</td></tr>
        <tr><td class="theme-label">Comments</td><td>This term allows users to determine how comprehensively an area has been sampled. Recommended best practice is to separate multiple values in a list with space vertical bar space ( | ).</td></tr>
        <tr><td class="theme-label">Examples</td><td><ul class="list-group list-group-flush"><li class="list-group-item"><code>census | based on sampling effort</code></li><li class="list-group-item"> <code>based on species accumulation curves</code></li></ul></td></tr>
    </tbody>
</table>
<p class="invisible">
    <a id="eco:isTaxonomicScopeFullyReported"></a><a id="isTaxonomicScopeFullyReported"></a></p>
<table class="table table-sm table-bordered">
    <tbody>
        <tr class="table-secondary"><th colspan="2">isTaxonomicScopeFullyReported <span class="badge badge-secondary float-right">Property</span></th></tr>
        <tr><td class="theme-label">Identifier</td><td><a href="http://rs.tdwg.org/eco/terms/isTaxonomicScopeFullyReported">http://rs.tdwg.org/eco/terms/isTaxonomicScopeFullyReported</a></td></tr>
        <tr><td class="theme-label">Definition</td><td>Every dwc:Organism that was included within the taxonomic scope, and was detected during the dwc:Event, was reported.</td></tr>
        <tr><td class="theme-label">Comments</td><td>This term is only relevant if the dwc:Event used restricted search or open search methods. If all dwc:Organisms included within the taxonomic scope and detected during the dwc:Event were reported, the value should be 'true'. Taxonomic scope is based on the combination of eco:targetTaxonomicScope and eco:excludedTaxonomicScope.</td></tr>
        <tr><td class="theme-label">Examples</td><td><ul class="list-group list-group-flush"><li class="list-group-item"><code>true</code></li><li class="list-group-item"><code>false</code></li></ul></td></tr>
    </tbody>
</table>
<p class="invisible">
    <a id="eco:isAbsenceReported"></a><a id="isAbsenceReported"></a></p>
<table class="table table-sm table-bordered">
    <tbody>
        <tr class="table-secondary"><th colspan="2">isAbsenceReported <span class="badge badge-secondary float-right">Property</span></th></tr>
        <tr><td class="theme-label">Identifier</td><td><a href="http://rs.tdwg.org/eco/terms/isAbsenceReported">http://rs.tdwg.org/eco/terms/isAbsenceReported</a></td></tr>
        <tr><td class="theme-label">Definition</td><td>Taxonomic absences were reported.</td></tr>
        <tr><td class="theme-label">Comments</td><td>Absences can be reported at any taxonomic level.</td></tr>
        <tr><td class="theme-label">Examples</td><td><ul class="list-group list-group-flush"><li class="list-group-item"><code>true</code></li><li class="list-group-item"><code>false</code></li></ul></td></tr>
    </tbody>
</table>
<p class="invisible">
    <a id="eco:absentTaxa"></a><a id="absentTaxa"></a></p>
<table class="table table-sm table-bordered">
    <tbody>
        <tr class="table-secondary"><th colspan="2">absentTaxa <span class="badge badge-secondary float-right">Property</span></th></tr>
        <tr><td class="theme-label">Identifier</td><td><a href="http://rs.tdwg.org/eco/terms/absentTaxa">http://rs.tdwg.org/eco/terms/absentTaxa</a></td></tr>
        <tr><td class="theme-label">Definition</td><td>A list (concatenated and separated) of taxa reported absent during the dwc:Event.</td></tr>
        <tr><td class="theme-label">Comments</td><td>Absences can be reported at any taxonomic level. Recommended best practice is to separate multiple values in a list with space vertical bar space ( | ).</td></tr>
        <tr><td class="theme-label">Examples</td><td><ul class="list-group list-group-flush"><li class="list-group-item"><code>Parabuteo unicinctus | Geranoaetus melanoleucus</code></li><li class="list-group-item"><code>Cetoniinae | Aclopinae | Cyclocephala modesta</code></li></ul></td></tr>
    </tbody>
</table>
<p class="invisible">
    <a id="eco:hasNonTargetTaxa"></a><a id="hasNonTargetTaxa"></a></p>
<table class="table table-sm table-bordered">
    <tbody>
        <tr class="table-secondary"><th colspan="2">hasNonTargetTaxa <span class="badge badge-secondary float-right">Property</span></th></tr>
        <tr><td class="theme-label">Identifier</td><td><a href="http://rs.tdwg.org/eco/terms/hasNonTargetTaxa">http://rs.tdwg.org/eco/terms/hasNonTargetTaxa</a></td></tr>
        <tr><td class="theme-label">Definition</td><td>One or more dwc:Organisms of taxa outside the target taxonomic scope (the combination of eco:targetTaxonomicScope and eco:excludedTaxonomicScope) were detected and reported for this dwc:Event.</td></tr>
        <tr><td class="theme-label">Comments</td><td>This term is meant to alert users to the presence of non-target taxa (in some disciplines called “bycatch”) reported in this dwc:Event. This term is relevant only if a target taxonomic scope is declared. Taxonomic scope is based on the combination of eco:targetTaxonomicScope and eco:excludedTaxonomicScope. Examination of the taxonomic scope is needed in order to identify the non-target taxa. It should be possible to confirm the expectations by investigating the dwc:Occurrences in this dwc:Event and in its child dwc:Events (if available) or by exploring eco:nonTargetTaxa for this dwc:Event (if populated). The value of this term should be 'true' if dwc:Occurrences of taxa outside the taxonomic scope as defined at the time of the dwc:Event are reported, otherwise the value of this term should be 'false'.</td></tr>
        <tr><td class="theme-label">Examples</td><td><ul class="list-group list-group-flush"><li class="list-group-item"><code>true</code></li><li class="list-group-item"><code>false</code></li></ul></td></tr>
    </tbody>
</table>
<p class="invisible">
    <a id="eco:nonTargetTaxa"></a><a id="nonTargetTaxa"></a></p>
<table class="table table-sm table-bordered">
    <tbody>
        <tr class="table-secondary"><th colspan="2">nonTargetTaxa <span class="badge badge-secondary float-right">Property</span></th></tr>
        <tr><td class="theme-label">Identifier</td><td><a href="http://rs.tdwg.org/eco/terms/nonTargetTaxa">http://rs.tdwg.org/eco/terms/nonTargetTaxa</a></td></tr>
        <tr><td class="theme-label">Definition</td><td>A list (concatenated and separated) of taxa reported during the dwc:Event that are outside of the target taxonomic scope (the combination of eco:targetTaxonomicScope and eco:excludedTaxonomicScope).</td></tr>
        <tr><td class="theme-label">Comments</td><td>This term is meant to allow the full list of taxa that are considered outside of the taxonomic scope and yet were reported in the dataset to be shared. This term is relevant only if a target taxonomic scope is declared and eco:hasNonTargetTaxa is ‘true’. Taxonomic scope is based on the combination of eco:targetTaxonomicScope and eco:excludedTaxonomicScope. Non-target taxa (in some disciplines called “bycatch”) can be reported at any taxonomic level. Recommended best practice is to separate multiple values in a list with space vertical bar space ( | ).</td></tr>
        <tr><td class="theme-label">Examples</td><td><ul class="list-group list-group-flush"><li class="list-group-item"><code>Parabuteo unicinctus | Geranoaetus melanoleucus</code></li><li class="list-group-item"><code>Cetoniinae | Aclopinae | Cyclocephala modesta</code></li></ul></td></tr>
    </tbody>
</table>
<p class="invisible">
    <a id="eco:areNonTargetTaxaFullyReported"></a><a id="areNonTargetTaxaFullyReported"></a></p>
<table class="table table-sm table-bordered">
    <tbody>
        <tr class="table-secondary"><th colspan="2">areNonTargetTaxaFullyReported <span class="badge badge-secondary float-right">Property</span></th></tr>
        <tr><td class="theme-label">Identifier</td><td><a href="http://rs.tdwg.org/eco/terms/areNonTargetTaxaFullyReported">http://rs.tdwg.org/eco/terms/areNonTargetTaxaFullyReported</a></td></tr>
        <tr><td class="theme-label">Definition</td><td>Every dwc:Organism that was outside of the target taxonomic scope (the combination of eco:targetTaxonomicScope and eco:excludedTaxonomicScope) and detected during the dwc:Event, and that was detectable using the given protocol (given in eco:protocolDescription and dwc:samplingProtocol), was reported.</td></tr>
        <tr><td class="theme-label">Comments</td><td>This term is meant to inform a user of the data whether there were non-target taxa that were detected, but left unreported. This term is only relevant if the dwc:Event used restricted search or open search methods and if a target taxonomic scope is declared. Taxonomic scope is based on the combination of eco:targetTaxonomicScope and eco:excludedTaxonomicScope. Within dwc:Events that used either a restricted search or an open search method and declared a taxonomic scope, if all dwc:Organisms that are not included within the target taxonomic scope and that were detected during the dwc:Event were reported, the value of this term should be 'true', otherwise the value of this term should be ‘false'.</td></tr>
        <tr><td class="theme-label">Examples</td><td><ul class="list-group list-group-flush"><li class="list-group-item"><code>true</code></li><li class="list-group-item"><code>false</code></li></ul></td></tr>
    </tbody>
</table>


## Organismal Scope

<div class="my-4">
        <a class="btn btn-sm btn-outline-secondary m-1" href="#eco:targetLifeStageScope">targetLifeStageScope</a>
        <a class="btn btn-sm btn-outline-secondary m-1" href="#eco:excludedLifeStageScope">excludedLifeStageScope</a>
        <a class="btn btn-sm btn-outline-secondary m-1" href="#eco:isLifeStageScopeFullyReported">isLifeStageScopeFullyReported</a>
        <a class="btn btn-sm btn-outline-secondary m-1" href="#eco:targetDegreeOfEstablishmentScope">targetDegreeOfEstablishmentScope</a>
        <a class="btn btn-sm btn-outline-secondary m-1" href="#eco:excludedDegreeOfEstablishmentScope">excludedDegreeOfEstablishmentScope</a>
        <a class="btn btn-sm btn-outline-secondary m-1" href="#eco:isDegreeOfEstablishmentScopeFullyReported">isDegreeOfEstablishmentScopeFullyReported</a>
        <a class="btn btn-sm btn-outline-secondary m-1" href="#eco:targetGrowthFormScope">targetGrowthFormScope</a>
        <a class="btn btn-sm btn-outline-secondary m-1" href="#eco:excludedGrowthFormScope">excludedGrowthFormScope</a>
        <a class="btn btn-sm btn-outline-secondary m-1" href="#eco:isGrowthFormScopeFullyReported">isGrowthFormScopeFullyReported</a>
        <a class="btn btn-sm btn-outline-secondary m-1" href="#eco:hasNonTargetOrganisms">hasNonTargetOrganisms</a>
        <a class="btn btn-sm btn-outline-secondary m-1" href="#eco:verbatimTargetScope">verbatimTargetScope</a>
    </div>


<p class="invisible">
    <a id="eco:targetLifeStageScope"></a><a id="targetLifeStageScope"></a></p>
<table class="table table-sm table-bordered">
    <tbody>
        <tr class="table-secondary"><th colspan="2">targetLifeStageScope <span class="badge badge-secondary float-right">Property</span></th></tr>
        <tr><td class="theme-label">Identifier</td><td><a href="http://rs.tdwg.org/eco/terms/targetLifeStageScope">http://rs.tdwg.org/eco/terms/targetLifeStageScope</a></td></tr>
        <tr><td class="theme-label">Definition</td><td>The age classes or life stages of the dwc:Organisms targeted for sampling during the dwc:Event.</td></tr>
        <tr><td class="theme-label">Comments</td><td>This term is defined based on dwc:lifeStage (<a href="http://rs.tdwg.org/dwc/terms/lifeStage">http://rs.tdwg.org/dwc/terms/lifeStage</a>). Recommended best practice is to use the same controlled vocabulary as for dwc:lifeStage and to separate multiple values in a list with space vertical bar space ( | ).</td></tr>
        <tr><td class="theme-label">Examples</td><td><ul class="list-group list-group-flush"><li class="list-group-item"><code>larva</code></li><li class="list-group-item"><code>adult | juvenile</code></li></ul></td></tr>
    </tbody>
</table>
<p class="invisible">
    <a id="eco:excludedLifeStageScope"></a><a id="excludedLifeStageScope"></a></p>
<table class="table table-sm table-bordered">
    <tbody>
        <tr class="table-secondary"><th colspan="2">excludedLifeStageScope <span class="badge badge-secondary float-right">Property</span></th></tr>
        <tr><td class="theme-label">Identifier</td><td><a href="http://rs.tdwg.org/eco/terms/excludedLifeStageScope">http://rs.tdwg.org/eco/terms/excludedLifeStageScope</a></td></tr>
        <tr><td class="theme-label">Definition</td><td>The age classes or life stages of the dwc:Organisms explicitly excluded from sampling during the dwc:Event.</td></tr>
        <tr><td class="theme-label">Comments</td><td>This term is defined based on dwc:lifeStage (<a href="http://rs.tdwg.org/dwc/terms/lifeStage">http://rs.tdwg.org/dwc/terms/lifeStage</a>). Recommended best practice is to use the same controlled vocabulary as for dwc:lifeStage and to separate multiple values in a list with space vertical bar space ( | ).</td></tr>
        <tr><td class="theme-label">Examples</td><td><ul class="list-group list-group-flush"><li class="list-group-item"><code>seedling</code></li><li class="list-group-item"><code>nestling | fledgling</code></li></ul></td></tr>
    </tbody>
</table>
<p class="invisible">
    <a id="eco:isLifeStageScopeFullyReported"></a><a id="isLifeStageScopeFullyReported"></a></p>
<table class="table table-sm table-bordered">
    <tbody>
        <tr class="table-secondary"><th colspan="2">isLifeStageScopeFullyReported <span class="badge badge-secondary float-right">Property</span></th></tr>
        <tr><td class="theme-label">Identifier</td><td><a href="http://rs.tdwg.org/eco/terms/isLifeStageScopeFullyReported">http://rs.tdwg.org/eco/terms/isLifeStageScopeFullyReported</a></td></tr>
        <tr><td class="theme-label">Definition</td><td>Every dwc:Organism that was included within the life stage scope, and was detected during the dwc:Event, was reported.</td></tr>
        <tr><td class="theme-label">Comments</td><td>This term is only relevant if the dwc:Event used restricted search or open search methods. If all dwc:Organisms included within the life stage scope and detected during the dwc:Event were reported, the value should be 'true'. Life stage scope is based on the combination of eco:targetLifeStageScope and eco:excludedLifeStageScope.</td></tr>
        <tr><td class="theme-label">Examples</td><td><ul class="list-group list-group-flush"><li class="list-group-item"><code>true</code></li><li class="list-group-item"><code>false</code></li></ul></td></tr>
    </tbody>
</table>
<p class="invisible">
    <a id="eco:targetDegreeOfEstablishmentScope"></a><a id="targetDegreeOfEstablishmentScope"></a></p>
<table class="table table-sm table-bordered">
    <tbody>
        <tr class="table-secondary"><th colspan="2">targetDegreeOfEstablishmentScope <span class="badge badge-secondary float-right">Property</span></th></tr>
        <tr><td class="theme-label">Identifier</td><td><a href="http://rs.tdwg.org/eco/terms/targetDegreeOfEstablishmentScope">http://rs.tdwg.org/eco/terms/targetDegreeOfEstablishmentScope</a></td></tr>
        <tr><td class="theme-label">Definition</td><td>The degrees of establishment of the dwc:Organisms targeted for sampling during the dwc:Event.</td></tr>
        <tr><td class="theme-label">Comments</td><td>Recommended best practice is to use controlled value strings from the controlled vocabulary (<a href="http://rs.tdwg.org/dwcdoe/">http://rs.tdwg.org/dwcdoe/</a>) for dwc:degreeOfEstablishment. For details, refer to <a href="https://doi.org/10.3897/biss.3.38084">https://doi.org/10.3897/biss.3.38084</a>. Recommended best practice is to separate multiple values in a list with space vertical bar space ( | ).</td></tr>
        <tr><td class="theme-label">Examples</td><td><ul class="list-group list-group-flush"><li class="list-group-item"><code>native</code></li><li class="list-group-item"><code>invasive | widespreadInvasive</code></li></ul></td></tr>
    </tbody>
</table>
<p class="invisible">
    <a id="eco:excludedDegreeOfEstablishmentScope"></a><a id="excludedDegreeOfEstablishmentScope"></a></p>
<table class="table table-sm table-bordered">
    <tbody>
        <tr class="table-secondary"><th colspan="2">excludedDegreeOfEstablishmentScope <span class="badge badge-secondary float-right">Property</span></th></tr>
        <tr><td class="theme-label">Identifier</td><td><a href="http://rs.tdwg.org/eco/terms/excludedDegreeOfEstablishmentScope">http://rs.tdwg.org/eco/terms/excludedDegreeOfEstablishmentScope</a></td></tr>
        <tr><td class="theme-label">Definition</td><td>The degrees of establishment of the dwc:Organisms explicitly excluded from sampling during the dwc:Event.</td></tr>
        <tr><td class="theme-label">Comments</td><td>Recommended best practice is to use controlled value strings from the controlled vocabulary (<a href="http://rs.tdwg.org/dwcdoe/">http://rs.tdwg.org/dwcdoe/</a>) for dwc:degreeOfEstablishment. For details, refer to <a href="https://doi.org/10.3897/biss.3.38084">https://doi.org/10.3897/biss.3.38084</a>. Recommended best practice is to separate multiple values in a list with space vertical bar space ( | ).</td></tr>
        <tr><td class="theme-label">Examples</td><td><ul class="list-group list-group-flush"><li class="list-group-item"><code>native</code></li><li class="list-group-item"><code>invasive | widespreadInvasive</code></li></ul></td></tr>
    </tbody>
</table>
<p class="invisible">
    <a id="eco:isDegreeOfEstablishmentScopeFullyReported"></a><a id="isDegreeOfEstablishmentScopeFullyReported"></a></p>
<table class="table table-sm table-bordered">
    <tbody>
        <tr class="table-secondary"><th colspan="2">isDegreeOfEstablishmentScopeFullyReported <span class="badge badge-secondary float-right">Property</span></th></tr>
        <tr><td class="theme-label">Identifier</td><td><a href="http://rs.tdwg.org/eco/terms/isDegreeOfEstablishmentScopeFullyReported">http://rs.tdwg.org/eco/terms/isDegreeOfEstablishmentScopeFullyReported</a></td></tr>
        <tr><td class="theme-label">Definition</td><td>Every dwc:Organism that was included within the degree of establishment scope, and was detected during the dwc:Event, was reported.</td></tr>
        <tr><td class="theme-label">Comments</td><td>This term is only relevant if the dwc:Event used restricted search or open search methods. If all dwc:Organisms included within the degree of establishment scope and detected during the dwc:Event were reported, the value should be 'true'. Degree of establishment scope is based on the combination of eco:targetDegreeOfEstablishmentScope and eco:excludedDegreeOfEstablishmentScope.</td></tr>
        <tr><td class="theme-label">Examples</td><td><ul class="list-group list-group-flush"><li class="list-group-item"><code>true</code></li><li class="list-group-item"><code>false</code></li></ul></td></tr>
    </tbody>
</table>
<p class="invisible">
    <a id="eco:targetGrowthFormScope"></a><a id="targetGrowthFormScope"></a></p>
<table class="table table-sm table-bordered">
    <tbody>
        <tr class="table-secondary"><th colspan="2">targetGrowthFormScope <span class="badge badge-secondary float-right">Property</span></th></tr>
        <tr><td class="theme-label">Identifier</td><td><a href="http://rs.tdwg.org/eco/terms/targetGrowthFormScope">http://rs.tdwg.org/eco/terms/targetGrowthFormScope</a></td></tr>
        <tr><td class="theme-label">Definition</td><td>The growth forms or habits of the dwc:Organisms targeted for sampling during the dwc:Event.</td></tr>
        <tr><td class="theme-label">Comments</td><td>Recommended best practice is to use a controlled vocabulary and separate multiple values in a list with space vertical bar space ( | ).</td></tr>
        <tr><td class="theme-label">Examples</td><td><ul class="list-group list-group-flush"><li class="list-group-item"><code>tree</code></li><li class="list-group-item"><code>shrub | subShrub</code></li></ul></td></tr>
    </tbody>
</table>
<p class="invisible">
    <a id="eco:excludedGrowthFormScope"></a><a id="excludedGrowthFormScope"></a></p>
<table class="table table-sm table-bordered">
    <tbody>
        <tr class="table-secondary"><th colspan="2">excludedGrowthFormScope <span class="badge badge-secondary float-right">Property</span></th></tr>
        <tr><td class="theme-label">Identifier</td><td><a href="http://rs.tdwg.org/eco/terms/excludedGrowthFormScope">http://rs.tdwg.org/eco/terms/excludedGrowthFormScope</a></td></tr>
        <tr><td class="theme-label">Definition</td><td>The growth forms or habits of the dwc:Organisms explicitly excluded from sampling during the dwc:Event.</td></tr>
        <tr><td class="theme-label">Comments</td><td>Recommended best practice is to use a controlled vocabulary and separate multiple values in a list with space vertical bar space ( | ).</td></tr>
        <tr><td class="theme-label">Examples</td><td><ul class="list-group list-group-flush"><li class="list-group-item"><code>tree</code></li><li class="list-group-item"><code>shrub | subShrub</code></li></ul></td></tr>
    </tbody>
</table>
<p class="invisible">
    <a id="eco:isGrowthFormScopeFullyReported"></a><a id="isGrowthFormScopeFullyReported"></a></p>
<table class="table table-sm table-bordered">
    <tbody>
        <tr class="table-secondary"><th colspan="2">isGrowthFormScopeFullyReported <span class="badge badge-secondary float-right">Property</span></th></tr>
        <tr><td class="theme-label">Identifier</td><td><a href="http://rs.tdwg.org/eco/terms/isGrowthFormScopeFullyReported">http://rs.tdwg.org/eco/terms/isGrowthFormScopeFullyReported</a></td></tr>
        <tr><td class="theme-label">Definition</td><td>Every dwc:Organism that was included within the growth form scope, and was detected during the dwc:Event, was reported.</td></tr>
        <tr><td class="theme-label">Comments</td><td>This term is only relevant if the dwc:Event used restricted search or open search methods. If all dwc:Organisms included within the growth form scope and detected during the dwc:Event were reported, the value should be 'true'. Growth form scope is based on the combination of eco:targetGrowthFormScope and eco:excludedGrowthFormScope.</td></tr>
        <tr><td class="theme-label">Examples</td><td><ul class="list-group list-group-flush"><li class="list-group-item"><code>true</code></li><li class="list-group-item"><code>false</code></li></ul></td></tr>
    </tbody>
</table>
<p class="invisible">
    <a id="eco:hasNonTargetOrganisms"></a><a id="hasNonTargetOrganisms"></a></p>
<table class="table table-sm table-bordered">
    <tbody>
        <tr class="table-secondary"><th colspan="2">hasNonTargetOrganisms <span class="badge badge-secondary float-right">Property</span></th></tr>
        <tr><td class="theme-label">Identifier</td><td><a href="http://rs.tdwg.org/eco/terms/hasNonTargetOrganisms">http://rs.tdwg.org/eco/terms/hasNonTargetOrganisms</a></td></tr>
        <tr><td class="theme-label">Definition</td><td>One or more dwc:Organisms outside the target organismal scopes (eco:targetDegreeOfEstablishmentScope, eco:targetGrowthFormScope, and eco:targetLifeStageScope) were detected and reported for this dwc:Event.</td></tr>
        <tr><td class="theme-label">Comments</td><td>This term is meant to alert users to the presence of non-target organisms (in some disciplines called “bycatch”) reported in this dwc:Event. This term is relevant only if a target organismal scope is declared. Organismal scope is based on the combination of all of the following terms: eco:targetLifeStageScope, eco:excludedLifeStageScope, eco:targetDegreeOfEstablishmentScope, eco:excludedDegreeOfEstablishmentScope, eco:targetGrowthFormScope, and eco:excludedGrowthFormScope. Examination of the organismal scope is needed in order to identify the non-target dwc:Organisms. It should be possible to confirm the expectations by investigating the dwc:Occurrences in this dwc:Event and in its child dwc:Events (if available). The value of this term should be 'true' if dwc:Occurrences of dwc:Organisms outside the organismal scope(s) as defined at the time of the dwc:Event are reported, otherwise the value of this term should be 'false'.</td></tr>
        <tr><td class="theme-label">Examples</td><td><ul class="list-group list-group-flush"><li class="list-group-item"><code>true</code></li><li class="list-group-item"><code>false</code></li></ul></td></tr>
    </tbody>
</table>
<p class="invisible">
    <a id="eco:verbatimTargetScope"></a><a id="verbatimTargetScope"></a></p>
<table class="table table-sm table-bordered">
    <tbody>
        <tr class="table-secondary"><th colspan="2">verbatimTargetScope <span class="badge badge-secondary float-right">Property</span></th></tr>
        <tr><td class="theme-label">Identifier</td><td><a href="http://rs.tdwg.org/eco/terms/verbatimTargetScope">http://rs.tdwg.org/eco/terms/verbatimTargetScope</a></td></tr>
        <tr><td class="theme-label">Definition</td><td>The verbatim original description of the dwc:Event scope.</td></tr>
        <tr><td class="theme-label">Comments</td><td>Recommended best practice is first to populate explicit scope terms to the fullest extent possible (e.g., eco:targetTaxonomicScope). It is not recommended to use this term in assessing absence or completeness.</td></tr>
        <tr><td class="theme-label">Examples</td><td><ul class="list-group list-group-flush"><li class="list-group-item"><code>small mammals</code></li><li class="list-group-item"><code>freshwater macroinvertebrates</code></li><li class="list-group-item"><code>dead animals</code>, <code>ground-living insects</code></li></ul></td></tr>
    </tbody>
</table>


## Methodology Description

<div class="my-4">
        <a class="btn btn-sm btn-outline-secondary m-1" href="#eco:compilationTypes">compilationTypes</a>
        <a class="btn btn-sm btn-outline-secondary m-1" href="#eco:compilationSourceTypes">compilationSourceTypes</a>
        <a class="btn btn-sm btn-outline-secondary m-1" href="#eco:inventoryTypes">inventoryTypes</a>
        <a class="btn btn-sm btn-outline-secondary m-1" href="#eco:protocolNames">protocolNames</a>
        <a class="btn btn-sm btn-outline-secondary m-1" href="#eco:protocolDescriptions">protocolDescriptions</a>
        <a class="btn btn-sm btn-outline-secondary m-1" href="#eco:protocolReferences">protocolReferences</a>
        <a class="btn btn-sm btn-outline-secondary m-1" href="#eco:isAbundanceReported">isAbundanceReported</a>
        <a class="btn btn-sm btn-outline-secondary m-1" href="#eco:isAbundanceCapReported">isAbundanceCapReported</a>
        <a class="btn btn-sm btn-outline-secondary m-1" href="#eco:abundanceCap">abundanceCap</a>
        <a class="btn btn-sm btn-outline-secondary m-1" href="#eco:isVegetationCoverReported">isVegetationCoverReported</a>
        <a class="btn btn-sm btn-outline-secondary m-1" href="#eco:isLeastSpecificTargetCategoryQuantityInclusive">isLeastSpecificTargetCategoryQuantityInclusive</a>
    </div>


<p class="invisible">
    <a id="eco:compilationTypes"></a><a id="compilationTypes"></a></p>
<table class="table table-sm table-bordered">
    <tbody>
        <tr class="table-secondary"><th colspan="2">compilationTypes <span class="badge badge-secondary float-right">Property</span></th></tr>
        <tr><td class="theme-label">Identifier</td><td><a href="http://rs.tdwg.org/eco/terms/compilationTypes">http://rs.tdwg.org/eco/terms/compilationTypes</a></td></tr>
        <tr><td class="theme-label">Definition</td><td>A statement specifying whether data reported are derived from sampling events, ancillary data compiled from other sources, or a combination of both.</td></tr>
        <tr><td class="theme-label">Comments</td><td>This term is only relevant if the dwc:Event is an inventory. Recommended best practice is to use a controlled vocabulary. Recommended best practice is to separate the values in a list with space vertical bar space (<code> | </code>).</td></tr>
        <tr><td class="theme-label">Examples</td><td><ul class="list-group list-group-flush"><li class="list-group-item"><code>samplingEvents</code></li><li class="list-group-item"><code>compilationOfExistingSourcesAndSamplingEvents</code></li><li class="list-group-item"><code>compilationOfExistingSources</code></li><li class="list-group-item"><code>compilationOfExistingSourcesAndSamplingEvents | compilationOfExistingSources</code></li></ul></td></tr>
    </tbody>
</table>
<p class="invisible">
    <a id="eco:compilationSourceTypes"></a><a id="compilationSourceTypes"></a></p>
<table class="table table-sm table-bordered">
    <tbody>
        <tr class="table-secondary"><th colspan="2">compilationSourceTypes <span class="badge badge-secondary float-right">Property</span></th></tr>
        <tr><td class="theme-label">Identifier</td><td><a href="http://rs.tdwg.org/eco/terms/compilationSourceTypes">http://rs.tdwg.org/eco/terms/compilationSourceTypes</a></td></tr>
        <tr><td class="theme-label">Definition</td><td>The types of data sources contributing to the compilation reported.</td></tr>
        <tr><td class="theme-label">Comments</td><td>This term is only relevant if the dwc:Event is a compilation in which one or more types of data sources were used. Recommended best practice is to use a controlled vocabulary and separate multiple values in a list with space vertical bar space ( | ).</td></tr>
        <tr><td class="theme-label">Examples</td><td><ul class="list-group list-group-flush"><li class="list-group-item"><code>museumSpecimens</code></li><li class="list-group-item"><code>literature</code></li><li class="list-group-item"><code>expertKnowledge | localKnowledge</code></li></ul></td></tr>
    </tbody>
</table>
<p class="invisible">
    <a id="eco:inventoryTypes"></a><a id="inventoryTypes"></a></p>
<table class="table table-sm table-bordered">
    <tbody>
        <tr class="table-secondary"><th colspan="2">inventoryTypes <span class="badge badge-secondary float-right">Property</span></th></tr>
        <tr><td class="theme-label">Identifier</td><td><a href="http://rs.tdwg.org/eco/terms/inventoryTypes">http://rs.tdwg.org/eco/terms/inventoryTypes</a></td></tr>
        <tr><td class="theme-label">Definition</td><td>The types of search processes used to conduct the inventory.</td></tr>
        <tr><td class="theme-label">Comments</td><td>This term is only relevant if the dwc:Event represents an inventory. Recommended best practice is to use a controlled vocabulary. Recommended best practice is to separate multiple values in a list with space vertical bar space ( | ).</td></tr>
        <tr><td class="theme-label">Examples</td><td><ul class="list-group list-group-flush"><li class="list-group-item"><code>restrictedSearch</code></li><li class="list-group-item"><code>openSearch</code></li><li class="list-group-item"><code>opportunisticSearch</code></li><li class="list-group-item"><code>adventitious</code></li><li class="list-group-item"><code>compilation</code></li><li class="list-group-item"><code>openSearch | opportunisticSearch</code></li></ul></td></tr>
    </tbody>
</table>
<p class="invisible">
    <a id="eco:protocolNames"></a><a id="protocolNames"></a></p>
<table class="table table-sm table-bordered">
    <tbody>
        <tr class="table-secondary"><th colspan="2">protocolNames <span class="badge badge-secondary float-right">Property</span></th></tr>
        <tr><td class="theme-label">Identifier</td><td><a href="http://rs.tdwg.org/eco/terms/protocolNames">http://rs.tdwg.org/eco/terms/protocolNames</a></td></tr>
        <tr><td class="theme-label">Definition</td><td>Categorical descriptive names for the methods used during the dwc:Event.</td></tr>
        <tr><td class="theme-label">Comments</td><td>Recommended best practice is to use a controlled vocabulary and separate multiple values in a list with space vertical bar space ( | ).</td></tr>
        <tr><td class="theme-label">Examples</td><td><ul class="list-group list-group-flush"><li class="list-group-item"><code>boxTrapping</code></li><li class="list-group-item"><code>floraInventory</code></li><li class="list-group-item"><code>boxTrapping | funnelTrapping</code></li></ul></td></tr>
    </tbody>
</table>
<p class="invisible">
    <a id="eco:protocolDescriptions"></a><a id="protocolDescriptions"></a></p>
<table class="table table-sm table-bordered">
    <tbody>
        <tr class="table-secondary"><th colspan="2">protocolDescriptions <span class="badge badge-secondary float-right">Property</span></th></tr>
        <tr><td class="theme-label">Identifier</td><td><a href="http://rs.tdwg.org/eco/terms/protocolDescriptions">http://rs.tdwg.org/eco/terms/protocolDescriptions</a></td></tr>
        <tr><td class="theme-label">Definition</td><td>A detailed description of the methods used during the dwc:Event.</td></tr>
        <tr><td class="theme-label">Comments</td><td>This description should be associated with protocols provided in eco:protocolNames. The description may include deviations from a protocol referred to in eco:protocolReferences. Recommended good practice is to provide information about instruments used, calibration, etc. Recommended best practice is to separate multiple values in a list with space vertical bar space ( | ).</td></tr>
        <tr><td class="theme-label">Examples</td><td><code>Three conventional harp traps (3.2m ht x 2.2m w) were established in flight path zones for a period of 4 hrs at dawn and dusk for a total of 10 trap nights. Traps were visited on an hourly basis during each deployment period and the trap catch recorded for species, size, weight, sex, age and maternal status.</code></td></tr>
    </tbody>
</table>
<p class="invisible">
    <a id="eco:protocolReferences"></a><a id="protocolReferences"></a></p>
<table class="table table-sm table-bordered">
    <tbody>
        <tr class="table-secondary"><th colspan="2">protocolReferences <span class="badge badge-secondary float-right">Property</span></th></tr>
        <tr><td class="theme-label">Identifier</td><td><a href="http://rs.tdwg.org/eco/terms/protocolReferences">http://rs.tdwg.org/eco/terms/protocolReferences</a></td></tr>
        <tr><td class="theme-label">Definition</td><td>The references to the methods used during the dwc:Event.</td></tr>
        <tr><td class="theme-label">Comments</td><td>Recommended best practice is to separate multiple values in a list with space vertical bar space ( | ).</td></tr>
        <tr><td class="theme-label">Examples</td><td><code>Penguins from space: faecal stains reveal the location of emperor penguin colonies, <a href="https://doi.org/10.1111/j.1466-8238.2009.00467.x">https://doi.org/10.1111/j.1466-8238.2009.00467.x</a></code></td></tr>
    </tbody>
</table>
<p class="invisible">
    <a id="eco:isAbundanceReported"></a><a id="isAbundanceReported"></a></p>
<table class="table table-sm table-bordered">
    <tbody>
        <tr class="table-secondary"><th colspan="2">isAbundanceReported <span class="badge badge-secondary float-right">Property</span></th></tr>
        <tr><td class="theme-label">Identifier</td><td><a href="http://rs.tdwg.org/eco/terms/isAbundanceReported">http://rs.tdwg.org/eco/terms/isAbundanceReported</a></td></tr>
        <tr><td class="theme-label">Definition</td><td>The number of dwc:Organisms collected or observed was reported.</td></tr>
        <tr><td class="theme-label">Comments</td><td>Typically the abundance values would be reported in the dwc:organismQuantity and dwc:organismQuantityType terms for the child dwc:Occurrence records for this dwc:Event.</td></tr>
        <tr><td class="theme-label">Examples</td><td><ul class="list-group list-group-flush"><li class="list-group-item"><code>true</code></li><li class="list-group-item"><code>false</code></li></ul></td></tr>
    </tbody>
</table>
<p class="invisible">
    <a id="eco:isAbundanceCapReported"></a><a id="isAbundanceCapReported"></a></p>
<table class="table table-sm table-bordered">
    <tbody>
        <tr class="table-secondary"><th colspan="2">isAbundanceCapReported <span class="badge badge-secondary float-right">Property</span></th></tr>
        <tr><td class="theme-label">Identifier</td><td><a href="http://rs.tdwg.org/eco/terms/isAbundanceCapReported">http://rs.tdwg.org/eco/terms/isAbundanceCapReported</a></td></tr>
        <tr><td class="theme-label">Definition</td><td>A maximum number of dwc:Organisms was reported, as specified or restricted by the protocol used.</td></tr>
        <tr><td class="theme-label">Comments</td><td>Values of abundance cap should be captured under the term eco:abundanceCap.</td></tr>
        <tr><td class="theme-label">Examples</td><td><ul class="list-group list-group-flush"><li class="list-group-item"><code>true</code></li><li class="list-group-item"><code>false</code></li></ul></td></tr>
    </tbody>
</table>
<p class="invisible">
    <a id="eco:abundanceCap"></a><a id="abundanceCap"></a></p>
<table class="table table-sm table-bordered">
    <tbody>
        <tr class="table-secondary"><th colspan="2">abundanceCap <span class="badge badge-secondary float-right">Property</span></th></tr>
        <tr><td class="theme-label">Identifier</td><td><a href="http://rs.tdwg.org/eco/terms/abundanceCap">http://rs.tdwg.org/eco/terms/abundanceCap</a></td></tr>
        <tr><td class="theme-label">Definition</td><td>The reported maximum number of dwc:Organisms.</td></tr>
        <tr><td class="theme-label">Comments</td><td></td></tr>
        <tr><td class="theme-label">Examples</td><td><ul class="list-group list-group-flush"><li class="list-group-item"><code>300</code></li><li class="list-group-item"><code>700</code></li></ul></td></tr>
    </tbody>
</table>
<p class="invisible">
    <a id="eco:isVegetationCoverReported"></a><a id="isVegetationCoverReported"></a></p>
<table class="table table-sm table-bordered">
    <tbody>
        <tr class="table-secondary"><th colspan="2">isVegetationCoverReported <span class="badge badge-secondary float-right">Property</span></th></tr>
        <tr><td class="theme-label">Identifier</td><td><a href="http://rs.tdwg.org/eco/terms/isVegetationCoverReported">http://rs.tdwg.org/eco/terms/isVegetationCoverReported</a></td></tr>
        <tr><td class="theme-label">Definition</td><td>A vegetation cover metric was reported.</td></tr>
        <tr><td class="theme-label">Comments</td><td>Typically values or descriptions of vegetation cover would be captured under the term eco:verbatimSiteDescriptions.</td></tr>
        <tr><td class="theme-label">Examples</td><td><ul class="list-group list-group-flush"><li class="list-group-item"><code>true</code></li><li class="list-group-item"><code>false</code></li></ul></td></tr>
    </tbody>
</table>
<p class="invisible">
    <a id="eco:isLeastSpecificTargetCategoryQuantityInclusive"></a><a id="isLeastSpecificTargetCategoryQuantityInclusive"></a></p>
<table class="table table-sm table-bordered">
    <tbody>
        <tr class="table-secondary"><th colspan="2">isLeastSpecificTargetCategoryQuantityInclusive <span class="badge badge-secondary float-right">Property</span></th></tr>
        <tr><td class="theme-label">Identifier</td><td><a href="http://rs.tdwg.org/eco/terms/isLeastSpecificTargetCategoryQuantityInclusive">http://rs.tdwg.org/eco/terms/isLeastSpecificTargetCategoryQuantityInclusive</a></td></tr>
        <tr><td class="theme-label">Definition</td><td>The total detected quantity for a dwc:Taxon (including subcategories thereof) in a dwc:Event is given explicitly in a single record (dwc:organismQuantity value) for that dwc:Taxon.</td></tr>
        <tr><td class="theme-label">Comments</td><td>Recommended values are 'true' and 'false'. This term is only relevant if dwc:organismQuantity is a number. For a detailed explanation, see <a href="http://rs.tdwg.org/eco/docs/inclusive/">http://rs.tdwg.org/eco/docs/inclusive/</a>.</td></tr>
        <tr><td class="theme-label">Examples</td><td><ul class="list-group list-group-flush"><li class="list-group-item"><code>true</code></li><li class="list-group-item"><code>false</code></li></ul></td></tr>
    </tbody>
</table>


## Material Collected

<div class="my-4">
        <a class="btn btn-sm btn-outline-secondary m-1" href="#eco:hasVouchers">hasVouchers</a>
        <a class="btn btn-sm btn-outline-secondary m-1" href="#eco:voucherInstitutions">voucherInstitutions</a>
        <a class="btn btn-sm btn-outline-secondary m-1" href="#eco:hasMaterialSamples">hasMaterialSamples</a>
        <a class="btn btn-sm btn-outline-secondary m-1" href="#eco:materialSampleTypes">materialSampleTypes</a>
    </div>


<p class="invisible">
    <a id="eco:hasVouchers"></a><a id="hasVouchers"></a></p>
<table class="table table-sm table-bordered">
    <tbody>
        <tr class="table-secondary"><th colspan="2">hasVouchers <span class="badge badge-secondary float-right">Property</span></th></tr>
        <tr><td class="theme-label">Identifier</td><td><a href="http://rs.tdwg.org/eco/terms/hasVouchers">http://rs.tdwg.org/eco/terms/hasVouchers</a></td></tr>
        <tr><td class="theme-label">Definition</td><td>Specimen vouchers were collected during the dwc:Event.</td></tr>
        <tr><td class="theme-label">Comments</td><td></td></tr>
        <tr><td class="theme-label">Examples</td><td><ul class="list-group list-group-flush"><li class="list-group-item"><code>true</code></li><li class="list-group-item"><code>false</code></li></ul></td></tr>
    </tbody>
</table>
<p class="invisible">
    <a id="eco:voucherInstitutions"></a><a id="voucherInstitutions"></a></p>
<table class="table table-sm table-bordered">
    <tbody>
        <tr class="table-secondary"><th colspan="2">voucherInstitutions <span class="badge badge-secondary float-right">Property</span></th></tr>
        <tr><td class="theme-label">Identifier</td><td><a href="http://rs.tdwg.org/eco/terms/voucherInstitutions">http://rs.tdwg.org/eco/terms/voucherInstitutions</a></td></tr>
        <tr><td class="theme-label">Definition</td><td>A list (concatenated and separated) of the names or acronyms of the institutions where vouchers collected during the dwc:Event were deposited.</td></tr>
        <tr><td class="theme-label">Comments</td><td>Recommended best practice is to separate multiple values in a list with space vertical bar space ( | ).</td></tr>
        <tr><td class="theme-label">Examples</td><td><ul class="list-group list-group-flush"><li class="list-group-item"><code>FMNH</code></li><li class="list-group-item"><code>AMNH | MVZ</code></li><li class="list-group-item"><code>Nairobi National Museum</code></li></ul></td></tr>
    </tbody>
</table>
<p class="invisible">
    <a id="eco:hasMaterialSamples"></a><a id="hasMaterialSamples"></a></p>
<table class="table table-sm table-bordered">
    <tbody>
        <tr class="table-secondary"><th colspan="2">hasMaterialSamples <span class="badge badge-secondary float-right">Property</span></th></tr>
        <tr><td class="theme-label">Identifier</td><td><a href="http://rs.tdwg.org/eco/terms/hasMaterialSamples">http://rs.tdwg.org/eco/terms/hasMaterialSamples</a></td></tr>
        <tr><td class="theme-label">Definition</td><td>Material samples were collected during the dwc:Event.</td></tr>
        <tr><td class="theme-label">Comments</td><td></td></tr>
        <tr><td class="theme-label">Examples</td><td><ul class="list-group list-group-flush"><li class="list-group-item"><code>true</code></li><li class="list-group-item"><code>false</code></li></ul></td></tr>
    </tbody>
</table>
<p class="invisible">
    <a id="eco:materialSampleTypes"></a><a id="materialSampleTypes"></a></p>
<table class="table table-sm table-bordered">
    <tbody>
        <tr class="table-secondary"><th colspan="2">materialSampleTypes <span class="badge badge-secondary float-right">Property</span></th></tr>
        <tr><td class="theme-label">Identifier</td><td><a href="http://rs.tdwg.org/eco/terms/materialSampleTypes">http://rs.tdwg.org/eco/terms/materialSampleTypes</a></td></tr>
        <tr><td class="theme-label">Definition</td><td>A list (concatenated and separated) of material sample types collected during the dwc:Event.</td></tr>
        <tr><td class="theme-label">Comments</td><td>Recommended best practice is to use a controlled vocabulary and separate multiple values in a list with space vertical bar space ( | ).</td></tr>
        <tr><td class="theme-label">Examples</td><td><ul class="list-group list-group-flush"><li class="list-group-item"><code>wholeOrganism</code></li><li class="list-group-item"><code>skeleton</code></li><li class="list-group-item"><code>tissue | blood | fecal | stomachContent</code></li></ul></td></tr>
    </tbody>
</table>


## Sampling Effort

<div class="my-4">
        <a class="btn btn-sm btn-outline-secondary m-1" href="#eco:samplingPerformedBy">samplingPerformedBy</a>
        <a class="btn btn-sm btn-outline-secondary m-1" href="#eco:isSamplingEffortReported">isSamplingEffortReported</a>
        <a class="btn btn-sm btn-outline-secondary m-1" href="#eco:samplingEffortProtocol">samplingEffortProtocol</a>
        <a class="btn btn-sm btn-outline-secondary m-1" href="#eco:samplingEffortValue">samplingEffortValue</a>
        <a class="btn btn-sm btn-outline-secondary m-1" href="#eco:samplingEffortUnit">samplingEffortUnit</a>
    </div>


<p class="invisible">
    <a id="eco:samplingPerformedBy"></a><a id="samplingPerformedBy"></a></p>
<table class="table table-sm table-bordered">
    <tbody>
        <tr class="table-secondary"><th colspan="2">samplingPerformedBy <span class="badge badge-secondary float-right">Property</span></th></tr>
        <tr><td class="theme-label">Identifier</td><td><a href="http://rs.tdwg.org/eco/terms/samplingPerformedBy">http://rs.tdwg.org/eco/terms/samplingPerformedBy</a></td></tr>
        <tr><td class="theme-label">Definition</td><td>A person, group, or organization responsible for recording the dwc:Event.</td></tr>
        <tr><td class="theme-label">Comments</td><td>The sampling dwc:Event could be at any level of hierarchy. In the case of a higher level (parent) dwc:Event, include all the organizations or people involved in the child dwc:Events that contributed to the parent dwc:Event. Recommended best practice is to separate multiple values in a list with space vertical bar space ( | ).</td></tr>
        <tr><td class="theme-label">Examples</td><td><ul class="list-group list-group-flush"><li class="list-group-item"><code>North American Butterlfy Association</code></li><li class="list-group-item"><code>KK Wall</code></li><li class="list-group-item"><code>JJ Green</code></li><li class="list-group-item"><code>LL Pink and FF Grey | Aspen Center for Environmental Studies</code></li></ul></td></tr>
    </tbody>
</table>
<p class="invisible">
    <a id="eco:isSamplingEffortReported"></a><a id="isSamplingEffortReported"></a></p>
<table class="table table-sm table-bordered">
    <tbody>
        <tr class="table-secondary"><th colspan="2">isSamplingEffortReported <span class="badge badge-secondary float-right">Property</span></th></tr>
        <tr><td class="theme-label">Identifier</td><td><a href="http://rs.tdwg.org/eco/terms/isSamplingEffortReported">http://rs.tdwg.org/eco/terms/isSamplingEffortReported</a></td></tr>
        <tr><td class="theme-label">Definition</td><td>The sampling effort associated with the dwc:Event was reported.</td></tr>
        <tr><td class="theme-label">Comments</td><td>Typically values of effort would be captured under the terms eco:samplingEffortValue and eco:samplingEffortUnit.</td></tr>
        <tr><td class="theme-label">Examples</td><td><ul class="list-group list-group-flush"><li class="list-group-item"><code>true</code></li><li class="list-group-item"><code>false</code></li></ul></td></tr>
    </tbody>
</table>
<p class="invisible">
    <a id="eco:samplingEffortProtocol"></a><a id="samplingEffortProtocol"></a></p>
<table class="table table-sm table-bordered">
    <tbody>
        <tr class="table-secondary"><th colspan="2">samplingEffortProtocol <span class="badge badge-secondary float-right">Property</span></th></tr>
        <tr><td class="theme-label">Identifier</td><td><a href="http://rs.tdwg.org/eco/terms/samplingEffortProtocol">http://rs.tdwg.org/eco/terms/samplingEffortProtocol</a></td></tr>
        <tr><td class="theme-label">Definition</td><td>A description of or reference (publication or URL) to the methods used to determine the sampling effort.</td></tr>
        <tr><td class="theme-label">Comments</td><td>This description should be associated with the values reported in eco:samplingEffortValue and eco:samplingEffortUnit. This is a specialization of eco:protocolDescription focused on effort, distinct from the survey method. The effort relates to the intensity of sampling and therefore can assist in interpreting estimates of completeness.</td></tr>
        <tr><td class="theme-label">Examples</td><td><ul class="list-group list-group-flush"><li class="list-group-item"><code>40 box traps deployed at even spacings along 4 parallel 100m transects placed 50m apart and visited at 6 hourly intervals over a 48 hour period</code></li><li class="list-group-item"><code>2 people occupying a bird hide for a period of 8 hours and undertaking a 30 minute count of species within the 150 degree field of view every 2 hours</code></li><li class="list-group-item"><code>A single baited camera trap station with motion sensor trigger, deployed for a period of 10 days and configured for detecting large fauna moving through a known traffic way</code></li></ul></td></tr>
    </tbody>
</table>
<p class="invisible">
    <a id="eco:samplingEffortValue"></a><a id="samplingEffortValue"></a></p>
<table class="table table-sm table-bordered">
    <tbody>
        <tr class="table-secondary"><th colspan="2">samplingEffortValue <span class="badge badge-secondary float-right">Property</span></th></tr>
        <tr><td class="theme-label">Identifier</td><td><a href="http://rs.tdwg.org/eco/terms/samplingEffortValue">http://rs.tdwg.org/eco/terms/samplingEffortValue</a></td></tr>
        <tr><td class="theme-label">Definition</td><td>The numeric value for the sampling effort expended during the dwc:Event.</td></tr>
        <tr><td class="theme-label">Comments</td><td>This term is meant to capture the total sampling effort value. To express details of how the effort was determined use eco:samplingEffortProtocol. For compilations it is recommend not to infer effort. An eco:samplingEffortValue must have a corresponding eco:samplingEffortUnit.</td></tr>
        <tr><td class="theme-label">Examples</td><td><ul class="list-group list-group-flush"><li class="list-group-item"><code>1900</code></li><li class="list-group-item"><code>40</code></li><li class="list-group-item"><code>5.5</code></li></ul></td></tr>
    </tbody>
</table>
<p class="invisible">
    <a id="eco:samplingEffortUnit"></a><a id="samplingEffortUnit"></a></p>
<table class="table table-sm table-bordered">
    <tbody>
        <tr class="table-secondary"><th colspan="2">samplingEffortUnit <span class="badge badge-secondary float-right">Property</span></th></tr>
        <tr><td class="theme-label">Identifier</td><td><a href="http://rs.tdwg.org/eco/terms/samplingEffortUnit">http://rs.tdwg.org/eco/terms/samplingEffortUnit</a></td></tr>
        <tr><td class="theme-label">Definition</td><td>The units associated with the eco:samplingEffortValue.</td></tr>
        <tr><td class="theme-label">Comments</td><td>Recommended best practice is to use a controlled vocabulary.</td></tr>
        <tr><td class="theme-label">Examples</td><td><ul class="list-group list-group-flush"><li class="list-group-item"><code>trapHours</code></li><li class="list-group-item"><code>personHours</code></li><li class="list-group-item"><code>trapDays</code></li></ul></td></tr>
    </tbody>
</table>

