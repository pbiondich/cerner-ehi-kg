# PULSE_GEN_SET_NODE

> Contains information about a pulse generator lead channel anode or cathode

**Description:** Pulse Generator Node  
**Table type:** ACTIVITY  
**Primary key:** _(not published — see note)_  
**Columns:** 15

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ELECTRODE_1_CD` | DOUBLE | NOT NULL |  | Defines the type of electrode for the node |
| 2 | `ELECTRODE_2_CD` | DOUBLE | NOT NULL |  | Defines the type of electrode for the node |
| 3 | `ELECTRODE_3_CD` | DOUBLE | NOT NULL |  | Defines the type of electrode for the node |
| 4 | `LOCATION_1_CD` | DOUBLE | NOT NULL |  | Defines the location of the node |
| 5 | `LOCATION_2_CD` | DOUBLE | NOT NULL |  | Defines the location of the node |
| 6 | `LOCATION_3_CD` | DOUBLE | NOT NULL |  | Defines the location of the node |
| 7 | `NODE_FUNCTION_CD` | DOUBLE | NOT NULL |  | Whether this node is a sensing or a pacing node |
| 8 | `NODE_TYPE_CD` | DOUBLE | NOT NULL |  | Whether this node is an anode or a cathode |
| 9 | `PULSE_GEN_SET_CHAN_ID` | DOUBLE | NOT NULL | FK→ | The channel setting associated with this node |
| 10 | `PULSE_GEN_SET_NODE_ID` | DOUBLE | NOT NULL |  | PRIMARY KEY |
| 11 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 12 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 13 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 14 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 15 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `PULSE_GEN_SET_CHAN_ID` | [PULSE_GEN_SET_CHAN](PULSE_GEN_SET_CHAN.md) | `PULSE_GEN_SET_CHAN_ID` |

