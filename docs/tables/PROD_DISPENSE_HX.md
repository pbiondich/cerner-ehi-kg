# PROD_DISPENSE_HX

> For the pharmacy orders dispensed, store the products associated with the dispensing event

**Description:** prod_dispense_hx  
**Table type:** ACTIVITY  
**Primary key:** _(not published — see note)_  
**Columns:** 41

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `AVAILABLE_WASTE_CHARGE_QTY` | DOUBLE |  |  | Amount of product remaining which is available to waste and will be charged for. |
| 2 | `AVAILABLE_WASTE_QTY` | DOUBLE |  |  | Amount of product remaining which is available to waste. |
| 3 | `CHARGE_IND` | DOUBLE |  |  | the charge indicator |
| 4 | `CHARGE_QTY` | DOUBLE |  |  | Amounts based on product unit (i.e. mg) to charge for. Rounded to 4 digits. |
| 5 | `COMPOUND_FLAG` | DOUBLE |  |  | Compound flag0 - normal; 1 -premix; 2 - compound |
| 6 | `COST` | DOUBLE |  |  | Cost associated with the dispense event |
| 7 | `CREDIT_QTY` | DOUBLE |  |  | Amounts based on product unit (i.e. mg) to credit |
| 8 | `DISPENSE_HX_ID` | DOUBLE | NOT NULL | FK→ | Identifier for the dispense history |
| 9 | `DISPENSE_QTY` | DOUBLE |  |  | the dispense quantity |
| 10 | `DOSE_QTY` | DOUBLE |  |  | Product's quantity per dose after rounding for the product dispense. |
| 11 | `INGRED_SEQUENCE` | DOUBLE | NOT NULL |  | Identifier for the ingredient |
| 12 | `ITEM_ID` | DOUBLE | NOT NULL | FK→ | Reference to the medication definition pharmacy product |
| 13 | `MANF_ITEM_ID` | DOUBLE | NOT NULL | FK→ | Manufacturer item_id dispensed |
| 14 | `MAX_WASTE_CHARGE_QTY` | DOUBLE |  |  | Maximum amount of product that could have been charged for. |
| 15 | `MAX_WASTE_QTY` | DOUBLE |  |  | Maximum amount of product that could have been entered as waste. |
| 16 | `MED_PRODUCT_ID` | DOUBLE | NOT NULL | FK→ | Stores unique field for NDC |
| 17 | `PACKAGE_TYPE_ID` | DOUBLE | NOT NULL | FK→ | the Package type id |
| 18 | `PARENT_PRODUCT_SEQ` | DOUBLE |  |  | For child products of a compound, this points to the parent order_product. |
| 19 | `PRICE` | DOUBLE |  |  | Calculated price associated with the dispense event |
| 20 | `PRICE_SCHED_ID` | DOUBLE | NOT NULL | FK→ | This is the price schedule Id used to determine charge/credit amounts |
| 21 | `PRODUCT_SEQ` | DOUBLE |  |  | Unique sequence for each order_product row. |
| 22 | `PROD_DISPENSE_HX_ID` | DOUBLE | NOT NULL |  | Unique, generated identifier for a product on a dispense event. |
| 23 | `RESIDUAL_COST_AMT` | DOUBLE |  |  | Cost for the Per Unit Residual Quantity |
| 24 | `RESIDUAL_PRICE` | DOUBLE | NOT NULL |  | The price needing to be charged after the reverse transaction was placed. |
| 25 | `RESIDUAL_QTY` | DOUBLE | NOT NULL |  | The quantity needing to be charged after the reverse transaction was placed. |
| 26 | `RESIDUAL_TAX_AMT` | DOUBLE | NOT NULL |  | The tax amount needing to be charged after the reverse transaction was placed. |
| 27 | `SCAN_FLAG` | DOUBLE | NOT NULL |  | Used to determine whether the product was scanned in during charge on administration. (0 = not scanned, 1 = scanned) |
| 28 | `TAX_AMT` | DOUBLE | NOT NULL |  | Identifies the tax amount. |
| 29 | `TNF_ID` | DOUBLE | NOT NULL |  | Key to template_non-formulary table |
| 30 | `UNROUNDED_CHARGE_QTY` | DOUBLE |  |  | Amounts based on product unit (i.e. mg) to charge for |
| 31 | `UNROUNDED_CREDIT_QTY` | DOUBLE |  |  | Amount based on product unit (i.e. mg) to credit. |
| 32 | `UNROUNDED_DOSE_QTY` | DOUBLE |  |  | Product's quantity per dose prior to rounding for the product dispense. |
| 33 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 34 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 35 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 36 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 37 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 38 | `WASTE_FLAG` | DOUBLE |  |  | Indicates this dispense event can have waste applied. |
| 39 | `WASTE_OFFSET_IND` | DOUBLE |  |  | Indicates this dispense will require offset financial credits/charges whenever waste charges and waste credits happen. |
| 40 | `WASTE_QTY` | DOUBLE |  |  | Amount wasted for this dipsense. |
| 41 | `ZERO_WASTE_FLAG` | DOUBLE |  |  | Used to determine if a product is waste bill eligible but has zero amount wasted as part of the dispense. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `DISPENSE_HX_ID` | [DISPENSE_HX](DISPENSE_HX.md) | `DISPENSE_HX_ID` |
| `ITEM_ID` | [ITEM_DEFINITION](ITEM_DEFINITION.md) | `ITEM_ID` |
| `MANF_ITEM_ID` | [ITEM_DEFINITION](ITEM_DEFINITION.md) | `ITEM_ID` |
| `MED_PRODUCT_ID` | [MED_PRODUCT](MED_PRODUCT.md) | `MED_PRODUCT_ID` |
| `PACKAGE_TYPE_ID` | [PACKAGE_TYPE](PACKAGE_TYPE.md) | `PACKAGE_TYPE_ID` |
| `PRICE_SCHED_ID` | [PRICE_SCHED](PRICE_SCHED.md) | `PRICE_SCHED_ID` |

