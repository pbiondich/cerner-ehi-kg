# MM_RANGE_PROCESS

> Information about the price calculations of each pricing formula.

**Description:** Pricing Formula Range Process  
**Table type:** ACTIVITY  
**Primary key:** _(not published — see note)_  
**Columns:** 10

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `LAST_RUN_DT_TM` | DATETIME |  |  | The date and time the previous price calculation was performed. |
| 2 | `MM_PRICE_FORMULA_RANGE_ID` | DOUBLE | NOT NULL | FK→ | The pricing formula range that this price evaluation was performed on. |
| 3 | `MM_RANGE_PROCESSING_ID` | DOUBLE | NOT NULL |  | Unique generated number that identifies a single row on the MM_RANGE_PROCESS table. |
| 4 | `NEXT_RUN_DT_TM` | DATETIME |  |  | The date and time the next price calculation is scheduled to run. |
| 5 | `NEXT_RUN_DT_TM_TZ` | DOUBLE | NOT NULL |  | Stores the time zone on which the next run date time is updated. |
| 6 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 7 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 8 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 9 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 10 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `MM_PRICE_FORMULA_RANGE_ID` | [MM_PRICE_FORMULA_RANGE](MM_PRICE_FORMULA_RANGE.md) | `MM_PRICE_FORMULA_RANGE_ID` |

