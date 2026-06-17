# UCMR_CASE_STEP

> This table stores specific information for each step of a case type's workflow.

**Description:** Unified Case Management Reference Case Step  
**Table type:** REFERENCE  
**Primary key:** `UCMR_CASE_STEP_ID`  
**Columns:** 17  
**Referenced by:** 5 columns

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ACTIVE_IND` | DOUBLE | NOT NULL |  | The table row is active or inactive. A row is generally active unless it is in an inactive state such as logically deleted, combined away, pending purge, etc. |
| 2 | `ACTIVE_STATUS_CD` | DOUBLE | NOT NULL |  | Indicates the status of the row itself (not the data in the row) such as active, inactive, combined away, pending purge, etc. |
| 3 | `BEG_EFFECTIVE_DT_TM` | DATETIME | NOT NULL |  | The date and time for which this table row becomes effective. Normally, this will be the date and time the row is added, but could be a past or future date and time. |
| 4 | `CASE_STEP_CAT_CD` | DOUBLE | NOT NULL |  | Indicates the catalog item to which this case step information is related. |
| 5 | `END_EFFECTIVE_DT_TM` | DATETIME | NOT NULL |  | The date/time after which the row is no longer valid as active current data. This may be valued with the date that the row became inactive. |
| 6 | `OPTIONAL_STEP_CD` | DOUBLE | NOT NULL |  | Identifies the optional properties of a case step such as Not Optional, Optional, Optional/Prompt, or Optional/Prompt/Default. |
| 7 | `PARENT_UCMR_CASE_STEP_ID` | DOUBLE | NOT NULL |  | Indicates the parent case step for this case step. This field will be used to position this case step in the workflow. |
| 8 | `SAMPLE_TYPE_CD` | DOUBLE | NOT NULL |  | Indicates the type of sample that will be created and then processed by this case step. For the first case step in a workup, this value will always be 0. |
| 9 | `STEP_SEQUENCE_NBR` | DOUBLE | NOT NULL |  | The sequence of the case step in context of other case steps with the same parent. |
| 10 | `UCMR_CASE_STEP_ID` | DOUBLE | NOT NULL | PK | Unique Identifier for the case step. |
| 11 | `UCMR_CASE_TYPE_ID` | DOUBLE | NOT NULL | FK→ | This field indicates the case type to which this step is related. |
| 12 | `UCMR_CASE_WORKUP_ID` | DOUBLE | NOT NULL | FK→ | Indicates the specific workup for this case type that this case step is part of. |
| 13 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 14 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 15 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 16 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 17 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `UCMR_CASE_TYPE_ID` | [UCMR_CASE_TYPE](UCMR_CASE_TYPE.md) | `UCMR_CASE_TYPE_ID` |
| `UCMR_CASE_WORKUP_ID` | [UCMR_CASE_WORKUP](UCMR_CASE_WORKUP.md) | `UCMR_CASE_WORKUP_ID` |

## Referenced by (5)

| From table | Column |
|------------|--------|
| [UCMR_CASE_GRP_STEP_R](UCMR_CASE_GRP_STEP_R.md) | `UCMR_CASE_STEP_ID` |
| [UCMR_EQUIVALENT_STEP](UCMR_EQUIVALENT_STEP.md) | `UCMR_CASE_STEP_ID` |
| [UCMR_REQUIRED_STEP](UCMR_REQUIRED_STEP.md) | `REQUIRED_UCMR_CASE_STEP_ID` |
| [UCMR_REQUIRED_STEP](UCMR_REQUIRED_STEP.md) | `UCMR_CASE_STEP_ID` |
| [UCM_CASE_STEP](UCM_CASE_STEP.md) | `UCMR_CASE_STEP_ID` |

