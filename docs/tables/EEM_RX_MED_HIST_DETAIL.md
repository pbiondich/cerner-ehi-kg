# EEM_RX_MED_HIST_DETAIL

> The EEM_RX_MED_HIST_DETAIL table stores summary data for medication history transactions. We use the table to store information about transactions sent to and from 3rd parties. The information stored is data need for either processing the inbound transaction or for use when displaying summary data about the transaction in a client application.

**Description:** EEM Medication History Detail  
**Table type:** ACTIVITY  
**Primary key:** _(not published — see note)_  
**Columns:** 19

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `CONTRIBUTOR_SYSTEM_CD` | DOUBLE | NOT NULL |  | Contributor system identifies the source feed of data from which a row was populated. This is mainly used to determine how to update a set of data that may have originated from more than one source feed. |
| 2 | `DATA_EXPIRE_DT_TM` | DATETIME |  |  | Date and time that the transaction response data is considered to be expired. |
| 3 | `EEM_RX_ELIG_DETAIL_ID` | DOUBLE | NOT NULL | FK→ | Primary identifier of EEM_RX_ELIG_DETAIL |
| 4 | `EEM_RX_MED_HIST_DETAIL_ID` | DOUBLE | NOT NULL |  | Primary identifier of EEM_RX_MED_HIST_DETAIL |
| 5 | `HEALTH_PLAN_ID` | DOUBLE | NOT NULL | FK→ | Identifier of the health plan for which history was requested |
| 6 | `INTERCHANGE_ID` | DOUBLE | NOT NULL |  | Primary identifier for a transaction |
| 7 | `ORGANIZATION_ID` | DOUBLE | NOT NULL | FK→ | Identifier of the carrier organization tied to the history request |
| 8 | `ORIGIN_INTERCHANGE_ID` | DOUBLE | NOT NULL |  | Unique identifier of the first transaction in the series that requested a patient's prescription history. |
| 9 | `PERSON_ID` | DOUBLE | NOT NULL | FK→ | Identifier of the person for who this transaction was sent |
| 10 | `REPLY_DT_TM` | DATETIME |  |  | Date and time the transaction was returned |
| 11 | `RESPONSE_CD` | DOUBLE | NOT NULL |  | Code used to describe the status of the response transaction |
| 12 | `SENT_DT_TM` | DATETIME |  |  | Date and time the transaction was sent outbound |
| 13 | `TRANS_DATA_CD` | DOUBLE | NOT NULL |  | Describes the high level status of a transaction message based on the system's business rules. The message may be in a pending, error, or returned state. |
| 14 | `TRANS_VENUE_TYPE_CD` | DOUBLE | NOT NULL |  | Defines the type of transaction and the venue from where it was submitted. |
| 15 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 16 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 17 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 18 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 19 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `EEM_RX_ELIG_DETAIL_ID` | [EEM_RX_ELIG_DETAIL](EEM_RX_ELIG_DETAIL.md) | `EEM_RX_ELIG_DETAIL_ID` |
| `HEALTH_PLAN_ID` | [HEALTH_PLAN](HEALTH_PLAN.md) | `HEALTH_PLAN_ID` |
| `ORGANIZATION_ID` | [ORGANIZATION](ORGANIZATION.md) | `ORGANIZATION_ID` |
| `PERSON_ID` | [PERSON](PERSON.md) | `PERSON_ID` |

