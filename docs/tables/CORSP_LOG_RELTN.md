# CORSP_LOG_RELTN

> This table is used to store all the correspondence relationships.

**Description:** CORRESPONDENCE LOG RELTN  
**Table type:** ACTIVITY  
**Primary key:** _(not published — see note)_  
**Columns:** 21

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ACCT_ID` | DOUBLE | NOT NULL | FK→ | Foreign key to the account table. |
| 2 | `ACTIVE_IND` | DOUBLE |  |  | The table row is active or inactive. A row is generally active unless it is in an inactive state such as logically deleted, combined away, pending purge, etc. |
| 3 | `ACTIVE_STATUS_CD` | DOUBLE | NOT NULL |  | Indicates the status of the row itself (not the data in the row) such as active, inactive, combined away, pending purge, etc. |
| 4 | `ACTIVE_STATUS_DT_TM` | DATETIME |  |  | The date and time that the active_status_cd was set. |
| 5 | `ACTIVE_STATUS_PRSNL_ID` | DOUBLE | NOT NULL |  | The person who caused the active_status_cd to be set or change. |
| 6 | `ACTIVITY_ID` | DOUBLE | NOT NULL | FK→ | Part of Primary key. Foreign key to the corsp_log table |
| 7 | `BEG_EFFECTIVE_DT_TM` | DATETIME |  |  | The date and time for which this table row becomes effective. Normally, this will be the date and time the row is added, but could be a past or future date and time. |
| 8 | `BILL_VRSN_NBR` | DOUBLE |  |  | Version number of the bill record |
| 9 | `CORSP_LOG_RELTN_ID` | DOUBLE | NOT NULL |  | Primary Key on Corsp_Log_Reltn table |
| 10 | `END_EFFECTIVE_DT_TM` | DATETIME |  |  | The date/time after which the row is no longer valid as active current data. This may be valued with the date that the row became inactive. |
| 11 | `KEYWORD_TXT` | VARCHAR(50) |  |  | Text related to the keyword. |
| 12 | `LONG_TEXT_ID` | DOUBLE | NOT NULL | FK→ | Foreign key to the long_text table. |
| 13 | `PARENT_ENTITY_ID` | DOUBLE | NOT NULL |  | Part of Primary key. |
| 14 | `PARENT_ENTITY_NAME` | VARCHAR(32) | NOT NULL |  | Part of Primary key |
| 15 | `PFT_ENCNTR_ID` | DOUBLE | NOT NULL | FK→ | Foreign key to the pft_encntr table. |
| 16 | `RECIPIENT_TYPE_CD` | DOUBLE | NOT NULL |  | For correspondence, represents the type of recipient (e.g. Patient, Guarantor, Subscriber, etc.) |
| 17 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 18 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 19 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 20 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 21 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `ACCT_ID` | [ACCOUNT](ACCOUNT.md) | `ACCT_ID` |
| `ACTIVITY_ID` | [CORSP_LOG](CORSP_LOG.md) | `ACTIVITY_ID` |
| `LONG_TEXT_ID` | [LONG_TEXT](LONG_TEXT.md) | `LONG_TEXT_ID` |
| `PFT_ENCNTR_ID` | [PFT_ENCNTR](PFT_ENCNTR.md) | `PFT_ENCNTR_ID` |

