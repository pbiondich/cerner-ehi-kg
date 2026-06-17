# BILLING_ENTITY_GROUP_RELTN

> This table stores the relationship between billing entity and billing entity group.

**Description:** Billing Entity Group Relationship  
**Table type:** REFERENCE  
**Primary key:** `BILLING_ENTITY_GROUP_RELTN_ID`  
**Columns:** 13  
**Referenced by:** 1 columns

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ACTIVE_IND` | DOUBLE | NOT NULL |  | The table row is active or inactive. A row is generally active unless it is in an inactive state such as logically deleted, combined away, pending purge, etc. |
| 2 | `BEG_EFFECTIVE_DT_TM` | DATETIME | NOT NULL |  | The date and time for which this table row becomes effective. Normally, this will be the date and time the row is added, but could be a past or future date and time. |
| 3 | `BILLING_ENTITY_GROUP_ID` | DOUBLE | NOT NULL | FK→ | Uniquely identifies the related billing entity group. |
| 4 | `BILLING_ENTITY_GROUP_RELTN_ID` | DOUBLE | NOT NULL | PK | Uniquely identifies a relationshipbetweena billing entity and a billing entity group. |
| 5 | `BILLING_ENTITY_ID` | DOUBLE | NOT NULL | FK→ | Uniquely identifies the related billing entity. |
| 6 | `END_EFFECTIVE_DT_TM` | DATETIME | NOT NULL |  | The date/time after which the row is no longer valid as active current data. This may be valued with the date that the row became inactive. |
| 7 | `ORIG_ID` | DOUBLE | NOT NULL | FK→ | Represents the primary key of the original for a group of billing entity relationships. |
| 8 | `PARENT_IND` | DOUBLE | NOT NULL |  | Represents the parent billing entity of a group of billing entities. |
| 9 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 10 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 11 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 12 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 13 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `BILLING_ENTITY_GROUP_ID` | [BILLING_ENTITY_GROUP](BILLING_ENTITY_GROUP.md) | `BILLING_ENTITY_GROUP_ID` |
| `BILLING_ENTITY_ID` | [BILLING_ENTITY](BILLING_ENTITY.md) | `BILLING_ENTITY_ID` |
| `ORIG_ID` | [BILLING_ENTITY_GROUP_RELTN](BILLING_ENTITY_GROUP_RELTN.md) | `BILLING_ENTITY_GROUP_RELTN_ID` |

## Referenced by (1)

| From table | Column |
|------------|--------|
| [BILLING_ENTITY_GROUP_RELTN](BILLING_ENTITY_GROUP_RELTN.md) | `ORIG_ID` |

