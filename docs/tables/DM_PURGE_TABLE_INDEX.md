# DM_PURGE_TABLE_INDEX

> Store indexes and the columns used in those indexes by tables that participate as parent tables in the purge process

**Description:** DM_PURGE_TABLE_INDEXES  
**Table type:** REFERENCE  
**Primary key:** _(not published — see note)_  
**Columns:** 13

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ADMIN_TABLE_IND` | DOUBLE | NOT NULL |  | An indicator of whether or not the given table is an admin table |
| 2 | `COLUMN_NAME` | VARCHAR(31) | NOT NULL |  | The name of a column used in an index |
| 3 | `DATA_TYPE` | VARCHAR(31) | NOT NULL |  | The data type of the column |
| 4 | `INDEX_NAME` | VARCHAR(31) | NOT NULL |  | The name of the index that is being used on the table |
| 5 | `LAST_DDL_DT_TM` | DATETIME | NOT NULL |  | The last date and time recorded that the table has been modified |
| 6 | `PRECEDENCE_NBR` | DOUBLE | NOT NULL |  | The order in which the column appears in the index |
| 7 | `TABLE_INDEX_ID` | DOUBLE | NOT NULL |  | A non-intelligent key for each row; populated from the DM_CLINICAL_SEQ sequence |
| 8 | `TABLE_NAME` | VARCHAR(31) | NOT NULL |  | The name of a table |
| 9 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 10 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 11 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 12 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 13 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

