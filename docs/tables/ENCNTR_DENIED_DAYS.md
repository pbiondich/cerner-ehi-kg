# ENCNTR_DENIED_DAYS

> The denied day periods for an encounter.

**Description:** Encounter Denied Days  
**Table type:** ACTIVITY  
**Primary key:** `ENCNTR_DENIED_DAYS_ID`  
**Columns:** 34  
**Referenced by:** 1 columns

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ACTIVE_IND` | DOUBLE | NOT NULL |  | The table row is active or inactive. A row is generally active unless it is in an inactive state such as logically deleted, combined away, pending purge, etc. |
| 2 | `ACTIVE_STATUS_CD` | DOUBLE | NOT NULL |  | Indicates the status of the row itself (not the data in the row) such as active, inactive, combined away, pending purge, etc. |
| 3 | `ACTIVE_STATUS_DT_TM` | DATETIME | NOT NULL |  | The date and time that the active_status_cd was set. |
| 4 | `ACTIVE_STATUS_PRSNL_ID` | DOUBLE | NOT NULL |  | The person who caused the active_status_cd to be set or change. |
| 5 | `APPEAL_BY_DT_TM` | DATETIME |  |  | The date to appeal the denied day period. |
| 6 | `BEG_DT_TM` | DATETIME |  |  | The begin date for the denied day period. |
| 7 | `CLAIM_NUMBER_TXT` | VARCHAR(40) | NOT NULL |  | Contains the patient account display claim number. |
| 8 | `CLOSED_DT_TM` | DATETIME |  |  | The date and time the denied day period was closed. |
| 9 | `COMMENT_LONG_TEXT_ID` | DOUBLE | NOT NULL | FK→ | Unique generated number that identifies a single row on the Long_text table that represents a comment for this relationship. |
| 10 | `DENIAL_CATEGORY_CD` | DOUBLE | NOT NULL |  | The category of the denial period. |
| 11 | `DENIAL_PRSNL_ID` | DOUBLE | NOT NULL | FK→ | Unique generated number that identifies a single row on the Prsnl table for the personnel in charge of the denied day period. |
| 12 | `DENIAL_REASON_CD` | DOUBLE | NOT NULL |  | The denial reason for the denied day period. |
| 13 | `DENIAL_RISK_AMOUNT` | DOUBLE | NOT NULL |  | The dollar amount that is at risk for loss from the denied day period. |
| 14 | `DENIAL_TYPE_CD` | DOUBLE | NOT NULL |  | The denial type for the denied day period. |
| 15 | `ENCNTR_DENIED_DAYS_ID` | DOUBLE | NOT NULL | PK | Unique generated number that identifies a single row on the Encntr_denied_days table. |
| 16 | `ENCNTR_ID` | DOUBLE | NOT NULL | FK→ | Unique generated number that identifies a single row on the Encounter table. The encounter associated with the denied days. |
| 17 | `END_DT_TM` | DATETIME |  |  | The end date for the denied day period. |
| 18 | `LETTER_DT_TM` | DATETIME |  |  | The date and time the letter was received for the denied day period. |
| 19 | `NOTICE_RECEIVED_DT_TM` | DATETIME |  |  | The date and time the noticed was received for the denied day period. |
| 20 | `PAYER_ORG_ID` | DOUBLE | NOT NULL | FK→ | Unique generated number that identifies a single row on the Organization table for the payer of the denied day period. |
| 21 | `PFT_QUEUE_ITEM_ID` | DOUBLE |  |  | Uniquely identifies the related ProFit queue item. |
| 22 | `REMARK_CD` | DOUBLE | NOT NULL |  | The patient account remark code which can come from code set 26399, 26398 or 24730. |
| 23 | `RESP_PARTY_NURSE_UNIT_CD` | DOUBLE | NOT NULL |  | The nurse unit that is responsible for the avoidable days period. |
| 24 | `RESP_PARTY_OTHER_CD` | DOUBLE | NOT NULL |  | The entity that is responsible for the avoidable days period. |
| 25 | `RESP_PARTY_PRSNL_ID` | DOUBLE | NOT NULL | FK→ | The personnel that is responsible for the avoidable days period. |
| 26 | `RESP_PARTY_SELF_IND` | DOUBLE | NOT NULL |  | Indicator for whether the patient or their family are responsible for the avoidable days period. |
| 27 | `RESP_PARTY_SERVICE_TYPE_CD` | DOUBLE | NOT NULL |  | The Service that is responsible for the avoidable days period. |
| 28 | `SERVICE_BEG_DT_TM` | DATETIME |  |  | The patient account service begin date time. |
| 29 | `SERVICE_END_DT_TM` | DATETIME |  |  | The patient account service end date time. |
| 30 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 31 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 32 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 33 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 34 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `COMMENT_LONG_TEXT_ID` | [LONG_TEXT](LONG_TEXT.md) | `LONG_TEXT_ID` |
| `DENIAL_PRSNL_ID` | [PRSNL](PRSNL.md) | `PERSON_ID` |
| `ENCNTR_ID` | [ENCOUNTER](ENCOUNTER.md) | `ENCNTR_ID` |
| `PAYER_ORG_ID` | [ORGANIZATION](ORGANIZATION.md) | `ORGANIZATION_ID` |
| `RESP_PARTY_PRSNL_ID` | [PRSNL](PRSNL.md) | `PERSON_ID` |

## Referenced by (1)

| From table | Column |
|------------|--------|
| [ENCNTR_DENIAL_APPEAL_RELTN](ENCNTR_DENIAL_APPEAL_RELTN.md) | `ENCNTR_DENIED_DAYS_ID` |

