# PFT_QUEUE_ITEM_WF_RELTN

> This table stores additional metadata related to work items.

**Description:** ProFit Queue Item Work Flow Relationship  
**Table type:** ACTIVITY  
**Primary key:** _(not published — see note)_  
**Columns:** 9

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `PARENT_ENTITY_ID` | DOUBLE | NOT NULL |  | Contains the identity of the row in the parent entity table that is related to this queue item. |
| 2 | `PARENT_ENTITY_NAME` | VARCHAR(30) | NOT NULL |  | Uniquely identifies the name of the table related to this queue item. |
| 3 | `PFT_QUEUE_ITEM_WF_HIST_ID` | DOUBLE | NOT NULL | FK→ | Uniquely identifies the related queue item wf history row involved in this relationship. |
| 4 | `PFT_QUEUE_ITEM_WF_RELTN_ID` | DOUBLE | NOT NULL |  | Uniquely identifies metadata related to work items. |
| 5 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 6 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 7 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 8 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 9 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `PFT_QUEUE_ITEM_WF_HIST_ID` | [PFT_QUEUE_ITEM_WF_HIST](PFT_QUEUE_ITEM_WF_HIST.md) | `PFT_QUEUE_ITEM_WF_HIST_ID` |

