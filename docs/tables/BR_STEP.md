# BR_STEP

> list of Bedrock wizards

**Description:** BEDROCK STEP  
**Table type:** REFERENCE  
**Primary key:** _(not published — see note)_  
**Columns:** 12

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `DEFAULT_SEQ` | DOUBLE |  |  | order in which the step will display |
| 2 | `EST_MIN_TO_COMPLETE` | DOUBLE | NOT NULL |  | estimated minutes to complete the step |
| 3 | `STEP_CAT_DISP` | VARCHAR(100) |  |  | display name of the step category |
| 4 | `STEP_CAT_MEAN` | VARCHAR(100) |  |  | category of the step (pathnet, core, etc.) |
| 5 | `STEP_DISP` | VARCHAR(100) | NOT NULL |  | front-end display name |
| 6 | `STEP_MEAN` | VARCHAR(100) | NOT NULL |  | short name of step |
| 7 | `STEP_TYPE` | VARCHAR(100) | NOT NULL |  | type of step |
| 8 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 9 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 10 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | date/time on which the record was added to the file |
| 11 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 12 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

