# PATHWAY_CUSTOMIZED_NOTIFY

> This table stores the notifications for pathway_customized_plan

**Description:** PATHWAY CUSTOMIZED NOTIFICATIONS  
**Table type:** REFERENCE  
**Primary key:** _(not published — see note)_  
**Columns:** 12

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ACTIVE_IND` | DOUBLE | NOT NULL |  | The table row is active or inactive. A row is generally active unless it is in an inactive state such as logically deleted, combined away, pending purge, etc. |
| 2 | `LONG_TEXT_ID` | DOUBLE | NOT NULL | FK→ | The long text ID from long text reference of the text for the notification |
| 3 | `NOTIFICATION_DT_TM` | DATETIME | NOT NULL |  | The date and time of the notification |
| 4 | `PATHWAY_CATALOG_ID` | DOUBLE | NOT NULL | FK→ | The pathway catalog ID of the plan that this notification is for. |
| 5 | `PATHWAY_CUSTOMIZED_NOTIFY_ID` | DOUBLE | NOT NULL |  | The primary key of this table |
| 6 | `PATHWAY_CUSTOMIZED_PLAN_ID` | DOUBLE | NOT NULL | FK→ | The pathway customized plan ID of the customized plan that this notification is for. |
| 7 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 8 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 9 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 10 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 11 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |
| 12 | `VERSION_PW_CAT_ID` | DOUBLE | NOT NULL | FK→ | The version pathway catalog ID of the plan that this notification is for |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `LONG_TEXT_ID` | [LONG_TEXT_REFERENCE](LONG_TEXT_REFERENCE.md) | `LONG_TEXT_ID` |
| `PATHWAY_CATALOG_ID` | [PATHWAY_CATALOG](PATHWAY_CATALOG.md) | `PATHWAY_CATALOG_ID` |
| `PATHWAY_CUSTOMIZED_PLAN_ID` | [PATHWAY_CUSTOMIZED_PLAN](PATHWAY_CUSTOMIZED_PLAN.md) | `PATHWAY_CUSTOMIZED_PLAN_ID` |
| `VERSION_PW_CAT_ID` | [PATHWAY_CATALOG](PATHWAY_CATALOG.md) | `PATHWAY_CATALOG_ID` |

