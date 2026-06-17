# PULSE_GEN_STAT

> Contains the start and end date and time of a pulse generator statistic

**Description:** Pulse Generator Statistic  
**Table type:** ACTIVITY  
**Primary key:** `PULSE_GEN_STAT_ID`  
**Columns:** 9  
**Referenced by:** 5 columns

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `END_DT_TM` | DATETIME |  |  | The date and time that this statistic ended |
| 2 | `PULSE_GEN_ID` | DOUBLE | NOT NULL | FK→ | The pulse generator associated with this pulse generator statistic |
| 3 | `PULSE_GEN_STAT_ID` | DOUBLE | NOT NULL | PK | PRIMARY KEY |
| 4 | `START_DT_TM` | DATETIME |  |  | The date and time that this statistic began |
| 5 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 6 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 7 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 8 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 9 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `PULSE_GEN_ID` | [PULSE_GEN](PULSE_GEN.md) | `PULSE_GEN_ID` |

## Referenced by (5)

| From table | Column |
|------------|--------|
| [PULSE_GEN_STAT_AT](PULSE_GEN_STAT_AT.md) | `PULSE_GEN_STAT_ID` |
| [PULSE_GEN_STAT_BRADY](PULSE_GEN_STAT_BRADY.md) | `PULSE_GEN_STAT_ID` |
| [PULSE_GEN_STAT_CRT](PULSE_GEN_STAT_CRT.md) | `PULSE_GEN_STAT_ID` |
| [PULSE_GEN_STAT_HR](PULSE_GEN_STAT_HR.md) | `PULSE_GEN_STAT_ID` |
| [PULSE_GEN_STAT_TACHY](PULSE_GEN_STAT_TACHY.md) | `PULSE_GEN_STAT_ID` |

