# MM_GL_LOG_DETAIL_HMW

> Gl Log Detail Table

**Description:** GL Log detail table  
**Table type:** ACTIVITY  
**Primary key:** _(not published — see note)_  
**Columns:** 30

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `CREATE_DT_TM` | DATETIME |  |  | The date and time the row was last inserted or updated. |
| 2 | `CREDIT_ACCOUNT` | VARCHAR(40) |  |  | Credit Account |
| 3 | `CREDIT_ACCOUNT_CLASS` | VARCHAR(10) |  |  | Credit Account Class |
| 4 | `CREDIT_AMOUNT` | DOUBLE |  |  | Credit Amount |
| 5 | `CREDIT_COMPANY` | VARCHAR(20) |  |  | Credit Company |
| 6 | `CREDIT_COST_CENTER` | VARCHAR(20) |  |  | Credit Cost Center |
| 7 | `CREDIT_COST_CENTER_CD` | DOUBLE | NOT NULL |  | Credit Cost Center Code |
| 8 | `CREDIT_INDICATOR` | VARCHAR(1) |  |  | Credit Indicator |
| 9 | `CREDIT_ORG_ID` | DOUBLE | NOT NULL |  | Credit Organization ID |
| 10 | `CREDIT_SUBACCOUNT` | VARCHAR(20) |  |  | Credit SubAccount Code |
| 11 | `CREDIT_SUBACCOUNT_CD` | DOUBLE | NOT NULL |  | Credit SubAccount Code |
| 12 | `DEBIT_ACCOUNT` | VARCHAR(40) |  |  | Debit Account |
| 13 | `DEBIT_ACCOUNT_CLASS` | VARCHAR(10) |  |  | Debit Account Class |
| 14 | `DEBIT_AMOUNT` | DOUBLE |  |  | Debit Amount |
| 15 | `DEBIT_COMPANY` | VARCHAR(20) |  |  | Debit Company |
| 16 | `DEBIT_COST_CENTER` | VARCHAR(20) |  |  | Debit Cost Center |
| 17 | `DEBIT_COST_CENTER_CD` | DOUBLE | NOT NULL |  | Debit Cost Center Code |
| 18 | `DEBIT_INDICATOR` | VARCHAR(1) |  |  | Debit Indicator |
| 19 | `DEBIT_ORG_ID` | DOUBLE | NOT NULL |  | Debit Organization ID |
| 20 | `DEBIT_SUBACCOUNT` | VARCHAR(20) |  |  | Debit Sub Account |
| 21 | `DEBIT_SUBACCOUNT_CD` | DOUBLE | NOT NULL |  | Debit Sub Account Code |
| 22 | `LOG_DETAIL_ID` | DOUBLE | NOT NULL |  | Primary Key |
| 23 | `LOG_ID` | DOUBLE | NOT NULL |  | Foreight Key to mm_gl_log_hmw table |
| 24 | `RAW_GL_LINE` | VARCHAR(200) |  |  | A duplicate of the line that was written to the flat file. |
| 25 | `REVERSAL_IND` | DOUBLE |  |  | Indicator used to determine if the entry is a month end posting or a reversal for the previous month. |
| 26 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 27 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 28 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 29 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 30 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

