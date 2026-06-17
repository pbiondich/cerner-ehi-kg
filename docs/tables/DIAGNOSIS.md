# DIAGNOSIS

> The diagnoses table stores medical diagnosis information for a patient encounter. This information describes symptoms the patient was experiencing at the time of the encounter.

**Description:** Diagnosis  
**Table type:** ACTIVITY  
**Primary key:** `DIAGNOSIS_ID`  
**Columns:** 64  
**Referenced by:** 13 columns

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ACTIVE_IND` | DOUBLE |  |  | The table row is active or inactive. A row is generally active unless it is in an inactive state such as logically deleted, combined away, pending purge, etc. |
| 2 | `ACTIVE_STATUS_CD` | DOUBLE | NOT NULL |  | Indicates the status of the row itself (not the data in the row) such as active, inactive, combined away, pending purge, etc. |
| 3 | `ACTIVE_STATUS_DT_TM` | DATETIME |  |  | The date and time that the active_status_cd was set. |
| 4 | `ACTIVE_STATUS_PRSNL_ID` | DOUBLE | NOT NULL |  | The person who caused the active_status_cd to be set or change. |
| 5 | `ASSERTED_DT_CD` | DOUBLE |  |  | Indicate to what level of accuracy the ASSERTED_CYCLE_DT_TM has been set (from code set 25320) |
| 6 | `ASSERTED_DT_FLAG` | DOUBLE |  |  | Indicates to what precision (Day, Month, Year, Week ) of the ASSERTED_CYCLE_DT_TM has been set |
| 7 | `ASSERTED_DT_TM` | DATETIME |  |  | The asserted date refers to the date when a patient or their caregiver reported or asserted the presence of a condition(Diagnosis) or problem; |
| 8 | `ASSERTED_TZ` | DOUBLE |  |  | Time zone associated with the ASSERTED_CYCLE_DT_TM column |
| 9 | `ATTESTATION_DT_TM` | DATETIME |  |  | The date by when the diagnosis was attested. |
| 10 | `BEG_EFFECTIVE_DT_TM` | DATETIME | NOT NULL |  | The date and time for which this table row becomes effective. Normally, this will be the date and time the row is added, but could be a past or future date and time. |
| 11 | `CERTAINTY_CD` | DOUBLE | NOT NULL |  | Description of the certainty level of the clinical diagnosis to be valid. |
| 12 | `CLASSIFICATION_CD` | DOUBLE | NOT NULL |  | Classification of the clinical diagnosis by the area of focus. |
| 13 | `CLINICAL_DIAG_PRIORITY` | DOUBLE |  |  | The priority of the diagnosis. |
| 14 | `CLINICAL_SERVICE_CD` | DOUBLE | NOT NULL |  | Associates the clinical diagnosis to a particular setting of care within an encounter. |
| 15 | `CONDITIONAL_QUAL_CD` | DOUBLE | NOT NULL |  | Supports the ability to further describe the clinical diagnosis by a qualifier that provides context information. |
| 16 | `CONFID_LEVEL_CD` | DOUBLE | NOT NULL |  | Indicates the confidentiality of the diagnosis data. |
| 17 | `CONFIRMATION_STATUS_CD` | DOUBLE | NOT NULL |  | Describes the definitiveness and clinical status of the diagnosis. |
| 18 | `CONTRIBUTOR_SYSTEM_CD` | DOUBLE | NOT NULL |  | Contributor system identifies the source feed of data from which a row was populated. This is mainly used to determine how to update a set of data that may have originated from more than one source feed. |
| 19 | `DIAGNOSIS_CLUSTER_IDENT_TXT` | VARCHAR(10) |  |  | The cluster, which includes several value types in the column, is a part of the column name. The following alphanumeric values will be stored: A-ZZ, 0, 1-7, 8, and 9. |
| 20 | `DIAGNOSIS_COMPLEXITY_LVL_TFLG` | VARCHAR(10) |  |  | Identifier for the respective row on the diagnosis table; it is the value assigned to the diagnosis codes. |
| 21 | `DIAGNOSIS_DISPLAY` | VARCHAR(255) |  |  | A denormalized, and possibly annotated description of the clinical diagnosis. This will default from the description of the chosen codified diagnosis code, and can be annotated (extended) by the clinician. This will be the column used when displaying this clinical diagnosis back to the user. |
| 22 | `DIAGNOSIS_GROUP` | DOUBLE | NOT NULL | FK→ | The unique identifier for the clinical diagnosis. The diagnosis_group can be associated with multiple diagnosis instances. When a new diagnosis is added to the diagnosis table the diagnosis group is assigned to the diagnosis_id |
| 23 | `DIAGNOSIS_ID` | DOUBLE | NOT NULL | PK | The primary key for the Diagnosis table. |
| 24 | `DIAGNOSTIC_CATEGORY_CD` | DOUBLE | NOT NULL |  | The category to which the diagnosis is assigned. |
| 25 | `DIAG_CLASS_CD` | DOUBLE | NOT NULL |  | The class to which the diagnosis is assigned. |
| 26 | `DIAG_DT_TM` | DATETIME |  |  | Date/time for which the Diagnosis was saved |
| 27 | `DIAG_FTDESC` | VARCHAR(255) |  |  | A free text diagnosis description. |
| 28 | `DIAG_NOTE` | VARCHAR(255) |  |  | Additional diagnosis information that may be added by user |
| 29 | `DIAG_PRIORITY` | DOUBLE |  |  | Priority of diagnoses as determined by application. |
| 30 | `DIAG_PRSNL_ID` | DOUBLE | NOT NULL |  | Prsnl_id of person that added the diagnosis. |
| 31 | `DIAG_PRSNL_NAME` | VARCHAR(100) |  |  | The name of the person that added the diagnosis. |
| 32 | `DIAG_TYPE_CD` | DOUBLE | NOT NULL |  | The type of diagnosis. |
| 33 | `ENCNTR_ID` | DOUBLE | NOT NULL | FK→ | This is the value of the unique primary identifier of the encounter table. It is an internal system assigned number. |
| 34 | `ENCNTR_SLICE_ID` | DOUBLE | NOT NULL | FK→ | Identifies an Encounter as it relates to a time slice. |
| 35 | `END_EFFECTIVE_DT_TM` | DATETIME | NOT NULL |  | The date/time after which the row is no longer valid as active current data. This may be valued with the date that the row became inactive. |
| 36 | `HAC_IND` | DOUBLE | NOT NULL |  | Indicates whether the diagnosis was a hospital acquired condition and contributed to a change in the grouper that likely resulted in a lower reimbursement. |
| 37 | `LATERALITY_CD` | DOUBLE | NOT NULL |  | Identifies the code value associated with the laterality of the clinical diagnosis. Code set 4002375. |
| 38 | `LIFE_CYCLE_DT_CD` | DOUBLE |  |  | Indicate to what level of accuracy the LIFE_CYCLE_DT_TM has been set; |
| 39 | `LIFE_CYCLE_DT_FLAG` | DOUBLE |  |  | Indicates to what precision (Day, Month, Year, Week Of) the LIFE_CYCLE_DT_TM has been set. |
| 40 | `LIFE_CYCLE_DT_TM` | DATETIME |  |  | The effective date and time of the condition's clinical status (life_cycle_status_cd) |
| 41 | `LIFE_CYCLE_STATUS_CD` | DOUBLE |  |  | The current status of the Diagnosis. - from code set 12030 |
| 42 | `LIFE_CYCLE_TZ` | DOUBLE |  |  | Time zone associated with the LIFE_CYCLE_DT_TM column |
| 43 | `LONG_BLOB_ID` | DOUBLE | NOT NULL | FK→ | If there are additional free text comments associated with the clinical diagnosis, this will contain the pointer to those comments on the long_blob table. |
| 44 | `MOD_NOMENCLATURE_ID` | DOUBLE | NOT NULL | FK→ | Contains the nomenclature ID from the nomenclature table for the nomenclature modifier. |
| 45 | `NOMENCLATURE_ID` | DOUBLE | NOT NULL | FK→ | This is the value of the unique primary identifier of the nomenclature table. It is an internal system assigned number. |
| 46 | `ORIGINATING_NOMENCLATURE_ID` | DOUBLE | NOT NULL | FK→ | The originating nomenclature id of the diagnosis. This is used to record the source nomenclature id of the diagnosis. |
| 47 | `PAC_CD` | DOUBLE |  |  | Indicates the post acute care coding value assigned to the diagnosis. |
| 48 | `PARENT_ENTITY_ID` | DOUBLE | NOT NULL |  | Primary key ID from the parent table. |
| 49 | `PARENT_ENTITY_NAME` | VARCHAR(30) | NOT NULL |  | Parent table name. |
| 50 | `PERSON_ID` | DOUBLE | NOT NULL | FK→ | This is the value of the unique primary identifier of the person table. It is an internal system assigned number. |
| 51 | `PRESENT_ON_ADMIT_CD` | DOUBLE | NOT NULL |  | Describes whether diagnosis is present on admission. |
| 52 | `PROBABILITY` | DOUBLE |  |  | Numeric percentage to reflect probability of validity of clinical diagnosis. |
| 53 | `RANKING_CD` | DOUBLE | NOT NULL |  | Codified ranking description. |
| 54 | `REFERENCE_NBR` | VARCHAR(100) |  |  | The combination of the reference nbr and the contributor system code provides a unique identifier to the origin of the data. |
| 55 | `SEG_UNIQUE_KEY` | VARCHAR(100) |  |  | This field contains a unique identifier for one of the multiple repetitions of the HL7 segment. |
| 56 | `SEVERITY_CD` | DOUBLE | NOT NULL |  | Codified severity of a condition identified by the clinical diagnosis |
| 57 | `SEVERITY_CLASS_CD` | DOUBLE | NOT NULL |  | Severity classification system by which the severity code is based on. |
| 58 | `SEVERITY_FTDESC` | VARCHAR(40) |  |  | Free text severity of a condition identified by clinical diagnosis |
| 59 | `SVC_CAT_HIST_ID` | DOUBLE | NOT NULL | FK→ | This is the unique identifier for the service category history table. |
| 60 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 61 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 62 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 63 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 64 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `DIAGNOSIS_GROUP` | [DIAGNOSIS](DIAGNOSIS.md) | `DIAGNOSIS_ID` |
| `ENCNTR_ID` | [ENCOUNTER](ENCOUNTER.md) | `ENCNTR_ID` |
| `ENCNTR_SLICE_ID` | [ENCNTR_SLICE](ENCNTR_SLICE.md) | `ENCNTR_SLICE_ID` |
| `LONG_BLOB_ID` | [LONG_BLOB](LONG_BLOB.md) | `LONG_BLOB_ID` |
| `MOD_NOMENCLATURE_ID` | [NOMENCLATURE](NOMENCLATURE.md) | `NOMENCLATURE_ID` |
| `NOMENCLATURE_ID` | [NOMENCLATURE](NOMENCLATURE.md) | `NOMENCLATURE_ID` |
| `ORIGINATING_NOMENCLATURE_ID` | [NOMENCLATURE](NOMENCLATURE.md) | `NOMENCLATURE_ID` |
| `PERSON_ID` | [PERSON](PERSON.md) | `PERSON_ID` |
| `SVC_CAT_HIST_ID` | [SERVICE_CATEGORY_HIST](SERVICE_CATEGORY_HIST.md) | `SVC_CAT_HIST_ID` |

## Referenced by (13)

| From table | Column |
|------------|--------|
| [CLRFCTN_ACTION](CLRFCTN_ACTION.md) | `DIAGNOSIS_ID` |
| [DIAGNOSIS](DIAGNOSIS.md) | `DIAGNOSIS_GROUP` |
| [DIAGNOSIS_ACTION](DIAGNOSIS_ACTION.md) | `DIAGNOSIS_ID` |
| [DIAGNOSIS_DETAIL](DIAGNOSIS_DETAIL.md) | `DIAGNOSIS_ID` |
| [DIAGNOSIS_DIAGNOSIS_RELTN](DIAGNOSIS_DIAGNOSIS_RELTN.md) | `CHILD_DIAGNOSIS_ID` |
| [DIAGNOSIS_DIAGNOSIS_RELTN](DIAGNOSIS_DIAGNOSIS_RELTN.md) | `PARENT_DIAGNOSIS_ID` |
| [DIAGNOSIS_PROCEDURE_RELTN](DIAGNOSIS_PROCEDURE_RELTN.md) | `CHILD_DIAGNOSIS_ID` |
| [DIAGNOSIS_SEC_LBL](DIAGNOSIS_SEC_LBL.md) | `DIAGNOSIS_GROUP_ID` |
| [ORDER_PROPOSAL_DIAG_RELTN](ORDER_PROPOSAL_DIAG_RELTN.md) | `DIAGNOSIS_ID` |
| [PM_WAIT_LIST_HIST](PM_WAIT_LIST_HIST.md) | `DIAGNOSIS_ID` |
| [PROCEDURE_DIAGNOSIS_RELTN](PROCEDURE_DIAGNOSIS_RELTN.md) | `PARENT_DIAGNOSIS_ID` |
| [SCD_STORY_CONCEPT](SCD_STORY_CONCEPT.md) | `DIAGNOSIS_GROUP_ID` |
| [VISITCODING_DX](VISITCODING_DX.md) | `DIAGNOSIS_ID` |

