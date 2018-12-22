DROP TABLE IF EXISTS clinical_trial;

CREATE TABLE clinical_trial (
	NCT_Number text NOT NULL,
	Title text,
	Study_Results text,
	Conditions text,
	Interventions text,
	Outcome_Measures text,
	Gender text,
	Age_Group text,
	Phases text,
	Enrollment Integer,
	Study_Type text,
	Study_Designs text,
	Start_Date Date,
	Primary_Completion_Date Date,
	Completion_Date Date,
	Allocation text,
	Intervention_Model text,
	Masking text,
	Primary_Purpose text,
	Intervention_Methods text,
	Duration integer,
	PRIMARY KEY(NCT_Number)
);