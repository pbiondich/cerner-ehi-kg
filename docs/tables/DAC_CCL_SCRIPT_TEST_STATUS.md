# DAC_CCL_SCRIPT_TEST_STATUS

> Storage of the status of a specific test within a specific run

**Description:** DAC_CCL_SCRIPT_TEST_STATUS  
**Table type:** ACTIVITY  
**Primary key:** _(not published — see note)_  
**Columns:** 12

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `CCL_SCRIPT_TEST_ID` | DOUBLE | NOT NULL | FK→ | A reference to the test for which this is a run |
| 2 | `CCL_SCRIPT_TEST_RUN_ID` | DOUBLE | NOT NULL | FK→ | A reference to the record of which run this test is associated with |
| 3 | `CCL_SCRIPT_TEST_STATUS_ID` | DOUBLE | NOT NULL |  | Primary key of the table |
| 4 | `END_DT_TM` | DATETIME | NOT NULL |  | The date and time at which the test ended |
| 5 | `START_DT_TM` | DATETIME | NOT NULL |  | The date and time at which the test started |
| 6 | `TEST_MESSAGE` | VARCHAR(500) |  |  | The message (if any) recorded at the conclusion or mid-execution of a test |
| 7 | `TEST_STATUS` | VARCHAR(10) | NOT NULL |  | The status of the specific test |
| 8 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 9 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 10 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 11 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 12 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `CCL_SCRIPT_TEST_ID` | [DAC_CCL_SCRIPT_TEST](DAC_CCL_SCRIPT_TEST.md) | `CCL_SCRIPT_TEST_ID` |
| `CCL_SCRIPT_TEST_RUN_ID` | [DAC_CCL_SCRIPT_TEST_RUN](DAC_CCL_SCRIPT_TEST_RUN.md) | `CCL_SCRIPT_TEST_RUN_ID` |

