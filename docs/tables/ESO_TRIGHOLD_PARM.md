# ESO_TRIGHOLD_PARM

> Stores trigger hold parameters for different class/type/subtype combinations. If a row exists for a particular combination, then that trigger can be held.

**Description:** ESO Trigger Hold Parameter  
**Table type:** REFERENCE  
**Primary key:** _(not published — see note)_  
**Columns:** 10

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `CLASS` | VARCHAR(15) | NOT NULL |  | The trigger's CQM class |
| 2 | `ESO_TRIGHOLD_PARM_ID` | DOUBLE | NOT NULL |  | Defines a unique ID for each trigger hold parameter |
| 3 | `SUBTYPE` | VARCHAR(15) | NOT NULL |  | The trigger's CQM subtype |
| 4 | `TRIG_ROLLUP_SCRIPT_NAME` | VARCHAR(40) |  |  | Defines which script will be used to combine multiple triggers |
| 5 | `TYPE` | VARCHAR(15) | NOT NULL |  | The trigger's CQM type |
| 6 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 7 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 8 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 9 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 10 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

