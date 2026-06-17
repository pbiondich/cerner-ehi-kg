# SUBSCRIPTION

> Subscription information

**Description:** Subscription  
**Table type:** ACTIVITY  
**Primary key:** `SUBSCRIPTION_ID`  
**Columns:** 11  
**Referenced by:** 2 columns

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ENCOUNTER_ID` | DOUBLE | NOT NULL | FK→ | The ENCNTR_ID from the Encounter related to this subscriptoin |
| 2 | `EXPIRATION_DT_TM` | DATETIME | NOT NULL |  | The Date and Time the subscription is set to expire. |
| 3 | `PERSON_ID` | DOUBLE | NOT NULL | FK→ | The ID of the Patient whom the Provider has a subscription with. |
| 4 | `PROVIDER_ID` | DOUBLE | NOT NULL |  | The ID of the Provider associated to the subscription. |
| 5 | `SUBSCRIPTION_ID` | DOUBLE | NOT NULL | PK | Unique, generated number that is used to identify an individual row on the SUBSCRIPTION table. |
| 6 | `SUBSCRIPTION_TYPE_FLAG` | DOUBLE | NOT NULL |  | Identifies the type of subscription. Current values are 1 = (Message Center and 2 = IView." |
| 7 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 8 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 9 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 10 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 11 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `ENCOUNTER_ID` | [ENCOUNTER](ENCOUNTER.md) | `ENCNTR_ID` |
| `PERSON_ID` | [PERSON](PERSON.md) | `PERSON_ID` |

## Referenced by (2)

| From table | Column |
|------------|--------|
| [SUBSCRIPTION_FILTER_MSG](SUBSCRIPTION_FILTER_MSG.md) | `SUBSCRIPTION_ID` |
| [SUBSCRIPTION_NEW_RESULTS](SUBSCRIPTION_NEW_RESULTS.md) | `SUBSCRIPTION_ID` |

