# OEN_INTERFACE

> List of all OEN interfaces.

**Description:** OEN Interface  
**Table type:** REFERENCE  
**Primary key:** `INTERFACE_ID`  
**Columns:** 18  
**Referenced by:** 5 columns

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ACTIVE_IND` | DOUBLE |  |  | The table row is active or inactive. A row is generally active unless it is in an inactive state such as logically deleted, combined away, pending purge, etc. |
| 2 | `DOMAIN_FLAG` | DOUBLE |  |  | 0 = common 1 = OE 2 = MDI |
| 3 | `FORMAT_FLAG` | DOUBLE |  |  | Not yet defined |
| 4 | `INTERFACE_ID` | DOUBLE | NOT NULL | PK | This is unique identifier for the interface |
| 5 | `PARENT_IND` | DOUBLE |  |  | Future use. |
| 6 | `PARENT_INTERFACE_ID` | DOUBLE | NOT NULL |  | future |
| 7 | `PRODUCTION_IND` | DOUBLE | NOT NULL |  | This column indicated if interface is in production or not. |
| 8 | `READ_ONLY_IND` | DOUBLE |  |  | Is the interface read_only. |
| 9 | `SCP_EID` | DOUBLE | NOT NULL |  | SCP id for the interface |
| 10 | `SERVICE_FLAG` | DOUBLE | NOT NULL |  | Indicates the service of the interface |
| 11 | `SERVICE_RESOURCE_CD` | DOUBLE | NOT NULL |  | Internal identifier for service resource |
| 12 | `SYSTEM_INTERFACE_ID` | DOUBLE | NOT NULL |  | system interface id. |
| 13 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 14 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 15 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 16 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 17 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |
| 18 | `VERSION_NBR` | DOUBLE | NOT NULL |  | Latest version of the interface. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Referenced by (5)

| From table | Column |
|------------|--------|
| [OEN_INTERFACE_ERR_R](OEN_INTERFACE_ERR_R.md) | `INTERFACE_ID` |
| [OEN_INTERFACE_SCR_R](OEN_INTERFACE_SCR_R.md) | `INTERFACE_ID` |
| [OEN_INTERFACE_TRAITS](OEN_INTERFACE_TRAITS.md) | `INTERFACE_ID` |
| [OEN_PUBLISHER_PUB_R](OEN_PUBLISHER_PUB_R.md) | `INTERFACE_ID` |
| [OEN_SUBSCRIBER_RULE_R](OEN_SUBSCRIBER_RULE_R.md) | `INTERFACE_ID` |

