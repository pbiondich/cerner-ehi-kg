# ENCNTR_LEGAL_STATUS_R

> Holds the relationship between encounters and their corresponding legal statuses.

**Description:** Encounter legal status relation.  
**Table type:** ACTIVITY  
**Primary key:** `LEGAL_STATUS_R_ID`  
**Columns:** 31  
**Referenced by:** 3 columns

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ACTIVE_IND` | DOUBLE | NOT NULL |  | The table row is active or inactive. A row is generally active unless it is in an inactive state such as logically deleted, combined away, pending purge, etc. |
| 2 | `ACTIVE_STATUS_CD` | DOUBLE | NOT NULL |  | Indicates the status of the row itself (not the data in the row) such as active, inactive, combined away, pending purge, etc. |
| 3 | `ACTIVE_STATUS_DT_TM` | DATETIME | NOT NULL |  | The date and time that the active_status_cd was set. |
| 4 | `ACTIVE_STATUS_PRSNL_ID` | DOUBLE | NOT NULL |  | The person who caused the active_status_cd to be set or change. |
| 5 | `ADJOURNMENT_DT_TM` | DATETIME |  |  | The date and time the case was adjourned. |
| 6 | `COURT_DT_TM` | DATETIME |  |  | The court date and time. |
| 7 | `COURT_FILE_NUM` | VARCHAR(40) |  |  | The file number representing the court case. |
| 8 | `COURT_LOCATION_CD` | DOUBLE | NOT NULL |  | The location at which the court proceedings took place. |
| 9 | `ENCNTR_ID` | DOUBLE | NOT NULL | FK→ | This is the value of the unique primary identifier of the encounter table. It is an internal system assigned number. |
| 10 | `END_DT_TM` | DATETIME |  |  | End Date and Time value |
| 11 | `LEGAL_STATUS_CD` | DOUBLE | NOT NULL |  | Legal Status Code |
| 12 | `LEGAL_STATUS_R_ID` | DOUBLE | NOT NULL | PK | Unique identifier for the encntr_legal_status_r table. |
| 13 | `LEGAL_STAT_INACTIVE_IND` | DOUBLE |  |  | Indicates whether the legal status has been inactivated by the user. |
| 14 | `NEXT_REVIEW_DT_TM` | DATETIME |  |  | The date and time of the next review. |
| 15 | `PROBABLE_SENTENCE_DT_TM` | DATETIME |  |  | The date and time of the probable sentence. |
| 16 | `REFERRAL_DT_TM` | DATETIME |  |  | The referring datetime of the corresponding legal status. |
| 17 | `REFERRAL_FACILITY_CD` | DOUBLE | NOT NULL |  | The referring facility for the corresponding legal status. |
| 18 | `REFERRAL_SOURCE_CD` | DOUBLE | NOT NULL |  | The referral source for the corresponding legal status. |
| 19 | `REFERRAL_TYPE_CD` | DOUBLE | NOT NULL |  | The referral type for the corresponding legal status. |
| 20 | `REGION_CD` | DOUBLE | NOT NULL |  | The corresponding region of the legal status. |
| 21 | `REQ_EXTENSION_DT_TM` | DATETIME |  |  | The date and time a request for extension was made. |
| 22 | `SENTENCE_DT_TM` | DATETIME |  |  | The date and the time the sentence was or will be given. |
| 23 | `START_DT_TM` | DATETIME |  |  | The time the legal status was activated. |
| 24 | `STAY_OF_PROCEEDINGS_DT_TM` | DATETIME |  |  | The date and time of the stay of proceedings. |
| 25 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 26 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 27 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 28 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 29 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |
| 30 | `VERBAL_STAY_DT_TM` | DATETIME |  |  | The date and time of the verbal stay. |
| 31 | `WRITTEN_STAY_DT_TM` | DATETIME |  |  | The date and time of the written stay. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `ENCNTR_ID` | [ENCOUNTER](ENCOUNTER.md) | `ENCNTR_ID` |

## Referenced by (3)

| From table | Column |
|------------|--------|
| [ENCNTR_LEGAL_REVIEW_R](ENCNTR_LEGAL_REVIEW_R.md) | `LEGAL_STATUS_R_ID` |
| [ENCNTR_LEGAL_STAT_CRIM_R](ENCNTR_LEGAL_STAT_CRIM_R.md) | `LEGAL_STATUS_R_ID` |
| [ENCNTR_LEGAL_STAT_HIST](ENCNTR_LEGAL_STAT_HIST.md) | `LEGAL_STATUS_R_ID` |

