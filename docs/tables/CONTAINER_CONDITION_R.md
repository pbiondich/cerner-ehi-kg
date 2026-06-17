# CONTAINER_CONDITION_R

> Contains container types and their condition relationships for the BB Shipping & Transfer application.

**Description:** Container Condition Reference Table  
**Table type:** REFERENCE  
**Primary key:** `CONTAINER_CONDITION_ID`  
**Columns:** 14  
**Referenced by:** 1 columns

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ACTIVE_IND` | DOUBLE |  |  | The table row is active or inactive. A row is generally active unless it is in an inactive state such as logically deleted, combined away, pending purge, etc. |
| 2 | `ACTIVE_STATUS_CD` | DOUBLE | NOT NULL |  | Indicates the status of the row itself (not the data in the row) such as active, inactive, combined away, pending purge, etc. |
| 3 | `ACTIVE_STATUS_DT_TM` | DATETIME |  |  | The date and time that the active_status_cd was set. |
| 4 | `ACTIVE_STATUS_PRSNL_ID` | DOUBLE | NOT NULL |  | The person who caused the active_status_cd to be set or change. |
| 5 | `CNTNR_TEMPERATURE_DEGREE_CD` | DOUBLE | NOT NULL |  | Indicates the default shipment temperature degree unit of measure associated with the container. |
| 6 | `CNTNR_TEMPERATURE_VALUE` | DOUBLE | NOT NULL |  | Indicates the default shipment temperature of the container. |
| 7 | `CONDITION_CD` | DOUBLE | NOT NULL | FK→ | Container CD |
| 8 | `CONTAINER_CONDITION_ID` | DOUBLE | NOT NULL | PK | Container Condition ID |
| 9 | `CONTAINER_TYPE_CD` | DOUBLE | NOT NULL | FK→ | Container Type CD |
| 10 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 11 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 12 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 13 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 14 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `CONDITION_CD` | [CODE_VALUE](CODE_VALUE.md) | `CODE_VALUE` |
| `CONTAINER_TYPE_CD` | [CODE_VALUE](CODE_VALUE.md) | `CODE_VALUE` |

## Referenced by (1)

| From table | Column |
|------------|--------|
| [CONTNR_TYPE_PROD_R](CONTNR_TYPE_PROD_R.md) | `CONTAINER_CONDITION_ID` |

