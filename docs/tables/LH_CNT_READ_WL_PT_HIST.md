# LH_CNT_READ_WL_PT_HIST

> Contains the historical records of patients that were placed on the Readmission Worklist.

**Description:** Readmission Worklist Patient History  
**Table type:** ACTIVITY  
**Primary key:** _(not published — see note)_  
**Columns:** 23

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ACTIVE_IND` | DOUBLE | NOT NULL |  | The table row is active or inactive. A row is generally active unless it is in an inactive state such as logically deleted, combined away, pending purge, etc. |
| 2 | `ADDED_DT_TM` | DATETIME | NOT NULL |  | Date/Time the patient was added |
| 3 | `ADDED_REASON_CD` | DOUBLE | NOT NULL |  | Reason patient was added to the worklist |
| 4 | `ADDED_UPDT_ID` | DOUBLE | NOT NULL |  | User who added the patient to the worklist |
| 5 | `BEG_EFFECTIVE_DT_TM` | DATETIME | NOT NULL |  | The date and time for which this table row becomes effective. Normally, this will be the date and time the row is added, but could be a past or future date and time. |
| 6 | `ENCNTR_ID` | DOUBLE | NOT NULL |  | Encounter Id |
| 7 | `END_EFFECTIVE_DT_TM` | DATETIME | NOT NULL |  | The date/time after which the row is no longer valid as active current data. This may be valued with the date that the row became inactive. |
| 8 | `LH_CNT_READMIT_WORKLIST_ID` | DOUBLE | NOT NULL |  | Original Key ID |
| 9 | `LH_CNT_READ_WL_PT_HIST_ID` | DOUBLE | NOT NULL |  | Unique generated number that identifies a single row on the LH_CNT_READ_WL_PT_HIST table. |
| 10 | `MANUALLY_ADDED_IND` | DOUBLE | NOT NULL |  | Defines if the patient was manually added to the worklist |
| 11 | `PERSON_ID` | DOUBLE | NOT NULL |  | Person Id |
| 12 | `RATING_DT_TM` | DATETIME | NOT NULL |  | Date/Time the rating was created |
| 13 | `RATING_REASON_CD` | DOUBLE | NOT NULL |  | Reason for the rating |
| 14 | `RATING_UPDT_ID` | DOUBLE | NOT NULL |  | User who created the rating |
| 15 | `RATING_VALUE` | DOUBLE | NOT NULL |  | Current Rating value for the patient |
| 16 | `REMOVE_DT_TM` | DATETIME | NOT NULL |  | Date/Time patient was removed from the worklist |
| 17 | `REMOVE_REASON_CD` | DOUBLE | NOT NULL |  | Reason for removing the patient from the worklist |
| 18 | `REMOVE_UPDT_ID` | DOUBLE | NOT NULL |  | User who removed the patient from the worklist |
| 19 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 20 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 21 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 22 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 23 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

