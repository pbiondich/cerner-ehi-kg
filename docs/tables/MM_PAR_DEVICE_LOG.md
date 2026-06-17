# MM_PAR_DEVICE_LOG

> Log information for the device, user and route.

**Description:** MM PAR DEVICE LOG  
**Table type:** ACTIVITY  
**Primary key:** `PAR_DEVICE_LOG_ID`  
**Columns:** 15  
**Referenced by:** 1 columns

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `CHECK_IN_DT_TM` | DATETIME |  |  | The date/time the user checked the device in. |
| 2 | `CHECK_OUT_DT_TM` | DATETIME |  |  | The date/time the user checked the device out. |
| 3 | `CREATE_APPLCTX` | DOUBLE |  |  | Application which created this row |
| 4 | `CREATE_DT_TM` | DATETIME |  |  | The date/time this entry was created. |
| 5 | `CREATE_ID` | DOUBLE | NOT NULL |  | ID of user who created this row |
| 6 | `CREATE_TASK` | DOUBLE |  |  | Task which created this row |
| 7 | `DEVICE_CD` | DOUBLE | NOT NULL |  | The device used to do the par counting for this route. |
| 8 | `PAR_DEVICE_LOG_ID` | DOUBLE | NOT NULL | PK | The unique id for this device log. |
| 9 | `PAR_ROUTE_ID` | DOUBLE | NOT NULL |  | The unique identifier for the route. |
| 10 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 11 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 12 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 13 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 14 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |
| 15 | `USER_ID` | DOUBLE | NOT NULL |  | The unique id of the person who is using the device on a route. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Referenced by (1)

| From table | Column |
|------------|--------|
| [MM_PAR_ROUTE_LOG](MM_PAR_ROUTE_LOG.md) | `PAR_DEVICE_LOG_ID` |

