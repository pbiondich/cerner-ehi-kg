# ONC_MTUITIVE_WORKSHEET

> Contains the oncology mTuitive worksheet data

**Description:** ONCOLOGY MTUITIVE WORKSHEET  
**Table type:** ACTIVITY  
**Primary key:** _(not published — see note)_  
**Columns:** 24

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ACTIVE_IND` | DOUBLE | NOT NULL |  | The table row is active or inactive. A row is generally active unless it is in an inactive state such as logically deleted, combined away, pending purge, etc. |
| 2 | `ANSWER_CONCEPT_CKI` | VARCHAR(256) |  |  | Answer Concept CKI of the MTuitive question; |
| 3 | `ANSWER_DATATYPE` | VARCHAR(256) |  |  | QUESTION DATATYPE. FOR EG. STRING, DECIMAL |
| 4 | `ANSWER_SHORT_STRING` | VARCHAR(256) |  |  | Short string of the answer, to match with the millenium Nomenclatures |
| 5 | `ANSWER_TEXT` | VARCHAR(1280) | NOT NULL |  | Full string Answer TEXT |
| 6 | `ANSWER_TYPE_TXT` | VARCHAR(256) |  |  | ANSWER TYPE. For Eg. LIST, FREETEXT Etc. |
| 7 | `BEG_EFFECTIVE_DT_TM` | DATETIME | NOT NULL |  | The date and time for which this table row becomes effective. Normally, this will be the date and time the row is added, but could be a past or future date and time. |
| 8 | `DTA_CONCEPT_CKI` | VARCHAR(256) |  |  | The concept_cki from Discrete_Task_assay table. |
| 9 | `END_EFFECTIVE_DT_TM` | DATETIME | NOT NULL |  | The date/time after which the row is no longer valid as active current data. This may be valued with the date that the row became inactive. |
| 10 | `NOMENCLATURE_ID` | DOUBLE |  | FK→ | The nomenclature_id from nomenclature table |
| 11 | `ONC_MTUITIVE_WORKSHEET_ID` | DOUBLE | NOT NULL |  | PRIMARY KEY |
| 12 | `QUESTION_CONCEPT_CKI` | VARCHAR(256) |  |  | Question Concept CKI of the mTuitive question |
| 13 | `QUESTION_DATATYPE` | VARCHAR(256) | NOT NULL |  | QUESTION DATATYPE. FOR EG. STRING, DECIMAL |
| 14 | `QUESTION_MULTI_IND` | DOUBLE |  |  | IF LIST, QUESTION MULTISELECT INDICATOR. NULL = FREETEXT, MULTI =TRUE and SINGLE = FALSE; |
| 15 | `QUESTION_TEXT` | VARCHAR(256) | NOT NULL |  | mTuitive Question text; |
| 16 | `QUESTION_TYPE_TXT` | VARCHAR(256) | NOT NULL |  | REPORT QUESTION TYPE. For Eg. LIST, FREETEXT Etc. |
| 17 | `REPORT_NAME_KEY` | VARCHAR(256) | NOT NULL |  | mTuitive Report name in CAPs, without special characters; |
| 18 | `REPORT_NAME_STRING` | VARCHAR(256) | NOT NULL |  | mTuitive Report name along with special characters; |
| 19 | `REPORT_VERSION_TXT` | VARCHAR(256) | NOT NULL |  | mTuitive Report Version |
| 20 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 21 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 22 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 23 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 24 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `NOMENCLATURE_ID` | [NOMENCLATURE](NOMENCLATURE.md) | `NOMENCLATURE_ID` |

