# HM_RECOMMENDATION_ACTION

> Maintains a record of each action taken against specific recommendations that are being mde by the Health Expectation subsystem.

**Description:** Health Maintenance Recommendation Actions  
**Table type:** ACTIVITY  
**Primary key:** `RECOMMENDATION_ACTION_ID`  
**Columns:** 40  
**Referenced by:** 3 columns

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ACTION_DT_TM` | DATETIME |  |  | Date of action |
| 2 | `ACTION_FLAG` | DOUBLE | NOT NULL |  | action taken against the recommendation: 0 No value / Null, 1 Created, 2 Postponed, 3 Expired, 4 Refused, 5 Cancelled, 6 Satisfied, 7 Change Frequency, 8 Change Due Date, 9 Change Qualification Interval, 10 Undo Refusal, 11 Undo Cancellation, 12 Undo Satisfaction, 13 Undo Postpone, 14 Qualified, 15 System Cancelled, 16 Assigned, 17 Satisfaction Expiration, 18 System Change Frequency, 19 System Change Name, 20 Unassigned, 21 Healthe Measure Update, 22 Healthe Measure Cancel, 23 Snooze, 24 Undo |
| 3 | `COPY_TO_ACTION_ID` | DOUBLE | NOT NULL | FK→ | The identifier of the recommendation action that this id has been copied to. |
| 4 | `DEPENDENT_SATISFACTION_ID` | DOUBLE | NOT NULL |  | Stores the actual ID of the Activity data that this event depends upon to satisfy the expectation |
| 5 | `DEPENDENT_SATISFACTION_SOURCE` | VARCHAR(30) |  |  | Source of the value for DEPENDENT_SATISFACTION_ID ( i.e., ORDERS ) |
| 6 | `DUE_DT_TM` | DATETIME |  |  | The new date and time that this recommendation will be due. |
| 7 | `ENCNTR_ID` | DOUBLE |  | FK→ | Encounter at which recommendation action was taken |
| 8 | `EXPECTATION_FTDESC` | VARCHAR(255) |  |  | A free text description of the expectation associated with this recommendation |
| 9 | `EXPECTATION_NAME_CD` | DOUBLE | NOT NULL |  | The code value of the overridden expectation name |
| 10 | `EXPECT_MOD_ID` | DOUBLE | NOT NULL | FK→ | Foreign Key value from the HM_EXPECT_MOD table. |
| 11 | `EXPECT_SAT_ID` | DOUBLE | NOT NULL | FK→ | Foreign Key value from the HM_EXPECT_SAT_TABLE |
| 12 | `EXPIRE_DT_TM` | DATETIME |  |  | The date and time when the person will no longer qualify for the recommendation |
| 13 | `FREQUENCY_OVERRIDE_ACTION_ID` | DOUBLE | NOT NULL |  | ** OBSOLETE** - This column will no longer be used when schema changes associated with DevTest feature 164316 are promoted / implemented (Nov. 2008).Indicates the frequency has been overridden. If this field is valued then it will reference the HM_RECOMMENDATION_ACTION row that represents the override. |
| 14 | `FREQUENCY_UNIT_CD` | DOUBLE | NOT NULL |  | The unit that is associated with the frequency. |
| 15 | `FREQUENCY_VAL` | DOUBLE | NOT NULL |  | The frequency between when this person should be recommended for this expectation. |
| 16 | `LONG_TEXT_ID` | DOUBLE | NOT NULL | FK→ | a comment associated with the action. This is the ID of the long text row in the LONG_TEXT table. |
| 17 | `ON_BEHALF_OF_PRSNL_ID` | DOUBLE | NOT NULL | FK→ | the person who authorized the action. |
| 18 | `OVERRIDE_IND` | DOUBLE | NOT NULL |  | Indicates the action was performed explicitly by a clinician to force a change. Changes caused by overrides will supersede any system triggered changes. |
| 19 | `PREV_DUE_DT_TM` | DATETIME |  |  | The due date and time before this action was performed |
| 20 | `PREV_EXPECTATION_NAME_CD` | DOUBLE | NOT NULL |  | the code value of the PREVIOUS overridden expectation name |
| 21 | `PREV_EXPIRE_DT_TM` | DATETIME |  |  | The expire date and time before this action was performed |
| 22 | `PREV_FREQUENCY_UNIT_CD` | DOUBLE | NOT NULL |  | The frequency unit code before this action was performed |
| 23 | `PREV_FREQUENCY_VAL` | DOUBLE |  |  | The frequency value before this action was performed |
| 24 | `PREV_QUALIFIED_DT_TM` | DATETIME |  |  | The qualified date and time before this action was performed |
| 25 | `QUALIFIED_DT_TM` | DATETIME |  |  | The date and time when the person qualified for the recommendation |
| 26 | `QUALIFY_AGE` | DOUBLE | NOT NULL |  | The age at which the person should now qualify for the expectation. |
| 27 | `QUALIFY_AGE_UNIT_CD` | DOUBLE | NOT NULL |  | The unit that is associated with the qualify age. |
| 28 | `REASON_CD` | DOUBLE | NOT NULL |  | the reason for the action (codesets 30440, 30441, 30442, 30443) |
| 29 | `RECOMMENDATION_ACTION_ID` | DOUBLE | NOT NULL | PK | Primary Key |
| 30 | `RECOMMENDATION_ID` | DOUBLE | NOT NULL | FK→ | Foreign Key value from the HM_RECOMMENDATION table. |
| 31 | `RECORD_NUMBER` | DOUBLE | NOT NULL |  | ** OBSOLETE** - This column will no longer be used when schema changes associated with DevTest feature 164316 are promoted / implemented (November 2008)Used to group records together |
| 32 | `RELATED_ACTION_ID` | DOUBLE | NOT NULL | FK→ | Foreign Key value from the HM_RECOMMENDATION_ACTION table. If the action flag is an undo action, then this is the action it undid. If the action flag is anything else, then this is the action_id of the undo action. |
| 33 | `SATISFACTION_DT_TM` | DATETIME |  |  | The date and time when the satisfaction occurred for the recommendation |
| 34 | `SATISFACTION_ID` | DOUBLE | NOT NULL |  | stores the actual id of the activity data that "satisfied" the exception. Source of value is shown in SATISFACTION_SOURCE field. |
| 35 | `SATISFACTION_SOURCE` | VARCHAR(30) | NOT NULL |  | Source of the value for SATISFACTION_ID |
| 36 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 37 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 38 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 39 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 40 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `COPY_TO_ACTION_ID` | [HM_RECOMMENDATION_ACTION](HM_RECOMMENDATION_ACTION.md) | `RECOMMENDATION_ACTION_ID` |
| `ENCNTR_ID` | [ENCOUNTER](ENCOUNTER.md) | `ENCNTR_ID` |
| `EXPECT_MOD_ID` | [HM_EXPECT_MOD](HM_EXPECT_MOD.md) | `EXPECT_MOD_ID` |
| `EXPECT_SAT_ID` | [HM_EXPECT_SAT](HM_EXPECT_SAT.md) | `EXPECT_SAT_ID` |
| `LONG_TEXT_ID` | [LONG_TEXT](LONG_TEXT.md) | `LONG_TEXT_ID` |
| `ON_BEHALF_OF_PRSNL_ID` | [PRSNL](PRSNL.md) | `PERSON_ID` |
| `RECOMMENDATION_ID` | [HM_RECOMMENDATION](HM_RECOMMENDATION.md) | `RECOMMENDATION_ID` |
| `RELATED_ACTION_ID` | [HM_RECOMMENDATION_ACTION](HM_RECOMMENDATION_ACTION.md) | `RECOMMENDATION_ACTION_ID` |

## Referenced by (3)

| From table | Column |
|------------|--------|
| [HM_EXPECT_MOD_HIST](HM_EXPECT_MOD_HIST.md) | `RECOMMENDATION_ACTION_ID` |
| [HM_RECOMMENDATION_ACTION](HM_RECOMMENDATION_ACTION.md) | `COPY_TO_ACTION_ID` |
| [HM_RECOMMENDATION_ACTION](HM_RECOMMENDATION_ACTION.md) | `RELATED_ACTION_ID` |

