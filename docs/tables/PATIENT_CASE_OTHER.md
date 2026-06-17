# PATIENT_CASE_OTHER

> Stores information about other miscellaneous case types.

**Description:** Patient Case Other  
**Table type:** ACTIVITY  
**Primary key:** _(not published — see note)_  
**Columns:** 12

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `HEARING_VISION_RX_DT_TM` | DATETIME |  |  | The date that a prescription was written for hearing devices or vision frames and lenses. |
| 2 | `INITIAL_CONTACT_DT_TM` | DATETIME |  |  | The date the patient first consulted the provider for the condition by any means. It is not necessarily the initial date of treatment. |
| 3 | `ONSET_DT_TM` | DATETIME |  |  | The date and time of the onset of acute symptoms for the current illness or condition. |
| 4 | `PATIENT_CASE_ID` | DOUBLE | NOT NULL | FK→ | Uniquely identifiers the related Patient Case. |
| 5 | `PATIENT_CASE_OTHER_ID` | DOUBLE | NOT NULL |  | Uniquely identifies information about other miscellaneous case types. |
| 6 | `POST_OP_ASSUME_CARE_DT_TM` | DATETIME |  |  | The date the patient care was assumed by another provider during post-operative care. |
| 7 | `POST_OP_RELINQ_CARE_DT_TM` | DATETIME |  |  | The date the provcider filing the clain ceased post-operative care. |
| 8 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 9 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 10 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 11 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 12 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `PATIENT_CASE_ID` | [PATIENT_CASE](PATIENT_CASE.md) | `PATIENT_CASE_ID` |

