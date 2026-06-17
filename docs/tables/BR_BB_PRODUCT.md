# BR_BB_PRODUCT

> Blood bank transfusion product reference data.

**Description:** BEDROCK BLOOD BANK PRODUCT  
**Table type:** REFERENCE  
**Primary key:** _(not published — see note)_  
**Columns:** 34

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ABORH_CONF_TEST_NAME` | VARCHAR(100) |  |  | Name (Synonym) of the ABORH confirmation test. |
| 2 | `ACTIVE_IND` | DOUBLE | NOT NULL |  | The table row is active or inactive. A row is generally active unless it is in an inactive state such as logically deleted, combined away, pending purge, etc. |
| 3 | `ACTIVE_STATUS_CD` | DOUBLE | NOT NULL |  | Indicates the status of the row itself (not the data in the row) such as active, inactive, combined away, pending purge, etc. |
| 4 | `ACTIVE_STATUS_DT_TM` | DATETIME | NOT NULL |  | The date and time that the active_status_cd was set. |
| 5 | `ACTIVE_STATUS_PRSNL_ID` | DOUBLE | NOT NULL |  | The person who caused the active_status_cd to be set or change. |
| 6 | `ALIQUOT_IND` | DOUBLE | NOT NULL |  | Indicates if value has an aliquot |
| 7 | `AUTOBUILD_IND` | DOUBLE | NOT NULL |  | Indicates if value is part of autobuild |
| 8 | `AUTO_IND` | DOUBLE |  |  | Indicates whether the product is an autologous product. |
| 9 | `BAR_CODE_VAL` | VARCHAR(100) |  |  | Bar code value for product identification. |
| 10 | `BR_CLIENT_ID` | DOUBLE | NOT NULL |  | Identifies which bedrock client the data belongs to |
| 11 | `CALC_EXP_FROM_DRAW_IND` | DOUBLE |  |  | Indicates whether the product expiration date should be calculated from the drawn date. |
| 12 | `DEF_STORAGE_TEMP` | VARCHAR(100) |  |  | Default storage temperature for this product. |
| 13 | `DEF_SUPPLIER` | VARCHAR(100) |  |  | Default supplier for the product. |
| 14 | `DESCRIPTION` | VARCHAR(100) |  |  | Long description for the product. |
| 15 | `DIRECTED_IND` | DOUBLE |  |  | Indicates whether the product is a directed donation product. |
| 16 | `DISPENSE_IND` | DOUBLE |  |  | Indicates whether the product can be dispensed. |
| 17 | `DISPLAY` | VARCHAR(100) |  |  | Display value for the product. |
| 18 | `INT_UNITS_IND` | DOUBLE |  |  | Indicates whether international units are applicable for this product. |
| 19 | `MAX_EXP_UNIT` | VARCHAR(100) |  |  | Hours or Days - the units of time before the product expires. |
| 20 | `MAX_EXP_VAL` | DOUBLE |  |  | The value of the unit of time before the product expires. |
| 21 | `MIN_BEF_QUAR` | DOUBLE |  |  | Number of minutes before the product is quarantined. |
| 22 | `PRODCAT_ID` | DOUBLE | NOT NULL |  | Identifier for the product category to which this product is related. |
| 23 | `PRODUCT_CD` | DOUBLE | NOT NULL |  | Code value for the product. |
| 24 | `PRODUCT_ID` | DOUBLE | NOT NULL |  | Unique identifier for the table. |
| 25 | `SELECTED_IND` | DOUBLE |  |  | Indicates whether the product has been selected. |
| 26 | `START_VERSION_NBR` | DOUBLE | NOT NULL |  | Identifies which version of start has been loaded. |
| 27 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 28 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 29 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 30 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 31 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |
| 32 | `VALIDATE_ANTIBODY_IND` | DOUBLE |  |  | Indicates whether antibody validation is required for the product. |
| 33 | `VALIDATE_TRANSF_REQ_IND` | DOUBLE |  |  | Indicates whether transfusion requirements must be validated. |
| 34 | `VOLUME_DEF` | DOUBLE |  |  | Default volume for the product. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

