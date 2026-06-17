# LH_CNT_CODE_MAP

> This table will house the codes used by Cerner Created Content.

**Description:** LH_CNT_CODE_MAP  
**Table type:** REFERENCE  
**Primary key:** _(not published — see note)_  
**Columns:** 22

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ACTIVE_IND` | DOUBLE | NOT NULL |  | The table row is active or inactive. A row is generally active unless it is in an inactive state such as logically deleted, combined away, pending purge, etc. |
| 2 | `BEG_EFFECTIVE_DT_TM` | DATETIME | NOT NULL |  | The date and time for which this table row becomes effective. Normally, this will be the date and time the row is added, but could be a past or future date and time. |
| 3 | `CATEGORY_MEAN` | VARCHAR(50) |  |  | The Bedrock Category_Mean that this piece of content is related to. |
| 4 | `CODE_STATUS_FLAG` | DOUBLE | NOT NULL |  | The status of the code mapping. |
| 5 | `CONTENT_NAME` | VARCHAR(255) | NOT NULL |  | The name of the content. |
| 6 | `CONTENT_TYPE` | VARCHAR(255) | NOT NULL |  | The type of content of this row of data. |
| 7 | `END_EFFECTIVE_DT_TM` | DATETIME | NOT NULL |  | The date/time after which the row is no longer valid as active current data. This may be valued with the date that the row became inactive. |
| 8 | `EXTRACT_DT_TM` | DATETIME |  |  | The date/time that the record was extracted from the source system. |
| 9 | `FILTER_MEAN` | VARCHAR(50) |  |  | The Bedrock Filter_Mean that this piece of content is related to. |
| 10 | `FIRST_PROCESS_DT_TM` | DATETIME |  |  | The date/time the record was first loaded into the table. |
| 11 | `HEALTH_SYSTEM_ID` | DOUBLE | NOT NULL |  | Identifies the delivery network responsible for supplying the data. |
| 12 | `HEALTH_SYSTEM_SOURCE_ID` | DOUBLE | NOT NULL |  | Identifies the unique source within the delivery network responsible for supplying the data. |
| 13 | `LAST_PROCESS_DT_TM` | DATETIME |  |  | The date/time the record was last loaded into the table. |
| 14 | `LH_CNT_CODE_MAP_ID` | DOUBLE | NOT NULL |  | Unique generated number that identifies a single row on the LH_CNT_CODE_MAP table. |
| 15 | `PARENT_CODE_IND` | DOUBLE | NOT NULL |  | Indicates whether the code is a parent or child. A value of 1 indicates the code is a parent code. (default 0). |
| 16 | `SOURCE_IDENTIFIER` | VARCHAR(100) | NOT NULL |  | This is the code, or source identifier from nomenclature, used for this row. |
| 17 | `SOURCE_VOCABULARY_CD` | DOUBLE |  |  | The Source_Vocabulary_Cd of |
| 18 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 19 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 20 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 21 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 22 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

