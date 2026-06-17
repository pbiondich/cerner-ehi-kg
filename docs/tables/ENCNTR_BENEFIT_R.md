# ENCNTR_BENEFIT_R

> This table contains specific encounter benefit-type information. We will allow encounter benefit information to be captured for each health plan.

**Description:** Encounter Benefit Relationship table  
**Table type:** ACTIVITY  
**Primary key:** `ENCNTR_BENEFIT_R_ID`  
**Columns:** 36  
**Referenced by:** 1 columns

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ACTIVE_IND` | DOUBLE |  |  | The table row is active or inactive. A row is generally active unless it is in an inactive state such as logically deleted, combined away, pending purge, etc. |
| 2 | `ACTIVE_STATUS_CD` | DOUBLE | NOT NULL |  | Indicates the status of the row itself (not the data in the row) such as active, inactive, combined away, pending purge, etc. |
| 3 | `ACTIVE_STATUS_DT_TM` | DATETIME |  |  | The date and time that the active_status_cd was set. |
| 4 | `ACTIVE_STATUS_PRSNL_ID` | DOUBLE | NOT NULL |  | The person who caused the active_status_cd to be set or change. |
| 5 | `BEG_EFFECTIVE_DT_TM` | DATETIME | NOT NULL |  | The date and time for which this table row becomes effective. Normally, this will be the date and time the row is added, but could be a past or future date and time. |
| 6 | `BENEFIT_PLAN_CD` | DOUBLE | NOT NULL |  | Used to specify the level of benefit information being captured. |
| 7 | `COINSURANCE_DAYS` | DOUBLE | NOT NULL |  | Hospital days for which the subscriber is responsible for paying, according to a fixed percentage or amount. For example, for skilled nursing facility (SNF) benefits. |
| 8 | `COINSURANCE_PCT` | DOUBLE | NOT NULL |  | The percentage that the covered person is responsible for paying after payment of the deductible. |
| 9 | `COINSURANCE_REMAIN_DAYS` | DOUBLE | NOT NULL |  | The number of hospital days remaining for which the covered person is responsible for paying, according to a fixed percentage or amount. |
| 10 | `COMMENT_ID` | DOUBLE | NOT NULL | FK→ | Encntr_benefit_reltn comment identifier. |
| 11 | `COPAY_AMT` | DOUBLE | NOT NULL |  | The portion of a claim or medical expense that a member must pay out of pocket, such as $10 in many HMOs. |
| 12 | `COVERAGE_DAYS` | DOUBLE | NOT NULL |  | Hospital days that are covered under the subscriber's policy. |
| 13 | `COVERAGE_REMAIN_DAYS` | DOUBLE | NOT NULL |  | The remaining hospital days that are covered under the subscriber's policy. |
| 14 | `DATA_STATUS_CD` | DOUBLE | NOT NULL |  | Data status indicates a level of authenticity of the row data. Typically this will either be AUTHENTICATED or UNAUTHENTICATED. |
| 15 | `DATA_STATUS_DT_TM` | DATETIME |  |  | The date and time that the data_status_cd was set. |
| 16 | `DATA_STATUS_PRSNL_ID` | DOUBLE | NOT NULL |  | The person who caused the data_status_cd to be set or change. |
| 17 | `DEDUCT_AMT` | DOUBLE | NOT NULL |  | The amount of deductible for this benefit. |
| 18 | `DEDUCT_MET_AMT` | DOUBLE | NOT NULL |  | The amount insurer paid toward deductible. |
| 19 | `DEDUCT_MET_DT_TM` | DATETIME |  |  | The date and time the deductible was met. |
| 20 | `DEDUCT_PCT` | DOUBLE | NOT NULL |  | The percentage that must be met by the patient before the insurer will begin covering the cost of care. |
| 21 | `DEDUCT_REMAIN_AMT` | DOUBLE | NOT NULL |  | The amount of deductible remaining to be met by the patient before the insurer will begin covering the cost of care. Will be a static, manual-entry field for this project, with plans to discuss ways to automatically decrement in the future. |
| 22 | `ENCNTR_BENEFIT_R_ID` | DOUBLE | NOT NULL | PK | Primary Key |
| 23 | `ENCNTR_PLAN_RELTN_ID` | DOUBLE | NOT NULL | FK→ | This is the value of the unique primary identifier of the encounter health plan relationship table. |
| 24 | `END_EFFECTIVE_DT_TM` | DATETIME | NOT NULL |  | The date/time after which the row is no longer valid as active current data. This may be valued with the date that the row became inactive. |
| 25 | `INTERNAL_SEQ` | DOUBLE | NOT NULL |  | A numeric number used to represent the order in which to consider benefit information if the encounter has more than one set of benefits. |
| 26 | `NON_COVERAGE_DAYS` | DOUBLE | NOT NULL |  | Hospital days that are not covered under the subscriber's policy. |
| 27 | `ROOM_COVERAGE_AMT` | DOUBLE | NOT NULL |  | The amount allowed (covered by the insurer) for room charges, which varies based on the room type. |
| 28 | `ROOM_COVERAGE_AMT_QUAL_CD` | DOUBLE | NOT NULL |  | Designates the units entered in room coverage amount. |
| 29 | `ROOM_COVERAGE_BOARD_INCL_CD` | DOUBLE | NOT NULL |  | A y/n field indicating if room and board charges are included in the room coverage amount established by the insurer for the specific room type. |
| 30 | `ROOM_COVERAGE_TYPE_CD` | DOUBLE | NOT NULL |  | The room type specifically associated with the room coverage amount covered by the insurer. |
| 31 | `SERVICE_TYPE_CD` | DOUBLE | NOT NULL |  | Used to specify the level of benefit information being captured. |
| 32 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 33 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 34 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 35 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 36 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `COMMENT_ID` | [LONG_TEXT](LONG_TEXT.md) | `LONG_TEXT_ID` |
| `ENCNTR_PLAN_RELTN_ID` | [ENCNTR_PLAN_RELTN](ENCNTR_PLAN_RELTN.md) | `ENCNTR_PLAN_RELTN_ID` |

## Referenced by (1)

| From table | Column |
|------------|--------|
| [ENCNTR_BENEFIT_SCH_R](ENCNTR_BENEFIT_SCH_R.md) | `ENCNTR_BENEFIT_R_ID` |

