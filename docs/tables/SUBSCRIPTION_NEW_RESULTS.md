# SUBSCRIPTION_NEW_RESULTS

> New results associated to a subscription

**Description:** Clinical Event Subscription new results  
**Table type:** ACTIVITY  
**Primary key:** `SUBSCRIPTION_NEW_RESULTS_ID`  
**Columns:** 13  
**Referenced by:** 1 columns

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `CLINSIG_UPDT_DT_TM` | DATETIME | NOT NULL |  | The Date and Time the new result was created and/or had a clinically significant update occur. This corresponds to the CLINICAL_EVENT table's clinsig_updt_dt_tm field. |
| 2 | `CREATED_DT_TM` | DATETIME | NOT NULL |  | The Date and Time the new result was created. |
| 3 | `EVENT_CLASS_CD` | DOUBLE | NOT NULL |  | Coded value which specifies how the event is stored in and retrieved from the event table sub-tables |
| 4 | `EVENT_ID` | DOUBLE | NOT NULL |  | The ID of the clinical event associated to the new result. |
| 5 | `EXPIRATION_DT_TM` | DATETIME | NOT NULL |  | The Date and Time the new result is set to expire. This field will determine when the new result is to be purged. |
| 6 | `SUBSCRIPTION_ID` | DOUBLE | NOT NULL | FK→ | Unique, generated number that is used to identify an individual row on the SUBSCRIPTION table. |
| 7 | `SUBSCRIPTION_NEW_RESULTS_ID` | DOUBLE | NOT NULL | PK | Unique, generated number that is used to identify an individual row on the CE_NEW_RESULTS table. |
| 8 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 9 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 10 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 11 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 12 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |
| 13 | `VIEW_STATUS_CD` | DOUBLE | NOT NULL |  | This is the state in which the physician will like to view the result in future interactions. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `SUBSCRIPTION_ID` | [SUBSCRIPTION](SUBSCRIPTION.md) | `SUBSCRIPTION_ID` |

## Referenced by (1)

| From table | Column |
|------------|--------|
| [SUBSCRPTN_FILTER_RESULTS_RELTN](SUBSCRPTN_FILTER_RESULTS_RELTN.md) | `SUBSCRIPTION_NEW_RESULTS_ID` |

