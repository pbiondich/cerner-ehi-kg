# MM_PAR_ROUTE

> Information about the route.

**Description:** MM PAR ROUTE  
**Table type:** REFERENCE  
**Primary key:** _(not published — see note)_  
**Columns:** 18

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `CREATE_APPLCTX` | DOUBLE |  |  | Application which created this row |
| 2 | `CREATE_DT_TM` | DATETIME |  |  | The date/time this entry was created. |
| 3 | `CREATE_ID` | DOUBLE | NOT NULL |  | ID of user who created this row |
| 4 | `CREATE_TASK` | DOUBLE |  |  | Task which created this row |
| 5 | `DEF_REPL_WINDOW` | DOUBLE |  |  | The default amount of hours which must pass before an asset location may be counted again. This value may be overridden by at a specific asset location. |
| 6 | `FACILITY_CD` | DOUBLE | NOT NULL |  | The unique id of the facility. |
| 7 | `OPEN_LOC_EX_PRINTER` | VARCHAR(60) |  |  | The printer que where the open location exception reports will print. |
| 8 | `PAR_ROUTE_ID` | DOUBLE | NOT NULL |  | The unique id of an entry on this table. |
| 9 | `PICK_LIST_PRINTER` | VARCHAR(60) |  |  | The printer que where the pick list will print. |
| 10 | `QOH_EX_PRINTER` | VARCHAR(60) |  |  | The printer que where the stock out exception will print. |
| 11 | `ROOT_LOC_CD` | DOUBLE | NOT NULL |  | The inventory view for this route. |
| 12 | `ROUTE_DESC` | VARCHAR(100) |  |  | The description of the route. |
| 13 | `UOM_EX_PRINTER` | VARCHAR(60) |  |  | The printer que where unit of measure change exceptions will print. |
| 14 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 15 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 16 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 17 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 18 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

