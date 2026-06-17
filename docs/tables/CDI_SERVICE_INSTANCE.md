# CDI_SERVICE_INSTANCE

> This table tracks installed/running CDI server instances

**Description:** Cerner Document Imaging Service Instance  
**Table type:** REFERENCE  
**Primary key:** `CDI_SERVICE_INSTANCE_ID`  
**Columns:** 12  
**Referenced by:** 1 columns

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `CDI_SERVICE_INSTANCE_ID` | DOUBLE | NOT NULL | PK | Unique generated number that identifies a single row on the CDI_SERVICE_INSTANCE table. |
| 2 | `HOST_NAME` | VARCHAR(50) |  |  | The services host machine name. |
| 3 | `LOGICAL_DOMAIN_ID` | DOUBLE |  | FK→ | The unique identifier for a logical domain. This identifier allows the data to be grouped by logical domain. For example, If you assign clients a logical_domain_id this would allow you to store data for multiple clients on this table. |
| 4 | `REGISTER_DT_TM` | DATETIME |  |  | The last date and time that this service instance was executed. |
| 5 | `SERVICE_NAME` | VARCHAR(50) |  |  | The name of the service instance. |
| 6 | `SERVICE_TYPE_FLAG` | DOUBLE |  |  | Identifies this service instances service type. |
| 7 | `SERVICE_USERNAME` | VARCHAR(50) |  |  | The username of the user that the service is running under. |
| 8 | `UPDT_APPLCTX` | DOUBLE |  |  | The application context number from the record info block. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 9 | `UPDT_CNT` | DOUBLE |  |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 10 | `UPDT_DT_TM` | DATETIME |  |  | The date and time the row was last inserted or updated. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 11 | `UPDT_ID` | DOUBLE |  |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 12 | `UPDT_TASK` | DOUBLE |  |  | The registered (assigned) task number for the process that inserted or updated the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `LOGICAL_DOMAIN_ID` | [LOGICAL_DOMAIN](LOGICAL_DOMAIN.md) | `LOGICAL_DOMAIN_ID` |

## Referenced by (1)

| From table | Column |
|------------|--------|
| [CDI_IMPORT_TYPE_SERVICE_R](CDI_IMPORT_TYPE_SERVICE_R.md) | `CDI_SERVICE_INSTANCE_ID` |

