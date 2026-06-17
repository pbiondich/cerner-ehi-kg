# PULSE_GEN_SET_TACHY

> Contains information about Tachycardia settings for a pulse generator

**Description:** Pulse Generator Tachycardia Settings  
**Table type:** ACTIVITY  
**Primary key:** _(not published — see note)_  
**Columns:** 9

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ASTAT_CD` | DOUBLE | NOT NULL |  | The high level programmed status for atrial tachy therapies |
| 2 | `PULSE_GEN_SET_ID` | DOUBLE | NOT NULL | FK→ | The pulse generator setting associated with this channel setting |
| 3 | `PULSE_GEN_SET_TACHY_ID` | DOUBLE | NOT NULL |  | PRIMARY KEY |
| 4 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 5 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 6 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 7 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 8 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |
| 9 | `VSTAT_CD` | DOUBLE | NOT NULL |  | The high level programmed status for ventricular tachy therapies |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `PULSE_GEN_SET_ID` | [PULSE_GEN_SET](PULSE_GEN_SET.md) | `PULSE_GEN_SET_ID` |

