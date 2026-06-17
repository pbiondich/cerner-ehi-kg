# RX_IMAGE_QUEUE_PRSNL_RELTN

> Stores the relationship between RX_IMAGE_QUEUE and PRSNL.

**Description:** Image Queue Personnel Relation  
**Table type:** REFERENCE  
**Primary key:** _(not published — see note)_  
**Columns:** 8

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `IMAGE_QUEUE_ID` | DOUBLE | NOT NULL | FK→ | Identifies the specific Image Queue that is involved in this Queue to Personnel relationship. |
| 2 | `IMAGE_QUEUE_PRSNL_RELTN_ID` | DOUBLE | NOT NULL |  | The unique identifier for the Image Queue to User (prsnl) relationship. |
| 3 | `PERSON_ID` | DOUBLE | NOT NULL | FK→ | The Personnel that uses the Image Queue. |
| 4 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 5 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 6 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 7 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 8 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `IMAGE_QUEUE_ID` | [RX_IMAGE_QUEUE](RX_IMAGE_QUEUE.md) | `IMAGE_QUEUE_ID` |
| `PERSON_ID` | [PRSNL](PRSNL.md) | `PERSON_ID` |

