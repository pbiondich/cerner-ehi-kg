# AP_CASE_SYNOPTIC_WS_DATA

> This table maintains discrete synoptic Worksheet data of worksheets associated with an Anatomic Pathology case.

**Description:** AP Case Synoptic Worksheet Data  
**Table type:** ACTIVITY  
**Primary key:** _(not published — see note)_  
**Columns:** 31

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ALT_ANSWER_CKI` | VARCHAR(255) |  |  | Alternate identifier for the answer. |
| 2 | `ALT_ANSWER_CODING_SYS_IDENT` | VARCHAR(255) |  |  | Identifies the coding system for the alternate answer identifier/CKI. The data in this column is only applicable if ALT_ANSWER_CKI is populated. |
| 3 | `ALT_ANSWER_TXT` | VARCHAR(2000) |  |  | Alternate name or description of the answer. The data in this column is only applicable if ALT_ANSWER_CKI is populated. |
| 4 | `ALT_QUESTION_CKI` | VARCHAR(255) |  |  | Alternate identifier for the question. |
| 5 | `ALT_QUESTION_CODING_SYS_IDENT` | VARCHAR(255) |  |  | Identifies the coding system for the alternate question identifier/CKI. |
| 6 | `ALT_QUESTION_TXT` | VARCHAR(2000) |  |  | Alternate name or description of the question. |
| 7 | `ANSWER_CODING_SYS_IDENT` | VARCHAR(255) |  |  | Identifies the coding system for the answer identifier/CKI. The data in this column is only applicable if ANSWER_CONCEPT_CKI is populated. |
| 8 | `ANSWER_CONCEPT_CKI` | VARCHAR(255) |  |  | The specific answer concept cki (nomenclature table) that this data is tied to |
| 9 | `ANSWER_LONG_TEXT_ID` | DOUBLE | NOT NULL | FK→ | Stores the long text identifier when answer type is text |
| 10 | `ANSWER_SUB_IDENT` | VARCHAR(255) |  |  | An identifier to group multiple answer components. This field is only applicable for fields with multiple answer components e.g. a selectable field with fill-in box. |
| 11 | `ANSWER_TEXT_FORMAT_CD` | DOUBLE | NOT NULL |  | Stores the answer text format code from codeset 23 (RTF, AS or AH) |
| 12 | `ANSWER_TXT` | VARCHAR(2000) |  |  | Name or description of the answer. The data in this column is only applicable if ANSWER_CONCEPT_CKI is populated. |
| 13 | `ANSWER_TYPE_FLAG` | DOUBLE | NOT NULL |  | Flag to indicate what type of answer is being stored |
| 14 | `ANSWER_TYPE_TXT` | VARCHAR(255) |  |  | The answer type name/identifier. |
| 15 | `ANSWER_UNIT_CD` | DOUBLE | NOT NULL |  | stores the unit of measure from codeset 54 when answer type is decimal or integer |
| 16 | `ANSWER_UNIT_CODING_SYS_IDENT` | VARCHAR(255) |  |  | Identifies the coding system for the answer unit of measure identifier. The data in this column is only applicable if ANSWER_UNIT_TEXT is populated. |
| 17 | `ANSWER_UNIT_IDENT` | VARCHAR(255) |  |  | Identifies the unit of measure. |
| 18 | `ANSWER_UNIT_TXT` | VARCHAR(255) |  |  | Name or description for the unit of measure. |
| 19 | `ANSWER_VALUE` | VARCHAR(255) |  |  | Stores the answer value. Answer_type_flag must be evaluated to determine proper conversion. |
| 20 | `AP_CASE_SYNOPTIC_WS_DATA_ID` | DOUBLE | NOT NULL |  | Unique generated number that identifies a single row on the AP_CASE_SYNOPTIC_WS_DATA table. |
| 21 | `CASE_WORKSHEET_ID` | DOUBLE |  | FK→ | The specific worksheet (ap_case_synoptic_ws) that the question/answer data is tied to |
| 22 | `QUESTION_CODING_SYS_IDENT` | VARCHAR(255) |  |  | Identifies the coding system used for the question identifier/CKI. |
| 23 | `QUESTION_CONCEPT_CKI` | VARCHAR(255) | NOT NULL |  | The specific question concept cki (nomenclature table) that this data is tied to |
| 24 | `QUESTION_TXT` | VARCHAR(2000) |  |  | Name of the descitiption of the question. |
| 25 | `REC_TYPE_FLAG` | DOUBLE | NOT NULL |  | Identifiers the type of the result row; The value will be 0 - for question/answer pair results; 1 - for the worksheet data. |
| 26 | `SUB_ANSWER_TYPE_TXT` | VARCHAR(255) |  |  | The type for the sub answers. This column is only applicable for fields with multiple answer components e.g. a selectable field with fill-in box. |
| 27 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 28 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 29 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 30 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 31 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `ANSWER_LONG_TEXT_ID` | [LONG_TEXT](LONG_TEXT.md) | `LONG_TEXT_ID` |
| `CASE_WORKSHEET_ID` | [AP_CASE_SYNOPTIC_WS](AP_CASE_SYNOPTIC_WS.md) | `CASE_WORKSHEET_ID` |

