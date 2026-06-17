# ASSAY_PROCESSING_R

> Stores relationships for assays and the service resouces that perform them. Used to store service resource specific information about task/assays used for result entry parameters

**Description:** Discrete Task Assay Processing Resolution  
**Table type:** REFERENCE  
**Primary key:** `LOADED_SERVICE_RESOURCE_CD`, `SERVICE_RESOURCE_CD`, `TASK_ASSAY_CD`  
**Columns:** 23  
**Referenced by:** 3 columns

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ACTIVE_IND` | DOUBLE |  |  | The table row is active or inactive. A row is generally active unless it is in an inactive state such as logically deleted, combined away, pending purge, etc. |
| 2 | `ACTIVE_STATUS_CD` | DOUBLE | NOT NULL |  | Indicates the status of the row itself (not the data in the row) such as active, inactive, combined away, pending purge, etc. |
| 3 | `ACTIVE_STATUS_DT_TM` | DATETIME |  |  | The date and time that the active_status_cd was set. |
| 4 | `ACTIVE_STATUS_PRSNL_ID` | DOUBLE | NOT NULL |  | The person who caused the active_status_cd to be set or change. |
| 5 | `CODE_SET` | DOUBLE |  |  | Used to store the code set referenced if a result type of "online code set" is chosen for a particular assay/resource combination. |
| 6 | `DEFAULT_RESULT_TEMPLATE_ID` | DOUBLE | NOT NULL | FK→ | A unique, internal, system-assigned number that identifies a specific result template to be displayed by default if a discrete task assay at the indicated service resource is resulted. Creates a relationship to the word processing template table. |
| 7 | `DEFAULT_RESULT_TYPE_CD` | DOUBLE | NOT NULL |  | A unique code value that identifies the specific default result type for the discrete task assay/service resource combination. |
| 8 | `DISPLAY_SEQUENCE` | DOUBLE |  |  | Defines the sequence number that determines the order in which the discrete task assays display in result entry applications. |
| 9 | `DNLD_ASSAY_ALIAS` | VARCHAR(100) |  |  | Defines the alias used to download the discrete task assay to a service resource that is a medical device (i.e. instrument). |
| 10 | `DOWNLD_IND` | DOUBLE |  |  | Indicates whether downloads will be performed for this service resource. |
| 11 | `LOADED_SERVICE_RESOURCE_CD` | DOUBLE | NOT NULL | PK FK→ | Service Resource where tests have been loaded. |
| 12 | `POST_ZERO_RESULT_IND` | DOUBLE |  |  | Indicates whether the system will accept zeroes as a valid result from this service resource. |
| 13 | `PROCESS_SEQUENCE` | DOUBLE |  |  | Indicates the sequence that will be used by a service resource for posting results from a medical device interface. |
| 14 | `QC_RESULT_TYPE_CD` | DOUBLE | NOT NULL |  | A unique code value that identifies a specific result type for QC samples posting from this service resource if it is a medical device (i.e. instrument). |
| 15 | `QC_SEQUENCE` | DOUBLE |  |  | Used to control the sequence of discrete task assays as they relate to quality control samples posting from a medical device service resource (i.e. instrument). |
| 16 | `SERVICE_RESOURCE_CD` | DOUBLE | NOT NULL | PK FK→ | A unique code value that identifies a specific service resource that is associated with the discrete task assay. |
| 17 | `TASK_ASSAY_CD` | DOUBLE | NOT NULL | PK FK→ | A unique code value that identifies a specific discrete task assay. |
| 18 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 19 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 20 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 21 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 22 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |
| 23 | `UPLD_ASSAY_ALIAS` | VARCHAR(25) |  |  | Defines the alias used for posting the discrete task assay back from a medical device service resource (i.e. instrument). |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `DEFAULT_RESULT_TEMPLATE_ID` | [WP_TEMPLATE](WP_TEMPLATE.md) | `TEMPLATE_ID` |
| `LOADED_SERVICE_RESOURCE_CD` | [SERVICE_RESOURCE](SERVICE_RESOURCE.md) | `SERVICE_RESOURCE_CD` |
| `SERVICE_RESOURCE_CD` | [SERVICE_RESOURCE](SERVICE_RESOURCE.md) | `SERVICE_RESOURCE_CD` |
| `TASK_ASSAY_CD` | [DISCRETE_TASK_ASSAY](DISCRETE_TASK_ASSAY.md) | `TASK_ASSAY_CD` |

## Referenced by (3)

| From table | Column |
|------------|--------|
| [ASSAY_RESOURCE_TRANSLATION](ASSAY_RESOURCE_TRANSLATION.md) | `LOADED_SERVICE_RESOURCE_CD` |
| [ASSAY_RESOURCE_TRANSLATION](ASSAY_RESOURCE_TRANSLATION.md) | `SERVICE_RESOURCE_CD` |
| [ASSAY_RESOURCE_TRANSLATION](ASSAY_RESOURCE_TRANSLATION.md) | `TASK_ASSAY_CD` |

