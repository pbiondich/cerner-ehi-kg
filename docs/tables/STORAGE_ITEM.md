# STORAGE_ITEM

> Storage Item

**Description:** PathNet Storage Tracking reference table storing trays and racks.  
**Table type:** REFERENCE  
**Primary key:** `STORAGE_ITEM_CD`  
**Columns:** 9  
**Referenced by:** 2 columns

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `EMPTY_IND` | DOUBLE | NOT NULL |  | An indicator set to 1 if the given rack or tray is empty. |
| 2 | `STORAGE_ITEM_CD` | DOUBLE | NOT NULL | PK FK→ | Unique identifier for the given rack or tray. |
| 3 | `STORAGE_ITEM_DESCRIPTION_CD` | DOUBLE | NOT NULL |  | Determines what type of tray or what type of rack. |
| 4 | `STORAGE_TYPE_CD` | DOUBLE | NOT NULL |  | Location type (either tray or rack) |
| 5 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 6 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 7 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 8 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 9 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `STORAGE_ITEM_CD` | [CODE_VALUE](CODE_VALUE.md) | `CODE_VALUE` |

## Referenced by (2)

| From table | Column |
|------------|--------|
| [STORAGE_CONTENT](STORAGE_CONTENT.md) | `STORAGE_ITEM_CD` |
| [STORAGE_CONTENT_EVENT](STORAGE_CONTENT_EVENT.md) | `STORAGE_ITEM_CD` |

