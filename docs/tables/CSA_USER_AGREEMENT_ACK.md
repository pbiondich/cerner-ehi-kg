# CSA_USER_AGREEMENT_ACK

> This table contains data indicating a user of Cerner software has acknowledged a User Agreement for the software while logging on.

**Description:** CSA User Agreement Acknowledge  
**Table type:** ACTIVITY  
**Primary key:** _(not published — see note)_  
**Columns:** 11

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `BEG_EFFECTIVE_DT_TM` | DATETIME | NOT NULL |  | The date and time for which this table row becomes effective. Normally, this will be the date and time the row is added, but could be a past or future date and time. |
| 2 | `END_EFFECTIVE_DT_TM` | DATETIME | NOT NULL |  | The date/time after which the row is no longer valid as active current data. This may be valued with the date that the row became inactive. |
| 3 | `LOGINS_CNT` | DOUBLE | NOT NULL |  | The number of times a user has logged in during the time interval for the User Agreement. The length of the interval is kept in the CSA_USER_AGREEMENT table |
| 4 | `PERSON_ID` | DOUBLE | NOT NULL | FK→ | This is a foreign key to table PERSON. Used to identify the user who logged in. |
| 5 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 6 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 7 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 8 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 9 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |
| 10 | `USER_AGREEMENT_ACK_ID` | DOUBLE | NOT NULL |  | Primary key of this table. |
| 11 | `USER_AGREEMENT_ID` | DOUBLE | NOT NULL | FK→ | Foreign key to the CSA_USER_AGREEMENT table. Identifies the user agreement that was effective during this logon. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `PERSON_ID` | [PERSON](PERSON.md) | `PERSON_ID` |
| `USER_AGREEMENT_ID` | [CSA_USER_AGREEMENT](CSA_USER_AGREEMENT.md) | `USER_AGREEMENT_ID` |

