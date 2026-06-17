# PROBLEM

> The Problem table contains coded and freetext problems that are being managed by care providers. Each row in the problem table represents an evolution of a problem.

**Description:** Problem  
**Table type:** ACTIVITY  
**Primary key:** `PROBLEM_INSTANCE_ID`  
**Columns:** 70  
**Referenced by:** 8 columns

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ACTIVE_IND` | DOUBLE |  |  | The table row is active or inactive. A row is generally active unless it is in an inactive state such as logically deleted, combined away, pending purge, etc. |
| 2 | `ACTIVE_STATUS_CD` | DOUBLE | NOT NULL |  | Indicates the status of the row itself (not the data in the row) such as active, inactive, combined away, pending purge, etc. |
| 3 | `ACTIVE_STATUS_DT_TM` | DATETIME |  |  | The date and time that the active_status_cd was set. |
| 4 | `ACTIVE_STATUS_PRSNL_ID` | DOUBLE | NOT NULL |  | The person who caused the active_status_cd to be set or change. |
| 5 | `ACTUAL_RESOLUTION_DT_TM` | DATETIME |  |  | The date and time that the problem was actually resolved. |
| 6 | `ANNOTATED_DISPLAY` | VARCHAR(255) |  |  | A de-normalized or annotated description of the problem. This is defaulted from the display term of the selected codified problem, and can be extended (annotated) by the clinician. |
| 7 | `ASSERTED_DT_CD` | DOUBLE |  |  | Indicate to what level of accuracy the ASSERTED_CYCLE_DT_TM has been set |
| 8 | `ASSERTED_DT_FLAG` | DOUBLE |  |  | Indicates to what precision (Day, Month, Year, Week Of) the ASSERTED_CYCLE_DT_TM has been set |
| 9 | `ASSERTED_DT_TM` | DATETIME |  |  | The asserted date refers to the date when a patient or their caregiver reported or asserted the presence of a condition(Diagnosis) or problem |
| 10 | `ASSERTED_TZ` | DOUBLE |  |  | Time zone associated with the ASSERTED_CYCLE_DT_TM column; |
| 11 | `BEG_EFFECTIVE_DT_TM` | DATETIME | NOT NULL |  | The date and time for which this table row becomes effective. Normally, this will be the date and time the row is added, but could be a past or future date and time. |
| 12 | `BEG_EFFECTIVE_TZ` | DOUBLE |  |  | Time zone associated with the corresponding DT_TM column. |
| 13 | `CANCEL_REASON_CD` | DOUBLE | NOT NULL |  | The cancel reason is required when a life cycle status of meaning CANCEL is selected. |
| 14 | `CERTAINTY_CD` | DOUBLE | NOT NULL |  | Contains a qualitative representation of the certainty of the problem. Alternative approach to probability_cd. |
| 15 | `CLASSIFICATION_CD` | DOUBLE | NOT NULL |  | Identifies the kind of problem. Used to categorize the problem so that it may be managed and viewed independently within different applications. |
| 16 | `COND_TYPE_FLAG` | DOUBLE | NOT NULL |  | The condition type. 0 - problem 1 - pregnancy related complication |
| 17 | `CONFIRMATION_STATUS_CD` | DOUBLE | NOT NULL |  | Indicates the verification status of the problem. |
| 18 | `CONTRIBUTOR_SYSTEM_CD` | DOUBLE | NOT NULL |  | Contributor system identifies the source feed of data from which a row was populated. This is mainly used to determine how to update a set of data that may have originated from more than one source feed. |
| 19 | `COURSE_CD` | DOUBLE | NOT NULL |  | Describes the progress of the disease, e.g. improving, stable, or worsening. |
| 20 | `DATA_STATUS_CD` | DOUBLE | NOT NULL |  | Data status indicates a level of authenticity of the row data. Typically this will either be AUTHENTICATED or UNAUTHENTICATED. |
| 21 | `DATA_STATUS_DT_TM` | DATETIME |  |  | The date and time that the data_status_cd was set. |
| 22 | `DATA_STATUS_PRSNL_ID` | DOUBLE | NOT NULL |  | The person who caused the data_status_cd to be set or change. |
| 23 | `DEL_IND` | DOUBLE |  |  | delete indicatorColumn |
| 24 | `END_EFFECTIVE_DT_TM` | DATETIME | NOT NULL |  | The date/time after which the row is no longer valid as active current data. This may be valued with the date that the row became inactive. |
| 25 | `ESTIMATED_RESOLUTION_DT_TM` | DATETIME |  |  | The estimated date and time that the problem will be resolved. |
| 26 | `FAMILY_AWARE_CD` | DOUBLE | NOT NULL |  | Indicates the family¿s comprehension of the actual problem and prognosis. |
| 27 | `IMPAIRMENT_TYPE_CD` | DOUBLE |  |  | UK REASONABLE ADJUSTMENT - IMPAIRMENT TYPE Code |
| 28 | `LATERALITY_CD` | DOUBLE | NOT NULL |  | Identifies the code value associated with the laterality of the problem. Code set 4002375 |
| 29 | `LIFE_CYCLE_DT_CD` | DOUBLE | NOT NULL |  | CODE SET: 25320 Indicate to what level of accuracy the life_cycle_dt_tm has been set. |
| 30 | `LIFE_CYCLE_DT_FLAG` | DOUBLE | NOT NULL |  | Indicates to what precision (Day, Month, Year) the life_cycle_dt_tm has been set. |
| 31 | `LIFE_CYCLE_DT_TM` | DATETIME |  |  | The effective date and time of the life_cycle_status_cd. |
| 32 | `LIFE_CYCLE_STATUS_CD` | DOUBLE | NOT NULL |  | The current status of the problem. |
| 33 | `LIFE_CYCLE_TZ` | DOUBLE |  |  | Time zone associated with the corresponding DT_TM column. |
| 34 | `NOMENCLATURE_ID` | DOUBLE | NOT NULL | FK→ | Unique identifier for nomenclature item. |
| 35 | `ONSET_DT_CD` | DOUBLE | NOT NULL |  | Not Used. |
| 36 | `ONSET_DT_FLAG` | DOUBLE |  |  | Indicates to what precision (Day, Month, or Year) the ONSET_DT_TM has been set. |
| 37 | `ONSET_DT_TM` | DATETIME |  |  | The date and time that the problem began. |
| 38 | `ONSET_TZ` | DOUBLE |  |  | Time zone associated with the corresponding DT_TM column. |
| 39 | `ORGANIZATION_ID` | DOUBLE | NOT NULL | FK→ | Organization ID. FK from ORGANIZATION table. |
| 40 | `ORIGINATING_ENCNTR_ID` | DOUBLE | NOT NULL | FK→ | The value of the unique primary identifierof the encounter table. Represents the originating encounter id on which the problem was first documented |
| 41 | `ORIGINATING_NOMENCLATURE_ID` | DOUBLE | NOT NULL | FK→ | The originating nomenclature id of the problem. This is used to record the source nomenclature id of the problem. |
| 42 | `OTHER_IMPAIRMENT_TEXT` | VARCHAR(255) |  |  | When 'Other' is chosen as the impairment type, this field should store the user's free text description of the impairment; |
| 43 | `PERSISTENCE_CD` | DOUBLE | NOT NULL |  | Indicates the perseverance of a problem. |
| 44 | `PERSON_AWARE_CD` | DOUBLE | NOT NULL |  | Identifies the person¿s comprehension of the problem. |
| 45 | `PERSON_AWARE_PROGNOSIS_CD` | DOUBLE | NOT NULL |  | Identifies the person¿s comprehension of the prognosis for the problem. |
| 46 | `PERSON_ID` | DOUBLE | NOT NULL | FK→ | This is the value of the unique primary identifier of the person table. It is an internal system assigned number. |
| 47 | `PROBABILITY` | DOUBLE |  |  | Contains a quantitative or numeric representation of the certainty of that the problem exists. For example, a .75 would imply a 75% probability that the problem was correclty identified. Alternative approach to certainty_cd. |
| 48 | `PROBLEM_FTDESC` | VARCHAR(255) |  |  | Allows a free text description of a problem not found in the nomenclature. |
| 49 | `PROBLEM_ID` | DOUBLE | NOT NULL |  | Uniquely defines a problem within the problem table. The problem_id can be associated with multiple problem instances. When a new problem is added to the problem table the problem_id is assigned to the problem_instance_id. |
| 50 | `PROBLEM_INSTANCE_ID` | DOUBLE | NOT NULL | PK | Unique identifier for the problem table. Each change or revision made to a problem creates a new problem instance. |
| 51 | `PROBLEM_INSTANCE_UUID` | VARCHAR(255) | NOT NULL |  | Problem instance unique universal identifierColumn |
| 52 | `PROBLEM_TYPE_FLAG` | DOUBLE | NOT NULL |  | Problem type flag (0 = problem, 1 = past medical history, 2 = Pregnancy) |
| 53 | `PROBLEM_UUID` | VARCHAR(255) | NOT NULL |  | Problem unique universal identifierColumn |
| 54 | `PROGNOSIS_CD` | DOUBLE | NOT NULL |  | Contains the prognosis for the person¿s problem. |
| 55 | `QUALIFIER_CD` | DOUBLE | NOT NULL |  | It supports the ability to further describe the clinical diagnosis by a qualifier that provides context information. |
| 56 | `RANKING_CD` | DOUBLE | NOT NULL |  | A user-defined prioritization of the problem. |
| 57 | `SENSITIVITY` | DOUBLE |  |  | Indicates the level of sensitivity surrounding the problem. |
| 58 | `SEVERITY_CD` | DOUBLE | NOT NULL |  | Severity of a condition identified by the problem. |
| 59 | `SEVERITY_CLASS_CD` | DOUBLE | NOT NULL |  | Severity classification system by which the severity code is based on |
| 60 | `SEVERITY_FTDESC` | VARCHAR(40) |  |  | Free text severity of a condition identified by the problem. |
| 61 | `SHOW_IN_PM_HISTORY_IND` | DOUBLE | NOT NULL |  | Used to show a particular problem item in past medical history view |
| 62 | `STATUS_UPDT_DT_TM` | DATETIME |  |  | The date time where the problem was modified. |
| 63 | `STATUS_UPDT_FLAG` | DOUBLE |  |  | Indicates to what precision (Day, Month, or Year) the status_upt_DT_TM has been set. |
| 64 | `STATUS_UPDT_PRECISION_CD` | DOUBLE | NOT NULL |  | Indicated to what level of accuracy the status_upd_DT_TM has been set. |
| 65 | `UPDATE_ENCNTR_ID` | DOUBLE | NOT NULL | FK→ | The value of the unique primary identifierof the encounter table. Represents the last encounter id on which the problem was modified |
| 66 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 67 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 68 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 69 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 70 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `NOMENCLATURE_ID` | [NOMENCLATURE](NOMENCLATURE.md) | `NOMENCLATURE_ID` |
| `ORGANIZATION_ID` | [ORGANIZATION](ORGANIZATION.md) | `ORGANIZATION_ID` |
| `ORIGINATING_ENCNTR_ID` | [ENCOUNTER](ENCOUNTER.md) | `ENCNTR_ID` |
| `ORIGINATING_NOMENCLATURE_ID` | [NOMENCLATURE](NOMENCLATURE.md) | `NOMENCLATURE_ID` |
| `PERSON_ID` | [PERSON](PERSON.md) | `PERSON_ID` |
| `UPDATE_ENCNTR_ID` | [ENCOUNTER](ENCOUNTER.md) | `ENCNTR_ID` |

## Referenced by (8)

| From table | Column |
|------------|--------|
| [ONC_FORM_ACTIVITY](ONC_FORM_ACTIVITY.md) | `PROBLEM_ID` |
| [PREGNANCY_INSTANCE](PREGNANCY_INSTANCE.md) | `PROBLEM_ID` |
| [PROBLEM_ACTION](PROBLEM_ACTION.md) | `PROBLEM_INSTANCE_ID` |
| [PROBLEM_COMMENT](PROBLEM_COMMENT.md) | `PROBLEM_ID` |
| [PROBLEM_DISCIPLINE](PROBLEM_DISCIPLINE.md) | `PROBLEM_ID` |
| [PROBLEM_EXT_DATA](PROBLEM_EXT_DATA.md) | `PROBLEM_ID` |
| [PROBLEM_PRSNL_R](PROBLEM_PRSNL_R.md) | `PROBLEM_ID` |
| [PROBLEM_SEC_LBL](PROBLEM_SEC_LBL.md) | `PROBLEM_ID` |

