# SA_ACTION_ITEM

> Documents additional information about an instance of an action Based on the number of actions that are documented during a case. Estimate 2:1 with SA_ACTION. 522,000

**Description:** SN Action Item  
**Table type:** ACTIVITY  
**Primary key:** _(not published — see note)_  
**Columns:** 17

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ACTION_VALUE` | VARCHAR(250) |  |  | The value associated with this action item |
| 2 | `ACTIVE_IND` | DOUBLE | NOT NULL |  | The table row is active or inactive. A row is generally active unless it is in an inactive state such as logically deleted, combined away, pending purge, etc. |
| 3 | `ACTIVE_STATUS_CD` | DOUBLE | NOT NULL |  | Indicates the status of the row itself (not the data in the row) such as active, inactive, combined away, pending purge, etc. |
| 4 | `ACTIVE_STATUS_DT_TM` | DATETIME | NOT NULL |  | The date and time that the active_status_cd was set. |
| 5 | `ACTIVE_STATUS_PRSNL_ID` | DOUBLE | NOT NULL |  | The person who caused the active_status_cd to be set or change. |
| 6 | `LONG_TEXT_ID` | DOUBLE | NOT NULL |  | The long_text record that contains the comment for this action item |
| 7 | `PRSNL_ID` | DOUBLE | NOT NULL | FK→ | The user who documented the action item, if 0, added by a macro |
| 8 | `SA_ACTION_ID` | DOUBLE | NOT NULL | FK→ | The action that this action item is documenting |
| 9 | `SA_ACTION_ITEM_ID` | DOUBLE | NOT NULL |  | Unique value that identifies the action item |
| 10 | `SA_ITEM_USAGE_ID` | DOUBLE | NOT NULL | FK→ | The item usage record created from this action item value |
| 11 | `SA_MACRO_ID` | DOUBLE | NOT NULL | FK→ | Ties to the macro that added the action item to the anesthesia record, if 0, added by user |
| 12 | `SA_REF_ACTION_ITEM_ID` | DOUBLE | NOT NULL | FK→ | The action item that this is documenting |
| 13 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 14 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 15 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 16 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 17 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `PRSNL_ID` | [PRSNL](PRSNL.md) | `PERSON_ID` |
| `SA_ACTION_ID` | [SA_ACTION](SA_ACTION.md) | `SA_ACTION_ID` |
| `SA_ITEM_USAGE_ID` | [SA_ITEM_USAGE](SA_ITEM_USAGE.md) | `SA_ITEM_USAGE_ID` |
| `SA_MACRO_ID` | [SA_MACRO](SA_MACRO.md) | `SA_MACRO_ID` |
| `SA_REF_ACTION_ITEM_ID` | [SA_REF_ACTION_ITEM](SA_REF_ACTION_ITEM.md) | `SA_REF_ACTION_ITEM_ID` |

