# TPM_RESULT

> TPM RESULT table

**Description:** TPM RESULT  
**Table type:** REFERENCE  
**Primary key:** `TPM_RESULT_ID`  
**Columns:** 20  
**Referenced by:** 6 columns

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ACTIVE_IND` | DOUBLE |  |  | The table row is active or inactive. A row is generally active unless it is in an inactive state such as logically deleted, combined away, pending purge, etc. |
| 2 | `ACTIVE_STATUS_CD` | DOUBLE | NOT NULL |  | Indicates the status of the row itself (not the data in the row) such as active, inactive, combined away, pending purge, etc. |
| 3 | `ACTIVE_STATUS_DT_TM` | DATETIME |  |  | The date and time that the active_status_cd was set. |
| 4 | `ACTIVE_STATUS_PRSNL_ID` | DOUBLE | NOT NULL |  | The person who caused the active_status_cd to be set or change. |
| 5 | `BEG_EFFECTIVE_DT_TM` | DATETIME |  |  | The date and time for which this table row becomes effective. Normally, this will be the date and time the row is added, but could be a past or future date and time. |
| 6 | `CR_ACCT_ID` | DOUBLE | NOT NULL |  | CREDIT ACCOUNT ID |
| 7 | `CR_ACCT_TEMPL_ID` | DOUBLE | NOT NULL |  | CREDIT ACCOUNT TEMPLATE ID |
| 8 | `CR_BE_ID` | DOUBLE | NOT NULL |  | Unique identifier of the billing entity related to the credit account. Candidate key reference to the billing_entity table. |
| 9 | `CR_GL_ACCT_ID` | DOUBLE | NOT NULL |  | CREDIT GENERAL LEDGER ACCOUNT ID |
| 10 | `DR_ACCT_ID` | DOUBLE | NOT NULL |  | DEBIT ACCOUNT ID |
| 11 | `DR_ACCT_TEMPL_ID` | DOUBLE | NOT NULL |  | DEBIT ACCOUNT TEMPLATE ID |
| 12 | `DR_BE_ID` | DOUBLE | NOT NULL |  | Unique identifier of the billing entity related to the debit account. Foreign key reference to the billing_entity table. |
| 13 | `DR_GL_ACCT_ID` | DOUBLE | NOT NULL |  | DEBIT GENERAL LEDGER ACCOUNT ID |
| 14 | `END_EFFECTIVE_DT_TM` | DATETIME |  |  | The date/time after which the row is no longer valid as active current data. This may be valued with the date that the row became inactive. |
| 15 | `TPM_RESULT_ID` | DOUBLE | NOT NULL | PK | Primary Key |
| 16 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 17 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 18 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 19 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 20 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Referenced by (6)

| From table | Column |
|------------|--------|
| [TPM_CHRG_TIER](TPM_CHRG_TIER.md) | `TPM_RESULT_ID` |
| [TPM_CONDITION](TPM_CONDITION.md) | `TPM_RESULT_ID` |
| [TPM_RESULT_HIST](TPM_RESULT_HIST.md) | `TPM_RESULT_ID` |
| [TPM_RULE_TIER](TPM_RULE_TIER.md) | `TPM_RESULT_ID` |
| [TPM_SUBTYPE_TIER](TPM_SUBTYPE_TIER.md) | `TPM_RESULT_ID` |
| [TPM_TRANS_RSN_TIER](TPM_TRANS_RSN_TIER.md) | `TPM_RESULT_ID` |

