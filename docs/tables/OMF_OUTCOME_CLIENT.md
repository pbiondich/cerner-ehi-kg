# OMF_OUTCOME_CLIENT

> Stores the list of OMF OUTCOMES SCORECARD CLIENTS

**Description:** OMF OUTCOME CLIENT  
**Table type:** REFERENCE  
**Primary key:** _(not published — see note)_  
**Columns:** 10

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `CLIENT_NBR` | DOUBLE | NOT NULL |  | This is a Cerner defined number describing each client |
| 2 | `HEALTH_PLAN_NAME` | CHAR(80) |  |  | This is the parent organization for this client |
| 3 | `HEALTH_SYSTEM_NAME` | CHAR(80) |  |  | This is the parent of the health plan |
| 4 | `HOSPITAL_NAME` | CHAR(80) |  |  | This is the name of the client |
| 5 | `JCAHO_HCO_NBR` | DOUBLE |  |  | This is the JCAHO number |
| 6 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 7 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 8 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 9 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 10 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

