# PFT_BALANCE

> Financial information tracking money owed, by whom, state/status.

**Description:** ProFit Balance  
**Table type:** ACTIVITY  
**Primary key:** `PFT_BALANCE_ID`  
**Columns:** 44  
**Referenced by:** 6 columns

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ACCT_ID` | DOUBLE | NOT NULL | FK→ | Account of the associated balance |
| 2 | `ADJUSTMENT_AMT` | DOUBLE | NOT NULL |  | Adjustments for the effective day |
| 3 | `ADMIT_PRSNL_ID` | DOUBLE | NOT NULL | FK→ | Admitting personnel associated with the patient encounter |
| 4 | `BALANCE_STATE_CD` | DOUBLE | NOT NULL |  | Current state of the associated balance |
| 5 | `BALANCE_TYPE_CD` | DOUBLE | NOT NULL |  | Identifies the level for which the balance is maintained, e.g., Bill, Line Item. |
| 6 | `BEG_BALANCE_AMT` | DOUBLE | NOT NULL |  | Balance at beginning of day |
| 7 | `BEG_EFFECTIVE_DT_TM` | DATETIME | NOT NULL |  | The date and time for which this table row becomes effective. Normally, this will be the date and time the row is added, but could be a past or future date and time. |
| 8 | `BEG_SERVICE_DT_TM` | DATETIME |  |  | Datetime service began |
| 9 | `BILLING_ENTITY_ID` | DOUBLE | NOT NULL | FK→ | Billing Entity which claims processing is being defined. |
| 10 | `BILL_DT_TM` | DATETIME |  |  | First submission/transmission datetime for associated bill |
| 11 | `BILL_TYPE_CD` | DOUBLE | NOT NULL |  | Type of bill for associated balance |
| 12 | `BILL_VRSN_NBR` | DOUBLE | NOT NULL | FK→ | Version number of the associated bill record |
| 13 | `BO_HP_RELTN_ID` | DOUBLE | NOT NULL | FK→ | Identifies the associated BO_HP_RELTN to the BO_HP balance this day |
| 14 | `CHARGE_AMT` | DOUBLE | NOT NULL |  | Charges for the effective day |
| 15 | `CLIENT_ORG_ID` | DOUBLE | NOT NULL | FK→ | Organization of responsible client |
| 16 | `CORSP_ACTIVITY_ID` | DOUBLE | NOT NULL | FK→ | Identifies the associated bill record |
| 17 | `ENCNTR_TYPE_CLASS_CD` | DOUBLE | NOT NULL |  | Further categorization of patients into general groups (i.e., inpatient, outpatient, emergency, recurring outpatient). |
| 18 | `END_BALANCE_AMT` | DOUBLE | NOT NULL |  | Current balance |
| 19 | `END_EFFECTIVE_DT_TM` | DATETIME | NOT NULL |  | The date/time after which the row is no longer valid as active current data. This may be valued with the date that the row became inactive. |
| 20 | `END_SERVICE_DT_TM` | DATETIME |  |  | Datetime service ended |
| 21 | `GUARANTOR_PERSON_ID` | DOUBLE | NOT NULL | FK→ | Guarantor/person responsible for the balance |
| 22 | `INTERIM_BILL_DT_TM` | DATETIME |  |  | Transmission date and time of the interim bill. |
| 23 | `LAST_PAYMENT_DT_TM` | DATETIME |  |  | Datetime of last payment against this balance |
| 24 | `PATIENT_RESP_AMT` | DOUBLE | NOT NULL |  | Patient responsibility for the day |
| 25 | `PAYER_TYPE_CD` | DOUBLE | NOT NULL |  | Type of payer associated to the bill, e.g., Selfpay, Insurance, Client, Unidentified |
| 26 | `PAYMENT_AMT` | DOUBLE | NOT NULL |  | Payments for the effective day |
| 27 | `PERFORM_PRSNL_ID` | DOUBLE | NOT NULL | FK→ | Performing personnel associated to the patient encounter |
| 28 | `PERSON_ID` | DOUBLE | NOT NULL | FK→ | Patient associated to the encounter |
| 29 | `PFT_BALANCE_ID` | DOUBLE | NOT NULL | PK | Uniquely identifies the financial information, tracking money owed, by whom, and state/status |
| 30 | `PFT_CHARGE_ID` | DOUBLE | NOT NULL | FK→ | Physician office charge associated to the balance |
| 31 | `PFT_ENCNTR_ID` | DOUBLE | NOT NULL | FK→ | Financial encounter associated to the balance |
| 32 | `PREV_BALANCE_ID` | DOUBLE | NOT NULL | FK→ | Previous balance that associated to the financial information, tracking money owed, by whom, and state/status |
| 33 | `TOTAL_ADJUSTMENT_AMT` | DOUBLE | NOT NULL |  | Total adjustments for the balance |
| 34 | `TOTAL_CHARGE_AMT` | DOUBLE | NOT NULL |  | Total charges for the balance |
| 35 | `TOTAL_PATIENT_RESP_AMT` | DOUBLE | NOT NULL |  | Total patient responsibility for the balance |
| 36 | `TOTAL_PAYMENT_AMT` | DOUBLE | NOT NULL |  | Total payments for the balance |
| 37 | `TOTAL_TRANSFER_AMT` | DOUBLE | NOT NULL |  | Total transfers for the balance |
| 38 | `TRANSFER_AMT` | DOUBLE | NOT NULL |  | Transfers (eob remainders, non-covered) for the effective day |
| 39 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 40 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 41 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 42 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 43 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |
| 44 | `ZERO_BALANCE_DT_TM` | DATETIME |  |  | Datetime the balance reached 0.0 |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `ACCT_ID` | [ACCOUNT](ACCOUNT.md) | `ACCT_ID` |
| `ADMIT_PRSNL_ID` | [PRSNL](PRSNL.md) | `PERSON_ID` |
| `BILLING_ENTITY_ID` | [BILLING_ENTITY](BILLING_ENTITY.md) | `BILLING_ENTITY_ID` |
| `BILL_VRSN_NBR` | [BILL_REC](BILL_REC.md) | `BILL_VRSN_NBR` |
| `BO_HP_RELTN_ID` | [BO_HP_RELTN](BO_HP_RELTN.md) | `BO_HP_RELTN_ID` |
| `CLIENT_ORG_ID` | [ORGANIZATION](ORGANIZATION.md) | `ORGANIZATION_ID` |
| `CORSP_ACTIVITY_ID` | [BILL_REC](BILL_REC.md) | `CORSP_ACTIVITY_ID` |
| `GUARANTOR_PERSON_ID` | [PERSON](PERSON.md) | `PERSON_ID` |
| `PERFORM_PRSNL_ID` | [PRSNL](PRSNL.md) | `PERSON_ID` |
| `PERSON_ID` | [PERSON](PERSON.md) | `PERSON_ID` |
| `PFT_CHARGE_ID` | [PFT_CHARGE](PFT_CHARGE.md) | `PFT_CHARGE_ID` |
| `PFT_ENCNTR_ID` | [PFT_ENCNTR](PFT_ENCNTR.md) | `PFT_ENCNTR_ID` |
| `PREV_BALANCE_ID` | [PFT_BALANCE](PFT_BALANCE.md) | `PFT_BALANCE_ID` |

## Referenced by (6)

| From table | Column |
|------------|--------|
| [PE_STATUS_REASON](PE_STATUS_REASON.md) | `PFT_BALANCE_ID` |
| [PFT_BALANCE](PFT_BALANCE.md) | `PREV_BALANCE_ID` |
| [PFT_BILL_ACTIVITY](PFT_BILL_ACTIVITY.md) | `PFT_BALANCE_ID` |
| [PFT_QUEUE_ITEM](PFT_QUEUE_ITEM.md) | `PFT_BALANCE_ID` |
| [TRANS_LOG](TRANS_LOG.md) | `CREDIT_BALANCE_ID` |
| [TRANS_LOG](TRANS_LOG.md) | `DEBIT_BALANCE_ID` |

