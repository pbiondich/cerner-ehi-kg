# RC_F_DAILY_CLAIM_EVENT_SMRY

> Contains aggregated claim data by the given dimensions for a given activity date.

**Description:** Revenue Cycle Daily Claim Event Summary  
**Table type:** ACTIVITY  
**Primary key:** _(not published — see note)_  
**Columns:** 22

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ACTIVITY_DT_NBR` | DOUBLE | NOT NULL | FK→ | Represents the date that the claim event data is being aggregated. |
| 2 | `FIRST_PROCESS_DT_TM` | DATETIME | NOT NULL |  | The date/time that the first ETL process started that created this record. |
| 3 | `LAST_PROCESS_DT_TM` | DATETIME | NOT NULL |  | The date/time that the last ETL process started that updated this record. |
| 4 | `MILL_LOGICAL_DOMAIN_ID` | DOUBLE | NOT NULL |  | Uniquely identifies the logical domain to which the row data belongs. |
| 5 | `PRIORITY_SEQUENCE` | DOUBLE | NOT NULL |  | Identifies who is responsible for the claim, (i.e. 1 = Primary, 2 = Secondary, 3 = Tertiary). |
| 6 | `RC_D_BILLING_ENTITY_ID` | DOUBLE | NOT NULL | FK→ | Uniquely identifies the billing entity associated to this fact row. |
| 7 | `RC_D_BILL_TYPE_ID` | DOUBLE | NOT NULL | FK→ | Uniquely identifies the bill type related to this fact row. |
| 8 | `RC_D_CLAIM_EVENT_TYPE_ID` | DOUBLE | NOT NULL | FK→ | Uniquely identifies a claim event type dimension row related to this fact row. |
| 9 | `RC_D_FINANCIAL_CLASS_ID` | DOUBLE | NOT NULL | FK→ | Uniquely identifies the financial class related to this fact row. |
| 10 | `RC_D_HEALTH_PLAN_ID` | DOUBLE | NOT NULL | FK→ | Uniquely identifies the health plan for which this claim was generated. |
| 11 | `RC_F_DAILY_CLAIM_EVENT_SMRY_ID` | DOUBLE | NOT NULL |  | Uniquely identifies aggregated claim data for a given activity date. |
| 12 | `SHR_D_LOCATION_ID` | DOUBLE | NOT NULL | FK→ | Uniquely identifies the patient encounter location at the time of the claim event. |
| 13 | `TOTAL_BILLED_AMT` | DOUBLE | NOT NULL |  | Represents the total amount billed of all the claims aggregated into a given row for a given activity date. |
| 14 | `TOTAL_DAYS_SINCE_DISCHARGE` | DOUBLE | NOT NULL |  | Represents the total number of days between discharge and the claim event (submission for example) for all of the claims summarized for a given activity date. |
| 15 | `TOTAL_DAYS_SINCE_GENERATION` | DOUBLE | NOT NULL |  | Represents the total number of days between generation and the claim event (submission for example) for all of the claims summarized for a given activity date. |
| 16 | `TOTAL_DAYS_SINCE_SUBMISSION` | DOUBLE | NOT NULL |  | Represents the total number of days between submission and the claim event (transmission for example) for all of the claims summarized for a given activity date. |
| 17 | `TOTAL_NUMBER_OF_CLAIMS` | DOUBLE | NOT NULL |  | Represents the number of claims that have been aggregated into this row for the given activity date. |
| 18 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 19 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 20 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 21 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 22 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `ACTIVITY_DT_NBR` | [OMF_DATE](OMF_DATE.md) | `DT_NBR` |
| `RC_D_BILLING_ENTITY_ID` | [RC_D_BILLING_ENTITY](RC_D_BILLING_ENTITY.md) | `RC_D_BILLING_ENTITY_ID` |
| `RC_D_BILL_TYPE_ID` | [RC_D_BILL_TYPE](RC_D_BILL_TYPE.md) | `RC_D_BILL_TYPE_ID` |
| `RC_D_CLAIM_EVENT_TYPE_ID` | [RC_D_CLAIM_EVENT_TYPE](RC_D_CLAIM_EVENT_TYPE.md) | `RC_D_CLAIM_EVENT_TYPE_ID` |
| `RC_D_FINANCIAL_CLASS_ID` | [RC_D_FINANCIAL_CLASS](RC_D_FINANCIAL_CLASS.md) | `RC_D_FINANCIAL_CLASS_ID` |
| `RC_D_HEALTH_PLAN_ID` | [RC_D_HEALTH_PLAN](RC_D_HEALTH_PLAN.md) | `RC_D_HEALTH_PLAN_ID` |
| `SHR_D_LOCATION_ID` | [SHR_D_LOCATION](SHR_D_LOCATION.md) | `SHR_D_LOCATION_ID` |

