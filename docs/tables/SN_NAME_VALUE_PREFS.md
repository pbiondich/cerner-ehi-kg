# SN_NAME_VALUE_PREFS

> SurgiNet Name Value Preferences Table

**Description:** SurgiNet Name Value Preferences  
**Table type:** REFERENCE  
**Primary key:** _(not published — see note)_  
**Columns:** 10

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `NAME_VALUE_PREFS_ID` | DOUBLE | NOT NULL |  | Unique ID for the Table |
| 2 | `PARENT_ENTITY_ID` | DOUBLE | NOT NULL |  | The ID from the table specified in PAREN_ENTITY_NAME |
| 3 | `PARENT_ENTITY_NAME` | VARCHAR(32) | NOT NULL |  | The Table that this row is a child of |
| 4 | `PREF_NAME` | VARCHAR(32) | NOT NULL |  | The Preference NameColumn |
| 5 | `PREF_VALUE` | VARCHAR(255) |  |  | The Prefernece Value |
| 6 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 7 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 8 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 9 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 10 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

