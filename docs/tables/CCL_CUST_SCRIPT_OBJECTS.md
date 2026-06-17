# CCL_CUST_SCRIPT_OBJECTS

> Stores Discern Explorer custom script names to provide automatic service routing of custom scripts

**Description:** CCL Custom Script Objects  
**Table type:** REFERENCE  
**Primary key:** _(not published — see note)_  
**Columns:** 9

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ACTIVE_IND` | DOUBLE | NOT NULL |  | The table row is active or inactive. A row is generally active unless it is in an inactive state such as logically deleted, combined away, pending purge, etc. |
| 2 | `CCL_CUST_SCRIPT_OBJECTS_ID` | DOUBLE | NOT NULL |  | Unique generated number that identifies a single row on the CCL_CUST_SCRIPT_OBJECTS table. |
| 3 | `GROUP_NUMBER` | DOUBLE | NOT NULL |  | The CCL group number of the custom script object (typically 0 or 1). |
| 4 | `OBJECT_NAME` | VARCHAR(30) | NOT NULL |  | The name of the custom script object. |
| 5 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 6 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 7 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 8 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 9 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

