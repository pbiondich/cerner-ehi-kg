# SA_ACTION

> Contains records that document the anesthesia Actions that exist on an anesthesia record Based on the number of actions that are documented during a case. Estimate 10:1 with SA_ANESTHESIA_RECORD. 261,000

**Description:** SA Actions  
**Table type:** ACTIVITY  
**Primary key:** `SA_ACTION_ID`  
**Columns:** 20  
**Referenced by:** 3 columns

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ACTION_DT_TM` | DATETIME |  |  | Action Date and Time |
| 2 | `ACTION_VALUE` | VARCHAR(250) |  |  | Action Value |
| 3 | `ACTIVE_IND` | DOUBLE | NOT NULL |  | The table row is active or inactive. A row is generally active unless it is in an inactive state such as logically deleted, combined away, pending purge, etc. |
| 4 | `ACTIVE_STATUS_CD` | DOUBLE | NOT NULL |  | Indicates the status of the row itself (not the data in the row) such as active, inactive, combined away, pending purge, etc. |
| 5 | `ACTIVE_STATUS_DT_TM` | DATETIME | NOT NULL |  | The date and time that the active_status_cd was set. |
| 6 | `ACTIVE_STATUS_PRSNL_ID` | DOUBLE | NOT NULL |  | The person who caused the active_status_cd to be set or change. |
| 7 | `EVENT_ID` | DOUBLE | NOT NULL |  | identifier for clinical event row(s) for this action |
| 8 | `LONG_TEXT_ID` | DOUBLE | NOT NULL |  | Long Text ID |
| 9 | `PREV_ACTION_ID` | DOUBLE | NOT NULL | FK→ | Previous SA Action ID |
| 10 | `PRSNL_ID` | DOUBLE | NOT NULL | FK→ | Action Personnel ID |
| 11 | `SA_ACTION_ID` | DOUBLE | NOT NULL | PK | Unique value that identifies the action contained on an anesthesia record |
| 12 | `SA_ANESTHESIA_RECORD_ID` | DOUBLE | NOT NULL | FK→ | The anesthesia record that the action is documented on |
| 13 | `SA_ITEM_USAGE_ID` | DOUBLE | NOT NULL | FK→ | SA ITEM USAGE ID |
| 14 | `SA_MACRO_ID` | DOUBLE | NOT NULL | FK→ | SA MACRO ID |
| 15 | `SA_REF_ACTION_ID` | DOUBLE | NOT NULL | FK→ | SA REFERENCE ACTION ID |
| 16 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 17 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 18 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 19 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 20 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `PREV_ACTION_ID` | [SA_ACTION](SA_ACTION.md) | `SA_ACTION_ID` |
| `PRSNL_ID` | [PRSNL](PRSNL.md) | `PERSON_ID` |
| `SA_ANESTHESIA_RECORD_ID` | [SA_ANESTHESIA_RECORD](SA_ANESTHESIA_RECORD.md) | `SA_ANESTHESIA_RECORD_ID` |
| `SA_ITEM_USAGE_ID` | [SA_ITEM_USAGE](SA_ITEM_USAGE.md) | `SA_ITEM_USAGE_ID` |
| `SA_MACRO_ID` | [SA_MACRO](SA_MACRO.md) | `SA_MACRO_ID` |
| `SA_REF_ACTION_ID` | [SA_REF_ACTION](SA_REF_ACTION.md) | `SA_REF_ACTION_ID` |

## Referenced by (3)

| From table | Column |
|------------|--------|
| [SA_ACTION](SA_ACTION.md) | `PREV_ACTION_ID` |
| [SA_ACTION_ITEM](SA_ACTION_ITEM.md) | `SA_ACTION_ID` |
| [SA_ACTION_SIGNATURE](SA_ACTION_SIGNATURE.md) | `SA_ACTION_ID` |

