# RESULT_EVENT

> Defines what result events have taken place for a given discrete task assay.

**Description:** Result Event  
**Table type:** ACTIVITY  
**Primary key:** _(not published — see note)_  
**Columns:** 14

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `CALLED_BACK_IND` | DOUBLE |  |  | Indicates whether the result was called back for this event. (Currently not implemented) |
| 2 | `EVENT_DT_TM` | DATETIME |  |  | Defines the date and time the event took place. |
| 3 | `EVENT_PERSONNEL_ID` | DOUBLE | NOT NULL | FK→ | A unique, internal, system-assigned number that identifies a specific person who performed the event on a result. Creates a relationship to the person table. |
| 4 | `EVENT_REASON` | VARCHAR(100) |  |  | Defines the purpose for the event being created. |
| 5 | `EVENT_SEQUENCE` | DOUBLE | NOT NULL |  | Starts at one and is incremented by one when multiple result events are completed at the same time. For example, when the user enters and verifies a result, the actions cause the system to execute perform and verify events at the same time. |
| 6 | `EVENT_TYPE_CD` | DOUBLE | NOT NULL |  | A unique code value that identifies the specific action of the event that took place on the result. |
| 7 | `PERFORM_RESULT_ID` | DOUBLE | NOT NULL |  | A unique, internal, system-assigned number that identifies a specific result has been performed. Creates a relationship to the perform result table. |
| 8 | `RESULT_ID` | DOUBLE | NOT NULL |  | A unique, internal, system-assigned number that identifies a specific result. Creates a relationship to the result table. |
| 9 | `SIGNATURE_LINE_IND` | DOUBLE |  |  | Indicates whether a signature line should be added to the result. |
| 10 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 11 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 12 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 13 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 14 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `EVENT_PERSONNEL_ID` | [PRSNL](PRSNL.md) | `PERSON_ID` |

