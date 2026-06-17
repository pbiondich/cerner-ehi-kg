# OMF_OUTCOME_RATE

> stores the rate based indicators

**Description:** OMF OUTCOME RATE  
**Table type:** ACTIVITY  
**Primary key:** _(not published — see note)_  
**Columns:** 38

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `CLIENT_NBR` | DOUBLE | NOT NULL |  | client number |
| 2 | `GROUP_DENOM` | DOUBLE |  |  | denominator for the peer group |
| 3 | `GROUP_DENOM_MAX` | DOUBLE |  |  | maximum denominator for the peer group |
| 4 | `GROUP_DENOM_MEAN` | DOUBLE |  |  | mean denominator for the peer group |
| 5 | `GROUP_DENOM_MEDIAN` | DOUBLE |  |  | median denominator for the peer group |
| 6 | `GROUP_DENOM_MIN` | DOUBLE |  |  | minimum denominator for the peer group |
| 7 | `GROUP_NUMBER_HCO` | DOUBLE |  |  | peer group number |
| 8 | `GROUP_NUMER` | DOUBLE |  |  | peer group numerator |
| 9 | `GROUP_NUMER_MAX` | DOUBLE |  |  | maximum peer group numerator |
| 10 | `GROUP_NUMER_MEAN` | DOUBLE |  |  | mean peer group numerator |
| 11 | `GROUP_NUMER_MEDIAN` | DOUBLE |  |  | median peer group numerator |
| 12 | `GROUP_NUMER_MIN` | DOUBLE |  |  | minimum peer group numerator |
| 13 | `GROUP_RATE` | DOUBLE |  |  | peer group value |
| 14 | `GROUP_RATE_MAX` | DOUBLE |  |  | maximum peer group value |
| 15 | `GROUP_RATE_MEAN` | DOUBLE |  |  | mean peer group value |
| 16 | `GROUP_RATE_MEDIAN` | DOUBLE |  |  | median peer group value |
| 17 | `GROUP_RATE_MIN` | DOUBLE |  |  | minimum peer group value |
| 18 | `GROUP_RATE_STD_DEV` | DOUBLE |  |  | standard deviation peer group value |
| 19 | `GROUP_TOTAL_CASES` | DOUBLE |  |  | peer group total cases |
| 20 | `GROUP_TOTAL_CASES_FOR_RATIO` | DOUBLE |  |  | total cases in peer group that qualified |
| 21 | `HCO_DENOM_VALUE` | DOUBLE |  |  | denominator for healthcare organization |
| 22 | `HCO_NUMER_VALUE` | DOUBLE |  |  | numerator for healthcare organization |
| 23 | `HCO_OBS_RATE` | DOUBLE |  |  | healthcare organization's observed rate |
| 24 | `HCO_OBS_RATIO_STD_DEV` | DOUBLE |  |  | healthcare organization observed rate standard deviation |
| 25 | `HCO_RISK_ADJ_NUMBER_OF_CASES` | DOUBLE |  |  | health care organizations risk adjusted number of cases |
| 26 | `HCO_RISK_ADJ_RATE` | DOUBLE |  |  | healthcare organization's risk adjusted rate |
| 27 | `HCO_RISK_ADJ_RATE_STD_DEV` | DOUBLE |  |  | standard deviation of healthcare organization's risk adjusted rate |
| 28 | `HCO_RISK_ADJ_RATIO_STD_DEV` | DOUBLE |  |  | standard deviation of healthcare organization's risk adjusted ratio |
| 29 | `HCO_TOTAL_CASES` | DOUBLE |  |  | healthcare organization's total cases |
| 30 | `HCO_TOTAL_CASES_FOR_RATIO` | DOUBLE |  |  | healthcare organization's total cases that qualified |
| 31 | `INDICATOR_NBR` | DOUBLE | NOT NULL |  | This is the Cerner defined number for this indicator |
| 32 | `JCAHO_REPORTED_MEASURE_IND` | DOUBLE |  |  | send this indicator to jcaho oryx |
| 33 | `REPORTING_PERIOD` | DATETIME | NOT NULL |  | reporting period |
| 34 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 35 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 36 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 37 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 38 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

