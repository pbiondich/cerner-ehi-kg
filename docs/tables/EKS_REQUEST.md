# EKS_REQUEST

> Maps CSA requests to EKS event numbers

**Description:** Discern Expert list of incoming requests to event map  
**Table type:** REFERENCE  
**Primary key:** _(not published — see note)_  
**Columns:** 13

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ACTIVE_IND` | DOUBLE |  |  | The table row is active or inactive. A row is generally active unless it is in an inactive state such as logically deleted, combined away, pending purge, etc. |
| 2 | `DOMAIN` | VARCHAR(40) | NOT NULL |  | Should always be set to "CERT" -- will be phased out in the future. |
| 3 | `EVENT_NUMBER` | DOUBLE | NOT NULL |  | The event number of the event being mapped to a request by this record. |
| 4 | `FORMAT_SCRIPT` | CHAR(30) |  |  | Format script used by the process server to format request |
| 5 | `REQUEST_NUMBER` | DOUBLE | NOT NULL |  | The request number of the request being mapped to an event by this record. |
| 6 | `REQUEST_TYPE` | CHAR(1) |  |  | Defines the type of request |
| 7 | `SERVER_TYPE` | CHAR(1) |  |  | The server type(s) that should load this mapping. valid types are: 'A' (ASYNC), 'S' (SYNC), or 'B' (BOTH). |
| 8 | `TARGET_REQUEST_NUMBER` | DOUBLE |  |  | Target request number used by the process server to format incoming request to this request |
| 9 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 10 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 11 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 12 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 13 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

