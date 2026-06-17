# CE_DRAFT_RELTN

> Stores the relationship linking a clinical event to a draft.

**Description:** Clinical Event Draft Relation  
**Table type:** ACTIVITY  
**Primary key:** _(not published — see note)_  
**Columns:** 8

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `CE_DRAFT_ID` | DOUBLE | NOT NULL | FK→ | The Draft that is related to this clinical_event. |
| 2 | `CE_DRAFT_RELTN_ID` | DOUBLE | NOT NULL |  | Unique, generated number that identifies a single row on the CE_DRAFT_RELTN table. |
| 3 | `EVENT_ID` | DOUBLE | NOT NULL |  | The Event that this draft is associated to. |
| 4 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 5 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 6 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 7 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 8 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `CE_DRAFT_ID` | [CE_DRAFT](CE_DRAFT.md) | `CE_DRAFT_ID` |

