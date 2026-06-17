# REPORT_QUEUE_R

> This activity table contains the relationship between user-built queues (defined on codeset 1319) and the cases assigned to the queues.

**Description:** Report Queue Reltn  
**Table type:** ACTIVITY  
**Primary key:** _(not published — see note)_  
**Columns:** 8

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `REPORT_ID` | DOUBLE | NOT NULL | FK→ | This field contains the foreign key value representing the individual report that is associated with a report queue. This value can be used to join to report information stored on the CASE_REPORT table, if desired. |
| 2 | `REPORT_QUEUE_CD` | DOUBLE | NOT NULL | FK→ | This field contains the foreign key value representing the report queue. Report queues are stored on codeset 1319. |
| 3 | `SEQUENCE` | DOUBLE |  |  | This field contains a sequence value used to determine display and processing hierarchy if multiple reports are associated with a single report queue. The report assigned the lowest sequence displays first; the report assigned the highest displays last. |
| 4 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 5 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 6 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 7 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 8 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `REPORT_ID` | [CASE_REPORT](CASE_REPORT.md) | `REPORT_ID` |
| `REPORT_QUEUE_CD` | [CODE_VALUE](CODE_VALUE.md) | `CODE_VALUE` |

