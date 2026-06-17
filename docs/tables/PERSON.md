# PERSON

> The person table contains all persons in the system. A row in the person table may or may not represent a person who is a patient and/or personnel (i.e., doctor, nurse, etc.).

**Description:** Person  
**Table type:** ACTIVITY  
**Primary key:** `PERSON_ID`  
**Columns:** 89  
**Referenced by:** 486 columns

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ABS_BIRTH_DT_TM` | DATETIME |  |  | The birth date/time "as entered" during registration. The date/time data in this field is "local" when the database is running in "UTC mode" and it is typically not populated (NULL) when the database is running in "local mode." This field is used for querying purposes only and helps eliminate edge cases where records fail to qualify because the user performing the search is in a different time zone than the patient. |
| 2 | `ACTIVE_IND` | DOUBLE |  |  | The table row is active or inactive. A row is generally active unless it is in an inactive state such as logically deleted, combined away, pending purge, etc. |
| 3 | `ACTIVE_STATUS_CD` | DOUBLE | NOT NULL |  | Indicates the status of the row itself (not the data in the row) such as active, inactive, combined away, pending purge, etc. |
| 4 | `ACTIVE_STATUS_DT_TM` | DATETIME |  |  | The date and time that the active_status_cd was set. |
| 5 | `ACTIVE_STATUS_PRSNL_ID` | DOUBLE | NOT NULL |  | The person who caused the active_status_cd to be set or change. |
| 6 | `AGE_AT_DEATH` | DOUBLE | NOT NULL |  | The age of the person when they became deceased. |
| 7 | `AGE_AT_DEATH_PREC_MOD_FLAG` | DOUBLE | NOT NULL |  | Precision modifier used to represent the precision of the age of death. A flag of 0 means unknown. 1 - The age is less than the stated age of death. 2 - The age is greater than the stated age of death. 3 - The stated age of death is approximated. 4 - The stated age of death is exact. |
| 8 | `AGE_AT_DEATH_UNIT_CD` | DOUBLE | NOT NULL |  | The unit of measurement for the age at death. (Years, Months, Days or Hours) |
| 9 | `ARCHIVE_ENV_ID` | DOUBLE | NOT NULL |  | This column will indicate the environment_id that contains the data for this person. This column will be 0 for persons that have not been archived. |
| 10 | `ARCHIVE_STATUS_CD` | DOUBLE | NOT NULL |  | This column will indicate the archive status for this person. It will use a new code set that is not yet created. |
| 11 | `ARCHIVE_STATUS_DT_TM` | DATETIME |  |  | This column will indicate the last time this person was involved in an archive or restore. |
| 12 | `AUTOPSY_CD` | DOUBLE | NOT NULL |  | Indicates whether an autopsy has been performed on this person. |
| 13 | `BEG_EFFECTIVE_DT_TM` | DATETIME | NOT NULL |  | The date and time for which this table row becomes effective. Normally, this will be the date and time the row is added, but could be a past or future date and time. |
| 14 | `BIRTH_DT_CD` | DOUBLE | NOT NULL |  | Birth date code indicates the kind of birth date and time value that is contained in the birth_dt_tm field. (i.e., estimated, still born, unknown, etc.) |
| 15 | `BIRTH_DT_TM` | DATETIME |  |  | The date and time of birth for the person. |
| 16 | `BIRTH_PREC_FLAG` | DOUBLE |  |  | Used to denote what information was captured for birth date and time. A flag of 0 means the date is precise to the day, a flag of 1 means the date is precise to the full date and time, a flag of 2 means the date is precise to month and a flag of 3 means the date is precise to year. |
| 17 | `BIRTH_TZ` | DOUBLE |  |  | Time zone associated with the corresponding DT_TM column. |
| 18 | `CAUSE_OF_DEATH` | VARCHAR(100) |  |  | This is a text description of what caused the death of the person. |
| 19 | `CAUSE_OF_DEATH_CD` | DOUBLE | NOT NULL |  | This is a codified value of what caused the death of the person. |
| 20 | `CITIZENSHIP_CD` | DOUBLE | NOT NULL |  | Identifies the citizenship status for a person. |
| 21 | `CONCEPTION_DT_TM` | DATETIME |  |  | The date and time the person was conceived in the mother's womb. |
| 22 | `CONFID_LEVEL_CD` | DOUBLE | NOT NULL |  | Confidential level identifies a level of security that may restrict access or release of information. |
| 23 | `CONFID_LEVEL_SOURCE_CD` | DOUBLE |  |  | Defines the source that provided the confidentiality level information concerning a person. |
| 24 | `CONTRIBUTOR_SYSTEM_CD` | DOUBLE | NOT NULL |  | Contributor system identifies the source feed of data from which a row was populated. This is mainly used to determine how to update a set of data that may have originated from more than one source feed. |
| 25 | `CREATE_DT_TM` | DATETIME |  |  | This is the date and time that a row is created in the person table. |
| 26 | `CREATE_PRSNL_ID` | DOUBLE | NOT NULL |  | This is the person/personnel responsible for creating a row in the person table. |
| 27 | `DATA_STATUS_CD` | DOUBLE | NOT NULL |  | Data status indicates a level of authenticity of the row data. Typically this will either be AUTHENTICATED or UNAUTHENTICATED. |
| 28 | `DATA_STATUS_DT_TM` | DATETIME |  |  | The date and time that the data_status_cd was set. |
| 29 | `DATA_STATUS_PRSNL_ID` | DOUBLE | NOT NULL |  | The person who caused the data_status_cd to be set or change. |
| 30 | `DECEASED_CD` | DOUBLE | NOT NULL |  | Identifies if the person is deceased. |
| 31 | `DECEASED_DT_TM` | DATETIME |  |  | The date and time of death for the person. |
| 32 | `DECEASED_DT_TM_PREC_FLAG` | DOUBLE | NOT NULL |  | Used to denote the precision of the deceased date and time. 0 - Precision is unknown. 1 - Date is precise to the full date and time. 2 - Date is precise to the month. 3 - Date is precise to the year. 4 - Date is precise to the day. |
| 33 | `DECEASED_ID_METHOD_CD` | DOUBLE | NOT NULL |  | Stores code values defining the specific way a patient was confirmed as being deceased. Possible values include Death Certificate, Physician Reported, etc. The code values are closely tied, workflow-wise, to the Deceased_Source_Cd which records if a patient was identified as being deceased from a Formal (Death Certificate) or Informal (no Death Certificate) source and the Deceased_Notify_Source_Cd which records who\ what provided the information regarding the patient's deceased status. |
| 34 | `DECEASED_NOTIFY_SOURCE_CD` | DOUBLE |  |  | Defines the particular source that gave notification regarding the deceased information concerning a person. For example, from a Government Agency Record, Inpatient Death, or Other. |
| 35 | `DECEASED_SOURCE_CD` | DOUBLE | NOT NULL |  | Defines the particular source that gave deceased information concerning a person. For example, from a Formal (Death Certificate) or Informal (no Death Certificate) source. |
| 36 | `DECEASED_TZ` | DOUBLE | NOT NULL |  | The time zone where the deceased date was entered. |
| 37 | `EMANCIPATION_DT_TM` | DATETIME |  |  | The date and time when the person was emancipated. |
| 38 | `END_EFFECTIVE_DT_TM` | DATETIME |  |  | The date/time after which the row is no longer valid as active current data. This may be valued with the date that the row became inactive. |
| 39 | `ETHNIC_GRP_CD` | DOUBLE | NOT NULL |  | Identifies a religious, national, racial, or cultural group of the person. |
| 40 | `FT_ENTITY_ID` | DOUBLE | NOT NULL |  | Used to identify the ID of the free textentity which this free textperson row is associated with. |
| 41 | `FT_ENTITY_NAME` | VARCHAR(32) |  |  | Name of the entity for which this free textperson row is associated. |
| 42 | `LANGUAGE_CD` | DOUBLE | NOT NULL |  | The primary language spoken by the person. |
| 43 | `LANGUAGE_DIALECT_CD` | DOUBLE | NOT NULL |  | The dialect of the primary language spoken by the person. |
| 44 | `LAST_ACCESSED_DT_TM` | DATETIME | NOT NULL |  | This column contains the date/time this person was last accessed. It affects when the person will be archived when archiving is active. |
| 45 | `LAST_ENCNTR_DT_TM` | DATETIME |  |  | The date and time of the last encounter for the person. |
| 46 | `LOGICAL_DOMAIN_ID` | DOUBLE | NOT NULL | FK→ | The unique identifier for a logical domain. This identifier allows the data to be grouped by logical domain. For example, If you assign clients a logical_domain_id this would allow you to store data for multiple clients on this table. |
| 47 | `MARITAL_TYPE_CD` | DOUBLE | NOT NULL |  | This field identifies the status of the person with regard to being married. |
| 48 | `MILITARY_BASE_LOCATION` | VARCHAR(100) |  |  | The location of the military base at which the person is stationed. |
| 49 | `MILITARY_RANK_CD` | DOUBLE | NOT NULL |  | Military ranking of individual (i.e. Private, Seargent, General, etc.) |
| 50 | `MILITARY_SERVICE_CD` | DOUBLE | NOT NULL |  | Military status of an individual (i.e. Active Duty, Reserves, etc.) |
| 51 | `MOTHER_MAIDEN_NAME` | VARCHAR(100) |  |  | The mother's last name she was given at birth. |
| 52 | `NAME_FIRST` | VARCHAR(200) |  |  | This is the person's given first name. |
| 53 | `NAME_FIRST_KEY` | VARCHAR(100) |  |  | This is the person's first given name all capitals with punctuation removed. This field is used for indexing and searching for a person by name. |
| 54 | `NAME_FIRST_KEY_A_NLS` | VARCHAR(400) |  |  | NAME_FIRST_KEY_A_NLS column |
| 55 | `NAME_FIRST_KEY_NLS` | VARCHAR(202) |  |  | First Name Key field converted to NLS format for internationalization requirements |
| 56 | `NAME_FIRST_PHONETIC` | VARCHAR(8) |  |  | Phonetic representation of person's first name. |
| 57 | `NAME_FIRST_SYNONYM_ID` | DOUBLE | NOT NULL |  | First Name Synonym Id |
| 58 | `NAME_FULL_FORMATTED` | VARCHAR(100) |  |  | This is the complete person name including punctuation and formatting. |
| 59 | `NAME_LAST` | VARCHAR(200) |  |  | This is the person's family name. |
| 60 | `NAME_LAST_KEY` | VARCHAR(100) |  |  | This is the person's family name all capitals with punctuation removed. This field is used for indexing and searching for a person by name. |
| 61 | `NAME_LAST_KEY_A_NLS` | VARCHAR(400) |  |  | NAME_LAST_KEY_A_NLS column |
| 62 | `NAME_LAST_KEY_NLS` | VARCHAR(202) |  |  | Last Name Key field converted to NLS format for internationalization requirements |
| 63 | `NAME_LAST_PHONETIC` | VARCHAR(8) |  |  | Phonetic representation of person's last name. |
| 64 | `NAME_MIDDLE` | VARCHAR(200) |  |  | This is the given middle name for the person. |
| 65 | `NAME_MIDDLE_KEY` | VARCHAR(100) |  |  | This is the person's middle name with all capitals with punctuation removed. This field is used for indexing and searching for a person by name. |
| 66 | `NAME_MIDDLE_KEY_A_NLS` | VARCHAR(400) |  |  | NAME_MIDDLE_KEY_A_NLS column |
| 67 | `NAME_MIDDLE_KEY_NLS` | VARCHAR(202) |  |  | Last Name Key field converted to NLS format for internationalization requirements |
| 68 | `NAME_PHONETIC` | CHAR(8) |  |  | This is the Soundex coded representation of the person's name. This field is used for indexing and searching for a patient by name when the exact spelling is not known. |
| 69 | `NATIONALITY_CD` | DOUBLE | NOT NULL |  | This field Identifies the nationality associated with the person. |
| 70 | `NEXT_RESTORE_DT_TM` | DATETIME |  |  | This column contains the date/time when this person needs to be restored from archive. |
| 71 | `PERSONAL_PRONOUN_CD` | DOUBLE |  |  | The person's desired personal pronouns to use as a simple substitue for their proper name that they feel best represents their gender identity. Examples may include She/Her/Hers, He/Him/His,They/Them/Theirs, etc. |
| 72 | `PERSONAL_PRONOUN_OTHER_TXT` | VARCHAR(100) |  |  | The other personal pronoun text of the person when the person's personal pronoun code is OTHER. |
| 73 | `PERSON_ID` | DOUBLE | NOT NULL | PK | This is the value of the unique primary identifier of the person table. It is an internal system assigned number. |
| 74 | `PERSON_STATUS_CD` | DOUBLE | NOT NULL |  | The current status of the person |
| 75 | `PERSON_TYPE_CD` | DOUBLE | NOT NULL |  | The person type field identifies the general type of data being stored in a given person row. As a general guideline, most rows in the person table will be identified with a person type of PERSON. This field can be used to filter out NON-PERSON rows. |
| 76 | `PURGE_OPTION_CD` | DOUBLE | NOT NULL |  | OBSOLETE: Purge Option Code Value |
| 77 | `RACE_CD` | DOUBLE | NOT NULL |  | A group of people classified together on the basis of common history, nationality, or geographical distribution. |
| 78 | `RELIGION_CD` | DOUBLE | NOT NULL |  | A particular integrated system of belief in a supernatural power. |
| 79 | `RESIDENT_CD` | DOUBLE | NOT NULL |  | Identifies the resident status for a person. |
| 80 | `SEX_AGE_CHANGE_IND` | DOUBLE |  |  | This field indicates that the sex of the person has changed as the result of a correction of the data or actual physical change to the person. |
| 81 | `SEX_CD` | DOUBLE | NOT NULL |  | The sex/gender that the patient is considered to have for administration and record keeping purposes. This is typically asserted by the patient when they present to administrative users. This may not match the biological sex as determined by anatomy or genetics, or the individual's preferred identification (gender identity). |
| 82 | `SPECIES_CD` | DOUBLE | NOT NULL |  | A fundamental category of taxonomic classification, ranking after a genus and consisting of organisms capable of interbreeding. |
| 83 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 84 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 85 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 86 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 87 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 88 | `VET_MILITARY_STATUS_CD` | DOUBLE | NOT NULL |  | Identifies the military status of a service veteran. |
| 89 | `VIP_CD` | DOUBLE | NOT NULL |  | Identifies and used to communicate that the person is identified as deserving special consideration during the stay or visit. A security level (confid_level_cd) may or may not be implied by a V.I.P. code. Examples include employee, famous person, etc. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `LOGICAL_DOMAIN_ID` | [LOGICAL_DOMAIN](LOGICAL_DOMAIN.md) | `LOGICAL_DOMAIN_ID` |

## Referenced by (486)

| From table | Column |
|------------|--------|
| [ABSTRACTING](ABSTRACTING.md) | `PERSON_ID` |
| [ABSTRACT_DATA](ABSTRACT_DATA.md) | `PERSON_ID` |
| [ABST_CODING_RELTN](ABST_CODING_RELTN.md) | `PERSON_ID` |
| [ACCT_BALANCE](ACCT_BALANCE.md) | `PERSON_ID` |
| [ACTIVITY_DATA_RELTN](ACTIVITY_DATA_RELTN.md) | `PERSON_ID` |
| [ACT_PW_COMP](ACT_PW_COMP.md) | `PERSON_ID` |
| [ACUTE_CARE_AUDIT_INFO](ACUTE_CARE_AUDIT_INFO.md) | `AUDIT_PATIENT_ID` |
| [AC_CLASS_PERSON_RELTN](AC_CLASS_PERSON_RELTN.md) | `PERSON_ID` |
| [ALERT_AUDIT_TRANSACTION](ALERT_AUDIT_TRANSACTION.md) | `PERSON_ID` |
| [ALLERGY](ALLERGY.md) | `PERSON_ID` |
| [ALLERGY_EXT_DATA](ALLERGY_EXT_DATA.md) | `CMB_PERSON_ID` |
| [ALLERGY_EXT_DATA](ALLERGY_EXT_DATA.md) | `PERSON_ID` |
| [AOAV_CONDITION](AOAV_CONDITION.md) | `PERSON_ID` |
| [AOAV_PERSON_ENCNTR](AOAV_PERSON_ENCNTR.md) | `PERSON_ID` |
| [APPLICATION_GROUP](APPLICATION_GROUP.md) | `PERSON_ID` |
| [AP_EXT_DATA](AP_EXT_DATA.md) | `PERSON_ID` |
| [AP_FT_EVENT](AP_FT_EVENT.md) | `PERSON_ID` |
| [AP_QA_INFO](AP_QA_INFO.md) | `PERSON_ID` |
| [ASSIGN](ASSIGN.md) | `PERSON_ID` |
| [AUTHORIZATION](AUTHORIZATION.md) | `PERSON_ID` |
| [AUTO_DIRECTED](AUTO_DIRECTED.md) | `PERSON_ID` |
| [AV_STATUS_EVENT](AV_STATUS_EVENT.md) | `PERSON_ID` |
| [BATCH_TRANS_FILE](BATCH_TRANS_FILE.md) | `GUARANTOR_PERSON_ID` |
| [BBHIST_PRODUCT_EVENT](BBHIST_PRODUCT_EVENT.md) | `PERSON_ID` |
| [BB_EDN_PRODUCT](BB_EDN_PRODUCT.md) | `PERSON_ID` |
| [BB_EXCEPTION](BB_EXCEPTION.md) | `PERSON_ID` |
| [BB_SPEC_EXPIRE_OVRD](BB_SPEC_EXPIRE_OVRD.md) | `PERSON_ID` |
| [BB_UPLOAD_REVIEW](BB_UPLOAD_REVIEW.md) | `PERSON_ID` |
| [BCE_EVENT_LOG](BCE_EVENT_LOG.md) | `ACTIVE_STATUS_PRSNL_ID` |
| [BCE_EVENT_LOG](BCE_EVENT_LOG.md) | `PERSON_ID` |
| [BH_GROUP_DOC_PATIENT](BH_GROUP_DOC_PATIENT.md) | `PERSON_ID` |
| [BLOOD_BANK_COMMENT](BLOOD_BANK_COMMENT.md) | `PERSON_ID` |
| [BLOOD_PRODUCT](BLOOD_PRODUCT.md) | `DONOR_PERSON_ID` |
| [BMDI_ACQUIRED_DATA_TRACK](BMDI_ACQUIRED_DATA_TRACK.md) | `PERSON_ID` |
| [BMDI_ACQUIRED_RESULTS](BMDI_ACQUIRED_RESULTS.md) | `PERSON_ID` |
| [BMDI_ASSOCIATION_HINTS](BMDI_ASSOCIATION_HINTS.md) | `PERSON_ID` |
| [CAC_DOCUMENT](CAC_DOCUMENT.md) | `PERSON_ID` |
| [CBOS_PERSON_RELTN](CBOS_PERSON_RELTN.md) | `PERSON_ID` |
| [CDI_TRANS_LOG](CDI_TRANS_LOG.md) | `PERSON_ID` |
| [CE_AUDIT_LOG](CE_AUDIT_LOG.md) | `PERSON_ID` |
| [CE_DYNAMIC_LABEL](CE_DYNAMIC_LABEL.md) | `PERSON_ID` |
| [CE_EVENT_ACTION](CE_EVENT_ACTION.md) | `PERSON_ID` |
| [CE_EVENT_MODIFIER](CE_EVENT_MODIFIER.md) | `MODIFIER_VALUE_PERSON_ID` |
| [CE_EVENT_PRSNL](CE_EVENT_PRSNL.md) | `PERSON_ID` |
| [CE_EVENT_PRSNL](CE_EVENT_PRSNL.md) | `RECEIVING_PERSON_ID` |
| [CE_FLAGGED_RESULT](CE_FLAGGED_RESULT.md) | `PERSON_ID` |
| [CE_GROUPING_QUEUE](CE_GROUPING_QUEUE.md) | `PERSON_ID` |
| [CE_INTAKE_OUTPUT_RESULT](CE_INTAKE_OUTPUT_RESULT.md) | `PERSON_ID` |
| [CE_IO_TOTAL_RESULT](CE_IO_TOTAL_RESULT.md) | `PERSON_ID` |
| [CE_MED_RESULT](CE_MED_RESULT.md) | `ADMIN_PROV_ID` |
| [CHARGE](CHARGE.md) | `PERSON_ID` |
| [CHARGE_EVENT](CHARGE_EVENT.md) | `PERSON_ID` |
| [CHART_ENCNTR_DISCHARGE](CHART_ENCNTR_DISCHARGE.md) | `PERSON_ID` |
| [CHART_PROCESS](CHART_PROCESS.md) | `PERSON_ID` |
| [CHART_REQUEST](CHART_REQUEST.md) | `PERSON_ID` |
| [CHART_TEMP](CHART_TEMP.md) | `PERSON_ID` |
| [CLINICAL_EVENT](CLINICAL_EVENT.md) | `PERSON_ID` |
| [CN_DCP_SHIFT_ASSIGNMENT_ST](CN_DCP_SHIFT_ASSIGNMENT_ST.md) | `PERSON_ID` |
| [CN_DCP_SHIFT_ASSIGNMENT_ST](CN_DCP_SHIFT_ASSIGNMENT_ST.md) | `RELATED_PERSON_ID` |
| [CODING](CODING.md) | `PERSON_ID` |
| [CODING_AUDIT](CODING_AUDIT.md) | `PERSON_ID` |
| [CODING_HIST](CODING_HIST.md) | `PERSON_ID` |
| [CODING_SPECIALTY](CODING_SPECIALTY.md) | `PERSON_ID` |
| [COMPLETION_HOLD](COMPLETION_HOLD.md) | `PERSON_ID` |
| [CONCEPT_PRSNL_CROSSMAP](CONCEPT_PRSNL_CROSSMAP.md) | `PERSON_ID` |
| [CONDITION_PRIORITY](CONDITION_PRIORITY.md) | `PERSON_ID` |
| [CONDITION_SUMMARY](CONDITION_SUMMARY.md) | `PERSON_ID` |
| [CONSENT](CONSENT.md) | `CONSENT_GIVEN_PERSON_ID` |
| [CONSENT](CONSENT.md) | `PERSON_ID` |
| [CONSENT_PATIENTSYNC_AUDIT](CONSENT_PATIENTSYNC_AUDIT.md) | `PERSON_ID` |
| [CONS_BO_SCHED](CONS_BO_SCHED.md) | `PERSON_ID` |
| [CORRECTED_PRODUCT](CORRECTED_PRODUCT.md) | `PERSON_ID` |
| [CP_PATHWAY_ACTIVITY](CP_PATHWAY_ACTIVITY.md) | `PERSON_ID` |
| [CREDIT_CARD_RELTN](CREDIT_CARD_RELTN.md) | `PERSON_ID` |
| [CROSSMATCH](CROSSMATCH.md) | `PERSON_ID` |
| [CR_REPORT_REQUEST](CR_REPORT_REQUEST.md) | `PERSON_ID` |
| [CR_XML_DOC_REQUEST](CR_XML_DOC_REQUEST.md) | `PERSON_ID` |
| [CSA_USER_AGREEMENT_ACK](CSA_USER_AGREEMENT_ACK.md) | `PERSON_ID` |
| [CS_CPP_ERROR_LOG](CS_CPP_ERROR_LOG.md) | `PERSON_ID` |
| [CS_CPP_UNDO](CS_CPP_UNDO.md) | `PERSON_ID` |
| [CT_PROT_PRESCREEN_JOB_INFO](CT_PROT_PRESCREEN_JOB_INFO.md) | `PERSON_ID` |
| [CT_PT_PROT_BATCH_LIST](CT_PT_PROT_BATCH_LIST.md) | `PERSON_ID` |
| [CT_PT_SETTINGS](CT_PT_SETTINGS.md) | `PERSON_ID` |
| [CT_REASON_DELETED](CT_REASON_DELETED.md) | `PERSON_ID` |
| [CT_USER_DOMAIN_INFO](CT_USER_DOMAIN_INFO.md) | `PERSON_ID` |
| [CUSTOM_PT_LIST_ENTRY](CUSTOM_PT_LIST_ENTRY.md) | `PERSON_ID` |
| [CV_CASE](CV_CASE.md) | `PERSON_ID` |
| [CV_PROC](CV_PROC.md) | `PERSON_ID` |
| [CV_PROC_HX](CV_PROC_HX.md) | `PERSON_ID` |
| [CV_STG_METADATA](CV_STG_METADATA.md) | `PERSON_ID` |
| [CW_DATA_CACHE](CW_DATA_CACHE.md) | `PERSON_ID` |
| [DCP_FORMS_ACTIVITY](DCP_FORMS_ACTIVITY.md) | `PERSON_ID` |
| [DCP_MP_PL_CUSTOM_ENTRY](DCP_MP_PL_CUSTOM_ENTRY.md) | `PERSON_ID` |
| [DCP_PL_CUSTOM_ENTRY](DCP_PL_CUSTOM_ENTRY.md) | `PERSON_ID` |
| [DCP_PL_PRIORITIZATION](DCP_PL_PRIORITIZATION.md) | `PERSON_ID` |
| [DCP_SHIFT_ASSIGNMENT](DCP_SHIFT_ASSIGNMENT.md) | `PERSON_ID` |
| [DCP_SHIFT_ASSIGNMENT](DCP_SHIFT_ASSIGNMENT.md) | `RELATED_PERSON_ID` |
| [DD_CONTRIBUTION](DD_CONTRIBUTION.md) | `PERSON_ID` |
| [DD_SDOC_SECTION](DD_SDOC_SECTION.md) | `PERSON_ID` |
| [DIAGNOSIS](DIAGNOSIS.md) | `PERSON_ID` |
| [DIAGNOSIS_HIST](DIAGNOSIS_HIST.md) | `PERSON_ID` |
| [DM_XNTR_JOB](DM_XNTR_JOB.md) | `PERSON_ID` |
| [DM_XNT_JOB_LOG_DTL](DM_XNT_JOB_LOG_DTL.md) | `PERSON_ID` |
| [DOCUMENT_QUALITY_REVIEW](DOCUMENT_QUALITY_REVIEW.md) | `PERSON_ID` |
| [DOC_TRANSCRIPTION_QUEUE](DOC_TRANSCRIPTION_QUEUE.md) | `PERSON_ID` |
| [DOSING_WEIGHT](DOSING_WEIGHT.md) | `PERSON_ID` |
| [DQR_DOCUMENT_ACTION](DQR_DOCUMENT_ACTION.md) | `PERSON_ID` |
| [DRG](DRG.md) | `PERSON_ID` |
| [DRG_ENCNTR_EXTENSION](DRG_ENCNTR_EXTENSION.md) | `PERSON_ID` |
| [DRG_SPECIALTY](DRG_SPECIALTY.md) | `PERSON_ID` |
| [DSM_ASSESSMENT](DSM_ASSESSMENT.md) | `PERSON_ID` |
| [DTS_TRANS_STATS](DTS_TRANS_STATS.md) | `PATIENT_ID` |
| [EEM_ABN_CHECK](EEM_ABN_CHECK.md) | `PERSON_ID` |
| [EEM_ABN_LINK](EEM_ABN_LINK.md) | `PERSON_ID` |
| [EEM_ADDRESS_DETAIL](EEM_ADDRESS_DETAIL.md) | `PERSON_ID` |
| [EEM_AUTH_DETAIL](EEM_AUTH_DETAIL.md) | `DEP_PERSON_ID` |
| [EEM_AUTH_DETAIL](EEM_AUTH_DETAIL.md) | `SUB_PERSON_ID` |
| [EEM_COVERAGE_DETAIL](EEM_COVERAGE_DETAIL.md) | `PERSON_ID` |
| [EEM_DEMOG_DETAIL](EEM_DEMOG_DETAIL.md) | `PERSON_ID` |
| [EEM_ELIG_DETAIL](EEM_ELIG_DETAIL.md) | `PAT_PERSON_ID` |
| [EEM_ELIG_DETAIL](EEM_ELIG_DETAIL.md) | `SUB_PERSON_ID` |
| [EEM_MOH_DETAIL](EEM_MOH_DETAIL.md) | `PERSON_ID` |
| [EEM_NEWBORN_DETAIL](EEM_NEWBORN_DETAIL.md) | `PERSON_ID` |
| [EEM_RX_ELIG_DETAIL](EEM_RX_ELIG_DETAIL.md) | `PERSON_ID` |
| [EEM_RX_MED_HIST_DETAIL](EEM_RX_MED_HIST_DETAIL.md) | `PERSON_ID` |
| [EHI_QUEUE_PERSON_RELTN](EHI_QUEUE_PERSON_RELTN.md) | `PERSON_ID` |
| [EI_ELIGIBLE_SERVICE](EI_ELIGIBLE_SERVICE.md) | `PERSON_ID` |
| [EI_INTERMEDHX_TRANSACTION](EI_INTERMEDHX_TRANSACTION.md) | `PERSON_ID` |
| [EKS_ADVSR_EVENT](EKS_ADVSR_EVENT.md) | `PERSON_ID` |
| [EKS_ALERT_ESCALATION](EKS_ALERT_ESCALATION.md) | `PERSON_ID` |
| [EKS_ALERT_ESC_HIST](EKS_ALERT_ESC_HIST.md) | `PERSON_ID` |
| [EKS_DLG_EVENT](EKS_DLG_EVENT.md) | `PERSON_ID` |
| [EKS_MODULE_AUDIT_DET](EKS_MODULE_AUDIT_DET.md) | `PERSON_ID` |
| [EMPI_CACHE_UPDATE_QUEUE](EMPI_CACHE_UPDATE_QUEUE.md) | `PERSON_ID` |
| [EMPI_PROCESS_LOG](EMPI_PROCESS_LOG.md) | `PERSON_ID` |
| [ENCNTR_DOMAIN](ENCNTR_DOMAIN.md) | `PERSON_ID` |
| [ENCNTR_EVENT_SET_IO](ENCNTR_EVENT_SET_IO.md) | `PERSON_ID` |
| [ENCNTR_FINANCIAL](ENCNTR_FINANCIAL.md) | `PERSON_ID` |
| [ENCNTR_FLEX_HIST](ENCNTR_FLEX_HIST.md) | `PERSON_ID` |
| [ENCNTR_PERSON_RELTN](ENCNTR_PERSON_RELTN.md) | `RELATED_PERSON_ID` |
| [ENCNTR_PLAN_RELTN](ENCNTR_PLAN_RELTN.md) | `PERSON_ID` |
| [ENCOUNTER](ENCOUNTER.md) | `PERSON_ID` |
| [EPA_RECORD](EPA_RECORD.md) | `PERSON_ID` |
| [EPISODE](EPISODE.md) | `PERSON_ID` |
| [ESI_LOG](ESI_LOG.md) | `PERSON_ID` |
| [EXAM_DATA](EXAM_DATA.md) | `PERSON_ID` |
| [EXPEDITE_MANUAL](EXPEDITE_MANUAL.md) | `PERSON_ID` |
| [EXT_DATA_GROUP](EXT_DATA_GROUP.md) | `PERSON_ID` |
| [EXT_DATA_INFO](EXT_DATA_INFO.md) | `PERSON_ID` |
| [EXT_REQ_STATUS](EXT_REQ_STATUS.md) | `PERSON_ID` |
| [FAMILY_RELATION_EXCEPTION](FAMILY_RELATION_EXCEPTION.md) | `PERSON_ID` |
| [FAMILY_RELATION_EXCEPTION](FAMILY_RELATION_EXCEPTION.md) | `SUGGESTED_RELATED_PERSON_ID` |
| [FHX_ACTIVITY](FHX_ACTIVITY.md) | `PERSON_ID` |
| [FHX_ACTIVITY](FHX_ACTIVITY.md) | `RELATED_PERSON_ID` |
| [FILL_PRINT_ORD_HX](FILL_PRINT_ORD_HX.md) | `PERSON_ID` |
| [FN_OMF_ENCNTR](FN_OMF_ENCNTR.md) | `PERSON_ID` |
| [FOLDER](FOLDER.md) | `PERSON_ID` |
| [FOREIGN_FOLDER](FOREIGN_FOLDER.md) | `PERSON_ID` |
| [GEN_LAB_EXT_DATA](GEN_LAB_EXT_DATA.md) | `PERSON_ID` |
| [GS_MED_CLAIM](GS_MED_CLAIM.md) | `PERSON_ID` |
| [HANDHELD_DETAIL](HANDHELD_DETAIL.md) | `PERSON1_ID` |
| [HANDHELD_DETAIL](HANDHELD_DETAIL.md) | `PERSON2_ID` |
| [HAPLOTYPE_CHART](HAPLOTYPE_CHART.md) | `PERSON_ID` |
| [HAPLOTYPE_DONOR](HAPLOTYPE_DONOR.md) | `PERSON_ID` |
| [HCM_COMM_EVENT](HCM_COMM_EVENT.md) | `CONTACTED_PERSON_ID` |
| [HCM_COMM_EVENT](HCM_COMM_EVENT.md) | `PERSON_ID` |
| [HCM_COMM_EVENT_H](HCM_COMM_EVENT_H.md) | `CONTACTED_PERSON_ID` |
| [HCM_COMM_EVENT_H](HCM_COMM_EVENT_H.md) | `PERSON_ID` |
| [HEALTH_CONCERN](HEALTH_CONCERN.md) | `PERSON_ID` |
| [HIM_PV_CHART](HIM_PV_CHART.md) | `PERSON_ID` |
| [HIM_PV_DOCUMENT](HIM_PV_DOCUMENT.md) | `PERSON_ID` |
| [HIM_REQUEST_CRITERIA](HIM_REQUEST_CRITERIA.md) | `PERSON_ID` |
| [HIM_REQUEST_PATIENT](HIM_REQUEST_PATIENT.md) | `PERSON_ID` |
| [HIM_UNSIGNED_ORDERS](HIM_UNSIGNED_ORDERS.md) | `PERSON_ID` |
| [HISTORY_ACTION](HISTORY_ACTION.md) | `PERSON_ID` |
| [HIS_OBSERVATION](HIS_OBSERVATION.md) | `PERSON_ID` |
| [HLA_ORDER_LOCK](HLA_ORDER_LOCK.md) | `PERSON_ID` |
| [HLA_SERA_QUERY_SERUM](HLA_SERA_QUERY_SERUM.md) | `PERSON_ID` |
| [HLA_XM_RES_TRAY](HLA_XM_RES_TRAY.md) | `DONOR_ID` |
| [HLA_X_SPECIMEN_ANALYSIS](HLA_X_SPECIMEN_ANALYSIS.md) | `PERSON_ID` |
| [HM_EXPECT_MOD](HM_EXPECT_MOD.md) | `PERSON_ID` |
| [HM_EXPECT_MOD_HIST](HM_EXPECT_MOD_HIST.md) | `PERSON_ID` |
| [HM_PERSON_NOTIFICATION](HM_PERSON_NOTIFICATION.md) | `PERSON_ID` |
| [HM_RECOMMENDATION](HM_RECOMMENDATION.md) | `PERSON_ID` |
| [HNA_EXCEPT_AUDIT](HNA_EXCEPT_AUDIT.md) | `PERSON_ID` |
| [HOLD_QUEUE](HOLD_QUEUE.md) | `PERSON_ID` |
| [IB_RX_REQ_ACTION](IB_RX_REQ_ACTION.md) | `PROPOSED_PERSON_ID` |
| [ICLASS_PERSON_RELTN](ICLASS_PERSON_RELTN.md) | `PERSON_ID` |
| [IMMUNIZATION_AUDIT](IMMUNIZATION_AUDIT.md) | `PERSON_ID` |
| [IMMUNIZATION_EXT_DATA](IMMUNIZATION_EXT_DATA.md) | `PERSON_ID` |
| [IMMUNIZATION_MODIFIER](IMMUNIZATION_MODIFIER.md) | `CONSENT_PERSON_ID` |
| [IMMUNIZATION_MODIFIER](IMMUNIZATION_MODIFIER.md) | `PERSON_ID` |
| [IMMUNIZATION_OBSERVATION](IMMUNIZATION_OBSERVATION.md) | `PERSON_ID` |
| [IMPLANT_HISTORY](IMPLANT_HISTORY.md) | `PERSON_ID` |
| [IM_U_NOTIFY](IM_U_NOTIFY.md) | `PERSON_ID` |
| [INVTN_COMMUNICATION](INVTN_COMMUNICATION.md) | `PERSON_ID` |
| [INVTN_INVITATION](INVTN_INVITATION.md) | `PERSON_ID` |
| [INVTN_INVITATION_ACTION](INVTN_INVITATION_ACTION.md) | `PERSON_ID` |
| [IO_DEVICE_INTERRUPT](IO_DEVICE_INTERRUPT.md) | `PERSON_ID` |
| [IO_TOTAL_START_TIME](IO_TOTAL_START_TIME.md) | `PERSON_ID` |
| [LAB_EXT_IDENTIFIER](LAB_EXT_IDENTIFIER.md) | `PERSON_ID` |
| [LH_CNT_IC_PATIENT_POP](LH_CNT_IC_PATIENT_POP.md) | `PERSON_ID` |
| [LH_CNT_IC_PATIENT_POP_TAGS](LH_CNT_IC_PATIENT_POP_TAGS.md) | `PERSON_ID` |
| [LH_CNT_IC_VAE](LH_CNT_IC_VAE.md) | `PERSON_ID` |
| [LH_CNT_LTD_DATA](LH_CNT_LTD_DATA.md) | `PERSON_ID` |
| [LH_CNT_PATIENT_EXTENSION](LH_CNT_PATIENT_EXTENSION.md) | `PERSON_ID` |
| [LH_CNT_READMIT_WORKLIST](LH_CNT_READMIT_WORKLIST.md) | `PERSON_ID` |
| [LH_CNT_WL_POP](LH_CNT_WL_POP.md) | `PERSON_ID` |
| [LH_CNT_WL_POP_H](LH_CNT_WL_POP_H.md) | `PERSON_ID` |
| [LINE_ITEM](LINE_ITEM.md) | `PERSON_ID` |
| [MAMMO_STUDY](MAMMO_STUDY.md) | `PERSON_ID` |
| [MARS_SUITE_RESPONSE](MARS_SUITE_RESPONSE.md) | `PERSON_ID` |
| [MEDIA_ENCNTR_RELTN](MEDIA_ENCNTR_RELTN.md) | `PERSON_ID` |
| [MEDIA_EXAM](MEDIA_EXAM.md) | `PERSON_ID` |
| [MEDIA_MASTER](MEDIA_MASTER.md) | `PERSON_ID` |
| [MED_ADMIN_INGREDIENT_META](MED_ADMIN_INGREDIENT_META.md) | `PERSON_ID` |
| [MED_ADMIN_MED_ERROR](MED_ADMIN_MED_ERROR.md) | `PERSON_ID` |
| [MED_ADMIN_PT_ERROR](MED_ADMIN_PT_ERROR.md) | `EXPECTED_PT_ID` |
| [MED_ADMIN_PT_ERROR](MED_ADMIN_PT_ERROR.md) | `IDENTIFIED_PT_ID` |
| [MED_ADMIN_RECORD](MED_ADMIN_RECORD.md) | `PERSON_ID` |
| [MED_HISTORY_AUDIT](MED_HISTORY_AUDIT.md) | `PERSON_ID` |
| [MED_HISTORY_STATUS](MED_HISTORY_STATUS.md) | `PERSON_ID` |
| [MESSAGING_AUDIT](MESSAGING_AUDIT.md) | `PERSON_ID` |
| [MESSAGING_FAVORITES](MESSAGING_FAVORITES.md) | `PERSON_ID` |
| [MESSAGING_NOTIFY](MESSAGING_NOTIFY.md) | `ASSIGN_PERSON_ID` |
| [MIC_ACT_ANG_SUM_RPT](MIC_ACT_ANG_SUM_RPT.md) | `PERSON_ID` |
| [MIC_EXT_DATA](MIC_EXT_DATA.md) | `PERSON_ID` |
| [MIC_IC_ORDERS](MIC_IC_ORDERS.md) | `PERSON_ID` |
| [MIC_STAT_ORDER](MIC_STAT_ORDER.md) | `PERSON_ID` |
| [MM_SUPPLY_CABINET](MM_SUPPLY_CABINET.md) | `PERSON_ID` |
| [MM_TRANS_HEADER](MM_TRANS_HEADER.md) | `TRANS_PERSON_ID` |
| [MM_TRANS_LINE](MM_TRANS_LINE.md) | `PATIENT_ID` |
| [MP_NOTIFICATION](MP_NOTIFICATION.md) | `PERSON_ID` |
| [MP_PRIMED_VIEW_ACT](MP_PRIMED_VIEW_ACT.md) | `PERSON_ID` |
| [MP_PRIMED_VIEW_POP](MP_PRIMED_VIEW_POP.md) | `PERSON_ID` |
| [NC_CHARTED_SECTION](NC_CHARTED_SECTION.md) | `PATIENT_ID` |
| [NC_CHARTED_VIEW](NC_CHARTED_VIEW.md) | `PATIENT_ID` |
| [NOMENCLATURE_ENCNTR_DESC](NOMENCLATURE_ENCNTR_DESC.md) | `PERSON_ID` |
| [NOMEN_ENTITY_RELTN](NOMEN_ENTITY_RELTN.md) | `PERSON_ID` |
| [OMF_ABSTRACT_DATA_ST](OMF_ABSTRACT_DATA_ST.md) | `PERSON_ID` |
| [OMF_ABST_CODING_RELTN_ST](OMF_ABST_CODING_RELTN_ST.md) | `PERSON_ID` |
| [OMF_CHARGE_ST](OMF_CHARGE_ST.md) | `PERSON_ID` |
| [OMF_CLINICAL_EVENT_ST](OMF_CLINICAL_EVENT_ST.md) | `PERSON_ID` |
| [OMF_ENCNTR_ST](OMF_ENCNTR_ST.md) | `OTHER_INS_PERSON_ID` |
| [OMF_ENCNTR_ST](OMF_ENCNTR_ST.md) | `PERSON_ID` |
| [OMF_ENCNTR_ST](OMF_ENCNTR_ST.md) | `PRIM_INS_PERSON_ID` |
| [OMF_ENCNTR_ST](OMF_ENCNTR_ST.md) | `SEC_INS_PERSON_ID` |
| [OMF_ENCNTR_TYPE_HIST_ST](OMF_ENCNTR_TYPE_HIST_ST.md) | `PERSON_ID` |
| [OMF_ORDER_ST](OMF_ORDER_ST.md) | `PERSON_ID` |
| [OMF_POSTED_CHARGE_ST](OMF_POSTED_CHARGE_ST.md) | `PERSON_ID` |
| [OMF_PRSNL_PAYPERIOD_ST](OMF_PRSNL_PAYPERIOD_ST.md) | `PERSON_ID` |
| [OMF_PRSNL_TIMEDATE_ST](OMF_PRSNL_TIMEDATE_ST.md) | `PERSON_ID` |
| [OMF_RADMGMT_ORDER_ST](OMF_RADMGMT_ORDER_ST.md) | `PATIENT_ID` |
| [ONC_ADHOC_PLAN](ONC_ADHOC_PLAN.md) | `PERSON_ID` |
| [ONC_FORM_ACTIVITY](ONC_FORM_ACTIVITY.md) | `PERSON_ID` |
| [ONC_II_AUTO_ACTIVITY](ONC_II_AUTO_ACTIVITY.md) | `PERSON_ID` |
| [ONC_INFUSION_ACTIVITY](ONC_INFUSION_ACTIVITY.md) | `PERSON_ID` |
| [ONC_TC_CAL_ITEMS](ONC_TC_CAL_ITEMS.md) | `PERSON_ID` |
| [ORDERS](ORDERS.md) | `PERSON_ID` |
| [ORDER_DAILY_REVIEW_RSPNL](ORDER_DAILY_REVIEW_RSPNL.md) | `PERSON_ID` |
| [ORDER_DISPENSE](ORDER_DISPENSE.md) | `PERSON_ID` |
| [ORDER_PROPOSAL](ORDER_PROPOSAL.md) | `PERSON_ID` |
| [ORDER_RADIOLOGY](ORDER_RADIOLOGY.md) | `PERSON_ID` |
| [ORDER_RECON](ORDER_RECON.md) | `PERSON_ID` |
| [ORDER_RX_SCRATCHPAD](ORDER_RX_SCRATCHPAD.md) | `PERSON_ID` |
| [ORDER_STAGING](ORDER_STAGING.md) | `PERSON_ID` |
| [ORDER_TRACKING_WORKLIST](ORDER_TRACKING_WORKLIST.md) | `PATIENT_ID` |
| [ORM_ERROR_LOG](ORM_ERROR_LOG.md) | `PERSON_ID` |
| [ORM_ORD_HIST_SNAPSHOT](ORM_ORD_HIST_SNAPSHOT.md) | `PATIENT_ID` |
| [OUTCOME_ACTIVITY](OUTCOME_ACTIVITY.md) | `PERSON_ID` |
| [PASSIVE_ALERT](PASSIVE_ALERT.md) | `PERSON_ID` |
| [PATHOLOGY_CASE](PATHOLOGY_CASE.md) | `PERSON_ID` |
| [PATHWAY](PATHWAY.md) | `PERSON_ID` |
| [PATIENT_CASE](PATIENT_CASE.md) | `PERSON_ID` |
| [PATIENT_DISPENSE](PATIENT_DISPENSE.md) | `PERSON_ID` |
| [PATIENT_EVENT](PATIENT_EVENT.md) | `PERSON_ID` |
| [PAT_ED_DOCUMENT](PAT_ED_DOCUMENT.md) | `PERSON_ID` |
| [PCA_ENCNTR_MEASURE_OUTCOME](PCA_ENCNTR_MEASURE_OUTCOME.md) | `PERSON_ID` |
| [PCA_ENCNTR_TOPIC_RELTN](PCA_ENCNTR_TOPIC_RELTN.md) | `PERSON_ID` |
| [PCA_PERSON_MEASURE_OUTCOME](PCA_PERSON_MEASURE_OUTCOME.md) | `PERSON_ID` |
| [PCA_PERSON_TOPIC_RELTN](PCA_PERSON_TOPIC_RELTN.md) | `PERSON_ID` |
| [PCT_IPASS](PCT_IPASS.md) | `PERSON_ID` |
| [PDOC_AUTOSAVE](PDOC_AUTOSAVE.md) | `PATIENT_ID` |
| [PERSON_ABORH](PERSON_ABORH.md) | `PERSON_ID` |
| [PERSON_ABORH_RESULT](PERSON_ABORH_RESULT.md) | `PERSON_ID` |
| [PERSON_ALIAS](PERSON_ALIAS.md) | `PERSON_ID` |
| [PERSON_ALIAS_HIST](PERSON_ALIAS_HIST.md) | `PERSON_ID` |
| [PERSON_ANTIBODY](PERSON_ANTIBODY.md) | `PERSON_ID` |
| [PERSON_ANTIGEN](PERSON_ANTIGEN.md) | `PERSON_ID` |
| [PERSON_CODE_VALUE_R](PERSON_CODE_VALUE_R.md) | `PERSON_ID` |
| [PERSON_CODE_VALUE_R_HIST](PERSON_CODE_VALUE_R_HIST.md) | `PERSON_ID` |
| [PERSON_COMBINE](PERSON_COMBINE.md) | `FROM_PERSON_ID` |
| [PERSON_COMBINE](PERSON_COMBINE.md) | `TO_PERSON_ID` |
| [PERSON_COMBINE_BATCH](PERSON_COMBINE_BATCH.md) | `FROM_PERSON_ID` |
| [PERSON_COMBINE_BATCH](PERSON_COMBINE_BATCH.md) | `TO_PERSON_ID` |
| [PERSON_DATA_NOT_COLL](PERSON_DATA_NOT_COLL.md) | `PERSON_ID` |
| [PERSON_DESIGNATION](PERSON_DESIGNATION.md) | `PERSON_ID` |
| [PERSON_DISMISSAL](PERSON_DISMISSAL.md) | `PERSON_ID` |
| [PERSON_FLEX_HIST](PERSON_FLEX_HIST.md) | `PERSON_ID` |
| [PERSON_HLA_AB_SCN_AUDIT](PERSON_HLA_AB_SCN_AUDIT.md) | `PERSON_ID` |

_… and 186 more (see `data/foreign_keys.jsonl`)._

