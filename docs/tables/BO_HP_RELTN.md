# BO_HP_RELTN

> Stores benefit order and health plan relationships for claim generation

**Description:** BENEFIT ORDER HEALTH PLAN RELATION  
**Table type:** ACTIVITY  
**Primary key:** `BO_HP_RELTN_ID`  
**Columns:** 43  
**Referenced by:** 13 columns

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ACTIVE_IND` | DOUBLE |  |  | The table row is active or inactive. A row is generally active unless it is in an inactive state such as logically deleted, combined away, pending purge, etc. |
| 2 | `ACTIVE_STATUS_CD` | DOUBLE | NOT NULL |  | Indicates the status of the row itself (not the data in the row) such as active, inactive, combined away, pending purge, etc. |
| 3 | `ACTIVE_STATUS_DT_TM` | DATETIME |  |  | The date and time that the active_status_cd was set. |
| 4 | `ACTIVE_STATUS_PRSNL_ID` | DOUBLE | NOT NULL |  | The person who caused the active_status_cd to be set or change. |
| 5 | `AMOUNT_OWED` | DOUBLE | NOT NULL |  | Current amount owed for this health plan |
| 6 | `AMOUNT_OWED_DR_CR_FLAG` | DOUBLE |  |  | Debit/Credit flag for the Amount Owed |
| 7 | `BEG_EFFECTIVE_DT_TM` | DATETIME | NOT NULL |  | The date and time for which this table row becomes effective. Normally, this will be the date and time the row is added, but could be a past or future date and time. |
| 8 | `BENEFIT_ORDER_ID` | DOUBLE | NOT NULL | FK→ | Foreign key to the benefit_order table |
| 9 | `BILL_TEMPL_ID` | DOUBLE | NOT NULL |  | Relates this record to a specific Bill Template. |
| 10 | `BO_HP_RELTN_ID` | DOUBLE | NOT NULL | PK | Primary key to the bo_hp_reltn table |
| 11 | `BO_HP_STATUS_CD` | DOUBLE | NOT NULL |  | Status of the bo_hp |
| 12 | `ENCNTR_PLAN_RELTN_ID` | DOUBLE | NOT NULL |  | Identifier of the encounter plan relation |
| 13 | `END_EFFECTIVE_DT_TM` | DATETIME | NOT NULL |  | The date/time after which the row is no longer valid as active current data. This may be valued with the date that the row became inactive. |
| 14 | `FIN_CLASS_CD` | DOUBLE | NOT NULL |  | Financial class code from the clinical encounter |
| 15 | `HEALTH_PLAN_ID` | DOUBLE | NOT NULL | FK→ | Foreign key to the health plan table |
| 16 | `LAST_ADJUST_DT_TM` | DATETIME |  |  | Date of last adjustment received |
| 17 | `LAST_BILLED_DT_TM` | DATETIME |  |  | Date that the benefit order/health plan was billed |
| 18 | `LAST_PAYMENT_DT_TM` | DATETIME |  |  | Date of last payment received |
| 19 | `ORIG_BILL_DT_TM` | DATETIME |  |  | Date that original bill was generated |
| 20 | `ORIG_BILL_SUBMIT_DT_TM` | DATETIME |  |  | A date / time stamp that will identify the date/time the bill was originally submitted to a third party. |
| 21 | `ORIG_BILL_TRANSMIT_DT_TM` | DATETIME |  |  | A date / time stamp that will identify the date/time the bill was originally transmitted to a third party. |
| 22 | `PAYOR_ORG_ID` | DOUBLE | NOT NULL |  | Contains the id from the organization table that represents the payor organization. |
| 23 | `PRIORITY_SEQ` | DOUBLE | NOT NULL |  | Sequence of related rows |
| 24 | `RELTN_TYPE_CD` | DOUBLE | NOT NULL |  | Contains the type of relationship between the benefit order and a health plan. |
| 25 | `RESUBMISSION_CNT` | DOUBLE | NOT NULL |  | Represents the number of times the claim has been resubmitted |
| 26 | `ROLL_DT_TM` | DATETIME |  |  | Date that the benefit order was rolled |
| 27 | `ROLL_REASON_CD` | DOUBLE | NOT NULL |  | Rolled reason code (i.e. manual, actual, expected, automated) |
| 28 | `ROLL_REVIEW_IND` | DOUBLE | NOT NULL |  | This indicator is used to identify whether or not the bo_hp_reltn record is sitting in workflow waiting for review. |
| 29 | `ROLL_TASK_ID` | DOUBLE | NOT NULL |  | Task identifier of what task rolled the benefit order. This field is populated with the current task that is executing in CCL (reqinfo->updt_task ) when an amount is "rolled" (transferred) from one bo_hp_reltn row to another. |
| 30 | `ROLL_USER_ID` | DOUBLE | NOT NULL |  | User identifier for who rolled the benefit order |
| 31 | `STMT_STATUS_CD` | DOUBLE | NOT NULL |  | statement status code (i.e. none, generated, generated with late charges) |
| 32 | `TIMELY_FILE_IND` | DOUBLE | NOT NULL |  | The column indicates if the BO_HP_RELTN should qualify for claim generation ignoring all holds. |
| 33 | `TOTAL_ADJ_AMOUNT` | DOUBLE | NOT NULL |  | Total amount of adjustments that have been applied |
| 34 | `TOTAL_ADJ_DR_CR_FLAG` | DOUBLE | NOT NULL |  | Flag to identify whether the total_adj_amount is a debit or credit |
| 35 | `TOTAL_BILLED_AMOUNT` | DOUBLE | NOT NULL |  | Total amount that has been billed |
| 36 | `TOTAL_BILLED_DR_CR_FLAG` | DOUBLE | NOT NULL |  | Flag to identify whether total_billed_amount is a debit or credit |
| 37 | `TOTAL_PAID_AMOUNT` | DOUBLE | NOT NULL |  | The total amount paid by the payor. |
| 38 | `TOTAL_PAID_DR_CR_FLAG` | DOUBLE | NOT NULL |  | Flag to identify whether the total_paid_amount is a debit or credit |
| 39 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 40 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 41 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 42 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 43 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `BENEFIT_ORDER_ID` | [BENEFIT_ORDER](BENEFIT_ORDER.md) | `BENEFIT_ORDER_ID` |
| `HEALTH_PLAN_ID` | [HEALTH_PLAN](HEALTH_PLAN.md) | `HEALTH_PLAN_ID` |

## Referenced by (13)

| From table | Column |
|------------|--------|
| [EXT_REQ_STATUS](EXT_REQ_STATUS.md) | `BO_HP_RELTN_ID` |
| [PE_STATUS_REASON](PE_STATUS_REASON.md) | `BO_HP_RELTN_ID` |
| [PFT_BALANCE](PFT_BALANCE.md) | `BO_HP_RELTN_ID` |
| [PFT_BILL_ACTIVITY](PFT_BILL_ACTIVITY.md) | `BO_HP_RELTN_ID` |
| [PFT_BR_EDIT_FAILURE](PFT_BR_EDIT_FAILURE.md) | `BO_HP_RELTN_ID` |
| [PFT_CM_EVENT_LOG](PFT_CM_EVENT_LOG.md) | `BO_HP_RELTN_ID` |
| [PFT_DAILY_BALANCE_BAL](PFT_DAILY_BALANCE_BAL.md) | `BO_HP_RELTN_ID` |
| [PFT_DAILY_BO_HP_CHRG_BAL](PFT_DAILY_BO_HP_CHRG_BAL.md) | `BO_HP_RELTN_ID` |
| [PFT_PRORATION](PFT_PRORATION.md) | `BO_HP_RELTN_ID` |
| [PFT_QUEUE_ITEM](PFT_QUEUE_ITEM.md) | `BO_HP_RELTN_ID` |
| [PFT_QUEUE_ITEM_HIST](PFT_QUEUE_ITEM_HIST.md) | `BO_HP_RELTN_ID` |
| [PFT_UNIFIED_BILLING_RELTN](PFT_UNIFIED_BILLING_RELTN.md) | `INST_BO_HP_RELTN_ID` |
| [PFT_UNIFIED_BILLING_RELTN](PFT_UNIFIED_BILLING_RELTN.md) | `PROF_BO_HP_RELTN_ID` |

