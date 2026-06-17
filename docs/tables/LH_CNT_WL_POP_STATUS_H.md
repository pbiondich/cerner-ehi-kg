# LH_CNT_WL_POP_STATUS_H

> This table is used to store the history of the LH_CNT_WL_POP_STATUS table.

**Description:** LH_CNT_WL_POP_STATUS_H  
**Table type:** ACTIVITY  
**Primary key:** _(not published — see note)_  
**Columns:** 12

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ADDED_REASON_CD` | DOUBLE | NOT NULL |  | Reason the patient was added. |
| 2 | `BEG_EFFECTIVE_DT_TM` | DATETIME | NOT NULL |  | The date and time for which this table row becomes effective. Normally, this will be the date and time the row is added, but could be a past or future date and time. |
| 3 | `END_EFFECTIVE_DT_TM` | DATETIME |  |  | The date/time after which the row is no longer valid as active current data. This may be valued with the date that the row became inactive. |
| 4 | `LH_CNT_WL_POP_ID` | DOUBLE | NOT NULL |  | Foreign key of the associated population member. |
| 5 | `LH_CNT_WL_POP_STATUS_H_ID` | DOUBLE | NOT NULL |  | Unique generated number that identifies a single row on the LH_CNT_WL_POP_STATUS_H table. |
| 6 | `LH_CNT_WL_POP_STATUS_ID` | DOUBLE | NOT NULL |  | Foreign key of the associated population status. |
| 7 | `REMOVED_REASON_CD` | DOUBLE | NOT NULL |  | Reason the patient was removed. |
| 8 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 9 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 10 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 11 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 12 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

