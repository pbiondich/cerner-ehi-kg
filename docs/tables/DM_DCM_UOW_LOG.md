# DM_DCM_UOW_LOG

> A table to hold details of the units of work of a work plan for the change management process

**Description:** Data Change Management Unit of Work Log  
**Table type:** ACTIVITY  
**Primary key:** _(not published — see note)_  
**Columns:** 13

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `DELETE_CNT` | DOUBLE | NOT NULL |  | Indicates the number of times a unit of work performed a delete |
| 2 | `DM_DCM_UOW_LOG_ID` | DOUBLE | NOT NULL |  | PRIMARY KEY |
| 3 | `FIRST_DML_DT_TM` | DATETIME | NOT NULL |  | The Date/Time the first DML occurred for a given table and UOW_GUID |
| 4 | `INSERT_CNT` | DOUBLE | NOT NULL |  | Indicates the number of times a unit of work performed an insert |
| 5 | `LAST_DML_DT_TM` | DATETIME | NOT NULL |  | The Date/Time the last DML occurred for a given table and UOW_GUID |
| 6 | `TABLE_NAME` | VARCHAR(30) | NOT NULL |  | Holds table name that was altered by unit of work |
| 7 | `UOW_GUID` | VARCHAR(50) | NOT NULL |  | Holds a globally unique value |
| 8 | `UPDATE_CNT` | DOUBLE | NOT NULL |  | Indicates the number of times a unit of work performed an update |
| 9 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 10 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 11 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 12 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 13 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

