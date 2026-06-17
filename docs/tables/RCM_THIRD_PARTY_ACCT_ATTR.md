# RCM_THIRD_PARTY_ACCT_ATTR

> This table stores third party additional security attribute informaiton

**Description:** RevWorks Care Management - Third Party Account Attribute  
**Table type:** REFERENCE  
**Primary key:** _(not published — see note)_  
**Columns:** 9

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ATTRIBUTE_TYPE_CD` | DOUBLE | NOT NULL |  | Identifies the type of attribute for the account. |
| 2 | `LONG_TEXT_ID` | DOUBLE | NOT NULL | FK→ | Uniquely identifies the record on the long text reference table which contains the information of the attribute. |
| 3 | `RCM_THIRD_PARTY_ACCOUNT_ID` | DOUBLE | NOT NULL | FK→ | Uniquely identifies the third party account to which these attributes relate. |
| 4 | `RCM_THIRD_PARTY_ACCT_ATTR_ID` | DOUBLE | NOT NULL |  | Uniquely identifies additional security attribute information related to a given account. |
| 5 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 6 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 7 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 8 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 9 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `LONG_TEXT_ID` | [LONG_TEXT_REFERENCE](LONG_TEXT_REFERENCE.md) | `LONG_TEXT_ID` |
| `RCM_THIRD_PARTY_ACCOUNT_ID` | [RCM_THIRD_PARTY_ACCOUNT](RCM_THIRD_PARTY_ACCOUNT.md) | `RCM_THIRD_PARTY_ACCOUNT_ID` |

