# PROT_QUESTIONNAIRE

> This table stores information on questionnaires connected to an amendment

**Description:** PROT QUESTIONNAIRE  
**Table type:** REFERENCE  
**Primary key:** `PROT_QUESTIONNAIRE_ID`  
**Columns:** 14  
**Referenced by:** 4 columns

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `BEG_EFFECTIVE_DT_TM` | DATETIME | NOT NULL |  | The date and time for which this table row becomes effective. Normally, this will be the date and time the row is added, but could be a past or future date and time. |
| 2 | `DESC_LONG_TEXT_ID` | DOUBLE | NOT NULL | FK→ | References the long text for the checklist description. Foreign key from the long text reference table. |
| 3 | `END_EFFECTIVE_DT_TM` | DATETIME | NOT NULL |  | The date/time after which the row is no longer valid as active current data. This may be valued with the date that the row became inactive. |
| 4 | `PREV_PROT_QUESTIONNAIRE_ID` | DOUBLE | NOT NULL | FK→ | The original value of prot_questionnaire_id used for grouping the related versions. Required for type2 versioning. |
| 5 | `PROT_AMENDMENT_ID` | DOUBLE | NOT NULL | FK→ | Refers to the amendment that this questionnaire is connected to |
| 6 | `PROT_QUESTIONNAIRE_ID` | DOUBLE | NOT NULL | PK | Uniquely identifies a questionnaire in the table |
| 7 | `QUESTIONNAIRE_NAME` | VARCHAR(255) |  |  | Free text name of the questionnaire. |
| 8 | `QUESTIONNAIRE_TYPE_CD` | DOUBLE | NOT NULL |  | Identifies the type of the questionnaire (CS: Checklist_type) |
| 9 | `SPECIAL_INST_LONG_TEXT_ID` | DOUBLE | NOT NULL | FK→ | References the long text for the checklist special instruction. Foreign key from the long text reference table. |
| 10 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 11 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 12 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 13 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 14 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `DESC_LONG_TEXT_ID` | [LONG_TEXT_REFERENCE](LONG_TEXT_REFERENCE.md) | `LONG_TEXT_ID` |
| `PREV_PROT_QUESTIONNAIRE_ID` | [PROT_QUESTIONNAIRE](PROT_QUESTIONNAIRE.md) | `PROT_QUESTIONNAIRE_ID` |
| `PROT_AMENDMENT_ID` | [PROT_AMENDMENT](PROT_AMENDMENT.md) | `PROT_AMENDMENT_ID` |
| `SPECIAL_INST_LONG_TEXT_ID` | [LONG_TEXT_REFERENCE](LONG_TEXT_REFERENCE.md) | `LONG_TEXT_ID` |

## Referenced by (4)

| From table | Column |
|------------|--------|
| [PROT_ELIG_QUEST](PROT_ELIG_QUEST.md) | `PROT_QUESTIONNAIRE_ID` |
| [PROT_QUESTIONNAIRE](PROT_QUESTIONNAIRE.md) | `PREV_PROT_QUESTIONNAIRE_ID` |
| [PT_ELIG_TRACKING](PT_ELIG_TRACKING.md) | `PROT_QUESTIONNAIRE_ID` |
| [QUESTIONNAIRE_DOC_RELTN](QUESTIONNAIRE_DOC_RELTN.md) | `PROT_QUESTIONNAIRE_ID` |

