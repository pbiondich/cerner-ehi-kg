# DCP_PL_QUERY_LIST

> Stores the user¿s based query patient list with template id and execution status.

**Description:** DCP PL QUERY LIST  
**Table type:** ACTIVITY  
**Primary key:** `PATIENT_LIST_ID`  
**Columns:** 9  
**Referenced by:** 1 columns

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `EXECUTION_DT_TM` | DATETIME |  |  | The date & time of the last execution of the query. |
| 2 | `EXECUTION_STATUS_CD` | DOUBLE | NOT NULL |  | Identifies the status of the query whether it is executing, completed or has never been run. |
| 3 | `PATIENT_LIST_ID` | DOUBLE | NOT NULL | PK | Unique identifier for the query based patient list. |
| 4 | `TEMPLATE_ID` | DOUBLE | NOT NULL | FK→ | The id of the template that the query based patient list was built from. |
| 5 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 6 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 7 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 8 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 9 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `TEMPLATE_ID` | [DCP_PL_QUERY_TEMPLATE](DCP_PL_QUERY_TEMPLATE.md) | `TEMPLATE_ID` |

## Referenced by (1)

| From table | Column |
|------------|--------|
| [DCP_PL_QUERY_VALUE](DCP_PL_QUERY_VALUE.md) | `PATIENT_LIST_ID` |

