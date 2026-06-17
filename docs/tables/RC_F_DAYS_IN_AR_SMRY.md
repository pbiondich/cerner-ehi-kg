# RC_F_DAYS_IN_AR_SMRY

> This table contains summarized days in AR data.

**Description:** Revenue Cycle Fact Days in AR Summary  
**Table type:** ACTIVITY  
**Primary key:** _(not published — see note)_  
**Columns:** 15

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ACTIVITY_DT_NBR` | DOUBLE | NOT NULL | FK→ | A number representing the activity date. References the key in the OMF_DATE table. |
| 2 | `FIRST_PROCESS_DT_TM` | DATETIME | NOT NULL |  | The date/time that the first ETL process started that created this record. |
| 3 | `LAST_PROCESS_DT_TM` | DATETIME | NOT NULL |  | The date/time that the last ETL process started that updated this record. |
| 4 | `MILL_LOGICAL_DOMAIN_ID` | DOUBLE | NOT NULL |  | Uniquely identifies the logical domain to which the row data belongs. |
| 5 | `RC_D_BILLING_ENTITY_ID` | DOUBLE | NOT NULL | FK→ | Uniquely identifies the billing entity related to this fact row. |
| 6 | `RC_D_DISCHARGE_AGE_ID` | DOUBLE | NOT NULL | FK→ | Uniquely identifies the age category to which this fact row is related based on the discharge age. |
| 7 | `RC_D_HOLD_ID` | DOUBLE | NOT NULL | FK→ | Uniquely identifies the hold related to this fact row. |
| 8 | `RC_F_DAYS_IN_AR_SMRY_ID` | DOUBLE | NOT NULL |  | Uniquely identifies summarized days in AR data. |
| 9 | `TOTAL_DAYS_IN_AR` | DOUBLE | NOT NULL |  | Represents the average number of days spent recovering AR. |
| 10 | `TOT_CREDIT_BALANCE_DAYS_IN_AR` | DOUBLE | NOT NULL |  | Represents the average number of days spent recovering credit AR. |
| 11 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 12 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 13 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 14 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 15 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `ACTIVITY_DT_NBR` | [OMF_DATE](OMF_DATE.md) | `DT_NBR` |
| `RC_D_BILLING_ENTITY_ID` | [RC_D_BILLING_ENTITY](RC_D_BILLING_ENTITY.md) | `RC_D_BILLING_ENTITY_ID` |
| `RC_D_DISCHARGE_AGE_ID` | [RC_D_AGE_CATEGORY](RC_D_AGE_CATEGORY.md) | `RC_D_AGE_CATEGORY_ID` |
| `RC_D_HOLD_ID` | [RC_D_HOLD](RC_D_HOLD.md) | `RC_D_HOLD_ID` |

