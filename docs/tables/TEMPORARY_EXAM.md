# TEMPORARY_EXAM

> The Temporary_Exam table contains information about exams that have been placed in a temporary folder.

**Description:** Temporary Exam  
**Table type:** ACTIVITY  
**Primary key:** `SEQ_EXAM_ID`  
**Columns:** 9  
**Referenced by:** 1 columns

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ENCNTR_ID` | DOUBLE | NOT NULL | FK→ | This is the value of the unique primary identifier of the encounter table. It is an internal system assigned number. |
| 2 | `EXAM_OBJECT_ID` | DOUBLE | NOT NULL | FK→ | The Exam_Object_Id is a foreign key to the Film_Exam table. |
| 3 | `SEQ_EXAM_ID` | DOUBLE | NOT NULL | PK FK→ | The Seq_Exam_Id is a foreign key to the Exam_Data table. |
| 4 | `SEQ_OBJECT_ID` | DOUBLE | NOT NULL | FK→ | The Seq_Object_Id is a foreign key to the Temporary_Folder table. It uniquely identifies the temporary folder that the temporary exam is stored in. |
| 5 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 6 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 7 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 8 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 9 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `ENCNTR_ID` | [ENCOUNTER](ENCOUNTER.md) | `ENCNTR_ID` |
| `EXAM_OBJECT_ID` | [TRACKABLE_OBJECT](TRACKABLE_OBJECT.md) | `SEQ_OBJECT_ID` |
| `SEQ_EXAM_ID` | [EXAM_DATA](EXAM_DATA.md) | `SEQ_EXAM_ID` |
| `SEQ_OBJECT_ID` | [TEMPORARY_FOLDER](TEMPORARY_FOLDER.md) | `SEQ_OBJECT_ID` |

## Referenced by (1)

| From table | Column |
|------------|--------|
| [TEMPORARY_DETAILS](TEMPORARY_DETAILS.md) | `SEQ_EXAM_ID` |

