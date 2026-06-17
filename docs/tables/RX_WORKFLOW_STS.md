# RX_WORKFLOW_STS

> Stores a workflow event that is routed to the pharmacy workflow monitor.

**Description:** Pharmacy Workflow Status  
**Table type:** ACTIVITY  
**Primary key:** `RX_WORKFLOW_STS_ID`  
**Columns:** 24  
**Referenced by:** 6 columns

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `CMPLT_DT_TM` | DATETIME |  |  | Date and time when a sequence was completed. |
| 2 | `CMPLT_TZ` | DOUBLE | NOT NULL |  | Time zone associated to the cmplt_dt_tm that records when the sequence was completed. |
| 3 | `CREATED_DT_TM` | DATETIME |  |  | Date and time the record was created. |
| 4 | `CREATED_TZ` | DOUBLE | NOT NULL |  | Time zone associated with the created_dt_tm column. |
| 5 | `DISPENSE_CATEGORY_S` | VARCHAR(40) | NOT NULL |  | The display value of the dispense category cd from 4008 that is associated to an event. |
| 6 | `DISPENSE_FROM_LOC_CD` | DOUBLE | NOT NULL |  | The location a dispense event of an order is to be dispensed from. |
| 7 | `DISPENSE_HX_ID` | DOUBLE | NOT NULL | FK→ | This field links the rx_workflow_sts record to the dispensing event record. This will enable users to track back to the original dispense. |
| 8 | `EVENT_NBR_DAY_SEQ` | DOUBLE | NOT NULL |  | An incrementing number of occurrences during a particular day. |
| 9 | `ITEM_ID` | DOUBLE | NOT NULL | FK→ | This column represents the item in the medication_definition table. |
| 10 | `PHARM_TYPE_CD` | DOUBLE | NOT NULL |  | Pharmacy type code that indicates if the event is Inpatient or Retail. |
| 11 | `PREP_INFO_CD` | DOUBLE | NOT NULL |  | Code value from code set 4760 that represents the worksheet associated to a workflow event. |
| 12 | `RX_WORKFLOW_STS_ID` | DOUBLE | NOT NULL | PK | Unique, generated key for each workflow_sts row. |
| 13 | `SCHED_DT_TM` | DATETIME |  |  | Date and time of the first admin a workflow event is to occur. |
| 14 | `SCHED_TZ` | DOUBLE | NOT NULL |  | Time zone associated with sched_dt_tm. |
| 15 | `STS_FLAG` | DOUBLE | NOT NULL |  | Indicates if the sequence is no longer active (0), active (1), or completed (2). |
| 16 | `TOTAL_DOSE_NBR` | DOUBLE | NOT NULL |  | Amount requested to be made for an event. |
| 17 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 18 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 19 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 20 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 21 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |
| 22 | `UPDT_TZ` | DOUBLE | NOT NULL |  | Time zone associated with field updt_dt_tm. |
| 23 | `WORKFLOW_CD` | DOUBLE | NOT NULL |  | Indicates the workflow sequence of an order. Used to route orders to workflow monitor. |
| 24 | `WORKFLOW_STS_CD` | DOUBLE | NOT NULL |  | Indicates the status of the workflow sequence associated to an order's dispense. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `DISPENSE_HX_ID` | [DISPENSE_HX](DISPENSE_HX.md) | `DISPENSE_HX_ID` |
| `ITEM_ID` | [MEDICATION_DEFINITION](MEDICATION_DEFINITION.md) | `ITEM_ID` |

## Referenced by (6)

| From table | Column |
|------------|--------|
| [RXS_ITEM_COUNTBACK](RXS_ITEM_COUNTBACK.md) | `RX_WORKFLOW_STS_ID` |
| [RX_PROD_VLDTN_EVENT](RX_PROD_VLDTN_EVENT.md) | `RX_WORKFLOW_STS_ID` |
| [RX_WF_WS](RX_WF_WS.md) | `RX_WORKFLOW_STS_ID` |
| [RX_WORKFLOW_STS_HX](RX_WORKFLOW_STS_HX.md) | `RX_WORKFLOW_STS_ID` |
| [RX_WORKFLOW_STS_ITEM](RX_WORKFLOW_STS_ITEM.md) | `RX_WORKFLOW_STS_ID` |
| [RX_WORKFLOW_STS_SCHED](RX_WORKFLOW_STS_SCHED.md) | `RX_WORKFLOW_STS_ID` |

