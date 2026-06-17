# RXA_SERVICE

> Stores parameters for retail application services.

**Description:** PharmNet Ambulatory Service  
**Table type:** ACTIVITY  
**Primary key:** _(not published — see note)_  
**Columns:** 13

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ACCOUNT_TXT` | VARCHAR(255) |  |  | Account number of the service. |
| 2 | `GROUPID_TXT` | VARCHAR(255) |  |  | Group ID of all the NABPs that this Service services. |
| 3 | `IP_TXT` | VARCHAR(255) |  |  | IP Address the Service connects to. |
| 4 | `NABP_TXT` | VARCHAR(255) |  |  | The name of the NABP(s) serviced by this Service. |
| 5 | `NAME_TXT` | VARCHAR(255) | NOT NULL |  | Name of the application service. |
| 6 | `PORT_TXT` | VARCHAR(255) |  |  | Port the service connects to. |
| 7 | `PROTOCOL_TXT` | VARCHAR(255) |  |  | Protocol the service connects to. |
| 8 | `RXA_SERVICE_ID` | DOUBLE | NOT NULL |  | Unique, generated number that identifies a single row on the RXA_SERVICE table. |
| 9 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 10 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 11 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 12 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 13 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

