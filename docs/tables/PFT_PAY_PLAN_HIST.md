# PFT_PAY_PLAN_HIST

> Profit payment plan history

**Description:** PFT PAY PLAN HIST  
**Table type:** ACTIVITY  
**Primary key:** _(not published — see note)_  
**Columns:** 32

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ACTIVE_IND` | DOUBLE |  |  | The table row is active or inactive. A row is generally active unless it is in an inactive state such as logically deleted, combined away, pending purge, etc. |
| 2 | `ACTIVE_STATUS_CD` | DOUBLE | NOT NULL |  | Indicates the status of the row itself (not the data in the row) such as active, inactive, combined away, pending purge, etc. |
| 3 | `ACTIVE_STATUS_DT_TM` | DATETIME |  |  | The date and time that the active_status_cd was set. |
| 4 | `ACTIVE_STATUS_PRSNL_ID` | DOUBLE | NOT NULL |  | The person who caused the active_status_cd to be set or change. |
| 5 | `AGENCY_NAME` | VARCHAR(200) |  |  | Stores the name of the agency. |
| 6 | `BEGIN_PLAN_DT_TM` | DATETIME |  |  | The date/time that the first payment is due |
| 7 | `BEG_EFFECTIVE_DT_TM` | DATETIME | NOT NULL |  | The date and time for which this table row becomes effective. Normally, this will be the date and time the row is added, but could be a past or future date and time. |
| 8 | `BILLING_ENTITY_GROUP_ID` | DOUBLE | NOT NULL |  | Uniquely identifies the related billing entity group. |
| 9 | `BILLING_ENTITY_ID` | DOUBLE | NOT NULL | FK→ | Foreign key to the Billing Entity for this payment plan. |
| 10 | `CONTRIBUTOR_SYSTEM_CD` | DOUBLE | NOT NULL |  | Contributor system identifies the source feed of data from which a row was populated. This is mainly used to determine how to update a set of data that may have originated from more than one source feed. |
| 11 | `CURRENT_PERIOD_START_DT_TM` | DATETIME |  |  | The start date/time of the current period for this plan. |
| 12 | `CURRENT_PLAN_STATUS_CD` | DOUBLE | NOT NULL |  | The current status of the payment plan |
| 13 | `CYCLE_LENGTH` | DOUBLE | NOT NULL |  | The length of the cycle between statements |
| 14 | `DUE_DAY` | DOUBLE |  |  | The day of the month that the payment is due by such as the 15th of the month. |
| 15 | `DURATION_PLAN_DT_TM` | DATETIME |  |  | The date that the plan should be paid off. This will be calculated based on the payment amount and number of payments. |
| 16 | `ENDING_PLAN_DT_TM` | DATETIME |  |  | The date/time that the pft_encntr was removed from a formal plan either by being paid or sent back to collection. |
| 17 | `ENDING_PLAN_STATUS_CD` | DOUBLE | NOT NULL |  | The status when the plan ended. Currently either FORMALNOPAY or PAIDIN FULL. |
| 18 | `END_EFFECTIVE_DT_TM` | DATETIME | NOT NULL |  | The date/time after which the row is no longer valid as active current data. This may be valued with the date that the row became inactive. |
| 19 | `INSTALLMENT_AMOUNT` | DOUBLE | NOT NULL |  | Total dollar amount that is due each period |
| 20 | `MINIMUM_INSTALLMENT_AMT` | DOUBLE |  |  | Stores the minimum installment amount. |
| 21 | `NUMBER_OF_PAYMENTS` | DOUBLE |  |  | The number of payments that will be made under the current plan. |
| 22 | `OVERRIDE_PRSNL_ID` | DOUBLE | NOT NULL |  | Stores the overriding FPP installment amount person ID. |
| 23 | `PARENT_ENTITY_ID` | DOUBLE | NOT NULL |  | Foreign key to the person_id for the guarantor |
| 24 | `PARENT_ENTITY_NAME` | VARCHAR(32) |  |  | Name of the parent entity |
| 25 | `PFT_PAYMENT_PLAN_ID` | DOUBLE | NOT NULL | FK→ | Foreign key to the pft_payment_plan table |
| 26 | `PFT_PAY_PLAN_HIST_ID` | DOUBLE | NOT NULL |  | The unique identifier to the table |
| 27 | `TOTAL_AMOUNT_DUE` | DOUBLE | NOT NULL |  | The total amount due when the formal payment plan originated |
| 28 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 29 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 30 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 31 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 32 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `BILLING_ENTITY_ID` | [BILLING_ENTITY](BILLING_ENTITY.md) | `BILLING_ENTITY_ID` |
| `PFT_PAYMENT_PLAN_ID` | [PFT_PAYMENT_PLAN](PFT_PAYMENT_PLAN.md) | `PFT_PAYMENT_PLAN_ID` |

