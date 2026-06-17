# MM_INSTANCE_TRANS_LINE_R

> In MM_INSTANCE, the user can dispense the equipment master item with its serial number. This table can track all items that are dispensed with the serial number so it maintains the relationship between MM_INSTANCE and MM_TRANS_LINE.

**Description:** Instance Trans Line Relation  
**Table type:** ACTIVITY  
**Primary key:** _(not published — see note)_  
**Columns:** 8

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `MM_INSTANCE_ID` | DOUBLE | NOT NULL | FK→ | The Instance that is related to this MM_TRANS_LINE row. |
| 2 | `MM_INSTANCE_TRANS_LINE_R_ID` | DOUBLE | NOT NULL |  | Unique, generated number that identifies a single row on the MM_INSTANCE_TRANS_LINE_R table. |
| 3 | `MM_TRANS_LINE_ID` | DOUBLE | NOT NULL | FK→ | Identifies the row on MM_TRANS_LINE that is associated to this MM_INSTANCE value. |
| 4 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 5 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 6 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 7 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 8 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `MM_INSTANCE_ID` | [MM_INSTANCE](MM_INSTANCE.md) | `MM_INSTANCE_ID` |
| `MM_TRANS_LINE_ID` | [MM_TRANS_LINE](MM_TRANS_LINE.md) | `MM_TRANS_LINE_ID` |

