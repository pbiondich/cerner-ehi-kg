# IMMUNIZATION_AUDIT

> This table stores immunization audit events

**Description:** IMMUNIZATION AUDIT  
**Table type:** ACTIVITY  
**Primary key:** _(not published — see note)_  
**Columns:** 14

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `EVENT_ID` | DOUBLE |  |  | This would be an event_id from clinical_event table. This will be useful piece of detail when capturing the audit event using the Lights on timers network. This would be only numerical value of double data type.; |
| 2 | `EVENT_TYPE_TFLG` | VARCHAR(40) |  |  | This would specify what kind of event this particular audit event is for. For example, if it is immunization administration or query for the registry etc. This column needs to be a flag. The possible values could be 'ADMIN_SUB_RES' or 'IIS_QUERY'. |
| 3 | `IMMUNIZATION_AUDIT_ID` | DOUBLE | NOT NULL |  | PRIMARY KEY |
| 4 | `MESSAGE_SENT_DT_TM` | DATETIME |  |  | The Date and Time the message was sent |
| 5 | `PERSON_ID` | DOUBLE |  | FK→ | This would be a person_id (foreign key) from the person table. This would be useful for the clients for reporting for the audit events of type queries. This would be only numerical value of double data type.; |
| 6 | `REGISTRY_IDENT` | VARCHAR(255) |  |  | This would be a unique identifier that identies a particular Immunization registry (i.e. IIS stands for Immunization Information System). FSI would be sending all this data. This detail will be captured as metadata on lights on so they could be sorted by IIS. |
| 7 | `RESPONSE_STATUS_DT_TM` | DATETIME |  |  | This is the date and time when an acknowledgement came back from IIS (Immunization registry) for the message sent earlier by FSI. As per FSI, it would always be in UTC. There will be some scenarios when the acknowledgement is lost (never received). |
| 8 | `RESPONSE_STATUS_TFLG` | VARCHAR(30) |  |  | This would specify what kind of response (or acknowledgement) was received for this particular audit event from IIS (Immunization Information System). For example, if it is successful or some kind of error. This column needs to be a flag. The possible values could be 'NO_RESPONSE' or 'ADMIN_SUB_SUCCESS'. |
| 9 | `TRANSACTION_IDENT` | VARCHAR(50) |  |  | This would be a unique identifier that could be used the table lookups and then populate some of the missing fields later. FSI would be sending this value as their trigger id (a double value), appended with a fully qualified domain name and separated by some delimeter like colon, for example, ipmdvla.ip.devcerner.net:7592922910 for mdvla (dev) domain.; |
| 10 | `UPDT_APPLCTX` | DOUBLE |  |  | The application context number from the record info block. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 11 | `UPDT_CNT` | DOUBLE |  |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 12 | `UPDT_DT_TM` | DATETIME |  |  | The date and time the row was last inserted or updated. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 13 | `UPDT_ID` | DOUBLE |  |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 14 | `UPDT_TASK` | DOUBLE |  |  | The registered (assigned) task number for the process that inserted or updated the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `PERSON_ID` | [PERSON](PERSON.md) | `PERSON_ID` |

