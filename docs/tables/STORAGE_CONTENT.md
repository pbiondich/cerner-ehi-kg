# STORAGE_CONTENT

> Describes the inventory content of a storage item.

**Description:** Storage Content  
**Table type:** ACTIVITY  
**Primary key:** _(not published — see note)_  
**Columns:** 14

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `CONTENT_STATUS_CD` | DOUBLE | NOT NULL |  | The current status of the storage content within the storage item. |
| 2 | `CONTENT_TABLE_ID` | DOUBLE | NOT NULL |  | This field contains the foreign key identifier to content information stored on the table named by the content table name. |
| 3 | `CONTENT_TABLE_NAME` | VARCHAR(30) | NOT NULL |  | This field contains the table name of content information stored on the table named in the field. |
| 4 | `EXPECTED_RETURN_DT_TM` | DATETIME |  |  | The date and time when the content is expected to be returned to storage. |
| 5 | `STORAGE_CONTENT_ID` | DOUBLE | NOT NULL |  | Uniquely identifies the inventory content of a storage item. |
| 6 | `STORAGE_ITEM_CD` | DOUBLE | NOT NULL | FK→ | Uniquely identifies the storage item related to the storage content. |
| 7 | `STORAGE_ITEM_CELL_ID` | DOUBLE | NOT NULL | FK→ | This field contains the foreign key value to the storage_item_cell table for the last storage item cell containing the storage content. |
| 8 | `SUGGESTED_DISCARD_DT_TM` | DATETIME |  |  | The suggested date and time for the content to be discarded. |
| 9 | `TRACKING_LOCATION_CD` | DOUBLE | NOT NULL |  | The destination to which the content has been tracked. |
| 10 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 11 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 12 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 13 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 14 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `STORAGE_ITEM_CD` | [STORAGE_ITEM](STORAGE_ITEM.md) | `STORAGE_ITEM_CD` |
| `STORAGE_ITEM_CELL_ID` | [STORAGE_ITEM_CELL](STORAGE_ITEM_CELL.md) | `STORAGE_ITEM_CELL_ID` |

