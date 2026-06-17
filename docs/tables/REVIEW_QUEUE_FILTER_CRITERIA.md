# REVIEW_QUEUE_FILTER_CRITERIA

> Defines a unique name for a specific user's review queue filter. Users can create review queue filter to limit the display in their review queue to specific review status and/or specific orderable procedures.

**Description:** Review Queue Filter Criteria  
**Table type:** REFERENCE  
**Primary key:** `FILTER_ID`, `PRSNL_ID`  
**Columns:** 8  
**Referenced by:** 4 columns

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `FILTER_ID` | DOUBLE | NOT NULL | PK | A sequentially assigned number which uniquely identifies a Review Queue Filter record. |
| 2 | `FILTER_NAME` | VARCHAR(20) |  |  | The name of the Review Queue Filter. Unique identifier the user gives the filter. |
| 3 | `PRSNL_ID` | DOUBLE | NOT NULL | PK FK→ | Identifies the users who created the filter. Only this user may use the filter. |
| 4 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 5 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 6 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 7 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 8 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `PRSNL_ID` | [PRSNL](PRSNL.md) | `PERSON_ID` |

## Referenced by (4)

| From table | Column |
|------------|--------|
| [REV_Q_FILT_CRIT_ORD_PROC](REV_Q_FILT_CRIT_ORD_PROC.md) | `FILTER_ID` |
| [REV_Q_FILT_CRIT_ORD_PROC](REV_Q_FILT_CRIT_ORD_PROC.md) | `PRSNL_ID` |
| [REV_Q_FILT_CRIT_REV_STAT](REV_Q_FILT_CRIT_REV_STAT.md) | `FILTER_ID` |
| [REV_Q_FILT_CRIT_REV_STAT](REV_Q_FILT_CRIT_REV_STAT.md) | `PRSNL_ID` |

