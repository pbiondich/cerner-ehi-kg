# OMF_OUTCOME_CONTINUOUS

> omf outcomes indicators stored here

**Description:** OMF OUTCOME CONTINUOUS  
**Table type:** ACTIVITY  
**Primary key:** _(not published — see note)_  
**Columns:** 35

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `CLIENT_NBR` | DOUBLE | NOT NULL |  | client number |
| 2 | `GROUP_NUMBER_CASES` | DOUBLE |  |  | number of cases in peer group |
| 3 | `GROUP_NUMBER_CASES_MAX` | DOUBLE |  |  | maximum number of cases in peer group |
| 4 | `GROUP_NUMBER_CASES_MEAN` | DOUBLE |  |  | average number of cases in peer group |
| 5 | `GROUP_NUMBER_CASES_MEDIAN` | DOUBLE |  |  | median number of cases in peer group |
| 6 | `GROUP_NUMBER_CASES_MIN` | DOUBLE |  |  | minimum number of cases in peer group |
| 7 | `GROUP_NUMBER_HCO` | DOUBLE |  |  | peer group number |
| 8 | `GROUP_OBS_MAX_OVERALL_MEAN` | DOUBLE |  |  | peer group observed overall mean |
| 9 | `GROUP_OBS_MEAN_OVERALL_MEAN` | DOUBLE |  |  | peer group observed mean overall mean |
| 10 | `GROUP_OBS_MEDIAN_OVERALL_MEAN` | DOUBLE |  |  | peer group observed median overall mean |
| 11 | `GROUP_OBS_MIN_OVERALL_MEAN` | DOUBLE |  |  | peer group observed min overall mean |
| 12 | `GROUP_OBS_OVERALL_MEAN` | DOUBLE |  |  | peer group observed overall mean |
| 13 | `GROUP_OBS_STD_DEV_OVERALL_MEAN` | DOUBLE |  |  | peer group observed standard deviation overall mean |
| 14 | `HCO_DIFF_OBS_RISK_ADJ_STD_DEV` | DOUBLE |  |  | healthcare organization's differential observed risk adjusted standard deviation |
| 15 | `HCO_NUMBER_OF_CASES` | DOUBLE |  |  | healthcare organization's number of cases |
| 16 | `HCO_OBS_MAX` | DOUBLE |  |  | healthcare organization's observed maximum |
| 17 | `HCO_OBS_MEAN` | DOUBLE |  |  | healthcare organization's observed mean |
| 18 | `HCO_OBS_MEDIAN` | DOUBLE |  |  | healthcare organization's observed median |
| 19 | `HCO_OBS_MIN` | DOUBLE |  |  | healthcare organization's observed minimum |
| 20 | `HCO_OBS_STD_DEV` | DOUBLE |  |  | healthcare organization's observed standard deviation |
| 21 | `HCO_RISK_ADJ_MAX` | DOUBLE |  |  | healthcare organization's risk adjusted maximum |
| 22 | `HCO_RISK_ADJ_MEAN` | DOUBLE |  |  | healthcare organization's risk adjusted mean |
| 23 | `HCO_RISK_ADJ_MEDIAN` | DOUBLE |  |  | healthcare organization's risk adjusted median |
| 24 | `HCO_RISK_ADJ_MIN` | DOUBLE |  |  | healthcare organization's risk adjusted minimum |
| 25 | `HCO_RISK_ADJ_NUMBER_OF_CASES` | DOUBLE |  |  | health care organizations risk adjusted number of cases |
| 26 | `HCO_RISK_ADJ_STD_DEV` | DOUBLE |  |  | healthcare organization's risk adjusted standard deviation |
| 27 | `HCO_TOTAL_CASES` | DOUBLE |  |  | healthcare organization's total cases |
| 28 | `INDICATOR_NBR` | DOUBLE | NOT NULL |  | This is the Cerner defined number for this indicator |
| 29 | `JCAHO_REPORTED_MEASURE_IND` | DOUBLE |  |  | indicates whether indicator is reported to jcaho |
| 30 | `REPORTING_PERIOD` | DATETIME | NOT NULL |  | reporting period |
| 31 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 32 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 33 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 34 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 35 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

