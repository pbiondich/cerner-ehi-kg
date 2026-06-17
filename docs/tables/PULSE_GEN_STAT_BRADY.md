# PULSE_GEN_STAT_BRADY

> Contains statistics from a single Bradycardia event

**Description:** Pulse Generator Bradycardia Statistics  
**Table type:** ACTIVITY  
**Primary key:** _(not published — see note)_  
**Columns:** 13

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `AP_VP_PERCENT` | DOUBLE |  |  | The percentage of atrial pace - ventricular pace sequences in relationship to all AV sequences |
| 2 | `AP_VS_PERCENT` | DOUBLE |  |  | The percentage of atrial pace - ventricular sense sequences in relationship to all AV sequences |
| 3 | `AS_VP_PERCENT` | DOUBLE |  |  | The percentage of atrial sense - ventricular pace sequences in relationship to all AV sequences |
| 4 | `AS_VS_PERCENT` | DOUBLE |  |  | The percentage of atrial sense - ventricular sense sequences in relationship to all AV sequences |
| 5 | `PULSE_GEN_STAT_BRADY_ID` | DOUBLE | NOT NULL |  | PRIMARY KEY |
| 6 | `PULSE_GEN_STAT_ID` | DOUBLE | NOT NULL | FK→ | The pulse generator statistic associated with this brady statistic |
| 7 | `RA_PACED_PERCENT` | DOUBLE |  |  | The percentage of pacing events in the right atrium |
| 8 | `RV_PACED_PERCENT` | DOUBLE |  |  | The percentage of pacing events in the right ventrical |
| 9 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 10 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 11 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 12 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 13 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `PULSE_GEN_STAT_ID` | [PULSE_GEN_STAT](PULSE_GEN_STAT.md) | `PULSE_GEN_STAT_ID` |

