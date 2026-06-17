# SI_EPA_LOG

> Log of various elements of the request initiation and response so that it can be accessed for use in subsequent transactions

**Description:** SI Electronic Prior Authorization Log  
**Table type:** ACTIVITY  
**Primary key:** _(not published — see note)_  
**Columns:** 15

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ACTIVE_IND` | DOUBLE | NOT NULL |  | The table row is active or inactive. A row is generally active unless it is in an inactive state such as logically deleted, combined away, pending purge, etc. |
| 2 | `CAMM_IDENT` | VARCHAR(50) |  |  | Reference to an attached document in CAMM - this is a GUID field |
| 3 | `CASE_IDENT` | VARCHAR(35) |  |  | case identifier assigned by the payor. It must be echoed in all subsequent requests. |
| 4 | `CREATE_DT_TM` | DATETIME |  |  | Date/Time at which the row was originally written |
| 5 | `DEADLINE_FOR_REPLY` | VARCHAR(50) |  |  | This is an iso 8601 formatted date or date/time value. It must be echoed in subsequent requests in the exact same format. |
| 6 | `LONG_BLOB_ID` | DOUBLE | NOT NULL | FK→ | Link to row on long_blob table |
| 7 | `MESSAGE_IDENT` | VARCHAR(35) |  |  | Transaction message identifier |
| 8 | `MSG_TYPE_FLAG` | DOUBLE |  |  | Indicator of whether this is the echo from PAInitationRequest (1), or the question set from: PAInitationRequest (1), PAInitiationResponse (2), PAResponse(3), PARequest(4), PACancel (5), Error(6), Status(7), PACancelResponse(8), RetrospectivePA (9), RetrospectiveClaimed (10), RxChangeRequest (11), Retrospective PA Response (12) |
| 9 | `REFERENCE_IDENT` | VARCHAR(35) |  |  | UUID assigned by the prescribing system on the initial transaction used as a tracking identifier on all subsequent request and response transactions |
| 10 | `SI_EPA_LOG_ID` | DOUBLE | NOT NULL |  | PRIMARY KEY |
| 11 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 12 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 13 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 14 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 15 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `LONG_BLOB_ID` | [LONG_BLOB](LONG_BLOB.md) | `LONG_BLOB_ID` |

