# PULSE_GEN_SET_CHAN

> Contains information about lead voltage channel settings for a pulse generator

**Description:** Pulse Generator Channel Settings  
**Table type:** ACTIVITY  
**Primary key:** `PULSE_GEN_SET_CHAN_ID`  
**Columns:** 16  
**Referenced by:** 1 columns

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `CHAMBER_CD` | DOUBLE | NOT NULL |  | Defines which chamber of the heart this channel is located. If this channel is a high voltage channel, this value will be zero. |
| 2 | `HVCHAN_IND` | DOUBLE | NOT NULL |  | One if this channel is a high voltage channel. Zero otherwise. |
| 3 | `PACING_AMPLITUDE_VALUE` | DOUBLE | NOT NULL |  | The pacing output amplitude in volts. If this channel is a high voltage channel, this value will be zero. |
| 4 | `PACING_CAPTURE_MODE_CD` | DOUBLE | NOT NULL |  | The method the device uses for managing pacing capture. If this channel is a high voltage channel, this value will be zero. |
| 5 | `PACING_POLARITY_CD` | DOUBLE | NOT NULL |  | The indication of unipolar or bipolar configuration for pacing. If this channel is a high voltage channel, this value will be zero. |
| 6 | `PACING_PULSEWIDTH_VALUE` | DOUBLE | NOT NULL |  | The pacing output pulse width in milliseconds. If this channel is a high voltage channel, this value will be zero. |
| 7 | `PULSE_GEN_SET_CHAN_ID` | DOUBLE | NOT NULL | PK | PRIMARY KEY |
| 8 | `PULSE_GEN_SET_ID` | DOUBLE | NOT NULL | FK→ | The pulse generator setting associated with this channel setting |
| 9 | `SENSING_ADAPTATION_MODE_CD` | DOUBLE | NOT NULL |  | Specifies whether the sensitivity is fixed or adapting. If this channel is a high voltage channel, this value will be zero. |
| 10 | `SENSING_POLARITY_CD` | DOUBLE | NOT NULL |  | The indication of unipolar or bipolar configuration for sensing. If this channel is a high voltage channel, this value will be zero. |
| 11 | `SENSING_SENSITIVITY_VALUE` | DOUBLE | NOT NULL |  | The smallest electrical signal programmed to be detected by the device's sensing circuitry in millivolts. If this channel is a high voltage channel, this value will be zero. |
| 12 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 13 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 14 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 15 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 16 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `PULSE_GEN_SET_ID` | [PULSE_GEN_SET](PULSE_GEN_SET.md) | `PULSE_GEN_SET_ID` |

## Referenced by (1)

| From table | Column |
|------------|--------|
| [PULSE_GEN_SET_NODE](PULSE_GEN_SET_NODE.md) | `PULSE_GEN_SET_CHAN_ID` |

