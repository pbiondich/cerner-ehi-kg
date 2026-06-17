# CLRFCTN_ACTION

> Clarification responses suggested by the DQR inference engine

**Description:** Clarification Response  
**Table type:** ACTIVITY  
**Primary key:** _(not published — see note)_  
**Columns:** 13

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ACCEPTED_TEXT_ID` | DOUBLE | NOT NULL | FK→ | The (potentially modified) documentation text that the physician accepts |
| 2 | `ACTION_CD` | DOUBLE | NOT NULL |  | The action taken by the physician on the clarification |
| 3 | `ACTION_DT_TM` | DATETIME |  |  | The date and time at which the personnel took action on the clarification |
| 4 | `ACTION_PRSNL_ID` | DOUBLE | NOT NULL | FK→ | The personnel who took action on the clarification |
| 5 | `CLARIFICATION_ID` | DOUBLE | NOT NULL | FK→ | Unique identifier on CLARIFICATION table |
| 6 | `CLRFCTN_ACTION_ID` | DOUBLE | NOT NULL |  | PRIMARY KEY |
| 7 | `CLRFCTN_RESPONSE_ID` | DOUBLE | NOT NULL | FK→ | Unique identifier on CLARIFICATION RESPONSE table |
| 8 | `DIAGNOSIS_ID` | DOUBLE | NOT NULL | FK→ | The diagnosis entered when physician accept the clarification |
| 9 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 10 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 11 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 12 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 13 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `ACCEPTED_TEXT_ID` | [LONG_TEXT](LONG_TEXT.md) | `LONG_TEXT_ID` |
| `ACTION_PRSNL_ID` | [PRSNL](PRSNL.md) | `PERSON_ID` |
| `CLARIFICATION_ID` | [CLARIFICATION](CLARIFICATION.md) | `CLARIFICATION_ID` |
| `CLRFCTN_RESPONSE_ID` | [CLRFCTN_RESPONSE](CLRFCTN_RESPONSE.md) | `CLRFCTN_RESPONSE_ID` |
| `DIAGNOSIS_ID` | [DIAGNOSIS](DIAGNOSIS.md) | `DIAGNOSIS_ID` |

