# CDI_ARCHIVE

> Stores archives configured for CPDI.

**Description:** CPDI Archive  
**Table type:** REFERENCE  
**Primary key:** `CDI_ARCHIVE_ID`  
**Columns:** 12  
**Referenced by:** 1 columns

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ARCHIVE_CREDENTIALS` | VARCHAR(1200) | NOT NULL |  | The encrypted credentials used to access the archive. |
| 2 | `ARCHIVE_NAME` | VARCHAR(255) | NOT NULL |  | The name of the archive. |
| 3 | `ARCHIVE_URL` | VARCHAR(255) | NOT NULL |  | The URL of the archive. This should include the fully qualified domain name and use a name recognized by DNS rather than an ip address. |
| 4 | `CDI_ARCHIVE_ID` | DOUBLE | NOT NULL | PK | Unique generated number that identifies a single row on the CDI_ARCHIVE table. |
| 5 | `DOMAIN_NAME` | VARCHAR(20) |  |  | The short domain name this archive configuration belongs to. This column prevents domain copies resulting in the wrong configuration being used. |
| 6 | `HISTORICAL_IND` | DOUBLE | NOT NULL |  | Indicates that this archive contains all historical documents. This is the destination archive when migrating images from any other location. 1= Historical |
| 7 | `LOGICAL_DOMAIN_ID` | DOUBLE | NOT NULL | FK→ | The unique identifier for a logical domain. This identifier allows the data to be grouped by logical domain. For example, If you assign clients a logical_domain_id this would allow you to store data for multiple clients on this table. |
| 8 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 9 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 10 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 11 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 12 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `LOGICAL_DOMAIN_ID` | [LOGICAL_DOMAIN](LOGICAL_DOMAIN.md) | `LOGICAL_DOMAIN_ID` |

## Referenced by (1)

| From table | Column |
|------------|--------|
| [CDI_ARCHIVE_FOLDER_RELTN](CDI_ARCHIVE_FOLDER_RELTN.md) | `CDI_ARCHIVE_ID` |

