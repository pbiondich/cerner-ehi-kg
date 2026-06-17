# BENEFIT_ORDER

> Benefit Order

**Description:** Store the information related to a benefit order.  
**Table type:** ACTIVITY  
**Primary key:** `BENEFIT_ORDER_ID`  
**Columns:** 55  
**Referenced by:** 7 columns

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ACTIVE_IND` | DOUBLE |  |  | The table row is active or inactive. A row is generally active unless it is in an inactive state such as logically deleted, combined away, pending purge, etc. |
| 2 | `ACTIVE_STATUS_CD` | DOUBLE | NOT NULL |  | Indicates the status of the row itself (not the data in the row) such as active, inactive, combined away, pending purge, etc. |
| 3 | `ACTIVE_STATUS_DT_TM` | DATETIME |  |  | The date and time that the active_status_cd was set. |
| 4 | `ACTIVE_STATUS_PRSNL_ID` | DOUBLE | NOT NULL |  | The person who caused the active_status_cd to be set or change. |
| 5 | `ALIAS_SEQ` | DOUBLE |  |  | ** OBSOLETE ** Alias sequence for insurance benefit orders. ** OBSOLETE ** |
| 6 | `BEG_EFFECTIVE_DT_TM` | DATETIME |  |  | The date and time for which this table row becomes effective. Normally, this will be the date and time the row is added, but could be a past or future date and time. |
| 7 | `BEG_SERVICE_DT_TM` | DATETIME |  |  | The service date and time at which the benefit order begins. |
| 8 | `BENEFIT_ORDER_ID` | DOUBLE | NOT NULL | PK | System defined unique identifier of a benefit order. |
| 9 | `BO_STATUS_CD` | DOUBLE | NOT NULL |  | State of the benefit order at a particular instance of time |
| 10 | `BO_STATUS_REASON_CD` | DOUBLE | NOT NULL |  | Reason for state of benefit order. |
| 11 | `BT_CONDITION_ID` | DOUBLE | NOT NULL | FK→ | Foreign key to the bt_condition table |
| 12 | `COLLECTION_ST_CD` | DOUBLE | NOT NULL |  | ** OBSOLETE ** CodeSet 25095 Identifies the collection state ** OBSOLETE ** |
| 13 | `CONS_BO_SCHED_ID` | DOUBLE | NOT NULL | FK→ | Foreign key reference to the cons_bo_sched table. |
| 14 | `CROSS_OVER_IND` | DOUBLE |  |  | Indicates whether or not health plan is a cooperative plan. |
| 15 | `DISP_NONCOVERED_IND` | DOUBLE |  |  | Indicates whether or not to display non-covered charges on a bill. |
| 16 | `DUNNING_HOLD_IND` | DOUBLE | NOT NULL |  | ** OBSOLETE ** Indicates if this benefit order remains at the same dunning level regardless of the other criteria. ** OBSOLETE ** |
| 17 | `DUNNING_IND` | DOUBLE | NOT NULL |  | ** OBSOLETE ** Indicates whether this financial encounter is excluded from dunning messages ** OBSOLETE ** |
| 18 | `DUNNING_LEVEL_CD` | DOUBLE | NOT NULL |  | ** OBSOLETE ** Specifies the state of an account ** OBSOLETE ** |
| 19 | `DUNNING_LEVEL_CHANGE_DT_TM` | DATETIME |  |  | ** OBSOLETE ** Date the dunning level was changed by the bill record generation process ** OBSOLETE ** |
| 20 | `DUNNING_LEVEL_CNT` | DOUBLE |  |  | ** OBSOLETE ** Indicates how many times a bill has been sent at the current dunning level code. ** OBSOLETE ** |
| 21 | `DUNNING_NO_PAY_CNT` | DOUBLE |  |  | ** OBSOLETE ** The number of times that no payament has been received at this dunning level. ** OBSOLETE ** |
| 22 | `DUNNING_PAY_CNT` | DOUBLE |  |  | ** OBSOLETE ** The number of times that an acceptable payment has been received at this dunning level. ** OBSOLETE ** |
| 23 | `DUNNING_UNACC_PAY_CNT` | DOUBLE |  |  | ** OBSOLETE ** The number of times and an unacceptable payment has been received at this dunning level. ** OBSOLETE ** |
| 24 | `ENCNTR_PLAN_RELTN_ID` | DOUBLE | NOT NULL |  | Foreign key reference to Encntr_plan_reltn. |
| 25 | `END_EFFECTIVE_DT_TM` | DATETIME |  |  | The date/time after which the row is no longer valid as active current data. This may be valued with the date that the row became inactive. |
| 26 | `END_SERVICE_DT_TM` | DATETIME |  |  | Service date and time at which the benefit order ends. |
| 27 | `EOP_DT_TM` | DATETIME |  |  | The End of Period date for the charge group's encounter. Used to quickly determine if a new charge group must be created during charge group creation |
| 28 | `EPR_UPT_CNT` | DOUBLE |  |  | Number of times Encounter Plan Relation has been updated. |
| 29 | `FIN_CLASS_CD` | DOUBLE | NOT NULL |  | Financial class of health plan. |
| 30 | `HEALTH_PLAN_ID` | DOUBLE | NOT NULL | FK→ | Foreign key reference to health plan. |
| 31 | `MAN_EDIT_IND` | DOUBLE |  |  | Indicates whether or not BO has been manually edited. |
| 32 | `ORIG_BILL_DT_TM` | DATETIME |  |  | The date and time the bill was originally billed. |
| 33 | `ORIG_DUE_DT_TM` | DATETIME |  |  | The date and time when the bill is originally due. |
| 34 | `PARENT_BO_ID` | DOUBLE | NOT NULL | FK→ | Allows relationships between Benefit Orders - No longer used |
| 35 | `PAT_BILL_PREF_FLAG` | DOUBLE |  |  | Values: (0) Sequential patient billing, (1) Concurrent patient billing, (2) Don't bill patient, (3) Bill patient only when due |
| 36 | `PAT_CONCURRENT_IND` | DOUBLE |  |  | Indicate whether a patient should be billed at the same time when the bill is sent to the health paln |
| 37 | `PFT_ENCNTR_ID` | DOUBLE | NOT NULL | FK→ | Foreign key to the pft_encntr_id |
| 38 | `PREVIOUS_PFT_ENCNTR_ID` | DOUBLE | NOT NULL |  | Stores the pft_encntr_id that this benefit_order was previously associated to prior to a financial encounter combine. |
| 39 | `PRIORITY_SEQ` | DOUBLE |  |  | Priority sequence of health plan in which it is billed. |
| 40 | `PRI_CONCURRENT_IND` | DOUBLE |  |  | Indicates whether or not health plan allows concurrent billing of secondary plan when this plan is primary. |
| 41 | `PRORATION_FLAG` | DOUBLE |  |  | Shows if this Benefit_order is affected by proration. 0 - No proration has been done, but needs to be. 1 - Proration has been done. 2 - No proration calculations are to be done. |
| 42 | `SEC_CONCURRENT_IND` | DOUBLE |  |  | Indicates whether or not health plan allows concurrent billing of other plans when this plan is not primary. |
| 43 | `SELF_PAY_STATUS_CD` | DOUBLE |  |  | ** OBSOLETE ** Uniquely identifies pay status. ** OBSOLETE ** |
| 44 | `STATEMENT_CYCLE_ID` | DOUBLE |  |  | ** OBSOLETE ** Uniquely identifies the related row on the statement_cycle table. ** OBSOLETE ** |
| 45 | `SUBSCRIBER_ID` | DOUBLE | NOT NULL |  | Identifies the person who is the subscriber of the health plan. |
| 46 | `TOTAL_CHARGE_AMT` | DOUBLE | NOT NULL |  | The sum of all group charges |
| 47 | `TOTAL_CHARGE_AMT_DR_CR_FLAG` | DOUBLE |  |  | The debit/credit flag for the total_charge_amt field |
| 48 | `UB_BILL_CLASS_CD` | DOUBLE | NOT NULL |  | UB bill class cd - No longer used |
| 49 | `UB_BILL_FREQ_CD` | DOUBLE | NOT NULL |  | Bill Frequency code - No longer used |
| 50 | `UB_FACILITY_TYPE_CD` | DOUBLE | NOT NULL |  | UB Facility Type Code - No longer used |
| 51 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 52 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 53 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 54 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 55 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `BT_CONDITION_ID` | [BT_CONDITION](BT_CONDITION.md) | `BT_CONDITION_ID` |
| `CONS_BO_SCHED_ID` | [CONS_BO_SCHED](CONS_BO_SCHED.md) | `CONS_BO_SCHED_ID` |
| `HEALTH_PLAN_ID` | [HEALTH_PLAN](HEALTH_PLAN.md) | `HEALTH_PLAN_ID` |
| `PARENT_BO_ID` | [BENEFIT_ORDER](BENEFIT_ORDER.md) | `BENEFIT_ORDER_ID` |
| `PFT_ENCNTR_ID` | [PFT_ENCNTR](PFT_ENCNTR.md) | `PFT_ENCNTR_ID` |

## Referenced by (7)

| From table | Column |
|------------|--------|
| [BENEFIT_ORDER](BENEFIT_ORDER.md) | `PARENT_BO_ID` |
| [BO_HP_RELTN](BO_HP_RELTN.md) | `BENEFIT_ORDER_ID` |
| [PFT_BILL_SUMMARY](PFT_BILL_SUMMARY.md) | `BENEFIT_ORDER_ID` |
| [PFT_CHARGE_BO_RELTN](PFT_CHARGE_BO_RELTN.md) | `BENEFIT_ORDER_ID` |
| [PFT_CHRG_GRP_RPRCS](PFT_CHRG_GRP_RPRCS.md) | `BENEFIT_ORDER_ID` |
| [PFT_CHRG_GRP_RPRCS_HIST](PFT_CHRG_GRP_RPRCS_HIST.md) | `BENEFIT_ORDER_ID` |
| [PFT_ENCNTR_COLLECTION_RELTN](PFT_ENCNTR_COLLECTION_RELTN.md) | `BENEFIT_ORDER_ID` |

