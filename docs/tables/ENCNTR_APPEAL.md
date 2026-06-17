# ENCNTR_APPEAL

> The insurance appeal for an encounter.

**Description:** Encounter appeal  
**Table type:** ACTIVITY  
**Primary key:** `ENCNTR_APPEAL_ID`  
**Columns:** 28  
**Referenced by:** 1 columns

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ACTIVE_IND` | DOUBLE | NOT NULL |  | The table row is active or inactive. A row is generally active unless it is in an inactive state such as logically deleted, combined away, pending purge, etc. |
| 2 | `ACTIVE_STATUS_CD` | DOUBLE | NOT NULL |  | Indicates the status of the row itself (not the data in the row) such as active, inactive, combined away, pending purge, etc. |
| 3 | `ACTIVE_STATUS_DT_TM` | DATETIME | NOT NULL |  | The date and time that the active_status_cd was set. |
| 4 | `ACTIVE_STATUS_PRSNL_ID` | DOUBLE | NOT NULL |  | The person who caused the active_status_cd to be set or change. |
| 5 | `ADVISOR_PRSNL_ID` | DOUBLE | NOT NULL | FK→ | Uniquely identifies the advisor. |
| 6 | `APPEAL_COMM_TYPE_CD` | DOUBLE | NOT NULL |  | The type of communication used to send the appeal. |
| 7 | `APPEAL_EXPECT_RESP_DT_TM` | DATETIME |  |  | The date and time of when a response is expected for the appeal. |
| 8 | `APPEAL_LEVEL_CD` | DOUBLE | NOT NULL |  | The appeal level for the appeal. |
| 9 | `APPEAL_OUTCOME_CD` | DOUBLE | NOT NULL |  | The final outcome of the appeal. |
| 10 | `APPEAL_OUTCOME_DT_TM` | DATETIME |  |  | The date and time the final outcome was reached for the appeal. |
| 11 | `APPEAL_PRSNL_ID` | DOUBLE | NOT NULL | FK→ | Unique generated number that identifies a single row on the Prsnl table for the personnel in charge of the appeal. |
| 12 | `APPEAL_SENT_DT_TM` | DATETIME |  |  | The date and time the appeal was sent. |
| 13 | `APPEAL_STATUS_CD` | DOUBLE | NOT NULL |  | The appeal status for the appeal. |
| 14 | `APPEAL_VERIFIED_DT_TM` | DATETIME |  |  | The date and time the appeal was verified. |
| 15 | `COMMENT_LONG_TEXT_ID` | DOUBLE | NOT NULL | FK→ | Unique generated number that identifies a single row on the Long_text table that represents a comment for this relationship. |
| 16 | `ENCNTR_APPEAL_ID` | DOUBLE | NOT NULL | PK | Unique generated number that identifies a single row on the Encntr_appeal table. |
| 17 | `ENCNTR_ID` | DOUBLE | NOT NULL | FK→ | Unique generated number that identifies a single row on the Encounter table related to the appeal. |
| 18 | `EXT_APPEAL_AGENCY_CD` | DOUBLE | NOT NULL |  | The external appeal agency handling the appeal. |
| 19 | `PAYER_ORG_ID` | DOUBLE | NOT NULL | FK→ | Unique generated number that identifies a single row on the Organization table for the payer of the appeal. |
| 20 | `POST_APPEAL_LEVEL_OF_CARE_CD` | DOUBLE | NOT NULL |  | The post-appeal level of care that was approved for encounter. |
| 21 | `PRE_APPEAL_LEVEL_OF_CARE_CD` | DOUBLE | NOT NULL |  | The pre-appeal level of care that was approved for encounter. |
| 22 | `PROVIDED_LEVEL_OF_CARE_CD` | DOUBLE | NOT NULL |  | The provided level of care that is being appealed for the encounter. |
| 23 | `TRACKING_NBR_TEXT` | VARCHAR(255) |  |  | The tracking number for the appeal communication. |
| 24 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 25 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 26 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 27 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 28 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `ADVISOR_PRSNL_ID` | [PRSNL](PRSNL.md) | `PERSON_ID` |
| `APPEAL_PRSNL_ID` | [PRSNL](PRSNL.md) | `PERSON_ID` |
| `COMMENT_LONG_TEXT_ID` | [LONG_TEXT](LONG_TEXT.md) | `LONG_TEXT_ID` |
| `ENCNTR_ID` | [ENCOUNTER](ENCOUNTER.md) | `ENCNTR_ID` |
| `PAYER_ORG_ID` | [ORGANIZATION](ORGANIZATION.md) | `ORGANIZATION_ID` |

## Referenced by (1)

| From table | Column |
|------------|--------|
| [ENCNTR_DENIAL_APPEAL_RELTN](ENCNTR_DENIAL_APPEAL_RELTN.md) | `ENCNTR_APPEAL_ID` |

