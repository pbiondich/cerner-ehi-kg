# SR_RESOURCE_GROUP_HIST

> History table used to track active relationships between parent and child service resources.

**Description:** Service Resource Resource Group History  
**Table type:** REFERENCE  
**Primary key:** _(not published — see note)_  
**Columns:** 13

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ACTIVE_IND` | DOUBLE | NOT NULL |  | The table row is active or inactive. A row is generally active unless it is in an inactive state such as logically deleted, combined away, pending purge, etc. |
| 2 | `BEG_EFFECTIVE_DT_TM` | DATETIME | NOT NULL |  | The date and time for which this table row becomes effective. Normally, this will be the date and time the row is added, but could be a past or future date and time. |
| 3 | `CHILD_SERVICE_RESOURCE_CD` | DOUBLE | NOT NULL | FK→ | The "child" in a resource to resource relationship. If the relationship is Department to Section, Department is the "parent" and Section is the "child". It is a unique internal identifier. |
| 4 | `END_EFFECTIVE_DT_TM` | DATETIME | NOT NULL |  | The date/time after which the row is no longer valid as active current data. This may be valued with the date that the row became inactive. |
| 5 | `PARENT_SERVICE_RESOURCE_CD` | DOUBLE | NOT NULL | FK→ | The "parent" in a resource to resource relationship. If the relationship is Department to Section, Department is the "parent" and Section is the "child". It is a unique internal identifier. |
| 6 | `RESOURCE_GROUP_TYPE_CD` | DOUBLE | NOT NULL | FK→ | The definition of the relationship. Generally it is the resource type associated with the parent's resource type. Each type has a Cerner defined cdf_meaning associated with it. |
| 7 | `ROOT_SERVICE_RESOURCE_CD` | DOUBLE | NOT NULL | FK→ | Used when creating "views". It is the internal identifier for the highest resource node in the view. Used to programmatically retrieve all levels in a view quickly. If the view is the "Master", root code will be zero. |
| 8 | `SR_RESOURCE_GROUP_HIST_ID` | DOUBLE | NOT NULL |  | The unique primary key of this table. It is an internally generated number. |
| 9 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 10 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 11 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 12 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 13 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `CHILD_SERVICE_RESOURCE_CD` | [RESOURCE_GROUP](RESOURCE_GROUP.md) | `CHILD_SERVICE_RESOURCE_CD` |
| `PARENT_SERVICE_RESOURCE_CD` | [RESOURCE_GROUP](RESOURCE_GROUP.md) | `PARENT_SERVICE_RESOURCE_CD` |
| `RESOURCE_GROUP_TYPE_CD` | [RESOURCE_GROUP](RESOURCE_GROUP.md) | `RESOURCE_GROUP_TYPE_CD` |
| `ROOT_SERVICE_RESOURCE_CD` | [RESOURCE_GROUP](RESOURCE_GROUP.md) | `ROOT_SERVICE_RESOURCE_CD` |

