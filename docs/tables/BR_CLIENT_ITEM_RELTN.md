# BR_CLIENT_ITEM_RELTN

> solutions & steps for each client

**Description:** BEDROCK CLIENT ITEM RELATIONSHIP  
**Table type:** REFERENCE  
**Primary key:** _(not published — see note)_  
**Columns:** 17

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `BR_CLIENT_ID` | DOUBLE | NOT NULL |  | Identifies which bedrock client data belongs to |
| 2 | `BR_CLIENT_ITEM_RELTN_ID` | DOUBLE | NOT NULL |  | Unique identifier for this table |
| 3 | `ITEM_DISPLAY` | VARCHAR(255) | NOT NULL |  | the display value of the ""STEP"" or ""SOLUTION"" |
| 4 | `ITEM_MEAN` | VARCHAR(255) | NOT NULL |  | the meaning of the ""STEP"" or ""SOLUTION"" |
| 5 | `ITEM_TYPE` | VARCHAR(255) | NOT NULL |  | Type of Item |
| 6 | `SOLUTION_SEQ` | DOUBLE |  |  | display sequence of the solution on the bedrock implementation page |
| 7 | `SOLUTION_TYPE_FLAG` | DOUBLE | NOT NULL |  | flag to identify the type of solution in the application (0=design/build,1=lighthouse) |
| 8 | `STATUS_DT_TM` | DATETIME |  |  | date/time the status was last updated |
| 9 | `STATUS_FLAG` | DOUBLE | NOT NULL |  | status of the step - not started (0), in process (1) or complete (2) |
| 10 | `STATUS_ID` | DOUBLE | NOT NULL |  | identifier of the user that caused the change in status - from the br_prsnl table |
| 11 | `STEP_CAT_DISP` | VARCHAR(100) |  |  | display associated with the solution of the step (i.e. PowerChart Office) |
| 12 | `STEP_CAT_MEAN` | VARCHAR(100) |  |  | meaning associated with the solution of the step (i.e. PCO) |
| 13 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 14 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 15 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 16 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 17 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

