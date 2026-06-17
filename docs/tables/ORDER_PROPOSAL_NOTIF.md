# ORDER_PROPOSAL_NOTIF

> This table stores notifications to inform users of proposed actions on orders.

**Description:** Order Proposal Notification  
**Table type:** ACTIVITY  
**Primary key:** `ORDER_PROPOSAL_NOTIF_ID`  
**Columns:** 21  
**Referenced by:** 1 columns

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ASSIGNED_PRSNL_ID` | DOUBLE | NOT NULL | FK→ | The identifier of the personnel who is assigned to the notification from within the personnel group context. |
| 2 | `FROM_PRSNL_GROUP_ID` | DOUBLE | NOT NULL | FK→ | The identifier of the personnel group which a personnel acted from when forwarding an order proposal notification. |
| 3 | `FROM_PRSNL_ID` | DOUBLE | NOT NULL | FK→ | The identifier of the personnel which created the notification by acting on an order proposal or forwarding an existing notification. |
| 4 | `NOTIFICATION_COMMENT` | VARCHAR(1000) |  |  | The free text comment that is supplied by the user to communicate details of the notification. |
| 5 | `NOTIFICATION_CREATED_DT_TM` | DATETIME | NOT NULL |  | The date/time when the notification was created. |
| 6 | `NOTIFICATION_CREATED_TZ` | DOUBLE |  |  | Time zone associated with the notification creation date/time. |
| 7 | `NOTIFICATION_ORIGIN_FLAG` | DOUBLE | NOT NULL |  | Illustrates the origin of the notification creation. Value flag values are: 1 - Newly created based on an action on an order proposal, 2 - Forwarded from an existing notification |
| 8 | `NOTIFICATION_RESOLVED_DT_TM` | DATETIME |  |  | The date/time when the notification was resolved (accepted, rejected, forwarded, or is no longer needed). |
| 9 | `NOTIFICATION_RESOLVED_TZ` | DOUBLE |  |  | Time zone associated with the notification resolved date/time. |
| 10 | `NOTIFICATION_STATUS_FLAG` | DOUBLE | NOT NULL |  | Illustrates the current status of the order proposal notification. Valid flag values are: 1 - Pending, 2 - Accepted, 3 - Rejected, 4 - Forwarded, 5 - No Longer Needed, 6 - No Longer Needed due to Withdraw. |
| 11 | `NOTIFICATION_TYPE_FLAG` | DOUBLE | NOT NULL |  | Illustrates the type of notification. Valid flag values are: 1 - Order Proposal Creation Notification. |
| 12 | `ORDER_PROPOSAL_ID` | DOUBLE | NOT NULL | FK→ | The identifier of the order proposal which is associated to the notification. |
| 13 | `ORDER_PROPOSAL_NOTIF_ID` | DOUBLE | NOT NULL | PK | The primary key of this table. It is internally assigned by the system. |
| 14 | `PARENT_OP_NOTIFICATION_ID` | DOUBLE | NOT NULL | FK→ | The identifier of the parent order proposal notification if the notification originated from a forward action. |
| 15 | `TO_PRSNL_GROUP_ID` | DOUBLE | NOT NULL | FK→ | The identifier of the personnel group which the notification is intended for. |
| 16 | `TO_PRSNL_ID` | DOUBLE | NOT NULL | FK→ | The identifier of the personnel which the notification is intended for. |
| 17 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 18 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 19 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 20 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 21 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `ASSIGNED_PRSNL_ID` | [PRSNL](PRSNL.md) | `PERSON_ID` |
| `FROM_PRSNL_GROUP_ID` | [PRSNL_GROUP](PRSNL_GROUP.md) | `PRSNL_GROUP_ID` |
| `FROM_PRSNL_ID` | [PRSNL](PRSNL.md) | `PERSON_ID` |
| `ORDER_PROPOSAL_ID` | [ORDER_PROPOSAL](ORDER_PROPOSAL.md) | `ORDER_PROPOSAL_ID` |
| `PARENT_OP_NOTIFICATION_ID` | [ORDER_PROPOSAL_NOTIF](ORDER_PROPOSAL_NOTIF.md) | `ORDER_PROPOSAL_NOTIF_ID` |
| `TO_PRSNL_GROUP_ID` | [PRSNL_GROUP](PRSNL_GROUP.md) | `PRSNL_GROUP_ID` |
| `TO_PRSNL_ID` | [PRSNL](PRSNL.md) | `PERSON_ID` |

## Referenced by (1)

| From table | Column |
|------------|--------|
| [ORDER_PROPOSAL_NOTIF](ORDER_PROPOSAL_NOTIF.md) | `PARENT_OP_NOTIFICATION_ID` |

