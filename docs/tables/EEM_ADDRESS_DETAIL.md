# EEM_ADDRESS_DETAIL

> A row represents summary of transaction data.

**Description:** Update Address Transaction Summary  
**Table type:** ACTIVITY  
**Primary key:** _(not published — see note)_  
**Columns:** 15

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ADDRESS_GUESS_IND` | DOUBLE | NOT NULL |  | Ministry Address Guess Indicator |
| 2 | `INTERCHANGE_ID` | DOUBLE | NOT NULL |  | This is the record number for interchange. |
| 3 | `PAYER_ID` | DOUBLE | NOT NULL | FK→ | Key to Organization table |
| 4 | `PERSON_ID` | DOUBLE | NOT NULL | FK→ | This is the value of the unique primary identifier of the person table. It is an internal system assigned number. |
| 5 | `PHN` | VARCHAR(200) |  |  | Personal Health Number (Person alias) |
| 6 | `PROFILE_ID` | DOUBLE | NOT NULL | FK→ | Profile ID. |
| 7 | `REPLY_DT_TM` | DATETIME |  |  | Date and Time the response was received |
| 8 | `SENDER_PRSNL_ID` | DOUBLE | NOT NULL | FK→ | Transaction sender Identifier |
| 9 | `SENT_DT_TM` | DATETIME | NOT NULL |  | Transaction sent date and time |
| 10 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 11 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 12 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 13 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 14 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |
| 15 | `VALID_ADDRESS_IND` | DOUBLE | NOT NULL |  | Valid Address Indicator |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `PAYER_ID` | [ORGANIZATION](ORGANIZATION.md) | `ORGANIZATION_ID` |
| `PERSON_ID` | [PERSON](PERSON.md) | `PERSON_ID` |
| `PROFILE_ID` | [EEM_PROFILE](EEM_PROFILE.md) | `PROFILE_ID` |
| `SENDER_PRSNL_ID` | [PRSNL](PRSNL.md) | `PERSON_ID` |

