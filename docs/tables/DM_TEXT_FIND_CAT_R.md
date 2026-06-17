# DM_TEXT_FIND_CAT_R

> This table will store meta-data about the new Text Search tool owned by DM

**Description:** Database Management Text Find Category Relation  
**Table type:** REFERENCE  
**Primary key:** _(not published — see note)_  
**Columns:** 9

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ACTIVE_IND` | DOUBLE | NOT NULL |  | The table row is active or inactive. A row is generally active unless it is in an inactive state such as logically deleted, combined away, pending purge, etc. |
| 2 | `DM_TEXT_FIND_CAT_ID` | DOUBLE | NOT NULL | FK→ | Reference to the DM_TEXT_FIND_CAT table |
| 3 | `DM_TEXT_FIND_CAT_R_ID` | DOUBLE | NOT NULL |  | Primary Key for table |
| 4 | `DM_TEXT_FIND_ID` | DOUBLE | NOT NULL | FK→ | Reference to the DM_TEXT_FIND table |
| 5 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 6 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 7 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 8 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 9 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `DM_TEXT_FIND_CAT_ID` | [DM_TEXT_FIND_CAT](DM_TEXT_FIND_CAT.md) | `DM_TEXT_FIND_CAT_ID` |
| `DM_TEXT_FIND_ID` | [DM_TEXT_FIND](DM_TEXT_FIND.md) | `DM_TEXT_FIND_ID` |

