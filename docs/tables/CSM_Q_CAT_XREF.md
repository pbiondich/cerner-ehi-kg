# CSM_Q_CAT_XREF

> The table to list the categories associated with various CSM queues.

**Description:** CSM Q CAT XREF  
**Table type:** REFERENCE  
**Primary key:** _(not published — see note)_  
**Columns:** 9

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `CSM_CAT_ID` | DOUBLE | NOT NULL | FK→ | The unique identifier for the CSM category. |
| 2 | `CSM_CAT_INCL_FLAG` | DOUBLE |  |  | The flag to indicate whether or not to include/exclude the record. |
| 3 | `CSM_QUEUE_ID` | DOUBLE | NOT NULL | FK→ | The unique identifier for the CSM queue. |
| 4 | `CSM_SUB_CAT_ID` | DOUBLE | NOT NULL |  | The unique identifier for the CSM sub category. |
| 5 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 6 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 7 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 8 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 9 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `CSM_CAT_ID` | [CSM_CATEGORIES](CSM_CATEGORIES.md) | `CSM_CAT_ID` |
| `CSM_QUEUE_ID` | [CSM_QUEUES](CSM_QUEUES.md) | `CSM_QUEUE_ID` |

