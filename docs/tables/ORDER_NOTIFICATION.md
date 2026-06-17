# ORDER_NOTIFICATION

> This table stores all Order Notifications for a user and the history of the notification.

**Description:** Order Notification  
**Table type:** ACTIVITY  
**Primary key:** `ORDER_NOTIFICATION_ID`  
**Columns:** 25  
**Referenced by:** 2 columns

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ACTION_SEQUENCE` | DOUBLE | NOT NULL |  | The order action that caused this notification to occur. An action_sequence = 0 signifies that should be applied to the order rather than the order action. |
| 2 | `ASSIGNED_PRSNL_ID` | DOUBLE | NOT NULL | FK→ | The identifier of the personnel who is assigned to the notification from within the personnel group context. |
| 3 | `CAUSED_BY_FLAG` | DOUBLE | NOT NULL |  | Action that causes the notification to be created. 0 = New; 1 = Forward; 2 = Refuse |
| 4 | `FROM_PRSNL_GROUP_ID` | DOUBLE | NOT NULL | FK→ | The identifier of the personnel group which created the notification by forwarding or refusing the "parent" notification. This field will be 0 when the original notification is created. |
| 5 | `FROM_PRSNL_ID` | DOUBLE | NOT NULL | FK→ | The user that is responsible for forwarding or refusing the "parent" notification. This field will be 0 when the original notification is created. |
| 6 | `NOTIFICATION_COMMENT` | VARCHAR(255) |  |  | The free text comment associated with the notification. |
| 7 | `NOTIFICATION_DISPLAY_DT_TM` | DATETIME |  |  | Stores the date on which a notification should be displayed. For renewal notifications (notification_type_flag=1), this field will be set to projected_stop_dt_tm minus renewal period associated to order's policy and duration. For other types of notifications, this field will be the date that the notification is created. |
| 8 | `NOTIFICATION_DISPLAY_TZ` | DOUBLE |  |  | Time zone associated with the corresponding NOTIFICATION_DISPLAY_DT_TM column. |
| 9 | `NOTIFICATION_DT_TM` | DATETIME |  |  | The time that the notification is created. |
| 10 | `NOTIFICATION_REASON_CD` | DOUBLE | NOT NULL |  | The reason associated with the notification. |
| 11 | `NOTIFICATION_STATUS_FLAG` | DOUBLE | NOT NULL |  | The status of the notification. 1 = Pending; 2 = Completed; 3 = Refused; 4 = Forwarded; 5 = Admin-Cleared; 6 = No Longer Needed |
| 12 | `NOTIFICATION_TYPE_FLAG` | DOUBLE | NOT NULL |  | The type of notification stored. 1 = Renew; 2 = Cosign; 3 = Med student; 4 = Incomplete Order; 5 = Refusal |
| 13 | `NOTIFICATION_TZ` | DOUBLE |  |  | Time zone associated with the corresponding DT_TM column. |
| 14 | `ORDER_ID` | DOUBLE | NOT NULL | FK→ | The order that caused this notification to occur |
| 15 | `ORDER_NOTIFICATION_ID` | DOUBLE | NOT NULL | PK | Unique ID for Order_Notification. |
| 16 | `PARENT_ORDER_NOTIFICATION_ID` | DOUBLE | NOT NULL | FK→ | The Link to a "parent " notification when it has been forwarded or refused. |
| 17 | `STATUS_CHANGE_DT_TM` | DATETIME |  |  | The time that the status was updated on the notification. |
| 18 | `STATUS_CHANGE_TZ` | DOUBLE |  |  | Time zone associated with the corresponding DT_TM column. |
| 19 | `TO_PRSNL_GROUP_ID` | DOUBLE | NOT NULL | FK→ | The identifier of the personnel group which the notification in intended for. |
| 20 | `TO_PRSNL_ID` | DOUBLE | NOT NULL | FK→ | The user this notification is intended for. For renew notifications that are suppressed, this field will be 0. |
| 21 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 22 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 23 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 24 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 25 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `ASSIGNED_PRSNL_ID` | [PRSNL](PRSNL.md) | `PERSON_ID` |
| `FROM_PRSNL_GROUP_ID` | [PRSNL_GROUP](PRSNL_GROUP.md) | `PRSNL_GROUP_ID` |
| `FROM_PRSNL_ID` | [PRSNL](PRSNL.md) | `PERSON_ID` |
| `ORDER_ID` | [ORDERS](ORDERS.md) | `ORDER_ID` |
| `PARENT_ORDER_NOTIFICATION_ID` | [ORDER_NOTIFICATION](ORDER_NOTIFICATION.md) | `ORDER_NOTIFICATION_ID` |
| `TO_PRSNL_GROUP_ID` | [PRSNL_GROUP](PRSNL_GROUP.md) | `PRSNL_GROUP_ID` |
| `TO_PRSNL_ID` | [PRSNL](PRSNL.md) | `PERSON_ID` |

## Referenced by (2)

| From table | Column |
|------------|--------|
| [HIM_UNSIGNED_ORDERS](HIM_UNSIGNED_ORDERS.md) | `ORDER_NOTIFICATION_ID` |
| [ORDER_NOTIFICATION](ORDER_NOTIFICATION.md) | `PARENT_ORDER_NOTIFICATION_ID` |

