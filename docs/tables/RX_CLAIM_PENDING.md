# RX_CLAIM_PENDING

> Claim transactions waiting to be picked up by the claim server.

**Description:** RX Claim Pending  
**Table type:** ACTIVITY  
**Primary key:** _(not published — see note)_  
**Columns:** 24

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ACTION_SEQUENCE_NBR` | DOUBLE | NOT NULL | FK→ | The action sequence taken from the order action table. |
| 2 | `CARD_HOLDER_IDENT` | VARCHAR(100) | NOT NULL | FK→ | The member number of the subscriber to the health plan. |
| 3 | `CLAIM_FORMAT_CD` | DOUBLE | NOT NULL |  | Format used in building the Message string, containing the claims information that is sent in the transaction. |
| 4 | `CLAIM_FORMAT_TYPE_CD` | DOUBLE | NOT NULL |  | This field contains the type of claim format that is used to submit the claim. |
| 5 | `CLAIM_PENDING_ID` | DOUBLE | NOT NULL |  | This field uniquely identifies this pending claim. |
| 6 | `CLAIM_TRANS_CD` | DOUBLE | NOT NULL |  | Type of claim transaction. |
| 7 | `COPAY_AMT` | DOUBLE | NOT NULL |  | This field contains the amount of co-pay that comes out of patient's pocket. |
| 8 | `DISPENSE_HX_ID` | DOUBLE | NOT NULL | FK→ | Dispense_hx_id from Dispense_hx table. |
| 9 | `DISP_EVENT_TYPE_CD` | DOUBLE | NOT NULL |  | Type of dispense that generated the claim. |
| 10 | `FILL_NBR` | DOUBLE | NOT NULL |  | This field contains the fill number for the current transaction. |
| 11 | `HEALTH_PLAN_ID` | DOUBLE | NOT NULL | FK→ | This field contains a unique reference back to the RX_HEALTH_PLAN table. |
| 12 | `LEVEL5_CD` | DOUBLE | NOT NULL |  | Location of the Workstation (PC) that was used in filling the prescription. |
| 13 | `ORDER_ID` | DOUBLE | NOT NULL | FK→ | This field contains a unique reference to the ORDERS table. |
| 14 | `PRICE_AMT` | DOUBLE | NOT NULL |  | This field contains the price amount for the current transaction. |
| 15 | `REIMBURSEMENT_AMT` | DOUBLE | NOT NULL |  | The field contains the reimbursement amount for the current transaction. |
| 16 | `SUBSECTION_CD` | DOUBLE | NOT NULL |  | Location of the Pharmacy that filled the prescription. |
| 17 | `SWITCH_CD` | DOUBLE | NOT NULL |  | Switch to which the claim transaction was sent. |
| 18 | `TRANS_DT_TM` | DATETIME |  |  | This field contains the date and time for this transaction. |
| 19 | `TRANS_TZ` | DOUBLE | NOT NULL |  | Time zone for the claim transaction |
| 20 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 21 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 22 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 23 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 24 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `ACTION_SEQUENCE_NBR` | [ORDER_HEALTH_PLAN](ORDER_HEALTH_PLAN.md) | `ACTION_SEQUENCE` |
| `CARD_HOLDER_IDENT` | [ORDER_HEALTH_PLAN](ORDER_HEALTH_PLAN.md) | `CARD_HOLDER_IDENT` |
| `DISPENSE_HX_ID` | [DISPENSE_HX](DISPENSE_HX.md) | `DISPENSE_HX_ID` |
| `HEALTH_PLAN_ID` | [ORDER_HEALTH_PLAN](ORDER_HEALTH_PLAN.md) | `HEALTH_PLAN_ID` |
| `HEALTH_PLAN_ID` | [RX_HEALTH_PLAN](RX_HEALTH_PLAN.md) | `HEALTH_PLAN_ID` |
| `ORDER_ID` | [ORDER_HEALTH_PLAN](ORDER_HEALTH_PLAN.md) | `ORDER_ID` |

