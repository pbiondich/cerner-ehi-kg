# PRODUCT_INDEX

> Contains a reference of all types of products defined at a site, e.g., red blood cells, platelets, etc. Determines how the system will validate that product in certain transactions.

**Description:** Product Index  
**Table type:** REFERENCE  
**Primary key:** `PRODUCT_CD`  
**Columns:** 29  
**Referenced by:** 11 columns

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ACTIVE_IND` | DOUBLE |  |  | The table row is active or inactive. A row is generally active unless it is in an inactive state such as logically deleted, combined away, pending purge, etc. |
| 2 | `ACTIVE_STATUS_CD` | DOUBLE | NOT NULL |  | Indicates the status of the row itself (not the data in the row) such as active, inactive, combined away, pending purge, etc. |
| 3 | `ACTIVE_STATUS_DT_TM` | DATETIME |  |  | The date and time that the active_status_cd was set. |
| 4 | `ACTIVE_STATUS_PRSNL_ID` | DOUBLE | NOT NULL |  | The person who caused the active_status_cd to be set or change. |
| 5 | `ALIQUOT_IND` | DOUBLE | NOT NULL |  | Indicates whether this type of product is aliquot, i.e., a product that is broken into fractional units (pediatric, syringe, etc.) |
| 6 | `ALLOW_DISPENSE_IND` | DOUBLE |  |  | Indicates whether or not this type of product should be dispensed to patients. |
| 7 | `AUTOLOGOUS_IND` | DOUBLE |  |  | Indicates whether this type of product is autologous, i.e., a product that was donated by a person to be transfused to himself/herself later. So, for autologous products the designated recipient is the same person who donated the product. |
| 8 | `AUTO_BILL_ITEM_CD` | DOUBLE | NOT NULL |  | Not currently used. |
| 9 | `AUTO_QUARANTINE_MIN` | DOUBLE |  |  | The number of elapsed minutes for this type of product to be used in the Return Products application as criteria for quarantining a returned product, i.e., if the returned product has been out of the blood bank for more than the number of minutes defined here, the Return Products application will quarantine the product. |
| 10 | `DEFAULT_SUPPLIER_ID` | DOUBLE | NOT NULL | FK→ | The supplier that should be defaulted for this product when it is received from an outside supplier. This column actually represents an ORGANIZATION_ID, which is the primary key of the ORGANIZATION table. It is an internal system-assigned number. |
| 11 | `DEFAULT_VOLUME` | DOUBLE |  |  | The volume that should be defaulted for this product. Used in the ReceiveProducts application as a default volume for the user to either enter or change. |
| 12 | `DIRECTED_IND` | DOUBLE |  |  | Indicates whether this type of product is directed, i.e., a product that was donated by a person to be transfused to a designated recipient (ex. relative or friend) later. |
| 13 | `DIR_BILL_ITEM_CD` | DOUBLE | NOT NULL |  | Not currently used at this time. |
| 14 | `DRAWN_DT_TM_IND` | DOUBLE |  |  | Indicates whether or not the drawn_dt_tm should be used to calculate a product's expriation date/time in ReceiveProducts. |
| 15 | `INTL_UNITS_IND` | DOUBLE |  |  | This column applies only to derivative products. It indicates whether or not this product should be tracked by international units. (If not tracked by international units, it will be tracked by quantity) |
| 16 | `MAX_DAYS_EXPIRE` | DOUBLE |  |  | Defines the maximum number of days to expiration for this product type. This column is used in the ReceiveProducts application to assist in detecting clerical errors in the expiration date/time entered on products received. The ReceiveProducts application adds this number of days and the MAX_HRS_EXPIRE to the current date/time, and if the expiration date/time entered for a product of this type exceeds that date, the user is warned. |
| 17 | `MAX_HRS_EXPIRE` | DOUBLE |  |  | Defines the maximum number of hours to expiration for this product type. This column is used in the ReceiveProducts application to assist in detecting clerical errors in the expiration date/time entered on products received. The ReceiveProducts application adds the MAX_DAYS_EXPIRE and this number of hours to the current date and time, and if the expiration date and time entered for a product of this type exceeds that date/time, the user is warned. |
| 18 | `PRODUCT_CAT_CD` | DOUBLE | NOT NULL | FK→ | The product category to which this type of product belongs. An example of a category is "Red Blood Cells", to which a product type of "RBC CPDA1" might belong. |
| 19 | `PRODUCT_CD` | DOUBLE | NOT NULL | PK | The type of product defined. In the case of blood products, the product type is labeled on the actual bag of blood. |
| 20 | `PRODUCT_CLASS_CD` | DOUBLE | NOT NULL | FK→ | Defines the class of products to which this type of product belongs. Currently, the classes are defined by Cerner only. Two classes have been pre-defined: blood products and derivatives. |
| 21 | `STORAGE_TEMP_CD` | DOUBLE | NOT NULL |  | Indicates the temperature at which a product should be stored |
| 22 | `SYNONYM_ID` | DOUBLE | NOT NULL | FK→ | This column represents the confirmatory test, if applicable, that should be automatically ordered on the product at the time it is received into inventory. This confirmatory test is built in the order catalog and given a synonym, which this column represents. It is the primary key of the SYNONYM table, and is an internal system-assigned number. |
| 23 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 24 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 25 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 26 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 27 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |
| 28 | `VALIDATE_AG_AB_IND` | DOUBLE |  |  | Indicates whether the red cell antigens should be validated against the person's antibodies at the time of dispense. |
| 29 | `VALIDATE_TRANS_REQ_IND` | DOUBLE |  |  | Indicates whether the attributes of the product should be validated against the person's transfusion requirements at the time of dispense. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `DEFAULT_SUPPLIER_ID` | [ORGANIZATION](ORGANIZATION.md) | `ORGANIZATION_ID` |
| `PRODUCT_CAT_CD` | [PRODUCT_CATEGORY](PRODUCT_CATEGORY.md) | `PRODUCT_CAT_CD` |
| `PRODUCT_CLASS_CD` | [PRODUCT_CLASS](PRODUCT_CLASS.md) | `PRODUCT_CLASS_CD` |
| `SYNONYM_ID` | [ORDER_CATALOG_SYNONYM](ORDER_CATALOG_SYNONYM.md) | `SYNONYM_ID` |

## Referenced by (11)

| From table | Column |
|------------|--------|
| [BB_DSPNS_BLOCK](BB_DSPNS_BLOCK.md) | `PRODUCT_CD` |
| [BB_DSPNS_BLOCK_PRODUCT](BB_DSPNS_BLOCK_PRODUCT.md) | `PRODUCT_CD` |
| [COMPONENT](COMPONENT.md) | `PRODUCT_CD` |
| [MODIFY_OPTION](MODIFY_OPTION.md) | `ORIG_PRODUCT_CD` |
| [MODIFY_OPTION_TESTING](MODIFY_OPTION_TESTING.md) | `NEW_PRODUCT_CD` |
| [POOL_OPTION](POOL_OPTION.md) | `NEW_PRODUCT_CD` |
| [PRODUCT_ABORH](PRODUCT_ABORH.md) | `PRODUCT_CD` |
| [PRODUCT_BARCODE](PRODUCT_BARCODE.md) | `PRODUCT_CD` |
| [PRODUCT_PATIENT_ABORH](PRODUCT_PATIENT_ABORH.md) | `PRODUCT_CD` |
| [PROD_ORD_PROD_IDX_R](PROD_ORD_PROD_IDX_R.md) | `PRODUCT_CD` |
| [TRANSFUSION_COMMITTEE](TRANSFUSION_COMMITTEE.md) | `PRODUCT_CD` |

