# GEL_BATCH

> Used to store information about a batch process for gels

**Description:** Gel Batch  
**Table type:** ACTIVITY  
**Primary key:** `GEL_BATCH_ID`  
**Columns:** 11  
**Referenced by:** 3 columns

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `GEL_BATCH_DESC` | VARCHAR(30) |  |  | The description of the Gel Batch |
| 2 | `GEL_BATCH_ID` | DOUBLE | NOT NULL | PK | Unique Identifier for the Gel Batch |
| 3 | `GEL_BATCH_IND` | DOUBLE | NOT NULL |  | Indicates whether or not this is a true batch (instead of a just a single gel). |
| 4 | `PREPARED_DT_TM` | DATETIME | NOT NULL |  | The Date the rack was prepared |
| 5 | `PREPARED_PRSNL_ID` | DOUBLE | NOT NULL | FK→ | The user id of the person who created the batch. |
| 6 | `RACK_ID` | DOUBLE | NOT NULL | FK→ | A foreign key reference to the rack used for the batch. |
| 7 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 8 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 9 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 10 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 11 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `PREPARED_PRSNL_ID` | [PRSNL](PRSNL.md) | `PERSON_ID` |
| `RACK_ID` | [THERMOCYCLER_RACK](THERMOCYCLER_RACK.md) | `RACK_ID` |

## Referenced by (3)

| From table | Column |
|------------|--------|
| [GEL_LOADING](GEL_LOADING.md) | `GEL_BATCH_ID` |
| [GEL_RESULT_COMMENT](GEL_RESULT_COMMENT.md) | `GEL_BATCH_ID` |
| [ORDER_THERMOCYCLER_RACK](ORDER_THERMOCYCLER_RACK.md) | `GEL_BATCH_ID` |

