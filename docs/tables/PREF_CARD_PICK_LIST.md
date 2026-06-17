# PREF_CARD_PICK_LIST

> Contains the items on the preference card pick list

**Description:** Preference Card Pick List  
**Table type:** REFERENCE  
**Primary key:** _(not published — see note)_  
**Columns:** 25

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ACTIVE_IND` | DOUBLE |  |  | The table row is active or inactive. A row is generally active unless it is in an inactive state such as logically deleted, combined away, pending purge, etc. |
| 2 | `ACTIVE_STATUS_CD` | DOUBLE | NOT NULL |  | Indicates the status of the row itself (not the data in the row) such as active, inactive, combined away, pending purge, etc. |
| 3 | `ACTIVE_STATUS_DT_TM` | DATETIME |  |  | The date and time that the active_status_cd was set. |
| 4 | `ACTIVE_STATUS_PRSNL_ID` | DOUBLE | NOT NULL |  | The person who caused the active_status_cd to be set or change. |
| 5 | `BEG_EFFECTIVE_DT_TM` | DATETIME | NOT NULL |  | The date and time for which this table row becomes effective. Normally, this will be the date and time the row is added, but could be a past or future date and time. |
| 6 | `CREATE_APPLCTX` | DOUBLE |  |  | Create Application ContextColumn |
| 7 | `CREATE_DT_TM` | DATETIME |  |  | Create Date and TimeColumn |
| 8 | `CREATE_PRSNL_ID` | DOUBLE | NOT NULL |  | Create Personnel IDColumn |
| 9 | `CREATE_TASK` | DOUBLE |  |  | Create TaskColumn |
| 10 | `END_EFFECTIVE_DT_TM` | DATETIME | NOT NULL |  | The date/time after which the row is no longer valid as active current data. This may be valued with the date that the row became inactive. |
| 11 | `INVALID_ORG_ASSOC_IND` | DOUBLE | NOT NULL |  | Indicates whether the item's organization association is valid for prefcard's organization |
| 12 | `ITEM_ID` | DOUBLE | NOT NULL | FK→ | Item Id of the Item on the Item Definition Table |
| 13 | `PARENT_ENTITY_ID` | DOUBLE | NOT NULL |  | *** OBSOLETE ***Column |
| 14 | `PARENT_ENTITY_NAME` | VARCHAR(32) |  |  | *** OBSOLETE ***Column |
| 15 | `PARENT_PACK_ID` | DOUBLE | NOT NULL |  | *** OBSOLETE ***Column |
| 16 | `PREF_CARD_ID` | DOUBLE | NOT NULL | FK→ | A reference (foreign key) to the PREFERENCE_CARD table indicating the preference card this pick list item is associated with. |
| 17 | `PREF_CARD_PICK_LIST_ID` | DOUBLE | NOT NULL |  | The primary key, uniquely identifying a preference card pick list item |
| 18 | `REQUEST_HOLD_QTY` | DOUBLE |  |  | The requested hold quantity for this pick list item |
| 19 | `REQUEST_OPEN_QTY` | DOUBLE |  |  | The requested open quantity for this pick list item |
| 20 | `SCHED_ITEM_IND` | DOUBLE |  |  | *** OBSOLETE ***Column |
| 21 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 22 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 23 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 24 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 25 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `ITEM_ID` | [ITEM_DEFINITION](ITEM_DEFINITION.md) | `ITEM_ID` |
| `PREF_CARD_ID` | [PREFERENCE_CARD](PREFERENCE_CARD.md) | `PREF_CARD_ID` |

