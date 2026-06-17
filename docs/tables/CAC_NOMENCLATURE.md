# CAC_NOMENCLATURE

> Stores nomenclatures and related information found during document parsing

**Description:** Computer Assisted Coding Nomenclature  
**Table type:** ACTIVITY  
**Primary key:** _(not published — see note)_  
**Columns:** 19

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ACCEPTED_FLAG` | DOUBLE | NOT NULL |  | Indicates whether this nomenclature record was accepted into the coding encounter or not. 0 indicated that this was legacy, 1 indicates that this was not accepted and 2 indicates that this was accepted. |
| 2 | `CAC_DOCUMENT_ID` | DOUBLE | NOT NULL | FK→ | Identifies the document this nomenclature was found in. |
| 3 | `CAC_NOMENCLATURE_ID` | DOUBLE | NOT NULL |  | Unique identifier number for this row. |
| 4 | `CAC_RULE_ID` | DOUBLE | NOT NULL | FK→ | This is the value of the unique primary identifier of the CAC_RULE table. This will be set if a rule was applied to the row. |
| 5 | `CERTAINTY_FLAG` | DOUBLE | NOT NULL |  | The indicator for the level of certainty for the nomenclature.0 - NOT DETERMINED1 - POSITIVE2 - NEGATIVE3 - UNCERTAIN |
| 6 | `DEFAULT_PRESENT_ON_ADMIT_CD` | DOUBLE | NOT NULL |  | This is the POA value that will be defaulted if this Nomenclature is accepted in the CAC Document. This field will be set via a CAC rule. |
| 7 | `END_POS` | DOUBLE | NOT NULL |  | The character end position this nomenclature was found at. |
| 8 | `HIDDEN_IND` | DOUBLE | NOT NULL |  | Indicates whether the nomenclature text will be decorated in the document. |
| 9 | `IGNORE_IND` | DOUBLE | NOT NULL |  | Indicates that this nomenclature has been ignored. |
| 10 | `MAPPED_NOMENCLATURE_ID` | DOUBLE | NOT NULL | FK→ | Identifies the manually mapped nomenclature row between the start_pos and end_pos locations. |
| 11 | `NOMENCLATURE_ID` | DOUBLE | NOT NULL | FK→ | Identifies the nomenclature row found by the NLP Engine between the start_pos and end_pos locations. |
| 12 | `PHYSICIAN_ID` | DOUBLE | NOT NULL | FK→ | This is the value of the unique identifier of the PRSNL table. This identifies the Physician who performed the procedure. |
| 13 | `PROC_DT_TM` | DATETIME |  |  | Stores the date and time the procedure was performed |
| 14 | `START_POS` | DOUBLE | NOT NULL |  | The character start position this nomenclature was found at. |
| 15 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 16 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 17 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 18 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 19 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `CAC_DOCUMENT_ID` | [CAC_DOCUMENT](CAC_DOCUMENT.md) | `CAC_DOCUMENT_ID` |
| `CAC_RULE_ID` | [CAC_RULE](CAC_RULE.md) | `CAC_RULE_ID` |
| `MAPPED_NOMENCLATURE_ID` | [NOMENCLATURE](NOMENCLATURE.md) | `NOMENCLATURE_ID` |
| `NOMENCLATURE_ID` | [NOMENCLATURE](NOMENCLATURE.md) | `NOMENCLATURE_ID` |
| `PHYSICIAN_ID` | [PRSNL](PRSNL.md) | `PERSON_ID` |

