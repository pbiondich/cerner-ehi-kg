# PT_ELIG_RESULT

> Stores all the answers entered when answering the eligibility questions to enrol a patient on a protocol

**Description:** Stores all the answers entered when answering the eligibility questions  
**Table type:** ACTIVITY  
**Primary key:** _(not published — see note)_  
**Columns:** 24

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ACTIVE_IND` | DOUBLE | NOT NULL |  | The table row is active or inactive. A row is generally active unless it is in an inactive state such as logically deleted, combined away, pending purge, etc. |
| 2 | `ACTIVE_STATUS_CD` | DOUBLE | NOT NULL |  | Indicates the status of the row itself (not the data in the row) such as active, inactive, combined away, pending purge, etc. |
| 3 | `ACTIVE_STATUS_DT_TM` | DATETIME | NOT NULL |  | The date and time that the active_status_cd was set. |
| 4 | `ACTIVE_STATUS_PRSNL_ID` | DOUBLE | NOT NULL |  | The person who caused the active_status_cd to be set or change. |
| 5 | `AUDITED_VALUE` | VARCHAR(255) |  |  | This field contains the value upon which the answer for the protocol eligibility question should have been based. |
| 6 | `AUDITED_VALUE_CD` | DOUBLE | NOT NULL |  | This field contains the answer for the protocol eligibility question entered during the verification process |
| 7 | `ELIG_INDICATOR_CD` | DOUBLE | NOT NULL |  | This field contains the code that indicates whether or not the patient met this eligibility requirement. |
| 8 | `ELIG_REVIEW_DT_TM` | DATETIME |  |  | This field contains the date and time on which the patient's eligibility for enrollment in the protocol was reviewed |
| 9 | `ELIG_VALUE_PROVIDER_ORG_ID` | DOUBLE | NOT NULL | FK→ | This field uniquely identifies a row in the organization table. This field identifies the institution/organization with which the individual who provided the value used to answer the protocol eligibility question was affiliated. |
| 10 | `ELIG_VALUE_PROVIDER_PERSON_ID` | DOUBLE | NOT NULL | FK→ | This field uniquely identifies a row in the person table. This field identifies the individual who supplied the value upon which the eligibility was based. |
| 11 | `PROT_AMENDMENT_ID` | DOUBLE | NOT NULL | FK→ | This field uniquely identifies a row in the prot_amendment table. This field identifies the protocol whose eligibility for enrollment is being evaluated. |
| 12 | `PROT_ELIG_QUEST_ID` | DOUBLE | NOT NULL | FK→ | This field uniquely identifies a row in the prot_elig_quest table. This field identifies the protocol eligibility question that was evaluated. |
| 13 | `PT_ELIG_RESULT_ID` | DOUBLE | NOT NULL |  | This is the value of the unique primary identifier of the pt_elig_result table. It is an internal system assigned number. |
| 14 | `PT_ELIG_TRACKING_ID` | DOUBLE | NOT NULL | FK→ | This field uniquely identifies a row in the pt_elig_tracking table. This field identifies the protocol enrollment attempt. |
| 15 | `SPECIMEN_TEST_DT_TM` | DATETIME |  |  | This field contains the date and time the specimen was collected or the date and time of the test upon which the patient's eligibility was determined. |
| 16 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 17 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 18 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 19 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 20 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |
| 21 | `VALUE` | VARCHAR(255) |  |  | This field contains the value upon which the patient's eligibility for enrollment in the protocol was determined. |
| 22 | `VALUE_CD` | DOUBLE | NOT NULL |  | The answer entered by the user during eligibility checking |
| 23 | `VERIFIED_ELIG_STATUS_CD` | DOUBLE | NOT NULL |  | This field contains the code identifying whether the patient met the eligibility criteria after the data was verified. |
| 24 | `VERIFIED_SPECIMEN_TEST_DT_TM` | DATETIME |  |  | This field contains the date and time the specimen was collected or the date and time of the test upon which the patient's eligibility was verified. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `ELIG_VALUE_PROVIDER_ORG_ID` | [ORGANIZATION](ORGANIZATION.md) | `ORGANIZATION_ID` |
| `ELIG_VALUE_PROVIDER_PERSON_ID` | [PRSNL](PRSNL.md) | `PERSON_ID` |
| `PROT_AMENDMENT_ID` | [PROT_AMENDMENT](PROT_AMENDMENT.md) | `PROT_AMENDMENT_ID` |
| `PROT_ELIG_QUEST_ID` | [PROT_ELIG_QUEST](PROT_ELIG_QUEST.md) | `PROT_ELIG_QUEST_ID` |
| `PT_ELIG_TRACKING_ID` | [PT_ELIG_TRACKING](PT_ELIG_TRACKING.md) | `PT_ELIG_TRACKING_ID` |

