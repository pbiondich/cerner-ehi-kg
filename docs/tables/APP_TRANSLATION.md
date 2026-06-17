# APP_TRANSLATION

> This table stores translations for captions used in CCL reports.

**Description:** APPLICATION TRANSLATION  
**Table type:** REFERENCE  
**Primary key:** _(not published — see note)_  
**Columns:** 10

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `APP_LANGUAGE_CD` | DOUBLE | NOT NULL | FK→ | Codified Value specifying the language for this translation. |
| 2 | `APP_NAME` | VARCHAR(100) |  |  | The name of the application (CCL Report) associated with this translation. |
| 3 | `CAPTION` | VARCHAR(255) |  |  | The translated text for the item. |
| 4 | `KEY_NAME` | VARCHAR(100) |  |  | A unique key value identifying each distinct string within an application. |
| 5 | `TRANSLATION_ID` | DOUBLE | NOT NULL |  | Primary Key |
| 6 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 7 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 8 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 9 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 10 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `APP_LANGUAGE_CD` | [CODE_VALUE](CODE_VALUE.md) | `CODE_VALUE` |

