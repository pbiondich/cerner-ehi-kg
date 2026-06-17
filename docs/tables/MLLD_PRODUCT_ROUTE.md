# MLLD_PRODUCT_ROUTE

> This table is a staging table used to help facilitate the MLTM tables load process. It is not intended for client use or use by any other process.

**Description:** MLLD_PRODUCT_ROUTE  
**Table type:** REFERENCE  
**Primary key:** _(not published — see note)_  
**Columns:** 9

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ROUTE_ABBR` | VARCHAR(30) |  |  | This field contains abbreviations for the various routes of administration. |
| 2 | `ROUTE_CD` | DOUBLE | NOT NULL |  | ROUTE CODE |
| 3 | `ROUTE_CODE` | DOUBLE | NOT NULL |  | This field contains a unique code for each route of administration. |
| 4 | `ROUTE_DESCRIPTION` | VARCHAR(30) |  |  | This field contains textual descriptions of the various routes of administration or product routes. |
| 5 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 6 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 7 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 8 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 9 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

