# OMF_CODING_ST

> omf_coding_st

**Description:** Care Profiling - stores ICD9 and CPT4 coding data.  
**Table type:** ACTIVITY  
**Primary key:** _(not published — see note)_  
**Columns:** 24

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ANESTHESIA_CD` | DOUBLE | NOT NULL |  | anesthesia code value |
| 2 | `ANESTHESIA_MINUTES` | DOUBLE |  |  | anesthesia minutes |
| 3 | `ANESTHESIOLOGIST_FT_NAME` | VARCHAR(255) |  |  | The free text name of the anesthesiologist. |
| 4 | `ANESTHESIOLOGIST_ID` | DOUBLE | NOT NULL |  | The unique identifier for the anesthesiologist |
| 5 | `ANESTHESIOLOGIST_KEY` | VARCHAR(255) |  |  | The concatenation of the anesthesiologist_id and free text name used for grouping within PowerVision |
| 6 | `ANESTH_POSITION_CD` | DOUBLE | NOT NULL |  | The Cerner-defined position for the anesthesiologist. |
| 7 | `ENCNTR_ID` | DOUBLE | NOT NULL | FK→ | This is the value of the unique primary identifier of the encounter table. It is an internal system assigned number. |
| 8 | `NOMENCLATURE_ID` | DOUBLE | NOT NULL |  | This is the value of the unique primary identifier of the nomenclature table. It is an internal system assigned number. |
| 9 | `OMF_CODING_ST_ID` | DOUBLE | NOT NULL |  | The unique identifier for the omf_coding_st. |
| 10 | `PRINCIPLE_TYPE_CD` | DOUBLE | NOT NULL |  | A general category used to group strings. |
| 11 | `PRIORITY` | DOUBLE |  |  | The priority for the coded data. |
| 12 | `PROCEDURE_DT_NBR` | DOUBLE |  |  | The Julian date on which the ICD9 procedure was performed. |
| 13 | `PROCEDURE_DT_TM` | DATETIME |  |  | The date/time on which the ICD9 Procedure was performed |
| 14 | `PROCEDURE_MINUTES` | DOUBLE |  |  | The number of minutes for the ICD9 procedure. |
| 15 | `PROCEDURE_MIN_NBR` | DOUBLE |  |  | The minute of the day on which the ICD9 procedure was performed. |
| 16 | `PROCEDURE_TZ` | DOUBLE |  |  | Time zone associated with the corresponding DT_TM column. |
| 17 | `SERVICE_CATEGORY_CD` | DOUBLE | NOT NULL |  | Codified field which identifies the category of service the patient is receiving; tied to the codified data from the coding system. |
| 18 | `SOURCE_VOCABULARY_CD` | DOUBLE | NOT NULL |  | The external vocabulary or lexicon that contributed the string, e.g. ICD9, SNOMED, etc. |
| 19 | `TISSUE_TYPE_CD` | DOUBLE | NOT NULL |  | tissue type code value |
| 20 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 21 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 22 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 23 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 24 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `ENCNTR_ID` | [ENCOUNTER](ENCOUNTER.md) | `ENCNTR_ID` |

