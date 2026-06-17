# WHC_F_MOTHER_PREGNANCY

> WHC Reporting - Fact Table containing data related to the MOTHER and the PREGNANCY

**Description:** WHC_F_MOTHER_PREGNANCY  
**Table type:** ACTIVITY  
**Primary key:** _(not published — see note)_  
**Columns:** 34

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ABORH_DESC` | VARCHAR(255) |  |  | NOT IMPLEMENTED AT THIS TIME |
| 2 | `ADMIT_DATE_NBR` | DOUBLE | NOT NULL | FK→ | Foreign key to OMF_DATE, corresponding to ENCOUNTER.REG_DT_TM for the associated mother's encounter during which the delivery occurred. |
| 3 | `ADMIT_TIME_NBR` | DOUBLE | NOT NULL | FK→ | Foreign key to OMF_TIME, corresponding to ENCOUNTER.REG_DT_TM for the associated mother's encounter during which the delivery occurred. |
| 4 | `ANTEPARTUM_RISK_FACTORS_DESC` | VARCHAR(255) |  |  | User-readable description of 'Risk Factors' value, taken from the clinical result recorded against CKI CERNER!28CD17AC-F1BD-4AE3-A9F6-1282F19618AB for the associated pregnancy. |
| 5 | `BIRTH_PLAN_FEEDING_ID` | DOUBLE | NOT NULL | FK→ | Foreign key to WHC_D_INTAKE_TYPE.WHC_D_INTAKE_TYPE_ID, representing the planned intake type for the resultant child or children. |
| 6 | `DIAGNOSIS_GROUP_ID` | DOUBLE | NOT NULL | FK→ | Foreign key to WHC_D_DIAGNOSIS_GROUP.WHC_D_DIAGNOSIS_GROUP_ID, representing a combination of diagnoses recorded against the mother within the specific context of the associated pregnancy. |
| 7 | `DISCHARGE_DATE_NBR` | DOUBLE | NOT NULL | FK→ | Foreign key to OMF_DATE corresponding to ENCOUNTER.DISCH_DT_TM for the associated mother's last encounter within the pregnancy care episode. |
| 8 | `DISCHARGE_TIME_NBR` | DOUBLE | NOT NULL | FK→ | Foreign key to OMF_TIME corresponding to ENCOUNTER.DISCH_DT_TM for the associated mother's last encounter within the pregnancy care episode. |
| 9 | `ECTOPIC_PREG_HIST` | DOUBLE |  |  | Value corresponding to the clinical result recorded against CKI CERNER!ASYr9AEYvUr1YoQHCqIGfQ, where the result was recorded between the previous pregnancy closure date to the current pregnancy closure date for the pregnancy in context. |
| 10 | `ED_DATE_NBR` | DOUBLE |  | FK→ | Foreign key to OMF_DATE corresponding to the most recently entered value in PREGNANCY_ESTIMATE.EST_DELIVERY_DT_TM for the associated mother's pregnancy. |
| 11 | `EGA_NBR` | DOUBLE |  |  | Value of PREGNANCY_ESTIMATE.EST_GEST_AGE_DAYS for the associated pregnancy, representing the gestational age at birth for the last child delivered within the pregnancy for the mother. |
| 12 | `GRAVIDA_NBR` | DOUBLE |  |  | Value corresponding to the clinical result value recorded against CKI CERNER!AEO/PQD7LLZ5Xf6zn4waeg, where the result was recorded between the previous pregnancy closure date to the current pregnancy closure date for the pregnancy in context. |
| 13 | `INDUCED_ABORT_PREG_HIST` | DOUBLE |  |  | Value corresponding to the clinical result recorded against CKI CERNER!ASYr9AEYvUr1YoQlCqIGfQ, where the result was recorded between the previous pregnancy closure date to the current pregnancy closure date for the pregnancy in context. |
| 14 | `MILL_PREGNANCY_ID` | DOUBLE | NOT NULL |  | Foreign key to PREGNANCY_INSTANCE.PREGNANCY_ID, representing the corresponding pregnancy in Millennium. |
| 15 | `MOTHER_ID` | DOUBLE | NOT NULL | FK→ | Foreign key to WHC_D_PERSON.WHC_D_PERSON_ID for the mother associated to the pregnancy in context. |
| 16 | `MULTIPLE_BIRTHS` | DOUBLE |  |  | Value corresponding to the clinical result recorded against CKI CERNER!C33FE830-5C65-4528-83F4-B32CB3C981BC, where the result was recorded between the previous pregnancy closure date to the current pregnancy closure date for the pregnancy in context |
| 17 | `ORGANIZATION_ID` | DOUBLE | NOT NULL | FK→ | Foreign key to WHC_F_ORGANIZATION.WHC_D_ORGANIZATION_ID, for the organization responsible for the mother's care during the pregnancy. |
| 18 | `PARA_ABORT_NBR` | DOUBLE |  |  | Value corresponding to the clinical result recorded against CKI CERNER!AVdLiAEMseBG5YD5CqIGfQ, where the result was recorded between the previous pregnancy closure date to the current pregnancy closure date for the pregnancy in context. |
| 19 | `PARA_LIVING_NBR` | DOUBLE |  |  | Value corresponding to the clinical result recorded against CKI CERNER!ASYr9AEYvUr1YofDCqIGfQ, where the result was recorded between the previous pregnancy closure date to the current pregnancy closure date for the pregnancy in context. |
| 20 | `PARA_NBR` | DOUBLE |  |  | Value corresponding to the clinical result recorded against CKI CERNER!AEO/PQD7LLZ5Xf67n4waeg, where the result was recorded between the previous pregnancy closure date to the current pregnancy closure date for the pregnancy in context. |
| 21 | `PARA_PRETERM_NBR` | DOUBLE |  |  | Value corresponding to the clinical result recorded against CKI CERNER!AVdLiAEMseBG5YDtCqIGfQ, where the result was recorded between the previous pregnancy closure date to the current pregnancy closure date for the pregnancy in context. |
| 22 | `PARA_TERM_NBR` | DOUBLE |  |  | Value corresponding to the clinical result recorded against CKI CERNER!AVdLiAEMseBG5YDhCqIGfQ, where the result was recorded between the previous pregnancy closure date to the current pregnancy closure date for the pregnancy in context. |
| 23 | `PREGNANCY_CLOSE_DATE_NBR` | DOUBLE |  | FK→ | Foreign key to OMF_date corresponding to PROBLEM.LIFE_CYCLE_DT_TM (in case populated for history pregnancy)/PREGNANCY_INSTANCE.PREG_END_DT_TM for the associated pregnancy representing Pregnancy Close Date. |
| 24 | `PREGNANCY_CLOSE_TIME_NBR` | DOUBLE |  | FK→ | Foreign key to OMF_time corresponding to PROBLEM.LIFE_CYCLE_DT_TM (in case populated for history pregnancy)/PREGNANCY_INSTANCE.PREG_END_DT_TM for the associated pregnancy representing Pregnancy Close Time. |
| 25 | `PREGNANCY_ONSET_DATE_NBR` | DOUBLE |  | FK→ | Foreign key to OMF_date corresponding to PROBLEM.ONSET_DT_TM (in case populated)/PREGNANCY_INSTANCE.PREG_START_DT_TM for the associated pregnancy representing Pregnancy Onset Date. |
| 26 | `PREGNANCY_ONSET_TIME_NBR` | DOUBLE |  | FK→ | Foreign key to OMF_time corresponding to PROBLEM.ONSET_DT_TM (in case populated)/PREGNANCY_INSTANCE.PREG_START_DT_TM for the associated pregnancy representing Pregnancy Onset Time. |
| 27 | `SPONTANEOUS_ABORT_PREG_HX` | DOUBLE |  |  | Value corresponding to the clinical result recorded against CKI CERNER!ASYr9AEYvUr1YoQWCqIGfQ, where the result was recorded between the previous pregnancy closure date to the current pregnancy closure date for the pregnancy in context. |
| 28 | `TRANSACTION_PROFILE_ID` | DOUBLE | NOT NULL | FK→ | Foreign key to WHC_D_TRANSACTION_PROFILE.WHC_D_TRANSACTION_PROFILE_ID. |
| 29 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 30 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 31 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 32 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 33 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 34 | `WHC_F_MOTHER_PREGNANCY_ID` | DOUBLE | NOT NULL |  | Primary Key |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `ADMIT_DATE_NBR` | [OMF_DATE](OMF_DATE.md) | `DT_NBR` |
| `ADMIT_TIME_NBR` | [OMF_TIME](OMF_TIME.md) | `MIN_NBR` |
| `BIRTH_PLAN_FEEDING_ID` | [WHC_D_INTAKE_TYPE](WHC_D_INTAKE_TYPE.md) | `WHC_D_INTAKE_TYPE_ID` |
| `DIAGNOSIS_GROUP_ID` | [WHC_D_DIAGNOSIS_GROUP](WHC_D_DIAGNOSIS_GROUP.md) | `WHC_D_DIAGNOSIS_GROUP_ID` |
| `DISCHARGE_DATE_NBR` | [OMF_DATE](OMF_DATE.md) | `DT_NBR` |
| `DISCHARGE_TIME_NBR` | [OMF_TIME](OMF_TIME.md) | `MIN_NBR` |
| `ED_DATE_NBR` | [OMF_DATE](OMF_DATE.md) | `DT_NBR` |
| `MOTHER_ID` | [WHC_D_PERSON](WHC_D_PERSON.md) | `WHC_D_PERSON_ID` |
| `ORGANIZATION_ID` | [WHC_D_ORGANIZATION](WHC_D_ORGANIZATION.md) | `WHC_D_ORGANIZATION_ID` |
| `PREGNANCY_CLOSE_DATE_NBR` | [OMF_DATE](OMF_DATE.md) | `DT_NBR` |
| `PREGNANCY_CLOSE_TIME_NBR` | [OMF_TIME](OMF_TIME.md) | `MIN_NBR` |
| `PREGNANCY_ONSET_DATE_NBR` | [OMF_DATE](OMF_DATE.md) | `DT_NBR` |
| `PREGNANCY_ONSET_TIME_NBR` | [OMF_TIME](OMF_TIME.md) | `MIN_NBR` |
| `TRANSACTION_PROFILE_ID` | [WHC_D_TRANSACTION_PROFILE](WHC_D_TRANSACTION_PROFILE.md) | `WHC_D_TRANSACTION_PROFILE_ID` |

