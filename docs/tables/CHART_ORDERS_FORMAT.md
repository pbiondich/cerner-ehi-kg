# CHART_ORDERS_FORMAT

> Stores the formatting parameters for the Orders section in the Chart Format Builder.

**Description:** Formatting parameters for Orders section.  
**Table type:** REFERENCE  
**Primary key:** _(not published — see note)_  
**Columns:** 48

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ACTION_IND` | DOUBLE |  |  | Indicates whether or not the action will display on the chart. Other action information like comments, reviews, and details can still display even if this is 0. |
| 2 | `ACTION_LBL` | VARCHAR(32) |  |  | The label that displays next to the action on the chart. It will only display if action_ind = 1. |
| 3 | `ACTION_SEQ_FLAG` | DOUBLE |  |  | Sort direction for actions within an order. 0 = ascending, 1 = descending |
| 4 | `ACTIVE_IND` | DOUBLE |  |  | The table row is active or inactive. A row is generally active unless it is in an inactive state such as logically deleted, combined away, pending purge, etc. |
| 5 | `ACTIVE_STATUS_CD` | DOUBLE | NOT NULL |  | Indicates the status of the row itself (not the data in the row) such as active, inactive, combined away, pending purge, etc. |
| 6 | `ACTIVE_STATUS_DT_TM` | DATETIME |  |  | The date and time that the active_status_cd was set. |
| 7 | `ACTIVE_STATUS_PRSNL_ID` | DOUBLE | NOT NULL |  | The person who caused the active_status_cd to be set or change. |
| 8 | `CANCELED_DTTM_LBL` | VARCHAR(32) |  |  | The label for the cancelled date/time if LABEL_BIT_MAP has 0x4 selected |
| 9 | `CANCEL_REASON_LBL` | VARCHAR(32) |  |  | The label for the cancel reason if LABEL_BIT_MAP has 0x40 selected. |
| 10 | `CHART_GROUP_ID` | DOUBLE | NOT NULL | FK→ | The primary identifier for the chart group to which the formatting information belongs. |
| 11 | `COMMENTS_IND` | DOUBLE |  |  | Indicates whether or not order comments will display on the chart. |
| 12 | `COMMENTS_LBL` | VARCHAR(32) |  |  | The label that displays next to the order comments. It will only display if comments_ind = 1. |
| 13 | `COMMENT_ORDER` | DOUBLE |  |  | The vertical order position of the order comments in relation to the review information and the order details. |
| 14 | `COMM_TYPE_LBL` | VARCHAR(32) |  |  | The label for the communication type if LABEL_BIT_MAP has 0x20 selected |
| 15 | `DATE_MASK` | VARCHAR(50) | NOT NULL |  | The format for dates within the section. |
| 16 | `DATE_TIME_IND` | DOUBLE |  |  | Indicates whether or not the order date and time will display on the chart for each order. |
| 17 | `DATE_TIME_LBL` | VARCHAR(32) |  |  | The label that displays next to the order date and time. It will only display if date_time_ind = 1 |
| 18 | `DEPT_STATUS_LBL` | VARCHAR(32) |  |  | The label for the department status if LABEL_BIT_MAP has 0x2 selected |
| 19 | `DETAILED_LAYOUT_IND` | DOUBLE | NOT NULL |  | Option to flex the layout of the orders section to the detailed layout. |
| 20 | `DETAILS_IND` | DOUBLE |  |  | Indicates whether or not the order details will display on the chart. |
| 21 | `DETAILS_LBL` | VARCHAR(32) |  |  | The label that displays next to the order details. It will only display if details_ind = 1. |
| 22 | `DETAIL_ORDER` | DOUBLE |  |  | The vertical order position of the order details in relation to the review information and the order comments. |
| 23 | `DISCONTINUED_DTTM_LBL` | VARCHAR(32) |  |  | The label for the order discontinued date/time if LABEL_BIT_MAP has 0x8 selected |
| 24 | `EXCLUDE_OSNAME_IND` | DOUBLE | NOT NULL |  | Indicates if order set names will be excluded from order section listsings |
| 25 | `FUTURE_DISC_DTTM_LBL` | VARCHAR(32) |  |  | The label for the order future discontinue date/time if LABEL_BIT_MAP has 0x10 selected |
| 26 | `LABEL_BIT_MAP` | DOUBLE | NOT NULL |  | List of which labels are enabled stored in a bitmap |
| 27 | `MNEMONIC_IND` | DOUBLE |  |  | Indicates whether or not the order mnemonic will display on the chart. |
| 28 | `MNEMONIC_LBL` | VARCHAR(32) |  |  | The label that appears next to the order mnemonic. It will only display if the mnemonic_ind = 1. |
| 29 | `ORDER_PHYS_IND` | DOUBLE |  |  | Indicates whether or not the Ordering Physician will display on the chart. |
| 30 | `ORDER_PHYS_LBL` | VARCHAR(32) |  |  | The label that appears next to the ordering physician. It will only appear if the order_phys_ind = 1. |
| 31 | `ORDER_PLACER_IND` | DOUBLE |  |  | Indicates whether or not the person who placed the order is shown on the chart. |
| 32 | `ORDER_PLACER_LBL` | VARCHAR(32) |  |  | The label that appears next to the person who placed the order. It will only appear if the order_placer_ind = 1. |
| 33 | `ORDER_SEQ_FLAG` | DOUBLE |  |  | Specifies the type of sorting sequence. |
| 34 | `ORDER_STATUS_IND` | DOUBLE |  |  | Indicates whether or not the order status will display on the chart. |
| 35 | `ORDER_STATUS_LBL` | VARCHAR(32) |  |  | The label that appears next to the order status. It will only appear if the order_status_ind = 1. |
| 36 | `ORDER_TYPE_IND` | DOUBLE |  |  | Indicates whether or not the order type will display on the chart. |
| 37 | `ORDER_TYPE_LBL` | VARCHAR(32) |  |  | The label that appears next to the order type. It will only display if the order_type_ind = 1. |
| 38 | `ORIG_ORDER_DTTM_LBL` | VARCHAR(32) |  |  | The label for the original order date/time if LABEL_BIT_MAP has 0x1 selected |
| 39 | `REVIEW_IND` | DOUBLE |  |  | Indicates whether or not the review information will display on the chart. |
| 40 | `REVIEW_LBL` | VARCHAR(32) |  |  | The label that appears next to the review information. It will only display if the review_ind = 1. |
| 41 | `REVIEW_ORDER` | DOUBLE |  |  | The order position of the review information in relation to the order details and order comments. |
| 42 | `SUPPRESS_MEDS_BIT_MAP` | DOUBLE |  |  | Suppress medication types from displaying according to the selection |
| 43 | `TIME_MASK` | VARCHAR(32) | NOT NULL |  | The format for all time values within the section. |
| 44 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 45 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 46 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 47 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 48 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `CHART_GROUP_ID` | [CHART_GROUP](CHART_GROUP.md) | `CHART_GROUP_ID` |

