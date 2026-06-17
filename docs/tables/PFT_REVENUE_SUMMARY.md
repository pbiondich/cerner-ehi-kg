# PFT_REVENUE_SUMMARY

> Monthly summarization view by period date. The summarized date will provide year to date trending analysis availability and enhanced performance revenue summary. reports for acute and physician care.

**Description:** ProFit Revenue Summary  
**Table type:** ACTIVITY  
**Primary key:** `PFT_REVENUE_SUMMARY_ID`  
**Columns:** 39  
**Referenced by:** 1 columns

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ACCOMMODATION_CD` | DOUBLE | NOT NULL |  | Current type of accommodations in which the patient (encounter) has been placed. (e.g. Private, Semi Private, etc.) |
| 2 | `ACTIVITY_TYPE_CD` | DOUBLE | NOT NULL |  | Identifies to which "net" (pathnet, Radnet) and/or what department (general lab, microbiology) an order belongs. |
| 3 | `ATTEND_PHYS_ID` | DOUBLE | NOT NULL | FK→ | PRSNL Identifier for the attending physician. |
| 4 | `BILLING_ENTITY_ID` | DOUBLE | NOT NULL | FK→ | Identifies the Billing entity |
| 5 | `BILL_ITEM_ID` | DOUBLE | NOT NULL | FK→ | Identifier for billable item |
| 6 | `CDM_NBR_TXT` | VARCHAR(40) |  |  | CDM Number from a Bill Item that was modified. |
| 7 | `CPT_NOMEN_ID` | DOUBLE | NOT NULL | FK→ | Identifies the associated CPT code nomenclature Id |
| 8 | `DRG_NOMEN_ID` | DOUBLE | NOT NULL | FK→ | Identifies the associated DRG nomenclature |
| 9 | `ENCNTR_TYPE_CD` | DOUBLE | NOT NULL |  | Categorizes the encounter into a logical group or type. examples may include inpatient, outpatient, etc. |
| 10 | `ENCNTR_TYPE_CLASS_CD` | DOUBLE | NOT NULL |  | Further categorization of patients into general groups (i.e., inpatient, outpatient, emergency, recurring outpatient). |
| 11 | `FIN_CLASS_CD` | DOUBLE | NOT NULL |  | Financial classification used for a given encounter. Examples may include worker's comp, self pay, etc. |
| 12 | `GL_ACCOUNT_ALIAS_NBR_TXT` | VARCHAR(100) |  |  | Defines the account structure in the general account number |
| 13 | `GL_ACCT_UNIT_ALIAS_NBR_TXT` | VARCHAR(100) |  |  | Defines an account unit in the general ledger account number |
| 14 | `GL_COMPANY_ALIAS_NBR_TXT` | VARCHAR(100) |  |  | Defines the company in the general ledger account number |
| 15 | `GL_COMPANY_UNIT_ALIAS_NBR_TXT` | VARCHAR(100) |  |  | Defines the sub account in the general ledger account number |
| 16 | `HCPCS_NOMEN_ID` | DOUBLE | NOT NULL | FK→ | Identifies the associated HCPCS nomenclature Id |
| 17 | `HEALTH_PLAN_ID` | DOUBLE | NOT NULL | FK→ | Identifies the associated Health Plan |
| 18 | `ICD9_NOMEN_ID` | DOUBLE | NOT NULL | FK→ | Identifies the associated ICD9 code nomenclature Id |
| 19 | `LOC_BUILDING_CD` | DOUBLE | NOT NULL |  | Identifies the associated building of the patient |
| 20 | `LOC_FACILITY_CD` | DOUBLE | NOT NULL |  | Identifies the associated facility of the patient |
| 21 | `LOC_NURSING_CD` | DOUBLE | NOT NULL |  | Identifies the associated Nursing Unit of the patient |
| 22 | `MED_SERVICE_CD` | DOUBLE | NOT NULL |  | Category of medical service that the patient is receiving in relation to their encounter. The category may be of treatment type, surgery, general resources, or others. |
| 23 | `PAYOR_ORG_ID` | DOUBLE | NOT NULL | FK→ | Identifies the associated payer's organization |
| 24 | `PERF_LOC_CD` | DOUBLE | NOT NULL |  | Identifies the associated location at which services were provided. |
| 25 | `PFT_FISCAL_PERIOD_ID` | DOUBLE | NOT NULL | FK→ | Identifies the associated fiscal period to which billing applied. |
| 26 | `PFT_REVENUE_SUMMARY_ID` | DOUBLE | NOT NULL | PK | Uniquely identifies each Monthly Revenue Summarization of acute and physician care. |
| 27 | `REVENUE_CD` | DOUBLE | NOT NULL |  | Identifies the associated Revenue code |
| 28 | `REV_CLASS_CD` | DOUBLE | NOT NULL |  | Identifies the associated classification of the revenue. |
| 29 | `TOT_CHRG_AMT` | DOUBLE |  |  | Total charge amount for a given Revenue code for a given fiscal period |
| 30 | `TOT_CHRG_QTY` | DOUBLE |  |  | Total charge quantity for a given Revenue code for a given fiscal period |
| 31 | `TOT_CREDIT_AMT` | DOUBLE |  |  | Total credit amount for a given Revenue code for a given fiscal period |
| 32 | `TOT_CREDIT_QTY` | DOUBLE |  |  | Total charge quantity for a given Revenue code for a given fiscal period |
| 33 | `TOT_DEBIT_AMT` | DOUBLE |  |  | Total debit amount for a given Revenue code for a given fiscal period |
| 34 | `TOT_DEBIT_QTY` | DOUBLE |  |  | Total charge quantity for a given Revenue code for a given fiscal period |
| 35 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 36 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 37 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 38 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 39 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `ATTEND_PHYS_ID` | [PRSNL](PRSNL.md) | `PERSON_ID` |
| `BILLING_ENTITY_ID` | [BILLING_ENTITY](BILLING_ENTITY.md) | `BILLING_ENTITY_ID` |
| `BILL_ITEM_ID` | [BILL_ITEM](BILL_ITEM.md) | `BILL_ITEM_ID` |
| `CPT_NOMEN_ID` | [NOMENCLATURE](NOMENCLATURE.md) | `NOMENCLATURE_ID` |
| `DRG_NOMEN_ID` | [NOMENCLATURE](NOMENCLATURE.md) | `NOMENCLATURE_ID` |
| `HCPCS_NOMEN_ID` | [NOMENCLATURE](NOMENCLATURE.md) | `NOMENCLATURE_ID` |
| `HEALTH_PLAN_ID` | [HEALTH_PLAN](HEALTH_PLAN.md) | `HEALTH_PLAN_ID` |
| `ICD9_NOMEN_ID` | [NOMENCLATURE](NOMENCLATURE.md) | `NOMENCLATURE_ID` |
| `PAYOR_ORG_ID` | [ORGANIZATION](ORGANIZATION.md) | `ORGANIZATION_ID` |
| `PFT_FISCAL_PERIOD_ID` | [PFT_FISCAL_PERIOD](PFT_FISCAL_PERIOD.md) | `PFT_FISCAL_PERIOD_ID` |

## Referenced by (1)

| From table | Column |
|------------|--------|
| [PFT_TRANS_RELTN](PFT_TRANS_RELTN.md) | `REVENUE_SUMMARY_ID` |

