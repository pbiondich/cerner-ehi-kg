# TEMPORARY_DETAILS

> The Temporary_Details table contains information about each component of a temporary exam.

**Description:** Temporary Details  
**Table type:** ACTIVITY  
**Primary key:** _(not published — see note)_  
**Columns:** 7

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `DISCRETE_ASSAY_TASK_CD` | DOUBLE | NOT NULL |  | The Discrete_Assay_Task_Cd is a foreign key to the Discrete_Task_Assay table. It uniquely identifies the detail procedure that is contained in the temporary folder. |
| 2 | `SEQ_EXAM_ID` | DOUBLE | NOT NULL | FK→ | The Seq_Exam_Id is a foreign key to the Temporary_Exam table. It identifies the temporary Exam that the detail exams are a part of. |
| 3 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 4 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 5 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 6 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 7 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `SEQ_EXAM_ID` | [TEMPORARY_EXAM](TEMPORARY_EXAM.md) | `SEQ_EXAM_ID` |

