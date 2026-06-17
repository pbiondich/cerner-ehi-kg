# UKRWH_CDS_RTT_PERIOD

> UK Reporting Warehouse Commissioning Data Set Referral To Treatment Periods

**Description:** UKRWH_CDS_RTT_PERIOD  
**Table type:** REFERENCE  
**Primary key:** _(not published — see note)_  
**Columns:** 18

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ACTIVE_IND` | DOUBLE | NOT NULL |  | The table row is active or inactive. A row is generally active unless it is in an inactive state such as logically deleted, combined away, pending purge, etc. |
| 2 | `EPISODE_SK` | VARCHAR(100) |  |  | This is the value of the unique primary identifier of the episode table. It is an internal system assigned number. |
| 3 | `HEALTH_SYSTEM_ID` | DOUBLE | NOT NULL |  | Unique number assigned by Health Facts. Typically the universal Cerner assigned client id of the health system. |
| 4 | `HEALTH_SYSTEM_SOURCE_ID` | DOUBLE | NOT NULL |  | Unique number assigned by Health Facts. Typically the universal Cerner assigned client id of the sending health system but may be adjusted if there is >1 HF feed from the client. |
| 5 | `LOC_RTT_PERIOD_END_DT_TM` | DATETIME |  |  | The end date of a referral to treatment period. |
| 6 | `LOC_RTT_PERIOD_START_DT_TM` | DATETIME |  |  | The start date of a referral to treatment period. |
| 7 | `PATIENT_PATHWAY_IDENT` | VARCHAR(20) |  |  | An identifier, which together with the organization code of the issuer uniquely identifies a patient pathway. |
| 8 | `RTT_PERIOD_END_DT_TM` | DATETIME |  |  | The end date of a referral to treatment period. |
| 9 | `RTT_PERIOD_KEY` | DOUBLE | NOT NULL |  | This is the value of the unique identifier of the UKRWH_CDS_RTT_PERIOD table. It is an internal system assigned number |
| 10 | `RTT_PERIOD_SEQ` | DOUBLE |  |  | The sequence of the RTT period within a patient pathway. |
| 11 | `RTT_PERIOD_START_DT_TM` | DATETIME |  |  | The start date of a referral to treatment period. |
| 12 | `RTT_PERIOD_START_EVENT_SK` | VARCHAR(100) |  |  | This is the unique identifier for the rtt event that represents the start of an rtt period |
| 13 | `RTT_PERIOD_STOP_EVENT_SK` | VARCHAR(100) |  |  | This is the unique identifier for the rtt event that represents the stop of an rtt period |
| 14 | `UPDATE_USER` | VARCHAR(40) | NOT NULL |  | The user that performs the insert or update to the record |
| 15 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 16 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 17 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 18 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

