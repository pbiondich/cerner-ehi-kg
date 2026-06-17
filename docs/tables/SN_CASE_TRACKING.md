# SN_CASE_TRACKING

> Surginet Case Tracking Table

**Description:** Surginet Case Tracking  
**Table type:** ACTIVITY  
**Primary key:** _(not published — see note)_  
**Columns:** 10

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ANTICIPATED_DURATION` | DOUBLE |  |  | The anticipated duration of the surgical case. Defaults to the scheduled duration, but may be over-ridden by the user. This field can be null. |
| 2 | `ANTICIPATED_OP_LOC_CD` | DOUBLE | NOT NULL |  | Anticipated Operating room location code |
| 3 | `ANTICIPATED_START_DT_TM` | DATETIME |  |  | The anticipated start time of the surgical case. Defaults to the scheduled start time, but may be over-ridden by the user. When the actual start time is documented, this field is updated with that value and may no longer be modified. This field can be null. |
| 4 | `SN_CASE_TRACKING_ID` | DOUBLE | NOT NULL |  | Unique identifier. |
| 5 | `SURG_CASE_ID` | DOUBLE | NOT NULL | FK→ | Foreign key to the SURGICAL_CASE table. |
| 6 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 7 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 8 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 9 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 10 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `SURG_CASE_ID` | [SURGICAL_CASE](SURGICAL_CASE.md) | `SURG_CASE_ID` |

