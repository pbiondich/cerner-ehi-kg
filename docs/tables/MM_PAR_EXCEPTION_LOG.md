# MM_PAR_EXCEPTION_LOG

> Log information for exceptions on a route.

**Description:** MM PAR EXCEPTION LOG  
**Table type:** ACTIVITY  
**Primary key:** _(not published — see note)_  
**Columns:** 15

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `CREATE_APPLCTX` | DOUBLE |  |  | Application which created this row |
| 2 | `CREATE_DT_TM` | DATETIME |  |  | The date/time this entry was created. |
| 3 | `CREATE_ID` | DOUBLE | NOT NULL |  | ID of user who created this row |
| 4 | `CREATE_TASK` | DOUBLE |  |  | Task which created this row |
| 5 | `EXCEPTION_FLAG` | DOUBLE |  |  | The exception type of this entry. |
| 6 | `ITEM_ID` | DOUBLE | NOT NULL |  | The unique id for the item master. |
| 7 | `LOCATION_CD` | DOUBLE | NOT NULL |  | The unique id of the asset location where the exception occurred. |
| 8 | `PAR_EXCEPTION_LOG_ID` | DOUBLE | NOT NULL |  | The unique id of this exception entry. |
| 9 | `PAR_ROUTE_LOG_ID` | DOUBLE | NOT NULL |  | The unique id on which route log this exception occurred. |
| 10 | `PKG_TYPE_ID` | DOUBLE | NOT NULL |  | The unique id for the package type for this exception. |
| 11 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 12 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 13 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 14 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 15 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

