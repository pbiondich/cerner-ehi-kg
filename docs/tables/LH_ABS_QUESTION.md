# LH_ABS_QUESTION

> Questions that can be used for the Lighthouse Abstractor (eQuality Check)

**Description:** LH_ABS_QUESTION  
**Table type:** REFERENCE  
**Primary key:** `HEALTH_SYSTEM_SOURCE_ID`, `LH_ABS_QUESTION_ID`  
**Columns:** 22  
**Referenced by:** 8 columns

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `BEG_EFFECTIVE_DT_TM` | DATETIME |  |  | The date and time for which this table row becomes effective. Normally, this will be the date and time the row is added, but could be a past or future date and time. |
| 2 | `END_EFFECTIVE_DT_TM` | DATETIME |  |  | The date/time after which the row is no longer valid as active current data. This may be valued with the date that the row became inactive. |
| 3 | `EXTRACT_DT_TM` | DATETIME |  |  | The date/time that the record was extracted from the source system. |
| 4 | `FIRST_PROCESS_DT_TM` | DATETIME |  |  | The date/time the record was first loaded into the table. |
| 5 | `GWTG_QUESTION_KEY` | VARCHAR(50) |  |  | Get With The Guidelines question key |
| 6 | `HEALTH_SYSTEM_ID` | DOUBLE | NOT NULL |  | Identifies the delivery network responsible for supplying the data. |
| 7 | `HEALTH_SYSTEM_SOURCE_ID` | DOUBLE | NOT NULL | PK | Identifies the unique source within the delivery network responsible for supplying the data. |
| 8 | `LAST_PROCESS_DT_TM` | DATETIME |  |  | The date/time the record was last loaded into the table. |
| 9 | `LH_ABS_QUESTION_ID` | DOUBLE | NOT NULL | PK | Unique generated number that identifies a single row on the LH_ABS_QUESTION table. |
| 10 | `NHIQM_QUESTION_KEY` | VARCHAR(50) |  |  | NHIQM question_key |
| 11 | `QUESTION_KEY` | VARCHAR(50) |  |  | An identifier that uniquely identifies the question. |
| 12 | `QUESTION_TITLE` | VARCHAR(200) |  |  | Short description of the question. |
| 13 | `QUESTION_TXT` | VARCHAR(4000) |  |  | Full text of the Question |
| 14 | `RESPONSE_DATATYPE_FLAG` | DOUBLE |  |  | Identifies the expected datatype of the user's response to the question.1 = alphanumeric2 = date3 = time4 = numeric |
| 15 | `RESPONSE_OCCURRENCES` | DOUBLE |  |  | Specifies the maximum number of responses that can be given for the question. |
| 16 | `TIME_SENSITIVE_IND` | DOUBLE | NOT NULL |  | Identifies questions that are checked for time sensitive warnings. |
| 17 | `TJC_QUESTION_KEY` | VARCHAR(50) |  |  | The Joint Commission question key |
| 18 | `UPDT_CNT` | DOUBLE |  |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 19 | `UPDT_DT_TM` | DATETIME |  |  | The date and time the row was last inserted or updated. |
| 20 | `UPDT_SOURCE` | VARCHAR(50) |  |  | The script name responsible for updating the record. |
| 21 | `UPDT_TASK` | VARCHAR(50) |  |  | The registered (assigned) task number for the process that inserted or updated the row. |
| 22 | `VERSION_TXT` | VARCHAR(25) |  |  | Specifies version of this question key |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Referenced by (8)

| From table | Column |
|------------|--------|
| [LH_ABS_ANSWER](LH_ABS_ANSWER.md) | `HEALTH_SYSTEM_SOURCE_ID` |
| [LH_ABS_ANSWER](LH_ABS_ANSWER.md) | `LH_ABS_QUESTION_ID` |
| [LH_ABS_LAYOUT](LH_ABS_LAYOUT.md) | `HEALTH_SYSTEM_SOURCE_ID` |
| [LH_ABS_LAYOUT](LH_ABS_LAYOUT.md) | `LH_ABS_QUESTION_ID` |
| [LH_ABS_RESPONSE](LH_ABS_RESPONSE.md) | `HEALTH_SYSTEM_SOURCE_ID` |
| [LH_ABS_RESPONSE](LH_ABS_RESPONSE.md) | `LH_ABS_QUESTION_ID` |
| [LH_ABS_SPECIAL_SKIP_LOGIC](LH_ABS_SPECIAL_SKIP_LOGIC.md) | `HEALTH_SYSTEM_SOURCE_ID` |
| [LH_ABS_SPECIAL_SKIP_LOGIC](LH_ABS_SPECIAL_SKIP_LOGIC.md) | `LH_ABS_QUESTION_ID` |

