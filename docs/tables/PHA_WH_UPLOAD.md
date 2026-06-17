# PHA_WH_UPLOAD

> Stores cost update information from wholesalers.

**Description:** Wholesaler cost update information  
**Table type:** ACTIVITY  
**Primary key:** _(not published — see note)_  
**Columns:** 13

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ACTIVE_IND` | DOUBLE | NOT NULL |  | The table row is active or inactive. A row is generally active unless it is in an inactive state such as logically deleted, combined away, pending purge, etc. |
| 2 | `COST` | DOUBLE |  |  | Udated wholesaler cost |
| 3 | `COST_BASIS_CD` | DOUBLE | NOT NULL |  | Cost field that this cost will be used to update (AWP, Cost1,Cost2...). |
| 4 | `DRUG_IDENTIFIER` | VARCHAR(255) | NOT NULL |  | Drug identifier |
| 5 | `PHA_WH_UPLOAD_ID` | DOUBLE | NOT NULL |  | Primary key to uniquely identify each row. |
| 6 | `POST_DT_TM` | DATETIME |  |  | Date and time this cost was used to update the Manufacturer_item table |
| 7 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 8 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 9 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 10 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 11 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |
| 12 | `UPLOAD_DT_TM` | DATETIME | NOT NULL |  | Date and time this information was originally loaded into the table. |
| 13 | `WH_FORMAT_CD` | DOUBLE | NOT NULL |  | Indicates which wholesaler format was used to load this data. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

