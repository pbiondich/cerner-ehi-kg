# SN_RPT_EVENT

> This table holds all of the events that were selected to be active for a report.

**Description:** SN RPT EVENT  
**Table type:** REFERENCE  
**Primary key:** _(not published — see note)_  
**Columns:** 12

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `CREATE_APPLCTX` | DOUBLE |  |  | The application context number from the record info block. |
| 2 | `CREATE_DT_TM` | DATETIME |  |  | The date and time the row was initially inserted. |
| 3 | `CREATE_PRSNL_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 4 | `CREATE_TASK` | DOUBLE |  |  | The registered (assigned) task number for the process that created the row. |
| 5 | `RPT_EVENT_ID` | DOUBLE | NOT NULL |  | Primary Key |
| 6 | `RPT_EVENT_REF_ID` | DOUBLE | NOT NULL |  | This is a foreign key into the SN_RPT_EVENT_REF table to indicate which reference event this came from. |
| 7 | `RPT_ID` | DOUBLE | NOT NULL |  | This is a foreign key into the SN_RPT table to indicate which report this event belongs to. |
| 8 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 9 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 10 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 11 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 12 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

