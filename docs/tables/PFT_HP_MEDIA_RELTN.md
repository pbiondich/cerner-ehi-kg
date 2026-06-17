# PFT_HP_MEDIA_RELTN

> Stores media types needed for each Health_Plan instead of firing off a rule every time we gen a claim to see what media type it goes out on.

**Description:** Stores media types needed for each Health_Plan instead of firing off a rule.  
**Table type:** REFERENCE  
**Primary key:** _(not published — see note)_  
**Columns:** 20

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ACTIVE_IND` | DOUBLE |  |  | The table row is active or inactive. A row is generally active unless it is in an inactive state such as logically deleted, combined away, pending purge, etc. |
| 2 | `ACTIVE_STATUS_CD` | DOUBLE | NOT NULL |  | Indicates the status of the row itself (not the data in the row) such as active, inactive, combined away, pending purge, etc. |
| 3 | `ACTIVE_STATUS_DT_TM` | DATETIME |  |  | The date and time that the active_status_cd was set. |
| 4 | `ACTIVE_STATUS_PRSNL_ID` | DOUBLE | NOT NULL |  | The person who caused the active_status_cd to be set or change. |
| 5 | `BATCH_ROUTE_IDENT` | VARCHAR(100) | NOT NULL |  | Identifies the batch route used to send electronic claims. |
| 6 | `BEG_EFFECTIVE_DT_TM` | DATETIME | NOT NULL |  | The date and time for which this table row becomes effective. Normally, this will be the date and time the row is added, but could be a past or future date and time. |
| 7 | `BILLING_ENTITY_ID` | DOUBLE | NOT NULL | FK→ | Foreign key to the Billing Entity table |
| 8 | `BILL_TYPE_CD` | DOUBLE | NOT NULL |  | Code value for the bill type |
| 9 | `END_EFFECTIVE_DT_TM` | DATETIME | NOT NULL |  | The date/time after which the row is no longer valid as active current data. This may be valued with the date that the row became inactive. |
| 10 | `MEDIA_SUB_TYPE_CD` | DOUBLE | NOT NULL |  | The Media sub type of the claim. |
| 11 | `MEDIA_TYPE_CD` | DOUBLE | NOT NULL |  | Media type code from code set |
| 12 | `PARENT_ENTITY_ID` | DOUBLE | NOT NULL |  | Id to the table identified in parent entity name |
| 13 | `PARENT_ENTITY_NAME` | VARCHAR(250) | NOT NULL |  | Table referenced by the parent entity id |
| 14 | `PFT_HP_MEDIA_RELTN_ID` | DOUBLE | NOT NULL |  | Unique identifier of this table |
| 15 | `PRIORITY_SEQ` | DOUBLE | NOT NULL |  | The sequence of the priority for this row |
| 16 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 17 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 18 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 19 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 20 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `BILLING_ENTITY_ID` | [BILLING_ENTITY](BILLING_ENTITY.md) | `BILLING_ENTITY_ID` |

