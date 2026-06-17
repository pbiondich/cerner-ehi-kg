# DD_SREF_SECTION

> Contains the candidate sections which structured documentation reference templates may target.

**Description:** Dynamic Documentation Structured Reference Section  
**Table type:** REFERENCE  
**Primary key:** `DD_SREF_SECTION_ID`  
**Columns:** 10  
**Referenced by:** 2 columns

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `CONCEPT_CKI` | VARCHAR(255) | NOT NULL |  | Conceptual identifier of this section within Cerner systems. |
| 2 | `DD_SREF_SECTION_ID` | DOUBLE | NOT NULL | PK | Uniquely identifies a candidate section which structured documentation reference templates may target. |
| 3 | `DISPLAY` | VARCHAR(255) |  |  | The display name for this section, if necessary to present to a user. |
| 4 | `DISPLAY_KEY` | VARCHAR(255) |  |  | The key used for display lookup. |
| 5 | `MERGE_TEMPLATE_IND` | DOUBLE | NOT NULL |  | Indication of whether this section should have its templates merged together when being documented, or if they should remain un-merged so that they can be documented independently. For example, a Physical Exam section would have merge_template_ind = 1 so that you only document answers once for an exam, across all templates. But History of Present Illness section would have merge_template_ind = 0,so multiple independent templates all contribute to the final output for a single section. |
| 6 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 7 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 8 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 9 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 10 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Referenced by (2)

| From table | Column |
|------------|--------|
| [DD_SDOC_SECTION](DD_SDOC_SECTION.md) | `DD_SREF_SECTION_ID` |
| [DD_SREF_TEMPLATE](DD_SREF_TEMPLATE.md) | `DD_SREF_SECTION_ID` |

