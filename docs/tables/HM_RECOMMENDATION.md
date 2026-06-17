# HM_RECOMMENDATION

> Maintains a record of specific recommendations that are being made by the Health Expectation subsystem.

**Description:** Health Maintenance Recommendations  
**Table type:** ACTIVITY  
**Primary key:** `RECOMMENDATION_ID`  
**Columns:** 31  
**Referenced by:** 2 columns

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ASSIGNED_BY_PRSNL_ID` | DOUBLE | NOT NULL | FK→ | The person who assigned the expectation to the patient. Zero means the expectation was assigned by the system. |
| 2 | `DUE_DT_TM` | DATETIME |  |  | the date the recommendation is due |
| 3 | `DUE_OVERRIDE_ACTION_ID` | DOUBLE | NOT NULL |  | Indicates the due date has been overridden. If this field is valued then it will reference the HM_RECOMMENDATION_ACTION row that represents the override. |
| 4 | `EXPECTATION_FTDESC` | VARCHAR(255) |  |  | A free text description of the expectation associated with this recommendation |
| 5 | `EXPECTATION_NAME_CD` | DOUBLE | NOT NULL |  | the code value of the overridden expectation name |
| 6 | `EXPECT_ID` | DOUBLE | NOT NULL | FK→ | Expectation ID from HM_EXPECT |
| 7 | `EXPIRE_DT_TM` | DATETIME |  |  | The date when the recommendation should no longer qualify for the person. |
| 8 | `FIRST_DUE_DT_TM` | DATETIME |  |  | the first date the recommendation was due |
| 9 | `FREQUENCY_OVERRIDE_ACTION_ID` | DOUBLE | NOT NULL |  | Indicates the frequency has been overridden. If this field is valued then it will reference the HM_RECOMMENDATION_ACTION row that represents the override. |
| 10 | `FREQUENCY_UNIT_CD` | DOUBLE | NOT NULL |  | The unit that is associated with the frequency. |
| 11 | `FREQUENCY_VAL` | DOUBLE | NOT NULL |  | The frequency between when this person should be recommended for this expectation. |
| 12 | `LAST_SATISFACTION_DT_TM` | DATETIME |  |  | The date and time that this recommendation was last satisfied. |
| 13 | `LAST_SATISFACTION_ID` | DOUBLE | NOT NULL |  | The actual id of the activity data that last "satisfied" the recommendation. The source of this value is shown in satisfaction_source field. |
| 14 | `LAST_SATISFACTION_SOURCE` | VARCHAR(30) | NOT NULL |  | Source of the value of the last_satisfaction_id |
| 15 | `LAST_SATISFIED_BY_ID` | DOUBLE | NOT NULL | FK→ | The person who last satisfied this recommendation. |
| 16 | `NEAR_DUE_DT_TM` | DATETIME |  |  | The date and time this recommendation becomes near due. |
| 17 | `OVERDUE_DT_TM` | DATETIME |  |  | The date and time this recommendation becomes overdue |
| 18 | `PERSON_ID` | DOUBLE | NOT NULL | FK→ | Patient Person_id |
| 19 | `QUALIFIED_DT_TM` | DATETIME | NOT NULL |  | The date and time on which the person qualified for the recommendation. |
| 20 | `RECOMMENDATION_ID` | DOUBLE | NOT NULL | PK | Primary Key |
| 21 | `STATUS_FLAG` | DOUBLE | NOT NULL |  | status of the recommendation |
| 22 | `STEP_ID` | DOUBLE | NOT NULL | FK→ | Expect Step ID from HM_EXPECT_STEP |
| 23 | `SYSTEM_FREQ_OVERRIDE_ACTION_ID` | DOUBLE | NOT NULL |  | indicates the system frequency has been overridden. if this field is valued then it will reference the hm_recommendation_action row that represents the override. |
| 24 | `SYSTEM_FREQ_UNIT_CD` | DOUBLE | NOT NULL |  | the unit that is associated with the system frequency. |
| 25 | `SYSTEM_FREQ_VAL` | DOUBLE | NOT NULL |  | the system frequency between when this person should be recommended for this expectation. |
| 26 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 27 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 28 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 29 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 30 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |
| 31 | `VERIFICATION_VERSION_NBR` | DOUBLE | NOT NULL |  | Help with complex verification logic to ensure that the state of the recommendation is correct based on all of the history. Server that will check the table against the latest version of the verification logic, if any row isn't up to date, it will be processed. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `ASSIGNED_BY_PRSNL_ID` | [PRSNL](PRSNL.md) | `PERSON_ID` |
| `EXPECT_ID` | [HM_EXPECT](HM_EXPECT.md) | `EXPECT_ID` |
| `LAST_SATISFIED_BY_ID` | [PRSNL](PRSNL.md) | `PERSON_ID` |
| `PERSON_ID` | [PERSON](PERSON.md) | `PERSON_ID` |
| `STEP_ID` | [HM_EXPECT_STEP](HM_EXPECT_STEP.md) | `EXPECT_STEP_ID` |

## Referenced by (2)

| From table | Column |
|------------|--------|
| [HM_RECOMMENDATION_ACTION](HM_RECOMMENDATION_ACTION.md) | `RECOMMENDATION_ID` |
| [HM_RECOMMENDATION_EXT](HM_RECOMMENDATION_EXT.md) | `RECOMMENDATION_ID` |

