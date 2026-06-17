# VALID_STATE

> A reference table to define what states of a product are valid to be used in each Blood Bank transaction.

**Description:** Valid State  
**Table type:** REFERENCE  
**Primary key:** _(not published — see note)_  
**Columns:** 11

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ACTIVE_DT_TM` | DATETIME |  |  | The date and time when this row became active. |
| 2 | `ACTIVE_IND` | DOUBLE |  |  | The table row is active or inactive. A row is generally active unless it is in an inactive state such as logically deleted, combined away, pending purge, etc. |
| 3 | `CATEGORY_CD` | DOUBLE | NOT NULL |  | The product category for which valid states are being defined. |
| 4 | `INACTIVE_DT_TM` | DATETIME |  |  | The date and time that this row became inactive. This column only applies to rows that have been inactivated at some point in time. Inactive rows have the ACTIVE_IND set to 0. |
| 5 | `PROCESS_CD` | DOUBLE | NOT NULL |  | The Cerner-defined process within the Blood Bank for which valid states of products are defined (ex. "Dispense"). |
| 6 | `STATE_CD` | DOUBLE | NOT NULL |  | The code value of the state that is defined as a valid state for a product in this category when it is accessed in this process. An example is "crossmatched" being a valid state for products in the "red cell products" category when they are accessed in the "Dispense" application. |
| 7 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 8 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 9 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 10 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 11 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

