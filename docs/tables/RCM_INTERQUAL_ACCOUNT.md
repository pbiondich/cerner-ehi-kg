# RCM_INTERQUAL_ACCOUNT

> Stores interqual account information.

**Description:** RevWorks Care Management Interqual Account  
**Table type:** REFERENCE  
**Primary key:** `RCM_INTERQUAL_ACCOUNT_ID`  
**Columns:** 11  
**Referenced by:** 1 columns

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ACCOUNT_DESC` | VARCHAR(100) | NOT NULL |  | A unique description of the account. |
| 2 | `ACCOUNT_PASSWORD` | VARCHAR(150) | NOT NULL |  | The encrypted InterQual account password. |
| 3 | `ACCOUNT_USERNAME` | VARCHAR(100) | NOT NULL |  | The InterQual Account username. |
| 4 | `PARAMS_LONG_TEXT_ID` | DOUBLE | NOT NULL |  | Uniquely identifies the interqual parameters xml. |
| 5 | `RCM_INTERQUAL_ACCOUNT_ID` | DOUBLE | NOT NULL | PK | Uniquely identifies and InterQual account. |
| 6 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 7 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 8 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 9 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 10 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |
| 11 | `URL_LONG_TEXT_ID` | DOUBLE | NOT NULL | FK→ | Contains the InterQual URL. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `URL_LONG_TEXT_ID` | [LONG_TEXT_REFERENCE](LONG_TEXT_REFERENCE.md) | `LONG_TEXT_ID` |

## Referenced by (1)

| From table | Column |
|------------|--------|
| [RCM_INTERQUAL_ACCT_ORG_R](RCM_INTERQUAL_ACCT_ORG_R.md) | `RCM_INTERQUAL_ACCOUNT_ID` |

