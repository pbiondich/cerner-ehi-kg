# SN_SURG_CASE_ST

> Contains summary data associated with surgical cases

**Description:** SurgiNet Surgical Case Summary Table  
**Table type:** ACTIVITY  
**Primary key:** _(not published — see note)_  
**Columns:** 13

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ACTUAL_SLOT_TYPE_ID` | DOUBLE | NOT NULL | FK→ | Actual Slot Type ID |
| 2 | `SCH_APPT_ID` | DOUBLE | NOT NULL |  | Scheduling Appointment ID |
| 3 | `SCH_FLEX_ID` | DOUBLE | NOT NULL | FK→ | Scheduling Flex String ID |
| 4 | `SCH_SLOT_OVERRIDE_IND` | DOUBLE |  |  | Scheduling Slot Override Indicator |
| 5 | `SCH_SLOT_STATE_MEANING` | CHAR(12) |  |  | Scheduling Slot State Meaning |
| 6 | `SCH_SLOT_TYPE_ID` | DOUBLE | NOT NULL | FK→ | Scheduled Slot Type ID |
| 7 | `SN_SURG_CASE_ST_ID` | DOUBLE | NOT NULL |  | SurgiNet Surgical Case Summary Table ID |
| 8 | `SURG_CASE_ID` | DOUBLE | NOT NULL | FK→ | Surgical Case ID |
| 9 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 10 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 11 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 12 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 13 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `ACTUAL_SLOT_TYPE_ID` | [SCH_SLOT_TYPE](SCH_SLOT_TYPE.md) | `SLOT_TYPE_ID` |
| `SCH_FLEX_ID` | [SCH_FLEX_STRING](SCH_FLEX_STRING.md) | `SCH_FLEX_ID` |
| `SCH_SLOT_TYPE_ID` | [SCH_SLOT_TYPE](SCH_SLOT_TYPE.md) | `SLOT_TYPE_ID` |
| `SURG_CASE_ID` | [SURGICAL_CASE](SURGICAL_CASE.md) | `SURG_CASE_ID` |

