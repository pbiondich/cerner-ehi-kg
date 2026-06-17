# UCM_CASE_STEP

> This table stores high level case information.

**Description:** Unified Case Management Case Step  
**Table type:** ACTIVITY  
**Primary key:** `UCM_CASE_STEP_ID`  
**Columns:** 15  
**Referenced by:** 6 columns

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `CREATE_DT_TM` | DATETIME | NOT NULL |  | This field contains the date and time this row/record was created. |
| 2 | `LOCKED_IND` | DOUBLE |  |  | This field indicates if this case step is locked by another user. Use the UPDT fields to determine who and when the case step was locked. |
| 3 | `OPT_ADDON_CATALOG_CD` | DOUBLE | NOT NULL |  | Orderable for an optional case step that was added on to a case. |
| 4 | `ORDER_ID` | DOUBLE | NOT NULL | FK→ | This field is used to store the order that represents this case step. |
| 5 | `PARENT_UCM_CASE_STEP_ID` | DOUBLE | NOT NULL | FK→ | Indicates the parent case step of a specific case step. |
| 6 | `SPECIMEN_ORDER_ID` | DOUBLE | NOT NULL | FK→ | Used to store the order that represents the specimen order that created this case step. |
| 7 | `UCMR_CASE_STEP_ID` | DOUBLE | NOT NULL | FK→ | This field is used to store the reference case step this case step was built using. |
| 8 | `UCM_CASE_ID` | DOUBLE | NOT NULL | FK→ | This field contains the unique identifier for the case. |
| 9 | `UCM_CASE_STEP_ID` | DOUBLE | NOT NULL | PK | This field contains a unique identifier for the case step. |
| 10 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 11 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 12 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 13 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 14 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 15 | `VIEW_SEQ` | DOUBLE | NOT NULL |  | Identifies the sequence the case step within the case is to be viewed. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `ORDER_ID` | [ORDERS](ORDERS.md) | `ORDER_ID` |
| `PARENT_UCM_CASE_STEP_ID` | [UCM_CASE_STEP](UCM_CASE_STEP.md) | `UCM_CASE_STEP_ID` |
| `SPECIMEN_ORDER_ID` | [ORDERS](ORDERS.md) | `ORDER_ID` |
| `UCMR_CASE_STEP_ID` | [UCMR_CASE_STEP](UCMR_CASE_STEP.md) | `UCMR_CASE_STEP_ID` |
| `UCM_CASE_ID` | [UCM_CASE](UCM_CASE.md) | `UCM_CASE_ID` |

## Referenced by (6)

| From table | Column |
|------------|--------|
| [UCM_CASE_EVENT](UCM_CASE_EVENT.md) | `RELATED_CASE_STEP_ID` |
| [UCM_CASE_EVENT](UCM_CASE_EVENT.md) | `UCM_CASE_STEP_ID` |
| [UCM_CASE_INTEGRATION](UCM_CASE_INTEGRATION.md) | `UCM_CASE_STEP_ID` |
| [UCM_CASE_STEP](UCM_CASE_STEP.md) | `PARENT_UCM_CASE_STEP_ID` |
| [UCM_REQUIRED_STEP](UCM_REQUIRED_STEP.md) | `REQUIRED_UCM_CASE_STEP_ID` |
| [UCM_REQUIRED_STEP](UCM_REQUIRED_STEP.md) | `UCM_CASE_STEP_ID` |

