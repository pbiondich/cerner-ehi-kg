# PROFILE_TASK_R

> Used to store relationships between order catalog items and the task/assays that comprise them

**Description:** Profile Task Relationship  
**Table type:** REFERENCE  
**Primary key:** `CATALOG_CD`, `TASK_ASSAY_CD`  
**Columns:** 26  
**Referenced by:** 6 columns

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ACTIVE_IND` | DOUBLE |  |  | The table row is active or inactive. A row is generally active unless it is in an inactive state such as logically deleted, combined away, pending purge, etc. |
| 2 | `ACTIVE_STATUS_CD` | DOUBLE | NOT NULL |  | Indicates the status of the row itself (not the data in the row) such as active, inactive, combined away, pending purge, etc. |
| 3 | `ACTIVE_STATUS_DT_TM` | DATETIME |  |  | The date and time that the active_status_cd was set. |
| 4 | `ACTIVE_STATUS_PRSNL_ID` | DOUBLE | NOT NULL |  | The person who caused the active_status_cd to be set or change. |
| 5 | `BEG_EFFECTIVE_DT_TM` | DATETIME | NOT NULL |  | The date and time for which this table row becomes effective. Normally, this will be the date and time the row is added, but could be a past or future date and time. |
| 6 | `CATALOG_CD` | DOUBLE | NOT NULL | PK FK→ | A unique code value that identifies a specific order catalog item that is comprised of discrete task assays. |
| 7 | `DUP_CHK_ACTION_CD` | DOUBLE | NOT NULL |  | (Currently not implemented) |
| 8 | `DUP_CHK_MIN` | DOUBLE |  |  | (Currently not implemented) |
| 9 | `END_EFFECTIVE_DT_TM` | DATETIME | NOT NULL |  | The date/time after which the row is no longer valid as active current data. This may be valued with the date that the row became inactive. |
| 10 | `GROUP_CD` | DOUBLE | NOT NULL |  | (Currently not implemented) |
| 11 | `ITEM_TYPE_FLAG` | DOUBLE |  |  | Defines the discrete task assay item type as it relates to the order catalog procedure. |
| 12 | `PENDING_IND` | DOUBLE |  |  | Indicates whether results for this discrete task assay must be performed before the order catalog item it is associated with will be considered complete. |
| 13 | `POST_PROMPT_IND` | DOUBLE |  |  | Indicates whether results for this prompt will be posted as performed or verified. |
| 14 | `PROMPT_LONG_TEXT_ID` | DOUBLE | NOT NULL |  | A unique, internal, system-assigned number that identifies the text associated with a prompt procedure. Creates a relationship to the long text table. |
| 15 | `PROMPT_RESOURCE_CD` | DOUBLE | NOT NULL |  | A unique code value that identifies the service resource used to look up reference ranges if the discrete task assay is marked as a prompt. |
| 16 | `REFERENCE_TASK_ID` | DOUBLE | NOT NULL |  | Used to store the identifier of the task that is referenced on the order_task table for CareNet tasklists. |
| 17 | `REPEAT_IND` | DOUBLE |  |  | Indicates whether repeats will be tracked by the system. |
| 18 | `RESTRICT_DISPLAY_IND` | DOUBLE |  |  | This indicator restricts the display of discrete task assays in result entry to only those that have results associated with them. |
| 19 | `SEQUENCE` | DOUBLE |  |  | Defines the sequence in which discrete task assays will be displayed in result entry applications. |
| 20 | `TASK_ASSAY_CD` | DOUBLE | NOT NULL | PK FK→ | A unique code value that identifies the discrete task assay that is associated with the order catalog item. |
| 21 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 22 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 23 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 24 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 25 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |
| 26 | `VERSION_NBR` | DOUBLE |  |  | (Currently not implemented) |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `CATALOG_CD` | [SERVICE_DIRECTORY](SERVICE_DIRECTORY.md) | `CATALOG_CD` |
| `TASK_ASSAY_CD` | [DISCRETE_TASK_ASSAY](DISCRETE_TASK_ASSAY.md) | `TASK_ASSAY_CD` |

## Referenced by (6)

| From table | Column |
|------------|--------|
| [ORDER_TASK_PROFILE_XREF](ORDER_TASK_PROFILE_XREF.md) | `CATALOG_CD` |
| [ORDER_TASK_PROFILE_XREF](ORDER_TASK_PROFILE_XREF.md) | `TASK_ASSAY_CD` |
| [PROFILE_RESOURCE_LIST](PROFILE_RESOURCE_LIST.md) | `CATALOG_CD` |
| [PROFILE_RESOURCE_LIST](PROFILE_RESOURCE_LIST.md) | `TASK_ASSAY_CD` |
| [REPORT_INPROC_STATUS](REPORT_INPROC_STATUS.md) | `CATALOG_CD` |
| [REPORT_INPROC_STATUS](REPORT_INPROC_STATUS.md) | `TASK_ASSAY_CD` |

