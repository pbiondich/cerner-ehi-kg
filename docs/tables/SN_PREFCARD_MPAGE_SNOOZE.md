# SN_PREFCARD_MPAGE_SNOOZE

> SurgiNet Preference Card MPage Snooze Table

**Description:** sn_pref_card_mpage_snooze  
**Table type:** ACTIVITY  
**Primary key:** _(not published — see note)_  
**Columns:** 12

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ACTION_FLAG` | DOUBLE | NOT NULL |  | action snoozed: 0 - modify, 1 - add, 2 - remove |
| 2 | `CREATE_DT_TM` | DATETIME |  |  | date time user snoozed the action |
| 3 | `EXPIRATION_DT_TM` | DATETIME |  |  | date snooze expires |
| 4 | `ITEM_ID` | DOUBLE | NOT NULL | FK→ | item being snoozed on prefcard by user |
| 5 | `PREF_CARD_ID` | DOUBLE | NOT NULL | FK→ | prefcard having item snoozed by user |
| 6 | `SN_PREFCARD_MPAGE_SNOOZE_ID` | DOUBLE | NOT NULL |  | Unique generated number that identifies a single row on the table. Primary Key. |
| 7 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 8 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 9 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 10 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 11 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |
| 12 | `USER_ID` | DOUBLE | NOT NULL | FK→ | user snoozing action on item on prefcard |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `ITEM_ID` | [ITEM_MASTER](ITEM_MASTER.md) | `ITEM_ID` |
| `PREF_CARD_ID` | [PREFERENCE_CARD](PREFERENCE_CARD.md) | `PREF_CARD_ID` |
| `USER_ID` | [PRSNL](PRSNL.md) | `PERSON_ID` |

