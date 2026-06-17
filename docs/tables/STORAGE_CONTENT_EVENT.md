# STORAGE_CONTENT_EVENT

> Describes te events for inventory content of a storage item.

**Description:** Storage Content Event  
**Table type:** ACTIVITY  
**Primary key:** _(not published — see note)_  
**Columns:** 19

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ACTION_CD` | DOUBLE | NOT NULL |  | The action that has been performed on the inventory for the given event. |
| 2 | `ACTION_DT_TM` | DATETIME | NOT NULL |  | Date and time the action occurred |
| 3 | `ACTION_PRSNL_ID` | DOUBLE | NOT NULL |  | Id of the person who performed the action |
| 4 | `BEG_EFFECTIVE_DT_TM` | DATETIME | NOT NULL |  | The date and time for which this table row becomes effective. Normally, this will be the date and time the row is added, but could be a past or future date and time. |
| 5 | `COMMENT_ID` | DOUBLE | NOT NULL | FK→ | The identifier of the comment recorded with the event that occurred. |
| 6 | `CONTENT_STATUS_CD` | DOUBLE | NOT NULL |  | The status of the storge content within the storage item after the event has occurred. |
| 7 | `DESTINATION_CD` | DOUBLE | NOT NULL |  | The destination for the storage content. |
| 8 | `DISPOSAL_REASON_CD` | DOUBLE | NOT NULL |  | The reason why the storage content was disposed. |
| 9 | `END_EFFECTIVE_DT_TM` | DATETIME | NOT NULL |  | The date/time after which the row is no longer valid as active current data. This may be valued with the date that the row became inactive. |
| 10 | `STATION_CD` | DOUBLE | NOT NULL |  | The station used to perform the event on the inventory. |
| 11 | `STORAGE_CONTENT_EVENT_ID` | DOUBLE | NOT NULL |  | Uniquely identifies and describes the events for inventory content of a storage item. |
| 12 | `STORAGE_CONTENT_ID` | DOUBLE | NOT NULL |  | Uniquely identifies the storage content to which this event applies. |
| 13 | `STORAGE_ITEM_CD` | DOUBLE | NOT NULL | FK→ | This field contains the code of the storage item containing the storage content for this event. |
| 14 | `STORAGE_ITEM_CELL_ID` | DOUBLE | NOT NULL | FK→ | Contains the identifier of the cell of the storage item that contains the storage content for this event. |
| 15 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 16 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 17 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 18 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 19 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `COMMENT_ID` | [LONG_TEXT](LONG_TEXT.md) | `LONG_TEXT_ID` |
| `STORAGE_ITEM_CD` | [STORAGE_ITEM](STORAGE_ITEM.md) | `STORAGE_ITEM_CD` |
| `STORAGE_ITEM_CELL_ID` | [STORAGE_ITEM_CELL](STORAGE_ITEM_CELL.md) | `STORAGE_ITEM_CELL_ID` |

