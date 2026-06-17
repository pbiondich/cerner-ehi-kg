# SI_OEN_COMCHANNEL

> Defines comserver channels that are loaded and ran inside of Open Engine comservers

**Description:** Open Engine Comserver Channel  
**Table type:** REFERENCE  
**Primary key:** `SI_OEN_COMCHANNEL_ID`  
**Columns:** 15  
**Referenced by:** 1 columns

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `AUTOSTART_IND` | DOUBLE | NOT NULL |  | Indicator for flagging comchannels that should be started when the comserver is started |
| 2 | `COMCHANNEL_NAME` | VARCHAR(255) | NOT NULL |  | User provided name for the comchannel |
| 3 | `COMCHANNEL_PROPERTY_ID` | DOUBLE | NOT NULL | FK→ | ID for configuration properties for the com channel |
| 4 | `COMCHANNEL_TYPE` | VARCHAR(100) |  |  | The type of channel for this comserver |
| 5 | `DESCRIPTION` | VARCHAR(255) |  |  | Long description of the comchannel |
| 6 | `ROUTER_PROPERTY_ID` | DOUBLE | NOT NULL | FK→ | ID for configuration properties for the router |
| 7 | `ROUTER_TYPE` | VARCHAR(100) |  |  | Class name of the router implementation to be used by the comchannel |
| 8 | `SI_OEN_COMCHANNEL_ID` | DOUBLE | NOT NULL | PK | Primary Key |
| 9 | `SI_OEN_CONTEXT_ID` | DOUBLE | NOT NULL | FK→ | ID of the comserver that the comchannel will run in |
| 10 | `SI_OEN_SUBSCRIPTION_ID` | DOUBLE | NOT NULL | FK→ | ID for the step subscriptions used by the comchannel |
| 11 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 12 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 13 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 14 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 15 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `COMCHANNEL_PROPERTY_ID` | [SI_OEN_PROPERTY](SI_OEN_PROPERTY.md) | `SI_OEN_PROPERTY_ID` |
| `ROUTER_PROPERTY_ID` | [SI_OEN_PROPERTY](SI_OEN_PROPERTY.md) | `SI_OEN_PROPERTY_ID` |
| `SI_OEN_CONTEXT_ID` | [SI_OEN_CONTEXT](SI_OEN_CONTEXT.md) | `SI_OEN_CONTEXT_ID` |
| `SI_OEN_SUBSCRIPTION_ID` | [SI_OEN_SUBSCRIPTION](SI_OEN_SUBSCRIPTION.md) | `SI_OEN_SUBSCRIPTION_ID` |

## Referenced by (1)

| From table | Column |
|------------|--------|
| [SI_OEN_CHANN_ENDPOINT_R](SI_OEN_CHANN_ENDPOINT_R.md) | `SI_OEN_COMCHANNEL_ID` |

