# CSM_QUEUES

> The table that records the queue names, ids, and parameters for CSM.

**Description:** CSM QUEUES  
**Table type:** REFERENCE  
**Primary key:** `CSM_QUEUE_ID`  
**Columns:** 8  
**Referenced by:** 3 columns

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `CSM_QUEUE_DESC` | CHAR(40) | NOT NULL |  | The queue name field. |
| 2 | `CSM_QUEUE_ID` | DOUBLE | NOT NULL | PK | The unique identifier for a queue. |
| 3 | `CSM_QUEUE_TYPE_IND` | DOUBLE | NOT NULL |  | Indicates whether the queue is for Callbacks or Call-ins. |
| 4 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 5 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 6 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 7 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 8 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Referenced by (3)

| From table | Column |
|------------|--------|
| [CSM_QUEUE_PERS_XREF](CSM_QUEUE_PERS_XREF.md) | `CSM_QUEUE_ID` |
| [CSM_Q_CAT_XREF](CSM_Q_CAT_XREF.md) | `CSM_QUEUE_ID` |
| [CSM_Q_ORG_XREF](CSM_Q_ORG_XREF.md) | `CSM_QUEUE_ID` |

