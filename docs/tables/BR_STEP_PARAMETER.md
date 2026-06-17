# BR_STEP_PARAMETER

> Parameters of a Bedrock Step, which represents a Bedrock Wizard entity. The parameters are used as metadata that needs to be defined for that particular Bedrock Step to function as intended by the Bedrock application. Not all Bedrock Steps need parameters defined, therefore this is optional metadata for a Bedrock Step.

**Description:** Bedrock Step Parameter  
**Table type:** REFERENCE  
**Primary key:** _(not published — see note)_  
**Columns:** 10

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `BR_STEP_PARAMETER_ID` | DOUBLE | NOT NULL |  | Unique generated number that identifies a single row on the br_step_parameter table. |
| 2 | `PARAMETER_NAME` | VARCHAR(100) | NOT NULL |  | The name of the step parameter. It is used as the key in the pairing between parameter_name and parameter_value. The name needs to be known to the Bedrock application for it to be used in a meaningful way. |
| 3 | `PARAMETER_SEQ` | DOUBLE | NOT NULL |  | The functional sequence of parameters with the same step_mean. This is an optional field and is only to be used if the sequence is of functional value. Otherwise, the default of 0 should be used. |
| 4 | `PARAMETER_VALUE` | VARCHAR(255) | NOT NULL |  | The value of the step parameter. It is used as the value in the pairing between parameter_name and parameter_value. |
| 5 | `STEP_MEAN` | VARCHAR(100) | NOT NULL |  | Short Name of the step |
| 6 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 7 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 8 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 9 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 10 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

