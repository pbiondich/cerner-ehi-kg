# PATIENT_CASE_THERAPY

> Stores infromation about a patient's therapy case.

**Description:** Patient Case Therapy  
**Table type:** ACTIVITY  
**Primary key:** _(not published — see note)_  
**Columns:** 12

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ACUTE_MANIFEST_DT_TM` | DATETIME |  |  | The date that the condition developed into or becomes a condition with a rapid onset and/or a short course. |
| 2 | `HEARING_VISION_RX_DT_TM` | DATETIME |  |  | The date that a prescription was written for hearing devices or vision frames and lenses. |
| 3 | `INITIAL_TREATMENT_DT_TM` | DATETIME |  |  | The date of the first treatment for the medical condition being treated for the patient case. |
| 4 | `LAST_SEEN_DT_TM` | DATETIME |  |  | The date and time that the patient was last seen by the attending or supervising physician for the condition related to the patient case. |
| 5 | `LAST_XRAY_DT_TM` | DATETIME |  |  | The date of the last x-ray for the medical condition being treated for the patient case. |
| 6 | `PATIENT_CASE_ID` | DOUBLE | NOT NULL | FK→ | Uniquely identifies the related patient case. |
| 7 | `PATIENT_CASE_THERAPY_ID` | DOUBLE | NOT NULL |  | Uniquely identifies information about a patient's therapy case. |
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

