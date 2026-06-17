# PRSNL_GROUP_POOL_ROUTING_R

> This table Identifies the prsnl_group_pool, it's routing rules, location and priority, used for Results to Endorse that are assigned to a prsnl_group. Data will be delted and not merged.

**Description:** Prsnl_group_pool_routing_reltn  
**Table type:** REFERENCE  
**Primary key:** _(not published — see note)_  
**Columns:** 13

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ACTIVE_IND` | DOUBLE | NOT NULL |  | The table row is active or inactive. A row is generally active unless it is in an inactive state such as logically deleted, combined away, pending purge, etc. |
| 2 | `LOCATION_CD` | DOUBLE | NOT NULL |  | The field identifies the current permanent location of the patient associated with routing rule. |
| 3 | `PRSNL_GROUP_POOL_ID` | DOUBLE | NOT NULL | FK→ | The PRSNL_GROUP_POOL_ID from the PRSNL_GROUP_POOL table |
| 4 | `PRSNL_GROUP_POOL_ROUTING_R_ID` | DOUBLE | NOT NULL |  | The ID of the table. SEQUENCE NAME:CARENET_SEQ |
| 5 | `PRSNL_ID` | DOUBLE | NOT NULL | FK→ | Personnel Id associated with routing rule |
| 6 | `ROUTE_TYPE_CD` | DOUBLE | NOT NULL |  | The code value that indicates the routing criteria |
| 7 | `ROUTING_PRIORITY_NBR` | DOUBLE | NOT NULL |  | The priority/ranking of importance for prsnl group pool routing relations |
| 8 | `SCH_FLEX_ID` | DOUBLE | NOT NULL | FK→ | The SCH_FLEX_ID from the SCH_FLEX_STRING table |
| 9 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 10 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 11 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 12 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 13 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `PRSNL_GROUP_POOL_ID` | [PRSNL_GROUP](PRSNL_GROUP.md) | `PRSNL_GROUP_ID` |
| `PRSNL_ID` | [PRSNL](PRSNL.md) | `PERSON_ID` |
| `SCH_FLEX_ID` | [SCH_FLEX_STRING](SCH_FLEX_STRING.md) | `SCH_FLEX_ID` |

