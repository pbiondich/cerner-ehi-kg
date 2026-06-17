# MM_XF_ERROR_LOG

> Contains errors for all Interface Transactions.

**Description:** Item Location / Locator Interface Error Log  
**Table type:** ACTIVITY  
**Primary key:** _(not published — see note)_  
**Columns:** 13

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ERROR_CD` | DOUBLE | NOT NULL |  | Code which specifies the error type of the Interface Transaction Error. |
| 2 | `ERROR_ID` | DOUBLE | NOT NULL |  | Primary Key |
| 3 | `FIELD_NAME` | VARCHAR(40) |  |  | Field Name |
| 4 | `INTERFACE_TYPE_CD` | DOUBLE | NOT NULL |  | Interface Type CD |
| 5 | `MSG` | VARCHAR(400) |  |  | Error Message |
| 6 | `PARENT_ENTITY_ID` | DOUBLE | NOT NULL |  | PARENT ENTITY ID |
| 7 | `PARENT_ENTITY_NAME` | VARCHAR(40) |  |  | PARENT ENTITY NAME |
| 8 | `SCRIPT_NAME` | VARCHAR(40) |  |  | Script Name |
| 9 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 10 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 11 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 12 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 13 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

