# LH_ABS_LAYOUT

> Defined layout of the Sections displayed in the Lighthouse Abstractor (eQuality Check)

**Description:** LH_ABS_LAYOUT  
**Table type:** REFERENCE  
**Primary key:** `HEALTH_SYSTEM_SOURCE_ID`, `LH_ABS_LAYOUT_ID`  
**Columns:** 22  
**Referenced by:** 2 columns

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `BEG_EFFECTIVE_DT_TM` | DATETIME |  |  | The date and time for which this table row becomes effective. Normally, this will be the date and time the row is added, but could be a past or future date and time. |
| 2 | `BR_DATAMART_CATEGORY_ID` | DOUBLE | NOT NULL |  | Identifies the Category (i.e. Stroke, VTE, or ED Throughput). Foreign Key to BR_DATAMART_CATEGORY |
| 3 | `END_EFFECTIVE_DT_TM` | DATETIME |  |  | The date/time after which the row is no longer valid as active current data. This may be valued with the date that the row became inactive. |
| 4 | `EXTRACT_DT_TM` | DATETIME |  |  | The date/time that the record was extracted from the source system. |
| 5 | `FIRST_PROCESS_DT_TM` | DATETIME |  |  | The date/time that the first ETL process started that created this record. |
| 6 | `GWTG_TJC_IND` | DOUBLE |  |  | Indicates a question that should be marked because it is only used for GWTG and/or TJC |
| 7 | `HEALTH_SYSTEM_ID` | DOUBLE | NOT NULL |  | Identifies the delivery network responsible for supplying the data. |
| 8 | `HEALTH_SYSTEM_SOURCE_ID` | DOUBLE | NOT NULL | PK FK→ | Identifies the unique source within the delivery network responsible for supplying the data. |
| 9 | `LAST_PROCESS_DT_TM` | DATETIME |  |  | The date/time that the last ETL process started that updated this record. |
| 10 | `LH_ABS_LAYOUT_ID` | DOUBLE | NOT NULL | PK | Unique generated number that identifies a single row on the LH_ABS_LAYOUT table. |
| 11 | `LH_ABS_QUESTION_ID` | DOUBLE | NOT NULL | FK→ | Identifies the Question that are grouped under the specified Section. Foreign Key to LH_ABS_QUESTION |
| 12 | `LH_ABS_SECTION_ID` | DOUBLE | NOT NULL | FK→ | Identifies Section. Foreign Key to LH_ABS_SECTION |
| 13 | `QUESTION_POS_SEQ` | DOUBLE | NOT NULL |  | Used to determine the position of a question if grouped within a question_seq. |
| 14 | `QUESTION_SEQ` | DOUBLE |  |  | Assigns the order the Questions will appear under the specified section |
| 15 | `SCRATCHPAD_IND` | DOUBLE | NOT NULL |  | Indicator to determine if scratchpad will be visible for this question. |
| 16 | `SECTION_SEQ` | DOUBLE |  |  | Assigns the order the Sections will appear in the Abstractor |
| 17 | `SHARED_RESPONSE_IND` | DOUBLE |  |  | The indicator to represent if a response is being shared across multiple conditions for the same patient. 0 - Yes; 1 - No. |
| 18 | `UPDT_CNT` | DOUBLE |  |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 19 | `UPDT_DT_TM` | DATETIME |  |  | The date and time the row was last inserted or updated. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 20 | `UPDT_SOURCE` | VARCHAR(50) |  |  | The script name responsible for updating the record. |
| 21 | `UPDT_TASK` | VARCHAR(50) |  |  | The registered (assigned) task number for the process that inserted or updated the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 22 | `USER_ID` | DOUBLE |  |  | The user that is assigned to a customized layout |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `HEALTH_SYSTEM_SOURCE_ID` | [LH_ABS_QUESTION](LH_ABS_QUESTION.md) | `HEALTH_SYSTEM_SOURCE_ID` |
| `HEALTH_SYSTEM_SOURCE_ID` | [LH_ABS_SECTION](LH_ABS_SECTION.md) | `HEALTH_SYSTEM_SOURCE_ID` |
| `LH_ABS_QUESTION_ID` | [LH_ABS_QUESTION](LH_ABS_QUESTION.md) | `LH_ABS_QUESTION_ID` |
| `LH_ABS_SECTION_ID` | [LH_ABS_SECTION](LH_ABS_SECTION.md) | `LH_ABS_SECTION_ID` |

## Referenced by (2)

| From table | Column |
|------------|--------|
| [LH_ABS_MEASURE_RELTN](LH_ABS_MEASURE_RELTN.md) | `HEALTH_SYSTEM_SOURCE_ID` |
| [LH_ABS_MEASURE_RELTN](LH_ABS_MEASURE_RELTN.md) | `LH_ABS_LAYOUT_ID` |

