# CONTAINER_ORG_R

> Holds the organization and it's related containers for the BB Shipping & Transfer application.

**Description:** Container Organization Reference  
**Table type:** REFERENCE  
**Primary key:** _(not published — see note)_  
**Columns:** 14

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ACTIVE_IND` | DOUBLE |  |  | The table row is active or inactive. A row is generally active unless it is in an inactive state such as logically deleted, combined away, pending purge, etc. |
| 2 | `ACTIVE_STATUS_CD` | DOUBLE | NOT NULL |  | Indicates the status of the row itself (not the data in the row) such as active, inactive, combined away, pending purge, etc. |
| 3 | `ACTIVE_STATUS_DT_TM` | DATETIME |  |  | The date and time that the active_status_cd was set. |
| 4 | `ACTIVE_STATUS_PRSNL_ID` | DOUBLE | NOT NULL |  | The person who caused the active_status_cd to be set or change. |
| 5 | `CONTAINER_ORG_ID` | DOUBLE | NOT NULL |  | Unique identifier for the CONTAINER_ORG_R table. |
| 6 | `CONTAINER_TYPE_CD` | DOUBLE | NOT NULL | FK→ | Type of container to which blood bank products can be added. |
| 7 | `INVENTORY_AREA_CD` | DOUBLE | NOT NULL |  | In addition to organizations, containers can be associated with inventory areas |
| 8 | `ORGANIZATION_ID` | DOUBLE | NOT NULL | FK→ | Unique identifier from the ORGANIZATION table. |
| 9 | `OWNER_AREA_CD` | DOUBLE | NOT NULL |  | In addition to organizations, containers can be associated with owner areas |
| 10 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 11 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 12 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 13 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 14 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `CONTAINER_TYPE_CD` | [CODE_VALUE](CODE_VALUE.md) | `CODE_VALUE` |
| `ORGANIZATION_ID` | [ORGANIZATION](ORGANIZATION.md) | `ORGANIZATION_ID` |

