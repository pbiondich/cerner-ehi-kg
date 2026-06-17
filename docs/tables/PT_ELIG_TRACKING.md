# PT_ELIG_TRACKING

> This table stores the eligiblity attempts done to enroll a patient on a protocol. It stores the status of the attempt, such as if the patient was found eligible etc.

**Description:** This table stores the eligiblity attempts done to enroll a patient on a protocol  
**Table type:** ACTIVITY  
**Primary key:** `PT_ELIG_TRACKING_ID`  
**Columns:** 21  
**Referenced by:** 6 columns

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `BEG_EFFECTIVE_DT_TM` | DATETIME | NOT NULL |  | The date and time for which this table row becomes effective. Normally, this will be the date and time the row is added, but could be a past or future date and time. |
| 2 | `ELIG_REQUEST_ORG_ID` | DOUBLE | NOT NULL | FK→ | Organization requesting the eligibilty attempt of the patient on the protocol |
| 3 | `ELIG_REQUEST_PERSON_ID` | DOUBLE | NOT NULL | FK→ | The person requesting the eligiblity attempt of the patient on the protocol |
| 4 | `ELIG_REVIEW_ORG_ID` | DOUBLE | NOT NULL | FK→ | The organization reviewing the eligibility attempt |
| 5 | `ELIG_REVIEW_PERSON_ID` | DOUBLE | NOT NULL | FK→ | The person reviewing the eligiblity |
| 6 | `ELIG_STATUS_CD` | DOUBLE | NOT NULL |  | This field contains the code defining the patient's eligibility for enrollment in the protocol. |
| 7 | `ENROLLMENT_NBR` | DOUBLE | NOT NULL |  | This field identifies the sequence of the protocol amendment for which the patient is being evaluated for eligibility. |
| 8 | `LAST_ATTEMPT_INDICATOR_CD` | DOUBLE | NOT NULL |  | This field contains the code that defines this attempt to enroll the patient in the protocol as the last attempt made to enroll the patient in the protocol. |
| 9 | `OVERRIDE_DT_TM` | DATETIME |  |  | Stores the date that the eligibility evaluation was over-ridden |
| 10 | `OVERRIDE_REASON_CD` | DOUBLE | NOT NULL |  | Stores the reason why eligibility evaluation was over-ridden |
| 11 | `PERSON_ID` | DOUBLE | NOT NULL | FK→ | This is the value of the unique primary identifier of the person table. It is an internal system assigned number. |
| 12 | `PROT_AMENDMENT_ID` | DOUBLE | NOT NULL | FK→ | This field uniquely identifies a row in the prot_amendment table. This field identifies the protocol amendment for which the patient's eligibility is being evaluated. ***OBSOLETE*** |
| 13 | `PROT_QUESTIONNAIRE_ID` | DOUBLE | NOT NULL | FK→ | Uniquely identifies a questionnaire in the table |
| 14 | `PT_ELIG_TRACKING_ID` | DOUBLE | NOT NULL | PK | Primary key of pt_elig_tracking table |
| 15 | `REASON_INELIGIBLE_CD` | DOUBLE | NOT NULL |  | This field contains the code for the primary reason the patient was found ineligible to be enrolled in the protocol. |
| 16 | `SEQUENCE_NBR` | DOUBLE | NOT NULL |  | This field contains the number of the attempt to enroll the patient in the protocol amendment. |
| 17 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 18 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 19 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 20 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 21 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `ELIG_REQUEST_ORG_ID` | [ORGANIZATION](ORGANIZATION.md) | `ORGANIZATION_ID` |
| `ELIG_REQUEST_PERSON_ID` | [PRSNL](PRSNL.md) | `PERSON_ID` |
| `ELIG_REVIEW_ORG_ID` | [ORGANIZATION](ORGANIZATION.md) | `ORGANIZATION_ID` |
| `ELIG_REVIEW_PERSON_ID` | [PRSNL](PRSNL.md) | `PERSON_ID` |
| `PERSON_ID` | [PERSON](PERSON.md) | `PERSON_ID` |
| `PROT_AMENDMENT_ID` | [PROT_AMENDMENT](PROT_AMENDMENT.md) | `PROT_AMENDMENT_ID` |
| `PROT_QUESTIONNAIRE_ID` | [PROT_QUESTIONNAIRE](PROT_QUESTIONNAIRE.md) | `PROT_QUESTIONNAIRE_ID` |

## Referenced by (6)

| From table | Column |
|------------|--------|
| [ASSIGN_ELIG_RELTN](ASSIGN_ELIG_RELTN.md) | `PT_ELIG_TRACKING_ID` |
| [CT_REASON_DELETED](CT_REASON_DELETED.md) | `PT_ELIG_TRACKING_ID` |
| [PT_ELIG_CONSENT_RELTN](PT_ELIG_CONSENT_RELTN.md) | `PT_ELIG_TRACKING_ID` |
| [PT_ELIG_RESULT](PT_ELIG_RESULT.md) | `PT_ELIG_TRACKING_ID` |
| [PT_ELIG_TRACKING_NOTES](PT_ELIG_TRACKING_NOTES.md) | `PT_ELIG_TRACKING_ID` |
| [PT_REG_ELIG_RELTN](PT_REG_ELIG_RELTN.md) | `PT_ELIG_TRACKING_ID` |

