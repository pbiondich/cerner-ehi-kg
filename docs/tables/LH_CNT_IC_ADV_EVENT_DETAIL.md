# LH_CNT_IC_ADV_EVENT_DETAIL

> Stores the event details saved within the Event Details component of the IC Advisor.

**Description:** LH_CNT_IC_ADV_EVENT_DETAIL  
**Table type:** ACTIVITY  
**Primary key:** _(not published — see note)_  
**Columns:** 20

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ACTIVE_IND` | DOUBLE | NOT NULL |  | The table row is active or inactive. A row is generally active unless it is in an inactive state such as logically deleted, combined away, pending purge, etc. |
| 2 | `BEG_EFFECTIVE_DT_TM` | DATETIME | NOT NULL |  | The date and time for which this table row becomes effective. Normally, this will be the date and time the row is added, but could be a past or future date and time. |
| 3 | `BSI_INFECTION_FLAG` | DOUBLE | NOT NULL |  | Indicates the selection of ""Secondary BSI infection"" radio button. |
| 4 | `CHLORHEXIDINE_FLAG` | DOUBLE | NOT NULL |  | Indicates the selection of ""Chlorhexidine Shower or Bath Complete"" radio button. |
| 5 | `DEATH_CONTRIBUTE_FLAG` | DOUBLE | NOT NULL |  | Indicates the selection of ""Event Contributed to Death"" radio button. |
| 6 | `EKS_ADVSR_EVENT_ID` | DOUBLE | NOT NULL | FK→ | Foreign key to EKS_ADVSR_EVENT table. |
| 7 | `END_EFFECTIVE_DT_TM` | DATETIME | NOT NULL |  | The date/time after which the row is no longer valid as active current data. This may be valued with the date that the row became inactive. |
| 8 | `ICU_CDAD_FLAG` | DOUBLE | NOT NULL |  | Indicates the selection of ""Admitted to ICU for CDAD Complications"" radio button. |
| 9 | `INF_AT_SURG_FLAG` | DOUBLE | NOT NULL |  | Flag value to determine the status of the "Infection Present at time of Surgery?" radio button question |
| 10 | `LH_CNT_IC_ADV_EVENT_DETAIL_ID` | DOUBLE | NOT NULL |  | Unique generated number that identifies a single row on the LH_CNT_IC_ADV_EVENT_DETAIL table. |
| 11 | `NHSN_PROCEDURE_CD` | DOUBLE | NOT NULL |  | NHSN Procedure code for the procedure associated to the HAI event. |
| 12 | `PATIENT_DIED_FLAG` | DOUBLE | NOT NULL |  | Indicates the selection of ""Patient Died"" radio button. |
| 13 | `POST_PROCEDURE_FLAG` | DOUBLE | NOT NULL |  | Indicates the selection of ""Post Procedure"" radio button. |
| 14 | `PROCEDURE_DT_TM` | DATETIME |  |  | Date of the procedure to be reported. |
| 15 | `SURG_CDAD_FLAG` | DOUBLE | NOT NULL |  | Indicates the selection of ""Surgery due to CDAD complications"". |
| 16 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 17 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 18 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 19 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 20 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `EKS_ADVSR_EVENT_ID` | [EKS_ADVSR_EVENT](EKS_ADVSR_EVENT.md) | `EKS_ADVSR_EVENT_ID` |

