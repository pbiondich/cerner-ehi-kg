# UCM_CASE

> This table stores high level case information.

**Description:** Unified Case Management Case  
**Table type:** ACTIVITY  
**Primary key:** `UCM_CASE_ID`  
**Columns:** 11  
**Referenced by:** 5 columns

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `CREATE_DT_TM` | DATETIME | NOT NULL |  | This field contains the date and time this record was created. |
| 2 | `LOCKED_IND` | DOUBLE |  |  | This field indicates if this case is locked by another user. Use the UPDT* fields to determine who and when the case was locked. |
| 3 | `ORDER_ID` | DOUBLE | NOT NULL | FK→ | This field uniquely identifies the order that represents this case. |
| 4 | `STATUS_ORDER_ID` | DOUBLE | NOT NULL | FK→ | Indicates order updated by UCM to help control the case order status. |
| 5 | `UCMR_CASE_TYPE_ID` | DOUBLE | NOT NULL | FK→ | This field contains the unique Identifier for the case type version. |
| 6 | `UCM_CASE_ID` | DOUBLE | NOT NULL | PK | This field contains the unique identifier for the case. |
| 7 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 8 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 9 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 10 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 11 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `ORDER_ID` | [ORDERS](ORDERS.md) | `ORDER_ID` |
| `STATUS_ORDER_ID` | [ORDERS](ORDERS.md) | `ORDER_ID` |
| `UCMR_CASE_TYPE_ID` | [UCMR_CASE_TYPE](UCMR_CASE_TYPE.md) | `UCMR_CASE_TYPE_ID` |

## Referenced by (5)

| From table | Column |
|------------|--------|
| [UCM_CASE_FLAG](UCM_CASE_FLAG.md) | `UCM_CASE_ID` |
| [UCM_CASE_GROUP_PREQUAL](UCM_CASE_GROUP_PREQUAL.md) | `UCM_CASE_ID` |
| [UCM_CASE_STEP](UCM_CASE_STEP.md) | `UCM_CASE_ID` |
| [UCM_CHARGE_ORDER_R](UCM_CHARGE_ORDER_R.md) | `UCM_CASE_ID` |
| [UCM_PRSNL_ASSIGNMENT](UCM_PRSNL_ASSIGNMENT.md) | `UCM_CASE_ID` |

