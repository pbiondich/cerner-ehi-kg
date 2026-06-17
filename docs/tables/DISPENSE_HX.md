# DISPENSE_HX

> Table to store historical pharmacy dispensing information

**Description:** Dispense History  
**Table type:** ACTIVITY  
**Primary key:** `DISPENSE_HX_ID`  
**Columns:** 109  
**Referenced by:** 44 columns

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ACTION_SEQUENCE` | DOUBLE | NOT NULL |  | Identifier to reference the action taken from order action |
| 2 | `ADJUSTMENT_DT_TM` | DATETIME |  |  | The data time this record was adjusted. |
| 3 | `AUTHORIZATION_NBR` | VARCHAR(50) |  |  | Authorization number for claims |
| 4 | `AUTO_CREDIT_IND` | DOUBLE | NOT NULL |  | Indicates if auto crediting should be performed on scheduled administration charge doses. |
| 5 | `BATCH_IDENT_TXT` | VARCHAR(40) |  |  | This is a unique identification assigned to each batch of dispensing data to be transferred outbound by FSI |
| 6 | `BILL_QTY` | DOUBLE |  |  | THE Bill Quantity |
| 7 | `CHARGE_DT_TM` | DATETIME |  |  | Date and time charge transaction sent |
| 8 | `CHARGE_IND` | DOUBLE |  |  | Flag to indicate whether charges were dropped |
| 9 | `CHARGE_ON_SCHED_ADMIN_IND` | DOUBLE | NOT NULL |  | Indicates if charges for a dispense should be based on the scheduled administration date for a particular dose. |
| 10 | `CHARGE_TZ` | DOUBLE |  |  | Time zone associated with the corresponding DT_TM column. |
| 11 | `CHRG_DISPENSE_HX_ID` | DOUBLE | NOT NULL | FK→ | The DISPENSE_HX_ID of the parent row (the parent charge related to this credit event row). |
| 12 | `CONTRIBUTOR_SYSTEM_CD` | DOUBLE | NOT NULL | FK→ | Contributor system identifies the source feed of data from which a row was populated. This is mainly used to determine how to update a set of data that may have originated from more than one source feed. |
| 13 | `CONTROL_IDENT_TXT` | VARCHAR(40) |  |  | This is a unique identification assigned by FSI to distinctly identify each individual dispense that is sent in a batch |
| 14 | `COPAY` | DOUBLE |  |  | Copay amount of dispense transaction |
| 15 | `COPAY_TIER_CD` | DOUBLE |  |  | Medications are assigned to one of several categories, knows as copay tiers, based on drug usage, cost and clinical effectiveness. This will be used to determine the charges while dispensing a drug. Examples are Generics, and Brand-name drugs. |
| 16 | `COST` | DOUBLE |  |  | the Cost |
| 17 | `CRDT_DISPENSE_HX_ID` | DOUBLE | NOT NULL | FK→ | The DISPENSE_HX_ID of the parent row (the parent credit related to this charge event row). |
| 18 | `DISCOUNT_AMOUNT` | DOUBLE |  |  | Discount amount of dispense transcation. |
| 19 | `DISPENSE_CATEGORY_CD` | DOUBLE |  |  | The dispense category that was applied to this dispense. |
| 20 | `DISPENSE_DT_TM` | DATETIME |  |  | date and time of dispense transaction |
| 21 | `DISPENSE_FEE` | DOUBLE |  |  | the dispense fee |
| 22 | `DISPENSE_HX_ID` | DOUBLE | NOT NULL | PK | The unique identifier for a dispensing event |
| 23 | `DISPENSE_PRSNL_ID` | DOUBLE | NOT NULL | FK→ | Identifier for personnel performing dispense event |
| 24 | `DISPENSE_TZ` | DOUBLE |  |  | Time zone associated with the corresponding DT_TM column. For inpatient rows, this is the time zone of the encounter. For Retail Pharmacy, it is the time zone of the pharmacy's facility. |
| 25 | `DISP_EVENT_TYPE_CD` | DOUBLE | NOT NULL |  | Identifier for the kind of dispense activity which occurred (extra dose, fill list, cart dose) |
| 26 | `DISP_LOC_CD` | DOUBLE | NOT NULL | FK→ | Identifies the Pharmacy Location where a dispense event occurred. |
| 27 | `DISP_PRIORITY_CD` | DOUBLE | NOT NULL |  | Dispense Priority of dispense transaction |
| 28 | `DISP_PRIORITY_DT_TM` | DATETIME |  |  | the Dispense Priority Date and Time |
| 29 | `DISP_PRIORITY_TZ` | DOUBLE |  |  | Time zone associated with the corresponding DT_TM column. |
| 30 | `DISP_QTY` | DOUBLE |  |  | Dispense Quantity for this dispense transaction |
| 31 | `DISP_QTY_UNIT_CD` | DOUBLE | NOT NULL |  | dispense quantity unit code |
| 32 | `DISP_SR_CD` | DOUBLE | NOT NULL |  | Service Resource Code of the Dispensing Location |
| 33 | `DOSES` | DOUBLE |  |  | The quantity of administrations dispensed |
| 34 | `EARLY_REASON_CD` | DOUBLE | NOT NULL |  | early reason code |
| 35 | `EVENT_ID` | DOUBLE | NOT NULL |  | Clinical Even ID |
| 36 | `EVENT_TOTAL_PRICE` | DOUBLE |  |  | Total Price associated with a dispense event |
| 37 | `EXTRA_REASON_CD` | DOUBLE | NOT NULL |  | extra reason code |
| 38 | `FILL_ANCHOR_DT_TM` | DATETIME |  |  | It is the Fill Date used to calculate the next dispense date/time. |
| 39 | `FILL_HX_ID` | DOUBLE | NOT NULL | FK→ | Unique identifier from fill_batch_hx pointing to which batch this dispense event is from |
| 40 | `FILL_NBR` | DOUBLE |  |  | Fill number for dispense transaction |
| 41 | `FIRST_DOSE_TIME` | DATETIME |  |  | Date and time of the first dose |
| 42 | `FIRST_DOSE_TZ` | DOUBLE |  |  | Time zone associated with the corresponding DT_TM column. |
| 43 | `FIRST_IV_SEQ` | DOUBLE |  |  | Sequence number of the first bag within an alternating IV |
| 44 | `FIRST_SCHEDULE_SEQ` | DOUBLE | NOT NULL |  | A single DISPENSE_HX row may contain multiple dispensed doses that span multiple schedule_sequences. This is the first schedule sequence dispensed for calculating which schedule_sequences were dispensed. |
| 45 | `FUTURE_CHARGE_IND` | DOUBLE | NOT NULL |  | Value will indicate whether or not charges should occur for a future order. |
| 46 | `GROUPER_DISPENSE_HX_ID` | DOUBLE |  | FK→ | The dispense history id of the first dispense of the group this dispense is a part of. Used to link dispense histories that are a part of the same dispense event. For example, this might link IDD (Individual Dose Dispenses) together.; |
| 47 | `HEALTH_PLAN_ID` | DOUBLE | NOT NULL | FK→ | health plan id |
| 48 | `INCENTIVE_AMT` | DOUBLE |  |  | the Incentive amount |
| 49 | `IVR_REFILL_IND` | DOUBLE |  |  | Indicates that this dispense was initiated via a refill request coming from an interactive voice response system. |
| 50 | `LAST_ADMIN_DT_TM` | DATETIME |  |  | The last administration date and time for a dispense. |
| 51 | `LAST_ADMIN_TZ` | DOUBLE |  |  | The timezone for the last_admin_dt_tm field. |
| 52 | `LATE_REASON_CD` | DOUBLE | NOT NULL |  | the late reason code |
| 53 | `LEVEL5_CD` | DOUBLE | NOT NULL |  | the Work station that started the event |
| 54 | `NEXT_DISPENSE_DT_TM` | DATETIME |  |  | Date/time next dose should be dispensed |
| 55 | `NEXT_DISPENSE_TZ` | DOUBLE |  |  | Time zone associated with the corresponding DT_TM column. |
| 56 | `OFFSET_DISPENSE_HX_ID` | DOUBLE |  | FK→ | Identifier for the waste dispense event which caused the current row's offset charge or credit to occur. |
| 57 | `ORDER_ID` | DOUBLE | NOT NULL | FK→ | Identifier to reference the order dispensed |
| 58 | `ORG_ACTION_SEQUENCE` | DOUBLE |  |  | the Org action sequence |
| 59 | `PBS_DISPENSING_INCENTIVE_AMT` | DOUBLE | NOT NULL |  | Dispensing incentive amount paid by PBS. |
| 60 | `PBS_DRUG_UUID` | VARCHAR(255) |  |  | The unique identifier for the drug that appears in the PBS_DRUG table. |
| 61 | `PBS_ELECTRONIC_RX_FEE_AMT` | DOUBLE | NOT NULL |  | The fee paid for electronic prescriptions by PBS. |
| 62 | `PBS_ITEM_CODE` | VARCHAR(10) |  |  | The PBS item code for the drug that appears in the PBS_LISTING table. |
| 63 | `PBS_ONLINE_INCENTIVE_AMT` | DOUBLE | NOT NULL |  | Amount paid by PBS for online incentives. |
| 64 | `PBS_PRF_AMT` | DOUBLE | NOT NULL |  | Amount recorded on the Prescription Record Form for PBS dispenses. Fee paid by patients when they charge a prescription. |
| 65 | `PF_DISPENSE_HX_ID` | DOUBLE | NOT NULL | FK→ | the pf dispense hx id |
| 66 | `PF_REASON_CD` | DOUBLE | NOT NULL |  | the pf reason cd |
| 67 | `PHARM_TYPE_CD` | DOUBLE | NOT NULL |  | Pharmacy Type associated with the Dispense transaction |
| 68 | `PREV_DISPENSE_DT_TM` | DATETIME |  |  | Date and time of previous dose |
| 69 | `PREV_DISPENSE_TZ` | DOUBLE |  |  | Time zone associated with the corresponding DT_TM column. |
| 70 | `QTY_REMAINING` | DOUBLE |  |  | the quantity remaining |
| 71 | `REASON_CD` | DOUBLE | NOT NULL |  | Identifier for cause of associated event type. |
| 72 | `REBILL_DISPENSE_HX_ID` | DOUBLE | NOT NULL | FK→ | Stores the dispense_hx_id of the originally billed order. |
| 73 | `REBILL_FLAG` | DOUBLE | NOT NULL |  | Stores the type of rebill action. |
| 74 | `REFILLS_REMAINING` | DOUBLE |  |  | number of refills remaining |
| 75 | `REFR_DISPENSE_HX_ID` | DOUBLE | NOT NULL | FK→ | This field will be populated with a dispense_hx_id that refers to a previous dispense associated to the original order. |
| 76 | `REIMBURSEMENT` | DOUBLE |  |  | Reimbursement Amount for this dispense transaction |
| 77 | `RESIDUAL_COPAY_AMT` | DOUBLE |  |  | Copay for the residual dispense quantity. |
| 78 | `RESIDUAL_COST_AMT` | DOUBLE |  |  | Total cost for the Residual Dispense Quantity. |
| 79 | `RESIDUAL_DISCOUNT_AMT` | DOUBLE |  |  | Discount amount for the residual dispense quantity. |
| 80 | `RESIDUAL_DISPENSE_FEE_AMT` | DOUBLE |  |  | Dispense fee for the residual dispense quantity. |
| 81 | `RESIDUAL_DISP_QTY` | DOUBLE |  |  | Amount of quantity that needs to be charged, after reversing the original charge, as a result of Cancel Owe event. |
| 82 | `RESIDUAL_DOSES` | DOUBLE | NOT NULL |  | The number of doses needing to be charged after the reverse transaction was placed. |
| 83 | `RESIDUAL_INCENTIVE_FEE_AMT` | DOUBLE |  |  | Incentive fee for the residual dispense quantity. |
| 84 | `RESIDUAL_PRICE` | DOUBLE | NOT NULL |  | The price needing to be charged after the reverse transaction was placed. |
| 85 | `RESIDUAL_REIMBURSEMENT_AMT` | DOUBLE |  |  | Reimbursement for the residual dispense quantity. |
| 86 | `RESIDUAL_SALES_TAX_AMT` | DOUBLE |  |  | Sales tax for the residual dispense quantity. |
| 87 | `RESIDUAL_UC_PRICE` | DOUBLE |  |  | Usual and Customary price for the residual dispense quantity. |
| 88 | `REVERSE_IND` | DOUBLE | NOT NULL |  | Indicates whether or not a reverse has been performed on the dispense. |
| 89 | `REV_DISPENSE_HX_ID` | DOUBLE | NOT NULL | FK→ | The Dispense History ID that was reversed to allow for the credit transaction to be successful. |
| 90 | `RUN_USER_ID` | DOUBLE | NOT NULL | FK→ | ID of the user generating the dispense event |
| 91 | `RXA_ORDERING_UNIT_CD` | DOUBLE | NOT NULL |  | The unit of the ordering quantity for the dispense. |
| 92 | `SALES_TAX` | DOUBLE |  |  | sales tax amount |
| 93 | `SKIPPED_SCHEDULE_SEQ` | DOUBLE | NOT NULL |  | The schedule sequence of a skipped dose. |
| 94 | `SPLIT_CONTAINER_FLAG` | DOUBLE |  |  | Indicates whether the dispense event was associated to a split container dispense. |
| 95 | `SUPPRESS_CHARGE_FLAG` | DOUBLE |  |  | Indicates whether the charges have been suppressed for the inpatient dispense |
| 96 | `SYSTEM_GENERATED_IND` | DOUBLE |  |  | Indicates the dispense event was generated by the system. |
| 97 | `TRACK_NBR` | DOUBLE |  |  | Tracking number of dispense transaction |
| 98 | `TRACK_NBR_CD` | DOUBLE | NOT NULL |  | the Tracking Number Prefix Code |
| 99 | `TRANSFER_TO_LOC_CD` | DOUBLE | NOT NULL |  | Location code where stock is transferred to. |
| 100 | `UC_PRICE` | DOUBLE |  |  | the Usual and Customary Price |
| 101 | `UNIQUE_SCHEDULE_SEQ_NBR` | DOUBLE | NOT NULL |  | The number of unique schedule sequences dispensed for this dispense event. |
| 102 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 103 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 104 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 105 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 106 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 107 | `WASTE_DISPENSE_HX_ID` | DOUBLE |  | FK→ | Identifier for the parent dispense event which this waste or waste offset was applied to. |
| 108 | `WASTE_FLAG` | DOUBLE |  |  | Indicates this dispense event can have waste applied. |
| 109 | `WITNS_PRSNL_ID` | DOUBLE | NOT NULL | FK→ | Identifier for witness overseeing dispense event |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `CHRG_DISPENSE_HX_ID` | [DISPENSE_HX](DISPENSE_HX.md) | `DISPENSE_HX_ID` |
| `CONTRIBUTOR_SYSTEM_CD` | [CONTRIBUTOR_SYSTEM](CONTRIBUTOR_SYSTEM.md) | `CONTRIBUTOR_SYSTEM_CD` |
| `CRDT_DISPENSE_HX_ID` | [DISPENSE_HX](DISPENSE_HX.md) | `DISPENSE_HX_ID` |
| `DISPENSE_PRSNL_ID` | [PRSNL](PRSNL.md) | `PERSON_ID` |
| `DISP_LOC_CD` | [LOCATION](LOCATION.md) | `LOCATION_CD` |
| `FILL_HX_ID` | [FILL_BATCH_HX](FILL_BATCH_HX.md) | `FILL_HX_ID` |
| `GROUPER_DISPENSE_HX_ID` | [DISPENSE_HX](DISPENSE_HX.md) | `DISPENSE_HX_ID` |
| `HEALTH_PLAN_ID` | [HEALTH_PLAN](HEALTH_PLAN.md) | `HEALTH_PLAN_ID` |
| `OFFSET_DISPENSE_HX_ID` | [DISPENSE_HX](DISPENSE_HX.md) | `DISPENSE_HX_ID` |
| `ORDER_ID` | [ORDERS](ORDERS.md) | `ORDER_ID` |
| `PF_DISPENSE_HX_ID` | [DISPENSE_HX](DISPENSE_HX.md) | `DISPENSE_HX_ID` |
| `REBILL_DISPENSE_HX_ID` | [DISPENSE_HX](DISPENSE_HX.md) | `DISPENSE_HX_ID` |
| `REFR_DISPENSE_HX_ID` | [DISPENSE_HX](DISPENSE_HX.md) | `DISPENSE_HX_ID` |
| `REV_DISPENSE_HX_ID` | [DISPENSE_HX](DISPENSE_HX.md) | `DISPENSE_HX_ID` |
| `RUN_USER_ID` | [PRSNL](PRSNL.md) | `PERSON_ID` |
| `WASTE_DISPENSE_HX_ID` | [DISPENSE_HX](DISPENSE_HX.md) | `DISPENSE_HX_ID` |
| `WITNS_PRSNL_ID` | [PRSNL](PRSNL.md) | `PERSON_ID` |

## Referenced by (44)

| From table | Column |
|------------|--------|
| [CE_MED_ADMIN_IDENT](CE_MED_ADMIN_IDENT.md) | `DISPENSE_HX_ID` |
| [DISPENSE_DETAIL](DISPENSE_DETAIL.md) | `DISPENSE_HX_ID` |
| [DISPENSE_HX](DISPENSE_HX.md) | `CHRG_DISPENSE_HX_ID` |
| [DISPENSE_HX](DISPENSE_HX.md) | `CRDT_DISPENSE_HX_ID` |
| [DISPENSE_HX](DISPENSE_HX.md) | `GROUPER_DISPENSE_HX_ID` |
| [DISPENSE_HX](DISPENSE_HX.md) | `OFFSET_DISPENSE_HX_ID` |
| [DISPENSE_HX](DISPENSE_HX.md) | `PF_DISPENSE_HX_ID` |
| [DISPENSE_HX](DISPENSE_HX.md) | `REBILL_DISPENSE_HX_ID` |
| [DISPENSE_HX](DISPENSE_HX.md) | `REFR_DISPENSE_HX_ID` |
| [DISPENSE_HX](DISPENSE_HX.md) | `REV_DISPENSE_HX_ID` |
| [DISPENSE_HX](DISPENSE_HX.md) | `WASTE_DISPENSE_HX_ID` |
| [DISPENSE_HX_ALIAS](DISPENSE_HX_ALIAS.md) | `DISPENSE_HX_ID` |
| [DISPENSE_REPLACE](DISPENSE_REPLACE.md) | `INIT_DISPENSE_HX_ID` |
| [DISPENSE_REPLACE](DISPENSE_REPLACE.md) | `ORIG_DISPENSE_HX_ID` |
| [DISPENSE_REPLACE](DISPENSE_REPLACE.md) | `REPLACE_DISPENSE_HX_ID` |
| [DISPENSE_REPLACE_AUDIT](DISPENSE_REPLACE_AUDIT.md) | `INIT_DISPENSE_HX_ID` |
| [DISPENSE_STATUS](DISPENSE_STATUS.md) | `DISPENSE_HX_ID` |
| [DISPENSE_STATUS_ERR](DISPENSE_STATUS_ERR.md) | `DISPENSE_HX_ID` |
| [DISPENSE_STATUS_HX](DISPENSE_STATUS_HX.md) | `DISPENSE_HX_ID` |
| [FILL_PRINT_ORD_HX](FILL_PRINT_ORD_HX.md) | `DISPENSE_ID` |
| [ORDER_DISPENSE](ORDER_DISPENSE.md) | `LAST_FILL_DISPENSE_HX_ID` |
| [ORDER_DISPENSE](ORDER_DISPENSE.md) | `LAST_RX_DISPENSE_HX_ID` |
| [PHA_BATCH_REPORT_ACT_DTL](PHA_BATCH_REPORT_ACT_DTL.md) | `DISPENSE_HX_ID` |
| [PHA_DISP_OBS_ST](PHA_DISP_OBS_ST.md) | `DISPENSE_HX_ID` |
| [PHA_PROD_DISP_OBS_ST](PHA_PROD_DISP_OBS_ST.md) | `DISPENSE_HX_ID` |
| [PROD_DISPENSE_HX](PROD_DISPENSE_HX.md) | `DISPENSE_HX_ID` |
| [RXA_ORD_DISP_HP_OBS_ST](RXA_ORD_DISP_HP_OBS_ST.md) | `DISPENSE_HX_ID` |
| [RXA_SUSPEND_ACT_LOG](RXA_SUSPEND_ACT_LOG.md) | `DISPENSE_HX_ID` |
| [RXA_WORK_LOAD_OBS_ST](RXA_WORK_LOAD_OBS_ST.md) | `DISPENSE_HX_ID` |
| [RXS_ACTIVITY_INDEX](RXS_ACTIVITY_INDEX.md) | `DISPENSE_HX_ID` |
| [RXS_ALERT](RXS_ALERT.md) | `DISPENSE_HX_ID` |
| [RX_ADMIN_DISPENSE_HX](RX_ADMIN_DISPENSE_HX.md) | `DISPENSE_HX_ID` |
| [RX_CLAIM](RX_CLAIM.md) | `DISPENSE_HX_ID` |
| [RX_CLAIM_OVERRIDE](RX_CLAIM_OVERRIDE.md) | `DISPENSE_HX_ID` |
| [RX_CLAIM_PENDING](RX_CLAIM_PENDING.md) | `DISPENSE_HX_ID` |
| [RX_DISPENSE_GENERATOR_AUDIT](RX_DISPENSE_GENERATOR_AUDIT.md) | `INITIATING_DISPENSE_HX_ID` |
| [RX_DISPENSE_ORDERS_RELTN](RX_DISPENSE_ORDERS_RELTN.md) | `DISPENSE_HX_ID` |
| [RX_INPT_CLAIM_HX](RX_INPT_CLAIM_HX.md) | `DISPENSE_HX_ID` |
| [RX_INPT_CLAIM_HX](RX_INPT_CLAIM_HX.md) | `OP_DISPENSE_HX_ID` |
| [RX_PENDING_REFILL](RX_PENDING_REFILL.md) | `DISPENSE_HX_ID` |
| [RX_PERSON_OWE](RX_PERSON_OWE.md) | `DISPENSE_HX_ID` |
| [RX_PERSON_OWE](RX_PERSON_OWE.md) | `RESOLVED_DHX_ID` |
| [RX_REFILL_HX](RX_REFILL_HX.md) | `DISPENSE_HX_ID` |
| [RX_WORKFLOW_STS](RX_WORKFLOW_STS.md) | `DISPENSE_HX_ID` |

