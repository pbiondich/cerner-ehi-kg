# MSG_OS_ORD_CONFIG

> This table is used to store the type of outstanding orders configuration (Encounter or Date Range)

**Description:** MSG CENTER OUTSTANDING ORDERS CONFIGURATION  
**Table type:** REFERENCE  
**Primary key:** _(not published — see note)_  
**Columns:** 9

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `CONFIG_TYPE_VALUE` | DOUBLE | NOT NULL |  | Specifies whether config is encounter type or date range type. Value of -1 is stored if it is encounter type and number of days is stored if it is of data range type. |
| 2 | `MSG_OS_ORD_CONFIG_ID` | DOUBLE | NOT NULL |  | Unique generated number that identifies a single row on the MSG_OS_ORD_CONFIG table. |
| 3 | `ORD_CATALOG_TYPE_CD` | DOUBLE | NOT NULL |  | Code Value of Order Catalog Type . ORD_STATUS_CD will be zero if this field is non zero |
| 4 | `ORD_STATUS_CD` | DOUBLE | NOT NULL |  | Code Value of Order Status . ORD_CATALOG_TYPE_CD will be zero if this field is non zero |
| 5 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 6 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 7 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 8 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 9 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

