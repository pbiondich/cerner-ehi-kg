# ACCT_TEMPLATE

> This table stores the default behaviors for all accounts that are created based on this template. An account template is only owned by one billing entity and cannot be used to create accounts for other billing entities.

**Description:** Account Template  
**Table type:** REFERENCE  
**Primary key:** `ACCT_TEMPL_ID`  
**Columns:** 22  
**Referenced by:** 6 columns

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ACCT_SUB_TYPE_CD` | DOUBLE | NOT NULL |  | Is a sub type of the Acct_Type_Cd to further define the account. |
| 2 | `ACCT_TEMPL_DESC` | VARCHAR(250) |  |  | Description of the purpose of the template |
| 3 | `ACCT_TEMPL_ID` | DOUBLE | NOT NULL | PK | Primary key and unique identifier. |
| 4 | `ACCT_TEMPL_NAME` | VARCHAR(50) |  |  | Stores the name given to the template |
| 5 | `ACCT_TEMPL_NAME_KEY` | VARCHAR(250) |  |  | Key Field for the Account Template Name in order to be sorted. |
| 6 | `ACCT_TYPE_CD` | DOUBLE | NOT NULL |  | Stores the type of accounts for this template (Cash, Revenue, General Patient) |
| 7 | `ACTIVE_IND` | DOUBLE |  |  | The table row is active or inactive. A row is generally active unless it is in an inactive state such as logically deleted, combined away, pending purge, etc. |
| 8 | `ACTIVE_STATUS_CD` | DOUBLE | NOT NULL |  | Indicates the status of the row itself (not the data in the row) such as active, inactive, combined away, pending purge, etc. |
| 9 | `ACTIVE_STATUS_DT_TM` | DATETIME |  |  | The date and time that the active_status_cd was set. |
| 10 | `ACTIVE_STATUS_PRSNL_ID` | DOUBLE | NOT NULL |  | The person who caused the active_status_cd to be set or change. |
| 11 | `BEG_EFFECTIVE_DT_TM` | DATETIME |  |  | The date and time for which this table row becomes effective. Normally, this will be the date and time the row is added, but could be a past or future date and time. |
| 12 | `CONSOLIDATION_CD` | DOUBLE | NOT NULL |  | Determines whether an account based on this template will be consolidated. |
| 13 | `DEF_POST_METHOD_CD` | DOUBLE | NOT NULL |  | Sets the default posting method for all accounts based on this template (FIFO, LIFO, Distributed) - No longer used |
| 14 | `END_EFFECTIVE_DT_TM` | DATETIME |  |  | The date/time after which the row is no longer valid as active current data. This may be valued with the date that the row became inactive. |
| 15 | `INACTIVITY_DAYS` | DOUBLE |  |  | Facilitates the automated process of closing accounts after a certain period of inactivity. |
| 16 | `OPEN_IND` | DOUBLE |  |  | Used to determine whether new accounts can be created off of this template. |
| 17 | `PRSNL_SEC_IND` | DOUBLE |  |  | Indicates whether this template has security permissions that override those at the Billing Entity level. - No longer used |
| 18 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 19 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 20 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 21 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 22 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Referenced by (6)

| From table | Column |
|------------|--------|
| [ACCOUNT](ACCOUNT.md) | `ACCT_TEMPL_ID` |
| [ACCT_TEMPL_HIST](ACCT_TEMPL_HIST.md) | `ACCOUNT_TEMPLATE_ID` |
| [AT_ACCT_RELTN](AT_ACCT_RELTN.md) | `ACCT_TEMPL_ID` |
| [BE_AT_RELTN](BE_AT_RELTN.md) | `ACCT_TEMPL_ID` |
| [PFT_CHARGE](PFT_CHARGE.md) | `CR_ACCT_TEMPL_ID` |
| [PFT_CHARGE](PFT_CHARGE.md) | `DR_ACCT_TEMPL_ID` |

