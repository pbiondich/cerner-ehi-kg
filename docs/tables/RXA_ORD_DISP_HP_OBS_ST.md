# RXA_ORD_DISP_HP_OBS_ST

> This table will store adjudicated health plan nformation per action and per dispense.

**Description:** RXA_ORD_DISP_HP_OBS_ST (summary table)  
**Table type:** ACTIVITY  
**Primary key:** _(not published — see note)_  
**Columns:** 27

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ACTION_SEQ` | DOUBLE | NOT NULL |  | Action_Sequence from order_action table |
| 2 | `DISPENSE_HX_ID` | DOUBLE | NOT NULL | FK→ | Dispense_hx_id from Dispense_hx table |
| 3 | `DISP_FROM_SR_CD` | DOUBLE | NOT NULL | FK→ | Service_Resource_Cd from Service_Resource table |
| 4 | `ORDER_ID` | DOUBLE | NOT NULL | FK→ | Order_id from orders table |
| 5 | `ORD_DISP_HP_ID` | DOUBLE | NOT NULL |  | Unique number per Row. NOTE: Will use sequence PHA_RANGE_SEQ. |
| 6 | `RXA_AUTH_NBR_TXT` | VARCHAR(250) | NOT NULL |  | Authorization number received from health plan |
| 7 | `RXA_CLAIM_FLAG` | DOUBLE | NOT NULL |  | Indicates whether the current fill has been claimed -1,"None",0,"Non-Adjudicated",1,"Adjudicated" |
| 8 | `RXA_CLAIM_ID` | DOUBLE | NOT NULL | FK→ | Rx_claim_id from rx_claim table |
| 9 | `RXA_CLAIM_STATUS_CD` | DOUBLE | NOT NULL |  | Indicates the status of the claim transaction for current health plan |
| 10 | `RXA_COPAY_AMT` | DOUBLE | NOT NULL |  | Copay amount specified by the health plan |
| 11 | `RXA_DUR_IND` | DOUBLE | NOT NULL |  | Indicates whether health plan performed drug utilization review |
| 12 | `RXA_HEALTH_PLAN_ID` | DOUBLE | NOT NULL | FK→ | The health plan used for this prescription |
| 13 | `RXA_HEALTH_PLAN_SEQ` | DOUBLE | NOT NULL |  | The sequence of the health plan in the list of health plans used for this prescription |
| 14 | `RXA_LEVEL5_CD` | DOUBLE | NOT NULL |  | The work station that requested the event |
| 15 | `RXA_MANUAL_OVERRIDE_IND` | DOUBLE | NOT NULL |  | indicates whether user manually overrode the claim status or not. 0 - no manual override 1 - manual override |
| 16 | `RXA_PF_TYPE_CD` | DOUBLE | NOT NULL |  | Indicates if a health plan supports NCPDP 51 partial fill submission process. |
| 17 | `RXA_PRIOR_AUTH_NBR_TXT` | VARCHAR(250) | NOT NULL |  | health plan's prior authorization number |
| 18 | `RXA_PRIOR_AUTH_TYPE_CD` | DOUBLE | NOT NULL |  | health plan's prior authorization type code |
| 19 | `RXA_REIMB_AMT` | DOUBLE | NOT NULL |  | Reimbursement amount received from health plan |
| 20 | `RXA_SWITCH_CD` | DOUBLE | NOT NULL |  | Switch used for Claim submission |
| 21 | `RXA_TRANS_DT_TM` | DATETIME |  |  | Transaction Date/Time for the claim |
| 22 | `RXA_TRANS_DT_TZ` | DOUBLE | NOT NULL |  | Transaction time zone for the claim |
| 23 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 24 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 25 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 26 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 27 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `DISPENSE_HX_ID` | [DISPENSE_HX](DISPENSE_HX.md) | `DISPENSE_HX_ID` |
| `DISP_FROM_SR_CD` | [SERVICE_RESOURCE](SERVICE_RESOURCE.md) | `SERVICE_RESOURCE_CD` |
| `ORDER_ID` | [ORDERS](ORDERS.md) | `ORDER_ID` |
| `RXA_CLAIM_ID` | [RX_CLAIM](RX_CLAIM.md) | `RX_CLAIM_ID` |
| `RXA_HEALTH_PLAN_ID` | [HEALTH_PLAN](HEALTH_PLAN.md) | `HEALTH_PLAN_ID` |

