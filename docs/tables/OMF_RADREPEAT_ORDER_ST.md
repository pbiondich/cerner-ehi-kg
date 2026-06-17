# OMF_RADREPEAT_ORDER_ST

> Summary table storing film adjustment information for radiology mgmt.

**Description:** OMF RADREPEAT ORDER ST  
**Table type:** ACTIVITY  
**Primary key:** _(not published — see note)_  
**Columns:** 14

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `FILM_SIZE_CD` | DOUBLE | NOT NULL |  | The code value for the film size associated with the film adjustment record. |
| 2 | `FILM_TYPE_CD` | DOUBLE | NOT NULL |  | The code value associated with the film type for this film adjustment record. |
| 3 | `OMF_RADREPEAT_ORDER_ST_ID` | DOUBLE | NOT NULL |  | Unique key for the radiology repeat summary table. |
| 4 | `ORDER_ID` | DOUBLE | NOT NULL | FK→ | The identification number associated with this order. |
| 5 | `REASON_CD` | DOUBLE | NOT NULL |  | The repeat reason associated with the film adjustment record. |
| 6 | `REPEAT_SEQ` | DOUBLE | NOT NULL |  | Provides uniqueness to the film adjustment records. |
| 7 | `STANDARD_QTY` | DOUBLE |  |  | The standard amount of film that should be used with this film type. |
| 8 | `TECHNOLOGIST_ID` | DOUBLE | NOT NULL | FK→ | The technologist responsible for the film adjustment. |
| 9 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 10 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 11 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 12 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 13 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |
| 14 | `WASTE_QTY` | DOUBLE |  |  | The amount of extra film associated associated with this film adjustment. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `ORDER_ID` | [ORDERS](ORDERS.md) | `ORDER_ID` |
| `TECHNOLOGIST_ID` | [PRSNL](PRSNL.md) | `PERSON_ID` |

