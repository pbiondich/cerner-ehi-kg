# UCM_CHARGE_ORDER_R

> Stores the activity data representing a professional charge that has been placed for a helix case.

**Description:** Unified Case Manager - Charge Order Relationship  
**Table type:** ACTIVITY  
**Primary key:** _(not published — see note)_  
**Columns:** 10

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ORDER_ID` | DOUBLE | NOT NULL | FK→ | Uniquely identifies the charge order to an order on the ORDERS table. |
| 2 | `RENDERING_PHYS_ID` | DOUBLE | NOT NULL | FK→ | Uniquely identifies the rendering physician for the charge order. |
| 3 | `SERVICE_DATE_CD` | DOUBLE | NOT NULL |  | Uniquely identifies the service date selection of this charge order. |
| 4 | `UCM_CASE_ID` | DOUBLE | NOT NULL | FK→ | Uniquely identifies the case to which this charge order is associated. |
| 5 | `UCM_CHARGE_ORDER_R_ID` | DOUBLE | NOT NULL |  | Uniquely identifies data representing a professional charge that has been placed for a helix case. |
| 6 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 7 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 8 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 9 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 10 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `ORDER_ID` | [ORDERS](ORDERS.md) | `ORDER_ID` |
| `RENDERING_PHYS_ID` | [PRSNL](PRSNL.md) | `PERSON_ID` |
| `UCM_CASE_ID` | [UCM_CASE](UCM_CASE.md) | `UCM_CASE_ID` |

