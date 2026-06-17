# QMD_LH_QRDA_AGGREGATION

> A table that stores the aggregated data for electronic hospital quality submissions that is leveraged by Quality Clearinghouse

**Description:** QMD_LH_QRDA_AGGREGATION  
**Table type:** ACTIVITY  
**Primary key:** _(not published — see note)_  
**Columns:** 40

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ADMIT_DT_TM` | DATETIME |  |  | An identifier that denotes admit date time from the submissison tables |
| 2 | `CCN_NBR_TXT` | VARCHAR(150) |  |  | An identifier for the facilty number of a hospital for center of medicare and medicaid |
| 3 | `CODE` | VARCHAR(100) |  |  | An identifier that denotes code key from the submissison tables |
| 4 | `CODE_DISPLAY` | VARCHAR(500) |  |  | An identifier that denotes code display key from the submissison tables |
| 5 | `CODE_DISPLAY_NEG` | VARCHAR(500) |  |  | An identifier that denotes code display negate key from the submissison tables |
| 6 | `CODE_NEG` | VARCHAR(100) |  |  | An identifier that denotes code negate key from the submissison tables |
| 7 | `CODE_SDTC` | VARCHAR(50) |  |  | An identifier that denotes code sdtc key from the submissison tables |
| 8 | `CODE_SDTC_NEG` | VARCHAR(50) |  |  | An identifier that denotes code sdtc negate key from the submissison tables |
| 9 | `CODE_SYSTEM` | VARCHAR(100) |  |  | An identifier that denotes code system key from the submissison tables |
| 10 | `CODE_SYSTEM_NAME` | VARCHAR(100) |  |  | An identifier that denotes code system name key from the submissison tables |
| 11 | `CODE_SYSTEM_NAME_NEG` | VARCHAR(50) |  |  | An identifier that denotes code system name negate key from the submissison tables |
| 12 | `CODE_SYSTEM_NEG` | VARCHAR(50) |  |  | An identifier that denotes code system negate key from the submissison tables |
| 13 | `DISCHARGE_DT_TM` | DATETIME |  |  | An identifier that denotes discharge date time from the submissison tables |
| 14 | `ENCNTR_ID` | DOUBLE | NOT NULL |  | An identifier that denotes an encounter id from the submissison tables |
| 15 | `ENTRY_ID` | DOUBLE | NOT NULL |  | An identifier that denotes an entry id from the submissison tables |
| 16 | `ENTRY_TYPE` | VARCHAR(50) |  |  | An identifier that denotes an entry type from the submissison tables |
| 17 | `ERROR_IND` | DOUBLE |  |  | AN identiifier to denote if there is any errors found in submission tables |
| 18 | `FINANCIAL_NBR_TXT` | VARCHAR(50) |  |  | An identifier that denotes FIN number |
| 19 | `HCO_NBR` | DOUBLE |  |  | An identifier for the facilty number of a hospital for Joint commission |
| 20 | `HIGH_TIME` | DATETIME |  |  | An identifier that denotes high time from the submissison tables |
| 21 | `HIGH_TIME_EXTRA` | DATETIME |  |  | An identifier that denotes high time extra from the submissison tables |
| 22 | `HIGH_TIME_NEG` | DATETIME |  |  | An identifier that denotes high time negate from the submissison tables |
| 23 | `LOW_TIME` | DATETIME |  |  | An identifier that denotes low time from the submissison tables |
| 24 | `LOW_TIME_EXTRA` | DATETIME |  |  | An identifier that denotes low time extra from the submissison tables |
| 25 | `LOW_TIME_NEG` | DATETIME |  |  | An identifier that denotes low time negate from the submissison tables |
| 26 | `METRIC_ID` | DOUBLE | NOT NULL |  | An identifier that denotes an metric id from the submissison tables |
| 27 | `METRIC_TYPE` | VARCHAR(50) |  |  | An identifier that denotes an metric type from the submissison tables |
| 28 | `NEG_IND` | DOUBLE | NOT NULL |  | An identifier that denotes negate id from the submissison tables |
| 29 | `NICU_IND` | DOUBLE |  |  | An identifier that denotes NICU id from the submissison tables |
| 30 | `PARENT_ID2` | DOUBLE | NOT NULL |  | An identifier that denotes an parent id from the submissison tables |
| 31 | `PARENT_NAME2` | VARCHAR(50) |  |  | An identifier that denotes an parent name from the submissison tables |
| 32 | `PERSON_ID` | DOUBLE | NOT NULL |  | An identifier that denotes an person id from the submissison tables |
| 33 | `PERSON_NAME` | VARCHAR(100) |  |  | A column for person name |
| 34 | `PRINCIPAL_IND` | DOUBLE |  |  | An identifier that denotes principal indicator from the submissison tables |
| 35 | `RESULTS_UNITS` | VARCHAR(50) |  |  | An identifier that denotes result units value from the submissison tables |
| 36 | `RESULT_VALUE` | VARCHAR(255) |  |  | An identifier that denotes result value from the submissison tables |
| 37 | `ROUTE_CODE` | VARCHAR(50) |  |  | An identifier that denotes route code from the submissison tables |
| 38 | `TEMPLATE` | VARCHAR(50) |  |  | An identifier that denotes the QRDA template from the submissison tables |
| 39 | `UPDT_DT_TM` | DATETIME |  |  | The date and time of ETL record to be updated |
| 40 | `UPDT_TASK` | VARCHAR(50) |  |  | The person who updated the record |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

