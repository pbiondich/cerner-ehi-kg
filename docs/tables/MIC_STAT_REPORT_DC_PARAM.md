# MIC_STAT_REPORT_DC_PARAM

> This statistical reference table contains the reports and susceptibility organisms duplicate checking information defined by service resource and source criteria.

**Description:** Micro Statistical Duplicate Checking Parameter  
**Table type:** REFERENCE  
**Primary key:** _(not published — see note)_  
**Columns:** 10

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ACROSS_ENCOUNTER_IND` | DOUBLE |  |  | This field indicates if duplicate checking should be across encounters or not. 0 = duplicate checking should not be across encounters. 1 = duplicate checking should be across encounters. |
| 2 | `ACROSS_SOURCE_IND` | DOUBLE |  |  | This field indicates if duplicate checking should be across sources or not. 0 = duplicate checking should not be across sources. 1 = duplicate checking should be across sources. |
| 3 | `LOOKBACK_HOURS` | DOUBLE |  |  | This field indicates the number of hours to look back for duplicates based on the collected date and time of the procedure. |
| 4 | `SERVICE_RESOURCE_CD` | DOUBLE | NOT NULL |  | This field contains the code_value of the service resource used to define reports and organisms duplicate checking preference. |
| 5 | `SOURCE_CD` | DOUBLE | NOT NULL |  | This field contains the code_value of the source used to define reports and organisms duplicate checking preference. |
| 6 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 7 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 8 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 9 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 10 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

