# INFOSCAN_NOTE

> Notes reference data for InfoScan data

**Description:** Infoscan notes  
**Table type:** REFERENCE  
**Primary key:** `NOTE_IDENTIFIER`  
**Columns:** 8  
**Referenced by:** 1 columns

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `NOTES` | VARCHAR(250) | NOT NULL |  | notes text |
| 2 | `NOTE_ADVISE_RESTRICT_IND` | DOUBLE |  |  | 1- Advisory 2- Restrictions |
| 3 | `NOTE_IDENTIFIER` | VARCHAR(10) | NOT NULL | PK | external identifier defined by infoscan |
| 4 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 5 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 6 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 7 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 8 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Referenced by (1)

| From table | Column |
|------------|--------|
| [INFOSCAN_PRODUCT](INFOSCAN_PRODUCT.md) | `NOTE_IDENTIFIER` |

