# MM_CS_PATIENT_PRICE

> Stores the price when Load Item Master 6 Ops job inserts or updates the patient price based off Variance defined in mmPricingTool.exe. Used for control of the ops job.

**Description:** Inveontory Charge Serices Patient Price  
**Table type:** ACTIVITY  
**Primary key:** _(not published — see note)_  
**Columns:** 17

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `COST_AMT` | DOUBLE | NOT NULL |  | Cost amount from the last run of the ops job. Original value from ITEM_LOCATION_COST.cost |
| 2 | `COST_TYPE_CD` | DOUBLE | NOT NULL |  | The cost type code allows differentiation between average cost, current cost, last cost, etc. |
| 3 | `ITEM_ID` | DOUBLE | NOT NULL | FK→ | The item that this cost and price applies to. |
| 4 | `MM_CS_PATIENT_PRICE_ID` | DOUBLE | NOT NULL |  | Unique, generated number that identifies a single row on the MM_CS_PATIENT_PRICE table. |
| 5 | `MM_PRICE_FORMULA_ID` | DOUBLE | NOT NULL | FK→ | Identifies the price formula that was used for this item. |
| 6 | `MM_PRICE_FORMULA_RANGE_ID` | DOUBLE | NOT NULL | FK→ | Identifies the price formula range that was used for this item. |
| 7 | `OPS_JOB_RUN_DT_TM` | DATETIME | NOT NULL |  | The date and time the ops job last ran and updated this row. |
| 8 | `ORGANIZATION_ID` | DOUBLE | NOT NULL | FK→ | The organization that this item price was calculated for. |
| 9 | `PRICE_AMT` | DOUBLE | NOT NULL |  | The patient price derived based on supply cost with markup. The official data value is stored in PRICE_SCHED_ITEMS.price |
| 10 | `PRICE_SCHED_ID` | DOUBLE | NOT NULL | FK→ | The price schedule that this item is a part of. |
| 11 | `RANGE_END_DT_TM` | DATETIME | NOT NULL |  | The end date of the pricing formula range. |
| 12 | `RANGE_START_DT_TM` | DATETIME | NOT NULL |  | The start date of the pricing formula range. |
| 13 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 14 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 15 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 16 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 17 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `ITEM_ID` | [ITEM_DEFINITION](ITEM_DEFINITION.md) | `ITEM_ID` |
| `MM_PRICE_FORMULA_ID` | [MM_PRICE_FORMULA](MM_PRICE_FORMULA.md) | `MM_PRICE_FORMULA_ID` |
| `MM_PRICE_FORMULA_RANGE_ID` | [MM_PRICE_FORMULA_RANGE](MM_PRICE_FORMULA_RANGE.md) | `MM_PRICE_FORMULA_RANGE_ID` |
| `ORGANIZATION_ID` | [ORGANIZATION](ORGANIZATION.md) | `ORGANIZATION_ID` |
| `PRICE_SCHED_ID` | [PRICE_SCHED](PRICE_SCHED.md) | `PRICE_SCHED_ID` |

