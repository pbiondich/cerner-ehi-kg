# DIST_LINE_ITEM_R

> A relationship table between the Distribution and Line Item tables.

**Description:** Distribution Line Item  
**Table type:** ACTIVITY  
**Primary key:** `DISTRIBUTION_ID`, `LINE_ITEM_ID`  
**Columns:** 16  
**Referenced by:** 2 columns

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `BACKORDER_IND` | DOUBLE |  |  | Back order indicator |
| 2 | `CREATE_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 3 | `CREATE_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was inserted. |
| 4 | `CREATE_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the insert of the row in the table. |
| 5 | `CREATE_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted the row. |
| 6 | `DISTRIBUTION_ID` | DOUBLE | NOT NULL | PK FK→ | Foreign key to the distribution table. |
| 7 | `FROM_COST_CENTER_CD` | DOUBLE |  |  | The cost center that the line item is coming from. |
| 8 | `FROM_SUB_ACCOUNT_CD` | DOUBLE |  |  | The sub account that the line item is coming from. |
| 9 | `LINE_ITEM_ID` | DOUBLE | NOT NULL | PK FK→ | Foreign key to the line_item table. |
| 10 | `TO_COST_CENTER_CD` | DOUBLE |  |  | The cost center that will be charged for this line item. |
| 11 | `TO_SUB_ACCOUNT_CD` | DOUBLE |  |  | The sub account that will be charged for this line item. |
| 12 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 13 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 14 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 15 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 16 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `DISTRIBUTION_ID` | [DISTRIBUTION](DISTRIBUTION.md) | `DISTRIBUTION_ID` |
| `LINE_ITEM_ID` | [LINE_ITEM](LINE_ITEM.md) | `LINE_ITEM_ID` |

## Referenced by (2)

| From table | Column |
|------------|--------|
| [DIST_LINE_DETAIL](DIST_LINE_DETAIL.md) | `DISTRIBUTION_ID` |
| [DIST_LINE_DETAIL](DIST_LINE_DETAIL.md) | `LINE_ITEM_ID` |

