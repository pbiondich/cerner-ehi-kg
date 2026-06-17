# PRODUCT_ABORH

> A user-defined reference table that defines the combinations of product and aborhs to be used in patient/product compatibility checking throughout the PathNet Blood Bank Transfusion system.

**Description:** Product Aborh  
**Table type:** REFERENCE  
**Primary key:** _(not published — see note)_  
**Columns:** 17

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ABORH_OPTION_FLAG` | DOUBLE |  |  | When associating this product type and ABORh with a patient, this flag defines whether the patient's entire ABORh should be validated, or just the patient's Rh type. |
| 2 | `ACTIVE_IND` | DOUBLE |  |  | The table row is active or inactive. A row is generally active unless it is in an inactive state such as logically deleted, combined away, pending purge, etc. |
| 3 | `ACTIVE_STATUS_CD` | DOUBLE | NOT NULL |  | Indicates the status of the row itself (not the data in the row) such as active, inactive, combined away, pending purge, etc. |
| 4 | `ACTIVE_STATUS_DT_TM` | DATETIME |  |  | The date and time that the active_status_cd was set. |
| 5 | `ACTIVE_STATUS_PRSNL_ID` | DOUBLE | NOT NULL |  | The person who caused the active_status_cd to be set or change. |
| 6 | `BBD_NO_GT_DIR_PRSN_FLAG` | DOUBLE | NOT NULL |  | OBSOLETE ** NO LONGER BEING USED ** Defines whether or not to allow a product of this type and ABORh to be associated to a person with no ABORh, within the "ReceiveProducts" application, when entering the recipient information in the Autologous/Directed window. |
| 7 | `DISP_NO_CURRABORH_PRSN_FLAG` | DOUBLE | NOT NULL |  | Defines whether or not to allow a product of this type and ABORh to be dispensed to a person with no current ABO. |
| 8 | `NO_GT_AUTODIR_PRSN_FLAG` | DOUBLE |  |  | Defines whether or not to allow a product of this type and ABORh to be associated to a person with no ABORh, within the "ReceiveProducts" application, when entering the recipient information in the Autologous/Directed window. |
| 9 | `NO_GT_ON_PRSN_FLAG` | DOUBLE |  |  | Defines whether or not to allow a product of this type and ABORh to be assigned, crossmatched, or dispensed. to a person with no ABORh. |
| 10 | `PRODUCT_ABORH_CD` | DOUBLE | NOT NULL |  | The product's ABORh that is being defined with a certain product type for patient ABORh compatibility (ex. "O Neg"). |
| 11 | `PRODUCT_CD` | DOUBLE | NOT NULL | FK→ | The type of product defined for patient compatibility (ex. "Red Blood Cells"). |
| 12 | `SEQUENCE_NBR` | DOUBLE | NOT NULL |  | An internal number which, when combined with the product type and product's ABORh. is used to make each row unique. It begins at 1 and is incremented by 1. It is needed because the user may choose to inactivate a product and ABORh combination, and later add it again as active. |
| 13 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 14 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 15 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 16 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 17 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `PRODUCT_CD` | [PRODUCT_INDEX](PRODUCT_INDEX.md) | `PRODUCT_CD` |

