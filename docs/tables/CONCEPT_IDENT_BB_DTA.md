# CONCEPT_IDENT_BB_DTA

> Stores reference data linking unique blood bank discrete task assays with concept identifier codes (LOINC).

**Description:** Concept Identifier Blood Bank Discrete Task Assays  
**Table type:** REFERENCE  
**Primary key:** _(not published — see note)_  
**Columns:** 16

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ACTIVE_IND` | DOUBLE | NOT NULL |  | The table row is active or inactive. A row is generally active unless it is in an inactive state such as logically deleted, combined away, pending purge, etc. |
| 2 | `ACTIVE_STATUS_CD` | DOUBLE | NOT NULL |  | Indicates the status of the row itself (not the data in the row) such as active, inactive, combined away, pending purge, etc. |
| 3 | `ACTIVE_STATUS_DT_TM` | DATETIME | NOT NULL |  | The date and time that the active_status_cd was set. |
| 4 | `ACTIVE_STATUS_PRSNL_ID` | DOUBLE | NOT NULL |  | The person who caused the active_status_cd to be set or change. |
| 5 | `BEG_EFFECTIVE_DT_TM` | DATETIME | NOT NULL |  | The date and time for which this table row becomes effective. Normally, this will be the date and time the row is added, but could be a past or future date and time. |
| 6 | `CONCEPT_CKI` | VARCHAR(255) |  | FK→ | The concept identifier. Used to link to the nomenclature row containing additional information about the concept identifier. |
| 7 | `CONCEPT_IDENT_BB_DTA_ID` | DOUBLE | NOT NULL |  | Uniquely identifies data linking unique blood bank discrete task assays with concept identifier codes (LOINC). |
| 8 | `CONCEPT_TYPE_FLAG` | DOUBLE | NOT NULL |  | Identifies the type of concept identifier associated to the code value. 1 = LOINC Analyte Code 2 = LOINC Attachment Code |
| 9 | `END_EFFECTIVE_DT_TM` | DATETIME | NOT NULL |  | The date/time after which the row is no longer valid as active current data. This may be valued with the date that the row became inactive. |
| 10 | `IGNORE_IND` | DOUBLE | NOT NULL |  | Identifies that the row will be ignored by the LOINC service. |
| 11 | `TASK_ASSAY_CD` | DOUBLE | NOT NULL |  | A task assay code that identifies the assay associated with the concept identifier. |
| 12 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 13 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 14 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 15 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 16 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `CONCEPT_CKI` | [CMT_CONCEPT](CMT_CONCEPT.md) | `CONCEPT_CKI` |

