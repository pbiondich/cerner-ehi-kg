# MIC_STAT_SUSCEPTIBILITY

> This summary table is comprised of records extracted from the MIC_SUS_ORDER_DETAIL and MIC_SUS_MED_RESULT tables. This information is utilized by the Microbiology Statistical Reporting package.

**Description:** Microbiology Statistical Susceptibility  
**Table type:** ACTIVITY  
**Primary key:** _(not published — see note)_  
**Columns:** 27

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ABNORMAL_IND` | DOUBLE |  |  | This field identifies whether or not the susceptibility result has been defined as an abnormal susceptibility response. Valid values include: 0 = Normal response 1 = Abnormal response |
| 2 | `ALPHA_RESULT_CD` | DOUBLE | NOT NULL |  | This field contains the internal identification code for the alpha susceptibility result value. |
| 3 | `ANTIBIOTIC_CD` | DOUBLE | NOT NULL |  | This field contains the internal identification code for the antibiotic being tested. |
| 4 | `ANTIBIOTIC_DISPLAY_ORDER` | DOUBLE | NOT NULL |  | This field identifies the order in which the antibiotics will be displayed. |
| 5 | `CHARTABLE_IND` | DOUBLE |  |  | This field indicates whether the susceptibility result should be displayed on patient reports or be displayed in inquiry applications. Valid values include: 0 = Non-chartable 1 = Chartable |
| 6 | `DELTA_CHECKING_IND` | DOUBLE |  |  | Indicates whether or not a delta checking failure occurred for the result. |
| 7 | `DETAIL_CD` | DOUBLE | NOT NULL |  | This field contains the internal identification code for the detail susceptibility procedure. |
| 8 | `DETAIL_DISPLAY_ORDER` | DOUBLE | NOT NULL |  | This field identifies the order in which the detail susceptibility procedures will be displayed. |
| 9 | `DETAIL_TYPE_FLAG` | DOUBLE |  |  | This field identifies the type of detail susceptibility procedure. |
| 10 | `DUP_ANTIBIOTIC_IND` | DOUBLE |  |  | This field indicates whether the antibiotic is considered to be a duplicate. The setting of the field is based on susceptibility duplicate checking rules. |
| 11 | `INTERP_RESULT_CD` | DOUBLE | NOT NULL |  | This field contains the internal identification code for the interpretation susceptibility result value. |
| 12 | `PANEL_CD` | DOUBLE | NOT NULL |  | This field contains the internal identification code for the susceptibility panel. |
| 13 | `PANEL_DISPLAY_ORDER` | DOUBLE | NOT NULL |  | This field identifies the order in which the susceptibility panels will be displayed. |
| 14 | `RESULT_DT_NBR` | DOUBLE | NOT NULL |  | The date number when the susceptibility result was last updated. Used to gather date information from the OMF_DATE table. |
| 15 | `RESULT_DT_TM` | DATETIME |  |  | This field contains the date and time at which the susceptibility result was last updated. |
| 16 | `RESULT_GROUP_CD` | DOUBLE | NOT NULL |  | This field contains the internal identification code for the susceptibility result grouping to which this result is associated. |
| 17 | `RESULT_MIN_NBR` | DOUBLE | NOT NULL |  | The minute number when the susceptibility result was last updated. Used to get time information from the OMF_TIME table. |
| 18 | `RESULT_NUMERIC` | DOUBLE | NOT NULL |  | This field identifies the susceptibility result when the detail susceptibility procedure is defined as 'numeric'. |
| 19 | `RESULT_PRSNL_ID` | DOUBLE | NOT NULL | FK→ | This field contains the internal identification code for the person whom last updated the susceptibility result. This could be used to join to the PRSNL table. |
| 20 | `RESULT_UNITS_CD` | DOUBLE | NOT NULL |  | This field contains the internal identification code for the units of measure associated with the numeric susceptibility result. |
| 21 | `STATUS_CD` | DOUBLE | NOT NULL |  | This field contains the internal identification code for the status of the susceptibility result. |
| 22 | `TASK_LOG_ID` | DOUBLE | NOT NULL | FK→ | This field contains the internal identification code assigned to the susceptibility task from the MIC_STAT_TASK table thus associating the susceptibility result with the appropriate susceptibility task. |
| 23 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 24 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 25 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 26 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 27 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `RESULT_PRSNL_ID` | [PRSNL](PRSNL.md) | `PERSON_ID` |
| `TASK_LOG_ID` | [MIC_STAT_TASK](MIC_STAT_TASK.md) | `TASK_LOG_ID` |

