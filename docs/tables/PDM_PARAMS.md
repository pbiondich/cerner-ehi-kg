# PDM_PARAMS

> Stores the reference data for Quatlity Control Patient Data Monitoring.

**Description:** Patient Data Monitoring Parameters  
**Table type:** REFERENCE  
**Primary key:** `PDM_PARAM_ID`  
**Columns:** 17  
**Referenced by:** 3 columns

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ACTIVE_IND` | DOUBLE | NOT NULL |  | The table row is active or inactive. A row is generally active unless it is in an inactive state such as logically deleted, combined away, pending purge, etc. |
| 2 | `BEG_EFFECTIVE_DT_TM` | DATETIME | NOT NULL |  | The date and time for which this table row becomes effective. Normally, this will be the date and time the row is added, but could be a past or future date and time. |
| 3 | `END_EFFECTIVE_DT_TM` | DATETIME | NOT NULL |  | The date/time after which the row is no longer valid as active current data. This may be valued with the date that the row became inactive. |
| 4 | `MIN_NBR_RESULTS` | DOUBLE | NOT NULL |  | Defines the minimum number of patient results required before converting the results into a quality control result. |
| 5 | `NBR_RESULTS` | DOUBLE | NOT NULL |  | Defines the number of patient results to use for the creation of a quality control result. Once this number is reached, the QC result will be created and the count will start over. |
| 6 | `PDM_PARAM_ID` | DOUBLE | NOT NULL | PK | A unique, internal, system-assigned number that identifies specific patient data monitoring parameters. |
| 7 | `RESULT_EVAL_FLAG` | DOUBLE | NOT NULL |  | Defines the number of results or the time period required to generate a quality control result. |
| 8 | `RULE_ID` | DOUBLE | NOT NULL |  | A unique, internal, system-assigned number that identifies the specific rule set used to evaluate the quality control result. |
| 9 | `SERVICE_RESOURCE_CD` | DOUBLE | NOT NULL |  | A unique code value that identifies the specific service resource where the result was performed. |
| 10 | `TASK_ASSAY_CD` | DOUBLE | NOT NULL |  | A unique code value that identifies the specific discrete task assay associated with the quality control result entered in the system. |
| 11 | `TIME_PERIOD_MINUTES` | DOUBLE | NOT NULL |  | Defines the number of minutes to accumulate patient results before converting them into a quality control result. |
| 12 | `TIME_PERIOD_UNITS_CD` | DOUBLE | NOT NULL |  | A unique code value that identifies the time units of measure (such as day, week, and so on) to accumulate patient results before converting them into a quality control result. |
| 13 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 14 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 15 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 16 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 17 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Referenced by (3)

| From table | Column |
|------------|--------|
| [PDM_RANGES](PDM_RANGES.md) | `PDM_PARAM_ID` |
| [QC_RESULT](QC_RESULT.md) | `PDM_PARAM_ID` |
| [QC_STAT_PERIOD](QC_STAT_PERIOD.md) | `PDM_PARAM_ID` |

