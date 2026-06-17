# BR_BP_RSLINK

> Stores right side links for activity groups and activities

**Description:** Bedrock BP Rslink  
**Table type:** REFERENCE  
**Primary key:** _(not published — see note)_  
**Columns:** 10

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `BEDROCK_ENTITY_MEAN` | VARCHAR(100) |  |  | Identifier for the parent |
| 2 | `BEDROCK_ENTITY_NAME` | VARCHAR(100) |  |  | Identifies what table the parent came from |
| 3 | `BR_BP_RSLINK_ID` | DOUBLE | NOT NULL |  | Unique ID |
| 4 | `RSLINK_TEXT` | VARCHAR(200) |  |  | Text for right side link |
| 5 | `RSLINK_URL` | VARCHAR(500) |  |  | URL for right side link to follow |
| 6 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 7 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 8 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 9 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 10 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

