# RAD_ENCNTR_TYPE_LOGOUT

> This table defines the action to be taken for an encounter type when an exam is completed.

**Description:** Rad Encounter Type Logout  
**Table type:** REFERENCE  
**Primary key:** _(not published — see note)_  
**Columns:** 8

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `CALL_TRANS_WAIT_ROOM_CD` | DOUBLE | NOT NULL |  | Transport location that a patient will be moved to when a transport is called after exam completion. |
| 2 | `ENCNTR_TYPE_CD` | DOUBLE | NOT NULL |  | Encounter type for this relationship |
| 3 | `LOG_OUT_ACTION` | DOUBLE |  |  | Action to be taken for this encounter type when an exam is completed. |
| 4 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 5 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 6 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 7 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 8 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

