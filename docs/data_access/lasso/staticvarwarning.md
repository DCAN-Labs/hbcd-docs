# <span style = "color: #ffa500;" class="fas fa-exclamation-triangle"></span> Static Variable Warning
To run a query successfully, your selection must include **at least one non-static instrument**—that is, data collected during specific **sessions or timepoints**. In the NBDC Data Release Platform, look for instruments **not marked as static** (i.e., not shaded differently or labeled as static). These will allow you to run your query and get the required data output. Please expand the following sections for details:  
<div id="query-static-only" class="notification-banner" onclick="toggleCollapse(this)">
  <span class="emoji"><i class="fa-regular fa-lightbulb"></i></span>
  <span class="text">Why You Cannot Run a Query with Only Static Variables</span>
  <span class="notification-arrow">▸</span>
</div>
<div class="notification-collapsible-content">
<p>The platform is designed to support <b>session-based and longitudinal analyses</b>—meaning, comparisons across different timepoints or visits. <br />
<ul>
<p><b>Static variables</b> refer to data that <strong>do not change</strong> across sessions for a participant, e.g.:</p>
<li>Sex assigned at birth  </li>
<li>Date of birth  </li>
<li>Genetic ancestry  </li>
<li>Family relationships  </li>
</ul>

<ul>
<p>Because static variables are constant, they do not provide meaningful variation over time. Querying <em>only</em> static variables undermines the ability to:</p>
<li>Track developmental or behavioral changes  </li>
<li>Compare across timepoints or visits  </li>
<li>Contextualize outcomes within session-specific measures</li>
</ul>
<p>Therefore, to run a query, you must include at least one <b>non-static instrument</b>—data collected at specific visits, such as cognitive assessments or imaging.  </p>
</div>

<div id="static-var-src" class="notification-banner" onclick="toggleCollapse(this)">
  <span class="emoji"><i class="fa-regular fa-lightbulb"></i></span>
  <span class="text">Overview of Static Variable Sources</span>
  <span class="notification-arrow">▸</span>
</div>
<div class="notification-collapsible-content">
<p>There are three main static measurement sources in the <b>ABCD</b> dataset. Here's what each includes: </p>

<ul>
<p>
<b>1. Genetic Population Structure</b> (<code>gn_y_popstruct</code>)<br>
Derived from genotyping data, this includes principal components of genetic ancestry used to account for population stratification in genetic analyses:<br>
<li><code>gn_y_popstruct_pc__01</code> to <code>gn_y_popstruct_pc__32</code>  </li>
<li>Each variable represents a principal component capturing ancestry-related genetic variation  </li>
</ul>
</p>

<ul>
<p>
<b>2. Genetic Relatedness</b> (<code>gn_y_genrel</code>)<br>
Describes genetic relationships between participants, such as familial ties or twin status. Values are derived from genotype-based estimates of relatedness and include:<br>
<li><code>gn_y_genrel_id__fam</code>: Family ID based on genetic similarity  </li>
<li><code>gn_y_genrel_id__birth</code>: Birth event ID (e.g., twins)  </li>
<li><code>gn_y_genrel_pihat__01–04</code>: Identity-by-descent probabilities  </li>
<li><code>gn_y_genrel_zyg__01–04</code>: Inferred zygosity (e.g., monozygotic twin) </li>
</ul>
</p>

<ul>
<p>
<b>3. Static Demographics / Study Design Info</b> (<code>ab_g_stc</code>)<br>
Fixed participant metadata collected at enrollment or inferred from administrative records, including:<br>
<li><code>ab_g_stc__design_id__fam</code>: Family ID based on caregiver report  </li>
<li><code>ab_g_stc__cohort_dob</code>: Anonymized date of birth  </li>
<li><code>ab_g_stc__cohort_saab</code>: Sex assigned at birth  </li>
<li>Genetic ancestry principal components (duplicated from <code>gn_y_popstruct</code>)  </li>
<li>Other design-level variables (e.g., nesting IDs, twin group IDs)  </li>
</ul>
</p>
</div>
<br>