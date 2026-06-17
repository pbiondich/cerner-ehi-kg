# RAD_INT_CASE_R

> Radiology Interesting Case Relation

**Description:** This table contains the cases that a radiologist has identified as interesting.  
**Table type:** ACTIVITY  
**Primary key:** _(not published — see note)_  
**Columns:** 12

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `DIAGNOSIS` | VARCHAR(255) |  |  | This column contains the diagnosis entered by the radiologist for this specific interesting case. |
| 2 | `INT_CASE_ENTRY_ID` | DOUBLE | NOT NULL |  | This column is a meaningless number that only exists to uniquely identify a row. |
| 3 | `INT_CASE_ID` | DOUBLE | NOT NULL | FK→ | This column contains a foreign key to the rad_int_case table. It identifies the interesting case subclass that this case resides in. |
| 4 | `RADIOLOGIST_ID` | DOUBLE | NOT NULL | FK→ | This column contains a foreign key to the prsnl table. It uniquely identifies the radiologist associated with the interesting case. |
| 5 | `REMINDER_DT_TM` | DATETIME |  |  | This column contains the reminder date and time for an entry in the reminder file. |
| 6 | `REVIEWED_DT_TM` | DATETIME |  |  | This column contains the date and time that the reminder case what reviewed. This indicates that the reminder has been satisfied. |
| 7 | `SEQ_EXAM_ID` | DOUBLE | NOT NULL | FK→ | This column contains a foreign key to the Exam Data table. It uniquely identifies the completed exam that has been entered into the interesting case file. |
| 8 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 9 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 10 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 11 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 12 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `INT_CASE_ID` | [RAD_INT_CASE](RAD_INT_CASE.md) | `INT_CASE_ID` |
| `RADIOLOGIST_ID` | [PRSNL](PRSNL.md) | `PERSON_ID` |
| `SEQ_EXAM_ID` | [EXAM_DATA](EXAM_DATA.md) | `SEQ_EXAM_ID` |

