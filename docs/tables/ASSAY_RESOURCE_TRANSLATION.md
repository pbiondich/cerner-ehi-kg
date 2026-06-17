# ASSAY_RESOURCE_TRANSLATION

> Contains discrete assay functionality (e.g., download y/n, upld alias, dnld alias, etc.) information by model that is required by the medical device interface to process the assay.

**Description:** Contains discrete assay information.  
**Table type:** REFERENCE  
**Primary key:** _(not published — see note)_  
**Columns:** 16

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ACTIVE_IND` | DOUBLE |  |  | The table row is active or inactive. A row is generally active unless it is in an inactive state such as logically deleted, combined away, pending purge, etc. |
| 2 | `ACTIVE_STATUS_CD` | DOUBLE | NOT NULL |  | Indicates the status of the row itself (not the data in the row) such as active, inactive, combined away, pending purge, etc. |
| 3 | `ACTIVE_STATUS_DT_TM` | DATETIME |  |  | The date and time that the active_status_cd was set. |
| 4 | `ACTIVE_STATUS_PRSNL_ID` | DOUBLE | NOT NULL |  | The person who caused the active_status_cd to be set or change. |
| 5 | `DECIMAL_MOVEMENT_NBR` | DOUBLE |  |  | Defines the decimal movement to be performed by the MDI Result server (231) on the result value obtained from the interface. This column would be updated by MDI Install tool while configuring the interface. |
| 6 | `LOADED_SERVICE_RESOURCE_CD` | DOUBLE | NOT NULL | FK→ | Service Resource where tests have been loaded. |
| 7 | `POST_ZERO_RESULT_IND` | DOUBLE |  |  | Contains a Boolean character to indicate if the user wants a value of 0 (zero) to post when received by the analyzer. |
| 8 | `PROCESS_SEQUENCE` | DOUBLE |  |  | Reserved for future use. |
| 9 | `SERVICE_RESOURCE_CD` | DOUBLE | NOT NULL | FK→ | Contains the service resource code of the analyzer. |
| 10 | `TASK_ASSAY_CD` | DOUBLE | NOT NULL | FK→ | Contains the DBMS assigned unique key field value from discrete_task_assay table. |
| 11 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 12 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 13 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 14 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 15 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |
| 16 | `UPLD_ASSAY_ALIAS` | VARCHAR(25) | NOT NULL |  | Contains the test mnemonic sent by the analyzer for a discrete assay. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `LOADED_SERVICE_RESOURCE_CD` | [ASSAY_PROCESSING_R](ASSAY_PROCESSING_R.md) | `LOADED_SERVICE_RESOURCE_CD` |
| `SERVICE_RESOURCE_CD` | [ASSAY_PROCESSING_R](ASSAY_PROCESSING_R.md) | `SERVICE_RESOURCE_CD` |
| `TASK_ASSAY_CD` | [ASSAY_PROCESSING_R](ASSAY_PROCESSING_R.md) | `TASK_ASSAY_CD` |

