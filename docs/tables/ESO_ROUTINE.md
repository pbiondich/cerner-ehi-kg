# ESO_ROUTINE

> This table defines the scripts or hard coded C routines that are accessible to ESO for event processing.

**Description:** ESO Routine Table  
**Table type:** REFERENCE  
**Primary key:** `ROUTINE_ID`  
**Columns:** 13  
**Referenced by:** 1 columns

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ACTIVE_IND` | DOUBLE | NOT NULL |  | The table row is active or inactive. A row is generally active unless it is in an inactive state such as logically deleted, combined away, pending purge, etc. |
| 2 | `ARGS_DEFAULT` | VARCHAR(255) |  |  | This string define the default arguments that may be used to populate routine_args element on the ESO_TRIG_ROUTINE_R table. |
| 3 | `ARGS_HELP` | VARCHAR(255) |  |  | This string may define the syntax or options for populating the routine_args element on the ESO_TRIG_ROUTINE_R table. |
| 4 | `CREATE_DT_TM` | DATETIME | NOT NULL |  | This is the date and time that a row is created in the eso_routine table. |
| 5 | `DESCRIPTION` | VARCHAR(255) |  |  | This string provides a description of the routine or script.. |
| 6 | `ROUTINE` | VARCHAR(50) | NOT NULL |  | Routine name. Define a hard coded C routine. If this is either GENERIC_SCRIPT_USE_REPLY or GENERIC_SCRIPT_USE_CTX, then the script field should be valued. |
| 7 | `ROUTINE_ID` | DOUBLE | NOT NULL | PK | This is the value of the unique primary identifier of the eso_routine table. It is an internal system assigned number. |
| 8 | `SCRIPT` | VARCHAR(50) |  |  | Script Name. If the routine field is either GENERIC_SCRIPT_USE_REPLY or GENERIC_SCRIPT_USE_CTX, then this field should be valued. |
| 9 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 10 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 11 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 12 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 13 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Referenced by (1)

| From table | Column |
|------------|--------|
| [ESO_TRIG_ROUTINE_R](ESO_TRIG_ROUTINE_R.md) | `ROUTINE_ID` |

