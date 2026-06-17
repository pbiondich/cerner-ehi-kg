# FILM_EXAM

> The Film_Exam table contains information about an exam, that has been performed, that is specific the the media type of film.

**Description:** Film Exam  
**Table type:** ACTIVITY  
**Primary key:** _(not published — see note)_  
**Columns:** 14

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `FILM_COUNT` | DOUBLE |  |  | The Film_Count contains the actual number of films that were produced as a result of the exam being performed. This is for tracking purposes only. |
| 2 | `FOLDER_ID` | DOUBLE | NOT NULL | FK→ | The Folder_Id is a foreign key to the Folder table. This identifies the folder that the exam resides in within the image management area. |
| 3 | `LOST_COMMENT` | VARCHAR(255) |  |  | The Lost_Comment contains any comments pertaining to lost films. |
| 4 | `LOST_COUNT` | DOUBLE |  |  | The Lost_Count identifies how many films have been lost out of the total film count. |
| 5 | `LOST_IND` | DOUBLE |  |  | The Lost_Ind indicates if the film has been lost. |
| 6 | `MULTI_DAY_IN_PROC_IND` | DOUBLE |  |  | The Multi_Day_In _Proc_Ind indicates whether or not a multi-day study is currently in process. |
| 7 | `SEQ_EXAM_ID` | DOUBLE | NOT NULL | FK→ | The Seq_Exam_Id is a foreign key to the Exam_Data table. |
| 8 | `SEQ_OBJECT_ID` | DOUBLE | NOT NULL | FK→ | The Seq_Object_Id is a foreign key to the Trackable_Object table. This identifies the film exam as a trackable object within the image management area. |
| 9 | `TEMP_FOLDER_ID` | DOUBLE | NOT NULL | FK→ | The Temp_Folder_Id is a foreign key to the Temporary Folder table. This identifies the temporary folder that the exam is currently residing in, if it's in a temporary folder at all. |
| 10 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 11 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 12 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 13 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 14 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `FOLDER_ID` | [FOLDER](FOLDER.md) | `SEQ_OBJECT_ID` |
| `SEQ_EXAM_ID` | [EXAM_DATA](EXAM_DATA.md) | `SEQ_EXAM_ID` |
| `SEQ_OBJECT_ID` | [TRACKABLE_OBJECT](TRACKABLE_OBJECT.md) | `SEQ_OBJECT_ID` |
| `TEMP_FOLDER_ID` | [TRACKABLE_OBJECT](TRACKABLE_OBJECT.md) | `SEQ_OBJECT_ID` |

