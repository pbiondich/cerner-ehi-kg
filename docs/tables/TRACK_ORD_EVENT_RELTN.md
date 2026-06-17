# TRACK_ORD_EVENT_RELTN

> Uesd to associate order catalog or catalog type code with the track_events

**Description:** TRACK ORD EVENT RELTN  
**Table type:** REFERENCE  
**Primary key:** _(not published — see note)_  
**Columns:** 9

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ASSOCIATION_TYPE_CD` | DOUBLE | NOT NULL |  | Defines what type of association from code set 20504 |
| 2 | `CAT_OR_CATTYPE_CD` | DOUBLE | NOT NULL |  | catalog code or catalog type code more often used is catalog cd from code set 200 and less often used is catalog type cd from 6000 |
| 3 | `TRACK_EVENT_ID` | DOUBLE | NOT NULL |  | Track event id from the track event table.Column |
| 4 | `TRACK_GROUP_CD` | DOUBLE | NOT NULL |  | tracking group codeColumn |
| 5 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 6 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 7 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 8 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 9 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

