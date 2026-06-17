# QC_RESULT_EVENT

> Tracks the different events that can occur for a qc result entered into the system.

**Description:** Quality Control Result Event  
**Table type:** ACTIVITY  
**Primary key:** _(not published — see note)_  
**Columns:** 11

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `EVENT_DT_TM` | DATETIME |  |  | Date and time the event is recorded to have taken place. |
| 2 | `EVENT_PERSONNEL_ID` | DOUBLE | NOT NULL | FK→ | A unique, internal, system-assigned number that identifies the specific person who performed the recorded event. |
| 3 | `EVENT_REASON` | VARCHAR(100) |  |  | Indicates the reason the event was initiated and recorded. |
| 4 | `EVENT_SEQUENCE` | DOUBLE | NOT NULL |  | Creates a unique element for the index and is the sequence in which the events took place. |
| 5 | `EVENT_TYPE_CD` | DOUBLE | NOT NULL |  | A unique code value that identifies the event action that took place. |
| 6 | `QC_RESULT_ID` | DOUBLE | NOT NULL | FK→ | A unique, internal, system-assigned number that identifies a specific quality control result that is associated with the event. |
| 7 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 8 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 9 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 10 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 11 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `EVENT_PERSONNEL_ID` | [PRSNL](PRSNL.md) | `PERSON_ID` |
| `QC_RESULT_ID` | [QC_RESULT](QC_RESULT.md) | `QC_RESULT_ID` |

