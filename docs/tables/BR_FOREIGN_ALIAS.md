# BR_FOREIGN_ALIAS

> Table to store foreign system alias values

**Description:** Bedrock Foreign Alias  
**Table type:** REFERENCE  
**Primary key:** _(not published — see note)_  
**Columns:** 16

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ACTIVITY_TYPE` | VARCHAR(40) | NOT NULL |  | The activity type associated to the order catalog item |
| 2 | `ALIAS_TYPE` | VARCHAR(50) | NOT NULL |  | Type of alias |
| 3 | `BR_FOREIGN_ALIAS_ID` | DOUBLE | NOT NULL |  | Unique id for each row |
| 4 | `CATALOG_TYPE` | VARCHAR(40) | NOT NULL |  | Catalog type for the alias |
| 5 | `FACILITY` | VARCHAR(40) | NOT NULL |  | Name of the foreign system facility |
| 6 | `INBOUND_ALIAS` | VARCHAR(255) | NOT NULL |  | Foreign system inbound alias value |
| 7 | `INTERFACE_NAME` | VARCHAR(40) | NOT NULL |  | Name of the foreign system interface |
| 8 | `LONG_NAME` | VARCHAR(100) | NOT NULL |  | Long name of the alias |
| 9 | `MATCH_IND` | DOUBLE | NOT NULL |  | Indicates if a match has been made |
| 10 | `OUTBOUND_ALIAS` | VARCHAR(255) | NOT NULL |  | Foreign system outbound alias value |
| 11 | `SHORT_NAME` | VARCHAR(100) | NOT NULL |  | Short name of the alias |
| 12 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 13 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 14 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 15 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 16 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

