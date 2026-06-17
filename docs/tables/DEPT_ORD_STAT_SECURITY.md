# DEPT_ORD_STAT_SECURITY

> Used to enable/disable functionality based the dept_status of an order.

**Description:** Department order status security  
**Table type:** REFERENCE  
**Primary key:** _(not published — see note)_  
**Columns:** 11

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ACTIVE_IND` | DOUBLE |  |  | The table row is active or inactive. A row is generally active unless it is in an inactive state such as logically deleted, combined away, pending purge, etc. |
| 2 | `ALLOW_MODIFY_IND` | DOUBLE |  |  | Determines whether the value of data identified by parent_entity_id can be modified for an order with that dept_status_cd. |
| 3 | `DEPT_ORD_STAT_SECURITY_ID` | DOUBLE | NOT NULL |  | Unique identifier for this table. |
| 4 | `DEPT_STATUS_CD` | DOUBLE | NOT NULL |  | Provides a more-detailed order status. This field is used to track the order status within a department. For example, a laboratory order may go through several different states before being completed, e.g. Collected, In-lab, Performed, Verified, etc. |
| 5 | `PARENT_ENTITY_ID` | DOUBLE | NOT NULL |  | The primary id of the table that this row is a child of. Will be the identifier to ORDER_ENTRY_FIELDS table. |
| 6 | `PARENT_ENTITY_NAME` | VARCHAR(32) |  |  | The name of the table that this row is a child of. Will be ORDER_ENTRY_FIELDS. |
| 7 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 8 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 9 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 10 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 11 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

