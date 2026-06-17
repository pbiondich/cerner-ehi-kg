# ANSWER

> Contains answers to reference database questions. Used by DBPreferenceWizard (database tool) to store answers to questions on Transfusion's system-wide parameters. Read by applications throughout Blood Bank Transfusion.

**Description:** Answer (reference table)  
**Table type:** REFERENCE  
**Primary key:** _(not published — see note)_  
**Columns:** 14

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ACTIVE_DT_TM` | DATETIME |  |  | The date and time that this row became active, usually the date and time that it was inserted. |
| 2 | `ACTIVE_IND` | DOUBLE |  |  | The table row is active or inactive. A row is generally active unless it is in an inactive state such as logically deleted, combined away, pending purge, etc. |
| 3 | `ANSWER` | VARCHAR(200) |  |  | Contains the answer to a system-wide preference question. This column may contain a code value to a valid response code, or a code value to a code set, or free-text. |
| 4 | `ANSWER_ID` | DOUBLE | NOT NULL |  | The primary key of this table. An internal system-assigned number that ensures the uniqueness of each row. |
| 5 | `INACTIVE_DT_TM` | DATETIME |  |  | If the row has been updated to an inactive status (as determined by the ACTIVE_IND), then this column is the date and time when that occurred. |
| 6 | `MODULE_CD` | DOUBLE | NOT NULL |  | The module to which the database preference questions apply (ex. Blood Bank Transfusion"). |
| 7 | `PROCESS_CD` | DOUBLE | NOT NULL |  | The process within the module for which the preference questions apply (ex. "Result Entry", "Dispense"). |
| 8 | `QUESTION_CD` | DOUBLE | NOT NULL | FK→ | The question that is being asked of the user concerning a certain process within the module. |
| 9 | `SEQUENCE` | DOUBLE | NOT NULL |  | The sequence in which the DBPreferenceWizard should display this answer. |
| 10 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 11 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 12 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 13 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 14 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `QUESTION_CD` | [QUESTION](QUESTION.md) | `QUESTION_CD` |

