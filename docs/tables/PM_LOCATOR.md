# PM_LOCATOR

> This table stores information used to locate patients.

**Description:** Person Managemetn Locator table  
**Table type:** ACTIVITY  
**Primary key:** _(not published — see note)_  
**Columns:** 13

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ENCNTR_ID` | DOUBLE | NOT NULL | FK→ | This is the value of the unique primary identifier of the encounter table. It is an internal system assigned number. |
| 2 | `LOCATOR_ID` | DOUBLE | NOT NULL |  | This is the primary key for this table. It is a numeric value. |
| 3 | `NAME_FIRST_KEY` | VARCHAR(100) |  |  | This is the person's first given name all capitals with punctuation removed. This field is used for indexing and searching for a person by name. |
| 4 | `NAME_FIRST_KEY_A_NLS` | VARCHAR(400) |  |  | NAME_FIRST_KEY_A_NLS column |
| 5 | `NAME_FIRST_KEY_NLS` | VARCHAR(202) |  |  | First Name Key field converted to NLS format for internationalization requirements. |
| 6 | `NAME_LAST_KEY` | VARCHAR(100) |  |  | This is the person's last name all capitals with punctuation removed. This field is used for indexing and searching for a person by name. |
| 7 | `NAME_LAST_KEY_A_NLS` | VARCHAR(400) |  |  | NAME_LAST_KEY_A_NLS column |
| 8 | `NAME_LAST_KEY_NLS` | VARCHAR(202) |  |  | Last Name Key field converted to NLS format for internationalization requirements. |
| 9 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 10 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 11 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 12 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 13 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `ENCNTR_ID` | [ENCOUNTER](ENCOUNTER.md) | `ENCNTR_ID` |

