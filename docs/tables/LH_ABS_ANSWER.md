# LH_ABS_ANSWER

> Answers that a user can select to questions of the Lighthouse Abstractor (eQuality Check)

**Description:** LH_ABS_ANSWER  
**Table type:** REFERENCE  
**Primary key:** _(not published — see note)_  
**Columns:** 19

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ANSWER_CODE` | VARCHAR(50) |  |  | The codified value of the answer. This will be that will be applied to submission files. |
| 2 | `ANSWER_SEQ` | DOUBLE |  |  | Defines the order that this Answer will presented to the user if multiple Answers are available for the Question |
| 3 | `ANSWER_SUB_SEQ` | DOUBLE |  |  | A Sub Answer sequence when ANSWER_SEQ is the same for QUESTION_KEY |
| 4 | `ANSWER_VALUE` | VARCHAR(1000) |  |  | Full text of the Answer |
| 5 | `BEG_EFFECTIVE_DT_TM` | DATETIME |  |  | The date and time for which this table row becomes effective. Normally, this will be the date and time the row is added, but could be a past or future date and time. |
| 6 | `END_EFFECTIVE_DT_TM` | DATETIME |  |  | The date/time after which the row is no longer valid as active current data. This may be valued with the date that the row became inactive. |
| 7 | `EXTRACT_DT_TM` | DATETIME |  |  | The date/time that the record was extracted from the source system. |
| 8 | `FIRST_PROCESS_DT_TM` | DATETIME |  |  | The date/time the record was first loaded into the table. |
| 9 | `GWTG_ANSWER_CODE` | VARCHAR(50) |  |  | Get With The Guidelines answer code |
| 10 | `HEALTH_SYSTEM_ID` | DOUBLE | NOT NULL |  | Identifies the delivery network responsible for supplying the data. |
| 11 | `HEALTH_SYSTEM_SOURCE_ID` | DOUBLE | NOT NULL | FK→ | Identifies the unique source within the delivery network responsible for supplying the data. |
| 12 | `LAST_PROCESS_DT_TM` | DATETIME |  |  | The date/time the record was last loaded into the table. |
| 13 | `LH_ABS_ANSWER_ID` | DOUBLE | NOT NULL |  | Unique generated number that identifies a single row on the LH_ABS_ANSWER table. |
| 14 | `LH_ABS_QUESTION_ID` | DOUBLE | NOT NULL | FK→ | Identifies the Question that this response can be applied to. Foreign Key to LH_ABS_QUESTION |
| 15 | `TJC_ANSWER_CODE` | VARCHAR(50) |  |  | The Joint Commission answer code |
| 16 | `UPDT_CNT` | DOUBLE |  |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 17 | `UPDT_DT_TM` | DATETIME |  |  | The date and time the row was last inserted or updated. |
| 18 | `UPDT_SOURCE` | VARCHAR(50) |  |  | The script name responsible for updating the record. |
| 19 | `UPDT_TASK` | VARCHAR(50) |  |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `HEALTH_SYSTEM_SOURCE_ID` | [LH_ABS_QUESTION](LH_ABS_QUESTION.md) | `HEALTH_SYSTEM_SOURCE_ID` |
| `LH_ABS_QUESTION_ID` | [LH_ABS_QUESTION](LH_ABS_QUESTION.md) | `LH_ABS_QUESTION_ID` |

