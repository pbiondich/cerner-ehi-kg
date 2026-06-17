# EKS_ADVSR_EVENT

> Event tracking table, contains a row for each time a Discern Advisor event has occurred.

**Description:** EKS Advisor Event  
**Table type:** ACTIVITY  
**Primary key:** `EKS_ADVSR_EVENT_ID`  
**Columns:** 18  
**Referenced by:** 11 columns

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ACTIVE_IND` | DOUBLE | NOT NULL |  | The table row is active or inactive. A row is generally active unless it is in an inactive state such as logically deleted, combined away, pending purge, etc. |
| 2 | `ADVSR_EVENT_DESC` | VARCHAR(100) | NOT NULL |  | This will be a brief description of the Discern Advisor that has been saved. |
| 3 | `ADVSR_GROUP_ID` | DOUBLE | NOT NULL |  | Group ID is used to track changes to the Discern Advisor event. The ADVSR_GROUP_ID will be the same for all rows of a specific Discern Advisor Event. The ADVSR_GROUP_ID will be the same as the EKS_ADVSR_EVENT_ID for the first event. |
| 4 | `ADVSR_STATUS_CD` | DOUBLE | NOT NULL |  | Indicates the status of the event itself (not the data in the row) such as COMPLETE, SAVED, SUBMITTED, INPROGRESS etc. |
| 5 | `ADVSR_TYPE_CD` | DOUBLE | NOT NULL |  | The type of event that row is being written from. Pre-defined values by Cerner. |
| 6 | `BEG_EFFECTIVE_DT_TM` | DATETIME | NOT NULL |  | The date and time for which this table row becomes effective. Normally, this will be the date and time the row is added, but could be a past or future date and time. |
| 7 | `EKS_ADVSR_EVENT_ID` | DOUBLE | NOT NULL | PK | This is the unique identifier for rows on this table. The value of this field is identified by obtaining the next sequential number in the PathNet_Seq. |
| 8 | `ENCNTR_ID` | DOUBLE | NOT NULL | FK→ | The encounter associated with the discern adviser event. |
| 9 | `END_EFFECTIVE_DT_TM` | DATETIME | NOT NULL |  | The date/time after which the row is no longer valid as active current data. This may be valued with the date that the row became inactive. |
| 10 | `EVENT_DT_TM` | DATETIME |  |  | This field identifies the date/time the advisor event has occurred or will occur. |
| 11 | `LOCATION_CD` | DOUBLE |  | FK→ | The field identifies the location of the patient. |
| 12 | `LONG_TEXT_ID` | DOUBLE | NOT NULL |  | Identifies entry in the long text table which contains contains the XML. |
| 13 | `PERSON_ID` | DOUBLE | NOT NULL | FK→ | The ID of the person associated to the discern adviser event. |
| 14 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 15 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 16 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 17 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 18 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `ENCNTR_ID` | [ENCOUNTER](ENCOUNTER.md) | `ENCNTR_ID` |
| `LOCATION_CD` | [LOCATION](LOCATION.md) | `LOCATION_CD` |
| `PERSON_ID` | [PERSON](PERSON.md) | `PERSON_ID` |

## Referenced by (11)

| From table | Column |
|------------|--------|
| [LH_CNT_ADVSR_EVENT](LH_CNT_ADVSR_EVENT.md) | `EKS_ADVSR_EVENT_ID` |
| [LH_CNT_IC_ADV_EVENT_DETAIL](LH_CNT_IC_ADV_EVENT_DETAIL.md) | `EKS_ADVSR_EVENT_ID` |
| [LH_CNT_IC_ADV_EVENT_LOC](LH_CNT_IC_ADV_EVENT_LOC.md) | `EKS_ADVSR_EVENT_ID` |
| [LH_CNT_IC_ADV_LAB_DATA](LH_CNT_IC_ADV_LAB_DATA.md) | `EKS_ADVSR_EVENT_ID` |
| [LH_CNT_IC_ADV_LTD](LH_CNT_IC_ADV_LTD.md) | `EKS_ADVSR_EVENT_ID` |
| [LH_CNT_IC_ADV_MICRO](LH_CNT_IC_ADV_MICRO.md) | `EKS_ADVSR_EVENT_ID` |
| [LH_CNT_IC_ADV_RISK_FACTOR](LH_CNT_IC_ADV_RISK_FACTOR.md) | `EKS_ADVSR_EVENT_ID` |
| [LH_CNT_IC_ADV_SEL_CRITERIA](LH_CNT_IC_ADV_SEL_CRITERIA.md) | `EKS_ADVSR_EVENT_ID` |
| [LH_CNT_IC_ADV_SPEC_EVENT](LH_CNT_IC_ADV_SPEC_EVENT.md) | `EKS_ADVSR_EVENT_ID` |
| [LH_CNT_IC_ADV_SURG_DATA](LH_CNT_IC_ADV_SURG_DATA.md) | `EKS_ADVSR_EVENT_ID` |
| [LH_CNT_IC_ADV_WOUND_DATA](LH_CNT_IC_ADV_WOUND_DATA.md) | `EKS_ADVSR_EVENT_ID` |

