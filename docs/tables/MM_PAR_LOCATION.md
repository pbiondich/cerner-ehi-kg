# MM_PAR_LOCATION

> Information about the asset locations on a route.

**Description:** MM PAR LOCATION  
**Table type:** REFERENCE  
**Primary key:** _(not published — see note)_  
**Columns:** 16

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `COUNT_ALL_IND` | DOUBLE |  |  | count all indicator |
| 2 | `CREATE_APPLCTX` | DOUBLE |  |  | Application which created this row |
| 3 | `CREATE_DT_TM` | DATETIME |  |  | The date/time this entry was created. |
| 4 | `CREATE_ID` | DOUBLE | NOT NULL |  | ID of user who created this row |
| 5 | `CREATE_TASK` | DOUBLE |  |  | Task which created this row |
| 6 | `LOCATION_CD` | DOUBLE | NOT NULL |  | The unique id of the asset location for a route. |
| 7 | `PAR_LOCATION_ID` | DOUBLE | NOT NULL |  | The unique id for an entry on this table. |
| 8 | `PAR_ROUTE_ID` | DOUBLE | NOT NULL |  | The unique id of the route. |
| 9 | `REPL_WINDOW` | DOUBLE |  |  | The number of hours that must pass before the asset location may be counted again. |
| 10 | `REQ_MODE_IND` | DOUBLE |  |  | The indicator will be used to determine if the quantity entered is the counted quantity (0) or the quantity to be requisitioned (1) |
| 11 | `SEQUENCE` | DOUBLE |  |  | The order in which the asset locations should be counted. |
| 12 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 13 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 14 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 15 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 16 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

