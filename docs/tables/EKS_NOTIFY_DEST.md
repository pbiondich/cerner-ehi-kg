# EKS_NOTIFY_DEST

> Holds the tcp/ip:port addresses of discern notify clients interested in messages routed to their specifc locations.

**Description:** This table holds the tcp/ip:port addresses of discern notify clients  
**Table type:** ACTIVITY  
**Primary key:** _(not published — see note)_  
**Columns:** 10

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `APP_VERSION_NBR` | DOUBLE | NOT NULL |  | The version of the packed DiscernNotify message structuree to use. |
| 2 | `LOCATION` | VARCHAR(100) | NOT NULL |  | The location defined in the registry of the PC interested in receiving notifications. |
| 3 | `PERSON_ID` | DOUBLE |  |  | This is the value of the unique primary identifier of the person table. It is an internal system assigned number. |
| 4 | `TCP_IP_ADDR` | VARCHAR(100) | NOT NULL |  | The TCP/IP address of the location interested in notifications. |
| 5 | `TCP_IP_PORT` | DOUBLE |  |  | TCP Port that the notification client is listening on. |
| 6 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 7 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 8 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 9 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 10 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

