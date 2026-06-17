# BR_BB_PRODCAT

> Blood bank transfusion product reference data.

**Description:** Bedrock Blood Bank Product Category  
**Table type:** REFERENCE  
**Primary key:** _(not published — see note)_  
**Columns:** 32

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ABORH_CONF_REQ_IND` | DOUBLE |  |  | Indicates whether aborh confirmation is required. |
| 2 | `ACTIVE_IND` | DOUBLE | NOT NULL |  | The table row is active or inactive. A row is generally active unless it is in an inactive state such as logically deleted, combined away, pending purge, etc. |
| 3 | `ACTIVE_STATUS_CD` | DOUBLE | NOT NULL |  | Indicates the status of the row itself (not the data in the row) such as active, inactive, combined away, pending purge, etc. |
| 4 | `ACTIVE_STATUS_DT_TM` | DATETIME | NOT NULL |  | The date and time that the active_status_cd was set. |
| 5 | `ACTIVE_STATUS_PRSNL_ID` | DOUBLE | NOT NULL |  | The person who caused the active_status_cd to be set or change. |
| 6 | `ALTERNATE_ID_IND` | DOUBLE |  |  | Indicates whether an alternate id number is required. |
| 7 | `AUTOBUILD_IND` | DOUBLE | NOT NULL |  | Indicates if value is part of autobuild |
| 8 | `BR_CLIENT_ID` | DOUBLE | NOT NULL |  | Identifies which bedrock client the data belongs to. |
| 9 | `COMP_TAG_REQ_IND` | DOUBLE |  |  | Indicates whether a component tag must be print |
| 10 | `DESCRIPTION` | VARCHAR(100) |  |  | Product category description. |
| 11 | `DISPLAY` | VARCHAR(100) |  |  | Display name of the product category. |
| 12 | `NEW_PRODCAT_IND` | DOUBLE | NOT NULL |  | Indicator used to define whether the product category was added during the current wizard conversation. |
| 13 | `PILOT_LABEL_REQ_IND` | DOUBLE |  |  | Indicates whether a pilot label must be printed. |
| 14 | `PRODCAT_CD` | DOUBLE | NOT NULL |  | Product category code value. |
| 15 | `PRODCAT_ID` | DOUBLE | NOT NULL |  | Unique identifier for the table. |
| 16 | `PRODUCT_CLASS_MEAN` | VARCHAR(100) |  |  | CDF meaning of the category's product class. |
| 17 | `PROMPT_FOR_VOL_IND` | DOUBLE |  |  | Indicates whether the system will prompt for the unit volume. |
| 18 | `RED_CELL_IND` | DOUBLE |  |  | Indicates whether this is a red cell product. |
| 19 | `RH_REQ_IND` | DOUBLE |  |  | Indicates whether this is an RH required product. |
| 20 | `SEG_NUM_IND` | DOUBLE |  |  | Indicates whether the system will prompt for a segment number. |
| 21 | `SELECTED_IND` | DOUBLE |  |  | Indicates whether the product category has been selected in the Wizard. |
| 22 | `SHIP_COND_DEF` | VARCHAR(100) |  |  | Default shipping condition for the products in the category. |
| 23 | `START_VERSION_NBR` | DOUBLE | NOT NULL |  | Indicates which version of start has been loaded. |
| 24 | `UOM_DEF` | VARCHAR(100) |  |  | Default unit of measure for the products in the category. |
| 25 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 26 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 27 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 28 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 29 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 30 | `VAL_COMPAT_IND` | DOUBLE |  |  | Indicates whether compatibility validation is required. |
| 31 | `XM_REQ_IND` | DOUBLE |  |  | Indicates whether a crossmatch is required. |
| 32 | `XM_TAG_REQ_IND` | DOUBLE |  |  | Indicates whether a crossmatch tag must be printed. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

