# PT_PROT_REG

> This table contains information about the registration of a patient on a protocol

**Description:** This table contains information about registration of a patient on a protocol  
**Table type:** ACTIVITY  
**Primary key:** `PT_PROT_REG_ID`  
**Columns:** 38  
**Referenced by:** 3 columns

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `BEG_EFFECTIVE_DT_TM` | DATETIME | NOT NULL |  | The date and time for which this table row becomes effective. Normally, this will be the date and time the row is added, but could be a past or future date and time. |
| 2 | `BEST_RESPONSE_CD` | DOUBLE | NOT NULL |  | This field contains the code that identifies the best response that the patient obtained while enrolled on the protocol. |
| 3 | `DIAGNOSIS_TYPE_CD` | DOUBLE | NOT NULL |  | This field contains the code identifying the diagnosis type for which the patient was enrolled in the protocol. |
| 4 | `END_EFFECTIVE_DT_TM` | DATETIME | NOT NULL |  | The date/time after which the row is no longer valid as active current data. This may be valued with the date that the row became inactive. |
| 5 | `ENROLLING_ORGANIZATION_ID` | DOUBLE | NOT NULL | FK→ | This field uniquely identifies a row in the organization table. This field identifies the institution that enrolled the patient in the protocol. |
| 6 | `EPISODE_ID` | DOUBLE | NOT NULL | FK→ | This is the value of the unique primary identifier of the episode table. It is an internal system assigned number. This episode is related to the enrollment. |
| 7 | `FIRST_CR_DT_TM` | DATETIME |  |  | This field contains the date and time on which the first complete remission occurred. |
| 8 | `FIRST_DIS_REL_EVENT_DEATH_CD` | DOUBLE | NOT NULL |  | This field contains the code indicating the first disease related event such as progression, relapse or second malignancy or death if death was the first disease related event to occur. |
| 9 | `FIRST_PD_DT_TM` | DATETIME |  |  | This field contains the date and time on which the first disease progression/relapse occurred. |
| 10 | `FIRST_PD_FAILURE_DT_TM` | DATETIME |  |  | This field contains the date and time of the first disease progression or relapse that occurred while the patient was on study. This field will be automatically updated when the relapse/progression is recorded in the patient protocol data. |
| 11 | `NOMENCLATURE_ID` | DOUBLE | NOT NULL | FK→ | This field uniquely identifies a row in the nomenclature table. This field identifies the diagnosis for which the patient was enrolled in the protocol. |
| 12 | `OFF_STUDY_DT_TM` | DATETIME |  |  | This field contains the date and time on which the patient was taken off study. If a patient dies on study, the date off study will be the patient's date of death. If a patient fails on study and is enrolled in a subsequent study, the date off study will be the date of enrollment on the subsequent study. |
| 13 | `OFF_TX_REMOVAL_ORGANIZATION_ID` | DOUBLE | NOT NULL | FK→ | Organization removing patient off treatment. |
| 14 | `OFF_TX_REMOVAL_PERSON_ID` | DOUBLE | NOT NULL | FK→ | Person removing patient off treatment.study. |
| 15 | `ON_STUDY_DT_TM` | DATETIME | NOT NULL |  | This field contains the date and time on which the patient was enrolled on the study. Often, this is the date the patient's consent form was signed. |
| 16 | `ON_TX_ASSIGN_PRSNL_ID` | DOUBLE | NOT NULL | FK→ | Assigning person when patent is on treatment |
| 17 | `ON_TX_COMMENT` | VARCHAR(255) | NOT NULL |  | Comments to be added when patent is on treatment |
| 18 | `ON_TX_ORGANIZATION_ID` | DOUBLE | NOT NULL | FK→ | Assigning institute when patent is on treatment |
| 19 | `PERSON_ID` | DOUBLE | NOT NULL | FK→ | This is the value of the unique primary identifier of the person table. It is an internal system assigned number. |
| 20 | `PROT_ACCESSION_NBR` | VARCHAR(255) | NOT NULL |  | This field contains the patient's accession number (order of enrollment) for this protocol. |
| 21 | `PROT_ARM_ID` | DOUBLE | NOT NULL | FK→ | This field uniquely identifies a row in the prot_arm table. This field identifies the protocol arm in which the patient was enrolled. |
| 22 | `PROT_MASTER_ID` | DOUBLE | NOT NULL | FK→ | Uniquelu identifies a row in prot_master table. This field identifies the protocol on which the patient is enrolled. |
| 23 | `PT_PROT_REG_ID` | DOUBLE | NOT NULL | PK | Primary key of the pt_prot_reg table. It is a system assigned number. |
| 24 | `REASON_OFF_TX_CD` | DOUBLE | NOT NULL |  | Reason Off Treatment |
| 25 | `REASON_OFF_TX_DESC` | VARCHAR(255) |  |  | Textual reason patient is taken off treatment. |
| 26 | `REG_ID` | DOUBLE | NOT NULL |  | A unique key for the registation of a patient on a protocol. No two active rows can have the same reg_id |
| 27 | `REMOVAL_ORGANIZATION_ID` | DOUBLE | NOT NULL | FK→ | This field uniquely identifies a row in the organization table. This field identifies the institution/organization with which the person who removed the patient from the protocol was associated. For this purpose, an institution can be another hospital, research institute, drug company, government agency, etc. |
| 28 | `REMOVAL_PERSON_ID` | DOUBLE | NOT NULL | FK→ | This field uniquely identifies a row in the person table. This field identifies the individual who removed the patient from the protocol. |
| 29 | `REMOVAL_REASON_CD` | DOUBLE | NOT NULL |  | Codified reason patient is taken off study. |
| 30 | `REMOVAL_REASON_DESC` | VARCHAR(255) |  |  | Textual reason patient is taken off study. |
| 31 | `STATUS_ENUM` | DOUBLE | NOT NULL |  | Number to indicate the current status of the enrolled patient(1: On Study,2:OnTreatment, 3:Off Treatment,4-OnFollowup,5-OffStudy) |
| 32 | `TX_COMPLETION_DT_TM` | DATETIME |  |  | This field contains the date and time on which treatment was completed. |
| 33 | `TX_START_DT_TM` | DATETIME |  |  | This field contains the date and time on which treatment commenced. |
| 34 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 35 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 36 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 37 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 38 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `ENROLLING_ORGANIZATION_ID` | [ORGANIZATION](ORGANIZATION.md) | `ORGANIZATION_ID` |
| `EPISODE_ID` | [EPISODE](EPISODE.md) | `EPISODE_ID` |
| `NOMENCLATURE_ID` | [NOMENCLATURE](NOMENCLATURE.md) | `NOMENCLATURE_ID` |
| `OFF_TX_REMOVAL_ORGANIZATION_ID` | [ORGANIZATION](ORGANIZATION.md) | `ORGANIZATION_ID` |
| `OFF_TX_REMOVAL_PERSON_ID` | [PRSNL](PRSNL.md) | `PERSON_ID` |
| `ON_TX_ASSIGN_PRSNL_ID` | [PRSNL](PRSNL.md) | `PERSON_ID` |
| `ON_TX_ORGANIZATION_ID` | [ORGANIZATION](ORGANIZATION.md) | `ORGANIZATION_ID` |
| `PERSON_ID` | [PERSON](PERSON.md) | `PERSON_ID` |
| `PROT_ARM_ID` | [PROT_ARM](PROT_ARM.md) | `PROT_ARM_ID` |
| `PROT_MASTER_ID` | [PROT_MASTER](PROT_MASTER.md) | `PROT_MASTER_ID` |
| `REMOVAL_ORGANIZATION_ID` | [ORGANIZATION](ORGANIZATION.md) | `ORGANIZATION_ID` |
| `REMOVAL_PERSON_ID` | [PRSNL](PRSNL.md) | `PERSON_ID` |

## Referenced by (3)

| From table | Column |
|------------|--------|
| [ASSIGN_REG_RELTN](ASSIGN_REG_RELTN.md) | `REG_ID` |
| [PT_REG_CONSENT_RELTN](PT_REG_CONSENT_RELTN.md) | `REG_ID` |
| [PT_REG_ELIG_RELTN](PT_REG_ELIG_RELTN.md) | `REG_ID` |

