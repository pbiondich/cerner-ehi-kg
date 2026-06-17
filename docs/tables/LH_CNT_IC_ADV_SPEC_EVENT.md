# LH_CNT_IC_ADV_SPEC_EVENT

> Stores the data selected within the IC Advisor Specify Event section

**Description:** lh_cnt_ic_adv_spec_event  
**Table type:** ACTIVITY  
**Primary key:** _(not published — see note)_  
**Columns:** 16

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ACTIVE_IND` | DOUBLE | NOT NULL |  | The table row is active or inactive. A row is generally active unless it is in an inactive state such as logically deleted, combined away, pending purge, etc. |
| 2 | `ASA_SCORE_CD` | DOUBLE | NOT NULL |  | The event code of the selected ASA score from codeset 10051. (ASA I, ASA II). |
| 3 | `BEG_EFFECTIVE_DT_TM` | DATETIME | NOT NULL |  | The date and time for which this table row becomes effective. Normally, this will be the date and time the row is added, but could be a past or future date and time. |
| 4 | `DETECTED_CD` | DOUBLE | NOT NULL |  | The selected event code of where the event was first detected from codeset 4003139. (At admission, after discharge, etc.) |
| 5 | `EKS_ADVSR_EVENT_ID` | DOUBLE | NOT NULL | FK→ | Foreign key to EKS_ADVSR_EVENT table. |
| 6 | `END_EFFECTIVE_DT_TM` | DATETIME | NOT NULL |  | The date/time after which the row is no longer valid as active current data. This may be valued with the date that the row became inactive. |
| 7 | `EVENT_FLAG` | DOUBLE | NOT NULL |  | This flag indicates whether any generic events have been signed in the advisor. 0 - None, 1 - CAUTI, 2 - CLABSI, 3 - Aspiration Pneumonia |
| 8 | `INFECTION_TYPE_CD` | DOUBLE | NOT NULL |  | The event code of the selected infection type from codeset 4003137. (HAI, CAI, etc.) |
| 9 | `LH_CNT_IC_ADV_SPEC_EVENT_ID` | DOUBLE | NOT NULL |  | Unique generated number that identifies a single row on the lh_cnt_ic_adv_spec_event table. |
| 10 | `SPECIFIC_EVENT_DT_TM` | DATETIME |  |  | The documented event date and time to be reported to NHSN. |
| 11 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 12 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 13 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 14 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 15 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 16 | `WOUND_CLASS_CD` | DOUBLE | NOT NULL |  | The event code of the selected wound class from codeset 10038. (Clean, contaminated, etc.) |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `EKS_ADVSR_EVENT_ID` | [EKS_ADVSR_EVENT](EKS_ADVSR_EVENT.md) | `EKS_ADVSR_EVENT_ID` |

