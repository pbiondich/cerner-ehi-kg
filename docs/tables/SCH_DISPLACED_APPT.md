# SCH_DISPLACED_APPT

> Displaced appointments are recorded here.

**Description:** Scheduling Displaced Appointment  
**Table type:** ACTIVITY  
**Primary key:** _(not published — see note)_  
**Columns:** 11

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `DEF_APPLY_ID` | DOUBLE | NOT NULL | FK→ | The ID of the row in the SCH_DEF_APPLY table that causes the appointment to be displaced. |
| 2 | `PLACEMENT_STATE_CD` | DOUBLE | NOT NULL |  | The state of the displaced appointment. |
| 3 | `PLACEMENT_STATE_MEANING` | VARCHAR(12) | NOT NULL |  | Additional text about the state of the displaced appointment. |
| 4 | `SCH_APPT_ID` | DOUBLE | NOT NULL | FK→ | The appointment ID of the displaced appointment. Relates back to the SCH_APPT table. |
| 5 | `SCH_DISPLACED_APPT_ID` | DOUBLE | NOT NULL |  | The unique primary key of this table. |
| 6 | `SCH_EVENT_ID` | DOUBLE | NOT NULL | FK→ | The scheduling event id of the displaced appointment. Relates to the SCH_EVENT table. |
| 7 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 8 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 9 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 10 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 11 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `DEF_APPLY_ID` | [SCH_DEF_APPLY](SCH_DEF_APPLY.md) | `DEF_APPLY_ID` |
| `SCH_APPT_ID` | [SCH_APPT](SCH_APPT.md) | `SCH_APPT_ID` |
| `SCH_EVENT_ID` | [SCH_EVENT](SCH_EVENT.md) | `SCH_EVENT_ID` |

