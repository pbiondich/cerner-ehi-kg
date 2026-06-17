# AUTH_ITEM_ORDER_R_HIST

> Stores information about the history of an authorization item/order relationship.

**Description:** Authorization Item Order Relationship History  
**Table type:** ACTIVITY  
**Primary key:** _(not published — see note)_  
**Columns:** 20

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ACTIVE_IND` | DOUBLE | NOT NULL |  | The table row is active or inactive. A row is generally active unless it is in an inactive state such as logically deleted, combined away, pending purge, etc. |
| 2 | `ACTIVE_STATUS_CD` | DOUBLE | NOT NULL |  | Indicates the status of the row itself (not the data in the row) such as active, inactive, combined away, pending purge, etc. |
| 3 | `ACTIVE_STATUS_DT_TM` | DATETIME | NOT NULL |  | The date and time that the active_status_cd was set. |
| 4 | `ACTIVE_STATUS_PRSNL_ID` | DOUBLE | NOT NULL |  | The person who caused the active_status_cd to be set or change. |
| 5 | `AUTHORIZATION_ITEM_ID` | DOUBLE | NOT NULL |  | Unique generated number that identifies a single row on the Authorization_Item table. |
| 6 | `AUTH_ITEM_ORDER_RELTN_ID` | DOUBLE | NOT NULL | FK→ | Unique generated number that identifiers a single row on the AUTH_ITEM_ORDER_RELTN table to which this history row is associated. |
| 7 | `AUTH_ITEM_ORDER_R_HIST_ID` | DOUBLE | NOT NULL |  | Unique generated number that identifiers a single row on the AUTH_ITEM_ORDER_R_HIST table. |
| 8 | `AUTH_USED_CNT` | DOUBLE | NOT NULL |  | The number of the item's authorized units that were used for the order. |
| 9 | `CHANGE_BIT` | DOUBLE | NOT NULL |  | Identifies which columns have had a change. |
| 10 | `CREATE_DT_TM` | DATETIME |  |  | The date and time the record was created |
| 11 | `CREATE_PRSNL_ID` | DOUBLE | NOT NULL | FK→ | This is the person responsible for creating a row in the Authorization Item/ Order Relationship table. |
| 12 | `ORDER_ID` | DOUBLE | NOT NULL | FK→ | Unique generated number that identifies a single row on the ORDERS table. |
| 13 | `PM_HIST_TRACKING_ID` | DOUBLE | NOT NULL | FK→ | This is the value of the unique primary identifier of the pm_hist_tracking table. It is an internal system assigned number. |
| 14 | `TRACKING_BIT` | DOUBLE | NOT NULL |  | Identifies which columns are being tracked for history. |
| 15 | `TRANSACTION_DT_TM` | DATETIME |  |  | ** OBSOLETE **. Use column updt_dt_tm for any filtering/ordering query. If transaction date time is needed, it should be retrieved from pm_hist_tracking table. Note that its date may be in the past, as in before the update date time. |
| 16 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 17 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 18 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 19 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 20 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `AUTH_ITEM_ORDER_RELTN_ID` | [AUTH_ITEM_ORDER_RELTN](AUTH_ITEM_ORDER_RELTN.md) | `AUTH_ITEM_ORDER_RELTN_ID` |
| `CREATE_PRSNL_ID` | [PRSNL](PRSNL.md) | `PERSON_ID` |
| `ORDER_ID` | [ORDERS](ORDERS.md) | `ORDER_ID` |
| `PM_HIST_TRACKING_ID` | [PM_HIST_TRACKING](PM_HIST_TRACKING.md) | `PM_HIST_TRACKING_ID` |

