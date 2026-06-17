# BB_QC_RESULT

> This table contains the outcomes for a specific Blood Bank QC reagent result.

**Description:** Blood Bank Quality Control Result  
**Table type:** ACTIVITY  
**Primary key:** `QC_RESULT_ID`  
**Columns:** 23  
**Referenced by:** 1 columns

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ABNORMAL_IND` | DOUBLE | NOT NULL |  | This field indicates if the result is abnormal or not an expected result. |
| 2 | `ACTION_DT_TM` | DATETIME |  |  | The date and time that the QC result status is changed without verifying the result. |
| 3 | `ACTION_PRSNL_ID` | DOUBLE | NOT NULL | FK→ | The ID of the person that changed the QC result status without verifying the result. |
| 4 | `COMMENT_TEXT_ID` | DOUBLE | NOT NULL | FK→ | This field contains the unique identifier of the comment associated with the result (LONG_TEXT) |
| 5 | `CONTROL_ACTIVITY_ID` | DOUBLE | NOT NULL | FK→ | This field links the result row with a specific Group Reagent Activity |
| 6 | `ENHANCEMENT_ACTIVITY_ID` | DOUBLE | NOT NULL | FK→ | This filed links the result row with a specific enhancement Group Reagent Activity |
| 7 | `GROUP_REAGENT_ACTIVITY_ID` | DOUBLE | NOT NULL | FK→ | This field links the QC result with a specific reagent activity row. |
| 8 | `NOMENCLATURE_ID` | DOUBLE | NOT NULL | FK→ | This field links the result row with a specific row on the nomenclature table. |
| 9 | `PHASE_CD` | DOUBLE | NOT NULL |  | This field contains the unique identifier of the phase used for the QC testing. |
| 10 | `PRIMARY_REVIEW_DT_TM` | DATETIME | NOT NULL |  | This field contains the date and time the result was reviewed by the primary user. |
| 11 | `PRIMARY_REVIEW_PRSNL_ID` | DOUBLE | NOT NULL | FK→ | This field contains the identifier of the primary reviewer. |
| 12 | `QC_RESULT_ID` | DOUBLE | NOT NULL | PK | quality control result identifier |
| 13 | `REASON_CD` | DOUBLE | NOT NULL |  | This field contains the unique identifier of the selected reason when a QC result is accepted, retested, or discarded. (CS:325576) |
| 14 | `RESULT_DT_TM` | DATETIME | NOT NULL |  | Contains the date and time the result was recorded. |
| 15 | `RESULT_PRSNL_ID` | DOUBLE | NOT NULL | FK→ | This field contains the unique identifier of the personnel that recorded the result |
| 16 | `SECONDARY_REVIEW_DT_TM` | DATETIME | NOT NULL |  | This field contains the date and time the result was reviewed by the secondary user. |
| 17 | `SECONDARY_REVIEW_PRSNL_ID` | DOUBLE | NOT NULL | FK→ | This field contains the identifier of the secondary reviewer. |
| 18 | `STATUS_CD` | DOUBLE | NOT NULL |  | This field contains the unique identifier of the current result status. |
| 19 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 20 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 21 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 22 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 23 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `ACTION_PRSNL_ID` | [PRSNL](PRSNL.md) | `PERSON_ID` |
| `COMMENT_TEXT_ID` | [LONG_TEXT](LONG_TEXT.md) | `LONG_TEXT_ID` |
| `CONTROL_ACTIVITY_ID` | [BB_QC_GRP_REAGENT_ACTIVITY](BB_QC_GRP_REAGENT_ACTIVITY.md) | `GROUP_REAGENT_ACTIVITY_ID` |
| `ENHANCEMENT_ACTIVITY_ID` | [BB_QC_GRP_REAGENT_ACTIVITY](BB_QC_GRP_REAGENT_ACTIVITY.md) | `GROUP_REAGENT_ACTIVITY_ID` |
| `GROUP_REAGENT_ACTIVITY_ID` | [BB_QC_GRP_REAGENT_ACTIVITY](BB_QC_GRP_REAGENT_ACTIVITY.md) | `GROUP_REAGENT_ACTIVITY_ID` |
| `NOMENCLATURE_ID` | [NOMENCLATURE](NOMENCLATURE.md) | `NOMENCLATURE_ID` |
| `PRIMARY_REVIEW_PRSNL_ID` | [PRSNL](PRSNL.md) | `PERSON_ID` |
| `RESULT_PRSNL_ID` | [PRSNL](PRSNL.md) | `PERSON_ID` |
| `SECONDARY_REVIEW_PRSNL_ID` | [PRSNL](PRSNL.md) | `PERSON_ID` |

## Referenced by (1)

| From table | Column |
|------------|--------|
| [BB_QC_RESULT_TROUBLESHOOTING_R](BB_QC_RESULT_TROUBLESHOOTING_R.md) | `QC_RESULT_ID` |

