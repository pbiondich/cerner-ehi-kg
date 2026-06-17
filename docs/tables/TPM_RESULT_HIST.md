# TPM_RESULT_HIST

> TPM RESULT HISTORY table

**Description:** TPM RESULT HISTORY  
**Table type:** REFERENCE  
**Primary key:** _(not published — see note)_  
**Columns:** 22

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
| 8 | `CR_BE_ID` | DOUBLE | NOT NULL |  | Credit Billing Entity ID |
| 9 | `CR_GL_ACCT_ID` | DOUBLE | NOT NULL |  | CREDIT GENERAL LEDGER ACCOUNT ID |
| 10 | `DR_ACCT_ID` | DOUBLE | NOT NULL |  | DEBIT ACCOUNT ID |
| 11 | `DR_ACCT_TEMPL_ID` | DOUBLE | NOT NULL |  | DEBIT ACCOUNT TEMPLATE ID |
| 12 | `DR_BE_ID` | DOUBLE | NOT NULL |  | Debit Billing Entity ID |
| 13 | `DR_GL_ACCT_ID` | DOUBLE | NOT NULL |  | DEBIT GENERAL ACCOUNT ID |
| 14 | `END_EFFECTIVE_DT_TM` | DATETIME |  |  | The date/time after which the row is no longer valid as active current data. This may be valued with the date that the row became inactive. |
| 15 | `TPM_RESULT_HIST_ID` | DOUBLE | NOT NULL |  | TPM RESULT HISTORY ID |
| 16 | `TPM_RESULT_ID` | DOUBLE | NOT NULL | FK→ | TPM RESULT ID |
| 17 | `TPM_RESULT_VRSN_NBR` | DOUBLE | NOT NULL |  | Stores the version number |
| 18 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 19 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 20 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 21 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 22 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `TPM_RESULT_ID` | [TPM_RESULT](TPM_RESULT.md) | `TPM_RESULT_ID` |

