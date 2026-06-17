# RCA_REG_ACTION

> Defines the base information about the Registration Action.

**Description:** Revenue Cycle Ambulatory - Registration Action  
**Table type:** REFERENCE  
**Primary key:** `RCA_REG_ACTION_ID`  
**Columns:** 13  
**Referenced by:** 2 columns

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ACTIVE_IND` | DOUBLE | NOT NULL |  | The table row is active or inactive. A row is generally active unless it is in an inactive state such as logically deleted, combined away, pending purge, etc. |
| 2 | `CONFIG_LONG_BLOB` | LONGBLOB |  |  | The long blob that contains generic configuration for a revenuecycle registration action. |
| 3 | `LOGICAL_DOMAIN_ID` | DOUBLE | NOT NULL | FK→ | The unique identifier for a logical domain. This identifier allows the data to be grouped by logical domain. For example, If you assign clients a logical_domain_id this would allow you to store data for multiple clients on this table. |
| 4 | `RCA_REG_ACTION_ID` | DOUBLE | NOT NULL | PK | Unique generataed number that identifies a single row on the RCA_REG_ACTION table. |
| 5 | `REG_ACTION_DESC` | VARCHAR(100) | NOT NULL |  | The description of the registration action. |
| 6 | `REG_ACTION_KEY_TXT` | VARCHAR(100) | NOT NULL |  | The uniquely identifiable key per logical domain. |
| 7 | `REG_ACTION_NAME` | VARCHAR(100) | NOT NULL |  | The name of the Registration Action. |
| 8 | `REG_ACTION_TYPE_CD` | DOUBLE | NOT NULL |  | The type of Registration Action. |
| 9 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 10 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 11 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 12 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 13 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `LOGICAL_DOMAIN_ID` | [LOGICAL_DOMAIN](LOGICAL_DOMAIN.md) | `LOGICAL_DOMAIN_ID` |

## Referenced by (2)

| From table | Column |
|------------|--------|
| [RCA_REG_ACTION_CONV_RELTN](RCA_REG_ACTION_CONV_RELTN.md) | `RCA_REG_ACTION_ID` |
| [RCA_REG_ACTION_ITEM](RCA_REG_ACTION_ITEM.md) | `RCA_REG_ACTION_ID` |

