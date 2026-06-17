# RC_SERVICE_SET_ITEM

> Items with in a service set

**Description:** Revenue Cycle Service Set Item  
**Table type:** REFERENCE  
**Primary key:** _(not published — see note)_  
**Columns:** 11

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ACTIVE_IND` | DOUBLE | NOT NULL |  | The table row is active or inactive. A row is generally active unless it is in an inactive state such as logically deleted, combined away, pending purge, etc. |
| 2 | `ORDER_ACTIVITY_SUB_TYPE_CD` | DOUBLE | NOT NULL |  | The order sub activity type code that is associated with this service set time. |
| 3 | `ORDER_ACTIVITY_TYPE_CD` | DOUBLE | NOT NULL |  | The order activity type code that is associated with this service set item. |
| 4 | `ORDER_CATALOG_TYPE_CD` | DOUBLE | NOT NULL |  | The order catalog type code that is associated with this service set item. |
| 5 | `RC_SERVICE_SET_ID` | DOUBLE | NOT NULL | FK→ | The identifier of the service set to which this item is associated. |
| 6 | `RC_SERVICE_SET_ITEM_ID` | DOUBLE | NOT NULL |  | Unique generated number that identifies a single row on the RC_SERVICE_SET_ITEM table. |
| 7 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 8 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 9 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 10 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 11 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `RC_SERVICE_SET_ID` | [RC_SERVICE_SET](RC_SERVICE_SET.md) | `RC_SERVICE_SET_ID` |

