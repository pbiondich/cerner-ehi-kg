# SI_OEN_ENDPOINT

> Definition of endpoints used for connecting with external systems

**Description:** Open Engine Endpoints  
**Table type:** REFERENCE  
**Primary key:** `SI_OEN_ENDPOINT_ID`  
**Columns:** 18  
**Referenced by:** 1 columns

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `CONNECTION_PROPERTY_ID` | DOUBLE | NOT NULL | FK→ | ID that links to the connection adapter configuration properties for the endpoint |
| 2 | `CONNECTION_TYPE` | VARCHAR(100) |  |  | The class name of the connection adapter to be used by the endpoint |
| 3 | `DEDICATED_IND` | DOUBLE | NOT NULL |  | Indicator that flags the endpoint as being able to only be used in one comchannel. |
| 4 | `DESCRIPTION` | VARCHAR(255) |  |  | Description of the endpoint |
| 5 | `ENDPOINT_NAME` | VARCHAR(255) | NOT NULL |  | Name of the endpoint |
| 6 | `ENDPOINT_PROPERTY_ID` | DOUBLE | NOT NULL | FK→ | ID that links the endpoint to its configuration properties |
| 7 | `ENDPOINT_TYPE` | VARCHAR(100) |  |  | Describes the type of endpoint: source, destination, or bidirectional |
| 8 | `EXCLUSIONARY_IND` | DOUBLE | NOT NULL |  | Indicator that flags the endpoint as being the only endpoint that can be used by the comchannel to that particular type |
| 9 | `PROTOCOL_PROPERTY_ID` | DOUBLE | NOT NULL | FK→ | ID that links to the protocol configuration properties for the endpoint |
| 10 | `PROTOCOL_TYPE` | VARCHAR(100) |  |  | The class name of the protocol to be used to read from or write to the connection |
| 11 | `SI_OEN_CONTEXT_ID` | DOUBLE | NOT NULL | FK→ | ID that links the endpoint to the comserver that it is used in. |
| 12 | `SI_OEN_ENDPOINT_ID` | DOUBLE | NOT NULL | PK | PRIMARY KEY |
| 13 | `SI_OEN_SUBSCRIPTION_ID` | DOUBLE | NOT NULL | FK→ | ID that links to the event subscriptions used by the endpoint |
| 14 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 15 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 16 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 17 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 18 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `CONNECTION_PROPERTY_ID` | [SI_OEN_PROPERTY](SI_OEN_PROPERTY.md) | `SI_OEN_PROPERTY_ID` |
| `ENDPOINT_PROPERTY_ID` | [SI_OEN_PROPERTY](SI_OEN_PROPERTY.md) | `SI_OEN_PROPERTY_ID` |
| `PROTOCOL_PROPERTY_ID` | [SI_OEN_PROPERTY](SI_OEN_PROPERTY.md) | `SI_OEN_PROPERTY_ID` |
| `SI_OEN_CONTEXT_ID` | [SI_OEN_CONTEXT](SI_OEN_CONTEXT.md) | `SI_OEN_CONTEXT_ID` |
| `SI_OEN_SUBSCRIPTION_ID` | [SI_OEN_SUBSCRIPTION](SI_OEN_SUBSCRIPTION.md) | `SI_OEN_SUBSCRIPTION_ID` |

## Referenced by (1)

| From table | Column |
|------------|--------|
| [SI_OEN_CHANN_ENDPOINT_R](SI_OEN_CHANN_ENDPOINT_R.md) | `SI_OEN_ENDPOINT_ID` |

