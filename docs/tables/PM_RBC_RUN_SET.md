# PM_RBC_RUN_SET

> The PM_RBC_RUN table stores information about each set in the execution of the room and bed charge process.

**Description:** Person Management - Room and Bed Charge Run Set  
**Table type:** ACTIVITY  
**Primary key:** `PM_RBC_RUN_SET_ID`  
**Columns:** 20  
**Referenced by:** 1 columns

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `CHARGE_EVENT_CNT` | DOUBLE | NOT NULL |  | Count of charge events submitted in this set. |
| 2 | `CHARGE_EVENT_FAIL_CNT` | DOUBLE | NOT NULL |  | Count of charge events that failed in this set. |
| 3 | `CHARGE_EVENT_SUCCESS_CNT` | DOUBLE | NOT NULL |  | Count of charge events that succeeded in this set. |
| 4 | `COMPLETE_DT_TM` | DATETIME |  |  | Date/time room & bed charge process execution completed. |
| 5 | `ENCNTR_CNT` | DOUBLE | NOT NULL |  | Count of encounters that qualified for this set. |
| 6 | `ENCNTR_FAIL_CNT` | DOUBLE | NOT NULL |  | Count of encounters that failed in this set. |
| 7 | `ENCNTR_SUCCESS_CNT` | DOUBLE | NOT NULL |  | Count of encounters that succeeded in this set. |
| 8 | `FAILURE_REASON_CD` | DOUBLE | NOT NULL |  | More detailed the reason the set is in a failed status. |
| 9 | `LOG_LONG_TEXT_ID` | DOUBLE | NOT NULL | FK→ | Stores the identifier of the row on the pm_rbc_long_text table containing the general logging text for this set in the execution of the room & bed charge process. |
| 10 | `PM_RBC_PARM_SET_R_ID` | DOUBLE | NOT NULL | FK→ | This is the value of the unique primary identifier of the PM_RBC_PARM_SET_R table. It is an internal system assigned number. |
| 11 | `PM_RBC_RUN_ID` | DOUBLE | NOT NULL | FK→ | This is the value of the unique primary identifier of the PM_RBC_RUN table. It is an internal system assigned number. |
| 12 | `PM_RBC_RUN_SET_ID` | DOUBLE | NOT NULL | PK | This is the value of the unique primary identifier of the PM_RBC_RUN_SET table. It is an internal system assigned number. |
| 13 | `QUERY_LONG_TEXT_ID` | DOUBLE | NOT NULL | FK→ | Stores the identifier of the row on the pm_rbc_long_text table containing the encounter query text for this set in the execution of the room & bed charge process. |
| 14 | `START_DT_TM` | DATETIME |  |  | Date/time room & bed charge process execution started. |
| 15 | `STATUS_CD` | DOUBLE | NOT NULL |  | Overall status of this set in the execution of the room & bed charge process. |
| 16 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 17 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 18 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 19 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 20 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `LOG_LONG_TEXT_ID` | [PM_RBC_LONG_TEXT](PM_RBC_LONG_TEXT.md) | `PM_RBC_LONG_TEXT_ID` |
| `PM_RBC_PARM_SET_R_ID` | [PM_RBC_PARM_SET_R](PM_RBC_PARM_SET_R.md) | `PM_RBC_PARM_SET_R_ID` |
| `PM_RBC_RUN_ID` | [PM_RBC_RUN](PM_RBC_RUN.md) | `PM_RBC_RUN_ID` |
| `QUERY_LONG_TEXT_ID` | [PM_RBC_LONG_TEXT](PM_RBC_LONG_TEXT.md) | `PM_RBC_LONG_TEXT_ID` |

## Referenced by (1)

| From table | Column |
|------------|--------|
| [PM_RBC_RS_ENCNTR_R](PM_RBC_RS_ENCNTR_R.md) | `PM_RBC_RUN_SET_ID` |

