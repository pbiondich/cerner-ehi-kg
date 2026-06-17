# DM_REFCHG_SOFT_CONSTRAINTS

> This table will store soft constraint information for use within the RDDS dual build detection logic.

**Description:** Database Management Reference Change Soft Constraints  
**Table type:** REFERENCE  
**Primary key:** `DM_REFCHG_SOFT_CONSTRAINTS_ID`  
**Columns:** 12  
**Referenced by:** 1 columns

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ACTIVE_IND` | DOUBLE | NOT NULL |  | The table row is active or inactive. A row is generally active unless it is in an inactive state such as logically deleted, combined away, pending purge, etc. |
| 2 | `BLOCK_WHERE_CLAUSE` | VARCHAR(2000) |  |  | This will be used to store a CCL version of the where clause already stored in the WHERE_CLAUSE column. |
| 3 | `CONSTRAINT_NAME` | VARCHAR(30) | NOT NULL |  | The name of the soft constraint |
| 4 | `DM_REFCHG_SOFT_CONSTRAINTS_ID` | DOUBLE | NOT NULL | PK | Primary Key for table |
| 5 | `RESET_STATUS` | VARCHAR(20) |  |  | Status to assign to rows that violate this constraint. |
| 6 | `TABLE_NAME` | VARCHAR(30) | NOT NULL |  | The table name to apply this constraint to |
| 7 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 8 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 9 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 10 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 11 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 12 | `WHERE_CLAUSE` | VARCHAR(2000) |  |  | Additional functional constraints to account for (i.e. ¿where cons.active_ind = 1 AND cons.column_name is NULL¿) |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Referenced by (1)

| From table | Column |
|------------|--------|
| [DM_REFCHG_SOFT_CONS_COLUMNS](DM_REFCHG_SOFT_CONS_COLUMNS.md) | `DM_REFCHG_SOFT_CONSTRAINTS_ID` |

