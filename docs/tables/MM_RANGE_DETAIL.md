# MM_RANGE_DETAIL

> This table will store the varius components that are considered to calculate the price for each date range.

**Description:** Pricing Formula Range Detail  
**Table type:** REFERENCE  
**Primary key:** `MM_RANGE_DETAIL_ID`  
**Columns:** 19  
**Referenced by:** 1 columns

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ACTIVE_IND` | DOUBLE | NOT NULL |  | The table row is active or inactive. A row is generally active unless it is in an inactive state such as logically deleted, combined away, pending purge, etc. |
| 2 | `ADMIN_CHARGE_AMT` | DOUBLE | NOT NULL |  | Administrative overhead which added/subtracted to base price to form the final cost |
| 3 | `BEGIN_EFFECTIVE_DT_TM` | DATETIME | NOT NULL |  | The date/time after which the row is considered valid as active current data. |
| 4 | `END_EFFECTIVE_DT_TM` | DATETIME | NOT NULL |  | The date/time after which the row is no longer valid as active current data. This may be valued with the date that the row became inactive. |
| 5 | `FROM_COST_AMT` | DOUBLE | NOT NULL |  | Base price of the item |
| 6 | `LAST_UPDT_PRSNL_ID` | DOUBLE | NOT NULL | FK→ | Personnel that last updated this row. |
| 7 | `MARKUP_PCT` | DOUBLE | NOT NULL |  | Percentage of markup overhead which added/subtracted to base price to form the final cost |
| 8 | `MIN_PRICE_AMT` | DOUBLE | NOT NULL |  | The minimum price an item can cost. |
| 9 | `MM_PRICE_FORMULA_RANGE_ID` | DOUBLE | NOT NULL | FK→ | The pricing formula range that these details pertain to. |
| 10 | `MM_RANGE_DETAIL_ID` | DOUBLE | NOT NULL | PK | Unique generated number that identifies a single row on the MM_RANGE_DETAIL table. |
| 11 | `PREV_MM_RANGE_DETAIL_ID` | DOUBLE | NOT NULL | FK→ | The id to the range detail row before the record was changed. If 0, this is the original unchanged record |
| 12 | `ROUND_UP_AMT` | DOUBLE | NOT NULL |  | Rounded value to the nearest number |
| 13 | `SERVICE_CHARGE_AMT` | DOUBLE | NOT NULL |  | Service charge overhead which added/subtracted to base price to form the final cost |
| 14 | `TO_COST_AMT` | DOUBLE | NOT NULL |  | Final price of an item |
| 15 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 16 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 17 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 18 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 19 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `LAST_UPDT_PRSNL_ID` | [PRSNL](PRSNL.md) | `PERSON_ID` |
| `MM_PRICE_FORMULA_RANGE_ID` | [MM_PRICE_FORMULA_RANGE](MM_PRICE_FORMULA_RANGE.md) | `MM_PRICE_FORMULA_RANGE_ID` |
| `PREV_MM_RANGE_DETAIL_ID` | [MM_RANGE_DETAIL](MM_RANGE_DETAIL.md) | `MM_RANGE_DETAIL_ID` |

## Referenced by (1)

| From table | Column |
|------------|--------|
| [MM_RANGE_DETAIL](MM_RANGE_DETAIL.md) | `PREV_MM_RANGE_DETAIL_ID` |

