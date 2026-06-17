# NOTE_PHRASE

> The purpose of this table is to information about user & system defined abbreviations that can be used to automatically insert text (generated from user/system defined queries). This table will store the abbreviation and a brief description of what will be inserted. The NOTE_PHRASE_COMP table will store information about what queries need to be run.

**Description:** NOTE PHRASE  
**Table type:** REFERENCE  
**Primary key:** `NOTE_PHRASE_ID`  
**Columns:** 9  
**Referenced by:** 3 columns

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ABBREVIATION` | VARCHAR(40) | NOT NULL |  | Shortcut text |
| 2 | `ABB_DESCRIPTION` | VARCHAR(255) |  |  | Brief description of what will be inserted in place of the abbreviation |
| 3 | `NOTE_PHRASE_ID` | DOUBLE | NOT NULL | PK | Unique Phrase ID |
| 4 | `PRSNL_ID` | DOUBLE | NOT NULL | FK→ | ID of user that owns this abbreviation. The system owns abbreviations where this ID is 0. |
| 5 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 6 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 7 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 8 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 9 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `PRSNL_ID` | [PRSNL](PRSNL.md) | `PERSON_ID` |

## Referenced by (3)

| From table | Column |
|------------|--------|
| [NOTE_PHRASE_COMP](NOTE_PHRASE_COMP.md) | `NOTE_PHRASE_ID` |
| [NOTE_PHRASE_FAVORITE](NOTE_PHRASE_FAVORITE.md) | `NOTE_PHRASE_ID` |
| [NOTE_PHRASE_LABEL](NOTE_PHRASE_LABEL.md) | `NOTE_PHRASE_ID` |

