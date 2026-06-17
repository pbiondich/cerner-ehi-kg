# RCM_THIRD_PARTY_ACCT_ORG_R

> This table stores third party account and facility relationship information

**Description:** RevWorks Care Management Third Party Account Organization Reltionship  
**Table type:** REFERENCE  
**Primary key:** _(not published — see note)_  
**Columns:** 9

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ORGANIZATION_ALIAS` | VARCHAR(100) |  |  | A third party alias value that is assigned to the organization for the account. A facility code would be an example for Curaspan. |
| 2 | `ORGANIZATION_ID` | DOUBLE | NOT NULL | FK→ | Uniquely identifies the facility organization related to the given account. |
| 3 | `RCM_THIRD_PARTY_ACCOUNT_ID` | DOUBLE | NOT NULL | FK→ | Uniquely identifies the Account to which the facility is related. |
| 4 | `RCM_THIRD_PARTY_ACCT_ORG_R_ID` | DOUBLE | NOT NULL |  | Uniquely identifies a relationship between an account and a facility. |
| 5 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 6 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 7 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 8 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 9 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `ORGANIZATION_ID` | [ORGANIZATION](ORGANIZATION.md) | `ORGANIZATION_ID` |
| `RCM_THIRD_PARTY_ACCOUNT_ID` | [RCM_THIRD_PARTY_ACCOUNT](RCM_THIRD_PARTY_ACCOUNT.md) | `RCM_THIRD_PARTY_ACCOUNT_ID` |

