# SEGMENT_PROCEDURE

> Contains the procedure associated with an "entry" of a perioperative document.

**Description:** Segment Procedure  
**Table type:** ACTIVITY  
**Primary key:** _(not published — see note)_  
**Columns:** 19

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ACTIVE_IND` | DOUBLE |  |  | The table row is active or inactive. A row is generally active unless it is in an inactive state such as logically deleted, combined away, pending purge, etc. |
| 2 | `ACTIVE_STATUS_CD` | DOUBLE | NOT NULL |  | Indicates the status of the row itself (not the data in the row) such as active, inactive, combined away, pending purge, etc. |
| 3 | `ACTIVE_STATUS_DT_TM` | DATETIME |  |  | The date and time that the active_status_cd was set. |
| 4 | `ACTIVE_STATUS_PRSNL_ID` | DOUBLE | NOT NULL |  | The person who caused the active_status_cd to be set or change. |
| 5 | `CREATE_APPLCTX` | DOUBLE |  |  | The application context responsible for inserting this row on the table. |
| 6 | `CREATE_DT_TM` | DATETIME |  |  | The date and time this row was inserted on the table. |
| 7 | `CREATE_PRSNL_ID` | DOUBLE | NOT NULL |  | The person responsible for inserting this row on the table. |
| 8 | `CREATE_TASK` | DOUBLE |  |  | The task responsible for inserting this row on the table. |
| 9 | `PARENT_ENTITY_NAME` | VARCHAR(50) |  |  | The table name for the "entry" of the perioperative document with which this row on the table is associated. |
| 10 | `PARENT_ENTITY_STATIC_ID` | DOUBLE | NOT NULL |  | The static id for the "entry" of the perioperative document with which this row on the table is associated. |
| 11 | `SEGMENT_PROC_ID` | DOUBLE | NOT NULL |  | The primary key, uniquely identifying a row on this table. |
| 12 | `SURG_CASE_PROC_ID` | DOUBLE | NOT NULL |  | Foreign key into the surg_case_procedure table.Column |
| 13 | `SURG_PROC_CD` | DOUBLE | NOT NULL |  | The surgical procedure documented as being associated with this "entry" of the perioperative document. |
| 14 | `SURG_PROC_PERF_STATIC_ID` | DOUBLE | NOT NULL |  | Surg Proc perf Static IDColumn |
| 15 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 16 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 17 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 18 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 19 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

