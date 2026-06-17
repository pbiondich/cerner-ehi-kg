# SN_NOMEN_ST

> Table will store Nomenclature's documented at the "case" and "procedure" level

**Description:** SN_NOMEN_ST  
**Table type:** ACTIVITY  
**Primary key:** _(not published — see note)_  
**Columns:** 13

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ACTUAL_IND` | DOUBLE | NOT NULL |  | Indicates whether this row holds scheduled data (0) or documented data (1) |
| 2 | `DIAGNOSIS_DISPLAY` | VARCHAR(255) | NOT NULL |  | Holds the nomenclature string if NOMENCLATURE_ID is supplied, otherwise, holds the free text user entered for the diagnosis |
| 3 | `DIAGNOSIS_IDENTIFIER` | VARCHAR(50) | NOT NULL |  | Holds the nomenclature identifier if NOMENCLATURE_ID is supplied, otherwise, is empty |
| 4 | `NOMENCLATURE_ID` | DOUBLE | NOT NULL | FK→ | The nomenclature(s) value when the case was finalized |
| 5 | `NOMENCLATURE_SEQ` | DOUBLE | NOT NULL |  | The order the nomenclature(s) were listed when the case was finalized |
| 6 | `POSTOP_IND` | DOUBLE | NOT NULL |  | Indicates whether this nomenclature is PreOp (0), or PostOp (1) |
| 7 | `SN_NOMEN_ST_ID` | DOUBLE | NOT NULL |  | PRIMARY KEY |
| 8 | `SURG_CASE_ID` | DOUBLE | NOT NULL | FK→ | Foreign key to the SURGICAL_CASE table. This identifiers the surgical case containing nomenclature(s) at either the case level, procedure level or both. |
| 9 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 10 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 11 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 12 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 13 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `NOMENCLATURE_ID` | [NOMENCLATURE](NOMENCLATURE.md) | `NOMENCLATURE_ID` |
| `SURG_CASE_ID` | [SURGICAL_CASE](SURGICAL_CASE.md) | `SURG_CASE_ID` |

