# OMF_DASHBOARD

> Primary table for omf dashboards

**Description:** This is the top level dashboard table, it stores all of the basic info.  
**Table type:** ACTIVITY  
**Primary key:** _(not published — see note)_  
**Columns:** 11

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `DISTRIBUTED_IND` | DOUBLE |  |  | Indicator whether the dashboard is distributed |
| 2 | `NAME` | VARCHAR(50) | NOT NULL |  | The Textual name of the dashboard |
| 3 | `OMF_DASHBOARD_ID` | DOUBLE | NOT NULL |  | Table key, unique identifier created by omf_seq |
| 4 | `PATH` | VARCHAR(250) |  |  | Contains the network path to the dashboard |
| 5 | `PREV_DASHBOARD_ID` | DOUBLE | NOT NULL |  | Contains a reference to the previous version of the dashboard, used to remove the previous version once the new version is distributed. |
| 6 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 7 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 8 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 9 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 10 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |
| 11 | `VERSION` | DOUBLE | NOT NULL |  | Contains the current version number for a dashboard |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

