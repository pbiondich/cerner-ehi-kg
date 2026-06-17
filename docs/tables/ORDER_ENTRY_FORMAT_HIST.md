# ORDER_ENTRY_FORMAT_HIST

> History- The format that will be associated to an orderable to identify the information to be captured at order time.

**Description:** ORDER ENTRY FORMAT -hist  
**Table type:** REFERENCE  
**Primary key:** _(not published — see note)_  
**Columns:** 13

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ACTION_DT_TM` | DATETIME |  |  | date and time when the Action (delete/update) was taken |
| 2 | `ACTION_TAKEN_TFLG` | VARCHAR(30) |  |  | The action taken by the user (delete/update) |
| 3 | `ACTION_TYPE_CD` | DOUBLE | NOT NULL |  | The action this format is built for. |
| 4 | `ACTION_USER_ID` | DOUBLE |  |  | user id of the person who took the action (delete/update) |
| 5 | `CATALOG_TYPE_CD` | DOUBLE | NOT NULL |  | The catalog type this format is built for. |
| 6 | `OE_FORMAT_ID` | DOUBLE | NOT NULL |  | The id for the format. |
| 7 | `OE_FORMAT_NAME` | VARCHAR(200) |  |  | The name of the format. |
| 8 | `ORDER_ENTRY_FORMAT_HIST_ID` | DOUBLE | NOT NULL |  | Primary Key |
| 9 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 10 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 11 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 12 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 13 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

