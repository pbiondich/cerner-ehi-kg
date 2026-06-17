# VALID_RESPONSE

> A Cerner-defined reference table of the valid responses for each question to be asked in the DB Preference Wizard. Used by Blood Bank Transfusion, Blood Bank Donor, and PharmNet at this time.

**Description:** Valid Response  
**Table type:** REFERENCE  
**Primary key:** `QUESTION_CD`, `RESPONSE_CD`  
**Columns:** 10  
**Referenced by:** 2 columns

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `MODULE_CD` | DOUBLE | NOT NULL |  | The Cerner-defined module to which the question pertains (ex. "PathNet Blood Bank Transfusion", "Pharmacy"). |
| 2 | `PROCESS_CD` | DOUBLE | NOT NULL |  | The Cerner-defined process within the module to which the question pertains (ex. the "Dispense" process within the PathNet Blood Bank Transfusion module). |
| 3 | `QUESTION_CD` | DOUBLE | NOT NULL | PK FK→ | The code value of the Cerner-defined question for which the valid response is defined. |
| 4 | `RESPONSE` | VARCHAR(40) |  |  | Not currently used. |
| 5 | `RESPONSE_CD` | DOUBLE | NOT NULL | PK | The code value of the actual response (ex. "Yes", "No", etc.) that is defined by Cerner as valid for this question. |
| 6 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 7 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 8 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 9 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 10 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `QUESTION_CD` | [QUESTION](QUESTION.md) | `QUESTION_CD` |

## Referenced by (2)

| From table | Column |
|------------|--------|
| [DEPENDENCY](DEPENDENCY.md) | `QUESTION_CD` |
| [DEPENDENCY](DEPENDENCY.md) | `RESPONSE_CD` |

