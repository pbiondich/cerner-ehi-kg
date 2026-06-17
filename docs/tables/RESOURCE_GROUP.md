# RESOURCE_GROUP

> Relationship table which associates one resource to another such as Institution to Department, Department to Section , etc.

**Description:** Service Resource Group  
**Table type:** REFERENCE  
**Primary key:** `CHILD_SERVICE_RESOURCE_CD`, `PARENT_SERVICE_RESOURCE_CD`, `RESOURCE_GROUP_TYPE_CD`, `ROOT_SERVICE_RESOURCE_CD`  
**Columns:** 17  
**Referenced by:** 4 columns

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ACTIVE_IND` | DOUBLE |  |  | The table row is active or inactive. A row is generally active unless it is in an inactive state such as logically deleted, combined away, pending purge, etc. |
| 2 | `ACTIVE_STATUS_CD` | DOUBLE | NOT NULL |  | Indicates the status of the row itself (not the data in the row) such as active, inactive, combined away, pending purge, etc. |
| 3 | `ACTIVE_STATUS_DT_TM` | DATETIME |  |  | The date and time that the active_status_cd was set. |
| 4 | `ACTIVE_STATUS_PRSNL_ID` | DOUBLE | NOT NULL |  | The person who caused the active_status_cd to be set or change. |
| 5 | `BEG_EFFECTIVE_DT_TM` | DATETIME | NOT NULL |  | The date and time for which this table row becomes effective. Normally, this will be the date and time the row is added, but could be a past or future date and time. |
| 6 | `CHILD_SERVICE_RESOURCE_CD` | DOUBLE | NOT NULL | PK FK→ | The "child" in a resource to resource relationship. If the relationship is Department to Section, Department is the "parent" and Section is the "child". It is a unique internal identifier. |
| 7 | `END_EFFECTIVE_DT_TM` | DATETIME | NOT NULL |  | The date/time after which the row is no longer valid as active current data. This may be valued with the date that the row became inactive. |
| 8 | `PARENT_SERVICE_RESOURCE_CD` | DOUBLE | NOT NULL | PK FK→ | The "parent" in a resource to resource relationship. If the relationship is Department to Section, Department is the "parent" and Section is the "child". It is a unique internal identifier. |
| 9 | `RESOURCE_GROUP_TYPE_CD` | DOUBLE | NOT NULL | PK | The definition of the relationship. Generally it is the resource type associated with the parent's resource type. Each type has a Cerner defined cdf_meaning associated with it. |
| 10 | `ROOT_SERVICE_RESOURCE_CD` | DOUBLE | NOT NULL | PK FK→ | Used when creating "views". It is the internal identifier for the highest resource node in the view. Used to programmatically retrieve all levels in a view quickly. If the view is the "Master", root code will be zero. |
| 11 | `SEQUENCE` | DOUBLE |  |  | An internal value to order or sequence multiple children of a single parent. |
| 12 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 13 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 14 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 15 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 16 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |
| 17 | `VIEW_TYPE_CD` | DOUBLE |  |  | Precursor to root_service_resource_cd. Needed for the conversion utility "LOC_CONVERT_VIEW_TYPES". The attribute is not used and will be removed. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `CHILD_SERVICE_RESOURCE_CD` | [SERVICE_RESOURCE](SERVICE_RESOURCE.md) | `SERVICE_RESOURCE_CD` |
| `PARENT_SERVICE_RESOURCE_CD` | [SERVICE_RESOURCE](SERVICE_RESOURCE.md) | `SERVICE_RESOURCE_CD` |
| `ROOT_SERVICE_RESOURCE_CD` | [CODE_VALUE](CODE_VALUE.md) | `CODE_VALUE` |

## Referenced by (4)

| From table | Column |
|------------|--------|
| [SR_RESOURCE_GROUP_HIST](SR_RESOURCE_GROUP_HIST.md) | `CHILD_SERVICE_RESOURCE_CD` |
| [SR_RESOURCE_GROUP_HIST](SR_RESOURCE_GROUP_HIST.md) | `PARENT_SERVICE_RESOURCE_CD` |
| [SR_RESOURCE_GROUP_HIST](SR_RESOURCE_GROUP_HIST.md) | `RESOURCE_GROUP_TYPE_CD` |
| [SR_RESOURCE_GROUP_HIST](SR_RESOURCE_GROUP_HIST.md) | `ROOT_SERVICE_RESOURCE_CD` |

