# RXA_SUSPEND_ACT_LOG

> Stores the activities that were taken on suspended orders

**Description:** Outpatient Pharmacy Suspend Activity Log  
**Table type:** ACTIVITY  
**Primary key:** `RXA_SUSPEND_ACT_LOG_ID`  
**Columns:** 15  
**Referenced by:** 4 columns

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ACT_DT_TM` | DATETIME |  |  | The date/time at which each activity log row is recorded/added to the table. |
| 2 | `DISPENSE_HX_ID` | DOUBLE | NOT NULL | FK→ | The dispense row that is pending to be refilled. This can be 0 when the refill action has not been initiated on the order. |
| 3 | `ORDER_ID` | DOUBLE | NOT NULL | FK→ | The order id tied to the fill request. This can be 0. |
| 4 | `ORIG_RXA_SUSPEND_ACT_LOG_ID` | DOUBLE | NOT NULL | FK→ | The unique identifier to the RXA_SUSPEND_ACT_LOG table. Identifies the initial log entry to link together ones that are part of a group. |
| 5 | `RXA_SUSPEND_ACT_LOG_ID` | DOUBLE | NOT NULL | PK | Unique generated number that identifies a single row on the RXA_SUSPEND_ACT_LOG table. |
| 6 | `SUSPEND_ACT_SEQ` | DOUBLE | NOT NULL |  | A number that identifies the sequence of activities performed on a particular suspended refill request. |
| 7 | `SUSPEND_ROUTING_TYPE_CD` | DOUBLE | NOT NULL |  | To store the specified delivery type of the medicine to the patient on the suspended order in queue. Examples: CMOP Certified Mail, Local Regular Mail, Window (in person) |
| 8 | `SUSPEND_STAGE_CD` | DOUBLE | NOT NULL |  | Stores the stage in which the suspended order is in during the suspend order workflow. System will run a qualification at regular intervals to create batch of orders to be sent to CMOP location, from where the medicines will be packaged and delivered through a mailer to patients. During this process, an order will travel through various points until it reaches the patient. These points are called stages. A stage will help in identifying where the order is currently. |
| 9 | `SUSPEND_STATUS_CD` | DOUBLE | NOT NULL |  | To store the status in which each suspend stage is in during the suspend order workflow |
| 10 | `SUSPEND_STATUS_DETAIL_CD` | DOUBLE | NOT NULL |  | The code value (Code set 4636007) representing the status detail of the suspended order within the current stage during the suspend order workflow. This can be 0, when there is no additional detail for the current stage. Ex: Cancel Back, Claim Failure Cancel, Pending Fulfillment |
| 11 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 12 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 13 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 14 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 15 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `DISPENSE_HX_ID` | [DISPENSE_HX](DISPENSE_HX.md) | `DISPENSE_HX_ID` |
| `ORDER_ID` | [ORDERS](ORDERS.md) | `ORDER_ID` |
| `ORIG_RXA_SUSPEND_ACT_LOG_ID` | [RXA_SUSPEND_ACT_LOG](RXA_SUSPEND_ACT_LOG.md) | `RXA_SUSPEND_ACT_LOG_ID` |

## Referenced by (4)

| From table | Column |
|------------|--------|
| [RXA_SUSPEND_ACT_LOG](RXA_SUSPEND_ACT_LOG.md) | `ORIG_RXA_SUSPEND_ACT_LOG_ID` |
| [RXA_SUSPEND_ACT_LOG_DTL](RXA_SUSPEND_ACT_LOG_DTL.md) | `RXA_SUSPEND_ACT_LOG_ID` |
| [RX_PENDING_REFILL](RX_PENDING_REFILL.md) | `RXA_SUSPEND_ACT_LOG_ID` |
| [RX_REFILL_HX](RX_REFILL_HX.md) | `RXA_SUSPEND_ACT_LOG_ID` |

