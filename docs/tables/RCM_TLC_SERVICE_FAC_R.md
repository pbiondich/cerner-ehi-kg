# RCM_TLC_SERVICE_FAC_R

> Relates the TLC Service to the Facility

**Description:** RevWorks Care Management - Service Facility Relationship  
**Table type:** ACTIVITY  
**Primary key:** _(not published — see note)_  
**Columns:** 15

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `CANCEL_REASON_CD` | DOUBLE | NOT NULL |  | The reason for this service was cancelled |
| 2 | `DISCHARGE_PRSNL_ID` | DOUBLE | NOT NULL | FK→ | The discharge planner personnel identifier that initiated the post-acute referral. |
| 3 | `PRIORITY_SEQ` | DOUBLE | NOT NULL |  | Sequences the priority of this relationship relative to other service/facility relationships. |
| 4 | `RCM_TLC_FACILITY_ID` | DOUBLE | NOT NULL | FK→ | Uniquely identifies the related facility |
| 5 | `RCM_TLC_SERVICE_FAC_R_ID` | DOUBLE | NOT NULL |  | Uniquely identifies a relationship between the TLC service and facility. |
| 6 | `RCM_TLC_SERVICE_ID` | DOUBLE | NOT NULL | FK→ | Uniquely identifies the related service. |
| 7 | `REPORT_REQUEST_ID` | DOUBLE | NOT NULL | FK→ | Identifies the report sent to the facility. |
| 8 | `RESPONSE_CD` | DOUBLE | NOT NULL |  | This is the codified response. |
| 9 | `TLC_EVENT_TYPE_CD` | DOUBLE | NOT NULL |  | This is the codified event type such as, Send Referral, Send CLINICAL, RECEIVEDRESP, PLACEPATIENT, or SENDFAXFAIL |
| 10 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 11 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 12 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 13 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 14 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |
| 15 | `VERSION_DT_TM` | DATETIME | NOT NULL |  | Provides a version date and time history. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `DISCHARGE_PRSNL_ID` | [PRSNL](PRSNL.md) | `PERSON_ID` |
| `RCM_TLC_FACILITY_ID` | [RCM_TLC_FACILITY](RCM_TLC_FACILITY.md) | `RCM_TLC_FACILITY_ID` |
| `RCM_TLC_SERVICE_ID` | [RCM_TLC_SERVICE](RCM_TLC_SERVICE.md) | `RCM_TLC_SERVICE_ID` |
| `REPORT_REQUEST_ID` | [CR_REPORT_REQUEST](CR_REPORT_REQUEST.md) | `REPORT_REQUEST_ID` |

