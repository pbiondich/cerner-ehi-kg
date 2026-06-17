# REPORT_INPROC_STATUS

> This reference table contains the associations between report order catalog items, report component procedures, and the in process status and cancelation options associated with those entries.

**Description:** Report Inprocess Status  
**Table type:** REFERENCE  
**Primary key:** _(not published — see note)_  
**Columns:** 11

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `CANCELABLE_IND` | DOUBLE |  |  | This field contains an indicator documenting whether or not a report that has achieved the associated status can be cancelled. |
| 2 | `CATALOG_CD` | DOUBLE | NOT NULL | FK→ | This field contains the foreign key value representing the order catalog item to which the report component procedures (discrete tasks) are associated. |
| 3 | `DICTATED_STATUS_CD` | DOUBLE | NOT NULL |  | This field is not used at this time. |
| 4 | `PROCESSING_SEQUENCE` | DOUBLE |  |  | This field contains a sequence value used to determine hierarchy if multiple report components have reached their associated statuses. If multiple components have been updated, this field determines which sequence takes precedence in display. |
| 5 | `TASK_ASSAY_CD` | DOUBLE | NOT NULL | FK→ | This field contains the foreign key value representing the report component procedure (discrete task) to which the in process status and parameters are defined. |
| 6 | `TRANSCRIBED_STATUS_CD` | DOUBLE | NOT NULL |  | This field is used to store the identification code of the transcribed status value. Report status codes are stored on codeset1305. |
| 7 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 8 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 9 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 10 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 11 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `CATALOG_CD` | [PROFILE_TASK_R](PROFILE_TASK_R.md) | `CATALOG_CD` |
| `TASK_ASSAY_CD` | [PROFILE_TASK_R](PROFILE_TASK_R.md) | `TASK_ASSAY_CD` |

