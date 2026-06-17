# ALIAS_POOL_SEQ

> Table used to hold sequence number information for assigning aliases

**Description:** Alias Pool Sequence Table  
**Table type:** REFERENCE  
**Primary key:** _(not published — see note)_  
**Columns:** 10

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ALIAS_POOL_CD` | DOUBLE | NOT NULL | FK→ | Unique identifier for associated alias pool |
| 2 | `AP_SEQ_TYPE_CD` | DOUBLE | NOT NULL |  | Unique identifier for sequence type |
| 3 | `MAX_NBR` | DOUBLE | NOT NULL |  | The upper value for alias sequence assignment |
| 4 | `NEXT_NBR` | DOUBLE | NOT NULL |  | The sequence value to be assigned next |
| 5 | `START_NBR` | DOUBLE | NOT NULL |  | The beginning value for alias sequence assignment |
| 6 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 7 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 8 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 9 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 10 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `ALIAS_POOL_CD` | [ALIAS_POOL](ALIAS_POOL.md) | `ALIAS_POOL_CD` |

