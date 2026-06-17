# SI_RESULT_SET_ORDER_RELTN

> Stores information that links a result_set_id (from the ce_result_set_link table) to an order_id (on the orders table)

**Description:** RESULT_SET_ORDER_RELTN  
**Table type:** ACTIVITY  
**Primary key:** _(not published — see note)_  
**Columns:** 12

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `CLINSIG_DT_TM` | DATETIME |  |  | Clinically significant date time for result_set |
| 2 | `ENTRY_MODE_CD` | DOUBLE | NOT NULL |  | ENTRY MODE - From codeset 29520 |
| 3 | `ORDER_ID` | DOUBLE | NOT NULL | FK→ | Order_id tied to result_set_id |
| 4 | `RESULT_SET_ID` | DOUBLE | NOT NULL |  | Value from column result_set_id on ce_result_set_link table. This column is used to find rowI(s) that relate to an ORDER. |
| 5 | `RESULT_SET_ORDER_RELTN_ID` | DOUBLE | NOT NULL |  | PRIMARY KEY |
| 6 | `RESULT_SET_STATUS_CD` | DOUBLE | NOT NULL |  | Status of result_set |
| 7 | `TASK_COMPLETION_DT_TM` | DATETIME |  |  | Date/time when task was completed by Task Completion Server or Interactive View |
| 8 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 9 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 10 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 11 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 12 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `ORDER_ID` | [ORDERS](ORDERS.md) | `ORDER_ID` |

