---
container: fluid
---

# Humboldt Core Extension quick reference guide

This document is intended to be an easy-to-read reference the currently recommended terms that extend the [Darwin Core standard](https://www.tdwg.org/standards/dwc/) with vocabulary to describe biological inventories. This document is not part of the standard. It draws on the [term names and definitions](../list/) from the normative part of the standard and combines them with comments and examples that are not normative, but that are meant to help people to use the terms consistently. Comprehensive metadata for current and obsolete terms in human readable form are found in a [list of terms document](../list/). CSV files with the [full history](https://github.com/tdwg/chrono/blob/master/vocabulary/term_versions.csv) of the terms, with [horizontal and vertical lists](https://github.com/tdwg/chrono/tree/master/dist) of these terms and the schema for the [Darwin Core Archive extension](https://github.com/tdwg/chrono/tree/master/dist) can be found in the [Humboldt Core repository](https://github.com/tdwg/hc).


## Event

<div class="my-4">
        <a class="btn btn-sm btn-outline-secondary m-1" href="#hc:samplingPerformedBy">samplingPerformedBy</a>
        <a class="btn btn-sm btn-outline-secondary m-1" href="#hc:siteCount">siteCount</a>
        <a class="btn btn-sm btn-outline-secondary m-1" href="#hc:siteNestingDescription">siteNestingDescription</a>
        <a class="btn btn-sm btn-outline-secondary m-1" href="#hc:verbatimSiteNames">verbatimSiteNames</a>
        <a class="btn btn-sm btn-outline-secondary m-1" href="#hc:verbatimSiteDescriptions">verbatimSiteDescriptions</a>
        <a class="btn btn-sm btn-outline-secondary m-1" href="#hc:geospatialScopeAreaInSquareKilometers">geospatialScopeAreaInSquareKilometers</a>
        <a class="btn btn-sm btn-outline-secondary m-1" href="#hc:totalAreaSampledInSquareKilometers">totalAreaSampledInSquareKilometers</a>
        <a class="btn btn-sm btn-outline-secondary m-1" href="#hc:eventDuration">eventDuration</a>
        <a class="btn btn-sm btn-outline-secondary m-1" href="#hc:eventDurationUnit">eventDurationUnit</a>
        <a class="btn btn-sm btn-outline-secondary m-1" href="#hc:targetTaxonomicScope">targetTaxonomicScope</a>
        <a class="btn btn-sm btn-outline-secondary m-1" href="#hc:excludedTaxonomicScope">excludedTaxonomicScope</a>
        <a class="btn btn-sm btn-outline-secondary m-1" href="#hc:targetLifestageScope">targetLifestageScope</a>
        <a class="btn btn-sm btn-outline-secondary m-1" href="#hc:excludedLifeStageScope">excludedLifeStageScope</a>
        <a class="btn btn-sm btn-outline-secondary m-1" href="#hc:targetDegreeOfEstablishmentScope">targetDegreeOfEstablishmentScope</a>
        <a class="btn btn-sm btn-outline-secondary m-1" href="#hc:excludedDegreeOfEstablishmentScope">excludedDegreeOfEstablishmentScope</a>
        <a class="btn btn-sm btn-outline-secondary m-1" href="#hc:targetGrowthFormScope">targetGrowthFormScope</a>
        <a class="btn btn-sm btn-outline-secondary m-1" href="#hc:excludedGrowthFormScope">excludedGrowthFormScope</a>
        <a class="btn btn-sm btn-outline-secondary m-1" href="#hc:habitatScope">habitatScope</a>
        <a class="btn btn-sm btn-outline-secondary m-1" href="#hc:excludedHabitatScope">excludedHabitatScope</a>
        <a class="btn btn-sm btn-outline-secondary m-1" href="#hc:reportedWeather">reportedWeather</a>
        <a class="btn btn-sm btn-outline-secondary m-1" href="#hc:reportedExtremeConditions">reportedExtremeConditions</a>
        <a class="btn btn-sm btn-outline-secondary m-1" href="#hc:inventoryTypes">inventoryTypes</a>
        <a class="btn btn-sm btn-outline-secondary m-1" href="#hc:compilationType">compilationType</a>
        <a class="btn btn-sm btn-outline-secondary m-1" href="#hc:compilationSourceTypes">compilationSourceTypes</a>
        <a class="btn btn-sm btn-outline-secondary m-1" href="#hc:protocolNames">protocolNames</a>
        <a class="btn btn-sm btn-outline-secondary m-1" href="#hc:protocolDescription">protocolDescription</a>
        <a class="btn btn-sm btn-outline-secondary m-1" href="#hc:protocolReferences">protocolReferences</a>
        <a class="btn btn-sm btn-outline-secondary m-1" href="#hc:isAbundanceReported">isAbundanceReported</a>
        <a class="btn btn-sm btn-outline-secondary m-1" href="#hc:isAbundanceCapReported">isAbundanceCapReported</a>
        <a class="btn btn-sm btn-outline-secondary m-1" href="#hc:abundanceCap">abundanceCap</a>
        <a class="btn btn-sm btn-outline-secondary m-1" href="#hc:isVegetationCoverReported">isVegetationCoverReported</a>
        <a class="btn btn-sm btn-outline-secondary m-1" href="#hc:isAbsenceReported">isAbsenceReported</a>
        <a class="btn btn-sm btn-outline-secondary m-1" href="#hc:absentTaxa">absentTaxa</a>
        <a class="btn btn-sm btn-outline-secondary m-1" href="#hc:hasVouchers">hasVouchers</a>
        <a class="btn btn-sm btn-outline-secondary m-1" href="#hc:voucherInstitutions">voucherInstitutions</a>
        <a class="btn btn-sm btn-outline-secondary m-1" href="#hc:hasMaterialSamples">hasMaterialSamples</a>
        <a class="btn btn-sm btn-outline-secondary m-1" href="#hc:materialSampleTypes">materialSampleTypes</a>
        <a class="btn btn-sm btn-outline-secondary m-1" href="#hc:isSamplingEffortReported">isSamplingEffortReported</a>
        <a class="btn btn-sm btn-outline-secondary m-1" href="#hc:samplingEffortProtocol">samplingEffortProtocol</a>
        <a class="btn btn-sm btn-outline-secondary m-1" href="#hc:samplingEffortValue">samplingEffortValue</a>
        <a class="btn btn-sm btn-outline-secondary m-1" href="#hc:samplingEffortUnit">samplingEffortUnit</a>
        <a class="btn btn-sm btn-outline-secondary m-1" href="#hc:taxonCompletenessReported">taxonCompletenessReported</a>
        <a class="btn btn-sm btn-outline-secondary m-1" href="#hc:taxonCompletenessProtocols">taxonCompletenessProtocols</a>
    </div>

<table class="table table-sm table-bordered">
    <tbody>
        <tr class="table-primary"><th colspan="2">Event <span class="badge badge-primary float-right">Class</span></th></tr>
        <tr><td class="theme-label">Identifier</td><td><a href="http://rs.tdwg.org/dwc/terms/Event">http://rs.tdwg.org/dwc/terms/Event</a></td></tr>
        <tr><td class="theme-label">Definition</td><td>An action that occurs at some location during some time.</td></tr>
        <tr><td class="theme-label">Comments</td><td></td></tr>
        <tr><td class="theme-label">Examples</td><td>A specimen collection process. A camera trap image capture.  A marine trawl.</td></tr>
    </tbody>
</table>

<p class="invisible">
    <a id="hc:samplingPerformedBy"></a><a id="samplingPerformedBy"></a></p>
<table class="table table-sm table-bordered">
    <tbody>
        <tr class="table-secondary"><th colspan="2">samplingPerformedBy <span class="badge badge-secondary float-right">Property</span></th></tr>
        <tr><td class="theme-label">Identifier</td><td><a href="http://rs.tdwg.org/hc/terms/samplingPerformedBy">http://rs.tdwg.org/hc/terms/samplingPerformedBy</a></td></tr>
        <tr><td class="theme-label">Definition</td><td>A person, group, or organization responsible for recording the Event.</td></tr>
        <tr><td class="theme-label">Comments</td><td>The sampling Event could be at any level of hierarchy. In the case of a higher level Event (parent), include all the organizations or people involved in the child Events that contributed to the parent Event. Recommended best practice is to separate multiple values in a list with space vertical bar space ( | ).</td></tr>
        <tr><td class="theme-label">Examples</td><td><code>North American Butterlfy Association</code>, <code>KK Wall</code>, <code>JJ Green</code>, <code>LL Pink and FF Grey | Aspen Center for Environmental Studies</code></td></tr>
    </tbody>
</table>
<p class="invisible">
    <a id="hc:siteCount"></a><a id="siteCount"></a></p>
<table class="table table-sm table-bordered">
    <tbody>
        <tr class="table-secondary"><th colspan="2">siteCount <span class="badge badge-secondary float-right">Property</span></th></tr>
        <tr><td class="theme-label">Identifier</td><td><a href="http://rs.tdwg.org/hc/terms/siteCount">http://rs.tdwg.org/hc/terms/siteCount</a></td></tr>
        <tr><td class="theme-label">Definition</td><td>Total number of individual sites surveyed during the Event.</td></tr>
        <tr><td class="theme-label">Comments</td><td>Site refers to the location at which observations are made or samples/measurements are taken. The site could be at any level of hierarchy.</td></tr>
        <tr><td class="theme-label">Examples</td><td><code>1</code>, <code>15</code></td></tr>
    </tbody>
</table>
<p class="invisible">
    <a id="hc:siteNestingDescription"></a><a id="siteNestingDescription"></a></p>
<table class="table table-sm table-bordered">
    <tbody>
        <tr class="table-secondary"><th colspan="2">siteNestingDescription <span class="badge badge-secondary float-right">Property</span></th></tr>
        <tr><td class="theme-label">Identifier</td><td><a href="http://rs.tdwg.org/hc/terms/siteNestingDescription">http://rs.tdwg.org/hc/terms/siteNestingDescription</a></td></tr>
        <tr><td class="theme-label">Definition</td><td>Textual description of the hierarchical sampling design.</td></tr>
        <tr><td class="theme-label">Comments</td><td>Site refers to the location at which observations are made or samples/measurements are taken. The site could be at any level of hierarchy.</td></tr>
        <tr><td class="theme-label">Examples</td><td><code>5 sampling sites of 3-5 plots each</code></td></tr>
    </tbody>
</table>
<p class="invisible">
    <a id="hc:verbatimSiteNames"></a><a id="verbatimSiteNames"></a></p>
<table class="table table-sm table-bordered">
    <tbody>
        <tr class="table-secondary"><th colspan="2">verbatimSiteNames <span class="badge badge-secondary float-right">Property</span></th></tr>
        <tr><td class="theme-label">Identifier</td><td><a href="http://rs.tdwg.org/hc/terms/verbatimSiteNames">http://rs.tdwg.org/hc/terms/verbatimSiteNames</a></td></tr>
        <tr><td class="theme-label">Definition</td><td>A list (concatenated and separated) of original site names.</td></tr>
        <tr><td class="theme-label">Comments</td><td>Site refers to the location at which observations are made or samples/measurements are taken. The site could be at any level of hierarchy. Recommended best practice is to separate multiple values in a list with space vertical bar space ( | ).</td></tr>
        <tr><td class="theme-label">Examples</td><td><code>East Coastal Fringe | St. Marks Wildlife Management Area</code>, <code>S1 | S2 | C1 | C2 | R14 | R22 | W1</code></td></tr>
    </tbody>
</table>
<p class="invisible">
    <a id="hc:verbatimSiteDescriptions"></a><a id="verbatimSiteDescriptions"></a></p>
<table class="table table-sm table-bordered">
    <tbody>
        <tr class="table-secondary"><th colspan="2">verbatimSiteDescriptions <span class="badge badge-secondary float-right">Property</span></th></tr>
        <tr><td class="theme-label">Identifier</td><td><a href="http://rs.tdwg.org/hc/terms/verbatimSiteDescriptions">http://rs.tdwg.org/hc/terms/verbatimSiteDescriptions</a></td></tr>
        <tr><td class="theme-label">Definition</td><td>Original textual description of the site(s).</td></tr>
        <tr><td class="theme-label">Comments</td><td>Site refers to the location at which observations are made or samples/measurements are taken. The site could be at any level of hierarchy. Recommended best practice is to separate multiple values in a list with space vertical bar space ( | ).</td></tr>
        <tr><td class="theme-label">Examples</td><td><code>Wet flatwoods | Wet depression surrounded by mesic longleaf pine flatwoods | Ground cover of thick Andropogon spp., Sporobolus floridanus, Vaccinium spp, Rhynchospora spp., Centella erecta, Panicum rigidulum.</code></td></tr>
    </tbody>
</table>
<p class="invisible">
    <a id="hc:geospatialScopeAreaInSquareKilometers"></a><a id="geospatialScopeAreaInSquareKilometers"></a></p>
<table class="table table-sm table-bordered">
    <tbody>
        <tr class="table-secondary"><th colspan="2">geospatialScopeAreaInSquareKilometers <span class="badge badge-secondary float-right">Property</span></th></tr>
        <tr><td class="theme-label">Identifier</td><td><a href="http://rs.tdwg.org/hc/terms/geospatialScopeAreaInSquareKilometers">http://rs.tdwg.org/hc/terms/geospatialScopeAreaInSquareKilometers</a></td></tr>
        <tr><td class="theme-label">Definition</td><td>Total area in km2 of the geospatial scope of the Event.</td></tr>
        <tr><td class="theme-label">Comments</td><td>Geospatial scope refers to the Event location reported using the dwc:Location class terms. This area is always greater than or equal to totalAreaSampledInSquareKilometers.</td></tr>
        <tr><td class="theme-label">Examples</td><td><code>25</code></td></tr>
    </tbody>
</table>
<p class="invisible">
    <a id="hc:totalAreaSampledInSquareKilometers"></a><a id="totalAreaSampledInSquareKilometers"></a></p>
<table class="table table-sm table-bordered">
    <tbody>
        <tr class="table-secondary"><th colspan="2">totalAreaSampledInSquareKilometers <span class="badge badge-secondary float-right">Property</span></th></tr>
        <tr><td class="theme-label">Identifier</td><td><a href="http://rs.tdwg.org/hc/terms/totalAreaSampledInSquareKilometers">http://rs.tdwg.org/hc/terms/totalAreaSampledInSquareKilometers</a></td></tr>
        <tr><td class="theme-label">Definition</td><td>Total area in km2 surveyed during the Event.</td></tr>
        <tr><td class="theme-label">Comments</td><td>This area is always less than or equal to geospatialScopeAreaInSquareKilometers.</td></tr>
        <tr><td class="theme-label">Examples</td><td><code>0.8</code></td></tr>
    </tbody>
</table>
<p class="invisible">
    <a id="hc:eventDuration"></a><a id="eventDuration"></a></p>
<table class="table table-sm table-bordered">
    <tbody>
        <tr class="table-secondary"><th colspan="2">eventDuration <span class="badge badge-secondary float-right">Property</span></th></tr>
        <tr><td class="theme-label">Identifier</td><td><a href="http://rs.tdwg.org/hc/terms/eventDuration">http://rs.tdwg.org/hc/terms/eventDuration</a></td></tr>
        <tr><td class="theme-label">Definition</td><td>The length of the Event in the unit reported in hc:eventDurationUnit.</td></tr>
        <tr><td class="theme-label">Comments</td><td>Recommended best practice is to use a controlled vocabulary. An hc:eventDuration should have a corresponding hc:eventDurationUnit.</td></tr>
        <tr><td class="theme-label">Examples</td><td><code>1</code>, <code>30</code></td></tr>
    </tbody>
</table>
<p class="invisible">
    <a id="hc:eventDurationUnit"></a><a id="eventDurationUnit"></a></p>
<table class="table table-sm table-bordered">
    <tbody>
        <tr class="table-secondary"><th colspan="2">eventDurationUnit <span class="badge badge-secondary float-right">Property</span></th></tr>
        <tr><td class="theme-label">Identifier</td><td><a href="http://rs.tdwg.org/hc/terms/eventDurationUnit">http://rs.tdwg.org/hc/terms/eventDurationUnit</a></td></tr>
        <tr><td class="theme-label">Definition</td><td>The temporal unit used to report hc:eventDuration.</td></tr>
        <tr><td class="theme-label">Comments</td><td>An hc:eventDurationUnit should have a corresponding hc:eventDuration.</td></tr>
        <tr><td class="theme-label">Examples</td><td><code>minutes</code>, <code>hours</code>, <code>days</code>, <code>months</code>, <code>years</code></td></tr>
    </tbody>
</table>
<p class="invisible">
    <a id="hc:targetTaxonomicScope"></a><a id="targetTaxonomicScope"></a></p>
<table class="table table-sm table-bordered">
    <tbody>
        <tr class="table-secondary"><th colspan="2">targetTaxonomicScope <span class="badge badge-secondary float-right">Property</span></th></tr>
        <tr><td class="theme-label">Identifier</td><td><a href="http://rs.tdwg.org/hc/terms/targetTaxonomicScope">http://rs.tdwg.org/hc/terms/targetTaxonomicScope</a></td></tr>
        <tr><td class="theme-label">Definition</td><td>Taxonomic group(s) targeted for sampling during the Event.</td></tr>
        <tr><td class="theme-label">Comments</td><td>The Event could be at any level of hierarchy. In the case of a higher level Event (parent), include all taxonomic groups surveyed in the child Events that contributed to the parent Event. Recommended best practice is to separate multiple values in a list with space vertical bar space ( | ).</td></tr>
        <tr><td class="theme-label">Examples</td><td><code>Aves</code>, <code>Aves | Mammalia</code>, <code>Procellariformes</code></td></tr>
    </tbody>
</table>
<p class="invisible">
    <a id="hc:excludedTaxonomicScope"></a><a id="excludedTaxonomicScope"></a></p>
<table class="table table-sm table-bordered">
    <tbody>
        <tr class="table-secondary"><th colspan="2">excludedTaxonomicScope <span class="badge badge-secondary float-right">Property</span></th></tr>
        <tr><td class="theme-label">Identifier</td><td><a href="http://rs.tdwg.org/hc/terms/excludedTaxonomicScope">http://rs.tdwg.org/hc/terms/excludedTaxonomicScope</a></td></tr>
        <tr><td class="theme-label">Definition</td><td>Taxonomic group(s) explicitly excluded from sampling during the Event.</td></tr>
        <tr><td class="theme-label">Comments</td><td>The Event could be at any level of hierarchy. In the case of a higher level Event (parent) include all the taxonomic groups explicitly excluded from the child Events that contributed to the parent Event. Recommended best practice is to separate multiple values in a list with space vertical bar space ( | ).</td></tr>
        <tr><td class="theme-label">Examples</td><td><code>nocturnal Aves</code>, <code>Quercus</code></td></tr>
    </tbody>
</table>
<p class="invisible">
    <a id="hc:targetLifestageScope"></a><a id="targetLifestageScope"></a></p>
<table class="table table-sm table-bordered">
    <tbody>
        <tr class="table-secondary"><th colspan="2">targetLifestageScope <span class="badge badge-secondary float-right">Property</span></th></tr>
        <tr><td class="theme-label">Identifier</td><td><a href="http://rs.tdwg.org/hc/terms/targetLifestageScope">http://rs.tdwg.org/hc/terms/targetLifestageScope</a></td></tr>
        <tr><td class="theme-label">Definition</td><td>The targeted age class(es) or life stage(s) of the Organism(s) sampled during the Event.</td></tr>
        <tr><td class="theme-label">Comments</td><td>This term i   s defined based on the definition of the Darwin Core term lifeStage (<a href="http://rs.tdwg.org/dwc/terms/lifeStage">http://rs.tdwg.org/dwc/terms/lifeStage</a>). Recommended best practice is to use a controlled vocabulary and separate multiple values in a list with space vertical bar space ( | ).</td></tr>
        <tr><td class="theme-label">Examples</td><td><code>larva</code>, <code>adult | juvenile</code></td></tr>
    </tbody>
</table>
<p class="invisible">
    <a id="hc:excludedLifeStageScope"></a><a id="excludedLifeStageScope"></a></p>
<table class="table table-sm table-bordered">
    <tbody>
        <tr class="table-secondary"><th colspan="2">excludedLifeStageScope <span class="badge badge-secondary float-right">Property</span></th></tr>
        <tr><td class="theme-label">Identifier</td><td><a href="http://rs.tdwg.org/hc/terms/excludedLifeStageScope">http://rs.tdwg.org/hc/terms/excludedLifeStageScope</a></td></tr>
        <tr><td class="theme-label">Definition</td><td>The explicitly excluded age class(es) or life stage(s) of the organism(s) sampled during the Event.</td></tr>
        <tr><td class="theme-label">Comments</td><td>This term is defined based on the definition of the Darwin Core term lifeStage (<a href="http://rs.tdwg.org/dwc/terms/lifeStage">http://rs.tdwg.org/dwc/terms/lifeStage</a>). Recommended best practice is to use a controlled vocabulary and to separate multiple values in a list with space vertical bar space ( | ).</td></tr>
        <tr><td class="theme-label">Examples</td><td><code>seedling</code>, <code>nestling | fledgling</code></td></tr>
    </tbody>
</table>
<p class="invisible">
    <a id="hc:targetDegreeOfEstablishmentScope"></a><a id="targetDegreeOfEstablishmentScope"></a></p>
<table class="table table-sm table-bordered">
    <tbody>
        <tr class="table-secondary"><th colspan="2">targetDegreeOfEstablishmentScope <span class="badge badge-secondary float-right">Property</span></th></tr>
        <tr><td class="theme-label">Identifier</td><td><a href="http://rs.tdwg.org/hc/terms/targetDegreeOfEstablishmentScope">http://rs.tdwg.org/hc/terms/targetDegreeOfEstablishmentScope</a></td></tr>
        <tr><td class="theme-label">Definition</td><td>Degree(s) of establishment targeted for sampling during the Event.</td></tr>
        <tr><td class="theme-label">Comments</td><td>Recommended best practice is to use controlled value strings from the controlled vocabulary (<a href="http://rs.tdwg.org/dwcdoe/">http://rs.tdwg.org/dwcdoe/</a>) for the Darwin Core term degreeOfEstablishment. For details, refer to <a href="https://doi.org/10.3897/biss.3.38084">https://doi.org/10.3897/biss.3.38084</a>. Recommended best practice is to separate multiple values in a list with space vertical bar space ( | ).</td></tr>
        <tr><td class="theme-label">Examples</td><td><code>native</code>, <code>invasive | widespreadInvasive</code></td></tr>
    </tbody>
</table>
<p class="invisible">
    <a id="hc:excludedDegreeOfEstablishmentScope"></a><a id="excludedDegreeOfEstablishmentScope"></a></p>
<table class="table table-sm table-bordered">
    <tbody>
        <tr class="table-secondary"><th colspan="2">excludedDegreeOfEstablishmentScope <span class="badge badge-secondary float-right">Property</span></th></tr>
        <tr><td class="theme-label">Identifier</td><td><a href="http://rs.tdwg.org/hc/terms/excludedDegreeOfEstablishmentScope">http://rs.tdwg.org/hc/terms/excludedDegreeOfEstablishmentScope</a></td></tr>
        <tr><td class="theme-label">Definition</td><td>Degree(s) of establishment explicitly excluded from sampling during the Event.</td></tr>
        <tr><td class="theme-label">Comments</td><td>Recommended best practice is to use controlled value strings from the controlled vocabulary (<a href="http://rs.tdwg.org/dwcdoe/">http://rs.tdwg.org/dwcdoe/</a>) for the Darwin Core term degreeOfEstablishment. For details, refer to <a href="https://doi.org/10.3897/biss.3.38084">https://doi.org/10.3897/biss.3.38084</a>. Recommended best practice is to separate multiple values in a list with space vertical bar space ( | ).</td></tr>
        <tr><td class="theme-label">Examples</td><td><code>native</code>, <code>invasive | widespreadInvasive</code></td></tr>
    </tbody>
</table>
<p class="invisible">
    <a id="hc:targetGrowthFormScope"></a><a id="targetGrowthFormScope"></a></p>
<table class="table table-sm table-bordered">
    <tbody>
        <tr class="table-secondary"><th colspan="2">targetGrowthFormScope <span class="badge badge-secondary float-right">Property</span></th></tr>
        <tr><td class="theme-label">Identifier</td><td><a href="http://rs.tdwg.org/hc/terms/targetGrowthFormScope">http://rs.tdwg.org/hc/terms/targetGrowthFormScope</a></td></tr>
        <tr><td class="theme-label">Definition</td><td>Targeted growth form(s) or habit(s) of the Organism(s) sampled during the Event.</td></tr>
        <tr><td class="theme-label">Comments</td><td>Recommended best practice is to use a controlled vocabulary and separate multiple values in a list with space vertical bar space ( | ).</td></tr>
        <tr><td class="theme-label">Examples</td><td><code>tree</code>, <code>shrub | sub-shrub</code></td></tr>
    </tbody>
</table>
<p class="invisible">
    <a id="hc:excludedGrowthFormScope"></a><a id="excludedGrowthFormScope"></a></p>
<table class="table table-sm table-bordered">
    <tbody>
        <tr class="table-secondary"><th colspan="2">excludedGrowthFormScope <span class="badge badge-secondary float-right">Property</span></th></tr>
        <tr><td class="theme-label">Identifier</td><td><a href="http://rs.tdwg.org/hc/terms/excludedGrowthFormScope">http://rs.tdwg.org/hc/terms/excludedGrowthFormScope</a></td></tr>
        <tr><td class="theme-label">Definition</td><td>Explicitly excluded growth form(s) or habit(s) of the Organism(s) sampled during the Event.</td></tr>
        <tr><td class="theme-label">Comments</td><td>Recommended best practice is to use a controlled vocabulary and separate multiple values in a list with space vertical bar space ( | ).</td></tr>
        <tr><td class="theme-label">Examples</td><td><code>tree</code>, <code>shrub | sub-shrub</code></td></tr>
    </tbody>
</table>
<p class="invisible">
    <a id="hc:habitatScope"></a><a id="habitatScope"></a></p>
<table class="table table-sm table-bordered">
    <tbody>
        <tr class="table-secondary"><th colspan="2">habitatScope <span class="badge badge-secondary float-right">Property</span></th></tr>
        <tr><td class="theme-label">Identifier</td><td><a href="http://rs.tdwg.org/hc/terms/habitatScope">http://rs.tdwg.org/hc/terms/habitatScope</a></td></tr>
        <tr><td class="theme-label">Definition</td><td>Targeted habitat(s) sampled during the Event.</td></tr>
        <tr><td class="theme-label">Comments</td><td>Recommended best practice is to use a controlled vocabulary and separate the values in a list with space vertical bar space ( | ).</td></tr>
        <tr><td class="theme-label">Examples</td><td><code>dunes</code>, <code>pine forest</code>, <code>riparian</code>, <code>scrub | grassland</code></td></tr>
    </tbody>
</table>
<p class="invisible">
    <a id="hc:excludedHabitatScope"></a><a id="excludedHabitatScope"></a></p>
<table class="table table-sm table-bordered">
    <tbody>
        <tr class="table-secondary"><th colspan="2">excludedHabitatScope <span class="badge badge-secondary float-right">Property</span></th></tr>
        <tr><td class="theme-label">Identifier</td><td><a href="http://rs.tdwg.org/hc/terms/excludedHabitatScope">http://rs.tdwg.org/hc/terms/excludedHabitatScope</a></td></tr>
        <tr><td class="theme-label">Definition</td><td>Explicitly excluded habitat(s) sampled during the Event.</td></tr>
        <tr><td class="theme-label">Comments</td><td>Recommended best practice is to use a controlled vocabulary and separate multiple values in a list with space vertical bar space ( | ).</td></tr>
        <tr><td class="theme-label">Examples</td><td><code>wet flatwoods</code>, <code>swamp | estuary</code></td></tr>
    </tbody>
</table>
<p class="invisible">
    <a id="hc:reportedWeather"></a><a id="reportedWeather"></a></p>
<table class="table table-sm table-bordered">
    <tbody>
        <tr class="table-secondary"><th colspan="2">reportedWeather <span class="badge badge-secondary float-right">Property</span></th></tr>
        <tr><td class="theme-label">Identifier</td><td><a href="http://rs.tdwg.org/hc/terms/reportedWeather">http://rs.tdwg.org/hc/terms/reportedWeather</a></td></tr>
        <tr><td class="theme-label">Definition</td><td>A list of weather or climatic conditions present at the time of the Event.</td></tr>
        <tr><td class="theme-label">Comments</td><td>Recommended best practice is to use a key:value encoding schema for a data interchange format such as JSON.</td></tr>
        <tr><td class="theme-label">Examples</td><td><code>{'minimumTemperatureInDegreesFarenheit':18, 'maximumTemperatureInDegreesFarenheit':32, 'stillWaterCondition':'Partly Frozen'}</code></td></tr>
    </tbody>
</table>
<p class="invisible">
    <a id="hc:reportedExtremeConditions"></a><a id="reportedExtremeConditions"></a></p>
<table class="table table-sm table-bordered">
    <tbody>
        <tr class="table-secondary"><th colspan="2">reportedExtremeConditions <span class="badge badge-secondary float-right">Property</span></th></tr>
        <tr><td class="theme-label">Identifier</td><td><a href="http://rs.tdwg.org/hc/terms/reportedExtremeConditions">http://rs.tdwg.org/hc/terms/reportedExtremeConditions</a></td></tr>
        <tr><td class="theme-label">Definition</td><td>A description of any extreme weather or environmental condition(s) that may have affected the Event.</td></tr>
        <tr><td class="theme-label">Comments</td><td></td></tr>
        <tr><td class="theme-label">Examples</td><td><code>flooding during week 3 of surveys</code>, <code>rockslide at site 2</code></td></tr>
    </tbody>
</table>
<p class="invisible">
    <a id="hc:inventoryTypes"></a><a id="inventoryTypes"></a></p>
<table class="table table-sm table-bordered">
    <tbody>
        <tr class="table-secondary"><th colspan="2">inventoryTypes <span class="badge badge-secondary float-right">Property</span></th></tr>
        <tr><td class="theme-label">Identifier</td><td><a href="http://rs.tdwg.org/hc/terms/inventoryTypes">http://rs.tdwg.org/hc/terms/inventoryTypes</a></td></tr>
        <tr><td class="theme-label">Definition</td><td>The type(s) of search process(es) used to conduct the inventory.</td></tr>
        <tr><td class="theme-label">Comments</td><td>This term is only relevant if the Event represents an inventory. Recommended best practice is to use a controlled vocabulary such as the terms included under the Biological Collections Ontology superclass 'taxonomic inventory process' (<a href="http://purl.obolibrary.org/obo/BCO_0000047">http://purl.obolibrary.org/obo/BCO_0000047</a>). Recommended best practice is to separate multiple values in a list with space vertical bar space ( | ).</td></tr>
        <tr><td class="theme-label">Examples</td><td><code>restricted search</code>, <code>open search</code>, <code>opportunistic search</code>, <code>adventitious</code>, <code>compilation</code>, <code>open search | opportunistic search</code></td></tr>
    </tbody>
</table>
<p class="invisible">
    <a id="hc:compilationType"></a><a id="compilationType"></a></p>
<table class="table table-sm table-bordered">
    <tbody>
        <tr class="table-secondary"><th colspan="2">compilationType <span class="badge badge-secondary float-right">Property</span></th></tr>
        <tr><td class="theme-label">Identifier</td><td><a href="http://rs.tdwg.org/hc/terms/compilationType">http://rs.tdwg.org/hc/terms/compilationType</a></td></tr>
        <tr><td class="theme-label">Definition</td><td>A statement specifying whether data reported are derived from sampling event(s), ancillary data compiled from other sources, or a combination of both.</td></tr>
        <tr><td class="theme-label">Comments</td><td>This term is only relevant if the Event is an inventory. Recommended best practice is to use a controlled vocabulary.</td></tr>
        <tr><td class="theme-label">Examples</td><td><code>surveyOnly</code>, <code>compilationIncludingSurveys</code>, <code>compilationNotIncludingSurveys</code></td></tr>
    </tbody>
</table>
<p class="invisible">
    <a id="hc:compilationSourceTypes"></a><a id="compilationSourceTypes"></a></p>
<table class="table table-sm table-bordered">
    <tbody>
        <tr class="table-secondary"><th colspan="2">compilationSourceTypes <span class="badge badge-secondary float-right">Property</span></th></tr>
        <tr><td class="theme-label">Identifier</td><td><a href="http://rs.tdwg.org/hc/terms/compilationSourceTypes">http://rs.tdwg.org/hc/terms/compilationSourceTypes</a></td></tr>
        <tr><td class="theme-label">Definition</td><td>The type(s) of data sources contributing to the compilation reported.</td></tr>
        <tr><td class="theme-label">Comments</td><td>This term is only relevant if the Event is a compilation in which one or more types of data sources were used. Recommended best practice is to use a controlled vocabulary and separate multiple values in a list with space vertical bar space ( | ).</td></tr>
        <tr><td class="theme-label">Examples</td><td><code>museum specimens</code>, <code>literature</code>, <code>expert knowledge | local knowledge</code></td></tr>
    </tbody>
</table>
<p class="invisible">
    <a id="hc:protocolNames"></a><a id="protocolNames"></a></p>
<table class="table table-sm table-bordered">
    <tbody>
        <tr class="table-secondary"><th colspan="2">protocolNames <span class="badge badge-secondary float-right">Property</span></th></tr>
        <tr><td class="theme-label">Identifier</td><td><a href="http://rs.tdwg.org/hc/terms/protocolNames">http://rs.tdwg.org/hc/terms/protocolNames</a></td></tr>
        <tr><td class="theme-label">Definition</td><td>Categorical descriptive name(s) for the method(s) used during the Event.</td></tr>
        <tr><td class="theme-label">Comments</td><td>Recommended best practice is to use a controlled vocabulary and separate multiple values in a list with space vertical bar space ( | ).</td></tr>
        <tr><td class="theme-label">Examples</td><td><code>boxTrapping</code>, <code>floraInventory</code>, <code>boxTrapping | funnelTrapping</code></td></tr>
    </tbody>
</table>
<p class="invisible">
    <a id="hc:protocolDescription"></a><a id="protocolDescription"></a></p>
<table class="table table-sm table-bordered">
    <tbody>
        <tr class="table-secondary"><th colspan="2">protocolDescription <span class="badge badge-secondary float-right">Property</span></th></tr>
        <tr><td class="theme-label">Identifier</td><td><a href="http://rs.tdwg.org/hc/terms/protocolDescription">http://rs.tdwg.org/hc/terms/protocolDescription</a></td></tr>
        <tr><td class="theme-label">Definition</td><td>A detailed description of the method(s) used during the Event.</td></tr>
        <tr><td class="theme-label">Comments</td><td>This description should be associated with reporting of protocolNames. This may include deviations from the published protocol referred to in protocolReferences. Good practices may include instruments used, calibration, etc.</td></tr>
        <tr><td class="theme-label">Examples</td><td>`Three conventional harp traps (3.2m ht x 2.2m w) were established in flight path zones for a period of 4 hrs at dawn and dusk for a total of 10 trap nights. Traps were visited on an hourly basis during each deployment period and the trap catch recorded for species, size, weight, sex, age and maternal status.</td></tr>
    </tbody>
</table>
<p class="invisible">
    <a id="hc:protocolReferences"></a><a id="protocolReferences"></a></p>
<table class="table table-sm table-bordered">
    <tbody>
        <tr class="table-secondary"><th colspan="2">protocolReferences <span class="badge badge-secondary float-right">Property</span></th></tr>
        <tr><td class="theme-label">Identifier</td><td><a href="http://rs.tdwg.org/hc/terms/protocolReferences">http://rs.tdwg.org/hc/terms/protocolReferences</a></td></tr>
        <tr><td class="theme-label">Definition</td><td>The reference(s) to the method(s) used during the Event.</td></tr>
        <tr><td class="theme-label">Comments</td><td>Recommended best practice is to separate multiple values in a list with space vertical bar space ( | ).</td></tr>
        <tr><td class="theme-label">Examples</td><td><code>Penguins from space: faecal stains reveal the location of emperor penguin colonies, <a href="https://doi.org/10.1111/j.1466-8238.2009.00467.x">https://doi.org/10.1111/j.1466-8238.2009.00467.x</a></code></td></tr>
    </tbody>
</table>
<p class="invisible">
    <a id="hc:isAbundanceReported"></a><a id="isAbundanceReported"></a></p>
<table class="table table-sm table-bordered">
    <tbody>
        <tr class="table-secondary"><th colspan="2">isAbundanceReported <span class="badge badge-secondary float-right">Property</span></th></tr>
        <tr><td class="theme-label">Identifier</td><td><a href="http://rs.tdwg.org/hc/terms/isAbundanceReported">http://rs.tdwg.org/hc/terms/isAbundanceReported</a></td></tr>
        <tr><td class="theme-label">Definition</td><td>A statement about whether the number of Organisms collected or observed is reported.</td></tr>
        <tr><td class="theme-label">Comments</td><td>If the Event is a compilation that contains at least one reported abundance, the value should be 'true'. Typically abundance values reported would be associated with related occurrences, either under the term dwc:individualCount or the combination of terms dwc:organismQuantity and dwc:organismQuantityType.</td></tr>
        <tr><td class="theme-label">Examples</td><td><code>true</code>, <code>false</code></td></tr>
    </tbody>
</table>
<p class="invisible">
    <a id="hc:isAbundanceCapReported"></a><a id="isAbundanceCapReported"></a></p>
<table class="table table-sm table-bordered">
    <tbody>
        <tr class="table-secondary"><th colspan="2">isAbundanceCapReported <span class="badge badge-secondary float-right">Property</span></th></tr>
        <tr><td class="theme-label">Identifier</td><td><a href="http://rs.tdwg.org/hc/terms/isAbundanceCapReported">http://rs.tdwg.org/hc/terms/isAbundanceCapReported</a></td></tr>
        <tr><td class="theme-label">Definition</td><td>A statement about whether a maximum number of Organisms is reported, as specified or restricted by the protocol used.</td></tr>
        <tr><td class="theme-label">Comments</td><td>If the Event is a compilation that contains at least one reported abundance capped, the value should be 'true'. Values of abundance cap should be captured under the term hc:abundanceCap.</td></tr>
        <tr><td class="theme-label">Examples</td><td><code>true</code>, <code>false</code></td></tr>
    </tbody>
</table>
<p class="invisible">
    <a id="hc:abundanceCap"></a><a id="abundanceCap"></a></p>
<table class="table table-sm table-bordered">
    <tbody>
        <tr class="table-secondary"><th colspan="2">abundanceCap <span class="badge badge-secondary float-right">Property</span></th></tr>
        <tr><td class="theme-label">Identifier</td><td><a href="http://rs.tdwg.org/hc/terms/abundanceCap">http://rs.tdwg.org/hc/terms/abundanceCap</a></td></tr>
        <tr><td class="theme-label">Definition</td><td>Maximum number of Organisms reported.</td></tr>
        <tr><td class="theme-label">Comments</td><td>If the Event is a compilation that contains at least one reported abundance capped, the value should be the maximum abundance cap among the ones reported.</td></tr>
        <tr><td class="theme-label">Examples</td><td><code>300</code>,<code>700</code></td></tr>
    </tbody>
</table>
<p class="invisible">
    <a id="hc:isVegetationCoverReported"></a><a id="isVegetationCoverReported"></a></p>
<table class="table table-sm table-bordered">
    <tbody>
        <tr class="table-secondary"><th colspan="2">isVegetationCoverReported <span class="badge badge-secondary float-right">Property</span></th></tr>
        <tr><td class="theme-label">Identifier</td><td><a href="http://rs.tdwg.org/hc/terms/isVegetationCoverReported">http://rs.tdwg.org/hc/terms/isVegetationCoverReported</a></td></tr>
        <tr><td class="theme-label">Definition</td><td>A statement about whether a vegetation cover metric is reported.</td></tr>
        <tr><td class="theme-label">Comments</td><td>If the Event is a compilation that contains at least one reported vegetation cover metric, the value should be 'true'. Typically values or descriptions of vegetation cover would be captured under the term hc:verbatimSiteDescriptions.</td></tr>
        <tr><td class="theme-label">Examples</td><td><code>true</code>, <code>false</code></td></tr>
    </tbody>
</table>
<p class="invisible">
    <a id="hc:isAbsenceReported"></a><a id="isAbsenceReported"></a></p>
<table class="table table-sm table-bordered">
    <tbody>
        <tr class="table-secondary"><th colspan="2">isAbsenceReported <span class="badge badge-secondary float-right">Property</span></th></tr>
        <tr><td class="theme-label">Identifier</td><td><a href="http://rs.tdwg.org/hc/terms/isAbsenceReported">http://rs.tdwg.org/hc/terms/isAbsenceReported</a></td></tr>
        <tr><td class="theme-label">Definition</td><td>A statement about whether taxonomic absences are reported.</td></tr>
        <tr><td class="theme-label">Comments</td><td>If the Event is a compilation that contains at least one reported taxonomic absence, the value should be 'true'. Absences could be reported at any taxonomic level.</td></tr>
        <tr><td class="theme-label">Examples</td><td><code>true</code>, <code>false</code></td></tr>
    </tbody>
</table>
<p class="invisible">
    <a id="hc:absentTaxa"></a><a id="absentTaxa"></a></p>
<table class="table table-sm table-bordered">
    <tbody>
        <tr class="table-secondary"><th colspan="2">absentTaxa <span class="badge badge-secondary float-right">Property</span></th></tr>
        <tr><td class="theme-label">Identifier</td><td><a href="http://rs.tdwg.org/hc/terms/absentTaxa">http://rs.tdwg.org/hc/terms/absentTaxa</a></td></tr>
        <tr><td class="theme-label">Definition</td><td>A list (concatenated and separated) of taxa reported absent during the Event.</td></tr>
        <tr><td class="theme-label">Comments</td><td>Absences could be reported at any taxonomic level. Recommended best practice is to separate multiple values in a list with space vertical bar space ( | ).</td></tr>
        <tr><td class="theme-label">Examples</td><td><code>Parabuteo unicinctus | Geranoaetus melanoleucus</code>, <code>Cetoniinae | Aclopinae | Cyclocephala modesta</code></td></tr>
    </tbody>
</table>
<p class="invisible">
    <a id="hc:hasVouchers"></a><a id="hasVouchers"></a></p>
<table class="table table-sm table-bordered">
    <tbody>
        <tr class="table-secondary"><th colspan="2">hasVouchers <span class="badge badge-secondary float-right">Property</span></th></tr>
        <tr><td class="theme-label">Identifier</td><td><a href="http://rs.tdwg.org/hc/terms/hasVouchers">http://rs.tdwg.org/hc/terms/hasVouchers</a></td></tr>
        <tr><td class="theme-label">Definition</td><td>A statement about whether specimen voucher(s) were collected during Event.</td></tr>
        <tr><td class="theme-label">Comments</td><td>If the Event is a compilation that contains at least one specimen voucher collected, the value should be 'true'.</td></tr>
        <tr><td class="theme-label">Examples</td><td><code>true</code>, <code>false</code></td></tr>
    </tbody>
</table>
<p class="invisible">
    <a id="hc:voucherInstitutions"></a><a id="voucherInstitutions"></a></p>
<table class="table table-sm table-bordered">
    <tbody>
        <tr class="table-secondary"><th colspan="2">voucherInstitutions <span class="badge badge-secondary float-right">Property</span></th></tr>
        <tr><td class="theme-label">Identifier</td><td><a href="http://rs.tdwg.org/hc/terms/voucherInstitutions">http://rs.tdwg.org/hc/terms/voucherInstitutions</a></td></tr>
        <tr><td class="theme-label">Definition</td><td>A list (concatenated and separated) of the name(s) or acronym(s) of the institution(s) where voucher(s) collected during the Event were deposited.</td></tr>
        <tr><td class="theme-label">Comments</td><td>Recommended best practice is to separate multiple values in a list with space vertical bar space ( | ).</td></tr>
        <tr><td class="theme-label">Examples</td><td><code>FMNH</code>, <code>AMNH | MVZ</code>, <code>Nairobi National Museum</code></td></tr>
    </tbody>
</table>
<p class="invisible">
    <a id="hc:hasMaterialSamples"></a><a id="hasMaterialSamples"></a></p>
<table class="table table-sm table-bordered">
    <tbody>
        <tr class="table-secondary"><th colspan="2">hasMaterialSamples <span class="badge badge-secondary float-right">Property</span></th></tr>
        <tr><td class="theme-label">Identifier</td><td><a href="http://rs.tdwg.org/hc/terms/hasMaterialSamples">http://rs.tdwg.org/hc/terms/hasMaterialSamples</a></td></tr>
        <tr><td class="theme-label">Definition</td><td>A statement about whether MaterialSample(s) were collected during the Event.</td></tr>
        <tr><td class="theme-label">Comments</td><td>If the Event is a compilation that contains at least one MaterialSample, the value should be 'true'.</td></tr>
        <tr><td class="theme-label">Examples</td><td><code>true</code>, <code>false</code></td></tr>
    </tbody>
</table>
<p class="invisible">
    <a id="hc:materialSampleTypes"></a><a id="materialSampleTypes"></a></p>
<table class="table table-sm table-bordered">
    <tbody>
        <tr class="table-secondary"><th colspan="2">materialSampleTypes <span class="badge badge-secondary float-right">Property</span></th></tr>
        <tr><td class="theme-label">Identifier</td><td><a href="http://rs.tdwg.org/hc/terms/materialSampleTypes">http://rs.tdwg.org/hc/terms/materialSampleTypes</a></td></tr>
        <tr><td class="theme-label">Definition</td><td>A list (concatenated and separated) of MaterialSample type(s) collected during the Event.</td></tr>
        <tr><td class="theme-label">Comments</td><td>Recommended best practice is to use a controlled vocabulary and separate multiple values in a list with space vertical bar space ( | ).</td></tr>
        <tr><td class="theme-label">Examples</td><td><code>whole organism</code>, <code>skeleton</code>, <code>tissue | blood | fecal | stomach content</code></td></tr>
    </tbody>
</table>
<p class="invisible">
    <a id="hc:isSamplingEffortReported"></a><a id="isSamplingEffortReported"></a></p>
<table class="table table-sm table-bordered">
    <tbody>
        <tr class="table-secondary"><th colspan="2">isSamplingEffortReported <span class="badge badge-secondary float-right">Property</span></th></tr>
        <tr><td class="theme-label">Identifier</td><td><a href="http://rs.tdwg.org/hc/terms/isSamplingEffortReported">http://rs.tdwg.org/hc/terms/isSamplingEffortReported</a></td></tr>
        <tr><td class="theme-label">Definition</td><td>A statement about whether sampling effort associated with the Event is reported.</td></tr>
        <tr><td class="theme-label">Comments</td><td>If the Event is a compilation that contains at least one sampling effort reported, the value should be 'true'. Typically values of effort would be captured under the terms hc:samplingEffortValue and hc:samplingEffortUnit.</td></tr>
        <tr><td class="theme-label">Examples</td><td><code>true</code>, <code>false</code></td></tr>
    </tbody>
</table>
<p class="invisible">
    <a id="hc:samplingEffortProtocol"></a><a id="samplingEffortProtocol"></a></p>
<table class="table table-sm table-bordered">
    <tbody>
        <tr class="table-secondary"><th colspan="2">samplingEffortProtocol <span class="badge badge-secondary float-right">Property</span></th></tr>
        <tr><td class="theme-label">Identifier</td><td><a href="http://rs.tdwg.org/hc/terms/samplingEffortProtocol">http://rs.tdwg.org/hc/terms/samplingEffortProtocol</a></td></tr>
        <tr><td class="theme-label">Definition</td><td>A description of or reference to (publication or URL) the method(s) used to determine the sampling effort.</td></tr>
        <tr><td class="theme-label">Comments</td><td>This description should be associated with reporting of hc:samplingEffortValue and hc:samplingEffortUnit. This is a specialisation of hc:protocolDescritption focused on the effort as distinct from the survey method itself. The effort relates to the intensity of sampling and therefore can assist in interpreting measures of completeness.</td></tr>
        <tr><td class="theme-label">Examples</td><td><code>40 box traps deployed at even spacings along 4 parallel 100m transects placed 50m apart and visited at 6 hourly intervals over a 48 hour period</code>, <code>2 people occupying a bird hide for a period of 8 hours and undertaking a 30 minute count of species within the 150 degree field of view every 2 hours</code>, <code>A single baited camera trap station with motion sensor trigger, deployed for a period of 10 days and configured for detecting large fauna moving through a known traffic way</code></td></tr>
    </tbody>
</table>
<p class="invisible">
    <a id="hc:samplingEffortValue"></a><a id="samplingEffortValue"></a></p>
<table class="table table-sm table-bordered">
    <tbody>
        <tr class="table-secondary"><th colspan="2">samplingEffortValue <span class="badge badge-secondary float-right">Property</span></th></tr>
        <tr><td class="theme-label">Identifier</td><td><a href="http://rs.tdwg.org/hc/terms/samplingEffortValue">http://rs.tdwg.org/hc/terms/samplingEffortValue</a></td></tr>
        <tr><td class="theme-label">Definition</td><td>The numeric value of sampling effort expended during the Event in the unit reported in hc:samplingEffortUnit.</td></tr>
        <tr><td class="theme-label">Comments</td><td>This term is meant to capture the total sampling effort value, to express details use hc:samplingEffortProtocol. For compilations it is recommend not to infer effort.</td></tr>
        <tr><td class="theme-label">Examples</td><td><code>1900</code>, <code>40</code>, <code>5.5</code></td></tr>
    </tbody>
</table>
<p class="invisible">
    <a id="hc:samplingEffortUnit"></a><a id="samplingEffortUnit"></a></p>
<table class="table table-sm table-bordered">
    <tbody>
        <tr class="table-secondary"><th colspan="2">samplingEffortUnit <span class="badge badge-secondary float-right">Property</span></th></tr>
        <tr><td class="theme-label">Identifier</td><td><a href="http://rs.tdwg.org/hc/terms/samplingEffortUnit">http://rs.tdwg.org/hc/terms/samplingEffortUnit</a></td></tr>
        <tr><td class="theme-label">Definition</td><td>The unit used to report hc:samplingEffortValue.</td></tr>
        <tr><td class="theme-label">Comments</td><td>Recommended best practice is to use a controlled vocabulary. hc:samplingEffortUnit should always be used in conjunction with hc:samplingEffortValue.</td></tr>
        <tr><td class="theme-label">Examples</td><td><code>trap hours</code>, <code>person hours</code>, <code>trap days</code></td></tr>
    </tbody>
</table>
<p class="invisible">
    <a id="hc:taxonCompletenessReported"></a><a id="taxonCompletenessReported"></a></p>
<table class="table table-sm table-bordered">
    <tbody>
        <tr class="table-secondary"><th colspan="2">taxonCompletenessReported <span class="badge badge-secondary float-right">Property</span></th></tr>
        <tr><td class="theme-label">Identifier</td><td><a href="http://rs.tdwg.org/hc/terms/taxonCompletenessReported">http://rs.tdwg.org/hc/terms/taxonCompletenessReported</a></td></tr>
        <tr><td class="theme-label">Definition</td><td>Statement about whether, given the hc:targetTaxonomicScope, the Event yielded a complete list of the expected taxa.</td></tr>
        <tr><td class="theme-label">Comments</td><td>Recommended best practice is to use a controlled vocabulary. For compilations it is recommended not to infer completeness.</td></tr>
        <tr><td class="theme-label">Examples</td><td><code>notReported</code>, <code>reportedComplete</code>, <code>reportedIncomplete</code></td></tr>
    </tbody>
</table>
<p class="invisible">
    <a id="hc:taxonCompletenessProtocols"></a><a id="taxonCompletenessProtocols"></a></p>
<table class="table table-sm table-bordered">
    <tbody>
        <tr class="table-secondary"><th colspan="2">taxonCompletenessProtocols <span class="badge badge-secondary float-right">Property</span></th></tr>
        <tr><td class="theme-label">Identifier</td><td><a href="http://rs.tdwg.org/hc/terms/taxonCompletenessProtocols">http://rs.tdwg.org/hc/terms/taxonCompletenessProtocols</a></td></tr>
        <tr><td class="theme-label">Definition</td><td>A description of or reference to (publication, URL) the method(s) used to determined hc:taxonCompletenessReported.</td></tr>
        <tr><td class="theme-label">Comments</td><td>This term allows users to determine how comprehensively an area has been sampled. Recommended best practice is to separate multiple values in a list with space vertical bar space ( | ).</td></tr>
        <tr><td class="theme-label">Examples</td><td><code>Census | Based on sampling effort</code>,  <code>Based on species accumulation curves</code></td></tr>
    </tbody>
</table>


## Identification

<div class="my-4">
        <a class="btn btn-sm btn-outline-secondary m-1" href="#dwc:identifiedBy">identifiedBy</a>
        <a class="btn btn-sm btn-outline-secondary m-1" href="#dwc:identificationReferences">identificationReferences</a>
    </div>

<table class="table table-sm table-bordered">
    <tbody>
        <tr class="table-primary"><th colspan="2">Identification <span class="badge badge-primary float-right">Class</span></th></tr>
        <tr><td class="theme-label">Identifier</td><td><a href="http://rs.tdwg.org/dwc/terms/Identification">http://rs.tdwg.org/dwc/terms/Identification</a></td></tr>
        <tr><td class="theme-label">Definition</td><td>A taxonomic determination (e.g., the assignment to a taxon).</td></tr>
        <tr><td class="theme-label">Comments</td><td></td></tr>
        <tr><td class="theme-label">Examples</td><td>A subspecies determination of an organism.</td></tr>
    </tbody>
</table>

<p class="invisible">
    <a id="dwc:identifiedBy"></a><a id="identifiedBy"></a></p>
<table class="table table-sm table-bordered">
    <tbody>
        <tr class="table-secondary"><th colspan="2">identifiedBy <span class="badge badge-secondary float-right">Property</span></th></tr>
        <tr><td class="theme-label">Identifier</td><td><a href="http://rs.tdwg.org/dwc/terms/identifiedBy">http://rs.tdwg.org/dwc/terms/identifiedBy</a></td></tr>
        <tr><td class="theme-label">Definition</td><td>A list (concatenated and separated) of names of people, groups, or organizations who assigned the Taxon to the subject.</td></tr>
        <tr><td class="theme-label">Comments</td><td>Recommended best practice is to separate multiple values in a list with space vertical bar space ( | ).</td></tr>
        <tr><td class="theme-label">Examples</td><td><code>James L. Patton</code>, <code>Theodore Pappenfuss | Robert Macey</code></td></tr>
    </tbody>
</table>
<p class="invisible">
    <a id="dwc:identificationReferences"></a><a id="identificationReferences"></a></p>
<table class="table table-sm table-bordered">
    <tbody>
        <tr class="table-secondary"><th colspan="2">identificationReferences <span class="badge badge-secondary float-right">Property</span></th></tr>
        <tr><td class="theme-label">Identifier</td><td><a href="http://rs.tdwg.org/dwc/terms/identificationReferences">http://rs.tdwg.org/dwc/terms/identificationReferences</a></td></tr>
        <tr><td class="theme-label">Definition</td><td>A list (concatenated and separated) of references (publication, global unique identifier, URI) used in the Identification.</td></tr>
        <tr><td class="theme-label">Comments</td><td>Recommended best practice is to separate the values in a list with space vertical bar space (<code> | </code>).</td></tr>
        <tr><td class="theme-label">Examples</td><td><code>Aves del Noroeste Patagonico. Christie et al. 2004.</code>, <code>Stebbins, R. Field Guide to Western Reptiles and Amphibians. 3rd Edition. 2003. | Irschick, D.J. and Shaffer, H.B. (1997). The polytypic species revisited: Morphological differentiation among tiger salamanders (Ambystoma tigrinum) (Amphibia: Caudata). Herpetologica, 53(1), 30-49.</code></td></tr>
    </tbody>
</table>

