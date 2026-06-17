# PROT_AMENDMENT

> This table contains information about all amendments to a protocol

**Description:** PROT AMENDMENT  
**Table type:** REFERENCE  
**Primary key:** `PROT_AMENDMENT_ID`  
**Columns:** 32  
**Referenced by:** 26 columns

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ACCRUAL_REQUIRED_INDC_CD` | DOUBLE | NOT NULL |  | This field contains a code indicating whether accrual figures are required for this protocol |
| 2 | `AMENDMENT_DESCRIPTION` | VARCHAR(255) |  |  | This field contains a description of the amendment. |
| 3 | `AMENDMENT_DT_TM` | DATETIME | NOT NULL |  | This field contains the date and time the amendment was approved. |
| 4 | `AMENDMENT_NBR` | DOUBLE | NOT NULL |  | This field contains the amendment sequence number (0 - initial protocol, 1 - first amendment, 2 - second amendment, 3 - third amendment, etc.). |
| 5 | `AMENDMENT_STATUS_CD` | DOUBLE | NOT NULL |  | Indicates the status of the amendment |
| 6 | `ANTICIPATED_PROT_DURATION` | DOUBLE | NOT NULL |  | Obsolete. This column has been replaced by new column ANTICIPATED_PROT_DUR_VALUE in order to support decimal values. |
| 7 | `ANTICIPATED_PROT_DUR_UOM_CD` | DOUBLE | NOT NULL |  | This field contains the code for the time units in which the anticipated protocol duration is expressed. Normally, this code would represent years or months. |
| 8 | `ANTICIPATED_PROT_DUR_VALUE` | DOUBLE | NOT NULL |  | This column replaces ANTICIPATED_PROT_DURATION. This new column will be defined an an F8 datatype for CCL in order to allow for decimal values. This field contains the anticipated duration of the protocol. The old column will be obsoleted. |
| 9 | `COMPENSATION_DESCRIPTION` | VARCHAR(255) |  |  | Free text description of the compensation to be received by patients enrolled on the amendment |
| 10 | `COMPENSATION_IND` | DOUBLE | NOT NULL |  | An Indicator to specify if there is compensation connected to this amendment. |
| 11 | `CT_DOMAIN_INFO_ID` | DOUBLE | NOT NULL | FK→ | The domain related to the amendment from the CT_DOMAIN_INFO table |
| 12 | `DATA_CAPTURE_IND` | DOUBLE | NOT NULL |  | Indicates if the amendment has data capture turned on or off. |
| 13 | `DATA_SCRIPT_CD` | DOUBLE | NOT NULL |  | The code value that points to the script that collects data for the protocol for integrate data capture. |
| 14 | `DCV_AUTO_ENROLL_IND` | DOUBLE | NOT NULL |  | This column indicates if the amendment has Discovere auto enrollment turned on or off. |
| 15 | `ENROLL_STRATIFICATION_TYPE_CD` | DOUBLE | NOT NULL |  | Indicates the stratification type of the amendment |
| 16 | `GROUPWIDE_TARGETED_ACCRUAL` | DOUBLE |  |  | This field contains the number of patients that the protocol would like to have enrolled in the protocol. This figure includes the enrollment from all collaborating groups. |
| 17 | `OTHER_APPLICABLE_PROT_IND` | DOUBLE |  |  | Indicates if this protocol targets patients who are currently eligible for treatment on other open/planned protocols |
| 18 | `PARENT_AMENDMENT_ID` | DOUBLE | NOT NULL | FK→ | The parent_amendment_id is the PK of the amendment a revision is for. |
| 19 | `PARTICIPATION_TYPE_CD` | DOUBLE | NOT NULL |  | Indicates the type of participation of the organizsation in the amendment. Examples include Institution only, cooperative group etc. |
| 20 | `PROT_AMENDMENT_ID` | DOUBLE | NOT NULL | PK | Primary Key |
| 21 | `PROT_MASTER_ID` | DOUBLE | NOT NULL | FK→ | Uniquely identifies the protocol to which this amendment is attached |
| 22 | `PROT_TITLE` | VARCHAR(2000) | NOT NULL |  | This field contains the title (name) of the protocol. |
| 23 | `REVISION_IND` | DOUBLE | NOT NULL |  | Indicates whether the amendment is a revision or not. |
| 24 | `REVISION_NBR_TXT` | VARCHAR(30) |  |  | Alphanumeric revision number for the revision. |
| 25 | `REVISION_SEQ` | DOUBLE | NOT NULL |  | Sequence the revision comes in after the amendment. |
| 26 | `SAFETY_MONITOR_COMMITTEE_IND` | DOUBLE |  |  | Indicator to specify if there is a safety committee connected to this amendment |
| 27 | `TARGETED_ACCRUAL` | DOUBLE |  |  | This field contains the number of patients that the protocol would like to have enrolled in the protocol from the coordinating institution. |
| 28 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 29 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 30 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 31 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 32 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `CT_DOMAIN_INFO_ID` | [CT_DOMAIN_INFO](CT_DOMAIN_INFO.md) | `CT_DOMAIN_INFO_ID` |
| `PARENT_AMENDMENT_ID` | [PROT_AMENDMENT](PROT_AMENDMENT.md) | `PROT_AMENDMENT_ID` |
| `PROT_MASTER_ID` | [PROT_MASTER](PROT_MASTER.md) | `PROT_MASTER_ID` |

## Referenced by (26)

| From table | Column |
|------------|--------|
| [AMENDMENT_REASON](AMENDMENT_REASON.md) | `PROT_AMENDMENT_ID` |
| [APPL_DISEASE](APPL_DISEASE.md) | `PROT_AMENDMENT_ID` |
| [CT_DOCUMENT](CT_DOCUMENT.md) | `PROT_AMENDMENT_ID` |
| [CT_MILESTONES](CT_MILESTONES.md) | `PROT_AMENDMENT_ID` |
| [CT_PROT_AMD_CUSTOM_FLD_VAL](CT_PROT_AMD_CUSTOM_FLD_VAL.md) | `PROT_AMENDMENT_ID` |
| [CT_PT_AMD_ASSIGNMENT](CT_PT_AMD_ASSIGNMENT.md) | `PROT_AMENDMENT_ID` |
| [CT_PT_AMD_ASSIGNMENT](CT_PT_AMD_ASSIGNMENT.md) | `TRANSFER_CHECKED_AMENDMENT_ID` |
| [DATA_SUBMISSION](DATA_SUBMISSION.md) | `PROT_AMENDMENT_ID` |
| [ENTITY_ACCESS](ENTITY_ACCESS.md) | `PROT_AMENDMENT_ID` |
| [INVEST_AGENT_DEV](INVEST_AGENT_DEV.md) | `PROT_AMENDMENT_ID` |
| [PROT_AMD_COMMITTEE_RELTN](PROT_AMD_COMMITTEE_RELTN.md) | `PROT_AMENDMENT_ID` |
| [PROT_AMENDMENT](PROT_AMENDMENT.md) | `PARENT_AMENDMENT_ID` |
| [PROT_ARM](PROT_ARM.md) | `PROT_AMENDMENT_ID` |
| [PROT_ELIG_QUEST](PROT_ELIG_QUEST.md) | `PROT_AMENDMENT_ID` |
| [PROT_GRANT_SPONSOR](PROT_GRANT_SPONSOR.md) | `PROT_AMENDMENT_ID` |
| [PROT_MODALITY](PROT_MODALITY.md) | `PROT_AMENDMENT_ID` |
| [PROT_OBJECTIVE](PROT_OBJECTIVE.md) | `PROT_AMENDMENT_ID` |
| [PROT_QUESTIONNAIRE](PROT_QUESTIONNAIRE.md) | `PROT_AMENDMENT_ID` |
| [PROT_ROLE](PROT_ROLE.md) | `PROT_AMENDMENT_ID` |
| [PROT_STRATUM](PROT_STRATUM.md) | `PROT_AMENDMENT_ID` |
| [PROT_SUSPENSION](PROT_SUSPENSION.md) | `PROT_AMENDMENT_ID` |
| [PT_CONSENT](PT_CONSENT.md) | `PROT_AMENDMENT_ID` |
| [PT_ELIG_RESULT](PT_ELIG_RESULT.md) | `PROT_AMENDMENT_ID` |
| [PT_ELIG_TRACKING](PT_ELIG_TRACKING.md) | `PROT_AMENDMENT_ID` |
| [REVISION](REVISION.md) | `PROT_AMENDMENT_ID` |
| [SAFETY_COMMITTEE](SAFETY_COMMITTEE.md) | `PROT_AMENDMENT_ID` |

