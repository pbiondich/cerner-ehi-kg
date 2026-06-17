# AOAV_ENCNTR_RISK_HIST

> Table contains the history of risk level for an encounter

**Description:** AOAV ENCOUNTER RISK HISTORY  
**Table type:** ACTIVITY  
**Primary key:** _(not published — see note)_  
**Columns:** 22

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ACTIVE_IND` | DOUBLE | NOT NULL |  | The table row is active or inactive. A row is generally active unless it is in an inactive state such as logically deleted, combined away, pending purge, etc. |
| 2 | `ACTIVE_STATUS_CD` | DOUBLE |  |  | Indicates the status of the row itself (not the data in the row) such as active, inactive, combined away, pending purge, etc. |
| 3 | `ACTIVE_STATUS_DT_TM` | DATETIME |  |  | The date and time that the active_status_cd was set. |
| 4 | `ACTIVE_STATUS_PRSNL_ID` | DOUBLE |  |  | The person who caused the active_status_cd to be set or change. |
| 5 | `AOAV_ENCNTR_RISK_HIST_ID` | DOUBLE | NOT NULL |  | PRIMARY KEY |
| 6 | `BEG_EFFECTIVE_DT_TM` | DATETIME | NOT NULL |  | The date and time for which this table row becomes effective. Normally, this will be the date and time the row is added, but could be a past or future date and time. |
| 7 | `CRITICAL_TIME_HOURS` | DOUBLE |  |  | The number of hours for a High Alert to become a Critical alert at the time this risk episode was started |
| 8 | `ENCNTR_ID` | DOUBLE | NOT NULL | FK→ | Unique generated number that identifies a single row on the ENCOUNTER table |
| 9 | `END_EFFECTIVE_DT_TM` | DATETIME | NOT NULL |  | The date/time after which the row is no longer valid as active current data. This may be valued with the date that the row became inactive. |
| 10 | `END_REASON_FLAG` | DOUBLE | NOT NULL |  | Flag that denotes the reason the risk ended (e.g. transfer to ICU, no risk, etc.) - 1=NO RISK 2=MODERATE RISK 3= HIGH RISK 4=CRITICAL RISK 5=TRANSFER TO ICU 6=TRANSFER TO SDU 7=TRANSFER TO FLOOR 8=DEATH 9=HOSPITAL DISCHARGE |
| 11 | `END_RISK_LEVEL_CD` | DOUBLE | NOT NULL |  | Code value from AOAV_RISK_LEVEL code_set that represents the specific risk level: Moderate, High, Critical or Low Risk that is indicated at the end of this episode |
| 12 | `END_RISK_VALUE` | DOUBLE |  |  | The value of DI_12_24 or DI_GT_24 that is used to end the risk episode or is current when the episode ended. |
| 13 | `HIGH_THRESHOLD_VALUE` | DOUBLE |  |  | The threshold value for a High alert at the time this risk episode was started |
| 14 | `LEVEL_OF_CARE_CD` | DOUBLE | NOT NULL |  | Code value that defines the level of care for a location |
| 15 | `MODERATE_THRESHOLD_VALUE` | DOUBLE |  |  | The threshold value for a Moderate alert at the time this risk episode was started |
| 16 | `RISK_LEVEL_CD` | DOUBLE | NOT NULL |  | Code value that defines the risk level (e.g. MODERATE, HIGH, CRITICAL) |
| 17 | `START_RISK_VALUE` | DOUBLE |  |  | The value of DI_12_24 or DI_GT_24 that is used to start the risk episode |
| 18 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 19 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 20 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 21 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 22 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `ENCNTR_ID` | [ENCOUNTER](ENCOUNTER.md) | `ENCNTR_ID` |

