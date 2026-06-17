# BILLING_ENTITY_GROUP

> This reference table stores the billing entity groups.

**Description:** Billing Entity Group  
**Table type:** REFERENCE  
**Primary key:** `BILLING_ENTITY_GROUP_ID`  
**Columns:** 11  
**Referenced by:** 4 columns

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ACTIVE_IND` | DOUBLE | NOT NULL |  | The table row is active or inactive. A row is generally active unless it is in an inactive state such as logically deleted, combined away, pending purge, etc. |
| 2 | `BEG_EFFECTIVE_DT_TM` | DATETIME | NOT NULL |  | The date and time for which this table row becomes effective. Normally, this will be the date and time the row is added, but could be a past or future date and time. |
| 3 | `BILLING_ENTITY_GROUP_ID` | DOUBLE | NOT NULL | PK | Uniquely identifies a billing entity group |
| 4 | `END_EFFECTIVE_DT_TM` | DATETIME | NOT NULL |  | The date/time after which the row is no longer valid as active current data. This may be valued with the date that the row became inactive. |
| 5 | `GROUP_NAME` | VARCHAR(250) | NOT NULL |  | Name of the billing entity group |
| 6 | `ORIG_BILLING_ENTITY_GROUP_ID` | DOUBLE | NOT NULL | FK→ | Represents the primary key of the original row for the given billing entity group. |
| 7 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 8 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 9 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 10 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 11 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `ORIG_BILLING_ENTITY_GROUP_ID` | [BILLING_ENTITY_GROUP](BILLING_ENTITY_GROUP.md) | `BILLING_ENTITY_GROUP_ID` |

## Referenced by (4)

| From table | Column |
|------------|--------|
| [BILLING_ENTITY_GROUP](BILLING_ENTITY_GROUP.md) | `ORIG_BILLING_ENTITY_GROUP_ID` |
| [BILLING_ENTITY_GROUP_RELTN](BILLING_ENTITY_GROUP_RELTN.md) | `BILLING_ENTITY_GROUP_ID` |
| [CONS_BO_SCHED](CONS_BO_SCHED.md) | `BILLING_ENTITY_GROUP_ID` |
| [PFT_PAYMENT_PLAN](PFT_PAYMENT_PLAN.md) | `BILLING_ENTITY_GROUP_ID` |

