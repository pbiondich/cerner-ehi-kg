# EEM_COVERAGE_DETAIL

> A row represents summary of transaction data

**Description:** Query Beneficiary Coverage Status Transaction Summary  
**Table type:** ACTIVITY  
**Primary key:** _(not published — see note)_  
**Columns:** 17

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ELIGIBLE_FLAG` | DOUBLE | NOT NULL |  | Indicates the status of the data w/in the transaction (not of the transaction itself). 0 - Error (response never came back) 1 - Eligible 2 - Denied 3 - Unknown (response was back but not filled/cannot determine |
| 2 | `FIRST_NAME` | VARCHAR(200) |  |  | Patient First Name |
| 3 | `INTERCHANGE_ID` | DOUBLE | NOT NULL |  | Interchange id of the transaction that this detail data came from. |
| 4 | `LAST_NAME` | VARCHAR(200) |  |  | Last Name |
| 5 | `PAYER_ID` | DOUBLE | NOT NULL | FK→ | Key to Organization table |
| 6 | `PERSON_ID` | DOUBLE | NOT NULL | FK→ | This is the value of the unique primary identifier of the person table. It is an internal system assigned number. |
| 7 | `PHN` | VARCHAR(200) |  |  | Personal Health Number (Person alias) |
| 8 | `PROFILE_ID` | DOUBLE | NOT NULL | FK→ | Profile ID. |
| 9 | `REPLY_DT_TM` | DATETIME |  |  | The date and time that the transaction's reply came back. |
| 10 | `SENDER_PRSNL_ID` | DOUBLE | NOT NULL | FK→ | Sender Personnel Identifier |
| 11 | `SENT_DT_TM` | DATETIME | NOT NULL |  | The date and time that the transaction was sent. |
| 12 | `TERM_DT_TM` | DATETIME |  |  | Patient termination date/time |
| 13 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 14 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 15 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 16 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 17 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `PAYER_ID` | [ORGANIZATION](ORGANIZATION.md) | `ORGANIZATION_ID` |
| `PERSON_ID` | [PERSON](PERSON.md) | `PERSON_ID` |
| `PROFILE_ID` | [EEM_PROFILE](EEM_PROFILE.md) | `PROFILE_ID` |
| `SENDER_PRSNL_ID` | [PRSNL](PRSNL.md) | `PERSON_ID` |

