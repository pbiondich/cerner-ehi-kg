# LH_CNT_WL_RATING_HIST

> Holds the history of the rating associated to patients in the readmission worklist

**Description:** LH_CNT_WL_RATING_HIST  
**Table type:** ACTIVITY  
**Primary key:** _(not published — see note)_  
**Columns:** 15

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ACTIVE_IND` | DOUBLE | NOT NULL |  | The table row is active or inactive. A row is generally active unless it is in an inactive state such as logically deleted, combined away, pending purge, etc. |
| 2 | `BEG_EFFECTIVE_DT_TM` | DATETIME | NOT NULL |  | The date and time for which this table row becomes effective. Normally, this will be the date and time the row is added, but could be a past or future date and time. |
| 3 | `END_EFFECTIVE_DT_TM` | DATETIME | NOT NULL |  | The date/time after which the row is no longer valid as active current data. This may be valued with the date that the row became inactive. |
| 4 | `LH_CNT_READMIT_WORKLIST_ID` | DOUBLE | NOT NULL |  | ID of corresponding row on the LH_CNT_READMIT_WORKLIST table |
| 5 | `LH_CNT_WL_RATING_HIST_ID` | DOUBLE | NOT NULL |  | PRIMARY KEY |
| 6 | `LH_CNT_WL_RATING_ID` | DOUBLE | NOT NULL |  | ID of corresponding row on the LH_CNT_WL_RATING table |
| 7 | `RATING_REASON_CD` | DOUBLE | NOT NULL |  | The reason code from code set 4003033 |
| 8 | `RATING_UPDT_DT_TM` | DATETIME | NOT NULL |  | Date & time that the rating was assigned to the patient |
| 9 | `RATING_UPDT_ID` | DOUBLE | NOT NULL |  | The id of person who assigned the rating to the patient |
| 10 | `RATING_VALUE` | DOUBLE | NOT NULL |  | Rating value of the patient |
| 11 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 12 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 13 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 14 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 15 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

