# COST_ADJ

> Defines the markup/discount for a grouping of or specific bill items.

**Description:** Cost Adjustment  
**Table type:** REFERENCE  
**Primary key:** _(not published — see note)_  
**Columns:** 11

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ADJUSTMENT_AMT` | DOUBLE | NOT NULL |  | The amount of the adjustment, either as a percentage or flat amount. |
| 2 | `ADJUSTMENT_TYPE_FLAG` | DOUBLE | NOT NULL |  | Indicates the type of adjustment: 1-Percentage, 2-Amount |
| 3 | `COST_ADJ_FLEX_ID` | DOUBLE | NOT NULL | FK→ | Cost Adjustment Flex ID - foreign key |
| 4 | `COST_ADJ_ID` | DOUBLE | NOT NULL |  | Cost Adjustment ID- Primary Key |
| 5 | `LOWER_THRESHOLD` | DOUBLE | NOT NULL |  | Defines the lower cost boundary for this range. |
| 6 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 7 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 8 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 9 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 10 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |
| 11 | `UPPER_THRESHOLD` | DOUBLE | NOT NULL |  | Defines the upper cost boundary for this range. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `COST_ADJ_FLEX_ID` | [COST_ADJ_FLEX](COST_ADJ_FLEX.md) | `COST_ADJ_FLEX_ID` |

