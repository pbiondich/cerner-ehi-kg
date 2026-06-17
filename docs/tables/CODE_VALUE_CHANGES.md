# CODE_VALUE_CHANGES

> This table is to support tracking changes in CODE_VALUE and determining when Cache Refreshes need to be done. This table stores code values that have been deleted, inserted, or chaged. Data will be deleted after use.

**Description:** CODE VALUE CHANGES  
**Table type:** ACTIVITY  
**Primary key:** _(not published — see note)_  
**Columns:** 8

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `CODE_VALUE` | DOUBLE | NOT NULL |  | The code value affected by the change |
| 2 | `CODE_VALUE_CHANGES_ID` | DOUBLE | NOT NULL |  | Primary Key from Reference_Seq |
| 3 | `CODE_VALUE_NODE_ID` | DOUBLE | NOT NULL | FK→ | THE NODE ID FROM CODE_VALUE_NODE |
| 4 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 5 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 6 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 7 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 8 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `CODE_VALUE_NODE_ID` | [CODE_VALUE_NODE](CODE_VALUE_NODE.md) | `CODE_VALUE_NODE_ID` |

