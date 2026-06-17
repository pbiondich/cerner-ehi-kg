# SCH_PEND_SURG_ITEM

> Surgical items related to an appointment draft.

**Description:** Scheduling Pending Surgical Item  
**Table type:** ACTIVITY  
**Primary key:** _(not published — see note)_  
**Columns:** 13

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `CHANGE_FLAG` | DOUBLE |  |  | Whether the preference card is schedulable. |
| 2 | `HOLD_QTY` | DOUBLE |  |  | Quantity of items to mark as ON-HOLD. |
| 3 | `ITEM_ID` | DOUBLE |  | FK→ | The item to be associated with the surgical appointment. |
| 4 | `LIST_ROLE_ID` | DOUBLE |  | FK→ | List role identifier associated to the preference card. |
| 5 | `OPEN_QTY` | DOUBLE |  |  | Quantity of items to mark as open. |
| 6 | `PREF_CARD_ID` | DOUBLE |  | FK→ | Preference card identifier associated to the draft order or orderable. |
| 7 | `SCH_PEND_ORDER_ID` | DOUBLE |  | FK→ | Unique identifier for the draft order or orderable |
| 8 | `SCH_PEND_SURG_ITEM_ID` | DOUBLE | NOT NULL |  | Unique generated number that identifies a single row on the SCH_PEND_SURG_ITEM table.; |
| 9 | `UPDT_APPLCTX` | DOUBLE |  |  | The application context number from the record info block. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 10 | `UPDT_CNT` | DOUBLE |  |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 11 | `UPDT_DT_TM` | DATETIME |  |  | The date and time the row was last inserted or updated. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 12 | `UPDT_ID` | DOUBLE |  |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 13 | `UPDT_TASK` | DOUBLE |  |  | The registered (assigned) task number for the process that inserted or updated the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `ITEM_ID` | [ITEM_DEFINITION](ITEM_DEFINITION.md) | `ITEM_ID` |
| `LIST_ROLE_ID` | [SCH_LIST_ROLE](SCH_LIST_ROLE.md) | `LIST_ROLE_ID` |
| `PREF_CARD_ID` | [PREFERENCE_CARD](PREFERENCE_CARD.md) | `PREF_CARD_ID` |
| `SCH_PEND_ORDER_ID` | [SCH_PEND_ORDER](SCH_PEND_ORDER.md) | `SCH_PEND_ORDER_ID` |

