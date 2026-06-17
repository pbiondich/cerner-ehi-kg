# ONC_NOMEN_TERM_RELTN

> Stores the oncology nomenclature and anatomy pathology term association information

**Description:** ONCOLOGY NOMENCLATURE TERM RELATION  
**Table type:** REFERENCE  
**Primary key:** _(not published — see note)_  
**Columns:** 17

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ACTIVE_IND` | DOUBLE | NOT NULL |  | The table row is active or inactive. A row is generally active unless it is in an inactive state such as logically deleted, combined away, pending purge, etc. |
| 2 | `CKI_IDENTIFIER` | VARCHAR(50) |  |  | concept identifier |
| 3 | `CKI_SOURCE` | VARCHAR(12) |  |  | Concept source code |
| 4 | `NOMENCLATURE_ID` | DOUBLE | NOT NULL | FK→ | Primary key from NOMECLATURE table. In this case used to identify the nomenlature associated with scr_term. |
| 5 | `ONC_NOMEN_TERM_RELTN_ID` | DOUBLE | NOT NULL |  | PRIMARY KEY |
| 6 | `ONC_TASK_SENT_RELTN_ID` | DOUBLE | NOT NULL | FK→ | Primary key from ONC_TASK_SENT_RELTN table,in this case used get nomenclature and term association information from ONC_TASK_SENT_RELTN. |
| 7 | `SCR_SENTENCE_ID` | DOUBLE | NOT NULL | FK→ | Foreign key from SCR_SENTENCE table, in this case used to identify the worksheet sentence by SCR_SENTENCE_ID |
| 8 | `SCR_TERM_DISPLAY` | VARCHAR(40) |  |  | A short display string for the term display |
| 9 | `SCR_TERM_HIER_ID` | DOUBLE | NOT NULL | FK→ | Primary key from SCR_TER_HIER table, in this case used to identify the scr_term_id by scr_term_hier_id |
| 10 | `SCR_TERM_ID` | DOUBLE | NOT NULL | FK→ | Primary Key frorm SCR_TERM table, in this case used to identify the term by scr_term_id. |
| 11 | `SHORT_STRING` | VARCHAR(40) |  |  | A short description of the source string from NOMENCLATURE table. |
| 12 | `SOURCE_STRING` | VARCHAR(256) |  |  | The SOURCE_STRING from NOMECLATURE, in this case used to identify source string of the the nomenclature defined. |
| 13 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 14 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 15 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 16 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 17 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `NOMENCLATURE_ID` | [NOMENCLATURE](NOMENCLATURE.md) | `NOMENCLATURE_ID` |
| `ONC_TASK_SENT_RELTN_ID` | [ONC_TASK_SENT_RELTN](ONC_TASK_SENT_RELTN.md) | `ONC_TASK_SENT_RELTN_ID` |
| `SCR_SENTENCE_ID` | [SCR_SENTENCE](SCR_SENTENCE.md) | `SCR_SENTENCE_ID` |
| `SCR_TERM_HIER_ID` | [SCR_TERM_HIER](SCR_TERM_HIER.md) | `SCR_TERM_HIER_ID` |
| `SCR_TERM_ID` | [SCR_TERM](SCR_TERM.md) | `SCR_TERM_ID` |

