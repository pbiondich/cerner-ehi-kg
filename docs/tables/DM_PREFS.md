# DM_PREFS

> This table is used to store user rows and user preferences

**Description:** DM PREFS  
**Table type:** REFERENCE  
**Primary key:** _(not published — see note)_  
**Columns:** 18

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `APPLICATION_NBR` | DOUBLE | NOT NULL |  | The number of the application with the init parameters in this row. |
| 2 | `PARENT_ENTITY_ID` | DOUBLE | NOT NULL |  | Used to store the identifier for the parent |
| 3 | `PARENT_ENTITY_NAME` | VARCHAR(32) |  |  | Used to store the name for the parent |
| 4 | `PERSON_ID` | DOUBLE | NOT NULL | FK→ | This is the value of the unique primary identifier of the person table. It is an internal system assigned number. |
| 5 | `PREF_CD` | DOUBLE | NOT NULL |  | Used to store the value part of the name value pair when the value portion is code value from the code set |
| 6 | `PREF_DOMAIN` | VARCHAR(255) | NOT NULL |  | The domain for the name value pair. |
| 7 | `PREF_DT_TM` | DATETIME |  |  | Used to store the value part of the name value pair when the value portion is a date. |
| 8 | `PREF_ID` | DOUBLE | NOT NULL |  | To uniquely define a row in the table |
| 9 | `PREF_NAME` | VARCHAR(255) | NOT NULL |  | The name portion of the name value pair |
| 10 | `PREF_NBR` | DOUBLE |  |  | Used to store the value part of the name value pair when the value portion is a number. |
| 11 | `PREF_SECTION` | VARCHAR(255) | NOT NULL |  | The section for the name value pair. |
| 12 | `PREF_STR` | VARCHAR(255) |  |  | Used to store the value part of the name value pair when the value portion is a character string. |
| 13 | `REFERENCE_IND` | DOUBLE |  |  | Specifies if this is row is reference = 1 or activity = 0 |
| 14 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 15 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 16 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 17 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 18 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `PERSON_ID` | [PRSNL](PRSNL.md) | `PERSON_ID` |

