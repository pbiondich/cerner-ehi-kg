# OMF_CFGRN_ITEM

> Items used to drive dynamic configuration/preference settings.

**Description:** OMF Configuration Item  
**Table type:** REFERENCE  
**Primary key:** `CFGRN_ITEM_ID`  
**Columns:** 13  
**Referenced by:** 2 columns

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `CFGRN_ITEM_ID` | DOUBLE | NOT NULL | PK | The system assigned unique value for the item. |
| 2 | `CFGRN_SECT_ID` | DOUBLE | NOT NULL | FK→ | The system assigned value of the item's parent section_id. |
| 3 | `DFLT_OPT_VALUE_TXT` | VARCHAR(255) |  |  | The item's default unique value setting. |
| 4 | `EPILOG_MSG_TXT` | VARCHAR(255) |  |  | Provides a message to the end user after a change has been made. |
| 5 | `FILTER_MEANING` | VARCHAR(50) |  | FK→ | The filter meaning associated with the configuration item. |
| 6 | `ITEM_DESC_TXT` | VARCHAR(255) | NOT NULL |  | The description of the item that will be displayed in the application. |
| 7 | `ITEM_NAME_TXT` | VARCHAR(255) | NOT NULL |  | The unique description of the item. |
| 8 | `OPT_TYPE_FLAG` | DOUBLE | NOT NULL |  | The type of option associated with the configuration item. |
| 9 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 10 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 11 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 12 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 13 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `CFGRN_SECT_ID` | [OMF_CFGRN_SECT](OMF_CFGRN_SECT.md) | `CFGRN_SECT_ID` |
| `FILTER_MEANING` | [OMF_FILTER_MEANING](OMF_FILTER_MEANING.md) | `FILTER_MEANING` |

## Referenced by (2)

| From table | Column |
|------------|--------|
| [OMF_CFGRN_ITEM_ACTN](OMF_CFGRN_ITEM_ACTN.md) | `CFGRN_ITEM_ID` |
| [OMF_CFGRN_ITEM_SETNG](OMF_CFGRN_ITEM_SETNG.md) | `CFGRN_ITEM_ID` |

