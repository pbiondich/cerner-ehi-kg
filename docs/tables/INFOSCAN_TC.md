# INFOSCAN_TC

> InfoScan Therapeutic Class Table

**Description:** InfoScan Therapeutic Class  
**Table type:** REFERENCE  
**Primary key:** `THERAP_CLASS_IDENTIFIER`, `THERAP_SUB_CLASS_IDENTIFIER`  
**Columns:** 9  
**Referenced by:** 2 columns

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `THERAP_CLASS_DESC` | VARCHAR(80) |  |  | Therapeutic class descriptionColumn |
| 2 | `THERAP_CLASS_IDENTIFIER` | DOUBLE | NOT NULL | PK | Therapeutic class identifierColumn |
| 3 | `THERAP_SUB_CLASS_DESC` | VARCHAR(80) |  |  | Therapeutic sub class descriptionColumn |
| 4 | `THERAP_SUB_CLASS_IDENTIFIER` | DOUBLE | NOT NULL | PK | Therapeutic sub class identifierColumn |
| 5 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 6 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 7 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 8 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 9 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Referenced by (2)

| From table | Column |
|------------|--------|
| [INFOSCAN_PRODUCT](INFOSCAN_PRODUCT.md) | `THERAP_CLASS_IDENTIFIER` |
| [INFOSCAN_PRODUCT](INFOSCAN_PRODUCT.md) | `THERAP_SUB_CLASS_IDENTIFIER` |

