# RCA_REG_ACTION_ITEM

> This table will represent launch items that can be associated to a registration action.

**Description:** Revenue Cycle Ambulatory - Registration Action Launch Item  
**Table type:** REFERENCE  
**Primary key:** _(not published — see note)_  
**Columns:** 9

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `LAUNCH_ITEM_CD` | DOUBLE | NOT NULL |  | Identifies the type of launch item |
| 2 | `PRIORITY_SEQ` | DOUBLE | NOT NULL |  | The priority of this launch item in relation to other launch items associated to the same registration action. |
| 3 | `RCA_REG_ACTION_ID` | DOUBLE | NOT NULL | FK→ | Uniquely identifies the related row on the RCA_REG_ACTION table. |
| 4 | `RCA_REG_ACTION_ITEM_ID` | DOUBLE | NOT NULL |  | System generated number to uniquely identify a row on the RCA_REG_ACTION_ITEM table. |
| 5 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 6 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 7 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 8 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 9 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `RCA_REG_ACTION_ID` | [RCA_REG_ACTION](RCA_REG_ACTION.md) | `RCA_REG_ACTION_ID` |

