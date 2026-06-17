# LH_ABS_SKIP_LOGIC

> Structure to define the Skip Logic for Lighthouse Abstractor (eQuality Check)

**Description:** LH_ABS_SKIP_LOGIC  
**Table type:** REFERENCE  
**Primary key:** _(not published — see note)_  
**Columns:** 18

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `BEG_EFFECTIVE_DT_TM` | DATETIME |  |  | The date and time for which this table row becomes effective. Normally, this will be the date and time the row is added, but could be a past or future date and time. |
| 2 | `BR_DATAMART_CATEGORY_ID` | DOUBLE | NOT NULL |  | Identifies the Category (i.e. Stroke, VTE, or ED Throughput). Foreign Key to BR_DATAMART_CATEGORY |
| 3 | `COND_ANSWER_ID` | DOUBLE | NOT NULL |  | The Conditional Answer for cond_question_id that will cause the lh_abs_question_id to be skipped.Foreign Key to LH_ABS_ANSWER |
| 4 | `COND_QUESTION_ID` | DOUBLE | NOT NULL |  | The Conditional Question that when paired with cond_answer_id will cause the lh_abs_question_id to be skipped.Foreign Key to LH_ABS_QUESTION |
| 5 | `END_EFFECTIVE_DT_TM` | DATETIME |  |  | The date/time after which the row is no longer valid as active current data. This may be valued with the date that the row became inactive. |
| 6 | `EXTRACT_DT_TM` | DATETIME |  |  | The date/time that the record was extracted from the source system. |
| 7 | `FIRST_PROCESS_DT_TM` | DATETIME |  |  | The date/time the record was first loaded into the table. |
| 8 | `GROUP_SEQ` | DOUBLE |  |  | Conditions that should be evaluated as AND conditions will contain the same group_seq. All conditions with a unique group_seq will be evaluated as ORs. |
| 9 | `HEALTH_SYSTEM_ID` | DOUBLE | NOT NULL |  | Identifies the delivery network responsible for supplying the data. |
| 10 | `HEALTH_SYSTEM_SOURCE_ID` | DOUBLE | NOT NULL |  | Identifies the unique source within the delivery network responsible for supplying the data. |
| 11 | `LAST_PROCESS_DT_TM` | DATETIME |  |  | The date/time the record was last loaded into the table. |
| 12 | `LH_ABS_QUESTION_ID` | DOUBLE | NOT NULL |  | The question which the cond_question_id and cond_answer_id are evaluating for.Foreign Key to LH_ABS_QUESTION |
| 13 | `LH_ABS_SKIP_LOGIC_ID` | DOUBLE | NOT NULL |  | Unique generated number that identifies a single row on the LH_ABS_SKIP_LOGIC table. |
| 14 | `NOT_IND` | DOUBLE | NOT NULL |  | Identifies when logic should be inverted |
| 15 | `UPDT_CNT` | DOUBLE |  |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 16 | `UPDT_DT_TM` | DATETIME |  |  | The date and time the row was last inserted or updated. |
| 17 | `UPDT_SOURCE` | VARCHAR(50) |  |  | The script name responsible for updating the record. |
| 18 | `UPDT_TASK` | VARCHAR(50) |  |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

