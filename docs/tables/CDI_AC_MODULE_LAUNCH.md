# CDI_AC_MODULE_LAUNCH

> The CDI Ascent Capture Module Launch table

**Description:** CDI Ascent Capture Module Launch  
**Table type:** ACTIVITY  
**Primary key:** _(not published — see note)_  
**Columns:** 18

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `CDI_AC_MODULE_LAUNCH_ID` | DOUBLE | NOT NULL |  | cdi ascent capture module launch identifier |
| 2 | `COMPLETEDTID` | VARCHAR(38) | NOT NULL |  | completed identifier |
| 3 | `ENDDATETIME` | DATETIME | NOT NULL |  | end date time |
| 4 | `INPROCESSTID` | VARCHAR(38) | NOT NULL |  | in process identifier |
| 5 | `MODULELAUNCHID` | VARCHAR(38) | NOT NULL |  | module launch identifier |
| 6 | `MODULENAME` | VARCHAR(32) | NOT NULL |  | module name |
| 7 | `MODULEUNIQUEID` | VARCHAR(250) |  |  | module unique identifier |
| 8 | `ORPHANED` | DOUBLE |  |  | orphaned |
| 9 | `SITEID` | DOUBLE |  |  | site identifier |
| 10 | `STARTDATETIME` | DATETIME |  |  | start date and time |
| 11 | `STATIONID` | VARCHAR(32) |  |  | station identifier |
| 12 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 13 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 14 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 15 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 16 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |
| 17 | `USERID` | VARCHAR(50) |  |  | user identifier |
| 18 | `USERNAME` | VARCHAR(80) | NOT NULL |  | Username of person |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

