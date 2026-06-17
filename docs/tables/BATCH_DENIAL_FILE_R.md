# BATCH_DENIAL_FILE_R

> Relates the batchs and denila codes.

**Description:** BATCH DENIAL FILE RELATION  
**Table type:** ACTIVITY  
**Primary key:** `BATCH_DENIAL_FILE_R_ID`  
**Columns:** 18  
**Referenced by:** 1 columns

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ACTIVE_IND` | DOUBLE |  |  | The table row is active or inactive. A row is generally active unless it is in an inactive state such as logically deleted, combined away, pending purge, etc. |
| 2 | `ACTIVE_STATUS_CD` | DOUBLE | NOT NULL |  | Indicates the status of the row itself (not the data in the row) such as active, inactive, combined away, pending purge, etc. |
| 3 | `ACTIVE_STATUS_DT_TM` | DATETIME |  |  | The date and time that the active_status_cd was set. |
| 4 | `ACTIVE_STATUS_PRSNL_ID` | DOUBLE | NOT NULL |  | The person who caused the active_status_cd to be set or change. |
| 5 | `BATCH_DENIAL_FILE_R_ID` | DOUBLE | NOT NULL | PK | Primary key |
| 6 | `BATCH_TRANS_FILE_ID` | DOUBLE | NOT NULL | FK→ | Foreign key reference to the batch_trans_file table. |
| 7 | `BEG_EFFECTIVE_DT_TM` | DATETIME |  |  | The date and time for which this table row becomes effective. Normally, this will be the date and time the row is added, but could be a past or future date and time. |
| 8 | `DENIAL_CD` | DOUBLE | NOT NULL |  | A claim remark providing additional information on why a claim was adjudicated. Additional information about a payment/adjustment on a claim. Valid codesets for this column are 26398, 26399, and 24730. |
| 9 | `DENIAL_CODE_TXT` | VARCHAR(255) |  |  | This field holds the text that relates to the denial code value |
| 10 | `DENIAL_TEXT` | VARCHAR(255) | NOT NULL |  | The payers alias representing the claim remark. |
| 11 | `DENIAL_TYPE_CD` | DOUBLE | NOT NULL |  | This defines the base type of the denial code i.e. provider, patient, technical, information only. |
| 12 | `END_EFFECTIVE_DT_TM` | DATETIME |  |  | The date/time after which the row is no longer valid as active current data. This may be valued with the date that the row became inactive. |
| 13 | `TRANS_RELTN_REASON_CD` | DOUBLE | NOT NULL |  | Stores TRANS_TRANS_RELTN tables TRANS_RELN_REASON_CD value in case of Transfer Transaction associated with remarks. |
| 14 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 15 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 16 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 17 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 18 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `BATCH_TRANS_FILE_ID` | [BATCH_TRANS_FILE](BATCH_TRANS_FILE.md) | `BATCH_TRANS_FILE_ID` |

## Referenced by (1)

| From table | Column |
|------------|--------|
| [BATCH_DENIAL_FILE_DETAIL_R](BATCH_DENIAL_FILE_DETAIL_R.md) | `BATCH_DENIAL_FILE_R_ID` |

