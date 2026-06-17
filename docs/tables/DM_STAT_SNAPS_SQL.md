# DM_STAT_SNAPS_SQL

> Stores the unique SQL entries flagged for a poor score or shareable memory through the MSA TOP SQL process, including their hash value and full SQL Text.

**Description:** Data Management Statistics Snapshot SQL  
**Table type:** ACTIVITY  
**Primary key:** _(not published — see note)_  
**Columns:** 9

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `CREATE_DT_TM` | DATETIME | NOT NULL |  | Contains the date and time the row was created. |
| 2 | `DM_STAT_SNAPS_SQL_ID` | DOUBLE | NOT NULL |  | Uniquely identifies an SQL statement that has been flagged for a poor score or shareable memory through the MSA TOP SQL process, including their hash value and full SQL text. |
| 3 | `SQL_IDENT` | DOUBLE | NOT NULL |  | This value is generated based on the SQL text. |
| 4 | `SQL_TEXT` | LONGTEXT |  |  | The full SQL Text of this SQL entry. |
| 5 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 6 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 7 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 8 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 9 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

