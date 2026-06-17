# MIC_SCRIPT_NODE_RESULT

> This reference table contains the biochemical result values for the parent biochemical (MIC_SCRIPT_NODE) which will cause associated 'actions' to be taken as well as ordering the next biochemical within a pathway.

**Description:** Microbiology Script Node Result  
**Table type:** REFERENCE  
**Primary key:** _(not published — see note)_  
**Columns:** 8

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `DETAIL_BIOCHEMICAL_CD` | DOUBLE | NOT NULL |  | This field contains the internal identification code of a detail biochemical task. If the biochemical_task_cd on the parent MIC_SCRIPT_NODE table is a group biochemical then this is a detail of that group, otherwise this is the same value as on the MIC_SCRIPT_NODE table. |
| 2 | `NODE_ID` | DOUBLE | NOT NULL | FK→ | This field contains the internal identification code to the parent MIC_SCRIPT_NODE row. |
| 3 | `RESULT_CD` | DOUBLE | NOT NULL |  | This field contains the internal identification code for a biochemical result. |
| 4 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 5 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 6 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 7 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 8 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `NODE_ID` | [MIC_SCRIPT_NODE](MIC_SCRIPT_NODE.md) | `NODE_ID` |

