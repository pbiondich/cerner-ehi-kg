# DAC_CCL_SCRIPT_TEST

> Storage of the test scripts associated with the automated testing harness framework.

**Description:** Database Access CCL Script Test  
**Table type:** REFERENCE  
**Primary key:** `CCL_SCRIPT_TEST_ID`  
**Columns:** 10  
**Referenced by:** 2 columns

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ACTIVE_IND` | DOUBLE | NOT NULL |  | The table row is active or inactive. A row is generally active unless it is in an inactive state such as logically deleted, combined away, pending purge, etc. |
| 2 | `CCL_SCRIPT_NAME` | VARCHAR(31) | NOT NULL |  | The script to be tested by the testing architecture |
| 3 | `CCL_SCRIPT_TEST_ID` | DOUBLE | NOT NULL | PK | The primary key of the table |
| 4 | `CCL_TEST_SCRIPT_NAME` | VARCHAR(31) | NOT NULL |  | The name of the test script that tests the script specified in CCL_SCRIPT_NAME |
| 5 | `PARENT_TEST_ID` | DOUBLE | NOT NULL | FK→ | The ID of the test that should precede this test, if any. |
| 6 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 7 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 8 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 9 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 10 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `PARENT_TEST_ID` | [DAC_CCL_SCRIPT_TEST](DAC_CCL_SCRIPT_TEST.md) | `CCL_SCRIPT_TEST_ID` |

## Referenced by (2)

| From table | Column |
|------------|--------|
| [DAC_CCL_SCRIPT_TEST](DAC_CCL_SCRIPT_TEST.md) | `PARENT_TEST_ID` |
| [DAC_CCL_SCRIPT_TEST_STATUS](DAC_CCL_SCRIPT_TEST_STATUS.md) | `CCL_SCRIPT_TEST_ID` |

