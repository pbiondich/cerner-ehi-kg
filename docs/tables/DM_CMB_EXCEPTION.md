# DM_CMB_EXCEPTION

> THIS TABLE IS USED DURING THE COMBINE AND UNCOMBINE PROCESSES TO IDENTIFY TABLES THAT WILL NOT BE COMBINED/UNCOMBINED USING THE GENERIC LOGIC. INSTEAD, THESE TABLES WILL BE COMBINED/UNCOMBINED USING CUSTOM SCRIPTS NAMED IN THIS TABLE.

**Description:** COMBINE EXCEPTION  
**Table type:** REFERENCE  
**Primary key:** _(not published — see note)_  
**Columns:** 12

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `CHILD_ENTITY` | VARCHAR(32) | NOT NULL |  | Name of the child table that needs to be combined using custom logic. |
| 2 | `DEL_CHG_ID_IND` | DOUBLE | NOT NULL |  | A 1 indicates that the custom script will change the person or encounter id on the child table to the 'to' value during a 'delete.' A 0 indicates that the custom script will not change the value of person or encounter id on the child table during a 'delete.' |
| 3 | `OPERATION_TYPE` | VARCHAR(20) | NOT NULL |  | Valid values are 'COMBINE' and 'UNCOMBINE.' This allows a child table to have a custom script for combines and a custom script for uncombines. |
| 4 | `PARENT_ENTITY` | VARCHAR(32) | NOT NULL |  | Parent table for the combine, e.g. person or encounter. |
| 5 | `SCRIPT_NAME` | VARCHAR(50) |  |  | Name of the custom script to be executed for the child table. A value of 'NONE' indicates that nothing should be done to the table during the operation (combine or uncombine). Scripts are named according to a naming convention: person_cmb_ , encntr_cmb_ , person_ucb_ , or encntr_ucb_ . |
| 6 | `SCRIPT_RUN_ORDER` | DOUBLE | NOT NULL |  | Some custom scripts need to be run before others in order for the logic to work correctly. The value here indicates the precedence for the script to be run. All the 1's are run first, then all the 2's, etc. |
| 7 | `SINGLE_ENCNTR_IND` | DOUBLE |  |  | Indicates whether the script should be called during a single-encounter person combine. A '1' means yes, and a '0' means no. If the child table has foreign key relationships to both person and encounter and custom logic is needed for person combines, the custom script should handle single-encounter person combines, and the value here should be '1'. Otherwise, the value should be '0.' |
| 8 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 9 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 10 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 11 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 12 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

