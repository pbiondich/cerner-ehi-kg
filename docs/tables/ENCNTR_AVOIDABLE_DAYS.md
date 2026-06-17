# ENCNTR_AVOIDABLE_DAYS

> The avoidable day periods for an encounter.

**Description:** Encounter Avoidable Days  
**Table type:** ACTIVITY  
**Primary key:** _(not published — see note)_  
**Columns:** 26

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ACTIVE_IND` | DOUBLE | NOT NULL |  | The table row is active or inactive. A row is generally active unless it is in an inactive state such as logically deleted, combined away, pending purge, etc. |
| 2 | `ACTIVE_STATUS_CD` | DOUBLE | NOT NULL |  | Indicates the status of the row itself (not the data in the row) such as active, inactive, combined away, pending purge, etc. |
| 3 | `ACTIVE_STATUS_DT_TM` | DATETIME | NOT NULL |  | The date and time that the active_status_cd was set. |
| 4 | `ACTIVE_STATUS_PRSNL_ID` | DOUBLE | NOT NULL |  | The person who caused the active_status_cd to be set or change. |
| 5 | `BEG_DT_TM` | DATETIME |  |  | The begin date and time of the avoidable days period for the encounter. |
| 6 | `COMMENT_LONG_TEXT_ID` | DOUBLE | NOT NULL | FK→ | Unique generated number that identifies a single row on the Long_text table that is used to record any comments for the avoidable days period. |
| 7 | `ENCNTR_AVOIDABLE_DAYS_ID` | DOUBLE | NOT NULL |  | Unique generated number that identifies a single row on the Encntr_avoidable_days table. |
| 8 | `ENCNTR_ID` | DOUBLE | NOT NULL | FK→ | The ID of the encounter the avoidable days are related to. |
| 9 | `END_DT_TM` | DATETIME |  |  | The begin date and time of the avoidable days period for the encounter. |
| 10 | `POST_ACUTE_PROVIDER_ID` | DOUBLE | NOT NULL | FK→ | Uniquely identifies the related post-acute provider. |
| 11 | `REASON_CD` | DOUBLE | NOT NULL |  | The reason for the avoidable days period for the encounter. |
| 12 | `REASON_TYPE_CD` | DOUBLE | NOT NULL |  | The type of reason for the avoidable days period for the encounter. |
| 13 | `RESP_PARTY_BUSINESS_ORG_ID` | DOUBLE | NOT NULL | FK→ | The business organization that is responsible for the avoidable days period. |
| 14 | `RESP_PARTY_BUSINESS_TYPE_CD` | DOUBLE | NOT NULL |  | The type code of the responsible business party. |
| 15 | `RESP_PARTY_NURSE_UNIT_CD` | DOUBLE | NOT NULL |  | The nurse unit that is responsible for the avoidable days period. |
| 16 | `RESP_PARTY_OTHER_CD` | DOUBLE | NOT NULL |  | The entity that is responsible for the avoidable days period. |
| 17 | `RESP_PARTY_PAYER_ORG_ID` | DOUBLE | NOT NULL | FK→ | The insurance payer organization that is responsible for the avoidable days period. |
| 18 | `RESP_PARTY_PRSNL_ID` | DOUBLE | NOT NULL | FK→ | The personnel that is responsible for the avoidable days period. |
| 19 | `RESP_PARTY_SELF_IND` | DOUBLE | NOT NULL |  | Indicator for whether the patient or their family are responsible for the avoidable days period. |
| 20 | `RESP_PARTY_SERVICE_TYPE_CD` | DOUBLE | NOT NULL |  | The Service that is responsible for the avoidable days period. |
| 21 | `TLC_FACILITY_ID` | DOUBLE | NOT NULL | FK→ | The uniquely identifies facility data on the table will represent long term care facilities that total living choices (tlc) is using to place patients. |
| 22 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 23 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 24 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 25 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 26 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `COMMENT_LONG_TEXT_ID` | [LONG_TEXT](LONG_TEXT.md) | `LONG_TEXT_ID` |
| `ENCNTR_ID` | [ENCOUNTER](ENCOUNTER.md) | `ENCNTR_ID` |
| `POST_ACUTE_PROVIDER_ID` | [RCM_POST_ACUTE_PROVIDER](RCM_POST_ACUTE_PROVIDER.md) | `RCM_POST_ACUTE_PROVIDER_ID` |
| `RESP_PARTY_BUSINESS_ORG_ID` | [ORGANIZATION](ORGANIZATION.md) | `ORGANIZATION_ID` |
| `RESP_PARTY_PAYER_ORG_ID` | [ORGANIZATION](ORGANIZATION.md) | `ORGANIZATION_ID` |
| `RESP_PARTY_PRSNL_ID` | [PRSNL](PRSNL.md) | `PERSON_ID` |
| `TLC_FACILITY_ID` | [RCM_TLC_FACILITY](RCM_TLC_FACILITY.md) | `RCM_TLC_FACILITY_ID` |

