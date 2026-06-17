# MLTM_MS_CATEGORIES

> This table contains the descriptions for a more specific categorization of medical supplies.

**Description:** Multum Medical Supply Categories  
**Table type:** REFERENCE  
**Primary key:** `MS_CATEGORY_ID`  
**Columns:** 7  
**Referenced by:** 1 columns

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `MS_CATEGORY_ID` | DOUBLE | NOT NULL | PK | This field assigns a more specific category to a medical supply. |
| 2 | `MS_CATEGORY_NAME` | VARCHAR(100) | NOT NULL |  | This field provides a more specific textual description of the medical supply type. |
| 3 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 4 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 5 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 6 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 7 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Referenced by (1)

| From table | Column |
|------------|--------|
| [MLTM_MS_CORE_DESCRIPTION](MLTM_MS_CORE_DESCRIPTION.md) | `MS_CATEGORY_ID` |

