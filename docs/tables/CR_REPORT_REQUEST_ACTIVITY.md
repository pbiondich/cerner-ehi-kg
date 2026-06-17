# CR_REPORT_REQUEST_ACTIVITY

> this table serves as checkpoints for the various statuses of a ; CR_REPORT_REQUEST row. We would only INSERT and SELECT from this table

**Description:** CR REPORT REQUEST ACTIVITY  
**Table type:** ACTIVITY  
**Primary key:** _(not published — see note)_  
**Columns:** 4

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ACTION_TS` | DATETIME(6) |  |  | ACTION TIMETAMP For when thee status action occurred |
| 2 | `REPORT_REQUEST_ACTIVITY_ID` | DOUBLE | NOT NULL |  | PRIMARY KEY |
| 3 | `REPORT_REQUEST_ID` | DOUBLE |  | FK→ | Foreign key value from the CR_REPORT_REQUEST row |
| 4 | `REPORT_STATUS_CD` | DOUBLE |  |  | Current status as of this activity time (code set 367571) |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `REPORT_REQUEST_ID` | [CR_REPORT_REQUEST](CR_REPORT_REQUEST.md) | `REPORT_REQUEST_ID` |

