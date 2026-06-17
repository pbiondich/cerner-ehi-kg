# CE_FLAGGED_RESULT_ROLE

> Store flag discipline information that will be related to a specific clinical event and a specific flagged result.

**Description:** Clinical Event Flagged Result Role  
**Table type:** ACTIVITY  
**Primary key:** _(not published — see note)_  
**Columns:** 9

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `CE_FLAGGED_RESULT_ID` | DOUBLE | NOT NULL | FK→ | Identifies the associated flagged clinical event. |
| 2 | `CE_FLAGGED_RESULT_ROLE_ID` | DOUBLE | NOT NULL |  | A unique, generated number that is used to identify an individual ce_flagged_result_role row. |
| 3 | `EVENT_ID` | DOUBLE | NOT NULL |  | The event that has been flagged by this role. |
| 4 | `ROLE_TYPE_CD` | DOUBLE | NOT NULL |  | The role of the personnel that flagged this result. |
| 5 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 6 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 7 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 8 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 9 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `CE_FLAGGED_RESULT_ID` | [CE_FLAGGED_RESULT](CE_FLAGGED_RESULT.md) | `CE_FLAGGED_RESULT_ID` |

