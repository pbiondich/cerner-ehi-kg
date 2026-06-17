# PULSE_GEN_MEAS_CHAN

> Contains measurements for the lead channel of a pulse generator

**Description:** Pulse Generator Lead Channel Measurement  
**Table type:** ACTIVITY  
**Primary key:** _(not published — see note)_  
**Columns:** 19

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `CHAMBER_CD` | DOUBLE | NOT NULL |  | Defines which chamber of the heart this channel is located |
| 2 | `IMPEDANCE_AMT` | DOUBLE |  |  | The sum of the impedances of the lead wires and the electrode-myocardial interface in ohms |
| 3 | `PACING_THRSHLD_AMPLITUDE_VALUE` | DOUBLE |  |  | The minimum pulse amplitude needed for pacing capture for a given pulse width |
| 4 | `PACING_THRSHLD_MEAS_METHOD_CD` | DOUBLE | NOT NULL |  | The method that was used to obtain the pacing threshold |
| 5 | `PACING_THRSHLD_POLARITY_CD` | DOUBLE | NOT NULL |  | The type of lead polarity that was used for the pacing threshold measurement |
| 6 | `PACING_THRSHLD_PWIDTH_VALUE` | DOUBLE |  |  | The pulse width that was applied when determining the pacing threshold amplitude |
| 7 | `POLARITY_CD` | DOUBLE | NOT NULL |  | The type of lead polarity used for measuring the lead impedance |
| 8 | `PULSE_GEN_MEAS_CHAN_ID` | DOUBLE | NOT NULL |  | PRIMARY KEY |
| 9 | `PULSE_GEN_MEAS_ID` | DOUBLE | NOT NULL | FK→ | The pulse generator measurement associated with this lead channel measurement |
| 10 | `SENSING_INTR_AMPL_MAX_VALUE` | DOUBLE |  |  | The maximum measured amplitude of the intrinsic cardiac signal |
| 11 | `SENSING_INTR_AMPL_MEAN_VALUE` | DOUBLE |  |  | The average measured amplitude of the intrinsic cardiac signal |
| 12 | `SENSING_INTR_AMPL_MIN_VALUE` | DOUBLE |  |  | The minimum measured amplitude of the intrinsic cardiac signal |
| 13 | `SENSING_POLARITY_CD` | DOUBLE | NOT NULL |  | The type of polarity used for the intrinsic amplitude measurement |
| 14 | `STATUS_CD` | DOUBLE | NOT NULL |  | The indication whether to check the lead |
| 15 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 16 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 17 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 18 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 19 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `PULSE_GEN_MEAS_ID` | [PULSE_GEN_MEAS](PULSE_GEN_MEAS.md) | `PULSE_GEN_MEAS_ID` |

