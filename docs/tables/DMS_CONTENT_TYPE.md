# DMS_CONTENT_TYPE

> Contains information about the general classification of media items.

**Description:** Digital media services content type.  
**Table type:** REFERENCE  
**Primary key:** `DMS_CONTENT_TYPE_ID`  
**Columns:** 22  
**Referenced by:** 4 columns

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ACCESS_FLAG` | DOUBLE | NOT NULL |  | This flag will be used by solutions to determine access privileges. 0 - No access, 1-Read access, 2 - Write access, 3 - Read/Write access. |
| 2 | `ACTIVE_IND` | DOUBLE | NOT NULL |  | The table row is active or inactive. A row is generally active unless it is in an inactive state such as logically deleted, combined away, pending purge, etc. |
| 3 | `AUDIT_IND` | DOUBLE | NOT NULL |  | Indicator used to enable or disable auditing for events on objects with this content type. |
| 4 | `AUDIT_NAME` | VARCHAR(64) |  |  | The name of the audit event to use for this content type. |
| 5 | `CERNER_IND` | DOUBLE | NOT NULL |  | This column is used to identify Cerner defined content types. |
| 6 | `CONTENT_GROUP_NAME` | VARCHAR(32) |  |  | Grouping mechanism used for storage usage reporting. |
| 7 | `CONTENT_TYPE_KEY` | VARCHAR(32) | NOT NULL |  | The content type key (no spaces, all uppercase) |
| 8 | `DESCRIPTION` | VARCHAR(255) | NOT NULL |  | The description of the content type |
| 9 | `DISPLAY` | VARCHAR(60) | NOT NULL |  | The display name of the content type |
| 10 | `DMS_CONTENT_TYPE_ID` | DOUBLE | NOT NULL | PK | Unique identifier for this row |
| 11 | `DMS_REPOSITORY_ID` | DOUBLE | NOT NULL | FK→ | Foreign key to the DMS_REPOSITORY table. |
| 12 | `EXPIRATION_DURATION` | DOUBLE | NOT NULL |  | The length of time (in days) to keep media instances of this content type. |
| 13 | `MAX_VERSIONS` | DOUBLE | NOT NULL |  | The maximum versions that can be stored for media instances of this content type |
| 14 | `METADATA_TABLE_EXISTS` | DOUBLE | NOT NULL |  | An indicator used to determine if XML Metadata queries are allowed. |
| 15 | `OWNERSHIP_IND` | DOUBLE | NOT NULL |  | Indicates if ownership is allowed or not. |
| 16 | `SIGNATURE_REQ_IND` | DOUBLE | NOT NULL |  | Used to indicate if digital signatures are required for a content type. If set to 0 then digital signatures are not required to save a media instance with this content type. If set to 1 then digital signatures are required to save a media instance with this content type. |
| 17 | `TEMPORARY_IND` | DOUBLE | NOT NULL |  | Indicates the temporal nature of the content |
| 18 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 19 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 20 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 21 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 22 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `DMS_REPOSITORY_ID` | [DMS_REPOSITORY](DMS_REPOSITORY.md) | `DMS_REPOSITORY_ID` |

## Referenced by (4)

| From table | Column |
|------------|--------|
| [DMS_EVENT_REASON_R](DMS_EVENT_REASON_R.md) | `DMS_CONTENT_TYPE_ID` |
| [DMS_MEDIA_INSTANCE](DMS_MEDIA_INSTANCE.md) | `DMS_CONTENT_TYPE_ID` |
| [DMS_MEDIA_METADATA_REF](DMS_MEDIA_METADATA_REF.md) | `DMS_CONTENT_TYPE_ID` |
| [DMS_VIEWER](DMS_VIEWER.md) | `CONTENT_TYPE_ID` |

