# TRANSACTION_ADDRESS_VERIFY

> Stores information to track addresss verification transaction history for a person.

**Description:** Transaction Address Verify  
**Table type:** ACTIVITY  
**Primary key:** _(not published — see note)_  
**Columns:** 14

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `PERSON_ID` | DOUBLE | NOT NULL | FK→ | Unique identifier to the person table for the person whose address was submitted for verification. |
| 2 | `REPLY_DT_TM` | DATETIME |  |  | The date and time the address verification transaction response was received inbound. |
| 3 | `REQUEST_LONG_TEXT_ID` | DOUBLE | NOT NULL | FK→ | Unique identifier of the long text table for storing the outbound request message |
| 4 | `RESPONSE_LONG_TEXT_ID` | DOUBLE | NOT NULL | FK→ | Unique identifier of the long text table for storing the inbound response message |
| 5 | `SENT_DT_TM` | DATETIME | NOT NULL |  | The date and time the address verification transaction was sent outbound. If an error occurred, it is the date and time the transaction was attempted |
| 6 | `SUBMITTER_PRSNL_ID` | DOUBLE | NOT NULL | FK→ | Unique identifier of the personnel that submitted the transaction outbound. |
| 7 | `TRANSACTION_ADDRESS_VERIFY_ID` | DOUBLE | NOT NULL |  | Unique generated number that identifies a single row on the TRANSACTION_ADDRESS_VERIFY table. |
| 8 | `TRANSACTION_SOURCE_IDENT` | VARCHAR(50) |  |  | The unique identifier of the transaction as assigned by Transaction Services. Links the transaction between a Millennium domain and Transaction Services. |
| 9 | `TRANSACTION_STATUS_CD` | DOUBLE | NOT NULL |  | The high level status of the transaction. |
| 10 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 11 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 12 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 13 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 14 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `PERSON_ID` | [PERSON](PERSON.md) | `PERSON_ID` |
| `REQUEST_LONG_TEXT_ID` | [LONG_TEXT](LONG_TEXT.md) | `LONG_TEXT_ID` |
| `RESPONSE_LONG_TEXT_ID` | [LONG_TEXT](LONG_TEXT.md) | `LONG_TEXT_ID` |
| `SUBMITTER_PRSNL_ID` | [PRSNL](PRSNL.md) | `PERSON_ID` |

