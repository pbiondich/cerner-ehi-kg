# PATIENT_CASE_ACCIDENT

> Stores information about a patient's accident case.

**Description:** Patient Case Accident  
**Table type:** ACTIVITY  
**Primary key:** _(not published — see note)_  
**Columns:** 17

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ACCIDENT_CD` | DOUBLE | NOT NULL |  | Identifies the type of accident (i.e., auto, work related, etc.). |
| 2 | `ACCIDENT_COUNTRY_CD` | DOUBLE | NOT NULL |  | The country where the accident occurred. |
| 3 | `ACCIDENT_DT_TM` | DATETIME |  |  | The date and time the accident occurred. |
| 4 | `ACCIDENT_LOCTN_TXT` | VARCHAR(100) |  |  | The text description of the location where the accident occurred. |
| 5 | `ACCIDENT_STATE_CD` | DOUBLE | NOT NULL |  | The state where the accident occurred. |
| 6 | `CLAIM_NBR_TXT` | VARCHAR(100) |  |  | The claim number associated with the workmen's comp or other type of claim. |
| 7 | `DISABILITY_BEG_DT_TM` | DATETIME |  |  | The date whn an impairment to the person's ability to function as a result of the accident began in the judgement of the provider. |
| 8 | `DISABILITY_END_DT_TM` | DATETIME |  |  | The date when an impairment to the person's ability to function as a result of the accident ended in the judgement of the provider. |
| 9 | `LAST_WORKED_DT_TM` | DATETIME |  |  | The date the patient last worked as a result of the disability. |
| 10 | `PATIENT_CASE_ACCIDENT_ID` | DOUBLE | NOT NULL |  | Uniquely identifies information about a patient's accident case. |
| 11 | `PATIENT_CASE_ID` | DOUBLE | NOT NULL | FK→ | Uniquely identifies the related patient case. |
| 12 | `RETURNED_TO_WORK_DT_TM` | DATETIME |  |  | The date the patient is authorized by the physician to return to work. |
| 13 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 14 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 15 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 16 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 17 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `PATIENT_CASE_ID` | [PATIENT_CASE](PATIENT_CASE.md) | `PATIENT_CASE_ID` |

