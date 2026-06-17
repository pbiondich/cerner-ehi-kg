# CONCEPT_IDENT_MIC_RPT

> Stores reference data linking unique microbiology report and source combinations with concept identifier codes (LOINC).

**Description:** Concept Identifier Micro Report  
**Table type:** REFERENCE  
**Primary key:** _(not published — see note)_  
**Columns:** 20

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ACTIVE_IND` | DOUBLE | NOT NULL |  | The table row is active or inactive. A row is generally active unless it is in an inactive state such as logically deleted, combined away, pending purge, etc. |
| 2 | `ACTIVE_STATUS_CD` | DOUBLE | NOT NULL |  | Indicates the status of the row itself (not the data in the row) such as active, inactive, combined away, pending purge, etc. |
| 3 | `ACTIVE_STATUS_DT_TM` | DATETIME | NOT NULL |  | The date and time that the active_status_cd was set. |
| 4 | `ACTIVE_STATUS_PRSNL_ID` | DOUBLE | NOT NULL |  | The person who caused the active_status_cd to be set or change. |
| 5 | `BEG_EFFECTIVE_DT_TM` | DATETIME | NOT NULL |  | The date and time for which this table row becomes effective. Normally, this will be the date and time the row is added, but could be a past or future date and time. |
| 6 | `CATALOG_CD` | DOUBLE | NOT NULL |  | A code value that identifies the specific microbiology order catalog item associated with the concept identifier. |
| 7 | `CONCEPT_CKI` | VARCHAR(255) |  | FK→ | The concept identifier. Used to link to the nomenclaure row containing additional information about the concept identifier. |
| 8 | `CONCEPT_IDENT_MIC_RPT_ID` | DOUBLE | NOT NULL |  | Uniquely identifies data linking a microbiology report and source combinations with concept identifier codes (LOINC). |
| 9 | `CONCEPT_TYPE_FLAG` | DOUBLE | NOT NULL |  | Identifies the type of concept identifier associated to the antibiotic and susceptibility method. 1 = LOINC Analyte Code 2 - LOINC Attachment Code |
| 10 | `END_EFFECTIVE_DT_TM` | DATETIME | NOT NULL |  | The date/time after which the row is no longer valid as active current data. This may be valued with the date that the row became inactive. |
| 11 | `IGNORE_IND` | DOUBLE | NOT NULL |  | Identifies that the row will be ignored by the LOINC service. |
| 12 | `ORG_CLASS_FLAG` | DOUBLE | NOT NULL |  | Identifies the organism type associated with the concept identifier. 0 - N/A 1 - Bacteria 2 - Mycobacteria 3 - Fungus 4 - Parasite 5 - Virus 6 - Yeast |
| 13 | `SERVICE_RESOURCE_CD` | DOUBLE | NOT NULL |  | A code value that identifies the specific microbiology service resource associated witth the concept identifier If the row is for a LOINC Analyte code, a service_resource_cd = 0.0 indicates all service resources. |
| 14 | `SOURCE_CD` | DOUBLE | NOT NULL |  | A code value that identifies the specific microbiology source/specimen type associated with the concept identifier. |
| 15 | `TASK_CD` | DOUBLE | NOT NULL |  | A code value that identifies the specific microbiology stain report task associated with the concept identifier. If the row is for a LOINC Analyte code a task_cd = 0.0 indicates a non-stain report. |
| 16 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 17 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 18 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 19 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 20 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `CONCEPT_CKI` | [CMT_CONCEPT](CMT_CONCEPT.md) | `CONCEPT_CKI` |

