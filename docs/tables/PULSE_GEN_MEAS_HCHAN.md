# PULSE_GEN_MEAS_HCHAN

> Contains measurements for the lead high voltage channel of a pulse generator

**Description:** Pulse Generator Lead High Voltage Channel Measurement  
**Table type:** ACTIVITY  
**Primary key:** _(not published — see note)_  
**Columns:** 10

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `IMPEDANCE_AMT` | DOUBLE |  |  | The sum of the impedances of the shock lead wires and the electrode-myocardial interface in ohms |
| 2 | `MEASUREMENT_TYPE_CD` | DOUBLE | NOT NULL |  | The electric pulse type used for measuring the shock lead impedance |
| 3 | `PULSE_GEN_MEAS_HCHAN_ID` | DOUBLE | NOT NULL |  | PRIMARY KEY |
| 4 | `PULSE_GEN_MEAS_ID` | DOUBLE | NOT NULL | FK→ | The pulse generator measurement associated with this high voltage channel measurement |
| 5 | `STATUS_CD` | DOUBLE | NOT NULL |  | The indication whether to check the lead |
| 6 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 7 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 8 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 9 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 10 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `PULSE_GEN_MEAS_ID` | [PULSE_GEN_MEAS](PULSE_GEN_MEAS.md) | `PULSE_GEN_MEAS_ID` |

