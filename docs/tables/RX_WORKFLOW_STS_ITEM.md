# RX_WORKFLOW_STS_ITEM

> Stores the child items of a workflow event that is not specific to a patient's dispense.

**Description:** Pharmacy Workflow Status Item  
**Table type:** ACTIVITY  
**Primary key:** _(not published — see note)_  
**Columns:** 9

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ITEM_ID` | DOUBLE | NOT NULL | FK→ | The item used in the workflow event. |
| 2 | `ITEM_QTY` | DOUBLE | NOT NULL |  | The quantity of the item needed to satisfy the Workflow event. |
| 3 | `RX_WORKFLOW_STS_ID` | DOUBLE | NOT NULL | FK→ | The workflow event this item belongs to. Foreign key to the RX_WORKFLOW_STS table. |
| 4 | `RX_WORKFLOW_STS_ITEM_ID` | DOUBLE | NOT NULL |  | Unique, generated number that identifies a single row in the RX_WORKFLOW_STS_ITEM table. |
| 5 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 6 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 7 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 8 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 9 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `ITEM_ID` | [MEDICATION_DEFINITION](MEDICATION_DEFINITION.md) | `ITEM_ID` |
| `RX_WORKFLOW_STS_ID` | [RX_WORKFLOW_STS](RX_WORKFLOW_STS.md) | `RX_WORKFLOW_STS_ID` |

