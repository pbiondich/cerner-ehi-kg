# SI_OEN_PROPERTY

> Defines configuration properties for Open engine processes

**Description:** Open Engine Property  
**Table type:** REFERENCE  
**Primary key:** `SI_OEN_PROPERTY_ID`  
**Columns:** 10  
**Referenced by:** 8 columns

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `PROPERTY_NAME` | VARCHAR(100) | NOT NULL |  | Name of the property |
| 2 | `PROPERTY_SET_ID` | DOUBLE | NOT NULL | FK→ | The set of properties that the property belongs to |
| 3 | `PROPERTY_TYPE` | VARCHAR(31) | NOT NULL |  | Data type of the property value |
| 4 | `PROPERTY_VALUE_TXT` | VARCHAR(255) |  |  | The configured valued for the property |
| 5 | `SI_OEN_PROPERTY_ID` | DOUBLE | NOT NULL | PK | PRIMARY KEY |
| 6 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 7 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 8 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 9 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 10 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `PROPERTY_SET_ID` | [SI_OEN_PROPERTY](SI_OEN_PROPERTY.md) | `SI_OEN_PROPERTY_ID` |

## Referenced by (8)

| From table | Column |
|------------|--------|
| [SI_OEN_COMCHANNEL](SI_OEN_COMCHANNEL.md) | `COMCHANNEL_PROPERTY_ID` |
| [SI_OEN_COMCHANNEL](SI_OEN_COMCHANNEL.md) | `ROUTER_PROPERTY_ID` |
| [SI_OEN_ENDPOINT](SI_OEN_ENDPOINT.md) | `CONNECTION_PROPERTY_ID` |
| [SI_OEN_ENDPOINT](SI_OEN_ENDPOINT.md) | `ENDPOINT_PROPERTY_ID` |
| [SI_OEN_ENDPOINT](SI_OEN_ENDPOINT.md) | `PROTOCOL_PROPERTY_ID` |
| [SI_OEN_PROPERTY](SI_OEN_PROPERTY.md) | `PROPERTY_SET_ID` |
| [SI_OEN_STEP](SI_OEN_STEP.md) | `STEP_PROPERTY_ID` |
| [SI_OEN_SUBSCRIPTION](SI_OEN_SUBSCRIPTION.md) | `SUBSCRIPTION_PROPERTY_ID` |

