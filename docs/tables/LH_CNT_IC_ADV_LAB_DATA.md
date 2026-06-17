# LH_CNT_IC_ADV_LAB_DATA

> Infection Control advisor saved lab data. Stores lab data that has been associated to an advisor and saved.

**Description:** Lighthouse Content Infection Control Advisor Lab Data  
**Table type:** ACTIVITY  
**Primary key:** _(not published — see note)_  
**Columns:** 18

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ACTIVE_IND` | DOUBLE | NOT NULL |  | The table row is active or inactive. A row is generally active unless it is in an inactive state such as logically deleted, combined away, pending purge, etc. |
| 2 | `BEG_EFFECTIVE_DT_TM` | DATETIME | NOT NULL |  | The date and time for which this table row becomes effective. Normally, this will be the date and time the row is added, but could be a past or future date and time. |
| 3 | `COLLECT_DT_TM` | DATETIME |  |  | Stores the collection date time of the saved lab event. |
| 4 | `EKS_ADVSR_EVENT_ID` | DOUBLE | NOT NULL | FK→ | Foreign key to EKS_ADVSR_EVENT table. |
| 5 | `ENCNTR_ID` | DOUBLE | NOT NULL | FK→ | Foreign key to ENCOUNTER table. |
| 6 | `END_EFFECTIVE_DT_TM` | DATETIME | NOT NULL |  | The date/time after which the row is no longer valid as active current data. This may be valued with the date that the row became inactive. |
| 7 | `EVENT_CD` | DOUBLE | NOT NULL |  | Event code value for the saved lab event. |
| 8 | `EVENT_ID` | DOUBLE | NOT NULL |  | Pseudo Foreign key to CLINICAL_EVENT table. |
| 9 | `LH_CNT_IC_ADV_LAB_DATA_ID` | DOUBLE | NOT NULL |  | Unique generated number that identifies a single row on the LH_CNT_IC_ADV_LAB_DATA table. |
| 10 | `MDRO_CAT_NAME` | VARCHAR(150) |  |  | Stores the name assigned to the category. |
| 11 | `MDRO_IN_PLAN_IND` | DOUBLE | NOT NULL |  | MDRO category in NHSN plan indicator. 1 = MDRO Category in Plan |
| 12 | `RESULT_STATUS_CD` | DOUBLE | NOT NULL |  | Stores the result status code of the saved lab event. |
| 13 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 14 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 15 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 16 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 17 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 18 | `VALUE_NOMENCLATURE_DISP` | VARCHAR(250) |  |  | Stores the result display for the saved lab event |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `EKS_ADVSR_EVENT_ID` | [EKS_ADVSR_EVENT](EKS_ADVSR_EVENT.md) | `EKS_ADVSR_EVENT_ID` |
| `ENCNTR_ID` | [ENCOUNTER](ENCOUNTER.md) | `ENCNTR_ID` |

