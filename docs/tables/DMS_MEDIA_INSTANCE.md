# DMS_MEDIA_INSTANCE

> Contains references to media items in the Media Management archive.

**Description:** Digital Media Services - Media Instance.  
**Table type:** ACTIVITY  
**Primary key:** `DMS_MEDIA_INSTANCE_ID`  
**Columns:** 41  
**Referenced by:** 6 columns

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `APP_CTX` | VARCHAR(128) |  |  | A string mnemonic of the application in context when this instance was created. |
| 2 | `CHECKSUM` | DOUBLE | NOT NULL |  | This contains the checksum value for the stored content. |
| 3 | `CONSUMERCREATED_DT_TM` | DATETIME |  |  | The media object's creation date and time set by the consumer. Basically it is whatever date the consumer says is the actual creation date, because they may have an object they created weeks before they actually put into MOM. |
| 4 | `CONSUMERCREATED_PREC_FLAG` | DOUBLE | NOT NULL |  | Used to indicate date precision. 0 - Date is precise to the second, 1 - Date is precise to the minute, 2 - Date is precise to the hour, 3 - Date is precise to the day, 4 - Date is precise to the month, 5 - Date is precise to the year. |
| 5 | `CONSUMERCREATED_TZ` | DOUBLE | NOT NULL |  | The time zone for the consumer created time. |
| 6 | `CONTENT_SIZE` | DOUBLE | NOT NULL |  | Indicates the byte size of the content. |
| 7 | `CONTENT_TYPE` | VARCHAR(32) | NOT NULL |  | OBSOLETE - NO LONGER USED. Replaced by dms_content_type_id. |
| 8 | `CONTENT_UID` | VARCHAR(64) | NOT NULL |  | The unique key to the content instance in the media archive. |
| 9 | `CONTRIBUTION_DT_TM` | DATETIME |  |  | The date and time this version of the media object was contributed |
| 10 | `CONTRIBUTOR_ID` | DOUBLE | NOT NULL | FK→ | The ID of the user who contributed this version of the media object. |
| 11 | `CREATED_BY_ID` | DOUBLE | NOT NULL | FK→ | The person_id that represents the individual that created this row. |
| 12 | `CREATED_DT_TM` | DATETIME | NOT NULL |  | The date and time that this row was created. |
| 13 | `DMS_CONTENT_TYPE_ID` | DOUBLE | NOT NULL | FK→ | The type of content that this media instance refers to. |
| 14 | `DMS_MEDIA_IDENTIFIER_GROUP_ID` | DOUBLE | NOT NULL |  | This column points to the DMS_MEDIA_IDENTIFIER row if the row is part of a group. |
| 15 | `DMS_MEDIA_IDENTIFIER_ID` | DOUBLE | NOT NULL |  | References the DMS_MEDIA_IDENTIFIER table for the media object identifier. |
| 16 | `DMS_MEDIA_INSTANCE_ID` | DOUBLE | NOT NULL | PK | Unique identifier for the row. |
| 17 | `DMS_REPOSITORY_ID` | DOUBLE | NOT NULL | FK→ | Index to the dms_repository table |
| 18 | `DMS_XML_METADATA_ID` | DOUBLE | NOT NULL |  | This is the identifier of the XML data in table DMS_XML_Metadata. |
| 19 | `ENCRYPTION_IND` | DOUBLE | NOT NULL |  | indicates the instance is encrypted |
| 20 | `IDENTIFIER` | VARCHAR(64) | NOT NULL |  | ** OBSOLETE - NO LONGER USED ** - The uniquely generated identifier for this media item. |
| 21 | `LONG_BLOB_ID` | DOUBLE | NOT NULL | FK→ | This is a foreign key to the long_blob table used to store content when the archive is not used. |
| 22 | `LONG_TEXT_ID` | DOUBLE | NOT NULL | FK→ | Reference to the LONG_TEXT_REFERENCE table for the actual XML metadata file. |
| 23 | `MEDIA_TYPE` | VARCHAR(255) | NOT NULL |  | Indicates the format of the content that this row refers to. Examples include "text/plain", "text/xml", etc. |
| 24 | `METADATA_VERSION` | DOUBLE |  |  | The version number of the meta-data schema that is associated with this media instance. |
| 25 | `NAME` | VARCHAR(255) |  |  | The name or title associated to the media instance. |
| 26 | `SENSITIVE_LEVEL_NBR` | DOUBLE | NOT NULL |  | This column is used to indicate sensitivity level. Any value greater than zero indicates that the object is sensitive. |
| 27 | `SERVICESTART_DT_TM` | DATETIME |  |  | The service start time. |
| 28 | `SERVICESTART_PREC_FLAG` | DOUBLE | NOT NULL |  | Used to indicate date precision. 0 - Date is precise to the second, 1 - Date is precise to the minute, 2 - Date is precise to the hour, 3 - Date is precise to the day, 4 - Date is precise to the month, 5 - Date is precise to the year. |
| 29 | `SERVICESTART_TZ` | DOUBLE | NOT NULL |  | The time zone for the service start time. |
| 30 | `SERVICESTOP_DT_TM` | DATETIME |  |  | The service stop time. |
| 31 | `SERVICESTOP_PREC_FLAG` | DOUBLE | NOT NULL |  | Used to indicate date precision. 0 - Date is precise to the second, 1 - Date is precise to the minute, 2 - Date is precise to the hour, 3 - Date is precise to the day, 4 - Date is precise to the month, 5 - Date is precise to the year. |
| 32 | `SERVICESTOP_TZ` | DOUBLE | NOT NULL |  | The time zone for the service stop time. |
| 33 | `STATUS_FLAG` | DOUBLE | NOT NULL |  | This column is used to indicate the state of the dms_media_instance row, either active, inactive or in-error. Additional statuses may also be stored. -2 - Deleted, -1 - In error, 0 - Inactive, 1 - Active, 2 - Inactive waiting deletion, 3 - Initialized. |
| 34 | `STORED_AS_DICOM_IND` | DOUBLE | NOT NULL |  | Used to indicate that the object was stored as a Dicom object. 0 - Not a Dicom object, 1 - Dicom object. |
| 35 | `THUMBNAIL_UID` | VARCHAR(64) |  |  | The unique key to the thumbnail image instance in the media archive. |
| 36 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 37 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 38 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 39 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 40 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 41 | `VERSION` | DOUBLE | NOT NULL |  | The version of the media instance. The first version is version 1. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `CONTRIBUTOR_ID` | [PRSNL](PRSNL.md) | `PERSON_ID` |
| `CREATED_BY_ID` | [PRSNL](PRSNL.md) | `PERSON_ID` |
| `DMS_CONTENT_TYPE_ID` | [DMS_CONTENT_TYPE](DMS_CONTENT_TYPE.md) | `DMS_CONTENT_TYPE_ID` |
| `DMS_REPOSITORY_ID` | [DMS_REPOSITORY](DMS_REPOSITORY.md) | `DMS_REPOSITORY_ID` |
| `LONG_BLOB_ID` | [LONG_BLOB](LONG_BLOB.md) | `LONG_BLOB_ID` |
| `LONG_TEXT_ID` | [LONG_TEXT](LONG_TEXT.md) | `LONG_TEXT_ID` |

## Referenced by (6)

| From table | Column |
|------------|--------|
| [DMS_EVENT](DMS_EVENT.md) | `DMS_MEDIA_INSTANCE_ID` |
| [DMS_MEDIA_GROUP](DMS_MEDIA_GROUP.md) | `DMS_MEDIA_CHILD_ID` |
| [DMS_MEDIA_GROUP](DMS_MEDIA_GROUP.md) | `DMS_MEDIA_PARENT_ID` |
| [DMS_MEDIA_METADATA](DMS_MEDIA_METADATA.md) | `DMS_MEDIA_INSTANCE_ID` |
| [DMS_MEDIA_SIGNATURE](DMS_MEDIA_SIGNATURE.md) | `DMS_MEDIA_INSTANCE_ID` |
| [DMS_VIEWER](DMS_VIEWER.md) | `DMS_MEDIA_INSTANCE_ID` |

