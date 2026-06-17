# DIST_LINE_DETAIL

> Detailed information for each line item on a distribution.

**Description:** Distribution Line Detail  
**Table type:** ACTIVITY  
**Primary key:** _(not published — see note)_  
**Columns:** 15

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ACTUAL_FILL_LOC_CD` | DOUBLE | NOT NULL |  | The actual location in which the item was picked. |
| 2 | `ACTUAL_ITEM_ID` | DOUBLE | NOT NULL | FK→ | The actual item that was picked for distribution. |
| 3 | `CREATE_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 4 | `CREATE_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was inserted. |
| 5 | `CREATE_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the insert of the row in the table. |
| 6 | `CREATE_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted the row. |
| 7 | `DISTRIBUTION_ID` | DOUBLE | NOT NULL | FK→ | Foreign key to the distribution table. |
| 8 | `DIST_LINE_APPROVED_FLAG` | DOUBLE | NOT NULL |  | To verify that the distributed QOH is approved in IN-Transit Review window.The field holds either 1 or 0. The value 1 Indicates the distributed line is approved and the value 0 indicates it is not approved. |
| 9 | `DIST_LINE_DETAIL_ID` | DOUBLE | NOT NULL |  | Primary Key |
| 10 | `LINE_ITEM_ID` | DOUBLE | NOT NULL | FK→ | Foreign key to the line item table. |
| 11 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 12 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 13 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 14 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 15 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `ACTUAL_ITEM_ID` | [ITEM_MASTER](ITEM_MASTER.md) | `ITEM_ID` |
| `DISTRIBUTION_ID` | [DIST_LINE_ITEM_R](DIST_LINE_ITEM_R.md) | `DISTRIBUTION_ID` |
| `LINE_ITEM_ID` | [DIST_LINE_ITEM_R](DIST_LINE_ITEM_R.md) | `LINE_ITEM_ID` |

