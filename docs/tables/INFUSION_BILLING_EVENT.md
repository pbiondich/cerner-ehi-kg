# INFUSION_BILLING_EVENT

> Stores infusion billing event information for a specific order such as the start and stop of the infusion.

**Description:** Infusion Billing Event  
**Table type:** ACTIVITY  
**Primary key:** `INFUSION_BILLING_EVENT_ID`  
**Columns:** 20  
**Referenced by:** 2 columns

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ACTIVE_IND` | DOUBLE | NOT NULL |  | The table row is active or inactive. A row is generally active unless it is in an inactive state such as logically deleted, combined away, pending purge, etc. |
| 2 | `BEGIN_EFFECTIVE_DT_TM` | DATETIME | NOT NULL |  | Date and time when the row became valid. |
| 3 | `COMMENT_LONG_TEXT_ID` | DOUBLE | NOT NULL | FK→ | Reference to a long text table that holds a comment entered during the infusion documentation process. |
| 4 | `CREATE_PRSNL_ID` | DOUBLE | NOT NULL | FK→ | Id of the person who entered the infusion record. |
| 5 | `ENCNTR_ID` | DOUBLE | NOT NULL | FK→ | The encounter associated with the billing event. |
| 6 | `END_EFFECTIVE_DT_TM` | DATETIME | NOT NULL |  | The date/time after which the row is no longer valid as active current data. This may be valued with the date that the row became inactive. |
| 7 | `INFUSED_VOLUME_VALUE` | DOUBLE | NOT NULL |  | The volume in mL that was infused for this infusion event. |
| 8 | `INFUSION_BILLING_EVENT_ID` | DOUBLE | NOT NULL | PK | Unique, generated number that identifies a single row on the INFUSION_BILLING_EVENT table. |
| 9 | `INFUSION_DURATION_MINS` | DOUBLE | NOT NULL |  | A value in minutes that represents the actual infusion time. This may be different from the time period between the infusion start and stop if there are short pauses in the administration. |
| 10 | `INFUSION_END_DT_TM` | DATETIME | NOT NULL |  | The date and time representing the end of the infusion. |
| 11 | `INFUSION_END_TZ` | DOUBLE | NOT NULL |  | Time zone associated with the infusion end date and time. |
| 12 | `INFUSION_START_DT_TM` | DATETIME | NOT NULL |  | The date and time representing the start of the infusion. |
| 13 | `INFUSION_START_TZ` | DOUBLE | NOT NULL |  | Time zone associated with the infusion start date and time. |
| 14 | `ORDER_ID` | DOUBLE | NOT NULL | FK→ | The order associated with the billing event. |
| 15 | `PREV_INFUSION_BILLING_EVENT_ID` | DOUBLE | NOT NULL | FK→ | The infusion billing id for the latest version of a given infusion record. |
| 16 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 17 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 18 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 19 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 20 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `COMMENT_LONG_TEXT_ID` | [LONG_TEXT](LONG_TEXT.md) | `LONG_TEXT_ID` |
| `CREATE_PRSNL_ID` | [PRSNL](PRSNL.md) | `PERSON_ID` |
| `ENCNTR_ID` | [ENCOUNTER](ENCOUNTER.md) | `ENCNTR_ID` |
| `ORDER_ID` | [ORDERS](ORDERS.md) | `ORDER_ID` |
| `PREV_INFUSION_BILLING_EVENT_ID` | [INFUSION_BILLING_EVENT](INFUSION_BILLING_EVENT.md) | `INFUSION_BILLING_EVENT_ID` |

## Referenced by (2)

| From table | Column |
|------------|--------|
| [INFUSION_BILLING_EVENT](INFUSION_BILLING_EVENT.md) | `PREV_INFUSION_BILLING_EVENT_ID` |
| [INFUSION_CE_RELTN](INFUSION_CE_RELTN.md) | `INFUSION_BILLING_EVENT_ID` |

