# RX_INPT_CLAIM_HX

> Track the linking of Inpatient Dispense events and their related Outpatient claims

**Description:** Pharmacy Inpatient Claim History  
**Table type:** ACTIVITY  
**Primary key:** _(not published — see note)_  
**Columns:** 24

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ACTIVE_IND` | DOUBLE | NOT NULL |  | The table row is active or inactive. A row is generally active unless it is in an inactive state such as logically deleted, combined away, pending purge, etc. |
| 2 | `CHILD_ORDER_ID` | DOUBLE | NOT NULL | FK→ | Identifies an inpatient child order associated with an original inpatient order (i.e. pass med orders) |
| 3 | `DETAIL_PROCESS_STATUS_CD` | DOUBLE | NOT NULL |  | Identifies a more detailed status for the qualified dispense. |
| 4 | `DISPENSE_HX_ID` | DOUBLE | NOT NULL | FK→ | Identifies an inpatient dispense that was processed |
| 5 | `HEALTH_PLAN_ID` | DOUBLE | NOT NULL | FK→ | Identifies the health plan used to qualify the inpatient dispense |
| 6 | `OP_ACTION_SEQUENCE` | DOUBLE | NOT NULL | FK→ | Identifies the outpatient action that initiated the fill action |
| 7 | `OP_DISPENSE_HX_ID` | DOUBLE | NOT NULL | FK→ | Identifies an outpatient dispense that was created for the outpatient order |
| 8 | `OP_ORDER_ID` | DOUBLE | NOT NULL | FK→ | Identifies an outpatient order associated to the inpatient order |
| 9 | `OP_RX_CLAIM_ID` | DOUBLE | NOT NULL | FK→ | Identifies the outpatient claim that was created for the outpatient dispense |
| 10 | `ORDER_ID` | DOUBLE | NOT NULL | FK→ | Identifies an inpatient order associated to the inpatient dispense |
| 11 | `PROCESS_DT_TM` | DATETIME | NOT NULL |  | Identifies the date of when the outpatient claim was processed |
| 12 | `PROCESS_STATUS_CD` | DOUBLE | NOT NULL |  | Identifies the status for the inpatient dispense |
| 13 | `PROD_CLAIM_QTY` | DOUBLE | NOT NULL |  | Identifies the net dispense quantity, in terms of base package unit, of the product that is being claimed |
| 14 | `PROD_DISPENSE_HX_ID` | DOUBLE | NOT NULL |  | Identifies a product associated with the inpatient dispense |
| 15 | `RX_ADMIN_DISPENSE_HX_ID` | DOUBLE | NOT NULL | FK→ | Identifies a specific administration associated with the inpatient dispense |
| 16 | `RX_ADMIN_PROD_DISPENSE_HX_ID` | DOUBLE | NOT NULL | FK→ | Identifies a product associated with a specific administration |
| 17 | `RX_INPT_CLAIM_HX_ID` | DOUBLE | NOT NULL |  | Unique generated number that identifies a single row on the RX_INPT_CLAIM_HX table. |
| 18 | `SERVICE_END_DT_TM` | DATETIME |  |  | Identifies the end date of when the service was provided |
| 19 | `SERVICE_START_DT_TM` | DATETIME |  |  | Identifies the begin date of when the service was provided |
| 20 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 21 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 22 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 23 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 24 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `CHILD_ORDER_ID` | [ORDERS](ORDERS.md) | `ORDER_ID` |
| `DISPENSE_HX_ID` | [DISPENSE_HX](DISPENSE_HX.md) | `DISPENSE_HX_ID` |
| `HEALTH_PLAN_ID` | [HEALTH_PLAN](HEALTH_PLAN.md) | `HEALTH_PLAN_ID` |
| `OP_ACTION_SEQUENCE` | [ORDER_ACTION](ORDER_ACTION.md) | `ACTION_SEQUENCE` |
| `OP_DISPENSE_HX_ID` | [DISPENSE_HX](DISPENSE_HX.md) | `DISPENSE_HX_ID` |
| `OP_ORDER_ID` | [ORDER_ACTION](ORDER_ACTION.md) | `ORDER_ID` |
| `OP_RX_CLAIM_ID` | [RX_CLAIM](RX_CLAIM.md) | `RX_CLAIM_ID` |
| `ORDER_ID` | [ORDERS](ORDERS.md) | `ORDER_ID` |
| `RX_ADMIN_DISPENSE_HX_ID` | [RX_ADMIN_DISPENSE_HX](RX_ADMIN_DISPENSE_HX.md) | `RX_ADMIN_DISPENSE_HX_ID` |
| `RX_ADMIN_PROD_DISPENSE_HX_ID` | [RX_ADMIN_PROD_DISPENSE_HX](RX_ADMIN_PROD_DISPENSE_HX.md) | `RX_ADMIN_PROD_DISPENSE_HX_ID` |

