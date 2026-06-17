# PHA_BATCH_REPORT_ACT_DTL

> Stores the records that qualified based on the batch parameters.

**Description:** Pharmacy Batch Report Activity Detail  
**Table type:** ACTIVITY  
**Primary key:** _(not published — see note)_  
**Columns:** 19

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `CHILD_ORDER_ID` | DOUBLE | NOT NULL | FK→ | Identifies a child order associated with an original inpatient order (i.e. pass med orders) |
| 2 | `DETAIL_PROCESS_STATUS_CD` | DOUBLE | NOT NULL |  | Identifies a more detailed status for the qualified dispense. |
| 3 | `DISPENSE_HX_ID` | DOUBLE | NOT NULL | FK→ | Identifies a dispense that qualified for the batch. |
| 4 | `HEALTH_PLAN_ID` | DOUBLE | NOT NULL | FK→ | Identifies the health plan used to qualify the dispense. |
| 5 | `ORDER_ID` | DOUBLE | NOT NULL | FK→ | Identifies an inpatient order associated to the inpatient dispense. |
| 6 | `PHA_BATCH_REPORT_ACT_DTL_ID` | DOUBLE | NOT NULL |  | Unique generated number that identifies a single row on the PHA_BATCH_REPORT_ACT_DTL table. |
| 7 | `PHA_BATCH_REPORT_ACT_ID` | DOUBLE | NOT NULL | FK→ | The particular execution of the batch report that this detail i for. |
| 8 | `PROCESS_STATUS_CD` | DOUBLE | NOT NULL |  | Identifies the status for the qualified dispense. |
| 9 | `PROD_CLAIM_QTY` | DOUBLE | NOT NULL |  | Net Dispense Quantity, in terms of Dispensing Package Unit, of the product that is being claimed. |
| 10 | `PROD_DISPENSE_HX_ID` | DOUBLE | NOT NULL |  | Identifies a product associated with the dispense |
| 11 | `RX_ADMIN_DISPENSE_HX_ID` | DOUBLE | NOT NULL | FK→ | Identifies a specific administration associated with the dispense. |
| 12 | `RX_ADMIN_PROD_DISPENSE_HX_ID` | DOUBLE | NOT NULL | FK→ | Identifies a product associated with a specific administration. |
| 13 | `SERVICE_END_DT_TM` | DATETIME |  |  | Identifies the end date of when the service was provided |
| 14 | `SERVICE_START_DT_TM` | DATETIME |  |  | Identifies the start date of when the service was provided. |
| 15 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 16 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 17 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 18 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 19 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `CHILD_ORDER_ID` | [ORDERS](ORDERS.md) | `ORDER_ID` |
| `DISPENSE_HX_ID` | [DISPENSE_HX](DISPENSE_HX.md) | `DISPENSE_HX_ID` |
| `HEALTH_PLAN_ID` | [HEALTH_PLAN](HEALTH_PLAN.md) | `HEALTH_PLAN_ID` |
| `ORDER_ID` | [ORDERS](ORDERS.md) | `ORDER_ID` |
| `PHA_BATCH_REPORT_ACT_ID` | [PHA_BATCH_REPORT_ACT](PHA_BATCH_REPORT_ACT.md) | `PHA_BATCH_REPORT_ACT_ID` |
| `RX_ADMIN_DISPENSE_HX_ID` | [RX_ADMIN_DISPENSE_HX](RX_ADMIN_DISPENSE_HX.md) | `RX_ADMIN_DISPENSE_HX_ID` |
| `RX_ADMIN_PROD_DISPENSE_HX_ID` | [RX_ADMIN_PROD_DISPENSE_HX](RX_ADMIN_PROD_DISPENSE_HX.md) | `RX_ADMIN_PROD_DISPENSE_HX_ID` |

