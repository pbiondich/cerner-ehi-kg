# BB_MOD_OPTION

> Stores a list of all modification options that can be performed on blood bank products

**Description:** Blood Bank Modification Option  
**Table type:** REFERENCE  
**Primary key:** `OPTION_ID`  
**Columns:** 35  
**Referenced by:** 4 columns

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ACTIVE_IND` | DOUBLE | NOT NULL |  | The table row is active or inactive. A row is generally active unless it is in an inactive state such as logically deleted, combined away, pending purge, etc. |
| 2 | `ACTIVE_STATUS_CD` | DOUBLE | NOT NULL |  | Indicates the status of the row itself (not the data in the row) such as active, inactive, combined away, pending purge, etc. |
| 3 | `ACTIVE_STATUS_DT_TM` | DATETIME | NOT NULL |  | The date and time that the active_status_cd was set. |
| 4 | `ACTIVE_STATUS_PRSNL_ID` | DOUBLE | NOT NULL |  | The person who caused the active_status_cd to be set or change. |
| 5 | `AD_HOC_IND` | DOUBLE |  |  | Indicates if the original products will be split into multiple products and the user will determine the quantity of products to create at the time of modification. |
| 6 | `BEG_EFFECTIVE_DT_TM` | DATETIME | NOT NULL |  | The date and time for which this table row becomes effective. Normally, this will be the date and time the row is added, but could be a past or future date and time. |
| 7 | `CHANGE_ATTRIBUTE_IND` | DOUBLE |  |  | Indicates if additional attribute(s) will be added to the original product. |
| 8 | `CHG_ORIG_EXP_DT_IND` | DOUBLE |  |  | Indicates if the original product's expiration date and time can be changed. |
| 9 | `CROSSOVER_IND` | DOUBLE |  |  | Indicates if the original product will be crossed over from autologous/directed to an allogeneic product. |
| 10 | `DISPLAY` | VARCHAR(40) | NOT NULL |  | The modification option description for display. |
| 11 | `DISPLAY_KEY` | VARCHAR(40) | NOT NULL |  | The modification option description in all uppercase used for performing indexed searches on the table. |
| 12 | `DISPLAY_KEY_A_NLS` | VARCHAR(160) |  |  | DISPLAY_KEY_A_NLS column |
| 13 | `DISPLAY_KEY_NLS` | VARCHAR(82) |  |  | The NLS versions of the modification option description in all uppercase used for performing indexed searches on the table. |
| 14 | `DISPOSE_ORIG_IND` | DOUBLE |  |  | indicates if the original product will be disposed of as a result of the modification. |
| 15 | `END_EFFECTIVE_DT_TM` | DATETIME | NOT NULL |  | The date/time after which the row is no longer valid as active current data. This may be valued with the date that the row became inactive. |
| 16 | `GENERATE_ISBT_NBR_IND` | DOUBLE | NOT NULL |  | Indicates the ISBT number should be generated for the ISBT pools. |
| 17 | `GENERATE_PROD_NBR_IND` | DOUBLE |  |  | Indicates if the system should automatically generate product number when pooling products. |
| 18 | `LABEL_INFO_PROMPT_IND` | DOUBLE | NOT NULL |  | Indicates if the system should prompt for label information when modifying products. |
| 19 | `NEW_PRODUCT_IND` | DOUBLE |  |  | Indicates if a new product will be created as the result of the modification. |
| 20 | `OPTION_ID` | DOUBLE | NOT NULL | PK | The internal system assigned number that uniquely identifies a modification option. |
| 21 | `ORIG_NBR_DAYS_EXP` | DOUBLE |  |  | Number of days to be added to the modification date to calculate the original product's new expiration date and time. |
| 22 | `ORIG_NBR_HRS_EXP` | DOUBLE |  |  | Number of hours to be added to the modification time to calculate the original product's new expiration date and time. |
| 23 | `POOL_PRODUCT_IND` | DOUBLE |  |  | Indicates if the original component products will be pooled to create a new product. |
| 24 | `PROD_NBR_CCYY_IND` | DOUBLE |  |  | Pooled product number year format for system generated product numbers. Indicates whether or not the year should format to 4 digits. A value of 1 indicates the year should format to 4 digits. A value of 0 indicates the year should format to 2 digits. |
| 25 | `PROD_NBR_PREFIX` | VARCHAR(10) |  |  | Pooled product number prefix for system generated product numbers. |
| 26 | `PROD_NBR_SEQ` | DOUBLE |  |  | Pooled product number sequence for system generated product numbers. |
| 27 | `PROD_NBR_STARTING_NBR` | DOUBLE |  |  | Pooled product number starting sequence number for system generated product numbers. |
| 28 | `PROD_NBR_YEAR` | DOUBLE |  |  | Pooled product number year for system generated product numbers. |
| 29 | `RECON_RBC_IND` | DOUBLE | NOT NULL |  | Indicates modification option is an RBC Reconstitution option. |
| 30 | `SPLIT_IND` | DOUBLE |  |  | Indicates if the original products will be split into multiple products. |
| 31 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 32 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 33 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 34 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 35 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Referenced by (4)

| From table | Column |
|------------|--------|
| [BB_MOD_DEVICE](BB_MOD_DEVICE.md) | `OPTION_ID` |
| [BB_MOD_NEW_PRODUCT](BB_MOD_NEW_PRODUCT.md) | `OPTION_ID` |
| [BB_MOD_ORIG_PRODUCT](BB_MOD_ORIG_PRODUCT.md) | `OPTION_ID` |
| [BB_MOD_POOL_NBR](BB_MOD_POOL_NBR.md) | `OPTION_ID` |

