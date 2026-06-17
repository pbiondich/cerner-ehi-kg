# DAC_CCL_SCRIPT_TEST_RUN

> Storage of a run of a specific test set

**Description:** DAC_CCL_SCRIPT_TEST_RUN  
**Table type:** ACTIVITY  
**Primary key:** `CCL_SCRIPT_TEST_RUN_ID`  
**Columns:** 12  
**Referenced by:** 1 columns

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `CCL_SCRIPT_TEST_RUN_ID` | DOUBLE | NOT NULL | PK | The primary key of the table |
| 2 | `END_DT_TM` | DATETIME | NOT NULL |  | The date and time at which the test run ended |
| 3 | `START_DT_TM` | DATETIME | NOT NULL |  | The date and time at which the test run started |
| 4 | `TESTER_USERNAME` | VARCHAR(31) | NOT NULL |  | The username of the user who ran the test |
| 5 | `TEST_RUN_MESSAGE` | VARCHAR(500) |  |  | The message, if any, that was reported by the test run |
| 6 | `TEST_RUN_SCRIPT` | VARCHAR(31) |  |  | The name of the script, as specified by the user, that was tested. This will be NULL if nothing was specified. |
| 7 | `TEST_RUN_STATUS` | VARCHAR(10) | NOT NULL |  | The status of the entire test set. |
| 8 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 9 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 10 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 11 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 12 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Referenced by (1)

| From table | Column |
|------------|--------|
| [DAC_CCL_SCRIPT_TEST_STATUS](DAC_CCL_SCRIPT_TEST_STATUS.md) | `CCL_SCRIPT_TEST_RUN_ID` |

