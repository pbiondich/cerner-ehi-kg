# ONC_DOCSETREF_CAT

> Stores categories for Doc Set Ref values

**Description:** Oncology DocsetRef Category  
**Table type:** REFERENCE  
**Primary key:** `ONC_DOCSETREF_CAT_ID`  
**Columns:** 11  
**Referenced by:** 2 columns

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `CATEGORY_DISPLAY` | VARCHAR(40) | NOT NULL |  | Category Display Name |
| 2 | `CATEGORY_DISPLAY_KEY` | VARCHAR(40) | NOT NULL |  | Defines the Key to the category display name |
| 3 | `IN_USE_IND` | DOUBLE | NOT NULL |  | used to filter out onc_docsetref_cat records that are no longer being unused. |
| 4 | `ONC_DOCSETREF_CAT_ID` | DOUBLE | NOT NULL | PK | Primary key. An internal system assigned number. |
| 5 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 6 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 7 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 8 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 9 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |
| 10 | `VALID_FROM_DT_TM` | DATETIME | NOT NULL |  | The date and time for which this category becomes effective. This is not the time that the row was created. |
| 11 | `VALID_UNTIL_DT_TM` | DATETIME | NOT NULL |  | The date and time after which the category is no longer valid. This is not the time that the row will become inactive. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Referenced by (2)

| From table | Column |
|------------|--------|
| [ONC_DOCSETREF_CAT_R](ONC_DOCSETREF_CAT_R.md) | `ONC_DOCSETREF_CAT_ID` |
| [ONC_FORM_ACTIVITY](ONC_FORM_ACTIVITY.md) | `ONC_DOCSETREF_CAT_ID` |

