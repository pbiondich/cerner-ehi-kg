# MM_PAR_ROUTE_LOG

> Log information about the route and locations visited.

**Description:** MM PAR ROUTE LOG  
**Table type:** ACTIVITY  
**Primary key:** _(not published — see note)_  
**Columns:** 14

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `CREATE_APPLCTX` | DOUBLE |  |  | Application which created this row |
| 2 | `CREATE_DT_TM` | DATETIME |  |  | The date/time this entry was created. |
| 3 | `CREATE_ID` | DOUBLE | NOT NULL |  | ID of user who created this row |
| 4 | `CREATE_TASK` | DOUBLE |  |  | Task which created this row |
| 5 | `END_DT_TM` | DATETIME |  |  | The date/time the last item at the asset location on the route was counted. |
| 6 | `LOCATION_CD` | DOUBLE | NOT NULL |  | The unique id of the asset location on the route. |
| 7 | `PAR_DEVICE_LOG_ID` | DOUBLE | NOT NULL | FK→ | The unique device log id associated with the routes asset locations. |
| 8 | `PAR_ROUTE_LOG_ID` | DOUBLE | NOT NULL |  | The unique id of this entry. |
| 9 | `START_DT_TM` | DATETIME |  |  | The date/time the first item at the asset location is displayed. |
| 10 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 11 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 12 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 13 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 14 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `PAR_DEVICE_LOG_ID` | [MM_PAR_DEVICE_LOG](MM_PAR_DEVICE_LOG.md) | `PAR_DEVICE_LOG_ID` |

