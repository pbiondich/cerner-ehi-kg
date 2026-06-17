# RAD_TRACKING_ROOMS

> This table is stores referece data for those locations that are used in radiology patient tracking

**Description:** Rad Tracking Rooms  
**Table type:** REFERENCE  
**Primary key:** _(not published — see note)_  
**Columns:** 12

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ALLOWED_TIME` | DOUBLE |  |  | Time a patient is allowed in a specified room before they are considered over due. |
| 2 | `CALL_TRANS_WAIT_ROOM_CD` | DOUBLE | NOT NULL |  | Transport location that a patient will be moved to when a transport is called after exam completion. |
| 3 | `LATE_REPORT_IND` | DOUBLE |  |  | Indicates if this location should be used on late reports |
| 4 | `LOG_OUT_ACTION` | DOUBLE |  |  | Defines what action should be taken when an exam is completed for this location. |
| 5 | `PARENT_ENTITY_ID` | DOUBLE | NOT NULL |  | Defines a reference to a row on a table defined by the parent entity name. |
| 6 | `PARENT_ENTITY_NAME` | VARCHAR(32) | NOT NULL |  | Defines what table the parent_entity_id references |
| 7 | `TRACKING_IND` | DOUBLE |  |  | Attribute that defines if this location will be used in patient tracking. |
| 8 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 9 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 10 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 11 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 12 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

