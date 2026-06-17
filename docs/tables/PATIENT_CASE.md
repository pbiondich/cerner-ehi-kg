# PATIENT_CASE

> Stores information about a patient's medical problem within a specific period of time across a continuum of care.

**Description:** Patient Case  
**Table type:** ACTIVITY  
**Primary key:** `PATIENT_CASE_ID`  
**Columns:** 16  
**Referenced by:** 8 columns

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ACTIVE_IND` | DOUBLE | NOT NULL |  | The table row is active or inactive. A row is generally active unless it is in an inactive state such as logically deleted, combined away, pending purge, etc. |
| 2 | `ACTIVE_STATUS_CD` | DOUBLE | NOT NULL |  | Indicates the status of the row itself (not the data in the row) such as active, inactive, combined away, pending purge, etc. |
| 3 | `ACTIVE_STATUS_DT_TM` | DATETIME | NOT NULL |  | The date and time that the active_status_cd was set. |
| 4 | `ACTIVE_STATUS_PRSNL_ID` | DOUBLE | NOT NULL |  | The person who caused the active_status_cd to be set or change. |
| 5 | `BEG_EFFECTIVE_DT_TM` | DATETIME | NOT NULL |  | The date and time for which this table row becomes effective. Normally, this will be the date and time the row is added, but could be a past or future date and time. |
| 6 | `CASE_DESC` | VARCHAR(100) |  |  | The free text description of the case. |
| 7 | `CASE_TYPE_CD` | DOUBLE | NOT NULL |  | Case type code identifies the kind of patient case (i.e., therapy, auto accident, worker's comp. etc.). |
| 8 | `COMMENT_ID` | DOUBLE | NOT NULL | FK→ | Uniquely identifies the entry in long_text with related textual patient case comments. |
| 9 | `END_EFFECTIVE_DT_TM` | DATETIME | NOT NULL |  | The date/time after which the row is no longer valid as active current data. This may be valued with the date that the row became inactive. |
| 10 | `PATIENT_CASE_ID` | DOUBLE | NOT NULL | PK | Uniquely identifies a patient's medical problem within a specific period of time across a continuum of care. |
| 11 | `PERSON_ID` | DOUBLE | NOT NULL | FK→ | Uniquely identifies the person related to this case. |
| 12 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 13 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 14 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 15 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 16 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `COMMENT_ID` | [LONG_TEXT](LONG_TEXT.md) | `LONG_TEXT_ID` |
| `PERSON_ID` | [PERSON](PERSON.md) | `PERSON_ID` |

## Referenced by (8)

| From table | Column |
|------------|--------|
| [PATIENT_CASE_ACCIDENT](PATIENT_CASE_ACCIDENT.md) | `PATIENT_CASE_ID` |
| [PATIENT_CASE_ENCNTR_R](PATIENT_CASE_ENCNTR_R.md) | `PATIENT_CASE_ID` |
| [PATIENT_CASE_IN_PMT_AGMT](PATIENT_CASE_IN_PMT_AGMT.md) | `PATIENT_CASE_ID` |
| [PATIENT_CASE_OB](PATIENT_CASE_OB.md) | `PATIENT_CASE_ID` |
| [PATIENT_CASE_OTHER](PATIENT_CASE_OTHER.md) | `PATIENT_CASE_ID` |
| [PATIENT_CASE_OUT_PMT_AGMT](PATIENT_CASE_OUT_PMT_AGMT.md) | `PATIENT_CASE_ID` |
| [PATIENT_CASE_THERAPY](PATIENT_CASE_THERAPY.md) | `PATIENT_CASE_ID` |
| [SCH_PEND_ENCNTR_DETAIL](SCH_PEND_ENCNTR_DETAIL.md) | `PATIENT_CASE_ID` |

