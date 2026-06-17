# PASSIVE_ALERT_POSITION

> Identify position codes relarted to a Passive Alert

**Description:** PASSIVE ALERT POSITION  
**Table type:** ACTIVITY  
**Primary key:** _(not published — see note)_  
**Columns:** 8

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `PASSIVE_ALERT_ID` | DOUBLE | NOT NULL | FK→ | Value of the unique primary identifier of the PASSIVE_ALERT table. It is an internal system assigned number. |
| 2 | `PASSIVE_ALERT_POSITION_ID` | DOUBLE | NOT NULL |  | PRIMARY KEY |
| 3 | `POSITION_CD` | DOUBLE | NOT NULL | FK→ | POSITION CODE From The Position Code Set |
| 4 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 5 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 6 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 7 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 8 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `PASSIVE_ALERT_ID` | [PASSIVE_ALERT](PASSIVE_ALERT.md) | `PASSIVE_ALERT_ID` |
| `POSITION_CD` | [CODE_VALUE](CODE_VALUE.md) | `CODE_VALUE` |

