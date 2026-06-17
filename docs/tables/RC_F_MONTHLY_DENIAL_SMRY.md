# RC_F_MONTHLY_DENIAL_SMRY

> This table contains summarizzed denial data by month.

**Description:** Revenue Cycle Fact Monthly Denial Summary  
**Table type:** ACTIVITY  
**Primary key:** _(not published — see note)_  
**Columns:** 18

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ACTIVITY_YEAR` | DOUBLE | NOT NULL |  | Contains the year in which the activity took place. |
| 2 | `DENIAL_BILLED_AMT` | DOUBLE | NOT NULL |  | The dollar amount associated with the denied bill. |
| 3 | `FIRST_PROCESS_DT_TM` | DATETIME | NOT NULL |  | The date/time that the first ETL process started that created this record. |
| 4 | `LAST_PROCESS_DT_TM` | DATETIME | NOT NULL |  | The date/time that the last ETL process started that updated this record. |
| 5 | `MILL_LOGICAL_DOMAIN_ID` | DOUBLE | NOT NULL |  | Uniquely identifies the logical domain to which the row data belongs. |
| 6 | `RC_D_BILLING_ENTITY_ID` | DOUBLE | NOT NULL | FK→ | Uniquely identifies the billing entity related to this fact row. |
| 7 | `RC_D_BILL_TYPE_ID` | DOUBLE | NOT NULL | FK→ | Uniquely identifies the bill type related to this fact row. |
| 8 | `RC_D_DENIAL_ALIAS_ID` | DOUBLE | NOT NULL | FK→ | The number that uniquely identifies a denial. |
| 9 | `RC_D_ENCNTR_TYPE_CLASS_ID` | DOUBLE | NOT NULL | FK→ | Uniquely identifies the encounter type class of the encounter associated to this denial. |
| 10 | `RC_D_FINANCIAL_CLASS_ID` | DOUBLE | NOT NULL | FK→ | Uniquely identifies the financial class of the health plan associated to the claim for which this denial was posted. |
| 11 | `RC_D_HEALTH_PLAN_ID` | DOUBLE | NOT NULL | FK→ | Uniquely identifies the health plan associated to the claim for which this denial was posted. |
| 12 | `RC_F_MONTHLY_DENIAL_SMRY_ID` | DOUBLE | NOT NULL |  | Uniquely identifies summarized denial data by month. |
| 13 | `SHR_D_MONTH_ID` | DOUBLE | NOT NULL | FK→ | Uniquely identifies the month related to this fact row. |
| 14 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 15 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 16 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 17 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 18 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `RC_D_BILLING_ENTITY_ID` | [RC_D_BILLING_ENTITY](RC_D_BILLING_ENTITY.md) | `RC_D_BILLING_ENTITY_ID` |
| `RC_D_BILL_TYPE_ID` | [RC_D_BILL_TYPE](RC_D_BILL_TYPE.md) | `RC_D_BILL_TYPE_ID` |
| `RC_D_DENIAL_ALIAS_ID` | [RC_D_DENIAL_ALIAS](RC_D_DENIAL_ALIAS.md) | `RC_D_DENIAL_ALIAS_ID` |
| `RC_D_ENCNTR_TYPE_CLASS_ID` | [RC_D_ENCNTR_TYPE_CLASS](RC_D_ENCNTR_TYPE_CLASS.md) | `RC_D_ENCNTR_TYPE_CLASS_ID` |
| `RC_D_FINANCIAL_CLASS_ID` | [RC_D_FINANCIAL_CLASS](RC_D_FINANCIAL_CLASS.md) | `RC_D_FINANCIAL_CLASS_ID` |
| `RC_D_HEALTH_PLAN_ID` | [RC_D_HEALTH_PLAN](RC_D_HEALTH_PLAN.md) | `RC_D_HEALTH_PLAN_ID` |
| `SHR_D_MONTH_ID` | [SHR_D_MONTH](SHR_D_MONTH.md) | `SHR_D_MONTH_ID` |

