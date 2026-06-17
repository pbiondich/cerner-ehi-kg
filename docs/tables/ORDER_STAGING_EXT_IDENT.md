# ORDER_STAGING_EXT_IDENT

> External identifiers of staged orders

**Description:** Order Staging External Identifier  
**Table type:** ACTIVITY  
**Primary key:** _(not published — see note)_  
**Columns:** 11

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `EXTERNAL_IDENT` | VARCHAR(255) |  |  | identifier of the External resource. |
| 2 | `EXTERNAL_RESOURCE_VERSION_TXT` | VARCHAR(4000) |  |  | The latest known version of the external resource |
| 3 | `EXTERNAL_URL` | VARCHAR(4000) |  |  | The URL for the external resource that populated the row. |
| 4 | `ORDER_STAGING_EXT_IDENT_ID` | DOUBLE | NOT NULL |  | Unique generated number that identifies a single row on the ORDER_STAGING_EXT_IDENT table. |
| 5 | `ORDER_STAGING_ID` | DOUBLE |  | FK→ | The associated order_staging_id from the Order_Staging table. |
| 6 | `SYSTEM_URI` | VARCHAR(4000) |  |  | The number or identifier of the external resource that populated the row. |
| 7 | `UPDT_APPLCTX` | DOUBLE |  |  | The application context number from the record info block. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 8 | `UPDT_CNT` | DOUBLE |  |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 9 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 10 | `UPDT_ID` | DOUBLE |  |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 11 | `UPDT_TASK` | DOUBLE |  |  | The registered (assigned) task number for the process that inserted or updated the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `ORDER_STAGING_ID` | [ORDER_STAGING](ORDER_STAGING.md) | `ORDER_STAGING_ID` |

