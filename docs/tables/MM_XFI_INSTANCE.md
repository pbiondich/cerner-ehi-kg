# MM_XFI_INSTANCE

> This table will hold item's instance data sent from 3rd party system. Data in this table is moved to MM_INSTANCE.

**Description:** Interface Instance  
**Table type:** REFERENCE  
**Primary key:** `TRANSACTION_ID`  
**Columns:** 35  
**Referenced by:** 2 columns

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ACTION_FLAG` | DOUBLE | NOT NULL |  | Determines instance upload action -- create / update / delete.1 for create or update, 2 for create only, 3 for update only and 5 for delete." |
| 2 | `BATCH_GROUP_ID` | DOUBLE |  | FK→ | Grouper TRANSACTION_ID for a set of MM_XFI_INSTANCE rows in order to perform batch processing on a subset of rows. |
| 3 | `CONTRIBUTOR_CD` | DOUBLE | NOT NULL |  | Foreign contributor code value for instance sync interface. |
| 4 | `CONTRIBUTOR_TXT` | VARCHAR(40) |  |  | Contributor can be the foreign system name if being used as an interface. Used to populate IDENTIFIER.Contributor_cd |
| 5 | `CONTROL_IDENT` | VARCHAR(400) | NOT NULL |  | Identifier assigned to an individual occurrence of an item.Used to populate MM_INSTANCE.control_ident and IDENTIFIER.value |
| 6 | `CREATE_DT_TM` | DATETIME | NOT NULL |  | Contains the date and time the instance was created. |
| 7 | `INSTANCE_IDENT` | VARCHAR(400) | NOT NULL |  | Identifier assigned to an individual occurrence of an item. |
| 8 | `INSTANCE_IDENT_ID` | DOUBLE | NOT NULL | FK→ | Identifier assigned to an individual occurrence of an item. |
| 9 | `ITEM_ID` | DOUBLE | NOT NULL | FK→ | This column represents the item that this occurrence is a part of. |
| 10 | `ITEM_IDENTIFIER` | VARCHAR(255) |  |  | Item identifier passed through the interface or upload to identify an item.Used to populate MM_INSTANCE.item_id |
| 11 | `ITEM_IDENTIFIER_TYPE_CD` | DOUBLE | NOT NULL |  | Identifies the type of identifier passed in. |
| 12 | `ITEM_IDENTIFIER_TYPE_TXT` | VARCHAR(40) |  |  | Item identifier type passed through the interface or upload to identify an item. String in this column will be resolved to a corresponding code value. |
| 13 | `LOGICAL_DOMAIN_ID` | DOUBLE | NOT NULL | FK→ | The unique identifier for a logical domain. This identifier allows the data to be grouped by logical domain. For example, If you assign clients a logical_domain_id this would allow you to store data for multiple clients on this table. |
| 14 | `MFR_CD` | DOUBLE | NOT NULL | FK→ | Codified value of the resolved manufacturer. |
| 15 | `MFR_NAME` | VARCHAR(60) |  |  | The manufacturer of the item.Used to populate MM_INSTANCE.mfr_cd |
| 16 | `MM_INSTANCE_ID` | DOUBLE | NOT NULL | FK→ | An ID identifier assigned to an individual occurrence of an item. |
| 17 | `MODEL_NBR_TXT` | VARCHAR(60) |  |  | The model number of this occurrence of an item. Used to populate MM_INSTAINCE.model_nbr_txt |
| 18 | `ORGANIZATION_ID` | DOUBLE | NOT NULL | FK→ | The identifier for the organization where the object is stored. |
| 19 | `ORGANIZATION_NAME` | VARCHAR(100) | NOT NULL |  | The organization where the instance is stored. |
| 20 | `PART_NBR_TXT` | VARCHAR(60) |  |  | The model number of this occurrence of an item. Used to populate MM_INSTANCE.part_nbr_txt |
| 21 | `PROCESS_FLAG` | DOUBLE | NOT NULL |  | Defines the state of the row in the upload process. |
| 22 | `SEGMENT_IDENTIFIER` | VARCHAR(10) | NOT NULL |  | Identifies type of upload. Enter EII for equipment item instance upload. |
| 23 | `SEGMENT_VERSION` | VARCHAR(10) | NOT NULL |  | Identifies version of the upload interface. |
| 24 | `SERIAL_NBR_ID` | DOUBLE | NOT NULL | FK→ | Identifier id for the serial number |
| 25 | `SERIAL_NBR_TXT` | VARCHAR(255) |  |  | Identifier assigned to an instance of an item. Used to populate IDENTIFIER.value |
| 26 | `STATUS_CD` | DOUBLE | NOT NULL |  | Code value that indicates the current status of the instance. Examples: Available, In use, Out of service. |
| 27 | `STATUS_DISPLAY_TXT` | VARCHAR(100) |  |  | The status as displayed to the user. |
| 28 | `STORAGE_LOCATION_CD` | DOUBLE | NOT NULL | FK→ | An instance has a location where it is kept when not in use. This location represents that storage location. |
| 29 | `STORAGE_LOCATION_TXT` | VARCHAR(100) |  |  | An instance has a location where it is kept when not in use. This location represents that storage location. Used to populate MM_INSTANCE.storage_location_cd |
| 30 | `TRANSACTION_ID` | DOUBLE | NOT NULL | PK | Unique, generated number that identifies a single row on the MM_XFI_INSTANCE table. |
| 31 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 32 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 33 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 34 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 35 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `BATCH_GROUP_ID` | [MM_XFI_INSTANCE](MM_XFI_INSTANCE.md) | `TRANSACTION_ID` |
| `INSTANCE_IDENT_ID` | [IDENTIFIER](IDENTIFIER.md) | `IDENTIFIER_ID` |
| `ITEM_ID` | [ITEM_DEFINITION](ITEM_DEFINITION.md) | `ITEM_ID` |
| `LOGICAL_DOMAIN_ID` | [LOGICAL_DOMAIN](LOGICAL_DOMAIN.md) | `LOGICAL_DOMAIN_ID` |
| `MFR_CD` | [SERVICE_RESOURCE](SERVICE_RESOURCE.md) | `SERVICE_RESOURCE_CD` |
| `MM_INSTANCE_ID` | [MM_INSTANCE](MM_INSTANCE.md) | `MM_INSTANCE_ID` |
| `ORGANIZATION_ID` | [ORGANIZATION](ORGANIZATION.md) | `ORGANIZATION_ID` |
| `SERIAL_NBR_ID` | [IDENTIFIER](IDENTIFIER.md) | `IDENTIFIER_ID` |
| `STORAGE_LOCATION_CD` | [LOCATION](LOCATION.md) | `LOCATION_CD` |

## Referenced by (2)

| From table | Column |
|------------|--------|
| [MM_XFI_INSTANCE](MM_XFI_INSTANCE.md) | `BATCH_GROUP_ID` |
| [MM_XFI_INSTANCE_BATCH](MM_XFI_INSTANCE_BATCH.md) | `BATCH_GROUP_ID` |

