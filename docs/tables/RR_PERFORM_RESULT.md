# RR_PERFORM_RESULT

> Stores result values and corresponding information relating to the result. If a result is performed multiple times a new entry into the table is added.

**Description:** Round Robin Perform Result  
**Table type:** ACTIVITY  
**Primary key:** `RR_PERFORM_RESULT_ID`  
**Columns:** 12  
**Referenced by:** 1 columns

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `NUMERIC_RESULT_VALUE` | DOUBLE | NOT NULL |  | Stores the actual result value entered for a given discrete task assay. |
| 2 | `PERFORM_DT_TM` | DATETIME |  |  | Stores the date and time when this result was performed. |
| 3 | `PERFORM_PERSONNEL_ID` | DOUBLE | NOT NULL | FK→ | A unique, internal, system-assigned number that identifies the person who performed the result. Creates a relationship to the person table. |
| 4 | `REPEAT_NBR` | DOUBLE |  |  | Stores the number used to indicate when the result is repeated. |
| 5 | `RESULT_STATUS_CD` | DOUBLE | NOT NULL |  | A unique code value that identifies the status of the result. |
| 6 | `RR_PERFORM_RESULT_ID` | DOUBLE | NOT NULL | PK | A unique, internal, system-assigned number that identifies a specific stage of a performed result. |
| 7 | `RR_RESULT_ID` | DOUBLE | NOT NULL | FK→ | A unique, internal, system-assigned number that identifies the specific result associated with a given discrete task assay. Creates a relationship to the round robin result table. |
| 8 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 9 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 10 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 11 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 12 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `PERFORM_PERSONNEL_ID` | [PRSNL](PRSNL.md) | `PERSON_ID` |
| `RR_RESULT_ID` | [RR_RESULT](RR_RESULT.md) | `RR_RESULT_ID` |

## Referenced by (1)

| From table | Column |
|------------|--------|
| [RR_RESULT_EVENT](RR_RESULT_EVENT.md) | `RR_PERFORM_RESULT_ID` |

