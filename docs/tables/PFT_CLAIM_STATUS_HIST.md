# PFT_CLAIM_STATUS_HIST

> Contains the history of changes to claim status and sub status (status reason)

**Description:** ProFit Claim Status History  
**Table type:** ACTIVITY  
**Primary key:** _(not published — see note)_  
**Columns:** 15

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ACTIVITY_DT_TM` | DATETIME | NOT NULL |  | The current date/time of the system that inserted the row. |
| 2 | `BEG_EFFECTIVE_DT_TM` | DATETIME |  |  | The date and time for which this table row becomes effective. Normally, this will be the date and time the row is added, but could be a past or future date and time. |
| 3 | `CLAIM_EVENT_STATUS_FLAG` | DOUBLE | NOT NULL |  | Identifies whether the event status is:0 - N/A1 - In Process2 - Failed3 - Success |
| 4 | `CLAIM_STATUS_CD` | DOUBLE | NOT NULL |  | Primary status of the claim (bill_status_cd on the bill_rec. |
| 5 | `CLAIM_SUB_STATUS_CD` | DOUBLE | NOT NULL |  | The secondary status of the claim (bill_status_reason_cd on the bill_rec. |
| 6 | `CORSP_ACTIVITY_ID` | DOUBLE | NOT NULL |  | Identifies the related claim identifier from the bill_rec table. |
| 7 | `END_EFFECTIVE_DT_TM` | DATETIME |  |  | The date/time after which the row is no longer valid as active current data. This may be valued with the date that the row became inactive. |
| 8 | `EXTERNAL_IDENT` | VARCHAR(250) |  |  | The external identifier is the unique identifier for an edi transaction for various payment types. |
| 9 | `LONG_TEXT_ID` | DOUBLE | NOT NULL | FK→ | Uniquely identifies a message specific to an event. |
| 10 | `PFT_CLAIM_STATUS_HIST_ID` | DOUBLE | NOT NULL |  | Uniquely identifiesa change to the claim status and sub status for a bill rec. |
| 11 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 12 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 13 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 14 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 15 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `LONG_TEXT_ID` | [LONG_TEXT](LONG_TEXT.md) | `LONG_TEXT_ID` |

