# MIC_STAT_REPORT_RESPONSE

> This summary table is comprised of records extracted from the MIC_REPORT_RESPONSE table. This information is utilized by the Microbiology Statistical Reporting package.

**Description:** Microbiology Statistical Report Response  
**Table type:** ACTIVITY  
**Primary key:** _(not published — see note)_  
**Columns:** 16

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ABNORMAL_IND` | DOUBLE |  |  | This field identifies whether or not the response has been defined as an abnormal report response. Valid values include: 0 = Normal response 1 = Abnormal response |
| 2 | `DUP_RESPONSE_IND` | DOUBLE |  |  | This field indicates whether the response is considered to be a duplicate. The setting of the field is based on report duplicate checking rules. |
| 3 | `GROUP_RESPONSE_ID` | DOUBLE | NOT NULL | FK→ | This field contains the internal identification code of the group response entered for the report task. This could be used to join to the MIC_GROUP_RESPONSE table. |
| 4 | `ORG_TASK_LOG_ID` | DOUBLE | NOT NULL | FK→ | This field is used to correlate multiple responses to one TASK_LOG_ID on the MIC_STAT_TASK table. |
| 5 | `POSITIVE_IND` | DOUBLE |  |  | This field identifies whether or not the response has been defined as a positive report response. Valid values include: 0 = negative response 1 = positive response |
| 6 | `RESPONSE_CD` | DOUBLE | NOT NULL |  | This field contains the internal identification code of the coded response entered for the report task. This could contain code set 1021, 1022... |
| 7 | `RESPONSE_CLASS_FLAG` | DOUBLE | NOT NULL |  | This field identifies the type of response used in issuing the report. |
| 8 | `RESPONSE_TEXT` | VARCHAR(500) |  |  | This field contains free text response information associated with the report task. |
| 9 | `SEQUENCE` | DOUBLE | NOT NULL |  | The field contains a value that uniquely identifies each report response. This value will allow multiples of the same report response to be uniquely identified. |
| 10 | `STATISTICS_FLAG` | DOUBLE |  |  | This field identifies how a report response will be counted in statistical reporting. |
| 11 | `TASK_LOG_ID` | DOUBLE | NOT NULL | FK→ | This field contains the internal identification code assigned to the report task from the MIC_STAT_TASK table thus associating the report result with the appropriate report task. |
| 12 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 13 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 14 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 15 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 16 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `GROUP_RESPONSE_ID` | [MIC_GROUP_RESPONSE](MIC_GROUP_RESPONSE.md) | `GROUP_RESPONSE_ID` |
| `ORG_TASK_LOG_ID` | [MIC_STAT_TASK](MIC_STAT_TASK.md) | `TASK_LOG_ID` |
| `TASK_LOG_ID` | [MIC_STAT_TASK](MIC_STAT_TASK.md) | `TASK_LOG_ID` |

