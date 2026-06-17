# DM_REFCHG_FILTER_TEST

> Stores the various tests that should be performed to see if a row for the given table should be recorded for RDDS. The tests could be simple comparison (like = 0 or in ('A','B','C') ) or it could be a statement - usually a Select.

**Description:** Data Management reference change filter tests  
**Table type:** REFERENCE  
**Primary key:** _(not published — see note)_  
**Columns:** 11

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ACTIVE_IND` | DOUBLE | NOT NULL |  | The table row is active or inactive. A row is generally active unless it is in an inactive state such as logically deleted, combined away, pending purge, etc. |
| 2 | `MOVER_STRING` | VARCHAR(1000) | NOT NULL |  | A filter string the mover uses when interacting with the table. |
| 3 | `STATEMENT_IND` | DOUBLE | NOT NULL |  | Indicates if this test is a statement like a Select. |
| 4 | `TABLE_NAME` | VARCHAR(30) | NOT NULL | FK→ | Name of the table which has a filter requirement on it. |
| 5 | `TEST_NBR` | DOUBLE | NOT NULL |  | Sequence number for PK |
| 6 | `TEST_STR` | VARCHAR(2000) | NOT NULL |  | Testing text to be used for filtering. Input variable will have :: around them. |
| 7 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 8 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 9 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 10 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 11 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `TABLE_NAME` | [DM_REFCHG_FILTER](DM_REFCHG_FILTER.md) | `TABLE_NAME` |

