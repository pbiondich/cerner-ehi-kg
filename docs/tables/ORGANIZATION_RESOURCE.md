# ORGANIZATION_RESOURCE

> Organization Resource

**Description:** Relationship between orgs and resources for reference lab concept in charting  
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
| 5 | `ORG_RESOURCE_TYPE_CD` | DOUBLE | NOT NULL | FK→ | Identifies the type of relationship between organizations and resources. For this table, it will generally be "Reference Lab" |
| 6 | `ORG_RES_ID` | DOUBLE | NOT NULL |  | An unique internal identifier for the relationship. |
| 7 | `PARENT_ENTITY_ID` | DOUBLE | NOT NULL |  | The organization's id or the location's cd. Associated with the patient's location or organization. |
| 8 | `PARENT_ENTITY_NAME` | VARCHAR(25) |  |  | The table name for the parent entity id. Will most likely be either organization or location |
| 9 | `REF_LAB_DESCRIPTION` | VARCHAR(100) |  |  | A text description which should be used on the chart to identify the resource which performed the work |
| 10 | `REF_LAB_IND` | DOUBLE |  |  | If set to 0, the resource is considered part of the organization in the relationship and charting will not attempt to identify work done by the resource with a footnote since the chart header should be indicative of the organization. If set to 1, the resource is NOT considered part of the organization in the relationship and charting WILL identify work done by the resource with either a footnote or in a reference lab chart section of the chart format. |
| 11 | `SERVICE_RESOURCE_CD` | DOUBLE | NOT NULL | FK→ | An internal identifier for the resource in the relationship. |
| 12 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 13 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 14 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 15 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 16 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `ORG_RESOURCE_TYPE_CD` | [CODE_VALUE](CODE_VALUE.md) | `CODE_VALUE` |
| `SERVICE_RESOURCE_CD` | [SERVICE_RESOURCE](SERVICE_RESOURCE.md) | `SERVICE_RESOURCE_CD` |

