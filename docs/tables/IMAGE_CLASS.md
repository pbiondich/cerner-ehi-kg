# IMAGE_CLASS

> The Image_Class table contains common information about a specific container of exams. (ex. folders, tapes, cine, etc.)

**Description:** Image Class  
**Table type:** ACTIVITY  
**Primary key:** `SEQ_OBJECT_ID`  
**Columns:** 20  
**Referenced by:** 6 columns

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ACTIVE_VOLUME_IND` | DOUBLE |  |  | The Active_Volume_Ind indicates if the folder is the current, active volume. |
| 2 | `CREATION_DT_TM` | DATETIME |  |  | The Creation_Dt_Tm captures the date and time that the folder/media was created within the system. |
| 3 | `FILING_NUMBER` | VARCHAR(100) |  |  | The Filing_Number contains an identifier for the folder/media specific to the filing method used. |
| 4 | `HISTORY_LABEL_PRINT_IND` | DOUBLE |  |  | The History_Label_Print_Ind indicates whether or not historical labels should be printed. |
| 5 | `IMAGE_CLASS_TYPE_CD` | DOUBLE | NOT NULL | FK→ | The Image_Class_Type_Cd is a foreign key to the Image_Class_Type table. This uniquely identifies a folder type. |
| 6 | `LABEL_PRINT_DT_TM` | DATETIME |  |  | The label_print_dt_tm contains the date and time that the folder label originally printed. |
| 7 | `LOST_COMMENT` | VARCHAR(255) |  |  | The Lost_Comment contains any free text comments related to the folder/media being lost. |
| 8 | `LOST_IND` | DOUBLE |  |  | the Lost_Ind indicates whether or not a folder is marked as lost. |
| 9 | `NBR_EXAMS` | DOUBLE |  |  | The Nbr_Exams contains the number of exams that reside in the folder/media item. |
| 10 | `NEW_FOLD_IND` | DOUBLE |  |  | The new_fold_ind indicates if the folder is a newly created folder in which no exams exist at this time. Once exams are placed in the folder, the new_fold_ind will no longer be set. |
| 11 | `PENDING_EXAM_CNT` | DOUBLE |  |  | The pending_exam_cnt keeps track of the number of exams that have been ordered that will eventually load to the specific folder. This number is only relevant if the folder is 'new'. |
| 12 | `PURGE_IND` | DOUBLE |  |  | The Purge_Ind indicates is the folder/media item has been marked for purge. |
| 13 | `SEQ_OBJECT_ID` | DOUBLE | NOT NULL | PK FK→ | The Seq_Object_Id is a foreign key to the Trackable_Object table. This uniquely identifies the folder/media item. |
| 14 | `UPDATEABLE_IND` | DOUBLE |  |  | The Updateable_Ind indicates if this volume is the active volume. |
| 15 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 16 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 17 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 18 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 19 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |
| 20 | `VOLUME` | DOUBLE |  |  | The Volume field contains the volume number of the folder. This is a sequential number. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `IMAGE_CLASS_TYPE_CD` | [IMAGE_CLASS_TYPE](IMAGE_CLASS_TYPE.md) | `IMAGE_CLASS_TYPE_CD` |
| `SEQ_OBJECT_ID` | [TRACKABLE_OBJECT](TRACKABLE_OBJECT.md) | `SEQ_OBJECT_ID` |

## Referenced by (6)

| From table | Column |
|------------|--------|
| [FOLDER](FOLDER.md) | `SEQ_OBJECT_ID` |
| [FOREIGN_FOLDER](FOREIGN_FOLDER.md) | `SEQ_OBJECT_ID` |
| [ICLASS_ACC_ORDER_R](ICLASS_ACC_ORDER_R.md) | `SEQ_OBJECT_ID` |
| [ICLASS_PERSON_RELTN](ICLASS_PERSON_RELTN.md) | `SEQ_OBJECT_ID` |
| [MEDIA](MEDIA.md) | `SEQ_OBJECT_ID` |
| [TEMPORARY_FOLDER](TEMPORARY_FOLDER.md) | `SEQ_OBJECT_ID` |

