# MODIFY_OPTION

> A reference of all types of modifications that a site could perform on products.

**Description:** Modify Option  
**Table type:** REFERENCE  
**Primary key:** `OPTION_ID`  
**Columns:** 24  
**Referenced by:** 2 columns

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ACTIVE_IND` | DOUBLE |  |  | The table row is active or inactive. A row is generally active unless it is in an inactive state such as logically deleted, combined away, pending purge, etc. |
| 2 | `ACTIVE_STATUS_CD` | DOUBLE | NOT NULL |  | Indicates the status of the row itself (not the data in the row) such as active, inactive, combined away, pending purge, etc. |
| 3 | `ACTIVE_STATUS_DT_TM` | DATETIME |  |  | The date and time that the active_status_cd was set. |
| 4 | `ACTIVE_STATUS_PRSNL_ID` | DOUBLE | NOT NULL |  | The person who caused the active_status_cd to be set or change. |
| 5 | `ALLOW_EXTEND_EXP_IND` | DOUBLE | NOT NULL |  | Indicates if the new product's expiration date can be extended beyond the original product's expiration date in Modify Products. |
| 6 | `BAG_TYPE_CD` | DOUBLE | NOT NULL |  | The type of bag in which the product must have been drawn, in order to perform this type of modification on it. |
| 7 | `BAG_TYPE_VALID_IND` | DOUBLE |  |  | Indicates whether the system should validate that the bag type of the product entered matches the bag type defined for this modification option. |
| 8 | `CALC_EXP_DRAWN_IND` | DOUBLE |  |  | Indicates whether the system should calculate the new expiration date and time from the date and time the product was drawn, instead of from the date and time of the modification. |
| 9 | `CALC_ORIG_EXP_DRAWN_IND` | DOUBLE | NOT NULL |  | Indicates if the drawn date should be used to calculated the original product's expiration date |
| 10 | `CHG_ORIG_EXP_DT_IND` | DOUBLE |  |  | Indicates whether the original product's expiration date and time should be changed or not. |
| 11 | `CROSSOVER_REASON_CD` | DOUBLE | NOT NULL |  | This column only applies to modification options of the crossover type. It defines the default reason products are being "crossed over" from autologous or directed to allogeneic types of products. This reason is displayed in the modification application at the time this option is chosen. |
| 12 | `DESCRIPTION` | VARCHAR(40) |  |  | %modifcati |
| 13 | `DISPOSE_ORIG_IND` | DOUBLE |  |  | Indicates whether the original product should be disposed when performing this type of modification. |
| 14 | `DIVISION_TYPE_FLAG` | DOUBLE |  |  | The type of division of the original product. |
| 15 | `OPTION_ID` | DOUBLE | NOT NULL | PK | The primary key of this table. An internal system-assigned number that ensures the uniqueness of each row. |
| 16 | `ORIG_NBR_DAYS_EXP` | DOUBLE |  |  | Determines how the system should calculate the new expiration date and time of the original product. The system will add the number of days defined here to the modification date and time, to calculate the new expiration date and time of the original product. (The system uses the value in the ORIG_NBR_HRS_EXP column as well) |
| 17 | `ORIG_NBR_HRS_EXP` | DOUBLE |  |  | Determines how the system should calculate the new expiration date and time of the original product. The system will add the number of hours defined here to the modification date and time, to calculate the new expiration date and time of the original product. (The system uses the value in the ORIG_NBR_DAYS_EXP column as well) |
| 18 | `ORIG_PRODUCT_CD` | DOUBLE | NOT NULL | FK→ | The product type that must be entered as the original product, in order to perform this type of modification. |
| 19 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 20 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 21 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 22 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 23 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |
| 24 | `VALIDATE_VOL_IND` | DOUBLE |  |  | Indicates whether the system should validate the volume entered for the new product(s). If this indicator is set, the system will subtract the volume of the new product(s) from the original product, and display the new remaining volume of the original product. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `ORIG_PRODUCT_CD` | [PRODUCT_INDEX](PRODUCT_INDEX.md) | `PRODUCT_CD` |

## Referenced by (2)

| From table | Column |
|------------|--------|
| [MODIFY_OPTION_TESTING](MODIFY_OPTION_TESTING.md) | `OPTION_ID` |
| [NEW_PRODUCT](NEW_PRODUCT.md) | `OPTION_ID` |

