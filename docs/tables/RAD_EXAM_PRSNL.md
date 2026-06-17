# RAD_EXAM_PRSNL

> The Rad_Exam_Prsnl table contains those personnel that were involved in performing the ordered procedure(s).

**Description:** Rad Exam Personnel  
**Table type:** ACTIVITY  
**Primary key:** _(not published — see note)_  
**Columns:** 13

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ACTION_DT_TM` | DATETIME |  |  | The Action_Dt_Tm captures the date and time that the person interacted with the detail exam. |
| 2 | `ACTION_SEQUENCE` | DOUBLE | NOT NULL |  | Used to keep exam personnel in a specific sequence (the order in which they were entered) |
| 3 | `ACTION_TYPE_CD` | DOUBLE | NOT NULL |  | The Action_Type_Cd identifies which action the person performed upon the detail exam. (ex. completed, started, etc.) |
| 4 | `EXAM_PRSNL_ID` | DOUBLE | NOT NULL | FK→ | The Exam_Prsnl_Id is a foreign key to the Prsnl table. It identifies the person that interacted with the detail exam. |
| 5 | `EXAM_RELATION_CD` | DOUBLE | NOT NULL |  | The Exam_Relation_Cd identifies the role that the person took when interacting with the detail exam. (ex: tech, nurse, radiologist, etc.) |
| 6 | `PRIMARY_PRSNL_IND` | DOUBLE | NOT NULL |  | Determines if this personnel was designated the primary personnel responsible for this exam. 1 = Primary Personnel, 0 = Secondary Personnel |
| 7 | `RAD_EXAM_ID` | DOUBLE | NOT NULL | FK→ | The Rad_Exam_Id is a foreign key to the Rad_Exam table. It indicates which detail exam the personnel are tied to. |
| 8 | `READ_IND` | DOUBLE | NOT NULL |  | Indicates that this radiologist or resident will be "marked" to be the person to read the x-ray for this exam. This indicator will make this exam show in their desktop application for their own personal worklist of exams assigned to them. 0 = Not assigned; 1 = Assigned to read |
| 9 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 10 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 11 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 12 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 13 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `EXAM_PRSNL_ID` | [PRSNL](PRSNL.md) | `PERSON_ID` |
| `RAD_EXAM_ID` | [RAD_EXAM](RAD_EXAM.md) | `RAD_EXAM_ID` |

