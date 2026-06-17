# DM_REFCHG_RTABLE_RESET

> Stores row level information about rows in the $R tables that need to be reset.

**Description:** Database Architecture Refchg $R Table Reset  
**Table type:** REFERENCE  
**Primary key:** _(not published — see note)_  
**Columns:** 12

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `BLOCK_STMT` | VARCHAR(4000) | NOT NULL |  | Holds a WHERE clause statement that will identify the rows in the LIVE table that were created with dual build. |
| 2 | `DM_REFCHG_RTABLE_RESET_ID` | DOUBLE | NOT NULL |  | Primary Key for table |
| 3 | `PK_WHERE` | VARCHAR(2000) | NOT NULL |  | Holds a string in the form of a WHERE clause that contains the columns that can locate the problematic rows on the $R tables. |
| 4 | `RESET_STATUS` | VARCHAR(20) | NOT NULL |  | Specifies the status that the current row is in |
| 5 | `TABLE_NAME` | VARCHAR(30) | NOT NULL |  | Holds the table name where a dual build occurred |
| 6 | `TRIG_TYPE_FLAG` | DOUBLE | NOT NULL |  | Indicates the type of triggers that identified the dual build problem. 1 - REG_MC trigger violations that block rows based on a unique constraint. This should be used even if it also qualifies as a type 2 (MUI column violation). 2 - REG_MC trigger violations that block rows based on MUI columns. If the MUI columns are supported by a unique constraints, implying that it could be both 1 and 2, it should be labeled as type 1 3 - REG_MD_MC trigger violations are type 3 4 - New REG_V |
| 7 | `TRIG_TYPE_INFO` | VARCHAR(30) |  |  | Holds additional information about the trigger that identified the problem (i.e. index name) |
| 8 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 9 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 10 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 11 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 12 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

