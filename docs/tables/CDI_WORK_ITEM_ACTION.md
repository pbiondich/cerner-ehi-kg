# CDI_WORK_ITEM_ACTION

> This table records actions taken while processing a work item.

**Description:** Work Item Action  
**Table type:** ACTIVITY  
**Primary key:** _(not published — see note)_  
**Columns:** 14

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ACTION_DT_TM` | DATETIME | NOT NULL |  | The date & time of the action represented by this row. |
| 2 | `ACTION_PRSNL_ID` | DOUBLE | NOT NULL | FK→ | The personnel ID of the user performing the action represented by this row. |
| 3 | `ACTION_TYPE_FLAG` | DOUBLE | NOT NULL |  | Flag indicating what type of action was performed. 0 - Patient Contact, 1 - Fax Out |
| 4 | `CDI_WORK_ITEM_ACTION_ID` | DOUBLE | NOT NULL |  | Unique generated number that identifies a single row on the CDI_WORK_ITEM_ACTION table. |
| 5 | `CDI_WORK_ITEM_ID` | DOUBLE | NOT NULL | FK→ | Foreign key to the work item table. |
| 6 | `COMMENT_CD` | DOUBLE | NOT NULL |  | Specifies any predefined comment selected by the user for this action. |
| 7 | `FOLLOW_UP_DT_TM` | DATETIME |  |  | The date & time of the follow up action represented by this row. |
| 8 | `LONG_TEXT_ID` | DOUBLE | NOT NULL | FK→ | Foreign key to the long_text table where the user entered comments are stored. |
| 9 | `OUTPUTCTX_HANDLE_ID` | DOUBLE | NOT NULL | FK→ | Identifies the output context for outbound fax actions (foreign key to the outputctx table) |
| 10 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 11 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 12 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 13 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 14 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `ACTION_PRSNL_ID` | [PRSNL](PRSNL.md) | `PERSON_ID` |
| `CDI_WORK_ITEM_ID` | [CDI_WORK_ITEM](CDI_WORK_ITEM.md) | `CDI_WORK_ITEM_ID` |
| `LONG_TEXT_ID` | [LONG_TEXT](LONG_TEXT.md) | `LONG_TEXT_ID` |
| `OUTPUTCTX_HANDLE_ID` | [OUTPUTCTX](OUTPUTCTX.md) | `HANDLE_ID` |

