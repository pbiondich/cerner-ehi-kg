# ENCNTR_CRIMINAL_CHRGS_HIST

> This table will hold the history of the outstanding criminal charges for an encounter.

**Description:** Encounter outstanding charges history.  
**Table type:** ACTIVITY  
**Primary key:** _(not published — see note)_  
**Columns:** 11

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `BEG_EFFECTIVE_DT_TM` | DATETIME | NOT NULL |  | The date and time for which this table row becomes effective. Normally, this will be the date and time the row is added, but could be a past or future date and time. |
| 2 | `COURT_DT_TM` | DATETIME |  |  | The court date and time. |
| 3 | `COURT_FILE_NUM` | VARCHAR(40) |  |  | The file number representing the court case. |
| 4 | `COURT_LOCATION_CD` | DOUBLE | NOT NULL |  | The location at which the court proceedings took place. |
| 5 | `END_EFFECTIVE_DT_TM` | DATETIME | NOT NULL |  | The date/time after which the row is no longer valid as active current data. This may be valued with the date that the row became inactive. |
| 6 | `OUTSTANDING_CHARGES_HIST_ID` | DOUBLE | NOT NULL |  | The unique identifier for the encntr_criminal_chrgs_hist table. |
| 7 | `OUTSTANDING_CHARGES_R_ID` | DOUBLE | NOT NULL |  | The unique identifier for the encntr_criminal_charges_r table. |
| 8 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 9 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 10 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 11 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

