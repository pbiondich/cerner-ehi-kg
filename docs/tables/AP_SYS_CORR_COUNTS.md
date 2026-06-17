# AP_SYS_CORR_COUNTS

> This activity table contains the total counts of cases that have met a system correlation criteria and those cases that qualified for a system initiated correlation event.

**Description:** Anatomic Pathology System Correlation Counts  
**Table type:** ACTIVITY  
**Primary key:** _(not published — see note)_  
**Columns:** 8

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `QUALIFIED_CASES` | DOUBLE | NOT NULL |  | This field contains the number of cases in which a correlation event has been initiated for a give system correlation trigger (AP_SYS_CORR). |
| 2 | `SYS_CORR_ID` | DOUBLE | NOT NULL | FK→ | This field contains the internal identification code to the AP_SYS_CORR table. |
| 3 | `TOTAL_CASES` | DOUBLE | NOT NULL |  | This field contains the number of cases for which a system correlation trigger (AP_SYS_CORR) were attempted to qualify on. |
| 4 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 5 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 6 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 7 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 8 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `SYS_CORR_ID` | [AP_SYS_CORR](AP_SYS_CORR.md) | `SYS_CORR_ID` |

