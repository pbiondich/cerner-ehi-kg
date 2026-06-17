# TPL_APPL_TASK_RELTN

> Stores the tasks associated to the applications used in the build and launch application tool.

**Description:** Third Party Launch Application Task Relation  
**Table type:** REFERENCE  
**Primary key:** `APPL_TASK_RELTN_ID`  
**Columns:** 8  
**Referenced by:** 1 columns

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `APPL_ID` | DOUBLE | NOT NULL | FK→ | Foreign key to the TPL_APPL table. |
| 2 | `APPL_TASK_RELTN_ID` | DOUBLE | NOT NULL | PK | Unique generated key for this table. |
| 3 | `TASK_NUMBER` | DOUBLE | NOT NULL |  | Task number from APPLICATION_TASK. |
| 4 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 5 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 6 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 7 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 8 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `APPL_ID` | [TPL_APPL](TPL_APPL.md) | `APPL_ID` |

## Referenced by (1)

| From table | Column |
|------------|--------|
| [TPL_APPL_DETAIL](TPL_APPL_DETAIL.md) | `APPL_TASK_RELTN_ID` |

