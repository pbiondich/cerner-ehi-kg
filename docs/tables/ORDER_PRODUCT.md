# ORDER_PRODUCT

> For each ingredient of a medication order store the pharmacy product(s) to dispense which satisfy this ingredient

**Description:** order_product  
**Table type:** ACTIVITY  
**Primary key:** `ACTION_SEQUENCE`, `INGRED_SEQUENCE`, `ITEM_ID`, `ORDER_ID`, `TNF_ID`  
**Columns:** 39  
**Referenced by:** 5 columns

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ACTION_SEQUENCE` | DOUBLE | NOT NULL | PK | Identifier to reference the action taken |
| 2 | `AUTO_ASSIGN_FLAG` | DOUBLE | NOT NULL |  | Auto assign flag |
| 3 | `BRAND_DESC` | VARCHAR(100) |  |  | brand desc for product |
| 4 | `CMPD_BASE_IND` | DOUBLE |  |  | Indicates compound base setting for product |
| 5 | `COMPOUND_FLAG` | DOUBLE |  |  | Compound flag |
| 6 | `DISP_QTY` | DOUBLE |  |  | Current Dispensable qty unit for REFILL event |
| 7 | `DISP_QTY_UNIT_CD` | DOUBLE | NOT NULL |  | Current Dispensable qty unit for REFILL event |
| 8 | `DOSE_QUANTITY` | DOUBLE |  |  | Value to describe this product dose |
| 9 | `DOSE_QUANTITY_TXT` | VARCHAR(150) |  |  | The concatenated string of the individual dose quantities for a variable dosed order. |
| 10 | `DOSE_QUANTITY_UNIT_CD` | DOUBLE | NOT NULL |  | Unit to apply to the dose quantity |
| 11 | `DRUG_IDENTIFIER` | VARCHAR(100) |  |  | Drug Id (NDC, etc.) for product |
| 12 | `GENERIC_DESC` | VARCHAR(100) |  |  | Generic desc for product |
| 13 | `IGNORE_IND` | DOUBLE |  |  | For PREMIXES, indicates whether or not to ignore current row |
| 14 | `INGRED_SEQUENCE` | DOUBLE | NOT NULL | PK | Identifier for the ingredient |
| 15 | `ITEM_ID` | DOUBLE | NOT NULL | PK FK→ | Reference to the medication definition pharmacy product |
| 16 | `IV_SEQ` | DOUBLE |  |  | For alternating IV"s, the place a bag holds in the series. |
| 17 | `LABEL_DESC` | VARCHAR(100) |  |  | Label desc for product |
| 18 | `MED_PRODUCT_ID` | DOUBLE | NOT NULL |  | Stores unique field for NDC |
| 19 | `ON_ADMIN_IND` | DOUBLE | NOT NULL |  | This field identifies whether or not this record was added because of Charge On Admin charge processing. |
| 20 | `ORDER_ID` | DOUBLE | NOT NULL | PK | Identifier for the order |
| 21 | `PACKAGE_TYPE_ID` | DOUBLE | NOT NULL |  | Package type id |
| 22 | `PARENT_PRODUCT_SEQ` | DOUBLE |  |  | For child products of a compound, this points to the parent order_product |
| 23 | `PBS_DRUG_UUID` | VARCHAR(255) |  |  | The drug identifier for the product. |
| 24 | `PRODUCT_SEQ` | DOUBLE |  |  | Unique sequence for each order_product row |
| 25 | `RXA_ORDERING_UNIT_CD` | DOUBLE | NOT NULL |  | The unit of the ordering quantity for the dispense. |
| 26 | `STRENGTH_WITH_OVERFILL_UNIT_CD` | DOUBLE | NOT NULL |  | The strength dose unit on the product's ingredient including the overfill added during TPN balancing. |
| 27 | `STRENGTH_WITH_OVERFILL_VALUE` | DOUBLE | NOT NULL |  | The strength dose on the product's ingredient including the overfill added during TPN balancing. |
| 28 | `TNF_ID` | DOUBLE | NOT NULL | PK | Key to template_non-formulary table |
| 29 | `TOTAL_CHARGE_QUANTITY` | DOUBLE |  |  | Cumulative counter for number of units charged. Amounts based on product unit (i.e. mg) |
| 30 | `TOTAL_CREDIT_QUANTITY` | DOUBLE |  |  | Cumulative counter for number of units to credit. Amounts based on product unit (i.e. mg) |
| 31 | `TOTAL_DISPENSE_QUANTITY` | DOUBLE |  |  | Cumulative counter for number of units dispensed. Amounts based on product unit (i.e. mg) |
| 32 | `UNROUNDED_DOSE_QTY` | DOUBLE | NOT NULL |  | Product's quantity per dose prior to rounding. |
| 33 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 34 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 35 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 36 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 37 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |
| 38 | `VOLUME_WITH_OVERFILL_UNIT_CD` | DOUBLE | NOT NULL |  | The volume dose unit on the product's ingredient including the overfill added during TPN balancing. |
| 39 | `VOLUME_WITH_OVERFILL_VALUE` | DOUBLE | NOT NULL |  | The volume dose on the product's ingredient including the overfill added during TPN balancing. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `ITEM_ID` | [ITEM_DEFINITION](ITEM_DEFINITION.md) | `ITEM_ID` |

## Referenced by (5)

| From table | Column |
|------------|--------|
| [ORDER_PRODUCT_DOSE](ORDER_PRODUCT_DOSE.md) | `ACTION_SEQUENCE` |
| [ORDER_PRODUCT_DOSE](ORDER_PRODUCT_DOSE.md) | `INGRED_SEQUENCE` |
| [ORDER_PRODUCT_DOSE](ORDER_PRODUCT_DOSE.md) | `ITEM_ID` |
| [ORDER_PRODUCT_DOSE](ORDER_PRODUCT_DOSE.md) | `ORDER_ID` |
| [ORDER_PRODUCT_DOSE](ORDER_PRODUCT_DOSE.md) | `TNF_ID` |

