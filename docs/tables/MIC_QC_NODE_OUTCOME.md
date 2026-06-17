# MIC_QC_NODE_OUTCOME

> This reference table contains outcomes that will occur when the defined rules fail or succeed the parent schedule.

**Description:** Microbiology Quality Control Node Outcome  
**Table type:** REFERENCE  
**Primary key:** _(not published — see note)_  
**Columns:** 16

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ACTION_STATUS_CD` | DOUBLE | NOT NULL |  | This field contains the internal identification code for the lot status change associated with the outcome. |
| 2 | `ACTION_TEXT_ID` | DOUBLE | NOT NULL | FK→ | This field contains the internal identification code to the LONG_TEXT row, which contains a textual value for a corrective action. |
| 3 | `ACTIVE_IND` | DOUBLE | NOT NULL |  | The table row is active or inactive. A row is generally active unless it is in an inactive state such as logically deleted, combined away, pending purge, etc. |
| 4 | `ACTIVE_STATUS_CD` | DOUBLE | NOT NULL |  | Indicates the status of the row itself (not the data in the row) such as active, inactive, combined away, pending purge, etc. |
| 5 | `ACTIVE_STATUS_DT_TM` | DATETIME | NOT NULL |  | The date and time that the active_status_cd was set. |
| 6 | `ACTIVE_STATUS_PRSNL_ID` | DOUBLE | NOT NULL |  | The person who caused the active_status_cd to be set or change. |
| 7 | `NODE_ID` | DOUBLE | NOT NULL |  | This field contains the internal identification code to the parent MIC_QC_NODE table. |
| 8 | `OUTCOME_ID` | DOUBLE | NOT NULL |  | This field contains the internal identification code that uniquely identifies the schedule node outcome. |
| 9 | `OUTCOME_TYPE_FLAG` | DOUBLE | NOT NULL |  | This field is used to identify the type of outcome. |
| 10 | `TARGET_NODE_ID` | DOUBLE | NOT NULL |  | This field contains the internal identification code to the parent MIC_QC_NODE row of the schedule that should be executed as a result of the outcome of the current schedule. |
| 11 | `UNSUCCESSFUL_IND` | DOUBLE | NOT NULL |  | This field indicates whether the outcome should be displayed if the corresponding rule fails or succeeds. |
| 12 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 13 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 14 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 15 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 16 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `ACTION_TEXT_ID` | [LONG_TEXT](LONG_TEXT.md) | `LONG_TEXT_ID` |

