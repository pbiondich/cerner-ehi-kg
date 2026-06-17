# CDI_WORK_QUEUE_PRSNL_RELTN

> The tables specifies individual users that are granted or denied access to a specific work queue.

**Description:** CDI Work Queue Personnel Relationship  
**Table type:** REFERENCE  
**Primary key:** _(not published — see note)_  
**Columns:** 9

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `CDI_WORK_QUEUE_ID` | DOUBLE | NOT NULL | FK→ | A foreign key from the CDI_WORK_QUEUE table. It is the work queue the personnel has access to. |
| 2 | `CDI_WORK_QUEUE_PRSNL_RELTN_ID` | DOUBLE | NOT NULL |  | The unique pimary key of this table. It is an internally generated number. |
| 3 | `EXCEPTION_IND` | DOUBLE | NOT NULL |  | Specified if the personnel is excluded. |
| 4 | `PERSON_ID` | DOUBLE | NOT NULL | FK→ | A foreign key from the PRSNL table. It is the ID of the person that can access the queue. |
| 5 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 6 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 7 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 8 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 9 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `CDI_WORK_QUEUE_ID` | [CDI_WORK_QUEUE](CDI_WORK_QUEUE.md) | `CDI_WORK_QUEUE_ID` |
| `PERSON_ID` | [PRSNL](PRSNL.md) | `PERSON_ID` |

