# RAD_VETTING_HOLD_DETAIL

> Contains the vetting hold details added while holding the order.

**Description:** RadNet Vetting Hold Detail  
**Table type:** ACTIVITY  
**Primary key:** _(not published — see note)_  
**Columns:** 15

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `HOLD_COMMENT_TXT` | VARCHAR(512) |  |  | Comments added while holding the order. |
| 2 | `LAST_UPDT_DT_TM` | DATETIME | NOT NULL |  | Last time the row was updated. |
| 3 | `LAST_UPDT_PRSNL_ID` | DOUBLE | NOT NULL | FK→ | The person that last updated this row. |
| 4 | `LAST_UPDT_TZ` | DOUBLE | NOT NULL |  | The time zone of the last update date. |
| 5 | `ORDER_ID` | DOUBLE | NOT NULL | FK→ | The Radnet order of the vetting held order. |
| 6 | `ORIG_HOLD_DT_TM` | DATETIME | NOT NULL |  | The date of the original vetting hold. |
| 7 | `ORIG_HOLD_PRSNL_ID` | DOUBLE | NOT NULL | FK→ | The personnel that originally held the vetting. |
| 8 | `ORIG_HOLD_TZ` | DOUBLE | NOT NULL |  | The time zone of the original hold date. |
| 9 | `PROXY_HOLD_PRSNL_ID` | DOUBLE | NOT NULL | FK→ | The person who edits the vetting hold comments on behalf of original vetting hold personnel. |
| 10 | `RAD_VETTING_HOLD_DETAIL_ID` | DOUBLE | NOT NULL |  | Unique generated number that identifies a single row on the RAD_VETTING_HOLD_DETAIL table. |
| 11 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 12 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 13 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 14 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 15 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `LAST_UPDT_PRSNL_ID` | [PRSNL](PRSNL.md) | `PERSON_ID` |
| `ORDER_ID` | [ORDER_RADIOLOGY](ORDER_RADIOLOGY.md) | `ORDER_ID` |
| `ORIG_HOLD_PRSNL_ID` | [PRSNL](PRSNL.md) | `PERSON_ID` |
| `PROXY_HOLD_PRSNL_ID` | [PRSNL](PRSNL.md) | `PERSON_ID` |

