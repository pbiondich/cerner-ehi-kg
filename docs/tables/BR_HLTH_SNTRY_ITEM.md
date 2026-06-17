# BR_HLTH_SNTRY_ITEM

> Data items from Health Sentry.

**Description:** Bedrock Health Sentry Item  
**Table type:** REFERENCE  
**Primary key:** `BR_HLTH_SNTRY_ITEM_ID`  
**Columns:** 15  
**Referenced by:** 1 columns

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `BR_HLTH_SNTRY_ITEM_ID` | DOUBLE | NOT NULL | PK | Unique, generated number that identifies a single row on the BR_HLTH_SNTRY_ITEM table. |
| 2 | `CODE_SET` | DOUBLE | NOT NULL |  | The Millennium code set that this item would map to. |
| 3 | `DESCRIPTION_1` | VARCHAR(255) |  |  | The first description for this item. From health sentry/health facts mapping. |
| 4 | `DESCRIPTION_2` | VARCHAR(255) |  |  | The second description for this item. From health sentry/health facts mapping. |
| 5 | `DESCRIPTION_3` | VARCHAR(255) |  |  | The third description for this item. From health sentry/health facts mapping. |
| 6 | `DESCRIPTION_4` | VARCHAR(255) |  |  | The fourth description for this item. From health sentry/health facts mapping. |
| 7 | `DESCRIPTION_5` | VARCHAR(255) |  |  | The fifth description for this item. From health sentry/health facts mapping. |
| 8 | `DESCRIPTION_6` | VARCHAR(255) |  |  | The sixth description for this item. From health sentry/health facts mapping. |
| 9 | `DIM_ITEM_IDENT` | DOUBLE | NOT NULL |  | Identifier of the item in the Health Sentry/Health Facts dimension tables. |
| 10 | `IGNORE_IND` | DOUBLE | NOT NULL |  | Indicates if this item needs to be mapped or if the user elected to ignore it. |
| 11 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 12 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 13 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 14 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 15 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Referenced by (1)

| From table | Column |
|------------|--------|
| [BR_HLTH_SNTRY_MILL_ITEM](BR_HLTH_SNTRY_MILL_ITEM.md) | `BR_HLTH_SNTRY_ITEM_ID` |

