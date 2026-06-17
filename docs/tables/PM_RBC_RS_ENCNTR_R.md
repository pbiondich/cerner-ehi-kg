# PM_RBC_RS_ENCNTR_R

> The PM_RBC_RUN_SET_ENCNTR_R table stores information about each encounter that qualified for each set in the execution of the room & bed charge process.

**Description:** Person Management - Room and Bed Charge Run Set Encounter Relationship  
**Table type:** ACTIVITY  
**Primary key:** `PM_RBC_RS_ENCNTR_R_ID`  
**Columns:** 20  
**Referenced by:** 1 columns

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `CHARGE_EVENT_CNT` | DOUBLE | NOT NULL |  | Count of charge events submitted for this encounter. |
| 2 | `CHARGE_EVENT_FAIL_CNT` | DOUBLE | NOT NULL |  | Count of charge events that failed for this encounter. |
| 3 | `CHARGE_EVENT_SUCCESS_CNT` | DOUBLE | NOT NULL |  | Count of charge events that succeeded for this encounter. |
| 4 | `COMPLETE_DT_TM` | DATETIME |  |  | Date/time the room & bed charge processing completed for this encounter. |
| 5 | `DISCH_DT_TM` | DATETIME |  |  | The actual date/time that the patient was discharged from the facility. For this table, it is the discharge date/time at the time the room & bed charge process was executed. |
| 6 | `ENCNTR_ID` | DOUBLE | NOT NULL | FK→ | This is the value of the unique primary identifier of the ENCOUNTER table. It is an internal system assigned number. |
| 7 | `FAILURE_REASON_CD` | DOUBLE | NOT NULL |  | More detailed the reason the set is in a failed status. |
| 8 | `INPATIENT_ADMIT_DT_TM` | DATETIME |  |  | The date/time the patient was admitted as an inpatient. For this table, it is the inpatient admit date/time at the time the room & bed charge process was executed. |
| 9 | `LOG_LONG_TEXT_ID` | DOUBLE | NOT NULL | FK→ | Stores the identifier of the row on the pm_rbc_long_text table containing the general logging text for the processing of this encounter during the execution of the room & bed charge process. |
| 10 | `PM_RBC_RS_ENCNTR_R_ID` | DOUBLE | NOT NULL | PK | This is the value of the unique primary identifier of the PM_RBC_RS_ENCNTR table. It is an internal system assigned number. |
| 11 | `PM_RBC_RUN_SET_ID` | DOUBLE | NOT NULL | FK→ | This is the value of the unique primary identifier of the PM_RBC_RUN_SET table. It is an internal system assigned number. |
| 12 | `QUERY_LONG_TEXT_ID` | DOUBLE | NOT NULL | FK→ | Stores the identifier of the row on the pm_rbc_long_text table containing the encounter query text for this set in the execution of the room & bed charge process. |
| 13 | `REG_DT_TM` | DATETIME |  |  | The date/time that the registration or admission process was performed. For this table, it is the registration date/time at the time the room & bed charge process was executed. |
| 14 | `START_DT_TM` | DATETIME |  |  | Date/time the room & bed charge processing started for this encounter. |
| 15 | `STATUS_CD` | DOUBLE | NOT NULL |  | Overall status of this execution of the room & bed charge process. |
| 16 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 17 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 18 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 19 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 20 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `ENCNTR_ID` | [ENCOUNTER](ENCOUNTER.md) | `ENCNTR_ID` |
| `LOG_LONG_TEXT_ID` | [PM_RBC_LONG_TEXT](PM_RBC_LONG_TEXT.md) | `PM_RBC_LONG_TEXT_ID` |
| `PM_RBC_RUN_SET_ID` | [PM_RBC_RUN_SET](PM_RBC_RUN_SET.md) | `PM_RBC_RUN_SET_ID` |
| `QUERY_LONG_TEXT_ID` | [PM_RBC_LONG_TEXT](PM_RBC_LONG_TEXT.md) | `PM_RBC_LONG_TEXT_ID` |

## Referenced by (1)

| From table | Column |
|------------|--------|
| [PM_RBC_RS_ENCNTR_CHARGE_R](PM_RBC_RS_ENCNTR_CHARGE_R.md) | `PM_RBC_RS_ENCNTR_R_ID` |

