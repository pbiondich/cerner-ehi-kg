# PRODUCT_CATEGORY

> A user-defined reference of all categories (groupings) of like products, e.g., the red cell category.

**Description:** Product Category  
**Table type:** REFERENCE  
**Primary key:** `PRODUCT_CAT_CD`  
**Columns:** 28  
**Referenced by:** 2 columns

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ACTIVE_IND` | DOUBLE |  |  | The table row is active or inactive. A row is generally active unless it is in an inactive state such as logically deleted, combined away, pending purge, etc. |
| 2 | `ACTIVE_STATUS_CD` | DOUBLE | NOT NULL |  | Indicates the status of the row itself (not the data in the row) such as active, inactive, combined away, pending purge, etc. |
| 3 | `ACTIVE_STATUS_DT_TM` | DATETIME |  |  | The date and time that the active_status_cd was set. |
| 4 | `ACTIVE_STATUS_PRSNL_ID` | DOUBLE | NOT NULL |  | The person who caused the active_status_cd to be set or change. |
| 5 | `COMPONENT_TAG_IND` | DOUBLE |  |  | Indicates whether a component tag should be printed for all product types within this category, at the time the product is assigned or dispensed to a patient. |
| 6 | `CONFIRM_REQUIRED_IND` | DOUBLE |  |  | Indicates whether an ABORh confirmatory test is required of all product types within this category. This indicator determines whether the Receive Products application will automatically order the confirmatory test defined for products logged into inventory. This indicator also determines whether the Result Entry and Dispense applications will validate that the ABORh has been confirmed on the product. |
| 7 | `CROSSMATCH_TAG_IND` | DOUBLE |  |  | Indicates whether a crossmatch tag should be printed for all product types within this category, at the time the product is crossmatched or dispensed to a patient. |
| 8 | `DEFAULT_SHIP_COND_CD` | DOUBLE | NOT NULL |  | Defines the shipping condition that should be displayed as a default for all product types within this category, at the time the products are logged into inventory with the Receive Products application. |
| 9 | `DEFAULT_UNIT_MEASURE_CD` | DOUBLE | NOT NULL |  | Defines the unit of measure that should be displayed as a default for all product types within this category, at the time the products are logged into inventory with the Receive Products application. |
| 10 | `DEFAULT_VIS_INSP_CD` | DOUBLE | NOT NULL |  | Defines the visual inspection that should be displayed as a default for all product types within this category, at the time the products are logged into inventory with the Receive Products application. |
| 11 | `DONOR_LABEL_ABORH_CNT` | DOUBLE | NOT NULL |  | Defines the number of ABO/Rh tests that are required for a product type to be label verified. |
| 12 | `PILOT_LABEL_IND` | DOUBLE |  |  | Indicates whether pilot labels should be generated whenever a product within this category is received into inventory via the Receive Products application. A value of 1 indicates pilot labels should be printed. A value of 0 indicates pilot labels should NOT be printed. Pilot labels are small labels that are affixed to the tubes. |
| 13 | `PRODUCT_CAT_CD` | DOUBLE | NOT NULL | PK | The code value for the actual product category defined. Combined wth the PRODUCT_CLASS, it makes each row unique. Product categories provide a way to group individual types of similar products into categories. Examples of product categories are: "Red Cell Products", "Plasma", "Platelets", etc. |
| 14 | `PRODUCT_CLASS_CD` | DOUBLE | NOT NULL | FK→ | The code value of the product class, as defined on code set 1606. Product classes are currently pre-defined by Cerner. Two product classes are currently provided: "Blood Products", and "Derivatives". |
| 15 | `PROMPT_ALTERNATE_IND` | DOUBLE |  |  | Indicates whether the Receive Products application should prompt for an alternate number for all types of products within this category. Alternate numbers are used when site choose to renumber their products, and still wish to retain a record of the original number from the supplier. |
| 16 | `PROMPT_SEGMENT_IND` | DOUBLE |  |  | Indicates whether the Receive Products application should allow the user to enter the segment number when product types within this category are logged into inventory. |
| 17 | `PROMPT_VOL_IND` | DOUBLE |  |  | Indicates whether the Receive Products application should allow the user to enter the volume when product types within this category are logged into inventory. |
| 18 | `RED_CELL_PRODUCT_IND` | DOUBLE |  |  | Indicates whether all product types built within this category are red cell products. This indicator is used throughout the system to determine when certain validation should occur, and also in reports. |
| 19 | `RH_REQUIRED_IND` | DOUBLE |  |  | Indicates whether an Rh type is required on all product types built within this category. |
| 20 | `SPECIAL_TESTING_IND` | DOUBLE |  |  | Indicates whether the Receive Products application should allow the user to enter special testing when product types within this category are logged into inventory. |
| 21 | `STORAGE_TEMP_CD` | DOUBLE | NOT NULL |  | Defines the storage temperature that should be associated with all product types within this category, at the time the products are logged into inventory with the Receive Products application. (Currently, this value is automatically attached to the product and the Receive Products application does not prompt the user for a different storage temperature.) |
| 22 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 23 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 24 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 25 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 26 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |
| 27 | `VALID_ABORH_COMPAT_IND` | DOUBLE |  |  | Indicates whether ABORh compatibility should be validated for all product types within this category, at the time a product is assigned, crossmatched, or dispensed to a patient. |
| 28 | `XMATCH_REQUIRED_IND` | DOUBLE |  |  | Indicates whether a crossmatch is required on any types of products within this product category, before dispensing it to a patient. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `PRODUCT_CLASS_CD` | [PRODUCT_CLASS](PRODUCT_CLASS.md) | `PRODUCT_CLASS_CD` |

## Referenced by (2)

| From table | Column |
|------------|--------|
| [PRODUCT_BARCODE](PRODUCT_BARCODE.md) | `PRODUCT_CAT_CD` |
| [PRODUCT_INDEX](PRODUCT_INDEX.md) | `PRODUCT_CAT_CD` |

