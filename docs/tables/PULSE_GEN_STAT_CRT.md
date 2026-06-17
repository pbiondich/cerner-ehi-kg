# PULSE_GEN_STAT_CRT

> Contains statistics from a single CRT event

**Description:** Pulse Generator CRT Statistics  
**Table type:** ACTIVITY  
**Primary key:** _(not published — see note)_  
**Columns:** 9

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `CRT_PACED_PERCENT` | DOUBLE |  |  | The percentage of LV pacing events due to CRT mode in relation to all ventricular events |
| 2 | `LV_PACED_PERCENT` | DOUBLE |  |  | The percentage of LV pacing events in relation to all LV events |
| 3 | `PULSE_GEN_STAT_CRT_ID` | DOUBLE | NOT NULL |  | PRIMARY KEY |
| 4 | `PULSE_GEN_STAT_ID` | DOUBLE | NOT NULL | FK→ | The pulse generator statistic associated with this CRT statistic |
| 5 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 6 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 7 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 8 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 9 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `PULSE_GEN_STAT_ID` | [PULSE_GEN_STAT](PULSE_GEN_STAT.md) | `PULSE_GEN_STAT_ID` |

