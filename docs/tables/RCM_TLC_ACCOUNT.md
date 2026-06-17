# RCM_TLC_ACCOUNT

> This table is used to find facilities to place patients who are being discharged.

**Description:** RevWorks Care Management - Total Living Choices Account  
**Table type:** REFERENCE  
**Primary key:** `RCM_TLC_ACCOUNT_ID`  
**Columns:** 10  
**Referenced by:** 2 columns

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ACCOUNT_DESC` | VARCHAR(100) | NOT NULL |  | The description of the account. Must be unique. |
| 2 | `RCM_TLC_ACCOUNT_ID` | DOUBLE | NOT NULL | PK | Uniquely identifies a TCL account. |
| 3 | `TLC_PRIVATE_KEY_LONG_TEXT_ID` | DOUBLE | NOT NULL | FK→ | Uniquely identifies the long text record related to the private key. |
| 4 | `TLC_PUBLIC_KEY_LONG_TEXT_ID` | DOUBLE | NOT NULL | FK→ | Uniquely identifies the record on the long text reference table related to the public key. |
| 5 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 6 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 7 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 8 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 9 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |
| 10 | `URL_LONG_TEXT_ID` | DOUBLE | NOT NULL | FK→ | Uniquely identifies the record on the long text reference table that is related to the URL |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `TLC_PRIVATE_KEY_LONG_TEXT_ID` | [LONG_TEXT_REFERENCE](LONG_TEXT_REFERENCE.md) | `LONG_TEXT_ID` |
| `TLC_PUBLIC_KEY_LONG_TEXT_ID` | [LONG_TEXT_REFERENCE](LONG_TEXT_REFERENCE.md) | `LONG_TEXT_ID` |
| `URL_LONG_TEXT_ID` | [LONG_TEXT_REFERENCE](LONG_TEXT_REFERENCE.md) | `LONG_TEXT_ID` |

## Referenced by (2)

| From table | Column |
|------------|--------|
| [RCM_TLC_ACCT_LD_R](RCM_TLC_ACCT_LD_R.md) | `RCM_TLC_ACCOUNT_ID` |
| [RCM_TLC_ACCT_ORG_R](RCM_TLC_ACCT_ORG_R.md) | `RCM_TLC_ACCOUNT_ID` |

