# PAT_ED_SHORTCUT

> The table will store the shortcut names of each relation id (instruction)

**Description:** Patient Education Shortcut  
**Table type:** REFERENCE  
**Primary key:** _(not published — see note)_  
**Columns:** 9

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `PAT_ED_RELTN_ID` | DOUBLE | NOT NULL | FK→ | Relation Id that relates to the pat_ed_reltn table on which instruction this row is. |
| 2 | `PAT_ED_SHORTCUT_ID` | DOUBLE | NOT NULL |  | Primary key |
| 3 | `SHORTCUT_NAME` | VARCHAR(1000) |  |  | This is storing a shortcut name of an instruction that is given by the content domain. |
| 4 | `SHORTCUT_NAME_KEY` | VARCHAR(1000) | NOT NULL |  | Displays the shortcut name with only alpha characters and all uppercase |
| 5 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 6 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 7 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 8 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 9 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `PAT_ED_RELTN_ID` | [PAT_ED_RELTN](PAT_ED_RELTN.md) | `PAT_ED_RELTN_ID` |

