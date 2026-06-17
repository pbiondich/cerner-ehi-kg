# LH_ABS_SCRATCHPAD

> Scratchpad entries for records being abstracted in the Lighthouse Abstractor (eQuality Check)

**Description:** LH_ABS_SCRATCHPAD  
**Table type:** ACTIVITY  
**Primary key:** _(not published — see note)_  
**Columns:** 24

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ABS_DT_TM` | DATETIME |  |  | When the result was documented |
| 2 | `ABS_NAME` | VARCHAR(75) |  |  | Name of the result being entered |
| 3 | `ABS_NOTE` | VARCHAR(255) |  |  | Free text entry for note taking use |
| 4 | `ABS_VALUE` | VARCHAR(250) |  |  | What the value of the result was |
| 5 | `ADDED_DT_TM` | DATETIME |  |  | When this item was added by the system or front end user |
| 6 | `BEG_EFFECTIVE_DT_TM` | DATETIME |  |  | The date and time for which this table row becomes effective. Normally, this will be the date and time the row is added, but could be a past or future date and time. |
| 7 | `BR_DATAMART_CATEGORY_ID` | DOUBLE | NOT NULL |  | Identifies the Category (i.e. Stroke, VTE, or ED Throughput). Foreign Key to BR_DATAMART_CATEGORY |
| 8 | `ENCNTR_ID` | DOUBLE | NOT NULL |  | Identifies the encounter against which the quality measure is associated. Foreign key to the ENCOUNTER table. |
| 9 | `END_EFFECTIVE_DT_TM` | DATETIME |  |  | The date/time after which the row is no longer valid as active current data. This may be valued with the date that the row became inactive. |
| 10 | `EXTRACT_DT_TM` | DATETIME |  |  | The date/time that the record was extracted from the source system. |
| 11 | `FIRST_PROCESS_DT_TM` | DATETIME |  |  | The date/time the record was first loaded into the table. |
| 12 | `HEALTH_SYSTEM_ID` | DOUBLE | NOT NULL |  | Identifies the delivery network responsible for supplying the data. |
| 13 | `HEALTH_SYSTEM_SOURCE_ID` | DOUBLE | NOT NULL |  | Identifies the unique source within the delivery network responsible for supplying the data. |
| 14 | `LAST_PROCESS_DT_TM` | DATETIME |  |  | The date/time the record was last loaded into the table. |
| 15 | `LH_ABS_QUESTION_ID` | DOUBLE | NOT NULL |  | Identifies the Question that is being answered. Foreign key to LH_ABS_QUESTION. |
| 16 | `LH_ABS_SCRATCHPAD_ID` | DOUBLE | NOT NULL |  | Unique generated number that identifies a single row on the LH_ABS_SCRATCHPAD table. |
| 17 | `PARENT_ENTITY_ID` | DOUBLE | NOT NULL |  | The ID of the Order, Document, Result, etc¿ if not user-defined |
| 18 | `PARENT_ENTITY_NAME` | VARCHAR(50) |  |  | The table the entry came from if not user-defined |
| 19 | `SOURCE` | VARCHAR(75) |  |  | The general name of where this entry came from I.E. "Orders", "Documents". |
| 20 | `UPDT_CNT` | DOUBLE |  |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 21 | `UPDT_DT_TM` | DATETIME |  |  | The date and time the row was last inserted or updated. |
| 22 | `UPDT_SOURCE` | VARCHAR(50) |  |  | The script name responsible for updating the record. |
| 23 | `UPDT_TASK` | VARCHAR(50) |  |  | The registered (assigned) task number for the process that inserted or updated the row. |
| 24 | `USER_ID` | DOUBLE | NOT NULL |  | The person_id of the user that answered the question. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

