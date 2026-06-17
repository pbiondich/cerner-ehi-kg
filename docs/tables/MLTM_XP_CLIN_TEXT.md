# MLTM_XP_CLIN_TEXT

> This table provides a textual description of each clinical text section and includes a unique code for each description.

**Description:** Multum XP Clinical Text  
**Table type:** REFERENCE  
**Primary key:** `TEXT_ID`  
**Columns:** 9  
**Referenced by:** 1 columns

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `CLINICAL_TEXT` | VARCHAR(2000) |  |  | ** OBSOLETE** textual description of each clinical text section. No longer used due to size limitation. Has been replaced by the LONG_TEXT_ID FK column. |
| 2 | `CLIN_TEXT` | LONGTEXT |  |  | Textual description of each clinical text section. This column replaces and negates use of long_text_id column. |
| 3 | `LONG_TEXT_ID` | DOUBLE | NOT NULL | FK→ | ** OBSOLETE ** ID from the LONG_TEXT_REFERENCE table for the Clinical Text related to this row. Replaces the clinical_text column. ** THIS COLUMN IS REPLACED BY THE NEW CLIN_TEXT COLUMN (which will have a LONG data type). |
| 4 | `TEXT_ID` | DOUBLE | NOT NULL | PK | PK column. A unique code for each description. |
| 5 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 6 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 7 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 8 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 9 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `LONG_TEXT_ID` | [LONG_TEXT_REFERENCE](LONG_TEXT_REFERENCE.md) | `LONG_TEXT_ID` |

## Referenced by (1)

| From table | Column |
|------------|--------|
| [MLTM_XP_CLIN_TEXT_XREF](MLTM_XP_CLIN_TEXT_XREF.md) | `TEXT_ID` |

