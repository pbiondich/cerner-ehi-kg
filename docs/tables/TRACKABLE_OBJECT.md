# TRACKABLE_OBJECT

> The Trackable_Object table contains information about those items that can be physically tracked within the image management area. These items include folders and all types of media.

**Description:** Trackable Object  
**Table type:** ACTIVITY  
**Primary key:** `SEQ_OBJECT_ID`  
**Columns:** 14  
**Referenced by:** 8 columns

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ACTIVE_IND` | DOUBLE |  |  | The table row is active or inactive. A row is generally active unless it is in an inactive state such as logically deleted, combined away, pending purge, etc. |
| 2 | `EXAM_IND` | DOUBLE |  |  | The Exam_Ind indicates if the trackable object is an exam or a folder. |
| 3 | `LOAN_TYPE_FLAG` | DOUBLE |  |  | The Loan_Type_Flag indicates is the current location of the folder/exam is a physician, patient, borrower, tracking point or library. |
| 4 | `MED_LEGAL_IND` | DOUBLE |  |  | The Med_Legal_Ind indicates if this trackable object has been marked as medical legal. |
| 5 | `RETURN_LOCATION_CD` | DOUBLE | NOT NULL |  | The Return_Location_Cd is a foreign key to the Track_Pt_Library table. It indicates where the trackable object resides permanently. |
| 6 | `SEQ_OBJECT_ID` | DOUBLE | NOT NULL | PK | The Seq_Object_Id uniquely identifies a row in the Trackable_Object table. It serves no other purpose other than to uniquely identify the row. |
| 7 | `TRACKING_POINT_CD` | DOUBLE | NOT NULL |  | The Tracking_Point_Cd identifies the trackable objects current location. This could be a physician, borrower, tracking point, library or patient. |
| 8 | `TRK_PT_ARRIVE_DT_TM` | DATETIME | NOT NULL |  | The Trk_Pt_Arrive_Dt_Tm captures the date and time that the trackable object entered the current tracking point. |
| 9 | `TRK_PT_ARRIVE_ID` | DOUBLE | NOT NULL | FK→ | The Trk_Pt_Arrive_Id captures the id of the user that moved the trackable object to its current location. |
| 10 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 11 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 12 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 13 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 14 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `TRK_PT_ARRIVE_ID` | [PRSNL](PRSNL.md) | `PERSON_ID` |

## Referenced by (8)

| From table | Column |
|------------|--------|
| [FILM_EXAM](FILM_EXAM.md) | `SEQ_OBJECT_ID` |
| [FILM_EXAM](FILM_EXAM.md) | `TEMP_FOLDER_ID` |
| [IMAGE_CLASS](IMAGE_CLASS.md) | `SEQ_OBJECT_ID` |
| [IMAGE_HISTORY](IMAGE_HISTORY.md) | `SEQ_OBJECT_ID` |
| [PULL_FOLDERS](PULL_FOLDERS.md) | `SEQ_OBJECT_ID` |
| [RAD_LOAN_INFO](RAD_LOAN_INFO.md) | `SEQ_OBJECT_ID` |
| [RAD_REQUEST](RAD_REQUEST.md) | `SEQ_OBJECT_ID` |
| [TEMPORARY_EXAM](TEMPORARY_EXAM.md) | `EXAM_OBJECT_ID` |

