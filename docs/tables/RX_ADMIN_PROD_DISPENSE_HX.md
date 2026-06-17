# RX_ADMIN_PROD_DISPENSE_HX

> Stores the historical pharmacy information related to the products of administrations assoiated with a dispense event.

**Description:** Pharmacy Administration Product Dispense History  
**Table type:** ACTIVITY  
**Primary key:** `RX_ADMIN_PROD_DISPENSE_HX_ID`  
**Columns:** 20  
**Referenced by:** 2 columns

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `CDM_OPTION_IND` | DOUBLE | NOT NULL |  | Indicates if the product is charged at the manufacturer level (0) or the drug formulary level (1). |
| 2 | `CHARGE_QTY` | DOUBLE | NOT NULL |  | The product quantity to be charged. |
| 3 | `CREDIT_QTY` | DOUBLE | NOT NULL |  | The product quantity to be credited. |
| 4 | `INGRED_SEQUENCE` | DOUBLE | NOT NULL |  | The order the ingredients are displayed. |
| 5 | `ITEM_ID` | DOUBLE | NOT NULL | FK→ | The medication definition pharmacy product. |
| 6 | `MANF_ITEM_ID` | DOUBLE | NOT NULL | FK→ | Information about the manufacturer of the dispensed product. |
| 7 | `PRICE_AMT` | DOUBLE | NOT NULL |  | The price of the dispensed product. |
| 8 | `PRICE_SCHED_ID` | DOUBLE | NOT NULL | FK→ | The price schedule of the dispensed product. |
| 9 | `RESIDUAL_PRICE_AMT` | DOUBLE | NOT NULL |  | The price to be charged after a reverse has occurred. |
| 10 | `RESIDUAL_QTY` | DOUBLE | NOT NULL |  | The quantity to be charged after a reverse has occurred. |
| 11 | `RESIDUAL_TAX_AMT` | DOUBLE | NOT NULL |  | The tax amount to be charged after a reverse has occurred. |
| 12 | `RX_ADMIN_DISPENSE_HX_ID` | DOUBLE | NOT NULL | FK→ | Identifies the admin dispense event to which this product is associated. |
| 13 | `RX_ADMIN_PROD_DISPENSE_HX_ID` | DOUBLE | NOT NULL | PK | Unique, generated number that identifies a single row on the RX_ADMIN_PROD_DISPENSE_HX table. |
| 14 | `TAX_AMT` | DOUBLE | NOT NULL |  | The amount of tax to be charged. |
| 15 | `TNF_ID` | DOUBLE | NOT NULL |  | The template non-formulary key that is associated with this admin prod dispense. A type of product that does not relate to a real medication. |
| 16 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 17 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 18 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 19 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 20 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `ITEM_ID` | [ITEM_DEFINITION](ITEM_DEFINITION.md) | `ITEM_ID` |
| `MANF_ITEM_ID` | [MANUFACTURER_ITEM](MANUFACTURER_ITEM.md) | `ITEM_ID` |
| `PRICE_SCHED_ID` | [PRICE_SCHED](PRICE_SCHED.md) | `PRICE_SCHED_ID` |
| `RX_ADMIN_DISPENSE_HX_ID` | [RX_ADMIN_DISPENSE_HX](RX_ADMIN_DISPENSE_HX.md) | `RX_ADMIN_DISPENSE_HX_ID` |

## Referenced by (2)

| From table | Column |
|------------|--------|
| [PHA_BATCH_REPORT_ACT_DTL](PHA_BATCH_REPORT_ACT_DTL.md) | `RX_ADMIN_PROD_DISPENSE_HX_ID` |
| [RX_INPT_CLAIM_HX](RX_INPT_CLAIM_HX.md) | `RX_ADMIN_PROD_DISPENSE_HX_ID` |

