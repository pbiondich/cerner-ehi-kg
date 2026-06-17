# RCM_THIRD_PARTY_ACCOUNT

> This stable stores third party account information for RevWorks Care Management system

**Description:** RevWorks Care Management - Third Party Account  
**Table type:** REFERENCE  
**Primary key:** `RCM_THIRD_PARTY_ACCOUNT_ID`  
**Columns:** 11  
**Referenced by:** 2 columns

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ACCOUNT_NAME` | VARCHAR(100) | NOT NULL |  | Stores the name of the account. |
| 2 | `ALL_FACILITY_IND` | DOUBLE | NOT NULL |  | Indicates this account is shared for all the facilities within the logical domain. |
| 3 | `LOGICAL_DOMAIN_ID` | DOUBLE | NOT NULL | FK→ | The identifier of the logical domain for the account. This identifies the data to be grouped by logical domain |
| 4 | `RCM_THIRD_PARTY_ACCOUNT_ID` | DOUBLE | NOT NULL | PK | Uniquely identifies a third party account. |
| 5 | `THIRD_PARTY_TYPE_CD` | DOUBLE | NOT NULL |  | The type of the third party such as JATA or MILLIMAN. |
| 6 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 7 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 8 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 9 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 10 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |
| 11 | `URL_LONG_TEXT_ID` | DOUBLE | NOT NULL | FK→ | Uniquely identifies the record on the long text reference table that is related to the URL. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `LOGICAL_DOMAIN_ID` | [LOGICAL_DOMAIN](LOGICAL_DOMAIN.md) | `LOGICAL_DOMAIN_ID` |
| `URL_LONG_TEXT_ID` | [LONG_TEXT_REFERENCE](LONG_TEXT_REFERENCE.md) | `LONG_TEXT_ID` |

## Referenced by (2)

| From table | Column |
|------------|--------|
| [RCM_THIRD_PARTY_ACCT_ATTR](RCM_THIRD_PARTY_ACCT_ATTR.md) | `RCM_THIRD_PARTY_ACCOUNT_ID` |
| [RCM_THIRD_PARTY_ACCT_ORG_R](RCM_THIRD_PARTY_ACCT_ORG_R.md) | `RCM_THIRD_PARTY_ACCOUNT_ID` |

