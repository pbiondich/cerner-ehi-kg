# MED_PRODUCT

> Stores the manufacturer item information for pharmacy products.

**Description:** Med Product  
**Table type:** REFERENCE  
**Primary key:** `MED_PRODUCT_ID`  
**Columns:** 19  
**Referenced by:** 16 columns

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ACTIVE_IND` | DOUBLE | NOT NULL |  | The table row is active or inactive. A row is generally active unless it is in an inactive state such as logically deleted, combined away, pending purge, etc. |
| 2 | `BILLING_FACTOR_NBR` | DOUBLE | NOT NULL |  | Used to calculate a charge services billing amount, by applying the billing factor to the normal charge quantity |
| 3 | `BILLING_FACTOR_UOM_CD` | DOUBLE | NOT NULL |  | Passed to charge services with the billing factor to identify the correct unit of measure for the charge services bill amount. |
| 4 | `BIO_EQUIV_IND` | DOUBLE |  |  | bio equiv ind |
| 5 | `BRAND_IND` | DOUBLE |  |  | brand ind |
| 6 | `COST_FACTOR_NBR` | DOUBLE | NOT NULL |  | Used to calculate a charge amount by applying the cost_factor on the actual cost of the manufacturer item. |
| 7 | `FORMULARY_STATUS_CD` | DOUBLE | NOT NULL |  | Code used to determine the status of the drug, i.e. Formulary, Non-Formulary, Investigational. |
| 8 | `INNER_PKG_TYPE_ID` | DOUBLE | NOT NULL | FK→ | Represents the number of individual units present in the innermost packaging of a drug. |
| 9 | `INV_FACTOR_NBR` | DOUBLE | NOT NULL |  | Indicates the relationship of package information between the Pharmacy and Inventory systems. |
| 10 | `MANF_ITEM_ID` | DOUBLE | NOT NULL | FK→ | manf item id |
| 11 | `MED_DEF_CKI` | VARCHAR(255) | NOT NULL |  | *** OBSOLETE *** |
| 12 | `MED_PRODUCT_ID` | DOUBLE | NOT NULL | PK | med product id |
| 13 | `OUTER_PKG_TYPE_ID` | DOUBLE | NOT NULL | FK→ | Represents the total number of inner packages present in the final packaged product. |
| 14 | `UNIT_DOSE_IND` | DOUBLE |  |  | unit_dose_ind |
| 15 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 16 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 17 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 18 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 19 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `INNER_PKG_TYPE_ID` | [PACKAGE_TYPE](PACKAGE_TYPE.md) | `PACKAGE_TYPE_ID` |
| `MANF_ITEM_ID` | [MANUFACTURER_ITEM](MANUFACTURER_ITEM.md) | `ITEM_ID` |
| `OUTER_PKG_TYPE_ID` | [PACKAGE_TYPE](PACKAGE_TYPE.md) | `PACKAGE_TYPE_ID` |

## Referenced by (16)

| From table | Column |
|------------|--------|
| [CE_MED_ADMIN_IDENT](CE_MED_ADMIN_IDENT.md) | `MED_PRODUCT_ID` |
| [FILL_PRINT_ORD_HX](FILL_PRINT_ORD_HX.md) | `MED_PRODUCT_ID` |
| [LOT_NUMBER_INFO](LOT_NUMBER_INFO.md) | `MED_PRODUCT_ID` |
| [MED_COST_HX](MED_COST_HX.md) | `MED_PRODUCT_ID` |
| [MED_IDENTIFIER](MED_IDENTIFIER.md) | `MED_PRODUCT_ID` |
| [MED_INGRED_SET](MED_INGRED_SET.md) | `CHILD_MED_PROD_ID` |
| [PROD_DISPENSE_HX](PROD_DISPENSE_HX.md) | `MED_PRODUCT_ID` |
| [RXS_ITEM_COUNTBACK](RXS_ITEM_COUNTBACK.md) | `MED_PRODUCT_ID` |
| [RX_MED_PROD_DESC](RX_MED_PROD_DESC.md) | `MED_PRODUCT_ID` |
| [SA_MEDICATION_ADMIN](SA_MEDICATION_ADMIN.md) | `MED_PRODUCT_ID` |
| [SA_REF_FLUID](SA_REF_FLUID.md) | `MED_PRODUCT_ID` |
| [SA_REF_MACRO_FLUID](SA_REF_MACRO_FLUID.md) | `MED_PRODUCT_ID` |
| [SA_REF_MACRO_MEDICATION](SA_REF_MACRO_MEDICATION.md) | `MED_PRODUCT_ID` |
| [SA_REF_MEDICATION](SA_REF_MEDICATION.md) | `MED_PRODUCT_ID` |
| [SA_TODO_FLUID](SA_TODO_FLUID.md) | `MED_PRODUCT_ID` |
| [SA_TODO_MEDICATION](SA_TODO_MEDICATION.md) | `MED_PRODUCT_ID` |

