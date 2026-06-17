# ICD10_EXTENSION

> Additional attributes for ICD-10 vocabulary used to drive functionality.

**Description:** ICD10 EXTENSION  
**Table type:** REFERENCE  
**Primary key:** _(not published — see note)_  
**Columns:** 27

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ACTIVE_DT_TM` | DATETIME |  |  | The table row is active or inactive. A row is generally active unless it is in an inactive state such as logically deleted, combined away, pending purge, etc. |
| 2 | `ACTIVE_IND` | DOUBLE | NOT NULL |  | The table row is active or inactive. A row is generally active unless it is in an inactive state such as logically deleted, combined away, pending purge, etc. |
| 3 | `ACTIVE_STATUS_CD` | DOUBLE | NOT NULL |  | Indicates the status of the row itself (not the data in the row) such as active, inactive, combined away, pending purge, etc. |
| 4 | `ACTIVE_STATUS_PRSNL_ID` | DOUBLE | NOT NULL |  | The person who caused the active_status_cd to be set or change. |
| 5 | `ACTIVITY_REQUIRED_IND` | DOUBLE |  |  | Indicates whether or not an Activity when Injured Code is required when this code is used. |
| 6 | `AGE_CHECK_IND` | DOUBLE |  |  | Indicates whether an age check is available. |
| 7 | `AGE_HIGH` | DOUBLE |  |  | High age value stored in days.Column |
| 8 | `AGE_LOW` | DOUBLE |  |  | Low age value stored in days.Column |
| 9 | `AGE_TYPE_EDIT_FLAG` | DOUBLE |  |  | All age-flagged codes will require an age type edit. |
| 10 | `BEG_EFFECTIVE_DT_TM` | DATETIME |  |  | The date and time for which this table row becomes effective. Normally, this will be the date and time the row is added, but could be a past or future date and time. |
| 11 | `BLOCK_NBR_TXT` | VARCHAR(10) |  |  | The block number is used to group icd10-am procedures together. |
| 12 | `CANCER_NOTIFICATION_IND` | DOUBLE |  |  | Indicates whether a cancer notification form is to be completed for this diagnosis. 0 = Not required; 1 = Required. |
| 13 | `CODE_FORM_FLAG` | DOUBLE |  |  | Indicates the 'form' of a code. |
| 14 | `END_EFFECTIVE_DT_TM` | DATETIME |  |  | The date/time after which the row is no longer valid as active current data. This may be valued with the date that the row became inactive. |
| 15 | `EXTERNAL_CAUSE_FLAG` | DOUBLE |  |  | Indicates whether an external cause code is required for use with this code. |
| 16 | `ICD10_EXTENSION_ID` | DOUBLE | NOT NULL |  | Primary key identifier for the ICD10_Extension table. |
| 17 | `OCCURRENCE_LOC_REQUIRED_IND` | DOUBLE |  |  | Indicates whether or not a Place of Occurrence Code is required when this code is used. |
| 18 | `PRIMARY_DIAG_IND` | DOUBLE |  |  | Indicates whether the code is unacceptable for use as a Principal Diagnosis |
| 19 | `RARE_DIAG_IND` | DOUBLE |  |  | An edit flag to indicate whether the code pertains to a rare and / or notifiable disease. 0 = Not rare; 1 = Rare |
| 20 | `SEX_FLAG` | DOUBLE |  |  | An edit flag to indicate whether the code is valid for a particular sex. |
| 21 | `SEX_TYPE_EDIT_FLAG` | DOUBLE |  |  | All sex-flagged codes require a sex type edit. |
| 22 | `SOURCE_IDENTIFIER` | VARCHAR(50) | NOT NULL |  | Source identifier from the nomenclature table.Column |
| 23 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 24 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 25 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 26 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 27 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

