# ORDER_DISPENSE

> Store a record of dispensing for each pharmacy order dispensed

**Description:** order_dispense  
**Table type:** ACTIVITY  
**Primary key:** _(not published — see note)_  
**Columns:** 103

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `AUTO_CREDIT_IND` | DOUBLE | NOT NULL |  | Used to determine if auto crediting should be performed on this order when the order gets end-stated. |
| 2 | `CART_FILL1_TZ` | DOUBLE |  |  | Time zone associated with the corresponding DT_TM column. |
| 3 | `CART_FILL2_TZ` | DOUBLE |  |  | Time zone associated with the corresponding DT_TM column. |
| 4 | `CART_FILL3_TZ` | DOUBLE |  |  | Time zone associated with the corresponding DT_TM column. |
| 5 | `CART_FILL_DOSES1` | DOUBLE |  |  | This is the number of doses calculated to fill from the last batch fill that was ran. |
| 6 | `CART_FILL_DOSES2` | DOUBLE |  |  | This is the number of doses calculated to fill from the last batch fill that was ran. |
| 7 | `CART_FILL_DOSES3` | DOUBLE |  |  | This is the number of doses calculated to fill from the last batch fill that was ran. |
| 8 | `CART_FILL_DT_TM1` | DATETIME |  |  | The from cycle date time specified by the fill batch from which this order qualified. |
| 9 | `CART_FILL_DT_TM2` | DATETIME |  |  | The from cycle date time specified by the fill batch from which this order qualified. |
| 10 | `CART_FILL_DT_TM3` | DATETIME |  |  | The from cycle date time specified by the fill batch from which this order qualified. |
| 11 | `CART_FILL_RUN_ID1` | DOUBLE |  |  | The run_id assigned to this fill batch run. The run_id will be on the fill_print_hx table. |
| 12 | `CART_FILL_RUN_ID2` | DOUBLE |  |  | The run_id assigned to this fill batch run. The run_id will be on the fill_print_hx table. |
| 13 | `CART_FILL_RUN_ID3` | DOUBLE |  |  | The run_id assigned to this fill batch run. The run_id will be on the fill_print_hx table. |
| 14 | `CLAIM_FLAG` | DOUBLE |  |  | Is there a claim on this order?0 - No claim; 1 - Claim |
| 15 | `COB_IND` | DOUBLE |  |  | Indicates if Coordination of benefits was used during the claim submission. |
| 16 | `DAW_CD` | DOUBLE | NOT NULL |  | dispense as written code |
| 17 | `DAYS_SUPPLY` | DOUBLE |  |  | Number of days the order will supply. |
| 18 | `DEPT_STATUS_CD` | DOUBLE | NOT NULL |  | Order status - department level |
| 19 | `DISPENSE_CATEGORY_CD` | DOUBLE | NOT NULL |  | Code value for the dispense category of the order |
| 20 | `DISPLAY_LINE` | VARCHAR(255) |  |  | order detail display line, similar to order sentence. |
| 21 | `ENCNTR_ID` | DOUBLE | NOT NULL | FK→ | encounter identifier value |
| 22 | `ERX_MSG_LONG_TEXT_ID` | DOUBLE |  | FK→ | long_text_id associated to the electronic prescription message on the long_text table |
| 23 | `EXPIRE_DT_TM` | DATETIME |  |  | expire date and time value |
| 24 | `EXPIRE_TZ` | DOUBLE |  |  | Time zone associated with the corresponding DT_TM column. |
| 25 | `FILL_NBR` | DOUBLE |  |  | Contains the fill number for this order. |
| 26 | `FLOORSTOCK_IND` | DOUBLE |  |  | Indicates whether this order is dispensed from floorstock |
| 27 | `FLOORSTOCK_OVERRIDE_IND` | DOUBLE |  |  | The floorstock override indicator overrides the number inventory dispensing logic and instructs the fill process not to fill the order from the Pharmacy inventory but from the floorstock (nursing station). |
| 28 | `FREQUENCY_ID` | DOUBLE | NOT NULL | FK→ | The frequency id is used to find the frequency_schedule information which specifies the interval at which the order should be dispensed. |
| 29 | `FUTURE_LOC_FACILITY_CD` | DOUBLE | NOT NULL | FK→ | Estimated facility for an order in a future status. Field value reverts to zero once the order is no longer a future order. |
| 30 | `FUTURE_LOC_NURSE_UNIT_CD` | DOUBLE | NOT NULL | FK→ | Estimated nurse unit location for an order in a future status. Field value reverts to zero once the order is no longer a future order. |
| 31 | `HEALTH_PLAN_ID` | DOUBLE | NOT NULL | FK→ | Contains the health plan related to this order. |
| 32 | `IGNORE_IND` | DOUBLE |  |  | The Ignore Indicator is used to temporarily mark an order not to qualify for a fill list. 1 = ignore (skip fill), 0 = fill as instructed. |
| 33 | `IV_SET_SIZE` | DOUBLE |  |  | The IV Set Size is denormalized from the order_details and specifies the number of IV bags that are in a set. |
| 34 | `LAST_CLIN_REVIEW_ACT_SEQ` | DOUBLE | NOT NULL |  | Sequence corresponding to the action sequence of the last action clinically reviewed. |
| 35 | `LAST_CLIN_REVIEW_INGR_SEQ` | DOUBLE | NOT NULL |  | Sequence corresponding to the action sequence of the last existing set of ingredients clinically reviewed. |
| 36 | `LAST_FILL_ACT_SEQ` | DOUBLE |  |  | Last action sequence for fill list |
| 37 | `LAST_FILL_DISPENSE_HX_ID` | DOUBLE | NOT NULL | FK→ | Contains the dispense ID for the last fill run on this order. (Related to (Inpatient) workflow). Identifies a dispense of a single order or dose on the dispense hx table. |
| 38 | `LAST_FILL_HX_ID` | DOUBLE | NOT NULL | FK→ | Identifies the id for the last batch or fill run on this order. |
| 39 | `LAST_FILL_INGR_SEQ` | DOUBLE |  |  | Contains the last ingredient sequence to be filled |
| 40 | `LAST_FILL_STATUS` | DOUBLE |  |  | Order status when the last fill was run. |
| 41 | `LAST_PBS_DRUG_UUID` | VARCHAR(255) |  |  | The drug UUID of the item used in the most recent dispense. |
| 42 | `LAST_PBS_ITEM_CODE` | VARCHAR(10) |  |  | The pbs code of the item used in the most recent dispense. |
| 43 | `LAST_REFILL_DT_TM` | DATETIME |  |  | Last refill date and time |
| 44 | `LAST_REFILL_TZ` | DOUBLE |  |  | Time zone associated with the corresponding DT_TM column. |
| 45 | `LAST_RX_DISPENSE_HX_ID` | DOUBLE | NOT NULL | FK→ | Stores the dispense_hx_id of the last fill performed on the order. (Related to PharmNet Ambulatory (Retail) flow) |
| 46 | `LAST_VER_ACT_SEQ` | DOUBLE |  |  | Last verified action sequence |
| 47 | `LAST_VER_INGR_SEQ` | DOUBLE |  |  | Last verified ingredient sequence |
| 48 | `LEGAL_STATUS_CD` | DOUBLE | NOT NULL |  | Legal Status Code |
| 49 | `NEED_RX_PROD_ASSIGN_FLAG` | DOUBLE | NOT NULL |  | Flag for identifying whether the order's product assignment has been completed or not. |
| 50 | `NEED_RX_VERIFY_IND` | DOUBLE |  |  | Indicator on whether Pharmacy needs to verify this order. (from Orders table) |
| 51 | `NEXT_DISPENSE_DT_TM` | DATETIME |  |  | Time stamp for when next dose is to be dispensed |
| 52 | `NEXT_DISPENSE_TZ` | DOUBLE |  |  | Time zone associated with the corresponding DT_TM column. For inpatient rows, this is the time zone of the encounter. For Retail Pharmacy, it is the time zone of the pharmacy's facility. |
| 53 | `NEXT_IV_SEQ` | DOUBLE |  |  | Next IV sequence to be dispensed |
| 54 | `ORDER_COST_VALUE` | DOUBLE |  |  | The order cost is denormalized from the order_details and represents the define cost of the order. |
| 55 | `ORDER_DISPENSE_IND` | DOUBLE |  |  | Indicates if this order is dispensable (1) or not (0). |
| 56 | `ORDER_ID` | DOUBLE | NOT NULL | FK→ | The unique identifier for the order |
| 57 | `ORDER_PRICE_VALUE` | DOUBLE |  |  | The order price is denormalized from the order_details and generally represents the price for each doses that will be charged. |
| 58 | `ORDER_TYPE` | DOUBLE |  |  | Order type indicates whether the order is med, continuous, or intermittent. |
| 59 | `OWE_QTY` | DOUBLE |  |  | Contains the latest quantity (of medication) owed to the patient on a fill. |
| 60 | `PARENT_ORDER_ID` | DOUBLE | NOT NULL |  | This field contains the Order_ID of the prescription placed in Easy Script that was used to create the current order. |
| 61 | `PAR_DOSES` | DOUBLE |  |  | PAR doses is denormalized from the order_details and specifies the number of doses on average that should be dispensed for a 24 hour period. |
| 62 | `PATIENT_MED_IND` | DOUBLE | NOT NULL |  | Indicates whether the order is a patient's own med. |
| 63 | `PERSON_ID` | DOUBLE | NOT NULL | FK→ | Person ID |
| 64 | `PHARM_TYPE_CD` | DOUBLE | NOT NULL |  | Pharmacy type code of the order (e.g. Inpatient, Ambulatory, etc.) |
| 65 | `PRICE_CODE_CD` | DOUBLE | NOT NULL |  | Contains the price code detail from order details. |
| 66 | `PRICE_SCHEDULE_ID` | DOUBLE | NOT NULL | FK→ | The price schedule id is denormalized from the order_detail table and contains information about which price schedule to use for calculating billing. |
| 67 | `PRINT_IND` | DOUBLE |  |  | Indicates whether this order is printable on batch fill output or whether this order can be skipped from being printed. Pharmacy order entry initially sets all orders as "printable" (true) and the fill process may later update the value to "not printable" (false) |
| 68 | `PRN_IND` | DOUBLE |  |  | Indicates if this is a prn order |
| 69 | `PROFILE_DISPLAY_DT_TM` | DATETIME |  |  | Display date and time |
| 70 | `QTY_REMAINING` | DOUBLE |  |  | Contains the remaining quantity of the order. |
| 71 | `REFILLS_REMAINING` | DOUBLE |  |  | Remaining refills for this order. |
| 72 | `REPLACE_EVERY` | DOUBLE |  |  | Replace Every is a numeric value representing the time interval at which the order should be replaced (dosed). The units associated with the replace_every value are contain in the replace_every_unit_cd column. |
| 73 | `REPLACE_EVERY_CD` | DOUBLE | NOT NULL |  | Replace Every Code Value determines the units the replace_every column is representing. i.e. Minutes, Hours, Days, Weeks. |
| 74 | `RESEARCH_ACCOUNT_ID` | DOUBLE | NOT NULL | FK→ | The research account that the order will be billed against. |
| 75 | `RESUME_DT_TM` | DATETIME |  |  | Date and time the order was resumed. |
| 76 | `RESUME_TZ` | DOUBLE |  |  | Time zone associated with the corresponding DT_TM column. |
| 77 | `REVIEWED_PARENT_ACTION_SEQ` | DOUBLE | NOT NULL |  | This field contains the action sequence of the parent order that was reviewed by the user that performed the latest fill on the current order. |
| 78 | `RXA_ERX_MULTICHILD_IND` | DOUBLE | NOT NULL |  | indicates whether the child Retail order is a part of multiple child orders or regular order. |
| 79 | `RXA_PRESCRIPTION_MSG_ID` | DOUBLE |  | FK→ | The unique identifier for the electronic prescription message associated to the external prescription |
| 80 | `RXA_SIG_OVERRIDE_IND` | DOUBLE | NOT NULL |  | Indicates whether user has manually overridden the Sig that was automatically expanded by the system based on Sig codes. |
| 81 | `RX_NBR` | DOUBLE |  |  | prescription number, generated by calling a script that increments the next_num column, for appropriate range, in pharmacy_range table |
| 82 | `RX_NBR_CD` | DOUBLE | NOT NULL |  | Prescription number code |
| 83 | `SOURCE_PARENT_ACTION_SEQ` | DOUBLE | NOT NULL |  | This field contains the action sequence of the parent order that was used as the source to create the current order. |
| 84 | `START_DISPENSE_DT_TM` | DATETIME |  |  | Date and time the order will start dispensing. |
| 85 | `START_DISPENSE_TZ` | DOUBLE | NOT NULL |  | Time zone associated with the corresponding start_dispense_dt_tm field. |
| 86 | `STOP_DT_TM` | DATETIME |  |  | Date and time the order was discontinued |
| 87 | `STOP_TYPE_CD` | DOUBLE | NOT NULL |  | Stop type code, indicates whether stop was hard, soft, etc. |
| 88 | `STOP_TZ` | DOUBLE |  |  | Time zone associated with the corresponding DT_TM column. |
| 89 | `SUSPEND_DT_TM` | DATETIME |  |  | Date and time the order was suspended. |
| 90 | `SUSPEND_TZ` | DOUBLE |  |  | Time zone associated with the corresponding DT_TM column. |
| 91 | `TOTAL_DISPENSE_DOSES` | DOUBLE |  |  | Cumulative counter for number of doses dispensed (administrations) |
| 92 | `TOTAL_RX_QTY` | DOUBLE |  |  | Quantity total from order details. |
| 93 | `TRANSFER_CNT` | DOUBLE |  |  | transfer count |
| 94 | `UNVERIFIED_ACTION_TYPE_CD` | DOUBLE | NOT NULL |  | Identifies the action that was performed. (from order_action) |
| 95 | `UNVERIFIED_COMM_TYPE_CD` | DOUBLE | NOT NULL |  | Identifies the communication type of the order. (from order_action) |
| 96 | `UNVERIFIED_ROUTE_CD` | DOUBLE | NOT NULL |  | Identifies the route of administration on a medication order (from order_detail table) |
| 97 | `UNVERIFIED_RX_ORD_PRIORITY_CD` | DOUBLE | NOT NULL |  | Identifies the pharmacy order priority. (from order_detail table) |
| 98 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 99 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 100 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 101 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 102 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 103 | `WORKFLOW_CD` | DOUBLE | NOT NULL |  | Indicates the workflow sequence of an order. Used to route orders to workflow monitor. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `ENCNTR_ID` | [ENCOUNTER](ENCOUNTER.md) | `ENCNTR_ID` |
| `ERX_MSG_LONG_TEXT_ID` | [LONG_TEXT](LONG_TEXT.md) | `LONG_TEXT_ID` |
| `FREQUENCY_ID` | [FREQUENCY_SCHEDULE](FREQUENCY_SCHEDULE.md) | `FREQUENCY_ID` |
| `FUTURE_LOC_FACILITY_CD` | [CODE_VALUE](CODE_VALUE.md) | `CODE_VALUE` |
| `FUTURE_LOC_NURSE_UNIT_CD` | [CODE_VALUE](CODE_VALUE.md) | `CODE_VALUE` |
| `HEALTH_PLAN_ID` | [HEALTH_PLAN](HEALTH_PLAN.md) | `HEALTH_PLAN_ID` |
| `LAST_FILL_DISPENSE_HX_ID` | [DISPENSE_HX](DISPENSE_HX.md) | `DISPENSE_HX_ID` |
| `LAST_FILL_HX_ID` | [FILL_BATCH_HX](FILL_BATCH_HX.md) | `FILL_HX_ID` |
| `LAST_RX_DISPENSE_HX_ID` | [DISPENSE_HX](DISPENSE_HX.md) | `DISPENSE_HX_ID` |
| `ORDER_ID` | [ORDERS](ORDERS.md) | `ORDER_ID` |
| `PERSON_ID` | [PERSON](PERSON.md) | `PERSON_ID` |
| `PRICE_SCHEDULE_ID` | [PRICE_SCHED](PRICE_SCHED.md) | `PRICE_SCHED_ID` |
| `RESEARCH_ACCOUNT_ID` | [RESEARCH_ACCOUNT](RESEARCH_ACCOUNT.md) | `RESEARCH_ACCOUNT_ID` |
| `RXA_PRESCRIPTION_MSG_ID` | [RXA_PRESCRIPTION_MSG](RXA_PRESCRIPTION_MSG.md) | `RXA_PRESCRIPTION_MSG_ID` |

