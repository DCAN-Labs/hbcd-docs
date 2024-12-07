def define_env(env):
    """
    Setup the environment for macros.
    """
    @env.macro
    def implementation_details(
        method, form_name, dictionary, translation, form_type, respondent, visits, time_estimate
    ):
        # Return the raw HTML as a string
        return f"""
<details>
<summary>Implementation & Data Collection Details</summary>
<ul>
<li><b>Method of Administration</b>: {method}</li>
<li><b>REDCap Form Name</b>: {form_name}</li>
<li><b>Pilot Data Dictionary</b>: {dictionary}</li>
<li><b>Spanish Translation</b>: {translation}</li>
<li><b>Child Specific/Unspecific Form</b>: {form_type}</li>
<li><b>Respondent:</b> {respondent}</li>
<li><b>Visits</b>: {visits}</li>
<li><b>Estimated length of time for completion</b>: {time_estimate}</li>
</ul>
</details>
"""
