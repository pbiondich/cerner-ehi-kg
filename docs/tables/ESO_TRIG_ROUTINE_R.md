# ESO_TRIG_ROUTINE_R

> This table define the relationships between ESO Triggers and ESO routines. For each outbound trigger event, this table define the list of processing units (scripts or routines) that are needed to format an outbound message according to UI specifications.

**Description:** ESO Trigger Routine Relation Table  
**Table type:** REFERENCE  
**Primary key:** `ROUTINE_ID`, `TRIGGER_ID`  
**Columns:** 14  
**Referenced by:** 2 columns

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ACTIVE_IND` | DOUBLE | NOT NULL |  | The table row is active or inactive. A row is generally active unless it is in an inactive state such as logically deleted, combined away, pending purge, etc. |
| 2 | `CREATE_DT_TM` | DATETIME | NOT NULL |  | This is the date and time that a row is created in the eso_trig_routine_r table. |
| 3 | `DEBUG_IND` | DOUBLE |  |  | This indicator may be used by the ESO Server to debug ESO routines or scripts while in a run-time mode. |
| 4 | `ROUTINE_ARGS` | VARCHAR(255) |  |  | This string defines the arguments that are passed into the ESO script or routine when the event trigger is processed. |
| 5 | `ROUTINE_CONTROL` | DOUBLE |  |  | This integer number is passed into the ESO script or routine when the event trigger is processed to control routine specific processing elements.. |
| 6 | `ROUTINE_ID` | DOUBLE | NOT NULL | PK FK→ | Part of the Unique Identifier fro this table. Identifies the routine from the ESO_ROUTINE table. |
| 7 | `SEQUENCE_NBR` | DOUBLE | NOT NULL |  | Identifies the sequence that the routine should be performed in by trigger (TRIGGER_ID). |
| 8 | `TRIGGER_ID` | DOUBLE | NOT NULL | PK FK→ | Part of the unique identifier for the table. Identifies the Trigger from the ESO_TRIGGER table. |
| 9 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 10 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 11 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 12 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 13 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |
| 14 | `VERBOSITY_FLAG` | DOUBLE |  |  | This flag may be used by the ESO Server to control the verbosity when debugging an ESO routine or script while in a run-time mode. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `ROUTINE_ID` | [ESO_ROUTINE](ESO_ROUTINE.md) | `ROUTINE_ID` |
| `TRIGGER_ID` | [ESO_TRIGGER](ESO_TRIGGER.md) | `TRIGGER_ID` |

## Referenced by (2)

| From table | Column |
|------------|--------|
| [SI_ESO_TRIG_ROUT_R_HIST](SI_ESO_TRIG_ROUT_R_HIST.md) | `ROUTINE_ID` |
| [SI_ESO_TRIG_ROUT_R_HIST](SI_ESO_TRIG_ROUT_R_HIST.md) | `TRIGGER_ID` |

