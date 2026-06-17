# BR_HLTH_SNTRY_MILL_ITEM

> Stores the relationships between Health Sentry items and Millennium items.

**Description:** Bedrock Health Sentry Millennium Item  
**Table type:** REFERENCE  
**Primary key:** _(not published — see note)_  
**Columns:** 8

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `BR_HLTH_SNTRY_ITEM_ID` | DOUBLE | NOT NULL | FK→ | The Health Sentry item that is related to this Millennium item. |
| 2 | `BR_HLTH_SNTRY_MILL_ITEM_ID` | DOUBLE | NOT NULL |  | Unique, generated number that identifies a single row on the BR_HLTH_SNTRY_MILL_ITEM table. |
| 3 | `CODE_VALUE` | DOUBLE | NOT NULL |  | The Millennium item that maps to the Health Sentry item on a row. |
| 4 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 5 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 6 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 7 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 8 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `BR_HLTH_SNTRY_ITEM_ID` | [BR_HLTH_SNTRY_ITEM](BR_HLTH_SNTRY_ITEM.md) | `BR_HLTH_SNTRY_ITEM_ID` |

