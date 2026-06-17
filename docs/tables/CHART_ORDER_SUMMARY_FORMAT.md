# CHART_ORDER_SUMMARY_FORMAT

> chart order summary format

**Description:** This table defines the format of the order summary section type  
**Table type:** REFERENCE  
**Primary key:** _(not published — see note)_  
**Columns:** 31

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ACTIVE_IND` | DOUBLE |  |  | The table row is active or inactive. A row is generally active unless it is in an inactive state such as logically deleted, combined away, pending purge, etc. |
| 2 | `ACTIVE_STATUS_CD` | DOUBLE | NOT NULL |  | Indicates the status of the row itself (not the data in the row) such as active, inactive, combined away, pending purge, etc. |
| 3 | `ACTIVE_STATUS_DT_TM` | DATETIME |  |  | The date and time that the active_status_cd was set. |
| 4 | `ACTIVE_STATUS_PRSNL_ID` | DOUBLE | NOT NULL |  | The person who caused the active_status_cd to be set or change. |
| 5 | `CANCEL_REASON_LBL` | VARCHAR(32) |  |  | This is the label for cancel reason column in a cancelled order summary section. |
| 6 | `CANCEL_REASON_ORDER` | DOUBLE |  |  | This is the order for cancel reason column in a cancelled order summary section. |
| 7 | `CHART_GROUP_ID` | DOUBLE | NOT NULL |  | This number uniquely identifies the chart group |
| 8 | `DATE_LBL` | VARCHAR(20) |  |  | This is the label for date column in a order summary section. |
| 9 | `DATE_MASK` | VARCHAR(50) |  |  | This is the date format mask for date column. |
| 10 | `DATE_ORDER` | DOUBLE |  |  | This is the order for date column in a order summary section. |
| 11 | `DEPT_STATUS_LBL` | VARCHAR(32) |  |  | This is the label for department status column in all orders or pending orders summary section |
| 12 | `DEPT_STATUS_ORDER` | DOUBLE |  |  | This is the order for department status column in all order or pending orders summary section. |
| 13 | `MNEMONIC_LBL` | VARCHAR(32) |  |  | This is the label for a order mnemonic column in a order summary section. |
| 14 | `MNEMONIC_ORDER` | DOUBLE |  |  | This is the order for a order mnemonic column in a order summary section. |
| 15 | `NAME_LBL` | VARCHAR(32) |  |  | This is the label for a order name column in a order summary section. |
| 16 | `NAME_ORDER` | DOUBLE |  |  | This is the order for a order name column in a order summary section. |
| 17 | `ORDER_PROVIDER_IND` | DOUBLE |  |  | This is the indicator to define whether to print the original, current, original and current, or all ordering providers |
| 18 | `ORDER_PROVIDER_LBL` | VARCHAR(32) |  |  | This is the label for ordering provider column in an orders summary section |
| 19 | `ORDER_PROVIDER_ORDER` | DOUBLE |  |  | This is the order for ordering provider column in an orders summary section |
| 20 | `ORDER_SEQ_FLAG` | DOUBLE |  |  | This flag indicates that the printed results are in the order of date/name or in the order of name/date. |
| 21 | `ORDER_SUMMARY_TYPE` | DOUBLE |  |  | This defines the type of order summary format that will print on the chart (i.e. pending, cancelled, ordered) |
| 22 | `STATUS_LBL` | VARCHAR(32) |  |  | This is the label for status column in a all orders or pending orders summary section. |
| 23 | `STATUS_ORDER` | DOUBLE |  |  | This is the order for status column in a all orders or pending orders summary section. |
| 24 | `TIME_LBL` | VARCHAR(20) |  |  | This is the label for a time column in a order summary section. |
| 25 | `TIME_MASK` | VARCHAR(50) |  |  | This is the time format for a time column in a order summary section. |
| 26 | `TIME_ORDER` | DOUBLE |  |  | This is the order for a time column in a order summary section. |
| 27 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 28 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 29 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 30 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 31 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

