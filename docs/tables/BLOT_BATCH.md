# BLOT_BATCH

> Relates a unique Blot Batch to the inventory lot.

**Description:** Blot Batch  
**Table type:** ACTIVITY  
**Primary key:** `BLOT_BATCH_ID`  
**Columns:** 11  
**Referenced by:** 1 columns

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `BLOT_BATCH_DESC` | VARCHAR(30) |  |  | The description of the Blot Batch. |
| 2 | `BLOT_BATCH_ID` | DOUBLE | NOT NULL | PK | Unique Identifier for the Blot Batch |
| 3 | `DOWNLOAD_DT_TM` | DATETIME |  |  | The date and time the batch was downloaded. |
| 4 | `DOWNLOAD_PRSNL_ID` | DOUBLE | NOT NULL |  | The ID of the user who downloaded the batch. |
| 5 | `FILL_COLUMN_IND` | DOUBLE | NOT NULL |  | Indicator to record whether a blot batch was filled by column.0 - filled by row1 - filled by column |
| 6 | `LOT_NUMBER_ID` | DOUBLE | NOT NULL | FK→ | Identifies the inventory lot of the Antibody Screen used for this batch. It is a foreign key reference to the primary key of the lot_number_info table. |
| 7 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 8 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 9 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 10 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 11 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `LOT_NUMBER_ID` | [LOT_NUMBER_INFO](LOT_NUMBER_INFO.md) | `LOT_NUMBER_ID` |

## Referenced by (1)

| From table | Column |
|------------|--------|
| [BLOT_BATCH_RESULT](BLOT_BATCH_RESULT.md) | `BLOT_BATCH_ID` |

