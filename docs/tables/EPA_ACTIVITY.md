# EPA_ACTIVITY

> Stores activity information for each Prior Authorization Transaction.

**Description:** Electronic Prior Authorization Activity  
**Table type:** ACTIVITY  
**Primary key:** _(not published — see note)_  
**Columns:** 22

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ACTIVE_IND` | DOUBLE | NOT NULL |  | The table row is active or inactive. A row is generally active unless it is in an inactive state such as logically deleted, combined away, pending purge, etc. |
| 2 | `APPEAL_EXPIRATION_DATE_TXT` | VARCHAR(255) |  |  | The deadline to appeal the PA decision. |
| 3 | `APPEAL_NOTE_ID` | DOUBLE | NOT NULL |  | **OBSOLETE** use column EPA_APPEAL_NOTE_ID |
| 4 | `DEADLINE_FOR_REPLY_TXT` | VARCHAR(255) |  |  | The deadline by which the prior authorization must be responded to. |
| 5 | `EAPPEAL_SUPPORTED_IND` | DOUBLE | NOT NULL |  | A boolean value that indicates if electronic appeals are supported. |
| 6 | `EPA_ACTIVITY_ID` | DOUBLE | NOT NULL |  | PRIMARY KEY |
| 7 | `EPA_APPEAL_NOTE_ID` | DOUBLE | NOT NULL | FK→ | The EPA_long_text id of the appeal note. |
| 8 | `EPA_PA_NOTE_ID` | DOUBLE | NOT NULL | FK→ | The EPA_long_text id of the pa note that corresponds to this activity. |
| 9 | `EPA_QUESTION_SET_BLOB_ID` | DOUBLE | NOT NULL | FK→ | The EPA_long_blob id of the question set blob. |
| 10 | `EPA_RECORD_ID` | DOUBLE | NOT NULL | FK→ | The identifier of the associated EPA_RECORD ( FK Value from EPA_RECORD) |
| 11 | `INBOUND_ATCHMT_IDENT` | VARCHAR(255) |  |  | The CAMM attachment identifier for a transaction level inbound attachment |
| 12 | `MESSAGE_IDENT` | VARCHAR(255) |  |  | The message id of the inbound NCPDP Transaction |
| 13 | `OUTBOUND_ATCHMT_IDENT` | VARCHAR(255) |  |  | The CAMM attachment identifier for a transaction level outbound attachment |
| 14 | `PA_NOTE_ID` | DOUBLE | NOT NULL |  | **OBSOLETE** use EPA_PA_NOTE_ID |
| 15 | `PA_REASON_BITMASK` | DOUBLE | NOT NULL |  | A bit mask that contains reason codes for the prior authorization status. |
| 16 | `QUESTION_SET_BLOB_ID` | DOUBLE | NOT NULL |  | **OBSOLETE** use EPA_QUESTION_SET_BLOB_ID |
| 17 | `STATUS_FLAG` | DOUBLE | NOT NULL |  | The status of the Electronic Prior Authorizations.See DM_FLAGS table for possible values ( 1- 17 ) |
| 18 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 19 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 20 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 21 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 22 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `EPA_APPEAL_NOTE_ID` | [EPA_LONG_TEXT](EPA_LONG_TEXT.md) | `EPA_LONG_TEXT_ID` |
| `EPA_PA_NOTE_ID` | [EPA_LONG_TEXT](EPA_LONG_TEXT.md) | `EPA_LONG_TEXT_ID` |
| `EPA_QUESTION_SET_BLOB_ID` | [EPA_LONG_BLOB](EPA_LONG_BLOB.md) | `EPA_LONG_BLOB_ID` |
| `EPA_RECORD_ID` | [EPA_RECORD](EPA_RECORD.md) | `EPA_RECORD_ID` |

