# MEDIA_EXAM

> The Media_Exam table contains information about a procedure that has been performed and whose results are stored on a type of media other than film.

**Description:** Media Exam  
**Table type:** ACTIVITY  
**Primary key:** _(not published — see note)_  
**Columns:** 13

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ENCNTR_ID` | DOUBLE | NOT NULL | FK→ | This is the value of the unique primary identifier of the encounter table. It is an internal system assigned number. |
| 2 | `EXAM_POSN` | DOUBLE |  |  | The Exam_Posn field contains a sequential number identifying where in the order the exam exists. |
| 3 | `OPTICAL_DISK_SIDE` | DOUBLE |  |  | The Optical_Disk_Side indicates which side of the optical disk an exam resides on. |
| 4 | `PERSON_ID` | DOUBLE | NOT NULL | FK→ | This is the value of the unique primary identifier of the person table. It is an internal system assigned number. |
| 5 | `SEQ_EXAM_ID` | DOUBLE | NOT NULL | FK→ | The Seq_Exam_Id is a foreign key to the Exam_Data table. It uniquely identifies the exam. |
| 6 | `SEQ_OBJECT_ID` | DOUBLE | NOT NULL |  | The Seq_Object_Id is a foreign key to the Media table. This identifies which media item the exam resides on. |
| 7 | `TRACK_BEGIN` | DOUBLE |  |  | The Track_Begin field identifies the track number at which the exams recording starts. |
| 8 | `TRACK_END` | DOUBLE |  |  | The Track_End field identifies the track number at which the exams recording ends. |
| 9 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 10 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 11 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 12 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 13 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `ENCNTR_ID` | [ENCOUNTER](ENCOUNTER.md) | `ENCNTR_ID` |
| `PERSON_ID` | [PERSON](PERSON.md) | `PERSON_ID` |
| `SEQ_EXAM_ID` | [EXAM_DATA](EXAM_DATA.md) | `SEQ_EXAM_ID` |

