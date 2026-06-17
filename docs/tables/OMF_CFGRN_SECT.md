# OMF_CFGRN_SECT

> The sections associated with items used to drive dynamic configuration/preference settings.

**Description:** OMF Configuration Section  
**Table type:** REFERENCE  
**Primary key:** `CFGRN_SECT_ID`  
**Columns:** 9  
**Referenced by:** 1 columns

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `CFGRN_DOMN_ID` | DOUBLE | NOT NULL | FK→ | The section's associated domain. |
| 2 | `CFGRN_SECT_ID` | DOUBLE | NOT NULL | PK | The system assigned unique value for the section. |
| 3 | `SECT_DESC_TXT` | VARCHAR(255) | NOT NULL |  | The description of the section that will be displayed in the application. |
| 4 | `SECT_NAME_TXT` | VARCHAR(255) | NOT NULL |  | The unique description of the section. |
| 5 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 6 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 7 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 8 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 9 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `CFGRN_DOMN_ID` | [OMF_CFGRN_DOMN](OMF_CFGRN_DOMN.md) | `CFGRN_DOMN_ID` |

## Referenced by (1)

| From table | Column |
|------------|--------|
| [OMF_CFGRN_ITEM](OMF_CFGRN_ITEM.md) | `CFGRN_SECT_ID` |

