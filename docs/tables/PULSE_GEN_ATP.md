# PULSE_GEN_ATP

> Contains information about ATP zone settings for a pulse generator

**Description:** Pulse Generator ATP Zone Settings  
**Table type:** ACTIVITY  
**Primary key:** _(not published — see note)_  
**Columns:** 10

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `PULSE_GEN_ATP_ID` | DOUBLE | NOT NULL |  | PRIMARY KEY |
| 2 | `PULSE_GEN_SET_ZONE_ID` | DOUBLE | NOT NULL | FK→ | The pulse generator zone setting ID associated with this ATP zone |
| 3 | `SEQUENCE_CNT` | DOUBLE |  |  | The number of anti-tachycardia pacing pulse (ATP) sequences programmed per ATP type |
| 4 | `TYPE_CD` | DOUBLE | NOT NULL |  | The type of anti-tachycardia pacing (ATP) sequences programmed per ATP type |
| 5 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 6 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 7 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 8 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 9 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |
| 10 | `ZONE_SEQ` | DOUBLE |  |  | The sequence number for this ATP setting, from 1 to 10 |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `PULSE_GEN_SET_ZONE_ID` | [PULSE_GEN_SET_ZONE](PULSE_GEN_SET_ZONE.md) | `PULSE_GEN_SET_ZONE_ID` |

