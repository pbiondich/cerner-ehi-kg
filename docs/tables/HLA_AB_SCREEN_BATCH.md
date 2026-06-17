# HLA_AB_SCREEN_BATCH

> Relates a unique HLA antibody screen batch number to the inventory lot and HLA antibody screen tray map selected for the batch.

**Description:** HLA Antibody Screen Batch  
**Table type:** ACTIVITY  
**Primary key:** `BATCH_ID`  
**Columns:** 12  
**Referenced by:** 4 columns

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `BATCH_DESC` | VARCHAR(30) |  |  | A user assigned description which uniquely identifies an Antibody Screen batch. |
| 2 | `BATCH_ID` | DOUBLE | NOT NULL | PK | A sequentially assigned number which uniquely identifies an Antibody Screen batch. |
| 3 | `BATCH_NUMBER` | DOUBLE |  |  | A sequentially assigned number which uniquely identifies an Antibody Screen batch. |
| 4 | `DOWNLOAD_DT_TM` | DATETIME |  |  | The date and time that the batch was downloaded. |
| 5 | `DOWNLOAD_PRSNL_ID` | DOUBLE | NOT NULL |  | The ID of the user who downloaded the batch. |
| 6 | `FILL_METHOD_FLAG` | DOUBLE | NOT NULL |  | Flag to record whether an antibody screen batch was filled by column. 0 = filled by row; 1 = filled by column |
| 7 | `LOT_NUMBER_ID` | DOUBLE | NOT NULL | FK→ | Identifies the inventory lot of the Antibody Screen used for this batch. It is a foreign key reference to the primary key of the lot_number_info table. |
| 8 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 9 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 10 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 11 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 12 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `LOT_NUMBER_ID` | [LOT_NUMBER_INFO](LOT_NUMBER_INFO.md) | `LOT_NUMBER_ID` |

## Referenced by (4)

| From table | Column |
|------------|--------|
| [HLA_AB_SCREEN_RESULT](HLA_AB_SCREEN_RESULT.md) | `BATCH_ID` |
| [HLA_AB_SCREEN_WELL_SCORE](HLA_AB_SCREEN_WELL_SCORE.md) | `BATCH_ID` |
| [HLA_SCREEN_ANALYSIS](HLA_SCREEN_ANALYSIS.md) | `BATCH_ID` |
| [HLA_X_SPECIMEN_DETAIL](HLA_X_SPECIMEN_DETAIL.md) | `BATCH_ID` |

