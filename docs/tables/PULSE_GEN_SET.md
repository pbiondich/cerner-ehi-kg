# PULSE_GEN_SET

> Parent of all pulse generator settings.

**Description:** Pulse Generator Setting  
**Table type:** ACTIVITY  
**Primary key:** `PULSE_GEN_SET_ID`  
**Columns:** 8  
**Referenced by:** 6 columns

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `PULSE_GEN_ID` | DOUBLE | NOT NULL | FK→ | The pulse generator associated with this setting |
| 2 | `PULSE_GEN_SET_ID` | DOUBLE | NOT NULL | PK | PRIMARY KEY |
| 3 | `SET_DT_TM` | DATETIME | NOT NULL |  | The date and time this setting was set on the pulse generator |
| 4 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 5 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 6 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 7 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 8 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `PULSE_GEN_ID` | [PULSE_GEN](PULSE_GEN.md) | `PULSE_GEN_ID` |

## Referenced by (6)

| From table | Column |
|------------|--------|
| [PULSE_GEN_SET_BRADY](PULSE_GEN_SET_BRADY.md) | `PULSE_GEN_SET_ID` |
| [PULSE_GEN_SET_CHAN](PULSE_GEN_SET_CHAN.md) | `PULSE_GEN_SET_ID` |
| [PULSE_GEN_SET_CRT](PULSE_GEN_SET_CRT.md) | `PULSE_GEN_SET_ID` |
| [PULSE_GEN_SET_MAG](PULSE_GEN_SET_MAG.md) | `PULSE_GEN_SET_ID` |
| [PULSE_GEN_SET_TACHY](PULSE_GEN_SET_TACHY.md) | `PULSE_GEN_SET_ID` |
| [PULSE_GEN_SET_ZONE](PULSE_GEN_SET_ZONE.md) | `PULSE_GEN_SET_ID` |

