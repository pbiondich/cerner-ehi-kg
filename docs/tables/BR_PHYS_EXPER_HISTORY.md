# BR_PHYS_EXPER_HISTORY

> Stores the history of changes made to the physician experience preferences.

**Description:** Bedrock Physician Experience History  
**Table type:** REFERENCE  
**Primary key:** _(not published — see note)_  
**Columns:** 12

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `BR_PHYS_EXPER_HISTORY_ID` | DOUBLE | NOT NULL |  | Unique, generated number that identifies a single row on the BR_PHYS_EXPER_HISTORY table. |
| 2 | `NEW_VALUE` | VARCHAR(100) | NOT NULL |  | The new value that was set for the preference. |
| 3 | `POSITION_CD` | DOUBLE | NOT NULL |  | The position that was updated. |
| 4 | `PREFERENCE_NAME` | VARCHAR(100) | NOT NULL |  | The preference name that was updated. |
| 5 | `PREVIOUS_VALUE` | VARCHAR(100) | NOT NULL |  | The previous value for the preference. |
| 6 | `TOPIC_NAME` | VARCHAR(100) | NOT NULL |  | The topic that was updated. |
| 7 | `TRANSACTION_DT_TM` | DATETIME | NOT NULL |  | The time that the update was made. |
| 8 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 9 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 10 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 11 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 12 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

