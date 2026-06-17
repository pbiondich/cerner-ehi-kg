# OMF_CFGRN_DOMN

> The domains associated with items used to drive dynamic configuration/preference settings.

**Description:** OMF Configuration Domain  
**Table type:** REFERENCE  
**Primary key:** `CFGRN_DOMN_ID`  
**Columns:** 8  
**Referenced by:** 1 columns

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `CFGRN_DOMN_ID` | DOUBLE | NOT NULL | PK | The system assigned unique value for the domain. |
| 2 | `DOMN_DESC_TXT` | VARCHAR(255) | NOT NULL |  | The description of the domain that will be displayed in the application. |
| 3 | `DOMN_NAME_TXT` | VARCHAR(255) | NOT NULL |  | The unique description of the domain. |
| 4 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 5 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 6 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 7 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 8 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Referenced by (1)

| From table | Column |
|------------|--------|
| [OMF_CFGRN_SECT](OMF_CFGRN_SECT.md) | `CFGRN_DOMN_ID` |

