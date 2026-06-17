# ORDER_STAGING_ERX_INFO

> Information for electronically prescribed staged orders.

**Description:** Order Staging eRx Information  
**Table type:** ACTIVITY  
**Primary key:** _(not published — see note)_  
**Columns:** 8

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `EXTERNAL_CHAIN` | VARCHAR(500) |  |  | An ExternalChain is an external id used to identify all; orders in one order chain. An order chain is a set; of orders that are linked together in chronological order. An; order chain is used when an order is renewed or replaced.; The purpose is to be able provide a grouping of related orders. |
| 2 | `ORDER_STAGING_ERX_INFO_ID` | DOUBLE | NOT NULL |  | Unique generated number that identifies a single row on the ORDER_STAGING_ERX_INFO table. |
| 3 | `ORDER_STAGING_ID` | DOUBLE |  | FK→ | The associated order_staging_id from the Order_Staging table. |
| 4 | `UPDT_APPLCTX` | DOUBLE |  |  | The application context number from the record info block. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 5 | `UPDT_CNT` | DOUBLE |  |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 6 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 7 | `UPDT_ID` | DOUBLE |  |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 8 | `UPDT_TASK` | DOUBLE |  |  | The registered (assigned) task number for the process that inserted or updated the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `ORDER_STAGING_ID` | [ORDER_STAGING](ORDER_STAGING.md) | `ORDER_STAGING_ID` |

