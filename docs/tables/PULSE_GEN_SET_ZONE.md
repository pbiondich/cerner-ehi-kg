# PULSE_GEN_SET_ZONE

> Contains information about zone settings for a pulse generator

**Description:** Pulse Generator Zone Settings  
**Table type:** ACTIVITY  
**Primary key:** `PULSE_GEN_SET_ZONE_ID`  
**Columns:** 14  
**Referenced by:** 2 columns

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `DETECTION_BEATS_DEN` | DOUBLE |  |  | The denominator portion of the tachy detection ratio in heartbeats |
| 2 | `DETECTION_BEATS_NUM` | DOUBLE |  |  | The numerator portion of the tachy detection ratio in heartbeats |
| 3 | `DETECTION_DETAILS` | VARCHAR(50) |  |  | A text describing arrhythmia detection details |
| 4 | `DETECTION_INTERVAL` | DOUBLE |  |  | The upper interval limit of the zone for tachy therapy detection in milliseconds |
| 5 | `PULSE_GEN_SET_ID` | DOUBLE | NOT NULL | FK→ | The pulse generator setting associated with this channel setting |
| 6 | `PULSE_GEN_SET_ZONE_ID` | DOUBLE | NOT NULL | PK | PRIMARY KEY |
| 7 | `STATUS_CD` | DOUBLE | NOT NULL |  | The status of the zone, whether it is is active or not |
| 8 | `TYPE_CD` | DOUBLE | NOT NULL |  | The general type of the zone for tachy therapy detection |
| 9 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 10 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 11 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 12 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 13 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |
| 14 | `VENDOR_TYPE_CD` | DOUBLE | NOT NULL |  | The vendor specific type of the zone for tachy therapy detection |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `PULSE_GEN_SET_ID` | [PULSE_GEN_SET](PULSE_GEN_SET.md) | `PULSE_GEN_SET_ID` |

## Referenced by (2)

| From table | Column |
|------------|--------|
| [PULSE_GEN_ATP](PULSE_GEN_ATP.md) | `PULSE_GEN_SET_ZONE_ID` |
| [PULSE_GEN_SET_SHOCK](PULSE_GEN_SET_SHOCK.md) | `PULSE_GEN_SET_ZONE_ID` |

