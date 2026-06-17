# PULSE_GEN_SET_BRADY

> Contains statistics from a single Bradycardia event

**Description:** Pulse Generator Bradycardia Statistics  
**Table type:** ACTIVITY  
**Primary key:** _(not published — see note)_  
**Columns:** 21

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `AT_MODE_SWITCH_MODE_CD` | DOUBLE | NOT NULL |  | The atrial tachycardia mode switch mode |
| 2 | `AT_MODE_SWITCH_RATE` | DOUBLE |  |  | The atrial tachycardia mode switch rate in beats per minute |
| 3 | `HYST_RATE` | DOUBLE |  |  | The lower rate for the hysteresis feature in beats per minute |
| 4 | `LOW_RATE` | DOUBLE |  |  | The rate in beats per minute at which the device paces in the absence of a cardiac rhythm faster than the lower rate and without influence from features that can affect the pacing rate |
| 5 | `MAX_SENSOR_RATE` | DOUBLE |  |  | The fastest sensor-driven pacing rate in beats per minute that can be achieved in a rate-adaptive pacing system |
| 6 | `MAX_TRACKING_RATE` | DOUBLE |  |  | The fastest atrial rate in beats per minute at which ventricular pacing occurs with 1:1 synchrony |
| 7 | `MODE_CD` | DOUBLE | NOT NULL |  | The brady pacing mode according to the NBG standard |
| 8 | `NIGHT_RATE` | DOUBLE |  |  | The lower rate for the night rate feature in beats per minute |
| 9 | `PAV_DELAY_HIGH_INTERVAL` | DOUBLE |  |  | The high interval from a paced atrial event to a paced ventricular event in milliseconds |
| 10 | `PAV_DELAY_LOW_INTERVAL` | DOUBLE |  |  | The low interval from a paced atrial event to a paced ventricular event in milliseconds |
| 11 | `PULSE_GEN_SET_BRADY_ID` | DOUBLE | NOT NULL |  | PRIMARY KEY |
| 12 | `PULSE_GEN_SET_ID` | DOUBLE | NOT NULL | FK→ | The pulse generator setting associated with this brady setting |
| 13 | `SAV_DELAY_HIGH_INTERVAL` | DOUBLE |  |  | The high interval from an intrinsic (sensed) P wave to a paced ventricular event in milliseconds |
| 14 | `SAV_DELAY_LOW_INTERVAL` | DOUBLE |  |  | The low interval from an intrinsic (sensed) P wave to a paced ventricular event in milliseconds |
| 15 | `SENSOR_TYPE` | VARCHAR(20) |  |  | The type of sensor applied for rate adaptive pacing |
| 16 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 17 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 18 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 19 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 20 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |
| 21 | `VENDOR_MODE` | VARCHAR(20) |  |  | The brady pacing mode as defined by vendor specific codes |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `PULSE_GEN_SET_ID` | [PULSE_GEN_SET](PULSE_GEN_SET.md) | `PULSE_GEN_SET_ID` |

