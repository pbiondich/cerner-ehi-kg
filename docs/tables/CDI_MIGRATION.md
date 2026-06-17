# CDI_MIGRATION

> This table contains identifiers of objects that need to be migrated from CAMM 6 to CAMM 7 as well as its status (ready, migrated, deleted)

**Description:** cdi_migration  
**Table type:** ACTIVITY  
**Primary key:** _(not published — see note)_  
**Columns:** 15

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `AX_APPID` | DOUBLE |  |  | The applicationxtender application ID that corresponded to this CAMM Archive object identifier. This is used to track where to restart the migration fill if it is stopped. |
| 2 | `AX_OBJECTID` | DOUBLE |  |  | The applicationxtender object ID that corresponded to this CAMM Archive object identifier. This is used to track where to restart the migration fill if it is stopped. |
| 3 | `AX_PAGE` | DOUBLE |  |  | The applicationxtender page ID that corresponds to this CAMM Archive object identifier. This is used to track where to restart the migration fill if it is stopped. |
| 4 | `AX_PATHID` | DOUBLE |  |  | The path id in ApplicationXtender that was used to create this row. |
| 5 | `BLOB_HANDLE` | VARCHAR(255) |  |  | Allows system engineer running migrations to more easily correlate documents failing migration to affected patients, if a document should fail to migrate. In support of Cures All Patient Export PN 10531824, requirement for CAMM 7 for all-patient export. |
| 6 | `CDI_MIGRATION_ID` | DOUBLE | NOT NULL |  | Unique generated number that identifies a single row on the cdi_migration table. |
| 7 | `DELETED_ID` | DOUBLE |  |  | Indicates if an object identified by the object_ident column has been deleted from CAMM. A null value indicates that this object has not been deleted. If the object has been deleted from CAMM, this must match the value of the cdi_migration_ID column. This column is designed so that in the case that the application must restart, the application can quickly find its position in the deleting queue. |
| 8 | `DELETED_TS` | DATETIME(6) |  |  | Indicates when this object was deleted from CAMM 6. This is used for troubleshooting purposes. |
| 9 | `ENQUEUED_TS` | DATETIME(6) |  |  | Indicates when this object was enqueued in this table to be migrated. This is used for troubleshooting purposes. |
| 10 | `FROM_LOCATION` | VARCHAR(128) |  |  | The base URL of the CAMM 6 archive that the object was copied from. |
| 11 | `MIGRATED_ID` | DOUBLE |  |  | Indicates if an object identified by the object_ident column has been migrated from CAMM 6 to CAMM 7. A null value indicates that this object has not been migrated. If the object has been migrated from CAMM 6 to CAMM 7, this must match the value of the cdi_migration_ID column. This column is designed so that in the case that the application must restart, the application can quickly find its position in the migrating queue. |
| 12 | `MIGRATED_TS` | DATETIME(6) |  |  | Indicates when this object was migrated from CAMM 6 to CAMM 7. This is used for troubleshooting purposes. |
| 13 | `OBJECT_IDENT` | VARCHAR(128) |  |  | The unique identifier that identifies this object. |
| 14 | `STATUS_FLAG` | DOUBLE | NOT NULL |  | Indicates the status of the migration. The Migration status could have one of the following values:0 - Ready to migrate1 - Successfully migrated2 - Failure migrating3 - Successfully deleted |
| 15 | `TO_LOCATION` | VARCHAR(128) |  |  | The base URL of the CAMM 7 archive that the object was copied to. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

