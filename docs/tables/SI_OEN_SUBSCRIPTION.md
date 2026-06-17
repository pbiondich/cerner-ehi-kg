# SI_OEN_SUBSCRIPTION

> Defines the configured event subscriptions

**Description:** Open engine subscription  
**Table type:** REFERENCE  
**Primary key:** `SI_OEN_SUBSCRIPTION_ID`  
**Columns:** 11  
**Referenced by:** 4 columns

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `BROADCAST_ENABLED_IND` | DOUBLE | NOT NULL |  | Indicator that defines whether the completion of the subscription should send a notification to the Controller service |
| 2 | `EVENT_TYPE` | VARCHAR(100) | NOT NULL |  | The class name of the event the subscription handles |
| 3 | `SI_OEN_SUBSCRIPTION_ID` | DOUBLE | NOT NULL | PK | PRIMARY KEY |
| 4 | `SUBSCRIPTION_PROPERTY_ID` | DOUBLE | NOT NULL | FK→ | ID that links the subscription to its configuration properties |
| 5 | `SUBSCRIPTION_SET_ID` | DOUBLE | NOT NULL | FK→ | ID that links the subscription to the subscription set it belongs to. |
| 6 | `SUBSCRIPTION_TYPE` | VARCHAR(31) | NOT NULL |  | Identifies the row as a subscription or subscription set |
| 7 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 8 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 9 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 10 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 11 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `SUBSCRIPTION_PROPERTY_ID` | [SI_OEN_PROPERTY](SI_OEN_PROPERTY.md) | `SI_OEN_PROPERTY_ID` |
| `SUBSCRIPTION_SET_ID` | [SI_OEN_SUBSCRIPTION](SI_OEN_SUBSCRIPTION.md) | `SI_OEN_SUBSCRIPTION_ID` |

## Referenced by (4)

| From table | Column |
|------------|--------|
| [SI_OEN_COMCHANNEL](SI_OEN_COMCHANNEL.md) | `SI_OEN_SUBSCRIPTION_ID` |
| [SI_OEN_ENDPOINT](SI_OEN_ENDPOINT.md) | `SI_OEN_SUBSCRIPTION_ID` |
| [SI_OEN_SUBSCRIPTION](SI_OEN_SUBSCRIPTION.md) | `SUBSCRIPTION_SET_ID` |
| [SI_OEN_SUBSCRIPTION_STEP_R](SI_OEN_SUBSCRIPTION_STEP_R.md) | `SI_OEN_SUBSCRIPTION_ID` |

