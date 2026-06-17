# PROT_MASTER

> Table stores information about protocols

**Description:** Protocol Master  
**Table type:** REFERENCE  
**Primary key:** `PROT_MASTER_ID`  
**Columns:** 33  
**Referenced by:** 22 columns

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ACCESSION_NBR_LAST` | DOUBLE | NOT NULL |  | this value holds the last acession number(order of enrollment) that was used to enroll patients on this protocol |
| 2 | `ACCESSION_NBR_PREFIX` | VARCHAR(255) |  |  | the prefix added to all acession numbers for enrollments on this protocol |
| 3 | `ACCESSION_NBR_SIG_DIG` | DOUBLE | NOT NULL |  | Number of significant digits in the accession number for enrollments on this protocol |
| 4 | `BEG_EFFECTIVE_DT_TM` | DATETIME | NOT NULL |  | The date and time for which this table row becomes effective. Normally, this will be the date and time the row is added, but could be a past or future date and time. |
| 5 | `COLLAB_SITE_ORG_ID` | DOUBLE | NOT NULL | FK→ | Collaborating Site Organization for the protocol. |
| 6 | `DISPLAY_IND` | DOUBLE | NOT NULL |  | This field is an indicator that tells whether the protocol enrollment information for this protocol will be displayed in the electronic medical record. |
| 7 | `END_EFFECTIVE_DT_TM` | DATETIME | NOT NULL |  | The date/time after which the row is no longer valid as active current data. This may be valued with the date that the row became inactive. |
| 8 | `INITIATING_SERVICE_CD` | DOUBLE | NOT NULL |  | This field contains a code for the service that is sponsoring (initiating) the protocol/study. Examples of a service would include, but not be limited to, Leukemia, Solid Tumor, After Completion of Therapy (ACT), Psychology, Department of Infectious Diseases, etc. |
| 9 | `INITIATING_SERVICE_DESC` | VARCHAR(255) |  |  | Free text description of the Initiating service |
| 10 | `LOGICAL_DOMAIN_ID` | DOUBLE | NOT NULL | FK→ | The unique identifier for a logical domain. This identifier allows the data to be grouped by logical domain. For example, If you assign clients a logical_domain_id this would allow you to store data for multiple clients on this table. |
| 11 | `NETWORK_FLAG` | DOUBLE | NOT NULL |  | A flag to determine if a protocol came from Research Network (0 = did not come from Research Network, 1 = came from Research Network but now a PowerTrials protocol, 2 = came from Research Network and still in Research Network) |
| 12 | `PARENT_PROT_MASTER_ID` | DOUBLE | NOT NULL | FK→ | The parent_prot_master_id is the PK of the protocol that is the parent. |
| 13 | `PARTICIPATION_TYPE_CD` | DOUBLE | NOT NULL |  | Indicates the type of participation of the organization on the protocol .. examples include Institution only, Cooperative group study, Clinical Practice study etc. |
| 14 | `PEER_REVIEW_INDICATOR_CD` | DOUBLE | NOT NULL |  | This field contains a code that indicates if the protocol undergoes peer review. |
| 15 | `PRESCREEN_TYPE_FLAG` | DOUBLE | NOT NULL |  | Type of prescreening associated with the protocol. 0 = Discern 1 = HE RuleBuilder |
| 16 | `PREV_PROT_MASTER_ID` | DOUBLE | NOT NULL | FK→ | The ORIGINAL value of prot_master_id used for grouping the related versions. Required for Type 2 Versioning methodology. |
| 17 | `PRIMARY_MNEMONIC` | VARCHAR(255) |  |  | Mnemonic assigned to the protocol |
| 18 | `PRIMARY_MNEMONIC_KEY` | VARCHAR(255) |  |  | Mnemonic of the protocol stripped of special characters |
| 19 | `PROGRAM_CD` | DOUBLE | NOT NULL |  | This field contains a code identifying the program that is sponsoring the protocol/study. Examples of programs would include, but not be limited to, be Hematologic Malignancy, Solid Malignancy, Transplantation and Gene Therapy, Neurobiology, Infectious Disease and Brain Tumors, etc. |
| 20 | `PROT_MASTER_ID` | DOUBLE | NOT NULL | PK | Primary Key |
| 21 | `PROT_PHASE_CD` | DOUBLE | NOT NULL |  | This field contains a code for the phase of the protocol. Examples of phases would include, but not be limited to, phase 1, phase 1A, phase 1B, phase 2, phase 3, etc. |
| 22 | `PROT_PURPOSE_CD` | DOUBLE | NOT NULL |  | This field contains a code identifying the purpose for the protocol/study. Examples of purposes would include, but not be limited to, cancer control, epidemiology, etc. |
| 23 | `PROT_STATUS_CD` | DOUBLE | NOT NULL |  | This field contains a code identifying the status of the protocol/study: approved, open, suspended (temporarily closed to accrual), closed to accrual, closed and terminated. |
| 24 | `PROT_TYPE_CD` | DOUBLE | NOT NULL |  | This field contains a code identifying the type of protocol; therapeutic, non-therapeutic, BCM guidelines etc. |
| 25 | `RESEARCH_SPONSOR_ORG_ID` | DOUBLE | NOT NULL | FK→ | This field uniquely identifies a row in the organization table. This field contains the organization_id from the organization for the primary research sponsor. For this purpose, a research sponsor can be another hospital, research institute, drug company, government agency, etc. |
| 26 | `SCREENER_IND` | DOUBLE | NOT NULL |  | An indicator to determine if a protocol originated from screener (0 = created from powertrials, 1 = created from screener ) |
| 27 | `SUB_INITIATING_SERVICE_CD` | DOUBLE | NOT NULL |  | This field contains a code for the service that is sub sponsoring (sub initiating) the protocol/study. |
| 28 | `SUB_INITIATING_SERVICE_DESC` | VARCHAR(255) |  |  | Free text description of the sub initiating service. |
| 29 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 30 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 31 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 32 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 33 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `COLLAB_SITE_ORG_ID` | [ORGANIZATION](ORGANIZATION.md) | `ORGANIZATION_ID` |
| `LOGICAL_DOMAIN_ID` | [LOGICAL_DOMAIN](LOGICAL_DOMAIN.md) | `LOGICAL_DOMAIN_ID` |
| `PARENT_PROT_MASTER_ID` | [PROT_MASTER](PROT_MASTER.md) | `PROT_MASTER_ID` |
| `PREV_PROT_MASTER_ID` | [PROT_MASTER](PROT_MASTER.md) | `PROT_MASTER_ID` |
| `RESEARCH_SPONSOR_ORG_ID` | [ORGANIZATION](ORGANIZATION.md) | `ORGANIZATION_ID` |

## Referenced by (22)

| From table | Column |
|------------|--------|
| [CONTRIBUTING_DEPT](CONTRIBUTING_DEPT.md) | `PROT_MASTER_ID` |
| [CT_PROT_CONFIG_VALUE](CT_PROT_CONFIG_VALUE.md) | `PROT_MASTER_ID` |
| [CT_PROT_MILESTONES](CT_PROT_MILESTONES.md) | `PROT_MASTER_ID` |
| [CT_PROT_PRESCREEN_JOB_INFO](CT_PROT_PRESCREEN_JOB_INFO.md) | `PROT_MASTER_ID` |
| [CT_PROT_REASON_DELETED](CT_PROT_REASON_DELETED.md) | `PARENT_PROT_MASTER_ID` |
| [CT_PT_PROT_BATCH_LIST](CT_PT_PROT_BATCH_LIST.md) | `PROT_MASTER_ID` |
| [CT_REASON_DELETED](CT_REASON_DELETED.md) | `PROT_MASTER_ID` |
| [CT_RN_PROT_CONFIG](CT_RN_PROT_CONFIG.md) | `PROT_MASTER_ID` |
| [CT_RN_PROT_RUN](CT_RN_PROT_RUN.md) | `PROT_MASTER_ID` |
| [CT_USER_PREFERENCE](CT_USER_PREFERENCE.md) | `PROT_MASTER_ID` |
| [PEER_REVIEWER](PEER_REVIEWER.md) | `PROT_MASTER_ID` |
| [PROT_ALIAS](PROT_ALIAS.md) | `PROT_MASTER_ID` |
| [PROT_AMENDMENT](PROT_AMENDMENT.md) | `PROT_MASTER_ID` |
| [PROT_CRPC_BILLING](PROT_CRPC_BILLING.md) | `PROT_MASTER_ID` |
| [PROT_CRPC_BILL_MODIFIER](PROT_CRPC_BILL_MODIFIER.md) | `PROT_MASTER_ID` |
| [PROT_MASTER](PROT_MASTER.md) | `PARENT_PROT_MASTER_ID` |
| [PROT_MASTER](PROT_MASTER.md) | `PREV_PROT_MASTER_ID` |
| [PROT_REGULATORY_REQ](PROT_REGULATORY_REQ.md) | `PROT_MASTER_ID` |
| [PT_PROT_PRESCREEN](PT_PROT_PRESCREEN.md) | `PROT_MASTER_ID` |
| [PT_PROT_PRESCREEN_TEST](PT_PROT_PRESCREEN_TEST.md) | `PROT_MASTER_ID` |
| [PT_PROT_REG](PT_PROT_REG.md) | `PROT_MASTER_ID` |
| [PW_PT_RELTN](PW_PT_RELTN.md) | `PROT_MASTER_ID` |

