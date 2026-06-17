# MIC_BPA_WORKLIST_DETAIL

> Stores the details (tasks and qc organisms) for a specific worklist.

**Description:** Microbiology Breakpoint Worklist Detail  
**Table type:** ACTIVITY  
**Primary key:** _(not published — see note)_  
**Columns:** 13

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ACTIVE_WELL_IND` | DOUBLE |  |  | Indicates whether the well are active or not. |
| 2 | `PARENT_ENTITY_ID` | DOUBLE | NOT NULL |  | This field contains the primary identifier for the parent table. |
| 3 | `PARENT_ENTITY_NAME` | VARCHAR(32) | NOT NULL |  | This field contains the table name of the parent. |
| 4 | `PLATE` | DOUBLE | NOT NULL |  | The breakpoint plate number assigned to the worklist detail. |
| 5 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 6 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 7 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 8 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 9 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |
| 10 | `WELL` | DOUBLE | NOT NULL |  | The breakpoint well number assigned to the worklist detail. |
| 11 | `WORKLIST_COMMENT` | VARCHAR(250) |  |  | Stores the internal comment for an individual worklist detail. |
| 12 | `WORKLIST_DETAIL_ID` | DOUBLE | NOT NULL |  | Internal identification code assigned to each breakpoint worklist detail. |
| 13 | `WORKLIST_ID` | DOUBLE | NOT NULL | FK→ | Internal identification code assigned to each breakpoint worklist. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `WORKLIST_ID` | [MIC_BPA_WORKLIST](MIC_BPA_WORKLIST.md) | `WORKLIST_ID` |

