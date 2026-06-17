# DMS_REPOSITORY

> Contains media object repository information

**Description:** DMS_REPOSITORY  
**Table type:** REFERENCE  
**Primary key:** `DMS_REPOSITORY_ID`  
**Columns:** 16  
**Referenced by:** 2 columns

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ACTIVE_IND` | DOUBLE | NOT NULL |  | The table row is active or inactive. A row is generally active unless it is in an inactive state such as logically deleted, combined away, pending purge, etc. |
| 2 | `DEFAULT_IND` | DOUBLE | NOT NULL |  | This column is used to indicate the default repository |
| 3 | `DMS_REPOSITORY_ID` | DOUBLE | NOT NULL | PK | Primary dms_repository table |
| 4 | `ENCRYPTION_IND` | DOUBLE | NOT NULL |  | This column is used to indicate if the object is encrypted |
| 5 | `LOCATION` | VARCHAR(255) |  |  | Repository location |
| 6 | `OVERFLOW_ID` | DOUBLE | NOT NULL |  | The DMS_REPOSITORY_ID of the repository used to store objects that exceed the size limit |
| 7 | `PASSWORD` | VARCHAR(64) |  |  | Repository access password |
| 8 | `REPOSITORY_NAME` | VARCHAR(16) |  |  | name of the repository used |
| 9 | `SIZE_LIMIT` | DOUBLE | NOT NULL |  | This column contains the size limit for objects stored on this repository |
| 10 | `TYPE_FLAG` | DOUBLE | NOT NULL |  | This column is used to indicate the type of repository 0 - archive, 1 - share,2 - Millennium |
| 11 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 12 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 13 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 14 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 15 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 16 | `USERNAME` | VARCHAR(64) |  |  | Repository access username |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Referenced by (2)

| From table | Column |
|------------|--------|
| [DMS_CONTENT_TYPE](DMS_CONTENT_TYPE.md) | `DMS_REPOSITORY_ID` |
| [DMS_MEDIA_INSTANCE](DMS_MEDIA_INSTANCE.md) | `DMS_REPOSITORY_ID` |

