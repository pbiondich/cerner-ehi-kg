# PFT_ACCT_FIN_ENCNTR

> Profit account financial encounter table used for OMF reporting

**Description:** PFT ACCT FIN ENCNTR  
**Table type:** ACTIVITY  
**Primary key:** _(not published — see note)_  
**Columns:** 76

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ACCT_ADJ_BALANCE` | DOUBLE | NOT NULL |  | The balance of adjustments made on the account |
| 2 | `ACCT_BALANCE` | DOUBLE | NOT NULL |  | The balance for the account |
| 3 | `ACCT_CHRG_BALANCE` | DOUBLE | NOT NULL |  | The balance of charges for the account |
| 4 | `ACCT_COMBINED_IND` | DOUBLE |  |  | Indicates whether the account was combined or not |
| 5 | `ACCT_COMBINED_INTO_ID` | DOUBLE | NOT NULL |  | If the account was combined, the id of the account it was combined into |
| 6 | `ACCT_ID` | DOUBLE | NOT NULL |  | The id of the account for this financial encounter |
| 7 | `ACCT_LAST_CHRG_DATE` | DATETIME |  |  | Date of last charge for the account |
| 8 | `ACCT_LAST_PAY_DATE` | DATETIME |  |  | Date of last payment on the account |
| 9 | `ACCT_PAY_BALANCE` | DOUBLE | NOT NULL |  | Balance of payments made on the account |
| 10 | `ACCT_STATUS_CD` | DOUBLE | NOT NULL |  | Contains the current status of the account (in collections, review, active) |
| 11 | `ACCT_STATUS_REASON_CD` | DOUBLE | NOT NULL |  | Stores the reason for the account being in its current status |
| 12 | `ACCT_SUB_TYPE_CD` | DOUBLE | NOT NULL |  | Further defines the account type |
| 13 | `ACCT_TEMPL_ID` | DOUBLE | NOT NULL |  | Account template used to generate the account |
| 14 | `ACCT_TYPE_CD` | DOUBLE | NOT NULL |  | Account type (example: Patient, Cash, Revenue...) |
| 15 | `ACTIVE_IND` | DOUBLE |  |  | The table row is active or inactive. A row is generally active unless it is in an inactive state such as logically deleted, combined away, pending purge, etc. |
| 16 | `ACTIVE_STATUS_CD` | DOUBLE | NOT NULL |  | Indicates the status of the row itself (not the data in the row) such as active, inactive, combined away, pending purge, etc. |
| 17 | `ACTIVE_STATUS_DT_TM` | DATETIME |  |  | The date and time that the active_status_cd was set. |
| 18 | `ACTIVE_STATUS_PRSNL_ID` | DOUBLE | NOT NULL |  | The person who caused the active_status_cd to be set or change. |
| 19 | `BANKRUPTCY_EFF_DT_TM` | DATETIME |  |  | If filed for bankruptcy, the beginning effective date of bankruptcy |
| 20 | `BEG_EFFECTIVE_DT_TM` | DATETIME |  |  | The date and time for which this table row becomes effective. Normally, this will be the date and time the row is added, but could be a past or future date and time. |
| 21 | `BILLING_ENTITY_ID` | DOUBLE | NOT NULL |  | ID of the Billing Entity |
| 22 | `BILLING_ENTITY_NAME` | VARCHAR(100) |  |  | Name of the Billing Entity |
| 23 | `CLIENT_ORG_ID` | DOUBLE | NOT NULL |  | If a client account, the organization ID |
| 24 | `CLIENT_ORG_NAME` | VARCHAR(100) |  |  | If client account, the organization name |
| 25 | `CONSOL_METH_CD` | DOUBLE | NOT NULL |  | Method of consolidation (ex: guarantor by account, guarantor by encounter |
| 26 | `ENCNTR_ID` | DOUBLE | NOT NULL | FK→ | This is the value of the unique primary identifier of the encounter table. It is an internal system assigned number. |
| 27 | `END_EFFECTIVE_DT_TM` | DATETIME |  |  | The date/time after which the row is no longer valid as active current data. This may be valued with the date that the row became inactive. |
| 28 | `EXT_ACCT_ID_TXT` | VARCHAR(40) |  |  | Account Alias |
| 29 | `INTERIM_IND` | DOUBLE |  |  | From pft_encntr. Indicates whether or not an encounter qualifies for interim billing. |
| 30 | `PATIENT_ID` | DOUBLE | NOT NULL |  | ID of patient associated with this account and encounter |
| 31 | `PATIENT_NAME_FIRST` | VARCHAR(100) |  |  | First name of the patient associated with this account and encounter |
| 32 | `PATIENT_NAME_FIRST_KEY` | VARCHAR(100) |  |  | First name key of the patient associated with this account and encounter |
| 33 | `PATIENT_NAME_FULL` | VARCHAR(100) |  |  | Full name of the patient associated with this account and encounter |
| 34 | `PATIENT_NAME_FULL_KEY` | VARCHAR(100) |  |  | Full name key of the patient associated with this account and encounter |
| 35 | `PATIENT_NAME_LAST` | VARCHAR(100) |  |  | Last name of the patient associated with this account and encounter |
| 36 | `PATIENT_NAME_LAST_KEY` | VARCHAR(100) |  |  | Last name key of the patient associated with this account and encounter |
| 37 | `PAYMENT_PLAN_IND` | DOUBLE |  |  | Indicates if this is on a payment plan |
| 38 | `PE_ACTIVITY_120_BALANCE` | DOUBLE | NOT NULL |  | 120 day aging balance for financial encounter based on activity date |
| 39 | `PE_ACTIVITY_180_PLUS_BALANCE` | DOUBLE | NOT NULL |  | 180 day aging balance for financial encounter based on activity date |
| 40 | `PE_ACTIVITY_30_BALANCE` | DOUBLE | NOT NULL |  | 30 day aging balance for financial encounter based on activity date |
| 41 | `PE_ACTIVITY_60_BALANCE` | DOUBLE | NOT NULL |  | 60 day aging balance for financial encounter based on activity date |
| 42 | `PE_ACTIVITY_90_BALANCE` | DOUBLE | NOT NULL |  | 90 day aging balance for financial encounter based on activity date |
| 43 | `PE_ADJ_BALANCE` | DOUBLE | NOT NULL |  | Balance of adjustments on the financial encounter |
| 44 | `PE_BAD_DEBT_BALANCE` | DOUBLE | NOT NULL |  | Balance of the bad debt on the financial encounter |
| 45 | `PE_BAD_DEBT_DT_TM` | DATETIME |  |  | If this went to bad debt, the date and time it went |
| 46 | `PE_BALANCE` | DOUBLE | NOT NULL |  | The balance for the financial encounter |
| 47 | `PE_CHARGE_BALANCE` | DOUBLE | NOT NULL |  | The balance of the charges on the financial encounter |
| 48 | `PE_COMBINED_IND` | DOUBLE |  |  | Indicates whether the financial encounter was combined or not |
| 49 | `PE_COMBINED_INTO_ID` | DOUBLE | NOT NULL |  | If the financial encounter was combined, the id of the financial encounter it was combined into. |
| 50 | `PE_DISCH_120_BALANCE` | DOUBLE | NOT NULL |  | 120 day aging balance based on the discharge date |
| 51 | `PE_DISCH_180_PLUS_BALANCE` | DOUBLE | NOT NULL |  | 180 day aging balance based on the discharge date |
| 52 | `PE_DISCH_30_BALANCE` | DOUBLE | NOT NULL |  | 30 day aging balance based on the discharge date |
| 53 | `PE_DISCH_60_BALANCE` | DOUBLE | NOT NULL |  | 60 day aging balance based on the discharge date |
| 54 | `PE_DISCH_90_BALANCE` | DOUBLE | NOT NULL |  | 90 day aging balance based on the discharge date |
| 55 | `PE_DNFB_120_BALANCE` | DOUBLE | NOT NULL |  | 120 day aging balance based on the discharged not final billed date |
| 56 | `PE_DNFB_180_PLUS_BALANCE` | DOUBLE | NOT NULL |  | 180 day aging balance based on the discharged not final billed date |
| 57 | `PE_DNFB_30_BALANCE` | DOUBLE | NOT NULL |  | 30 day aging balance based on the discharged not final billed date |
| 58 | `PE_DNFB_60_BALANCE` | DOUBLE | NOT NULL |  | 60 day aging balance based on the discharged not final billed date |
| 59 | `PE_DNFB_90_BALANCE` | DOUBLE | NOT NULL |  | 90 day aging balance based on the discharged not final billed date |
| 60 | `PE_DUNNING_LEVEL_CD` | DOUBLE | NOT NULL |  | Specifies the status of an account |
| 61 | `PE_FIN_CHARGE_BALANCE` | DOUBLE | NOT NULL |  | The balance of the financel changes for the financial encounter |
| 62 | `PE_FIN_CLASS_CD` | DOUBLE | NOT NULL |  | Financial class |
| 63 | `PE_LAST_CHRG_DATE` | DATETIME |  |  | The date of the last charge for the financial encounter |
| 64 | `PE_LAST_PAY_DATE` | DATETIME |  |  | The date of the last payment for the financial encounter |
| 65 | `PE_PAY_BALANCE` | DOUBLE | NOT NULL |  | The balance of payments made on the financial encounter |
| 66 | `PE_PAY_PLAN_STATUS_CD` | DOUBLE | NOT NULL |  | Status of the payment plan (ex. paid, behind, delinquent) |
| 67 | `PE_STATUS_CD` | DOUBLE | NOT NULL |  | Status of the encounter. Active / Pending |
| 68 | `PFT_ACCT_FIN_ENCNTR_ID` | DOUBLE | NOT NULL |  | Unique identifier of this table |
| 69 | `PFT_ENCNTR_ALIAS` | VARCHAR(40) |  |  | From the pft_encntr. Stores the financial encounter's alias which will be used to identify the financial encounter |
| 70 | `PFT_ENCNTR_ID` | DOUBLE | NOT NULL |  | The id of the encounter associated with this entry |
| 71 | `RELATED_ACCT_ID` | DOUBLE | NOT NULL |  | If joined to a delivery system, the id of the account |
| 72 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 73 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 74 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 75 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 76 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `ENCNTR_ID` | [ENCOUNTER](ENCOUNTER.md) | `ENCNTR_ID` |

