# PFT_PRORATION

> This table stores the Prorated amounts for each Benefit_Order, if Proration is to be calculated.

**Description:** Stores the Prorated amounts for each Benefit_Order, if Proration is to be calced  
**Table type:** ACTIVITY  
**Primary key:** `PFT_PRORATION_ID`  
**Columns:** 30  
**Referenced by:** 2 columns

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ACTIVE_IND` | DOUBLE | NOT NULL |  | The table row is active or inactive. A row is generally active unless it is in an inactive state such as logically deleted, combined away, pending purge, etc. |
| 2 | `ACTIVE_STATUS_CD` | DOUBLE | NOT NULL |  | Indicates the status of the row itself (not the data in the row) such as active, inactive, combined away, pending purge, etc. |
| 3 | `ACTIVE_STATUS_DT_TM` | DATETIME | NOT NULL |  | The date and time that the active_status_cd was set. |
| 4 | `ACTIVE_STATUS_PRSNL_ID` | DOUBLE | NOT NULL |  | The person who caused the active_status_cd to be set or change. |
| 5 | `BEG_EFFECTIVE_DT_TM` | DATETIME |  |  | The date and time for which this table row becomes effective. Normally, this will be the date and time the row is added, but could be a past or future date and time. |
| 6 | `BO_HP_RELTN_ID` | DOUBLE | NOT NULL | FK→ | Unique Identifier |
| 7 | `CURR_AMOUNT_DR_CR_FLAG` | DOUBLE | NOT NULL |  | Flag showing DR_CR Status of Curr_Amount_Due |
| 8 | `CURR_AMT_DUE` | DOUBLE | NOT NULL |  | The Current Amount Due for this realationship |
| 9 | `END_EFFECTIVE_DT_TM` | DATETIME |  |  | The date/time after which the row is no longer valid as active current data. This may be valued with the date that the row became inactive. |
| 10 | `HEALTH_PLAN_ID` | DOUBLE | NOT NULL | FK→ | Unique identifier of a health plan for the health_plan table |
| 11 | `HIGH_AMOUNT_DR_CR_FLAG` | DOUBLE | NOT NULL |  | Flag showing DR_CR Status of High_Amount_Due |
| 12 | `HIGH_AMT` | DOUBLE | NOT NULL |  | The Highest Amount calculated for this relationship |
| 13 | `NON_COVERED_AMT` | DOUBLE | NOT NULL |  | The Amount that is not covered by the deductible - primarily for Pat Res |
| 14 | `NON_COVERED_AMT_DR_CR_FLAG` | DOUBLE | NOT NULL |  | Flag showing DR_CR Status of Non_Covered_Amount |
| 15 | `ORIG_AMOUNT_DR_CR_FLAG` | DOUBLE | NOT NULL |  | Flag showing DR_CR Status of Orig_Amount_Due |
| 16 | `ORIG_AMT_DUE` | DOUBLE | NOT NULL |  | Original Amount calculated for this relationship |
| 17 | `PERSON_ID` | DOUBLE | NOT NULL | FK→ | This is the value of the unique primary identifier of the person table. It is an internal system assigned number. |
| 18 | `PFT_ENCNTR_ID` | DOUBLE | NOT NULL | FK→ | The PFT_Encntr related to this data - Foreign Key-PFT_ENCNTR |
| 19 | `PFT_PRORATION_ID` | DOUBLE | NOT NULL | PK | Primary Key : Built from pft_activity_seq |
| 20 | `PRIORITY_SEQ` | DOUBLE |  |  | If the Proration_Type_CD = PAYEROTHER then this field will store the level of the payer - 2, 3, so forth |
| 21 | `PRORATION_TYPE_CD` | DOUBLE | NOT NULL |  | The type of relationship to this record |
| 22 | `TOTAL_ADJ` | DOUBLE | NOT NULL |  | Total Adjustments made on this relationship |
| 23 | `TOTAL_ADJ_DR_CR_FLAG` | DOUBLE | NOT NULL |  | Flag showing DR_CR Status of Total_Adjustment |
| 24 | `TOTAL_PAY_AMT` | DOUBLE | NOT NULL |  | Total payments made on this relationship. |
| 25 | `TOTAL_PAY_AMT_DR_CR_FLAG` | DOUBLE | NOT NULL |  | Flag showing debit/credit status of total pay. |
| 26 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 27 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 28 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 29 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 30 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `BO_HP_RELTN_ID` | [BO_HP_RELTN](BO_HP_RELTN.md) | `BO_HP_RELTN_ID` |
| `HEALTH_PLAN_ID` | [HEALTH_PLAN](HEALTH_PLAN.md) | `HEALTH_PLAN_ID` |
| `PERSON_ID` | [PERSON](PERSON.md) | `PERSON_ID` |
| `PFT_ENCNTR_ID` | [PFT_ENCNTR](PFT_ENCNTR.md) | `PFT_ENCNTR_ID` |

## Referenced by (2)

| From table | Column |
|------------|--------|
| [PFT_DAILY_BO_HP_BAL](PFT_DAILY_BO_HP_BAL.md) | `PFT_PRORATION_ID` |
| [PFT_PRORATION_RELTN](PFT_PRORATION_RELTN.md) | `PFT_PRORATION_ID` |

