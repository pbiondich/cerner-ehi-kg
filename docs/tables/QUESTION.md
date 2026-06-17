# QUESTION

> A reference table of the questions to be asked of the user in the Preference wizard. The questions vary by HNA module.

**Description:** Question  
**Table type:** REFERENCE  
**Primary key:** `QUESTION_CD`  
**Columns:** 17  
**Referenced by:** 2 columns

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ACTIVE_IND` | DOUBLE |  |  | The table row is active or inactive. A row is generally active unless it is in an inactive state such as logically deleted, combined away, pending purge, etc. |
| 2 | `CDF_MEANING` | CHAR(12) |  |  | For a question whose responses are to come from a Code Set, this field (CDF_MEANING) indicates that the valid values from the Code Set are to come from a subset with a CDF_Meaning on the Code_Value table with a value equal to the value in this field. |
| 3 | `CODE_SET` | DOUBLE |  |  | The number of the code set where the question is defined. |
| 4 | `DEF_ANSWER` | VARCHAR(200) |  |  | The Cerner-defined default answer defined for this question (ex. "Yes", "No", etc.) |
| 5 | `DWB_IND` | DOUBLE |  |  | Not currently used. |
| 6 | `MODULE_CD` | DOUBLE | NOT NULL |  | The module to which the question pertains (ex. "PathNet Blood Bank Transfusion", "Pharmacy"). |
| 7 | `PROCESS_CD` | DOUBLE | NOT NULL |  | The process within the module to which the question pertains (ex. the "Dispense" process within the PathNet Blood Bank Transfusion module). |
| 8 | `QUESTION` | VARCHAR(200) |  |  | The Cerner-defined text of the question that should be asked of the user. |
| 9 | `QUESTION_CD` | DOUBLE | NOT NULL | PK | The code value of the question, from code set 1661. |
| 10 | `RESPONSE_FLAG` | DOUBLE |  |  | The type of response to this question. |
| 11 | `RESPONSE_LENGTH` | DOUBLE |  |  | The Cerner-defined maximum length of the answer. |
| 12 | `SEQUENCE` | DOUBLE |  |  | The Cerner-defined sequence in which the questions should display within a process. |
| 13 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 14 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 15 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 16 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 17 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Referenced by (2)

| From table | Column |
|------------|--------|
| [ANSWER](ANSWER.md) | `QUESTION_CD` |
| [VALID_RESPONSE](VALID_RESPONSE.md) | `QUESTION_CD` |

