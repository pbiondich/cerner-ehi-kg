# PERSON_FIN_ASSET_HIST

> Contains historical information from the PERSON_FIN_ASSET table

**Description:** Person Financial Asset History  
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
| 5 | `ASSET_DETAIL_TXT` | VARCHAR(255) |  |  | The freetext description which gives additional information about the person's financial asset. |
| 6 | `ASSET_TYPE_CD` | DOUBLE | NOT NULL |  | The financial asset type code defines the tyep of asset (for example: bank accounts, vehicles, re estate properties, etc.) |
| 7 | `ASSET_VALUE` | DOUBLE |  |  | The monetary value of the financial asset as defined by the person's financial asset type code. |
| 8 | `CHANGE_BIT` | DOUBLE | NOT NULL |  | Identifies which columns have had a change. |
| 9 | `PARENT_ENTITY_ID` | DOUBLE | NOT NULL |  | The value of the primary identifier of the parent table to which the person's financial asset row is related. |
| 10 | `PARENT_ENTITY_NAME` | VARCHAR(30) | NOT NULL |  | The upper case name of the table to which this person financial asset row is related (i.e., person, financial_case, etc). |
| 11 | `PERSON_FIN_ASSET_HIST_ID` | DOUBLE | NOT NULL |  | Uniquely generated number to identify a specific row on the PERSON_FIN_ASSET_HIST table. |
| 12 | `PERSON_FIN_ASSET_ID` | DOUBLE | NOT NULL | FK→ | Uniquely generated number to identify a row on the PERSON_FIN_ASSET table. |
| 13 | `PM_HIST_TRACKING_ID` | DOUBLE | NOT NULL | FK→ | This is the value of the unique primary identifier of the pm_hist_tracking table. It is an internal system assigned number. |
| 14 | `TRACKING_BIT` | DOUBLE | NOT NULL |  | Identifies which columns are being tracked for history. |
| 15 | `TRANSACTION_DT_TM` | DATETIME |  |  | ** OBSOLETE **. Use column updt_dt_tm for any filtering/ordering query. If transaction date time is needed, it should be retrieved from pm_hist_tracking table. Note that its date may be in the past, as in before the update date time. |
| 16 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 17 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 18 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 19 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 20 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 21 | `VERIFY_DT_TM` | DATETIME |  |  | The date and time the financial asset was last verified. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `PERSON_FIN_ASSET_ID` | [PERSON_FIN_ASSET](PERSON_FIN_ASSET.md) | `PERSON_FIN_ASSET_ID` |
| `PM_HIST_TRACKING_ID` | [PM_HIST_TRACKING](PM_HIST_TRACKING.md) | `PM_HIST_TRACKING_ID` |

