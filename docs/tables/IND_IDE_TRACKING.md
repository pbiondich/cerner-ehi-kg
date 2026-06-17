# IND_IDE_TRACKING

> This table is used to track investigational new drug or device

**Description:** this table is used to track drugs/devices  
**Table type:** REFERENCE  
**Primary key:** _(not published — see note)_  
**Columns:** 12

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `AGENT_DEV_ID` | DOUBLE | NOT NULL |  | This field uniquely identifies a row in the invest_agent_dev table. |
| 2 | `BEG_EFFECTIVE_DT_TM` | DATETIME | NOT NULL |  | The date and time for which this table row becomes effective. Normally, this will be the date and time the row is added, but could be a past or future date and time. |
| 3 | `COMMENT_TXT` | LONGBLOB |  |  | This field contains any comments about the tracking that are deemed appropriate. |
| 4 | `END_EFFECTIVE_DT_TM` | DATETIME | NOT NULL |  | The date/time after which the row is no longer valid as active current data. This may be valued with the date that the row became inactive. |
| 5 | `IND_IDE_TRACKING_ID` | DOUBLE | NOT NULL |  | Primary Key |
| 6 | `TRACKING_CD` | DOUBLE | NOT NULL |  | This field contains a code indicating the type of tracking that was performed. |
| 7 | `TRACKING_DT_TM` | DATETIME | NOT NULL |  | This field contains the date and time on which the IND/IDE tracking was performed. |
| 8 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 9 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 10 | `UPDT_DT_TM` | DOUBLE | NOT NULL |  | The date and time the row was last inserted or updated. |
| 11 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 12 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

