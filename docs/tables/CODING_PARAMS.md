# CODING_PARAMS

> This tables stores coding interface parameters such as interface input path, interface output path and interface source path.

**Description:** ProFile encoder interface parameters  
**Table type:** REFERENCE  
**Primary key:** _(not published — see note)_  
**Columns:** 49

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ABSTR_REQ_FINAL_IND` | DOUBLE | NOT NULL |  | Abstract Request Final Indicator |
| 2 | `ACTIVE_IND` | DOUBLE |  |  | The table row is active or inactive. A row is generally active unless it is in an inactive state such as logically deleted, combined away, pending purge, etc. |
| 3 | `ACTIVE_STATUS_CD` | DOUBLE | NOT NULL |  | Indicates the status of the row itself (not the data in the row) such as active, inactive, combined away, pending purge, etc. |
| 4 | `ACTIVE_STATUS_DT_TM` | DATETIME |  |  | The date and time that the active_status_cd was set. |
| 5 | `ACTIVE_STATUS_PRSNL_ID` | DOUBLE | NOT NULL |  | The person who caused the active_status_cd to be set or change. |
| 6 | `ADMIT_DIAG_REQUIRED_IND` | DOUBLE |  |  | When this indicator is set to1, admit diagonosis is required to save as final. |
| 7 | `AUTO_IMPORT_IND` | DOUBLE |  |  | auto import indicator |
| 8 | `BEG_EFFECTIVE_DT_TM` | DATETIME |  |  | The date and time for which this table row becomes effective. Normally, this will be the date and time the row is added, but could be a past or future date and time. |
| 9 | `CANCER_CODE_CNT_IND` | DOUBLE | NOT NULL |  | Cancer Code Count Indicator |
| 10 | `CHANGE_AFTER_FINAL_IND` | DOUBLE |  |  | Enable or disable the ability for users to change codes after they have been saved as final |
| 11 | `CLINICAL_CODING_IND` | DOUBLE |  |  | clinical coding indicator |
| 12 | `CODING_PARAMS_ID` | DOUBLE | NOT NULL |  | This is the value of the unique primary identifier of the coding params table. It is an internal system assigned number |
| 13 | `CPT_CODE_CNT` | DOUBLE |  |  | This is the number of cpt codes that the encoder interface is expecting, used with fixed length file interface. |
| 14 | `DEFAULT_REPORT_NAME` | VARCHAR(255) |  |  | This is the default report name that will be used if no report name is found in the coding flex summary |
| 15 | `DIAGNOSIS_CODE_CNT` | DOUBLE |  |  | This is the number of diagnosis codes that the encoder interface is expecting, used with fixed length file interface. |
| 16 | `DRAFT_DROP_BILL_IND` | DOUBLE |  |  | To send outbound drop bill info when coding saved as draft |
| 17 | `DRG_CODE_CNT` | DOUBLE |  |  | This is the number of drg codes that the encoder interface is expecting, used with fixed length file interface. |
| 18 | `DROP_BILL_FLAG` | DOUBLE |  |  | Drop Bill Flag |
| 19 | `DROP_BILL_IND` | DOUBLE |  |  | Indicates if a drop bill notification should be sent |
| 20 | `EDIT_CHK_IND` | DOUBLE |  |  | Parameter to turn ICD-10 edit checking on/off. |
| 21 | `ENCNTR_SLICE_IND` | DOUBLE |  |  | Indicates whether coding is at the encounter slice level |
| 22 | `ENCODER_INPUT_PATH` | VARCHAR(255) |  |  | This is the path of the encoder interface input directory |
| 23 | `ENCODER_OUTPUT_PATH` | VARCHAR(255) |  |  | This is the path of the encoder interface output directory |
| 24 | `ENCODER_SOURCE_PATH` | VARCHAR(255) |  |  | This is the path of the encoder interface source directory |
| 25 | `ENCODER_TYPE_CD` | DOUBLE | NOT NULL |  | This is the type of encoder used |
| 26 | `END_EFFECTIVE_DT_TM` | DATETIME |  |  | The date/time after which the row is no longer valid as active current data. This may be valued with the date that the row became inactive. |
| 27 | `GENERIC_COLUMN_IND` | DOUBLE |  |  | Flag that determines if the "Generic Field" will have it's value displayed in a column on the procedure view in himChartCoding. |
| 28 | `GENERIC_DEFAULT_VAL_CD` | DOUBLE | NOT NULL |  | Stores the default value for the Generic Field in himChartCoding. |
| 29 | `GENERIC_LABEL_NAME` | VARCHAR(100) |  |  | Stores the label for the Generic Field in himChartCoding. |
| 30 | `GENERIC_REQUIRED_IND` | DOUBLE |  |  | Flag that determines if the Generic Field is required in himChartCoding. |
| 31 | `GENERIC_VISIBLE_IND` | DOUBLE |  |  | Flag that determines if the Generic Field is enabled in himChartCoding. |
| 32 | `GROUPER_REQUIRED_FLAG` | DOUBLE | NOT NULL |  | Flag specifying whether a grouper code is required in certain scenarios. |
| 33 | `GROUP_PRINCIPLE_TYPE_CD` | DOUBLE | NOT NULL |  | This is the default group principle type used. |
| 34 | `INTERFACE_PATH` | VARCHAR(255) |  |  | This is the path of the encoder interface |
| 35 | `LAUNCH_ABSTR_DRAFT_IND` | DOUBLE | NOT NULL |  | Launch Abstract Draft indicator |
| 36 | `MERGED_ACCOUNT_IND` | DOUBLE |  |  | Yes if this site will be merging two encounters for coding purposes, no if the site will not be merging two encounters for coding purposes. |
| 37 | `OCE_DEF_INFOX_CARRIER` | VARCHAR(40) |  |  | Default value to be used for the CarrierID field of the USER record when generating OCE Edits input files for use with the Info-X system. CarrierID is to be filled out with the CODE_VALUE.Display for the Outbound Code Value Alias for Info-X (contributor system) for the Financial Class associated with an encounter. If an Outbound Code Value Alias is not found for Info-X for the encounter's Financial_Class_Cd, the value in this field will be used to populate the CarrierID field. |
| 38 | `OCE_EDITS_FLAG` | DOUBLE | NOT NULL |  | The flag indicates if OCE edits should be called and when. |
| 39 | `OCE_EDITS_INPUT_PATH` | VARCHAR(255) |  |  | This is the directory where we will put the input file for the OCE edits. |
| 40 | `OCE_EDITS_OUTPUT_PATH` | VARCHAR(255) |  |  | This is the directory where we will look for the output file created from the OCE edits. |
| 41 | `PAYER_VALIDATION_IND` | DOUBLE | NOT NULL |  | indicator for payer validation |
| 42 | `PROBLEM_LIST_IND` | DOUBLE |  |  | Indicator that toggles whether a site will be able to launch to the Problem List from Chart Coding. |
| 43 | `PROCEDURE_CODE_CNT` | DOUBLE |  |  | This is the number of procedure codes that the encoder interface is expecting, used with fixed length file interface. |
| 44 | `SERVICE_CAT_IND` | DOUBLE |  |  | Determines if site is coding at service category level or encounterlevel. |
| 45 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 46 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 47 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 48 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 49 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

