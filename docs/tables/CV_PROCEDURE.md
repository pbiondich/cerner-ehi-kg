# CV_PROCEDURE

> Cvnet Omf Summary table

**Description:** CVNet Summary Table-Used in storing non clinical events for OMF Management rep  
**Table type:** ACTIVITY  
**Primary key:** `PROCEDURE_ID`  
**Columns:** 46  
**Referenced by:** 1 columns

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ACTIVE_IND` | DOUBLE |  |  | The table row is active or inactive. A row is generally active unless it is in an inactive state such as logically deleted, combined away, pending purge, etc. |
| 2 | `ACTIVE_STATUS_CD` | DOUBLE | NOT NULL |  | Indicates the status of the row itself (not the data in the row) such as active, inactive, combined away, pending purge, etc. |
| 3 | `ACTIVE_STATUS_DT_TM` | DATETIME |  |  | The date and time that the active_status_cd was set. |
| 4 | `ACTIVE_STATUS_PRSNL_ID` | DOUBLE | NOT NULL |  | The person who caused the active_status_cd to be set or change. |
| 5 | `BEG_EFFECTIVE_DT_TM` | DATETIME |  |  | The date and time for which this table row becomes effective. Normally, this will be the date and time the row is added, but could be a past or future date and time. |
| 6 | `CV_CASE_ID` | DOUBLE | NOT NULL | FK→ | This is a foreign key and it is the unique identifier to the Cv_Case table |
| 7 | `DATA_STATUS_CD` | DOUBLE | NOT NULL |  | Data status indicates a level of authenticity of the row data. Typically this will either be AUTHENTICATED or UNAUTHENTICATED. |
| 8 | `DATA_STATUS_DT_TM` | DATETIME |  |  | The date and time that the data_status_cd was set. |
| 9 | `DATA_STATUS_PRSNL_ID` | DOUBLE | NOT NULL |  | The person who caused the data_status_cd to be set or change. |
| 10 | `DEPT_CD` | DOUBLE | NOT NULL |  | Used for CVNet Management reporting. |
| 11 | `DOC_INLAB_DT_TM` | DATETIME |  |  | The date and time the attending physician shows up in the lab |
| 12 | `DOC_PREP_MIN` | DOUBLE |  |  | The time the physician prepares before the procedure in minutes |
| 13 | `END_EFFECTIVE_DT_TM` | DATETIME |  |  | The date/time after which the row is no longer valid as active current data. This may be valued with the date that the row became inactive. |
| 14 | `EVENT_TYPE_CD` | DOUBLE | NOT NULL |  | Event type code defines the group of data this particular event belongs for example Lesion,PTCA. Case. etc. |
| 15 | `LOS_ADM_PROC` | DOUBLE |  |  | Length of Stay From the time the patient was admitted to the time a procedure was performed. |
| 16 | `LOS_PROC_DISCH` | DOUBLE |  |  | Length of Stay from the begining of the Procedure to Discharge |
| 17 | `NUM_LESION` | DOUBLE |  |  | Numbers of lesions attempted |
| 18 | `NUM_PROC_COMPL` | DOUBLE |  |  | Numbers of Procedure complicationsColumn |
| 19 | `NUM_PROC_IND` | DOUBLE |  |  | Numbers of procedure indications. Used for calculating the numbers of procedure |
| 20 | `NURSE_ID` | DOUBLE | NOT NULL |  | Nurse identity. This is the person id of the attending nurse or staff. It is derived from the person table |
| 21 | `PAT_ADM_DT_TM` | DATETIME |  |  | Patient Admission Date and time. |
| 22 | `PAT_ADM_IND` | DOUBLE |  |  | Patient Admision IndicatorColumn |
| 23 | `PAT_DEATH_IND` | DOUBLE |  |  | Patient death indicator. This attributes assist in calculating the mortality rate in "OMF" |
| 24 | `PAT_DISCH_DT_TM` | DATETIME |  |  | The time and date a patient is discharged |
| 25 | `PAT_DISCH_IND` | DOUBLE |  |  | An indicator to shows that a patient has been discharged |
| 26 | `PAT_INLAB_DT_TM` | DATETIME |  |  | The date and time a patient was in the lab |
| 27 | `PAT_INLAB_MIN` | DOUBLE |  |  | The time a patient spent in the lab calculated in minutes. |
| 28 | `PAT_WAIT_MIN` | DOUBLE |  |  | Patient waiting time expressed in minutes |
| 29 | `PROCEDURE_ID` | DOUBLE | NOT NULL | PK | This is the unique identifier of a row |
| 30 | `PROC_COMPLETE_IND` | DOUBLE |  |  | An indicator that flags the completion of a procedure This is used in calculating the numbers of completed procedures |
| 31 | `PROC_DUR_MIN` | DOUBLE |  |  | The time in minutes the procedure lasted |
| 32 | `PROC_END_DT_TM` | DATETIME |  |  | The date and time the procedure ended |
| 33 | `PROC_NAME_CD` | DOUBLE | NOT NULL |  | Name of procedure . |
| 34 | `PROC_PHYSIC_ID` | DOUBLE | NOT NULL |  | Procedure physician id. This is derived from the person table. It is the primary indicator of the person table |
| 35 | `PROC_START_DAY` | DOUBLE |  |  | Procedure Start day. The day of the week the procedure was started e.g. 1 = Monday |
| 36 | `PROC_START_DT_TM` | DATETIME |  |  | Procedure Start date and time. The date and time the procedure was started |
| 37 | `PROC_START_HOUR` | DOUBLE |  |  | Hour of the day the procedure was started e.g. 10.00 |
| 38 | `PROC_START_MNTH` | DOUBLE |  |  | The month of the year the procedure was started |
| 39 | `TOTAL_PROC_COMPL` | DOUBLE |  |  | Total numbers of procedure complicationsColumn |
| 40 | `UPDT_APP` | DOUBLE |  |  | Registered (assigned) application number for the process that inserted or updated the row |
| 41 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 42 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 43 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 44 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 45 | `UPDT_REQ` | DOUBLE |  |  | registered of assigned request number for the process that inserted or updated the row |
| 46 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `CV_CASE_ID` | [CV_CASE](CV_CASE.md) | `CV_CASE_ID` |

## Referenced by (1)

| From table | Column |
|------------|--------|
| [CV_PROC_ABSTR_DATA](CV_PROC_ABSTR_DATA.md) | `PROCEDURE_ID` |

