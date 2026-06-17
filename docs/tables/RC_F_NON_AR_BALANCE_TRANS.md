# RC_F_NON_AR_BALANCE_TRANS

> This table contains data related to Non AR account transaction balance

**Description:** Revenue Cycle Fact Non Accounts Receivable Balance Transaction  
**Table type:** ACTIVITY  
**Primary key:** _(not published — see note)_  
**Columns:** 21

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ACTIVITY_DT_NBR` | DOUBLE | NOT NULL | FK→ | A number representing the activity date. References the key in the OMF_DATE table. |
| 2 | `MILL_ACTIVITY_ID` | DOUBLE | NOT NULL |  | Number that identifies the row in the pft_trans_reltn millennium database table from which this row was derived. |
| 3 | `MILL_LOGICAL_DOMAIN_ID` | DOUBLE | NOT NULL |  | Uniquely identifies the related logical domain record. |
| 4 | `POST_DT_NBR` | DOUBLE | NOT NULL | FK→ | A number representing the post date. References the key in the OMF_DATE table. |
| 5 | `RC_D_ACCOUNT_ID` | DOUBLE | NOT NULL | FK→ | Uniquely identifies the related account record. |
| 6 | `RC_D_ACCOUNT_TYPE_ID` | DOUBLE | NOT NULL | FK→ | Unique genereated number that identifies the row on the rc_d_account_type table related to this fact. |
| 7 | `RC_D_BILLING_ENTITY_ID` | DOUBLE | NOT NULL | FK→ | Uniquely identifies billing entity information related to this fact row. |
| 8 | `RC_D_GL_ALIAS_ID` | DOUBLE | NOT NULL | FK→ | Uniquely identifies the GL Alias information associated to this fact row. |
| 9 | `RC_D_OTHER_GL_ALIAS_ID` | DOUBLE | NOT NULL | FK→ | Uniquely identifies GL alias information such as company name and account name for alias other than NON AR GL Alias |
| 10 | `RC_D_TRANSACTION_ALIAS_ID` | DOUBLE | NOT NULL | FK→ | Uniquely identifies a Transaction Alias Dimension row related to this fact row |
| 11 | `RC_D_TRANSACTION_BATCH_ID` | DOUBLE | NOT NULL | FK→ | Uniquely identifies a Transaction Batch Dimension row related to this fact row |
| 12 | `RC_D_TRANSACTION_TYPE_ID` | DOUBLE | NOT NULL | FK→ | Uniquely identifies a Transaction Type Dimension row realted to this fact row |
| 13 | `RC_F_NON_AR_BALANCE_TRANS_ID` | DOUBLE | NOT NULL |  | Unique generated number that identifies a single row on the RC_F_NON_AR_BALANCE_TRANS table. |
| 14 | `SHR_D_POSTING_PRSNL_ID` | DOUBLE | NOT NULL | FK→ | Uniquely identifies a row on the Shared Person Dimension table that represents the person who posted the information about the related fact row |
| 15 | `TIME_ZONE_INDEX` | DOUBLE | NOT NULL |  | Stores the time zone from which the data was extracted. |
| 16 | `TRANSACTION_AMT` | DOUBLE | NOT NULL |  | Contains the dollar amount associated to the given transaction. |
| 17 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 18 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 19 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 20 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 21 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `ACTIVITY_DT_NBR` | [OMF_DATE](OMF_DATE.md) | `DT_NBR` |
| `POST_DT_NBR` | [OMF_DATE](OMF_DATE.md) | `DT_NBR` |
| `RC_D_ACCOUNT_ID` | [RC_D_ACCOUNT](RC_D_ACCOUNT.md) | `RC_D_ACCOUNT_ID` |
| `RC_D_ACCOUNT_TYPE_ID` | [RC_D_ACCOUNT_TYPE](RC_D_ACCOUNT_TYPE.md) | `RC_D_ACCOUNT_TYPE_ID` |
| `RC_D_BILLING_ENTITY_ID` | [RC_D_BILLING_ENTITY](RC_D_BILLING_ENTITY.md) | `RC_D_BILLING_ENTITY_ID` |
| `RC_D_GL_ALIAS_ID` | [RC_D_GL_ALIAS](RC_D_GL_ALIAS.md) | `RC_D_GL_ALIAS_ID` |
| `RC_D_OTHER_GL_ALIAS_ID` | [RC_D_GL_ALIAS](RC_D_GL_ALIAS.md) | `RC_D_GL_ALIAS_ID` |
| `RC_D_TRANSACTION_ALIAS_ID` | [RC_D_TRANSACTION_ALIAS](RC_D_TRANSACTION_ALIAS.md) | `RC_D_TRANSACTION_ALIAS_ID` |
| `RC_D_TRANSACTION_BATCH_ID` | [RC_D_TRANSACTION_BATCH](RC_D_TRANSACTION_BATCH.md) | `RC_D_TRANSACTION_BATCH_ID` |
| `RC_D_TRANSACTION_TYPE_ID` | [RC_D_TRANSACTION_TYPE](RC_D_TRANSACTION_TYPE.md) | `RC_D_TRANSACTION_TYPE_ID` |
| `SHR_D_POSTING_PRSNL_ID` | [SHR_D_PERSON](SHR_D_PERSON.md) | `SHR_D_PERSON_ID` |

