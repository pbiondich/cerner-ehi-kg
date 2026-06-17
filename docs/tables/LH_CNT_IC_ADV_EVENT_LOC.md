# LH_CNT_IC_ADV_EVENT_LOC

> Infection Control advisor saved location of event data. Stores location of event data that has been associated to an advisor and saved.

**Description:** LH_CNT_IC_ADV_EVENT_LOC  
**Table type:** ACTIVITY  
**Primary key:** _(not published — see note)_  
**Columns:** 18

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ACTIVE_IND` | DOUBLE | NOT NULL |  | The table row is active or inactive. A row is generally active unless it is in an inactive state such as logically deleted, combined away, pending purge, etc. |
| 2 | `BEG_EFFECTIVE_DT_TM` | DATETIME | NOT NULL |  | The date and time for which this table row becomes effective. Normally, this will be the date and time the row is added, but could be a past or future date and time. |
| 3 | `EKS_ADVSR_EVENT_ID` | DOUBLE | NOT NULL | FK→ | Foreign key to EKS_ADVSR_EVENT table. |
| 4 | `ENCNTR_ID` | DOUBLE | NOT NULL | FK→ | Foreign key to ENCOUNTER table. |
| 5 | `ENCNTR_LOC_HIST_ID` | DOUBLE | NOT NULL | FK→ | Foreign key to ENCNTR_LOC_HIST table. |
| 6 | `END_EFFECTIVE_DT_TM` | DATETIME | NOT NULL |  | The date/time after which the row is no longer valid as active current data. This may be valued with the date that the row became inactive. |
| 7 | `LH_CNT_IC_ADV_EVENT_LOC_ID` | DOUBLE | NOT NULL |  | PRIMARY KEY |
| 8 | `LOC_BED_CD` | DOUBLE | NOT NULL |  | Stores the location bed code for the saved location event. |
| 9 | `LOC_END_DT_TM` | DATETIME |  |  | Stores the end_effective_dt_tm from the ENCNTR_LOC_HIST table for the saved location event. |
| 10 | `LOC_FACILITY_CD` | DOUBLE | NOT NULL |  | Stores the location facility code for the saved location event. |
| 11 | `LOC_NURSE_UNIT_CD` | DOUBLE | NOT NULL |  | Stores the location nurse unit code for the saved location event. |
| 12 | `LOC_ROOM_CD` | DOUBLE | NOT NULL |  | Stores the location room code for the saved location event. |
| 13 | `LOC_START_DT_TM` | DATETIME |  |  | Stores the beg_effective_dt_tm from the ENCNTR_LOC_HIST table for the saved location event. |
| 14 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 15 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 16 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 17 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 18 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `EKS_ADVSR_EVENT_ID` | [EKS_ADVSR_EVENT](EKS_ADVSR_EVENT.md) | `EKS_ADVSR_EVENT_ID` |
| `ENCNTR_ID` | [ENCOUNTER](ENCOUNTER.md) | `ENCNTR_ID` |
| `ENCNTR_LOC_HIST_ID` | [ENCNTR_LOC_HIST](ENCNTR_LOC_HIST.md) | `ENCNTR_LOC_HIST_ID` |

