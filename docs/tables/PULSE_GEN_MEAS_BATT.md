# PULSE_GEN_MEAS_BATT

> Contains measurements for the battery of a pulse generator

**Description:** Pulse Generator Battery Measurement  
**Table type:** ACTIVITY  
**Primary key:** _(not published — see note)_  
**Columns:** 13

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `IMPEDANCE_NBR` | DOUBLE |  |  | The measured battery impedance |
| 2 | `PULSE_GEN_MEAS_BATT_ID` | DOUBLE | NOT NULL |  | PRIMARY KEY |
| 3 | `PULSE_GEN_MEAS_ID` | DOUBLE | NOT NULL | FK→ | The pulse generator measurement associated with this battery measurement |
| 4 | `REMAINING_LONGEVITY_AMT` | DOUBLE |  |  | The estimated amount of battery capacity remaining in months |
| 5 | `REMAINING_PERCENTAGE_VALUE` | DOUBLE |  |  | The estimated amount of battery capacity remaining in percent |
| 6 | `RRT_TRIGGER` | VARCHAR(50) |  |  | The criteria for determining battery end of service condition |
| 7 | `STATUS_CD` | DOUBLE | NOT NULL |  | The stage of battery depletion |
| 8 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 9 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 10 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 11 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 12 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |
| 13 | `VOLTAGE_VALUE` | DOUBLE |  |  | The measured battery voltage |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `PULSE_GEN_MEAS_ID` | [PULSE_GEN_MEAS](PULSE_GEN_MEAS.md) | `PULSE_GEN_MEAS_ID` |

