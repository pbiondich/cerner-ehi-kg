# DM_SQL_TEST_SEQUENCES

> This is where all test sequences are stored

**Description:** DM SQL TEST SEQUENCES  
**Table type:** ACTIVITY  
**Primary key:** _(not published — see note)_  
**Columns:** 4

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `DESCRIPTION` | VARCHAR(80) |  |  | description for the test_sequence |
| 2 | `TEST_SEQUENCE` | DOUBLE | NOT NULL |  | this is the test sequence |
| 3 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 4 | `USER_NAME` | VARCHAR(30) |  |  | this is the creator of the test sequence |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

