# SN_RPT_EVENT_REF

> Contains all events that are available for a given report type.

**Description:** SN RPT EVENT REF  
**Table type:** REFERENCE  
**Primary key:** _(not published — see note)_  
**Columns:** 10

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `DESCRIPTION` | VARCHAR(255) | NOT NULL |  | The description of the event. |
| 2 | `DISPLAY` | VARCHAR(60) | NOT NULL |  | The display representation of the event. |
| 3 | `EVENT_KEY` | VARCHAR(20) | NOT NULL |  | The unique SurgiNet defined key for the event. |
| 4 | `RPT_EVENT_REF_ID` | DOUBLE | NOT NULL |  | Primary Key |
| 5 | `RPT_TYPE_CD` | DOUBLE | NOT NULL |  | The type of report that the event applies to. |
| 6 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 7 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 8 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 9 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 10 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

