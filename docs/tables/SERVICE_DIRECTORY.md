# SERVICE_DIRECTORY

> Sub-type table of order catalog that contains more details for catalog item

**Description:** Service directory  
**Table type:** REFERENCE  
**Primary key:** `CATALOG_CD`  
**Columns:** 29  
**Referenced by:** 8 columns

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ACTIVE_DT_TM` | DATETIME |  |  | (Currently not implemented) |
| 2 | `ACTIVE_IND` | DOUBLE |  |  | The table row is active or inactive. A row is generally active unless it is in an inactive state such as logically deleted, combined away, pending purge, etc. |
| 3 | `ACTIVE_STATUS_CD` | DOUBLE | NOT NULL |  | Indicates the status of the row itself (not the data in the row) such as active, inactive, combined away, pending purge, etc. |
| 4 | `ACTIVE_STATUS_DT_TM` | DATETIME |  |  | The date and time that the active_status_cd was set. |
| 5 | `ACTIVE_STATUS_PRSNL_ID` | DOUBLE | NOT NULL |  | The person who caused the active_status_cd to be set or change. |
| 6 | `BB_DEFAULT_PHASES_CD` | DOUBLE | NOT NULL |  | A unique code value that identifies the processing code used by Blood Bank result entry to set the default phases for Blood Bank order catalog items. |
| 7 | `BB_PROCESSING_CD` | DOUBLE | NOT NULL |  | A unique code value that identifies the processing code used by Blood Bank result entry to drive prompts and workflow in the Blood Bank result entry applications. |
| 8 | `BEG_EFFECTIVE_DT_TM` | DATETIME | NOT NULL |  | The date and time for which this table row becomes effective. Normally, this will be the date and time the row is added, but could be a past or future date and time. |
| 9 | `BIOLOGICAL_CATEGORY_CD` | DOUBLE | NOT NULL |  | Denotes the origin of the sequence of the part of the DNA or RNA being tested and the species of the organism being tested (animal, bacteria, or virus) for this orderable. |
| 10 | `CATALOG_CD` | DOUBLE | NOT NULL | PK FK→ | A unique code value that identifies a specific order catalog item. |
| 11 | `CHARGE_AT_GROUP_DETAIL` | DOUBLE |  |  | (Currently not implemented) |
| 12 | `DESCRIPTION` | VARCHAR(100) |  |  | Used to store the long description of the order catalog item. |
| 13 | `DUP_CHECK_LVL_FLAG` | DOUBLE |  |  | (Currently not implemented) |
| 14 | `END_EFFECTIVE_DT_TM` | DATETIME | NOT NULL |  | The date/time after which the row is no longer valid as active current data. This may be valued with the date that the row became inactive. |
| 15 | `GROUP_IND` | DOUBLE |  |  | (Currently not implemented) |
| 16 | `INACTIVE_DT_TM` | DATETIME |  |  | (Currently not implemented) |
| 17 | `PROMPT_IND` | DOUBLE |  |  | Indicates whether the discrete task assay has been associated with an order catalog item that is marked as a prompt. |
| 18 | `RAD_FLOURO_USED_IND` | DOUBLE |  |  | *** OBSOLETE - no longer used *** Indicates whether flouroscopy is used for the procedure. |
| 19 | `RAD_ORGAN_ID` | DOUBLE | NOT NULL | FK→ | *** OBSOLETE - no longer used *** A unique, internal, system-assigned number that identifies a specific Radiology exposure value associated with the procedure. Creates a relationship to the radiology exposure values table. |
| 20 | `RAD_PROTOCOL_REQ_IND` | DOUBLE | NOT NULL |  | Indicates if this orderable requires protocolling. |
| 21 | `SHORT_DESCRIPTION` | VARCHAR(100) |  |  | Used to store the short description of the order catalog item. |
| 22 | `SPECIMEN_REQUIRED` | DOUBLE |  |  | Indicates whether a specimen is required for this order catalog item. |
| 23 | `SYNONYM_ID` | DOUBLE | NOT NULL |  | A unique, internal, system-assigned number that identifies the primary synonym for the order catalog item. Creates a relationship to the order catalog synonym table. |
| 24 | `SYSTEM_DEFINED_IND` | DOUBLE |  |  | (Currently not implemented) |
| 25 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 26 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 27 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 28 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 29 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `CATALOG_CD` | [ORDER_CATALOG](ORDER_CATALOG.md) | `CATALOG_CD` |
| `RAD_ORGAN_ID` | [RAD_EXPOSURE_VALUES](RAD_EXPOSURE_VALUES.md) | `EXPOSURE_VALUE_ID` |

## Referenced by (8)

| From table | Column |
|------------|--------|
| [DEPT_DUP_CHECK](DEPT_DUP_CHECK.md) | `CATALOG_CD` |
| [EXAM_FOLDER](EXAM_FOLDER.md) | `CATALOG_CD` |
| [EXAM_REASON](EXAM_REASON.md) | `CATALOG_CD` |
| [FILM_USAGE](FILM_USAGE.md) | `CATALOG_CD` |
| [PROFILE_TASK_R](PROFILE_TASK_R.md) | `CATALOG_CD` |
| [RAD_PROTOCOL_CATALOG_R](RAD_PROTOCOL_CATALOG_R.md) | `CATALOG_CD` |
| [REPLACE_GROUPING](REPLACE_GROUPING.md) | `CATALOG_CD` |
| [REPLACE_GROUPING](REPLACE_GROUPING.md) | `REPLACE_CATALOG_CD` |

