# CONTAINER

> Each and every specimen container tracked by the PathNet Specimen Collections module will be represented by a row in this table.

**Description:** Container  
**Table type:** ACTIVITY  
**Primary key:** `CONTAINER_ID`  
**Columns:** 39  
**Referenced by:** 11 columns

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ADDITIONAL_LABELS` | DOUBLE |  |  | The number of extra labels which will be printed for orders with these collection requirements. The additional labels will not be assigned to a container. |
| 2 | `AUTO_PRINT_ALIQUOT_IND` | DOUBLE |  |  | Indicates whether aliquot labels have automatically printed once the specimen container reaches the login location. A value of 0 means the aliquot labels have not printed. A value of 1 means the aliquot labels have printed. |
| 3 | `COLLECTION_LIST_ID` | DOUBLE | NOT NULL | FK→ | Unique system identifier of a collection list. |
| 4 | `COLLECTION_METHOD_CD` | DOUBLE | NOT NULL |  | The procedure for collecting a specimen. |
| 5 | `COLLECTION_TASK_ELIG_FLAG` | DOUBLE | NOT NULL |  | This field indicates whether the container is elibible for a nurse collection task. 0 - Not Eligible; 1 - Eligible |
| 6 | `COLL_CLASS_CD` | DOUBLE | NOT NULL |  | The internal number assigned by the system to the Collection Class associated with the collection requirements. |
| 7 | `COLL_COMMENT_ID` | DOUBLE | NOT NULL | FK→ | The identifier in the long text table of the collection comment for the container if one exists. |
| 8 | `CONTAINER_ID` | DOUBLE | NOT NULL | PK | Unique system identifier for a container. |
| 9 | `CURRENT_LOCATION_CD` | DOUBLE | NOT NULL |  | The container's current location. |
| 10 | `DISCARD_DT_TM` | DATETIME |  |  | The date and time the container was discarded. |
| 11 | `DISCARD_REASON_CD` | DOUBLE | NOT NULL |  | The reason why the container was disposed. |
| 12 | `DRAWN_DT_TM` | DATETIME |  |  | The date and time when the specimen was collected. |
| 13 | `DRAWN_ID` | DOUBLE | NOT NULL | FK→ | The system identifier of the person who collected the specimen. |
| 14 | `FIXATIVE_CD` | DOUBLE | NOT NULL |  | Not currently used. |
| 15 | `INSTR_LOGIN_IND` | DOUBLE |  |  | This field is to indicate whether a container is initially logged in by Auto Login. instr_login_ind = 0 means the container initially is not logged in by instrument. instr_login_ind = 1 means the container is initially logged in by an instrument. |
| 16 | `LABEL_DT_TM` | DATETIME |  |  | The date and time printed on the label. |
| 17 | `ON_ROBOTICS_LINE_FLAG` | DOUBLE | NOT NULL |  | When a container is placed on the robotics line, this flag is set to 1. |
| 18 | `ORIGINAL_STORAGE_DT_TM` | DATETIME |  |  | The date and time the container is placed in storage. |
| 19 | `PARENT_CONTAINER_ID` | DOUBLE | NOT NULL | FK→ | This unique system identifier is used to indicate which container the aliquot came from. |
| 20 | `RECEIVED_DT_TM` | DATETIME |  |  | The date and time when the container was logged in. |
| 21 | `RECEIVED_ID` | DOUBLE | NOT NULL | FK→ | The system identifier for the user who logged in the container. |
| 22 | `REMAINING_VOLUME` | DOUBLE |  |  | The remaining volume in the container. |
| 23 | `SPECIMEN_ID` | DOUBLE | NOT NULL | FK→ | Unique system identifier for the specimen in the container. |
| 24 | `SPECIMEN_TYPE_CD` | DOUBLE | NOT NULL |  | The type of specimen in the container. |
| 25 | `SPEC_CNTNR_CD` | DOUBLE | NOT NULL | FK→ | The type of container the specimen is in. |
| 26 | `SPEC_HNDL_CD` | DOUBLE | NOT NULL |  | Any special handling for the container. |
| 27 | `STORAGE_RACK_CELL_ID` | DOUBLE | NOT NULL | FK→ | The storage location of the given container. Used by storage tracking. |
| 28 | `STORAGE_STATUS_CD` | DOUBLE | NOT NULL |  | Obsolete, No longer being used. Identifies the current status of each container as it relates to Storage Tracking. Identifies whether the Container has never been placed in storage, is currently in storage, is checked out from storage, or has been discarded. |
| 29 | `SUGGESTED_DISCARD_DT_TM` | DATETIME |  |  | Obsolete, No longer being used. The suggested date and time when the container should be discarded. |
| 30 | `TASK_LOG_ID` | DOUBLE | NOT NULL | FK→ | Allows microbiology to uniquely an organizm. |
| 31 | `TRANSFER_LIST_ID` | DOUBLE | NOT NULL | FK→ | The unique system identifier for a transfer list. |
| 32 | `UNITS_CD` | DOUBLE | NOT NULL |  | The units the container is measured in. |
| 33 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 34 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 35 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 36 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 37 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 38 | `VOLUME` | DOUBLE |  |  | The total volume of the container. |
| 39 | `VOLUME_UNIT` | CHAR(15) |  |  | The volume units of the container. No longer used. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `COLLECTION_LIST_ID` | [COLLECTION_LIST](COLLECTION_LIST.md) | `COLLECTION_LIST_ID` |
| `COLL_COMMENT_ID` | [LONG_TEXT](LONG_TEXT.md) | `LONG_TEXT_ID` |
| `DRAWN_ID` | [PRSNL](PRSNL.md) | `PERSON_ID` |
| `PARENT_CONTAINER_ID` | [CONTAINER](CONTAINER.md) | `CONTAINER_ID` |
| `RECEIVED_ID` | [PRSNL](PRSNL.md) | `PERSON_ID` |
| `SPECIMEN_ID` | [V500_SPECIMEN](V500_SPECIMEN.md) | `SPECIMEN_ID` |
| `SPEC_CNTNR_CD` | [SPECIMEN_CONTAINER](SPECIMEN_CONTAINER.md) | `SPEC_CNTNR_CD` |
| `STORAGE_RACK_CELL_ID` | [STORAGE_ITEM_CELL](STORAGE_ITEM_CELL.md) | `STORAGE_ITEM_CELL_ID` |
| `TASK_LOG_ID` | [MIC_TASK_LOG](MIC_TASK_LOG.md) | `TASK_LOG_ID` |
| `TRANSFER_LIST_ID` | [COLLECTION_LIST](COLLECTION_LIST.md) | `COLLECTION_LIST_ID` |

## Referenced by (11)

| From table | Column |
|------------|--------|
| [CONTAINER](CONTAINER.md) | `PARENT_CONTAINER_ID` |
| [CONTAINER_EVENT](CONTAINER_EVENT.md) | `PARENT_CONTAINER_ID` |
| [CONTAINER_LAB_HANDLING](CONTAINER_LAB_HANDLING.md) | `CONTAINER_ID` |
| [FOREIGN_CONTAINER](FOREIGN_CONTAINER.md) | `CONTAINER_ID` |
| [FOREIGN_CONTAINER_EXCPTN](FOREIGN_CONTAINER_EXCPTN.md) | `CONTAINER_ID` |
| [HANDHELD_DETAIL](HANDHELD_DETAIL.md) | `CONTAINER_ID` |
| [ORDER_CONTAINER_R](ORDER_CONTAINER_R.md) | `DEST_CONTAINER_ID` |
| [PERSON_ABORH_RESULT](PERSON_ABORH_RESULT.md) | `CONTAINER_ID` |
| [SPECIMEN_USAGE](SPECIMEN_USAGE.md) | `CREATED_CONTAINER_ID` |
| [SPECIMEN_USAGE](SPECIMEN_USAGE.md) | `PARENT_CONTAINER_ID` |
| [TASK_ACTIVITY](TASK_ACTIVITY.md) | `CONTAINER_ID` |

