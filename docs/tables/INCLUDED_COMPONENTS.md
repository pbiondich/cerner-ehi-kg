# INCLUDED_COMPONENTS

> Defines the components that were used to perform a result for a calculation.

**Description:** Included Components  
**Table type:** ACTIVITY  
**Primary key:** _(not published — see note)_  
**Columns:** 9

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ACTIVITY_FLAG` | DOUBLE |  |  | Used to determine if the result was taken from activity or from clinical events. (Currently not implemented) |
| 2 | `PERFORM_RESULT_ID` | DOUBLE | NOT NULL |  | A unique, internal, system-assigned number that identifies a specific perform result value of the equation. Creates a relationship to the perform result table. |
| 3 | `RESULT_ID` | DOUBLE | NOT NULL |  | A unique. internal. system-assigned number that identifies a specific result value used as a component of the equation. Creates a relationship to the result table. |
| 4 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 5 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 6 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 7 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 8 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |
| 9 | `USED_PERFORM_RESULT_ID` | DOUBLE | NOT NULL |  | A unique, internal, system-assigned number that identifies a specific perform result value used as a component of the equation. Creates a relationship to the perform result table. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

