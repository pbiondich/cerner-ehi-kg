# CONTAINER_EVENT

> Events that happen to a container are recorded here to support container tracking.

**Description:** Container Event.  
**Table type:** ACTIVITY  
**Primary key:** `CONTAINER_ID`, `EVENT_SEQUENCE`  
**Columns:** 50  
**Referenced by:** 2 columns

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ADDITIONAL_LABELS` | DOUBLE |  |  | The number of extra labels which will be printed for orders with these collection requirements. The additional labels will not be assigned to a container. Not currently used. |
| 2 | `COLLECTION_LIST_ID` | DOUBLE | NOT NULL | FK→ | Unique system identifier of a collection list. |
| 3 | `COLLECTION_METHOD_CD` | DOUBLE | NOT NULL |  | The procedure for collecting a specimen. |
| 4 | `COLLECTION_TASK_ELIG_FLAG` | DOUBLE | NOT NULL |  | This field contains whether the container is eligible for a nurse collection task. 0 - Not Eligible; 1 - Eligible |
| 5 | `COLL_CLASS_CD` | DOUBLE | NOT NULL |  | The internal number assigned by the system to the Collection Class associated with the collection requirements. |
| 6 | `COLL_COMMENT_ID` | DOUBLE | NOT NULL | FK→ | The identifier of the collection comment in the long_text table. |
| 7 | `CONTAINER_ID` | DOUBLE | NOT NULL | PK | Unique system identifier for a container. |
| 8 | `CONVERSATION_ID` | DOUBLE | NOT NULL |  | A system generated number that uniquely identifies the group of orders that caused the container event. |
| 9 | `CURRENT_LOCATION_CD` | DOUBLE | NOT NULL |  | The container's current location. |
| 10 | `DISCARD_DT_TM` | DATETIME |  |  | The date/time that the container was discarded. |
| 11 | `DISCARD_REASON_CD` | DOUBLE | NOT NULL |  | The reason why the container was disposed. |
| 12 | `DRAWN_DT_TM` | DATETIME |  |  | The date and time when the specimen was collected. |
| 13 | `DRAWN_ID` | DOUBLE | NOT NULL |  | The system identifier of the person who collected the specimen. |
| 14 | `EVENT_DT_TM` | DATETIME |  |  | The Date and Time the event occurred |
| 15 | `EVENT_SEQUENCE` | DOUBLE | NOT NULL | PK | Sequential number to indicate the order events on a container. |
| 16 | `EVENT_TYPE_CD` | DOUBLE | NOT NULL |  | The type of event which occurred on the container. |
| 17 | `FIXATIVE_CD` | DOUBLE | NOT NULL |  | Not currently used. |
| 18 | `FROM_SERVICE_RESOURCE_CD` | DOUBLE |  | FK→ | Unique generated number that identifies a specific prior service resource where the container was located. |
| 19 | `LABEL_DT_TM` | DATETIME |  |  | The date and time printed on the label. |
| 20 | `LABEL_PRINTER_NAME` | VARCHAR(100) |  |  | This is used to save the label printer which was used to print the labels in container event table. The label printer details will be displayed in container inquiry application when it is called from scs_get_container_accession script. |
| 21 | `ORIGINAL_STORAGE_DT_TM` | DATETIME |  |  | The date/time that the container was placed in storage originally, |
| 22 | `PARENT_CONTAINER_ID` | DOUBLE | NOT NULL | FK→ | This unique system identifier is used to indicate which container the aliquot came from. |
| 23 | `PROCESSING_FLAG` | DOUBLE | NOT NULL |  | Identifies the type of processing that should occur as a result of the container event. 0 - No Processing Needed; 1 - Container Tracking Event; 2 - Nurse Collection Task |
| 24 | `REASON_MISSED_CD` | DOUBLE | NOT NULL |  | The reason a container was missed. |
| 25 | `REASON_MISSED_DT_TM` | DATETIME |  |  | The date/time a container was marked as missed. |
| 26 | `REASON_MISSED_ID` | DOUBLE | NOT NULL |  | The ID of the person who marked the container as missed. |
| 27 | `RECEIVED_DT_TM` | DATETIME |  |  | The date and time when the container was logged in. |
| 28 | `RECEIVED_ID` | DOUBLE | NOT NULL |  | The system identifier for the user who logged in the container. |
| 29 | `REMAINING_VOLUME` | DOUBLE |  |  | Obsolete - No longer in use. Replaced by Remaining_Volume_NBR |
| 30 | `REMAINING_VOLUME_NBR` | DOUBLE | NOT NULL |  | The remaining volume in the container. |
| 31 | `SERVICE_RESOURCE_CD` | DOUBLE |  | FK→ | Unique generated number that identifies a specific service resource associated with the container. |
| 32 | `SPECIMEN_ID` | DOUBLE | NOT NULL | FK→ | Unique system identifier for the specimen in the container. |
| 33 | `SPECIMEN_TYPE_CD` | DOUBLE | NOT NULL |  | The type of specimen in the container. |
| 34 | `SPEC_CNTNTR_CD` | DOUBLE | NOT NULL |  | The type of container the specimen is in. |
| 35 | `SPEC_HNDL_CD` | DOUBLE | NOT NULL |  | Any special handling for the container. |
| 36 | `STORAGE_LOCATION_TXT` | VARCHAR(100) |  |  | The storage location of the container when the event occurs |
| 37 | `STORAGE_RACK_CELL_ID` | DOUBLE | NOT NULL | FK→ | The storage location of the container |
| 38 | `SUB_EVENT_TYPE_CD` | DOUBLE | NOT NULL |  | Provides context for the source of the container event. |
| 39 | `SUGGESTED_DISCARD_DT_TM` | DATETIME |  |  | Obsolete, No longer being used. The suggested discard date/time of the container for storage tracking. |
| 40 | `TASK_LOG_ID` | DOUBLE | NOT NULL | FK→ | Used by Microbiology to uniquely identify an organism, |
| 41 | `TRANSFER_LIST_ID` | DOUBLE | NOT NULL | FK→ | The unique system identifier for a transfer list. |
| 42 | `UNITS_CD` | DOUBLE | NOT NULL |  | The units the container is measured in. |
| 43 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 44 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 45 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 46 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 47 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 48 | `VOLUME` | DOUBLE |  |  | Obsolete - No longer in use. Replaced by Volume_NBR |
| 49 | `VOLUME_NBR` | DOUBLE | NOT NULL |  | The total volume of the container. |
| 50 | `VOLUME_UNITS` | CHAR(15) |  |  | The volume units of the container. No longer used. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `COLLECTION_LIST_ID` | [COLLECTION_LIST](COLLECTION_LIST.md) | `COLLECTION_LIST_ID` |
| `COLL_COMMENT_ID` | [LONG_TEXT](LONG_TEXT.md) | `LONG_TEXT_ID` |
| `FROM_SERVICE_RESOURCE_CD` | [SERVICE_RESOURCE](SERVICE_RESOURCE.md) | `SERVICE_RESOURCE_CD` |
| `PARENT_CONTAINER_ID` | [CONTAINER](CONTAINER.md) | `CONTAINER_ID` |
| `SERVICE_RESOURCE_CD` | [SERVICE_RESOURCE](SERVICE_RESOURCE.md) | `SERVICE_RESOURCE_CD` |
| `SPECIMEN_ID` | [V500_SPECIMEN](V500_SPECIMEN.md) | `SPECIMEN_ID` |
| `STORAGE_RACK_CELL_ID` | [STORAGE_ITEM_CELL](STORAGE_ITEM_CELL.md) | `STORAGE_ITEM_CELL_ID` |
| `TASK_LOG_ID` | [MIC_TASK_LOG](MIC_TASK_LOG.md) | `TASK_LOG_ID` |
| `TRANSFER_LIST_ID` | [COLLECTION_LIST](COLLECTION_LIST.md) | `COLLECTION_LIST_ID` |

## Referenced by (2)

| From table | Column |
|------------|--------|
| [CONTAINER_EVENT_DETAILS](CONTAINER_EVENT_DETAILS.md) | `CONTAINER_ID` |
| [CONTAINER_EVENT_DETAILS](CONTAINER_EVENT_DETAILS.md) | `EVENT_SEQUENCE` |

