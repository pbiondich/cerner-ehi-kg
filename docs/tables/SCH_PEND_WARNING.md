# SCH_PEND_WARNING

> Warnings overridden during the booking process.

**Description:** Scheduling Pending Warning  
**Table type:** ACTIVITY  
**Primary key:** _(not published — see note)_  
**Columns:** 10

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `SCH_PEND_APPT_ID` | DOUBLE |  | FK→ | Appointment participant that the warning belongs to. |
| 2 | `SCH_PEND_WARNING_ID` | DOUBLE | NOT NULL |  | Unique generated number that identifies a single row on the SCH_PEND_WARNING table. |
| 3 | `UPDT_APPLCTX` | DOUBLE |  |  | The application context number from the record info block. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 4 | `UPDT_CNT` | DOUBLE |  |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 5 | `UPDT_DT_TM` | DATETIME |  |  | The date and time the row was last inserted or updated. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 6 | `UPDT_ID` | DOUBLE |  |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 7 | `UPDT_TASK` | DOUBLE |  |  | The registered (assigned) task number for the process that inserted or updated the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 8 | `WARN_PRSNL_ID` | DOUBLE |  | FK→ | Unique identifier of the personnel that overrode the warning. |
| 9 | `WARN_REASON_CD` | DOUBLE |  |  | Reason the warning was overridden. |
| 10 | `WARN_TYPE_CD` | DOUBLE |  |  | Type of warning being overridden. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `SCH_PEND_APPT_ID` | [SCH_PEND_APPT](SCH_PEND_APPT.md) | `SCH_PEND_APPT_ID` |
| `WARN_PRSNL_ID` | [PRSNL](PRSNL.md) | `PERSON_ID` |

