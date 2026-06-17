# SUCCESSION_TYPE_CD

> SUCCESSION TYPE CODE VALUES TABLE

**Description:** SUCCESSION TYPE CODE  
**Table type:** REFERENCE  
**Primary key:** _(not published — see note)_  
**Columns:** 15

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `CODE_DEFINITION` | VARCHAR(40) |  |  | Code Definition |
| 2 | `CODE_DESCR` | VARCHAR(20) |  |  | Code Description |
| 3 | `CODE_DISP` | VARCHAR(12) |  |  | Code Display |
| 4 | `CODE_DISP_KEY` | VARCHAR(12) | NOT NULL |  | Code Display Key |
| 5 | `CODE_STATUS_CD` | DOUBLE | NOT NULL |  | Code Status Code |
| 6 | `COLLATING_SEQ` | DOUBLE |  |  | Collating Sequence |
| 7 | `SUCCESSION_TYPE_CD` | DOUBLE | NOT NULL |  | Succession Type Code |
| 8 | `SUCCN_CLASS_CD` | DOUBLE | NOT NULL |  | Succession Class Code |
| 9 | `SUCCN_PRIORITY` | DOUBLE |  |  | Succession Priority |
| 10 | `SUCCN_STATUS_CD` | DOUBLE | NOT NULL |  | Succession Status Code |
| 11 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 12 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 13 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 14 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 15 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

