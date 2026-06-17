# LH_ABS_CASE_NOTES

> Case Notes for records being abstracted in the Lighthouse Abstractor (eQuality Check)

**Description:** LH_ABS_CASE_NOTES  
**Table type:** ACTIVITY  
**Primary key:** _(not published — see note)_  
**Columns:** 17

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `BEG_EFFECTIVE_DT_TM` | DATETIME |  |  | The date and time for which this table row becomes effective. Normally, this will be the date and time the row is added, but could be a past or future date and time. |
| 2 | `BR_DATAMART_CATEGORY_ID` | DOUBLE | NOT NULL |  | Holds the br_datamart_category_id of the condition and version that the case note was added for. Possibly zero in the case of condition spanning older styled case notes. |
| 3 | `CREATE_DT_TM` | DATETIME |  |  | Date time the case note was created |
| 4 | `ENCNTR_ID` | DOUBLE | NOT NULL |  | Identifies the encounter against which the quality measure is associated. Foreign key to the ENCOUNTER table. |
| 5 | `END_EFFECTIVE_DT_TM` | DATETIME |  |  | The date/time after which the row is no longer valid as active current data. This may be valued with the date that the row became inactive. |
| 6 | `EXTRACT_DT_TM` | DATETIME |  |  | The date/time that the record was extracted from the source system. |
| 7 | `FIRST_PROCESS_DT_TM` | DATETIME |  |  | The date/time the record was first loaded into the table. |
| 8 | `HEALTH_SYSTEM_ID` | DOUBLE | NOT NULL |  | Identifies the delivery network responsible for supplying the data. |
| 9 | `HEALTH_SYSTEM_SOURCE_ID` | DOUBLE | NOT NULL |  | Identifies the unique source within the delivery network responsible for supplying the data. |
| 10 | `LAST_PROCESS_DT_TM` | DATETIME |  |  | The date/time the record was last loaded into the table. |
| 11 | `LH_ABS_CASE_NOTES_ID` | DOUBLE | NOT NULL |  | Unique generated number that identifies a single row on the LH_ABS_CASE_NOTES table. |
| 12 | `NOTES_TXT` | VARCHAR(3200) |  |  | Case Notes related to this visit |
| 13 | `UPDT_CNT` | DOUBLE |  |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 14 | `UPDT_DT_TM` | DATETIME |  |  | The date and time the row was last inserted or updated. |
| 15 | `UPDT_SOURCE` | VARCHAR(50) |  |  | The script name responsible for updating the record. |
| 16 | `UPDT_TASK` | VARCHAR(50) |  |  | The registered (assigned) task number for the process that inserted or updated the row. |
| 17 | `USER_ID` | DOUBLE | NOT NULL |  | The person_id of the user that answered the question. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

