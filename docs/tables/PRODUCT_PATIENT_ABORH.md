# PRODUCT_PATIENT_ABORH

> A reference table of the valid combinations of a type of product and its aborh with a certain aborhof the patient. Used at the time the product is assigned, crossmatched, or dispensed to the patient.

**Description:** Product Patient Aborh  
**Table type:** REFERENCE  
**Primary key:** _(not published — see note)_  
**Columns:** 14

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ACTIVE_IND` | DOUBLE |  |  | The table row is active or inactive. A row is generally active unless it is in an inactive state such as logically deleted, combined away, pending purge, etc. |
| 2 | `ACTIVE_STATUS_CD` | DOUBLE | NOT NULL |  | Indicates the status of the row itself (not the data in the row) such as active, inactive, combined away, pending purge, etc. |
| 3 | `ACTIVE_STATUS_DT_TM` | DATETIME |  |  | The date and time that the active_status_cd was set. |
| 4 | `ACTIVE_STATUS_PRSNL_ID` | DOUBLE | NOT NULL |  | The person who caused the active_status_cd to be set or change. |
| 5 | `PRODUCT_CD` | DOUBLE | NOT NULL | FK→ | The type of product being defined for patient ABORh compatibility (ex. "Red Blood Cells"). |
| 6 | `PROD_ABORH_CD` | DOUBLE | NOT NULL |  | The product's ABORh that is being defined with a certain product type for patient ABORh compatibility (ex. "O Neg"). |
| 7 | `PRSN_ABORH_CD` | DOUBLE | NOT NULL |  | The person's ABORh that is being defined with a certain product type for patient ABORh compatibility (ex. "O Neg"). By being listed, it means that it is valid to assign, crossmatch, or dispense this product type and ABORh to a person with this ABORh. |
| 8 | `SEQUENCE_NBR` | DOUBLE | NOT NULL |  | An internal number which, when combined with the product type, product's ABORh, and person's ABORH, makes each row unique. It begins at 1 and is incremented by 1. It is needed because the user may choose to inactivate a product and ABORh combination, and later add it again as active. |
| 9 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 10 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 11 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 12 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 13 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |
| 14 | `WARN_IND` | DOUBLE |  |  | Indicates whether or not the user should be warned when a product of this product type and this ABORh is associated (assigned, crossmatched, or dispensed) to a person with the ABORh defined. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `PRODUCT_CD` | [PRODUCT_INDEX](PRODUCT_INDEX.md) | `PRODUCT_CD` |

