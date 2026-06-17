# PM_OFFER_HIST

> Contains the transactional history of a list of offers for an encounter. All columns, except offer_hist_id, create_dt_tm, and the updt_* columns, are representing a snapshot of the pm_offer table, including the active_* columns.

**Description:** Patient Management Offer History  
**Table type:** ACTIVITY  
**Primary key:** _(not published — see note)_  
**Columns:** 36

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ACTIVE_IND` | DOUBLE | NOT NULL |  | The table row is active or inactive. A row is generally active unless it is in an inactive state such as logically deleted, combined away, pending purge, etc. |
| 2 | `ACTIVE_STATUS_CD` | DOUBLE | NOT NULL |  | Indicates the status of the row itself (not the data in the row) such as active, inactive, combined away, pending purge, etc. |
| 3 | `ACTIVE_STATUS_DT_TM` | DATETIME | NOT NULL |  | The date and time that the active_status_cd was set. |
| 4 | `ACTIVE_STATUS_PRSNL_ID` | DOUBLE | NOT NULL |  | The person who caused the active_status_cd to be set or change. |
| 5 | `ADMIT_OFFER_OUTCOME_CD` | DOUBLE | NOT NULL |  | The outcome of the admission offer. |
| 6 | `APPT_DT_TM` | DATETIME |  |  | The date time of the appointment associated with the offer. |
| 7 | `ARRIVED_ON_TIME_IND` | DOUBLE | NOT NULL |  | An indicator representing whether the patient arrived on time for their appointment or not. |
| 8 | `ATTENDANCE_CD` | DOUBLE | NOT NULL |  | The type of attendance. |
| 9 | `CANCEL_DT_TM` | DATETIME |  |  | The date time if the offer is cancelled. |
| 10 | `CREATE_DT_TM` | DATETIME | NOT NULL |  | The date and time that the history row was created. |
| 11 | `DNA_DT_TM` | DATETIME |  |  | The date time if the patient did not arrive. |
| 12 | `ENCNTR_ID` | DOUBLE | NOT NULL | FK→ | The encounter that the offer is written for. |
| 13 | `MEDICAL_STAFF_TYPE_CD` | DOUBLE | NOT NULL |  | Identifies the type of medical staff |
| 14 | `OFFER_DT_TM` | DATETIME |  |  | Offer_dt_tm is the date/time that the offer was made for. So if yesterday morning I offered a patient an appointment on May 5th at 8:00, my offer_made_dt_tm would be 4/15/2009 11:15am and my offer_dt_tm would be 5/5/2009 8:00am. |
| 15 | `OFFER_MADE_DT_TM` | DATETIME |  |  | The date and time the offer was made or refused. |
| 16 | `OFFER_TYPE_CD` | DOUBLE | NOT NULL |  | The Type of Offer that was recorded (accepted, refused, etc.). |
| 17 | `OUTCOME_OF_ATTENDANCE_CD` | DOUBLE | NOT NULL |  | The outcome of the Attendance. |
| 18 | `PAT_INITIATED_IND` | DOUBLE | NOT NULL |  | Indicator to note whether or not the patient initiated the offer date. |
| 19 | `PIFU_EXPIRY_DT_TM` | DATETIME |  |  | Specifies the date by which a patient initiated follow up pathway will expire. |
| 20 | `PIFU_OUTCOME_CD` | DOUBLE |  |  | Specifies the outcome of a patient initiated follow up pathway |
| 21 | `PIFU_PATHWAY_IND` | DOUBLE |  |  | Specifies whether there is a patient initiated follow up pathway present for the offer |
| 22 | `PIFU_REVIEW_DT_TM` | DATETIME |  |  | Specifies the date by which a patient initiated follow up pathway needs to be reviewed |
| 23 | `PM_OFFER_HIST_ID` | DOUBLE | NOT NULL |  | This is the value of the unique primary identifier of the offer hist table. It is an internal system assigned number. |
| 24 | `PM_OFFER_ID` | DOUBLE | NOT NULL | FK→ | The ID of the offer the history is related to. |
| 25 | `REASONABLE_OFFER_IND` | DOUBLE | NOT NULL |  | An indicator representing whether or not the offer was considered reasonable. |
| 26 | `REMOVE_FROM_WL_IND` | DOUBLE | NOT NULL |  | An indicator representing whether this offer should trigger the patient to be removed from the waitlist. |
| 27 | `SCHEDULE_ID` | DOUBLE | NOT NULL |  | The Schedule that this offer represents. |
| 28 | `SCH_REASON_CD` | DOUBLE | NOT NULL |  | The Reason for the latest change to the appointment associated to the offer. Could be the Cancel reason, the Reschedule reason, or the DNA reason. |
| 29 | `TCI_DT_TM` | DATETIME |  |  | The date and time the patient should arrive. |
| 30 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 31 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 32 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 33 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 34 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 35 | `WL_REASON_FOR_REMOVAL_CD` | DOUBLE | NOT NULL |  | The reason the patient should be removed from the waitlist. |
| 36 | `WL_REMOVAL_DT_TM` | DATETIME |  |  | The date and time for the removal from the waitlist. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `ENCNTR_ID` | [ENCOUNTER](ENCOUNTER.md) | `ENCNTR_ID` |
| `PM_OFFER_ID` | [PM_OFFER](PM_OFFER.md) | `PM_OFFER_ID` |

