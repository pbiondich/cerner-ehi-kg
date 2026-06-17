# REGIMEN_ACTION

> Storage for actions taken on regimens

**Description:** Regimen Action  
**Table type:** ACTIVITY  
**Primary key:** _(not published — see note)_  
**Columns:** 13

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ACTION_DT_TM` | DATETIME | NOT NULL |  | Indicates the date and time the action was taken on the regimen |
| 2 | `ACTION_PRSNL_ID` | DOUBLE | NOT NULL |  | Indicates the person who took the action on the regimen |
| 3 | `ACTION_TYPE_CD` | DOUBLE | NOT NULL |  | Indicates the type of action taken on the regimen |
| 4 | `ACTION_TZ` | DOUBLE | NOT NULL |  | TIME ZONE FOR THE ACTION DATE TIME |
| 5 | `DISCONTINUE_REASON_CD` | DOUBLE | NOT NULL |  | Indicates the codified reason for the discontinue action taken on the regimen |
| 6 | `LONG_TEXT_ID` | DOUBLE | NOT NULL | FK→ | Contains the free text reason for the action taken on the regimen |
| 7 | `REGIMEN_ACTION_ID` | DOUBLE | NOT NULL |  | sequence name: CareNet_seq Unique identifier for the REGIMEN_ACTION table. |
| 8 | `REGIMEN_ID` | DOUBLE | NOT NULL | FK→ | sequence name: CareNet_seq Unique identifier for the REGIMEN table. |
| 9 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 10 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 11 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 12 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 13 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `LONG_TEXT_ID` | [LONG_TEXT](LONG_TEXT.md) | `LONG_TEXT_ID` |
| `REGIMEN_ID` | [REGIMEN](REGIMEN.md) | `REGIMEN_ID` |

