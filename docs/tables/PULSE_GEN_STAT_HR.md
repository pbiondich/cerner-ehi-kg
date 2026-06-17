# PULSE_GEN_STAT_HR

> Contains statistics froma single heart rate recording

**Description:** Pulse Generator Heart Rate Statistics  
**Table type:** ACTIVITY  
**Primary key:** _(not published — see note)_  
**Columns:** 13

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `A_MAX_VAL` | DOUBLE |  |  | The maximum atrial heart rate |
| 2 | `A_MEAN_VAL` | DOUBLE |  |  | The average atrial heart rate |
| 3 | `A_MIN_VAL` | DOUBLE |  |  | The minimum atrial heart rate |
| 4 | `PULSE_GEN_STAT_HR_ID` | DOUBLE | NOT NULL |  | PRIMARY KEY |
| 5 | `PULSE_GEN_STAT_ID` | DOUBLE | NOT NULL | FK→ | The pulse generator statistic associated with this heart rate statistic |
| 6 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 7 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 8 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 9 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 10 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |
| 11 | `V_MAX_VAL` | DOUBLE |  |  | The maximum ventricular heart rate |
| 12 | `V_MEAN_VAL` | DOUBLE |  |  | The average ventricular heart rate |
| 13 | `V_MIN_VAL` | DOUBLE |  |  | The minimum ventricular heart rate |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `PULSE_GEN_STAT_ID` | [PULSE_GEN_STAT](PULSE_GEN_STAT.md) | `PULSE_GEN_STAT_ID` |

