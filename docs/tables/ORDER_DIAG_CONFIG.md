# ORDER_DIAG_CONFIG

> Stores client defined settings on how orders should behave with regards to dignoses. The client can define whether or not a diagnosis is required for an order

**Description:** Order Diagnosis Configuration  
**Table type:** REFERENCE  
**Primary key:** _(not published — see note)_  
**Columns:** 12

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `CATALOG_CD` | DOUBLE | NOT NULL | FK→ | Stores the order catalog that the configuration applies to. |
| 2 | `CATALOG_TYPE_CD` | DOUBLE | NOT NULL | FK→ | Stores the catalog type that the configuration applies to. |
| 3 | `CONFIG_MEANING` | VARCHAR(12) | NOT NULL |  | Stores a key for the diagnosis configuration being defined. |
| 4 | `CONFIG_VALUE` | DOUBLE | NOT NULL |  | Stores the value for the diagnosis configuration |
| 5 | `HEALTH_PLAN_ID` | DOUBLE | NOT NULL | FK→ | Foreign key to the Health_Plan table |
| 6 | `ORDER_DIAG_CONFIG_ID` | DOUBLE | NOT NULL |  | The primary key of this table |
| 7 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 8 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 9 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 10 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 11 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 12 | `VENUE_TYPE_FLAG` | DOUBLE | NOT NULL |  | Stores a flag indicating the type of venue that the configuration applies to. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `CATALOG_CD` | [ORDER_CATALOG](ORDER_CATALOG.md) | `CATALOG_CD` |
| `CATALOG_TYPE_CD` | [CODE_VALUE](CODE_VALUE.md) | `CODE_VALUE` |
| `HEALTH_PLAN_ID` | [HEALTH_PLAN](HEALTH_PLAN.md) | `HEALTH_PLAN_ID` |

