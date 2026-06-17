# BB_ISBT_LABEL_PARAM

> This table will store the default label parameters used to print Blood Bank ISBT Labels.

**Description:** Blood Bank ISBT Label Parameter  
**Table type:** REFERENCE  
**Primary key:** _(not published — see note)_  
**Columns:** 15

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `BB_ISBT_LABEL_PARAM_ID` | DOUBLE | NOT NULL |  | Contains the unique identifier for the ISBT label parameter. |
| 2 | `LABEL_TYPE_CD` | DOUBLE | NOT NULL |  | Indicates the type of label used for the print option. |
| 3 | `LICENSED_MODIFIER_IND` | DOUBLE | NOT NULL |  | Indicates if the modifying facility is licensed for the associated product. |
| 4 | `LICENSED_SUPPLIER_IND` | DOUBLE | NOT NULL |  | Indicates if the supplying facility is licensed for the associated product. |
| 5 | `NEW_PRODUCT_CD` | DOUBLE | NOT NULL |  | Uniquely identifies the new product type associated with the label parameter. |
| 6 | `NEW_PRODUCT_IND` | DOUBLE | NOT NULL |  | Indicates if the associated product is created as a result of the modification or if it is the original product. |
| 7 | `OPTION_ID` | DOUBLE | NOT NULL |  | Uniquely identifies the modification option associated with the label parameter. |
| 8 | `ORIG_PRODUCT_CD` | DOUBLE | NOT NULL |  | Uniquely identifies the original product type associated with the label parameter. |
| 9 | `PRINT_IND` | DOUBLE | NOT NULL |  | Indicates whether or not a label should be printed for the modification option/product type combination. |
| 10 | `SUPPLIER_IND` | DOUBLE | NOT NULL |  | Indicates if the facility is the supplying facility. |
| 11 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 12 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 13 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 14 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 15 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

