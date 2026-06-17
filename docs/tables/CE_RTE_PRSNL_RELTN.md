# CE_RTE_PRSNL_RELTN

> Stores the provider information to whom notifications are sent for RTE.

**Description:** Clinical Event Results To Endorsement Personnel Relation  
**Table type:** ACTIVITY  
**Primary key:** _(not published — see note)_  
**Columns:** 9

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ACTION_PRSNL_ID` | DOUBLE | NOT NULL | FK→ | The personnel who carried out the action. |
| 2 | `CE_EVENT_ACTION_ID` | DOUBLE | NOT NULL | FK→ | The clinical event action that this notification was sent for. |
| 3 | `CE_RTE_PRSNL_RELTN_ID` | DOUBLE | NOT NULL |  | Unique generated number that identifies a single row on the CE_RTE_PRSNL_RELTN table. |
| 4 | `RELTN_TYPE_CD` | DOUBLE | NOT NULL |  | This defines the relationship between person and provider. Example: Attending Provider. CodeSet: 331 or 333. |
| 5 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 6 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 7 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 8 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 9 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `ACTION_PRSNL_ID` | [PRSNL](PRSNL.md) | `PERSON_ID` |
| `CE_EVENT_ACTION_ID` | [CE_EVENT_ACTION](CE_EVENT_ACTION.md) | `CE_EVENT_ACTION_ID` |

