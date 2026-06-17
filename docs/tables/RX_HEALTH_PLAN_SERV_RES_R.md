# RX_HEALTH_PLAN_SERV_RES_R

> Stores the relationship between a pharmacy health plan and a service resource. Pharmacy health plans can be mapped to one or more service resources. This relationship will be used in Retail medication manager to decide if the selected health plan is enabled for the service resource to process 'HAAD claims'. This applies to Middle east claims only currently.

**Description:** Pharmacy Health Plan Service Resource Relation  
**Table type:** REFERENCE  
**Primary key:** _(not published — see note)_  
**Columns:** 8

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `HEALTH_PLAN_ID` | DOUBLE | NOT NULL | FK→ | The health plan that is mapped to this service resource. |
| 2 | `RX_HEALTH_PLAN_SERV_RES_R_ID` | DOUBLE | NOT NULL |  | Unique, generated number that identifies a single row on the RX_HEALTH_PLAN_SERV_RES_R table. |
| 3 | `SERVICE_RESOURCE_CD` | DOUBLE | NOT NULL | FK→ | The service resource that is mapped to the pharmacy health plan on the same row. |
| 4 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 5 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 6 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 7 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 8 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `HEALTH_PLAN_ID` | [RX_HEALTH_PLAN](RX_HEALTH_PLAN.md) | `HEALTH_PLAN_ID` |
| `SERVICE_RESOURCE_CD` | [SERVICE_RESOURCE](SERVICE_RESOURCE.md) | `SERVICE_RESOURCE_CD` |

