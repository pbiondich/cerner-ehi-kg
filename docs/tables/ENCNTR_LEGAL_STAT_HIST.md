# ENCNTR_LEGAL_STAT_HIST

> Holds the history of the relationships between encounters and their corresponding legal statuses

**Description:** Encounter Legal Status Relation History  
**Table type:** ACTIVITY  
**Primary key:** _(not published — see note)_  
**Columns:** 27

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ADJOURNMENT_DT_TM` | DATETIME |  |  | The date and time the case was adjourned |
| 2 | `BEG_EFFECTIVE_DT_TM` | DATETIME | NOT NULL |  | The date and time for which this table row becomes effective. Normally, this will be the date and time the row is added, but could be a past or future date and time. |
| 3 | `COURT_DT_TM` | DATETIME |  |  | The Date and Time of the court hearing |
| 4 | `COURT_FILE_NUM` | VARCHAR(40) |  |  | The file number representing the court case |
| 5 | `COURT_LOCATION_CD` | DOUBLE | NOT NULL |  | The location at which the court proceedings took place |
| 6 | `END_DT_TM` | DATETIME |  |  | The time the legal status was inactivated |
| 7 | `END_EFFECTIVE_DT_TM` | DATETIME | NOT NULL |  | The date/time after which the row is no longer valid as active current data. This may be valued with the date that the row became inactive. |
| 8 | `LEGAL_STATUS_HIST_ID` | DOUBLE | NOT NULL |  | Unique identifier for the ENCNTR_LEGAL_STATUS_HIST_R table |
| 9 | `LEGAL_STATUS_R_ID` | DOUBLE | NOT NULL | FK→ | Inherited Identifier for rows associated from the ENCNTR_LEGAL_STATUS_R table |
| 10 | `NEXT_REVIEW_DT_TM` | DATETIME |  |  | The date and time of the next review |
| 11 | `PROBABLE_SENTENCE_DT_TM` | DATETIME |  |  | The date and time of the probable sentence |
| 12 | `REFERRAL_DT_TM` | DATETIME |  |  | The referring datetime of the corresponding legal status. |
| 13 | `REFERRAL_FACILITY_CD` | DOUBLE | NOT NULL |  | The referring facility for the corresponding legal status. |
| 14 | `REFERRAL_SOURCE_CD` | DOUBLE | NOT NULL |  | The referral source for the corresponding legal status. |
| 15 | `REFERRAL_TYPE_CD` | DOUBLE | NOT NULL |  | The referral type for the corresponding legal status. |
| 16 | `REGION_CD` | DOUBLE | NOT NULL |  | The corresponding region of the legal status. |
| 17 | `REQ_EXTENSION_DT_TM` | DATETIME |  |  | The date and time a request for extension was made |
| 18 | `SENTENCE_DT_TM` | DATETIME |  |  | The date and time the sentence was or will be given |
| 19 | `START_DT_TM` | DATETIME |  |  | The time the legal status was activated |
| 20 | `STAY_OF_PROCEEDINGS_DT_TM` | DATETIME |  |  | The date and time of the Stay of Proceedings |
| 21 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 22 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 23 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 24 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 25 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |
| 26 | `VERBAL_STAY_DT_TM` | DATETIME |  |  | The date and time of the Verbal Stay |
| 27 | `WRITTEN_STAY_DT_TM` | DATETIME |  |  | The date and time of the Written Stay |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `LEGAL_STATUS_R_ID` | [ENCNTR_LEGAL_STATUS_R](ENCNTR_LEGAL_STATUS_R.md) | `LEGAL_STATUS_R_ID` |

