# MODEM_COMMANDS

> Identifies the various modem commands associated with each modem.

**Description:** MODEM COMMANDS  
**Table type:** REFERENCE  
**Primary key:** _(not published — see note)_  
**Columns:** 13

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `COMMAND_STRING` | VARCHAR(100) |  |  | String which contains specific modem commands for a particular Modem Type.Column |
| 2 | `COMMAND_TYPE_CD` | DOUBLE | NOT NULL |  | Identifies that type of command being sent to the modem.Column |
| 3 | `CR_LF_IND` | DOUBLE |  |  | Indicates whether to send a carriage return line feed commands to the device. |
| 4 | `DELAY` | DOUBLE |  |  | How many seconds to wait before sending the command.Column |
| 5 | `EXP_RESPONSE` | CHAR(20) |  |  | What type of response is expected from the modem when the command string is sent. |
| 6 | `MODEM_TYPE_ID` | DOUBLE | NOT NULL | FK→ | The type of modem.Column |
| 7 | `QUALIFIER` | DOUBLE | NOT NULL |  | A unique number identifying the command string for a particular modem typeColumn |
| 8 | `REMOTE_DEV_TYPE_ID` | DOUBLE | NOT NULL |  | Indicates what remote device type is using this modem.Column |
| 9 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 10 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 11 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 12 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 13 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `MODEM_TYPE_ID` | [MODEM_TYPE](MODEM_TYPE.md) | `MODEM_TYPE_ID` |

