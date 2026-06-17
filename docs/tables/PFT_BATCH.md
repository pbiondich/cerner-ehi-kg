# PFT_BATCH

> PFT Batch table for Prolfit OMF reporting

**Description:** PFT BATCH  
**Table type:** ACTIVITY  
**Primary key:** _(not published — see note)_  
**Columns:** 38

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ACTIVE_IND` | DOUBLE |  |  | The table row is active or inactive. A row is generally active unless it is in an inactive state such as logically deleted, combined away, pending purge, etc. |
| 2 | `ACTIVE_STATUS_CD` | DOUBLE | NOT NULL |  | Indicates the status of the row itself (not the data in the row) such as active, inactive, combined away, pending purge, etc. |
| 3 | `ACTIVE_STATUS_DT_TM` | DATETIME |  |  | The date and time that the active_status_cd was set. |
| 4 | `ACTIVE_STATUS_PRSNL_ID` | DOUBLE | NOT NULL |  | The person who caused the active_status_cd to be set or change. |
| 5 | `ADJ_COMPUTED_TOTAL` | DOUBLE | NOT NULL |  | Actual total number of all of the adjustment transactions. Used as a control number for reconciling. |
| 6 | `ADJ_RESTATED_TOTAL` | DOUBLE | NOT NULL |  | Re-stated total number of all of the adjustment transactions. Used as a control number for reconciling. |
| 7 | `ADJ_STATED_TOTAL` | DOUBLE | NOT NULL |  | Stated total number of all of the adjustment transactions. Used as a control number for reconciling. |
| 8 | `BATCHJOB_IND` | DOUBLE |  |  | Indicates whether a batch job |
| 9 | `BATCH_STATUS_CD` | DOUBLE | NOT NULL |  | Batch status code |
| 10 | `BATCH_TRANS_ID` | DOUBLE | NOT NULL |  | Id to the batch_trans table |
| 11 | `BATCH_TYPE_FLAG` | DOUBLE |  |  | The value indicates which tool has created the batch. |
| 12 | `BEG_EFFECTIVE_DT_TM` | DATETIME |  |  | The date and time for which this table row becomes effective. Normally, this will be the date and time the row is added, but could be a past or future date and time. |
| 13 | `BILLING_ENTITY_ID` | DOUBLE | NOT NULL |  | The id of the billing entity |
| 14 | `BILLING_ENTITY_NAME` | VARCHAR(100) |  |  | The name of the billing entity |
| 15 | `CREATED_DT_TM` | DATETIME |  |  | The date and time when the batch was created |
| 16 | `CREATED_PRSNL_ID` | DOUBLE | NOT NULL |  | The id of the person who created the batch |
| 17 | `CREATED_PRSNL_NAME_FULL` | VARCHAR(100) |  |  | The name of the person who created the batch |
| 18 | `END_EFFECTIVE_DT_TM` | DATETIME |  |  | The date/time after which the row is no longer valid as active current data. This may be valued with the date that the row became inactive. |
| 19 | `EXT_BATCH_ID_TXT` | VARCHAR(40) |  |  | The name of the batch |
| 20 | `FC_COMPUTED_TOTAL` | DOUBLE | NOT NULL |  | Actual total number of all of the finance charge transactions. Used as a control number for reconciling. |
| 21 | `FC_RESTATED_TOTAL` | DOUBLE | NOT NULL |  | Re-stated total number of all of the finance charge transactions. Used as a control number for reconciling. |
| 22 | `FC_STATED_TOTAL` | DOUBLE | NOT NULL |  | Stated total number of all of the finance charge transactions. Used as a control number for reconciling. |
| 23 | `ONEPAYMENT_IND` | DOUBLE |  |  | Represents that all payments are associated to a single check or funds transfer |
| 24 | `PAY_COMPUTED_TOTAL` | DOUBLE | NOT NULL |  | Actual total number of all of the payment transactions. Used as a control number for reconciling. |
| 25 | `PAY_RESTATED_TOTAL` | DOUBLE | NOT NULL |  | Re-stated total number of all of the payment transactions. Used as a control number for reconciling. |
| 26 | `PAY_STATED_TOTAL` | DOUBLE | NOT NULL |  | Stated total number of all of the payment transactions. Used as a control number for reconciling. |
| 27 | `PFT_BATCH_ID` | DOUBLE | NOT NULL |  | Unique identifier for this table |
| 28 | `PFT_EVENT_OCCUR_LOG_ID` | DOUBLE | NOT NULL |  | Id of pft_event_occur_log |
| 29 | `POST_DT_TM` | DATETIME |  |  | posted date and time |
| 30 | `PURGED_IND` | DOUBLE |  |  | Indicates whether or not it is a cancelled batch |
| 31 | `SUBMITTED_DT_TM` | DATETIME |  |  | If submitted, the date and time of submittal |
| 32 | `SUBMITTED_IND` | DOUBLE |  |  | Indicates whether or not submitted |
| 33 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 34 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 35 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 36 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 37 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |
| 38 | `USERNAME` | VARCHAR(50) |  |  | Username of person who posted the batch |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

