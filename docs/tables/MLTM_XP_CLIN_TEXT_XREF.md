# MLTM_XP_CLIN_TEXT_XREF

> This table contains essential information about drug lactation hazards, pharmacology, pregnancy hazards, side effects, and warnings and contraindications, including codes for each of the drugs, identifiers for a particular type of clinical information, text level, body system identification, display order, and a code representing specific text describing the clinical information.

**Description:** Multum XP Clin Text Xref  
**Table type:** REFERENCE  
**Primary key:** _(not published — see note)_  
**Columns:** 12

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `DISPLAY_ORDER` | DOUBLE |  |  | The display order |
| 2 | `DRUG_IDENTIFIER` | VARCHAR(6) | NOT NULL | FK→ | This field contains Multum's identification codes for generic drugs. |
| 3 | `FUNCTION_ID` | DOUBLE | NOT NULL | FK→ | The function ID from MLTM FUNCTION TYPE table |
| 4 | `LEVEL_ID` | DOUBLE | NOT NULL |  | Part of the unique identifier for this table. |
| 5 | `SEVERITY_ID` | DOUBLE | NOT NULL | FK→ | FK from the Multum severity table |
| 6 | `SYST_ID` | DOUBLE | NOT NULL | FK→ | FK from the MLTM SYST IDENTIFIER TABLE |
| 7 | `TEXT_ID` | DOUBLE | NOT NULL | FK→ | PK from the Multum XP Clin Text table |
| 8 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 9 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 10 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 11 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 12 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `DRUG_IDENTIFIER` | [MLTM_DRUG_ID](MLTM_DRUG_ID.md) | `DRUG_IDENTIFIER` |
| `FUNCTION_ID` | [MLTM_FUNCTION_TYPE](MLTM_FUNCTION_TYPE.md) | `FUNCTION_ID` |
| `SEVERITY_ID` | [MLTM_SEVERITY](MLTM_SEVERITY.md) | `SEVERITY_ID` |
| `SYST_ID` | [MLTM_SYST_IDENTIFIER](MLTM_SYST_IDENTIFIER.md) | `SYST_ID` |
| `TEXT_ID` | [MLTM_XP_CLIN_TEXT](MLTM_XP_CLIN_TEXT.md) | `TEXT_ID` |

