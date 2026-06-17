# RC_F_CLAIM_EVENT

> This table contains data related to claims.

**Description:** Revenue Cycle Fact Claim Event  
**Table type:** ACTIVITY  
**Primary key:** _(not published — see note)_  
**Columns:** 27

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `BILL_NUMBER_IDENT` | VARCHAR(40) | NOT NULL |  | Contains the display value associated to a bill number. |
| 2 | `BILL_VRSN_NBR` | DOUBLE | NOT NULL |  | The version of the bill that has been generated. |
| 3 | `CLAIM_BILLED_AMT` | DOUBLE | NOT NULL |  | Contains the dollar amount billed on the claim. |
| 4 | `CLAIM_EVENT_DT_NBR` | DOUBLE | NOT NULL | FK→ | A number representing the date of the claim event. References the key in the OMF_DATE table. |
| 5 | `DAYS_SINCE_DISCHARGE_CNT` | DOUBLE | NOT NULL |  | Contains the number of days since the encounter's discharge. |
| 6 | `DAYS_SINCE_GENERATION_CNT` | DOUBLE | NOT NULL |  | Contains the number of days since the generation of the claim. |
| 7 | `DAYS_SINCE_SUBMISSION_CNT` | DOUBLE | NOT NULL |  | Contains the number of days since the submission of the claim. |
| 8 | `FIRST_PROCESS_DT_TM` | DATETIME | NOT NULL |  | The date/time that the first ETL process started that created this record. |
| 9 | `LAST_PROCESS_DT_TM` | DATETIME | NOT NULL |  | The date/time that the last ETL process started that updated this record. |
| 10 | `MILL_CORSP_ID` | DOUBLE | NOT NULL |  | Identifies the row in the Bill_Rec table in the Millennium database from which the data for this table was derived. |
| 11 | `MILL_LOGICAL_DOMAIN_ID` | DOUBLE | NOT NULL |  | Uniquely identifies the logical domain to which the row data belongs. |
| 12 | `PRIORITY_SEQ_NBR` | DOUBLE | NOT NULL |  | Sequence that defines the hierarchy for insurance responsibility. |
| 13 | `RC_AF_PATIENT_AR_BALANCE_ID` | DOUBLE | NOT NULL | FK→ | Uniquely identifies data related to the RC_F_Claim_Event table. |
| 14 | `RC_D_BILLING_ENTITY_ID` | DOUBLE | NOT NULL | FK→ | Uniquely identifies the billing entity dimension row related to this fact row. |
| 15 | `RC_D_BILL_TYPE_ID` | DOUBLE | NOT NULL | FK→ | Uniquely identifies the bill type related to this fact row. |
| 16 | `RC_D_CLAIM_EVENT_TYPE_ID` | DOUBLE | NOT NULL | FK→ | Uniquely identifies a claim event type dimension row related to this fact row. |
| 17 | `RC_D_FINANCIAL_CLASS_ID` | DOUBLE | NOT NULL | FK→ | Uniquely identifies the financial class related to this fact row. |
| 18 | `RC_D_HEALTH_PLAN_ID` | DOUBLE | NOT NULL | FK→ | Uniquely identifies the health plan related to this fact row. |
| 19 | `RC_F_CLAIM_EVENT_ID` | DOUBLE | NOT NULL |  | Uniquely identifies data related to claims. |
| 20 | `SHR_D_ADMIT_PRSNL_ID` | DOUBLE | NOT NULL | FK→ | Uniquely identifies the admit person for this claim event. |
| 21 | `SHR_D_LOCATION_ID` | DOUBLE | NOT NULL | FK→ | Uniquely identifies the patient encounter location at the time the claim event. |
| 22 | `SHR_D_PERSON_ID` | DOUBLE | NOT NULL | FK→ | Uniquely identifies the person related to this claim event. |
| 23 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 24 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 25 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 26 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 27 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `CLAIM_EVENT_DT_NBR` | [OMF_DATE](OMF_DATE.md) | `DT_NBR` |
| `RC_AF_PATIENT_AR_BALANCE_ID` | [RC_AF_PATIENT_AR_BALANCE](RC_AF_PATIENT_AR_BALANCE.md) | `RC_AF_PATIENT_AR_BALANCE_ID` |
| `RC_D_BILLING_ENTITY_ID` | [RC_D_BILLING_ENTITY](RC_D_BILLING_ENTITY.md) | `RC_D_BILLING_ENTITY_ID` |
| `RC_D_BILL_TYPE_ID` | [RC_D_BILL_TYPE](RC_D_BILL_TYPE.md) | `RC_D_BILL_TYPE_ID` |
| `RC_D_CLAIM_EVENT_TYPE_ID` | [RC_D_CLAIM_EVENT_TYPE](RC_D_CLAIM_EVENT_TYPE.md) | `RC_D_CLAIM_EVENT_TYPE_ID` |
| `RC_D_FINANCIAL_CLASS_ID` | [RC_D_FINANCIAL_CLASS](RC_D_FINANCIAL_CLASS.md) | `RC_D_FINANCIAL_CLASS_ID` |
| `RC_D_HEALTH_PLAN_ID` | [RC_D_HEALTH_PLAN](RC_D_HEALTH_PLAN.md) | `RC_D_HEALTH_PLAN_ID` |
| `SHR_D_ADMIT_PRSNL_ID` | [SHR_D_PERSON](SHR_D_PERSON.md) | `SHR_D_PERSON_ID` |
| `SHR_D_LOCATION_ID` | [SHR_D_LOCATION](SHR_D_LOCATION.md) | `SHR_D_LOCATION_ID` |
| `SHR_D_PERSON_ID` | [SHR_D_PERSON](SHR_D_PERSON.md) | `SHR_D_PERSON_ID` |

