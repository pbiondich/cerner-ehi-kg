# GUAR_FIN_RESP_RELTN_HIST

> Used for tracking history of changes to the guarantor financial responsibility relationship.

**Description:** Guarantor Financial Responsibility Relationship History  
**Table type:** ACTIVITY  
**Primary key:** _(not published — see note)_  
**Columns:** 21

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ACTIVE_IND` | DOUBLE | NOT NULL |  | The table row is active or inactive. A row is generally active unless it is in an inactive state such as logically deleted, combined away, pending purge, etc. |
| 2 | `ACTIVE_STATUS_CD` | DOUBLE | NOT NULL |  | Indicates the status of the row itself (not the data in the row) such as active, inactive, combined away, pending purge, etc. |
| 3 | `ACTIVE_STATUS_DT_TM` | DATETIME | NOT NULL |  | The date and time that the active_status_cd was set. |
| 4 | `ACTIVE_STATUS_PRSNL_ID` | DOUBLE | NOT NULL |  | The person who caused the active_status_cd to be set or change. |
| 5 | `BEG_EFFECTIVE_DT_TM` | DATETIME | NOT NULL |  | The date and time for which this table row becomes effective. Normally, this will be the date and time the row is added, but could be a past or future date and time. |
| 6 | `CHANGE_BIT` | DOUBLE | NOT NULL |  | Identifies which columns have had a change. |
| 7 | `END_EFFECTIVE_DT_TM` | DATETIME | NOT NULL |  | The date/time after which the row is no longer valid as active current data. This may be valued with the date that the row became inactive. |
| 8 | `GUAR_FINANCIAL_RESP_ID` | DOUBLE | NOT NULL | FK→ | Unique generated number that identifies a single row on the GUAR_FINANCIAL_RESP table. |
| 9 | `GUAR_FINANCIAL_RESP_TYPE_CD` | DOUBLE | NOT NULL |  | **OBSOLETE** This functionality for this column has been moved to the GUAR_FINANCIAL_RESP table. Defines the scope of the guarantor¿s financial responsibility. |
| 10 | `GUAR_FIN_RESP_RELTN_HIST_ID` | DOUBLE | NOT NULL |  | Unique generated number identifying the row on the GUAR_FINANCIAL_RESP table to which the guarantor is related. |
| 11 | `GUAR_FIN_RESP_RELTN_ID` | DOUBLE | NOT NULL | FK→ | Unique generated number that identifies a single row on the GUAR_FIN_RESP_RELTN table. |
| 12 | `PARENT_ENTITY_ID` | DOUBLE | NOT NULL |  | The value of the primary identifier of the table representing the guarantor and to which the financial responsibility row is related. |
| 13 | `PARENT_ENTITY_NAME` | VARCHAR(30) | NOT NULL |  | The upper case name of the table to which this financial responsibility row is related (i.e., person_person_reltn, encntr_person_reltn, person_org_reltn, encntr_org_reltn, etc.). |
| 14 | `PM_HIST_TRACKING_ID` | DOUBLE | NOT NULL | FK→ | This is the value of the unique primary identifier of the pm_hist_tracking table. It is an internal system assigned number. |
| 15 | `TRACKING_BIT` | DOUBLE | NOT NULL |  | Identifies which columns are being tracked for history. |
| 16 | `TRANSACTION_DT_TM` | DATETIME | NOT NULL |  | ** OBSOLETE **. Use column updt_dt_tm for any filtering/ordering query. If transaction date time is needed, it should be retrieved from pm_hist_tracking table. Note that its date may be in the past, as in before the update date time. |
| 17 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 18 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 19 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 20 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 21 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `GUAR_FINANCIAL_RESP_ID` | [GUAR_FINANCIAL_RESP](GUAR_FINANCIAL_RESP.md) | `GUAR_FINANCIAL_RESP_ID` |
| `GUAR_FIN_RESP_RELTN_ID` | [GUAR_FIN_RESP_RELTN](GUAR_FIN_RESP_RELTN.md) | `GUAR_FIN_RESP_RELTN_ID` |
| `PM_HIST_TRACKING_ID` | [PM_HIST_TRACKING](PM_HIST_TRACKING.md) | `PM_HIST_TRACKING_ID` |

