# SCR_TERM

> The standard entry will be a text term which may be set to true,false or undetermined. Data Required for more complex and unusual terms is stored in subtables to conserve space.

**Description:** Contains an entry for each term in a sentence  
**Table type:** REFERENCE  
**Primary key:** `SCR_TERM_ID`  
**Columns:** 23  
**Referenced by:** 5 columns

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ACTIVE_IND` | DOUBLE |  |  | The table row is active or inactive. A row is generally active unless it is in an inactive state such as logically deleted, combined away, pending purge, etc. |
| 2 | `ACTIVE_STATUS_CD` | DOUBLE | NOT NULL |  | Indicates the status of the row itself (not the data in the row) such as active, inactive, combined away, pending purge, etc. |
| 3 | `ACTIVE_STATUS_DT_TM` | DATETIME |  |  | The date and time that the active_status_cd was set. |
| 4 | `ACTIVE_STATUS_PRSNL_ID` | DOUBLE | NOT NULL |  | The person who caused the active_status_cd to be set or change. |
| 5 | `CONCEPT_CKI` | VARCHAR(255) |  |  | The default concept that the term relates to. (The merging of concept_identifier and concept_source_cd columns into one column) |
| 6 | `CONCEPT_IDENTIFIER` | CHAR(18) |  |  | Concept identifier |
| 7 | `CONCEPT_SOURCE_CD` | DOUBLE | NOT NULL |  | Concept Source Code |
| 8 | `ELIGIBILITY_CHECK_CD` | DOUBLE | NOT NULL |  | eligibilty check code |
| 9 | `OLDEST_AGE` | DOUBLE |  |  | Oldest Age comparsion field. |
| 10 | `REPEAT_CD` | DOUBLE | NOT NULL |  | repeat code |
| 11 | `RESTRICT_TO_SEX` | CHAR(12) |  |  | restrict to sec |
| 12 | `SCR_TERM_DEF_ID` | DOUBLE | NOT NULL |  | Term Def Id - |
| 13 | `SCR_TERM_ID` | DOUBLE | NOT NULL | PK | Unique ID (PK) |
| 14 | `STATE_LOGIC_CD` | DOUBLE | NOT NULL |  | State logic Code |
| 15 | `STORE_CD` | DOUBLE | NOT NULL |  | store Code |
| 16 | `TERM_TYPE_CD` | DOUBLE | NOT NULL |  | term type code |
| 17 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 18 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 19 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 20 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 21 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |
| 22 | `VISIBLE_CD` | DOUBLE | NOT NULL |  | Visible_cd |
| 23 | `YOUNGEST_AGE` | DOUBLE |  |  | Youngst Age |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Referenced by (5)

| From table | Column |
|------------|--------|
| [ONC_NOMEN_TERM_RELTN](ONC_NOMEN_TERM_RELTN.md) | `SCR_TERM_ID` |
| [SCD_TERM](SCD_TERM.md) | `SCR_TERM_ID` |
| [SCR_TERM_DEFINITION](SCR_TERM_DEFINITION.md) | `SCR_TERM_DEF_ID` |
| [SCR_TERM_HIER](SCR_TERM_HIER.md) | `SCR_TERM_ID` |
| [SCR_TERM_TEXT](SCR_TERM_TEXT.md) | `SCR_TERM_ID` |

