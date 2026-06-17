# MARS_SUITE_ACTIVITY

> Identifies an execution of a suite. Suites contain multiple reports and can take a long time to run. As such it is necessary that a user not be forced to wait for a reply. The idea is that the user will be able given a reference to their run. They can use this reference to check on the status and fetch the reply (assuming the reports have completed successfully). The ID on this table is that reference.

**Description:** MARS Suite Activity  
**Table type:** ACTIVITY  
**Primary key:** `MARS_SUITE_ACTIVITY_ID`  
**Columns:** 7  
**Referenced by:** 1 columns

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `MARS_SUITE_ACTIVITY_ID` | DOUBLE | NOT NULL | PK | PRIMARY KEY |
| 2 | `MARS_SUITE_ID` | DOUBLE | NOT NULL | FK→ | Unique Suite ID referencing the metadata regarding this suite |
| 3 | `UPDT_APPLCTX` | DOUBLE |  |  | The application context number from the record info block. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 4 | `UPDT_CNT` | DOUBLE |  |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 5 | `UPDT_DT_TM` | DATETIME |  |  | The date and time the row was last inserted or updated. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 6 | `UPDT_ID` | DOUBLE |  |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 7 | `UPDT_TASK` | DOUBLE |  |  | The registered (assigned) task number for the process that inserted or updated the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `MARS_SUITE_ID` | [MARS_SUITE](MARS_SUITE.md) | `MARS_SUITE_ID` |

## Referenced by (1)

| From table | Column |
|------------|--------|
| [MARS_SUITE_RESPONSE](MARS_SUITE_RESPONSE.md) | `MARS_SUITE_ACTIVITY_ID` |

