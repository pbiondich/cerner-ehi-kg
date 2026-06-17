# BB_MOD_NEW_PRODUCT

> Stores a list of new products to create as the result of a modification option.

**Description:** Blood Bank New Product  
**Table type:** REFERENCE  
**Primary key:** `MOD_NEW_PROD_ID`  
**Columns:** 33  
**Referenced by:** 1 columns

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ALLOW_EXTEND_EXP_IND` | DOUBLE |  |  | Indicates if the new product's expiration date and time can be extended beyond the original product's expiration date and time. |
| 2 | `ALLOW_NO_ABORH_IND` | DOUBLE |  |  | Indicates if the new product's ABO/Rh can be left blank when pooling products. |
| 3 | `BAG_TYPE_CD` | DOUBLE | NOT NULL |  | The code value that identifies the bag type that must have been drawn in order to perform the modification. |
| 4 | `CALC_EXP_DRAWN_IND` | DOUBLE |  |  | Indicates if the new product's expiration date should be calculated from the original product's drawn date and time instead of from the modification date and time. |
| 5 | `CALC_EXP_ORIG_RECV_IND` | DOUBLE |  |  | Indicates if the new product's expiration date should be calculated from the original product's received date and time instead of from the modification date and time. |
| 6 | `CALC_VOL_IND` | DOUBLE |  |  | Indicates if the new product's volume should automatically be calculated from the original component products when pooling products. |
| 7 | `CODABAR_BARCODE` | VARCHAR(20) |  |  | Default Codabar product type barcode for the new product created in the modification. |
| 8 | `CROSSOVER_REASON_CD` | DOUBLE | NOT NULL |  | The code value that identifies the default crossover reason. |
| 9 | `DEFAULT_EXP_DAYS` | DOUBLE |  |  | Defines the number of days that will be added to the modification/drawn date and time in order to calculate the new product's expiration date. |
| 10 | `DEFAULT_EXP_HRS` | DOUBLE |  |  | Defines the number of hours that will be added to the modification/drawn date and time in order to calculate the new product's expiration date and time. |
| 11 | `DEFAULT_ORIG_EXP_IND` | DOUBLE |  |  | Indicates if the new product's expiration date and time should default to the original product's expiration date and time. |
| 12 | `DEFAULT_ORIG_VOL_IND` | DOUBLE |  |  | Indicates if the new product's volume should default to the original product's volume. |
| 13 | `DEFAULT_SUB_ID_FLAG` | DOUBLE |  |  | Defines the default sub product ID that should be assigned to each new product in order to make each product unique for the same product number. 0 - No Default 1 - Uppercase alpha 2 - Lowercase alpha 3 - Numeric |
| 14 | `DEFAULT_SUPPLIER_ID` | DOUBLE | NOT NULL | FK→ | Identifies the default supplier id that should be associated with the new product. The supplier is defined on the organization table. |
| 15 | `DEFAULT_UNIT_OF_MEAS_CD` | DOUBLE | NOT NULL |  | The code value that identifies the default unit of measure associated with the new product volume. |
| 16 | `DEFAULT_VOLUME` | DOUBLE |  |  | Defines the default volume for the new product. |
| 17 | `ISBT_BARCODE` | VARCHAR(20) |  |  | Default ISBT product type barcode for the new product created in the modification. |
| 18 | `MAX_PREP_HRS` | DOUBLE |  |  | The maximum component preparation hours defines the number of hours to be added to the drawn date and time of the original product that cannot be exceeded in order to create the new product. |
| 19 | `MOD_NEW_PROD_ID` | DOUBLE | NOT NULL | PK | The internal system assigned number that uniquely identifies a new blood bank product. |
| 20 | `NEW_PRODUCT_CD` | DOUBLE | NOT NULL |  | The code value that uniquely identifies a new product. |
| 21 | `OPTION_ID` | DOUBLE | NOT NULL | FK→ | The internal system assigned number that uniquely identifies a modification option. |
| 22 | `ORIG_PLASMA_PROD_CD` | DOUBLE | NOT NULL |  | For reconstituted product option, this is the plasma and the RBC is the Orig_product_cd field |
| 23 | `ORIG_PRODUCT_CD` | DOUBLE | NOT NULL |  | The code value that uniquely identifies an original component product. |
| 24 | `PROMPT_VOL_IND` | DOUBLE |  |  | Indicates if the system should prompt for the new product's volume. |
| 25 | `QUANTITY` | DOUBLE |  |  | The quantity of new products of a given type to create when performing a product split. |
| 26 | `REQUIRE_ASSIGN_IND` | DOUBLE |  |  | Indicates if the system should require the new product to be assigned to a patient. |
| 27 | `SYNONYM_ID` | DOUBLE | NOT NULL | FK→ | Identifies the confirmatory test that should be automatically ordered by the system when the modification is performed. |
| 28 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 29 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 30 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 31 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 32 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 33 | `VALIDATE_VOL_IND` | DOUBLE |  |  | Indicates if the volume of the new products volume should be validated to confirm it doesn't exceed the original products volume. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `DEFAULT_SUPPLIER_ID` | [ORGANIZATION](ORGANIZATION.md) | `ORGANIZATION_ID` |
| `OPTION_ID` | [BB_MOD_OPTION](BB_MOD_OPTION.md) | `OPTION_ID` |
| `SYNONYM_ID` | [ORDER_CATALOG_SYNONYM](ORDER_CATALOG_SYNONYM.md) | `SYNONYM_ID` |

## Referenced by (1)

| From table | Column |
|------------|--------|
| [BB_MOD_SPECIAL_TESTING](BB_MOD_SPECIAL_TESTING.md) | `MOD_NEW_PROD_ID` |

