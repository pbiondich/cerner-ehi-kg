# ENCNTR_LEGAL_STAT_REV_HIST

> Legal status review history.

**Description:** ENCNTR LEGAL STAT REV HIST  
**Table type:** ACTIVITY  
**Primary key:** _(not published — see note)_  
**Columns:** 17

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `BEG_EFFECTIVE_DT_TM` | DATETIME | NOT NULL |  | The date and time for which this table row becomes effective. Normally, this will be the date and time the row is added, but could be a past or future date and time. |
| 2 | `DECISION_CD` | DOUBLE | NOT NULL |  | The decision reached by the review board. ex. (guilty, not guilty) |
| 3 | `DISPOSITION_RECVD_DT_TM` | DATETIME |  |  | The date and time the disposition was received. |
| 4 | `ENCNTR_LEGSTAT_REV_HIST_ID` | DOUBLE | NOT NULL |  | Encounter legal status review relation id. |
| 5 | `ENCNTR_LEG_STAT_REV_R_ID` | DOUBLE | NOT NULL |  | The unique identifier for the encntr_legal_status_rev_r table. |
| 6 | `END_EFFECTIVE_DT_TM` | DATETIME | NOT NULL |  | The date/time after which the row is no longer valid as active current data. This may be valued with the date that the row became inactive. |
| 7 | `HEARING_DT_TM` | DATETIME |  |  | The date and time of the hearing. |
| 8 | `LEGAL_RECOMMENDATION_CD` | DOUBLE | NOT NULL |  | Legal recommendation action. |
| 9 | `LOCATION_CD` | DOUBLE | NOT NULL |  | The location of the hearing. |
| 10 | `OTHER_RECOMMENDATION_CD` | DOUBLE | NOT NULL |  | Other recommended action. |
| 11 | `REASON_RECVD_DT_TM` | DATETIME |  |  | Date and time the reason was received. |
| 12 | `RECOMMENDATION_CD` | DOUBLE | NOT NULL |  | Recommended action. |
| 13 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 14 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 15 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 16 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 17 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

