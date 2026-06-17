# DUP_CHECKING

> Used to define the time range and action for order duplicate checking.

**Description:** DUP CHECKING  
**Table type:** REFERENCE  
**Primary key:** _(not published — see note)_  
**Columns:** 19

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ACTIVE_IND` | DOUBLE |  |  | The table row is active or inactive. A row is generally active unless it is in an inactive state such as logically deleted, combined away, pending purge, etc. |
| 2 | `CATALOG_CD` | DOUBLE | NOT NULL | FK→ | catalog code for the orderable |
| 3 | `DUP_CHECK_SEQ` | DOUBLE | NOT NULL |  | sequence number for duplicate checking |
| 4 | `EXACT_HIT_ACTION_CD` | DOUBLE | NOT NULL |  | Action code if the start date time are exact the same. |
| 5 | `MIN_AHEAD` | DOUBLE |  |  | number of minute ahead of the start date time of the order |
| 6 | `MIN_AHEAD_ACTION_CD` | DOUBLE | NOT NULL |  | Action code for minute ahead dup checking. |
| 7 | `MIN_BEHIND` | DOUBLE |  |  | number of minute behind the start date time of the order |
| 8 | `MIN_BEHIND_ACTION_CD` | DOUBLE | NOT NULL |  | Action code for minute behind dup checking. |
| 9 | `OUTPAT_EXACT_HIT_ACTION_CD` | DOUBLE |  |  | Dup check rule for out patient - action code if the start date time are exact the same. |
| 10 | `OUTPAT_FLEX_IND` | DOUBLE |  |  | Indicator to turn on special dup checking rules for out patient. |
| 11 | `OUTPAT_MIN_AHEAD` | DOUBLE |  |  | Dup checking rule for out patient - number of minute ahead of the start date time of the order |
| 12 | `OUTPAT_MIN_AHEAD_ACTION_CD` | DOUBLE |  |  | Dup checking rule for out patient - action code for minute ahead dup checking. |
| 13 | `OUTPAT_MIN_BEHIND` | DOUBLE |  |  | Dup checking rule for out patient - number of minute behind the start date time of the order |
| 14 | `OUTPAT_MIN_BEHIND_ACTION_CD` | DOUBLE |  |  | Dup checking rule for out patient - action code for minute behind dup checking. |
| 15 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 16 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 17 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 18 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 19 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `CATALOG_CD` | [ORDER_CATALOG](ORDER_CATALOG.md) | `CATALOG_CD` |

