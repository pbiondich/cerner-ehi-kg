# HIM_EVENT_EXTENSION

> Stores fields like anticipated ind and multiple anticipated reports ind.

**Description:** This table stores event information for ProFile documents  
**Table type:** REFERENCE  
**Primary key:** _(not published — see note)_  
**Columns:** 26

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ACTIVE_IND` | DOUBLE |  |  | The table row is active or inactive. A row is generally active unless it is in an inactive state such as logically deleted, combined away, pending purge, etc. |
| 2 | `ACTIVE_STATUS_CD` | DOUBLE | NOT NULL |  | Indicates the status of the row itself (not the data in the row) such as active, inactive, combined away, pending purge, etc. |
| 3 | `ACTIVE_STATUS_DT_TM` | DATETIME |  |  | The date and time that the active_status_cd was set. |
| 4 | `ACTIVE_STATUS_PRSNL_ID` | DOUBLE | NOT NULL |  | The person who caused the active_status_cd to be set or change. |
| 5 | `BEG_EFFECTIVE_DT_TM` | DATETIME |  |  | The date and time for which this table row becomes effective. Normally, this will be the date and time the row is added, but could be a past or future date and time. |
| 6 | `COSIGN_IND` | DOUBLE |  |  | Indicates if this document type requires a co-signature |
| 7 | `COSIGN_PRSNL_TYPE_CD` | DOUBLE | NOT NULL |  | This is the type of physician that needs to cosign the document. |
| 8 | `DICTATION_DELINQUENCY_TIME` | DOUBLE |  |  | This is the time in minutes, that the dictation needs to be completed by before the document is considered delinquent |
| 9 | `DICTATION_TURNAROUND_TIME` | DOUBLE |  |  | This is the time that the document should be dictated after an event (i.e. discharge event). |
| 10 | `DOCUMENT_DISPLAY_ORDER` | DOUBLE |  |  | This is the display order for document type that is used by the frontend and reports. |
| 11 | `END_EFFECTIVE_DT_TM` | DATETIME |  |  | The date/time after which the row is no longer valid as active current data. This may be valued with the date that the row became inactive. |
| 12 | `EVENT_CD` | DOUBLE | NOT NULL |  | This is the document type. |
| 13 | `MATCHING_PHYSICIAN_IND` | DOUBLE |  |  | When matching a new report to anticipated reports, should we match an physician also. |
| 14 | `MULTIPLE_EVENT_FLAG` | DOUBLE |  |  | Can we create multiple document for the same encounter. |
| 15 | `ORGANIZATION_ID` | DOUBLE | NOT NULL | FK→ | This is the value of the unique primary identifier of the organization table. It is an internal system assigned number. |
| 16 | `SERV_RES_CD` | DOUBLE | NOT NULL |  | The service resource that this document type is associated with. |
| 17 | `SIGNATURE_DELINQUENCY_TIME` | DOUBLE |  |  | This is the amount of time that is allowed for a signature before it becomes delinquent |
| 18 | `SIGNATURE_REQUIRED_IND` | DOUBLE |  |  | Is there a signature requirement for this document type |
| 19 | `SIGNATURE_TURNAROUND_TIME` | DOUBLE |  |  | This is the turnaround time for signatures |
| 20 | `TRANSCRIPTION_TURNAROUND_TIME` | DOUBLE |  |  | This is the amount of time allotted for transcription turnaround |
| 21 | `TRAN_TIME_IND` | DOUBLE |  |  | This indicator is used to determine if a client wants to include the time a document is in a Requested Transcribe status when calculating the age of a document. If set to 1, it will be included. |
| 22 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 23 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 24 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 25 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 26 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `ORGANIZATION_ID` | [ORGANIZATION](ORGANIZATION.md) | `ORGANIZATION_ID` |

