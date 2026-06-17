# MLLD_MS_NDC_COST

> This table is a staging table used to help facilitate the MLTM tables load process. It is not intended for client use or use by any other process.

**Description:** MLLD_MS_NDC_COST  
**Table type:** REFERENCE  
**Primary key:** _(not published — see note)_  
**Columns:** 9

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `MS_COST` | DOUBLE | NOT NULL |  | A specific cost for a medical supply. There is one cost stored for each inventory type, so it is possible to maintain separate price information for each inventory type. |
| 2 | `MS_INVENTORY_TYPE` | VARCHAR(5) | NOT NULL |  | This field designates the pricing description for the product: A - Average Wholesale Price, F - Federal Upper Limit Cost, M - Manufacturer Direct Price, W - Average Wholesale Cost |
| 3 | `MS_NDC_CODE` | VARCHAR(11) | NOT NULL |  | The National Drug Code is the standard 11 digit identifier for each drug product, as recognized by HCFA, other federal and state agencies, and many commercial enterprises. It is unique to each specific product. The first 5 numbers identify the manufacturer of a product. The second 4 numbers identify the product, and the last 2 numbers identify the package size of that product. |
| 4 | `TIME_STAMP` | DATETIME | NOT NULL |  | This field contains the Time/Date when each cost record was added to Multum's databases. If the record was added at 12:00 am, the time stamp will be blank and only the date stamp will appear. |
| 5 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 6 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 7 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 8 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 9 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

