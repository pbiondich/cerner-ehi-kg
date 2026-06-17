# PM_BBL_ACTION

> This table contains information pertaining to when bed are borrowed from a service for anothers service's use.

**Description:** Bed borrowing and lending action table.  
**Table type:** ACTIVITY  
**Primary key:** _(not published — see note)_  
**Columns:** 16

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ACTION_DT_TM` | DATETIME | NOT NULL |  | Date and time of action. |
| 2 | `ACTION_FLAG` | DOUBLE | NOT NULL |  | Flag used to determine type of action. |
| 3 | `ACTIVE_IND` | DOUBLE | NOT NULL |  | The table row is active or inactive. A row is generally active unless it is in an inactive state such as logically deleted, combined away, pending purge, etc. |
| 4 | `BEDS` | DOUBLE | NOT NULL |  | Number of beds in the action. |
| 5 | `BEG_EFFECTIVE_DT_TM` | DATETIME | NOT NULL |  | The date and time for which this table row becomes effective. Normally, this will be the date and time the row is added, but could be a past or future date and time. |
| 6 | `END_EFFECTIVE_DT_TM` | DATETIME | NOT NULL |  | The date/time after which the row is no longer valid as active current data. This may be valued with the date that the row became inactive. |
| 7 | `FROM_SERVICE_CD` | DOUBLE | NOT NULL |  | Service that lent the beds. |
| 8 | `PM_BBL_ACTION_ID` | DOUBLE | NOT NULL |  | Unique identifier. |
| 9 | `RETURNED_BEDS` | DOUBLE |  |  | Number of returned beds. |
| 10 | `TO_SERVICE_CD` | DOUBLE | NOT NULL |  | Service receiving the beds. |
| 11 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 12 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 13 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 14 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 15 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |
| 16 | `USER_ID` | DOUBLE | NOT NULL |  | User who performed the action. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

