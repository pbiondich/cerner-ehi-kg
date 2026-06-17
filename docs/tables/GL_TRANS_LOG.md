# GL_TRANS_LOG

> General Ledger Transaction Log

**Description:** General Ledger Trans Log  
**Table type:** ACTIVITY  
**Primary key:** `GL_TRANS_LOG_ID`  
**Columns:** 41  
**Referenced by:** 2 columns

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ACCOUNT_ALIAS_NBR` | VARCHAR(50) |  |  | Number defining the account structure in the general account number |
| 2 | `ACCT_TYPE_CD` | DOUBLE | NOT NULL |  | Code value indicating the type of account. |
| 3 | `ACCT_UNIT_ALIAS_NBR` | VARCHAR(50) |  |  | Number defining the account unit in the general ledger account number |
| 4 | `ACTIVE_IND` | DOUBLE |  |  | The table row is active or inactive. A row is generally active unless it is in an inactive state such as logically deleted, combined away, pending purge, etc. |
| 5 | `ACTIVE_STATUS_CD` | DOUBLE | NOT NULL |  | Indicates the status of the row itself (not the data in the row) such as active, inactive, combined away, pending purge, etc. |
| 6 | `ACTIVE_STATUS_DT_TM` | DATETIME |  |  | The date and time that the active_status_cd was set. |
| 7 | `ACTIVE_STATUS_PRSNL_ID` | DOUBLE | NOT NULL |  | The person who caused the active_status_cd to be set or change. |
| 8 | `ACTIVITY_DT_TM` | DATETIME |  |  | The date and time GL activity occurred. |
| 9 | `ACTIVITY_ID` | DOUBLE | NOT NULL | FK→ | Foreign key to the trans_log table |
| 10 | `AMOUNT` | DOUBLE |  |  | Dollar amount to post to the particular gl account |
| 11 | `BEG_EFFECTIVE_DT_TM` | DATETIME |  |  | The date and time for which this table row becomes effective. Normally, this will be the date and time the row is added, but could be a past or future date and time. |
| 12 | `BILLING_ENTITY_ID` | DOUBLE | NOT NULL | FK→ | It indicates the BILLING_ENTITY_ID of respective ACTIVITY_ID |
| 13 | `COMPANY_ALIAS_NBR` | VARCHAR(50) |  |  | Number defining the company in the general ledger account number |
| 14 | `CREATED_DT_TM` | DATETIME |  |  | Date and time the record was created. |
| 15 | `CREATED_PRSNL_ID` | DOUBLE | NOT NULL | FK→ | Unique identifier of the person that created the record. |
| 16 | `DR_CR_FLAG` | DOUBLE |  |  | Indicates whether the transaction is debit or credit |
| 17 | `END_EFFECTIVE_DT_TM` | DATETIME |  |  | The date/time after which the row is no longer valid as active current data. This may be valued with the date that the row became inactive. |
| 18 | `GL_ACCOUNT_ALIAS_ID` | DOUBLE | NOT NULL | FK→ | It gives the alias id corresponding to gl_account_alias_nbr |
| 19 | `GL_ACCOUNT_ALIAS_NBR` | VARCHAR(100) |  |  | Number defining the account structure in the general account number. |
| 20 | `GL_ACCT_UNIT_ALIAS_ID` | DOUBLE | NOT NULL | FK→ | It gives the alias id corresponding to gl_acct_unit_alias_nbr |
| 21 | `GL_ACCT_UNIT_ALIAS_NBR` | VARCHAR(100) |  |  | Number defining the account unit in the general ledger account number. |
| 22 | `GL_COMPANY_ALIAS_ID` | DOUBLE | NOT NULL | FK→ | It gives the alias id corresponding to gl_company_alias_nbr |
| 23 | `GL_COMPANY_ALIAS_NBR` | VARCHAR(100) |  |  | Number defining the company in the general ledger account number. |
| 24 | `GL_COMPANY_UNIT_ALIAS_ID` | DOUBLE | NOT NULL | FK→ | It gives the alias id corresponding to gl_company_unit_alias_nbr |
| 25 | `GL_COMPANY_UNIT_ALIAS_NBR` | VARCHAR(100) |  |  | Number defining the sub account in the general ledger account number. |
| 26 | `GL_IMPACT_DT_TM` | DATETIME |  |  | Holds the date and time which is expected to impact the general ledge system. This date can vary from activity_dt_tm based on system settings |
| 27 | `GL_INTERFACE_DT_TM` | DATETIME |  |  | The date and time the GL interface occurred. |
| 28 | `GL_STATUS_CD` | DOUBLE | NOT NULL |  | Code value to tell what state this transactions is in, in relationship to the general ledger interface. The states include Pending, Error, or Submitted |
| 29 | `GL_TRANS_LOG_ID` | DOUBLE | NOT NULL | PK | Primary key |
| 30 | `LOGICAL_DOMAIN_ID` | DOUBLE | NOT NULL | FK→ | The unique identifier for a logical domain. This identifier allows the data to be grouped by logical domain. For example, If you assign clients a logical_domain_id this would allow you to store data for multiple clients on this table. |
| 31 | `PARENT_GL_TRANS_LOG_ID` | DOUBLE | NOT NULL |  | Foreign key to a record on the gl_trans_log table |
| 32 | `PFT_FISCAL_PERIOD_ID` | DOUBLE | NOT NULL |  | *** OBSOLETE *** |
| 33 | `POSTED_DT_TM` | DATETIME |  |  | The date the transaction was posted into they system as defined by the user. |
| 34 | `RECLASSIFIED_IND` | DOUBLE | NOT NULL |  | The purpose of this field is to store the value whether or not the GL_TRANS_LOG record has been reclassified by the reclassifying AR functionality. |
| 35 | `SI_BATCH_ID` | DOUBLE | NOT NULL | FK→ | Identifies which outbound batch the transaction was included on. This column is constrained on the SI_BATCH table. |
| 36 | `SUB_ACCT_ALIAS_NBR` | VARCHAR(50) |  |  | Number defining the sub account in the general ledger account number |
| 37 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 38 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 39 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 40 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 41 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `ACTIVITY_ID` | [TRANS_LOG](TRANS_LOG.md) | `ACTIVITY_ID` |
| `BILLING_ENTITY_ID` | [BILLING_ENTITY](BILLING_ENTITY.md) | `BILLING_ENTITY_ID` |
| `CREATED_PRSNL_ID` | [PRSNL](PRSNL.md) | `PERSON_ID` |
| `GL_ACCOUNT_ALIAS_ID` | [GL_ALIAS](GL_ALIAS.md) | `GL_ALIAS_ID` |
| `GL_ACCT_UNIT_ALIAS_ID` | [GL_ALIAS](GL_ALIAS.md) | `GL_ALIAS_ID` |
| `GL_COMPANY_ALIAS_ID` | [GL_ALIAS](GL_ALIAS.md) | `GL_ALIAS_ID` |
| `GL_COMPANY_UNIT_ALIAS_ID` | [GL_ALIAS](GL_ALIAS.md) | `GL_ALIAS_ID` |
| `LOGICAL_DOMAIN_ID` | [LOGICAL_DOMAIN](LOGICAL_DOMAIN.md) | `LOGICAL_DOMAIN_ID` |
| `SI_BATCH_ID` | [SI_BATCH](SI_BATCH.md) | `BATCH_ID` |

## Referenced by (2)

| From table | Column |
|------------|--------|
| [GL_TRANS_QUALIFIER](GL_TRANS_QUALIFIER.md) | `GL_TRANS_LOG_ID` |
| [PFT_TRANS_RELTN](PFT_TRANS_RELTN.md) | `GL_TRANS_LOG_ID` |

