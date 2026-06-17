# SPECIAL_TESTING

> Contains all special testing done on a product, whether from the base label on the bag, or from resulting procedures on the product. This includes antigen typings as well as any other special testing, e.g., CMV negative, etc.

**Description:** Special Testing  
**Table type:** ACTIVITY  
**Primary key:** `SPECIAL_TESTING_ID`  
**Columns:** 16  
**Referenced by:** 2 columns

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ACTIVE_IND` | DOUBLE |  |  | The table row is active or inactive. A row is generally active unless it is in an inactive state such as logically deleted, combined away, pending purge, etc. |
| 2 | `ACTIVE_STATUS_CD` | DOUBLE | NOT NULL |  | Indicates the status of the row itself (not the data in the row) such as active, inactive, combined away, pending purge, etc. |
| 3 | `ACTIVE_STATUS_DT_TM` | DATETIME |  |  | The date and time that the active_status_cd was set. |
| 4 | `ACTIVE_STATUS_PRSNL_ID` | DOUBLE | NOT NULL |  | The person who caused the active_status_cd to be set or change. |
| 5 | `BARCODE_VALUE_TXT` | VARCHAR(20) | NOT NULL |  | Contains the ISBT barcode associated with the special testing attribute. |
| 6 | `CONFIRMED_IND` | DOUBLE |  |  | Indicates whether or not this antigen or attribute of the product has is considered confirmed or not. ***NOT USED AT THIS TIME |
| 7 | `MODIFIABLE_FLAG` | DOUBLE | NOT NULL |  | Indicates if the user can remove the special testing from the product. 0 = Special Testing was added manually and can be modified by the user. 1 = Special Testing was added via barcode scan, and can NOT be modified by the user. |
| 8 | `PRODUCT_ID` | DOUBLE | NOT NULL | FK→ | The primary key to the PRODUCT table. An internal system-assigned number. On this table, it identifies the product for which special testing (antigens or attributes) has been recorded. |
| 9 | `PRODUCT_RH_PHENOTYPE_ID` | DOUBLE | NOT NULL | FK→ | Links the antigen on this row to the Rh phenotype to which it belongs. Links this row to a row on the Product_rh_phenotype table. An example is C+ on this row originating from the Rh phenotype of "CDE/cde". |
| 10 | `SPECIAL_TESTING_CD` | DOUBLE | NOT NULL |  | Defines the special testing item (antigen or attribute) that was recorded on the product, whether it was done at the time the product was received into the blood bank's inventory, or at the time the results were verified for the testing. |
| 11 | `SPECIAL_TESTING_ID` | DOUBLE | NOT NULL | PK | The primary key of this table. An internal system-assigned number to ensure the uniqueness of each row. |
| 12 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 13 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 14 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 15 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 16 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `PRODUCT_ID` | [PRODUCT](PRODUCT.md) | `PRODUCT_ID` |
| `PRODUCT_RH_PHENOTYPE_ID` | [PRODUCT_RH_PHENOTYPE](PRODUCT_RH_PHENOTYPE.md) | `PRODUCT_RH_PHENOTYPE_ID` |

## Referenced by (2)

| From table | Column |
|------------|--------|
| [CORRECTED_SPECIAL_TESTS](CORRECTED_SPECIAL_TESTS.md) | `ORIG_SPECIAL_TESTING_ID` |
| [SPECIAL_TESTING_RESULT](SPECIAL_TESTING_RESULT.md) | `SPECIAL_TESTING_ID` |

