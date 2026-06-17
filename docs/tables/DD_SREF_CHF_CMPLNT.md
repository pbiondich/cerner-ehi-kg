# DD_SREF_CHF_CMPLNT

> This table is a starting point for identifying a structured documentation reference template to use for a patient's chief complaint, when that complaint is coded in a standard terminology such as SNOMED-CT. Many code values may point to the same template, so this table maps many of its rows to a single row on DD_SREF_CHF_CMPLNT_CRIT.

**Description:** Dynamic Documentation - Structured Reference Chief Complaint  
**Table type:** REFERENCE  
**Primary key:** _(not published — see note)_  
**Columns:** 8

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `CONCEPT_CKI` | VARCHAR(255) |  |  | The concept_cki that this complaint is associated with. SNOMED!440028005 for example. Intended as a way to identify chief complaints based on industry standard vocabularies. |
| 2 | `DD_SREF_CHF_CMPLNT_ID` | DOUBLE | NOT NULL |  | This table is a starting point for identifying a structured documentation reference template to use for a patient's chief complaint is coded in a standard terminology such as SNOMED-CT. Many code values may point to the same template, so this table maps many of its rows to a single row on DD_SREF_CHF_CMPLNT_CRIT. |
| 3 | `OCID_IDENT` | VARCHAR(255) | NOT NULL |  | The chief complaint concept that should be used to identify criteria to evaluate further for a match to the CONCEPT_CKI identified in this row. This is an internal (non-industry standard) id to identify a group of criteria to evaluate. |
| 4 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 5 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 6 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 7 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 8 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

