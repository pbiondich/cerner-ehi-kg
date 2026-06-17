# RCM_TLC_ACCT_LD_R

> Account Logical domain relation Total Living Choices Account Logical Domain Identifier

**Description:** RevWorks Care Management - Total Living Choices Account Logical Domain ID  
**Table type:** REFERENCE  
**Primary key:** _(not published — see note)_  
**Columns:** 8

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `LOGICAL_DOMAIN_ID` | DOUBLE | NOT NULL | FK→ | Uniquely identifies the related logical domain. |
| 2 | `RCM_TLC_ACCOUNT_ID` | DOUBLE | NOT NULL | FK→ | Uniquely identifies the related account |
| 3 | `RCM_TLC_ACCT_LD_R_ID` | DOUBLE | NOT NULL |  | Uniquely identifies the relationship between the account and the logical domain table. |
| 4 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 5 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 6 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 7 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 8 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `LOGICAL_DOMAIN_ID` | [LOGICAL_DOMAIN](LOGICAL_DOMAIN.md) | `LOGICAL_DOMAIN_ID` |
| `RCM_TLC_ACCOUNT_ID` | [RCM_TLC_ACCOUNT](RCM_TLC_ACCOUNT.md) | `RCM_TLC_ACCOUNT_ID` |

