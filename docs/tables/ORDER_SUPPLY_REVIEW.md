# ORDER_SUPPLY_REVIEW

> Order Supply Review table stores information entered during pharmacy discharge process.

**Description:** ORDER_SUPPLY_REVIEW  
**Table type:** ACTIVITY  
**Primary key:** `ORDER_SUPPLY_REVIEW_ID`  
**Columns:** 13  
**Referenced by:** 1 columns

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ACTIVE_IND` | DOUBLE | NOT NULL |  | The table row is active or inactive. A row is generally active unless it is in an inactive state such as logically deleted, combined away, pending purge, etc. |
| 2 | `ENCNTR_ID` | DOUBLE | NOT NULL | FK→ | The ID of the encounter this supply/verify information is related to. If the order is continued onto a second encounter this value could differ from the encounter ID on the Orders table. |
| 3 | `LOCATION_EXISTS_IND` | DOUBLE | NOT NULL |  | An indicator to confirm that location_cd exists in the child table. |
| 4 | `LONG_TEXT_ID` | DOUBLE | NOT NULL |  | The long text id for the long text table |
| 5 | `NURSE_REVIEW_IND` | DOUBLE | NOT NULL |  | An indicator to confirm that nurse review is performed. This column is Obsolete. |
| 6 | `ORDER_ID` | DOUBLE | NOT NULL | FK→ | The id of the order. |
| 7 | `ORDER_SUPPLY_REVIEW_ID` | DOUBLE | NOT NULL | PK | Unique generated number that identifies a single row on the ORDER_SUPPLY_REVIEW table. |
| 8 | `PHARMACY_REVIEW_IND` | DOUBLE | NOT NULL |  | An indicator to confirm that pharmacy review is performed. |
| 9 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 10 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 11 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 12 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 13 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `ENCNTR_ID` | [ENCOUNTER](ENCOUNTER.md) | `ENCNTR_ID` |
| `ORDER_ID` | [ORDERS](ORDERS.md) | `ORDER_ID` |

## Referenced by (1)

| From table | Column |
|------------|--------|
| [ORDER_SUPPLY_LOCATION](ORDER_SUPPLY_LOCATION.md) | `ORDER_SUPPLY_REVIEW_ID` |

