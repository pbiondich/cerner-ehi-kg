# SCR_PATTERN_CONCEPT

> This table relates patterns to concepts. It contains a row for each concept of each pattern.

**Description:** The relationship table between tables scr_pattern and concept.  
**Table type:** REFERENCE  
**Primary key:** _(not published — see note)_  
**Columns:** 9

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `CONCEPT_CKI` | VARCHAR(255) | NOT NULL |  | The cki of the concept associated to a pattern. This is a merge of concept_identifier and concept_source_cd columns into one column. |
| 2 | `CONCEPT_IDENTIFIER` | VARCHAR(242) | NOT NULL |  | A member of the concept table's primary key |
| 3 | `CONCEPT_SOURCE_CD` | DOUBLE | NOT NULL |  | A member of the concept table's primary key. |
| 4 | `SCR_PATTERN_ID` | DOUBLE | NOT NULL | FK→ | A member of the scr_pattern table's primary key |
| 5 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 6 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 7 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 8 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 9 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `SCR_PATTERN_ID` | [SCR_PATTERN](SCR_PATTERN.md) | `SCR_PATTERN_ID` |

