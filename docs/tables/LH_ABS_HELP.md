# LH_ABS_HELP

> Structure to define the help documentation for Lighthouse Abstractor (eQuality Check)

**Description:** LH_ABS_HELP  
**Table type:** REFERENCE  
**Primary key:** _(not published — see note)_  
**Columns:** 19

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `BEG_EFFECTIVE_DT_TM` | DATETIME |  |  | The date and time for which this table row becomes effective. Normally, this will be the date and time the row is added, but could be a past or future date and time. |
| 2 | `BR_DATAMART_CATEGORY_ID` | DOUBLE | NOT NULL |  | Identifies the Category (i.e. Stroke, VTE, or ED Throughput). Foreign Key to BR_DATAMART_CATEGORY |
| 3 | `DISPLAY` | VARCHAR(50) |  |  | Help file's display text. This will only be present for top level help. |
| 4 | `END_EFFECTIVE_DT_TM` | DATETIME |  |  | The date/time after which the row is no longer valid as active current data. This may be valued with the date that the row became inactive. |
| 5 | `EXTRACT_DT_TM` | DATETIME |  |  | The date/time that the record was extracted from the source system. |
| 6 | `FIRST_PROCESS_DT_TM` | DATETIME |  |  | The date/time that the first ETL process started that created this record. |
| 7 | `HEALTH_SYSTEM_ID` | DOUBLE | NOT NULL |  | Identifies the delivery network responsible for supplying the data. |
| 8 | `HEALTH_SYSTEM_SOURCE_ID` | DOUBLE | NOT NULL |  | Identifies the unique source within the delivery network responsible for supplying the data. |
| 9 | `HELP_FILENAME` | VARCHAR(100) |  |  | Help file's file name |
| 10 | `HELP_PATH` | VARCHAR(100) |  |  | Relative directory text where the help file is residing |
| 11 | `HELP_SEQ` | DOUBLE |  |  | Assigns display order for the top level help files |
| 12 | `LAST_PROCESS_DT_TM` | DATETIME |  |  | The date/time that the last ETL process started that updated this record. |
| 13 | `LH_ABS_HELP_ID` | DOUBLE | NOT NULL |  | Unique generated number that identifies a single row on the LH_ABS_HELP table. |
| 14 | `LH_ABS_QUESTION_ID` | DOUBLE | NOT NULL |  | The question which the help file is for. This has the potential to be null for top level help. Foreign Key to LH_ABS_QUESTION but can be null/0 |
| 15 | `LINK_TEXT` | VARCHAR(50) |  |  | Help file's text to be used as a link. |
| 16 | `UPDT_CNT` | DOUBLE |  |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 17 | `UPDT_DT_TM` | DATETIME |  |  | The date and time the row was last inserted or updated. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 18 | `UPDT_SOURCE` | VARCHAR(50) |  |  | The script name responsible for updating the record. |
| 19 | `UPDT_TASK` | VARCHAR(50) |  |  | The registered (assigned) task number for the process that inserted or updated the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

