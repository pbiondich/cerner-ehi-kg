# CLRFCTN_RESPONSE

> Clarification responses suggested by the DQR inference engine

**Description:** CLRFCTN_RESPONSE  
**Table type:** ACTIVITY  
**Primary key:** `CLRFCTN_RESPONSE_ID`  
**Columns:** 8  
**Referenced by:** 1 columns

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `CLARIFICATION_ID` | DOUBLE | NOT NULL | FK→ | Unique identifier on CLARIFICATION table |
| 2 | `CLRFCTN_RESPONSE_ID` | DOUBLE | NOT NULL | PK | Unique generated number that identifies a single row on the CLARIFICATION_RESPONSE table. |
| 3 | `PROPOSED_TEXT_ID` | DOUBLE | NOT NULL | FK→ | Proposed documentation text to go in the document if the clarification response is accepted |
| 4 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 5 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 6 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 7 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 8 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `CLARIFICATION_ID` | [CLARIFICATION](CLARIFICATION.md) | `CLARIFICATION_ID` |
| `PROPOSED_TEXT_ID` | [LONG_TEXT](LONG_TEXT.md) | `LONG_TEXT_ID` |

## Referenced by (1)

| From table | Column |
|------------|--------|
| [CLRFCTN_ACTION](CLRFCTN_ACTION.md) | `CLRFCTN_RESPONSE_ID` |

