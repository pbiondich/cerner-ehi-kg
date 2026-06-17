# SCR_TERM_HIER

> This table defines the parent-child hierarchy which forms the terms within a pattern.

**Description:** Defines a parent-child hierachy.  
**Table type:** REFERENCE  
**Primary key:** `SCR_TERM_HIER_ID`  
**Columns:** 19  
**Referenced by:** 3 columns

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `CKI_IDENTIFIER` | VARCHAR(50) |  |  | Cerner Knowledge Index, Identifier |
| 2 | `CKI_SOURCE` | CHAR(12) |  |  | Cerner Knowledge Index, Source |
| 3 | `CONCEPT_CKI` | VARCHAR(255) |  |  | This relates the term in the context of the current hierarchy and it's concept. |
| 4 | `DEFAULT_CD` | DOUBLE | NOT NULL |  | default code |
| 5 | `DEPENDENCY_CD` | DOUBLE | NOT NULL |  | dependency code |
| 6 | `DEPENDENCY_GROUP` | DOUBLE |  |  | dependency group |
| 7 | `PARENT_TERM_HIER_ID` | DOUBLE | NOT NULL |  | parent term hierachy Id |
| 8 | `RECOMMENDED_CD` | DOUBLE | NOT NULL |  | recommened code |
| 9 | `SCR_PATTERN_ID` | DOUBLE | NOT NULL | FK→ | Pattern Identifier |
| 10 | `SCR_SENTENCE_ID` | DOUBLE | NOT NULL | FK→ | Sentence Identifier |
| 11 | `SCR_TERM_HIER_ID` | DOUBLE | NOT NULL | PK | Term Hierarchy Identifier |
| 12 | `SCR_TERM_ID` | DOUBLE | NOT NULL | FK→ | Term Identifier |
| 13 | `SEQUENCE_NUMBER` | DOUBLE |  |  | sequence number |
| 14 | `SOURCE_TERM_HIER_ID` | DOUBLE | NOT NULL |  | source term hierarch id |
| 15 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 16 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 17 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 18 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 19 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `SCR_PATTERN_ID` | [SCR_PATTERN](SCR_PATTERN.md) | `SCR_PATTERN_ID` |
| `SCR_SENTENCE_ID` | [SCR_SENTENCE](SCR_SENTENCE.md) | `SCR_SENTENCE_ID` |
| `SCR_TERM_ID` | [SCR_TERM](SCR_TERM.md) | `SCR_TERM_ID` |

## Referenced by (3)

| From table | Column |
|------------|--------|
| [ONC_NOMEN_TERM_RELTN](ONC_NOMEN_TERM_RELTN.md) | `SCR_TERM_HIER_ID` |
| [SCD_SENTENCE](SCD_SENTENCE.md) | `SCR_TERM_HIER_ID` |
| [SCD_TERM](SCD_TERM.md) | `SCR_TERM_HIER_ID` |

