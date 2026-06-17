# REGIMEN_DETAIL_ACTION

> Storage for actions taken on regimen detail row

**Description:** Regimen Detail Action  
**Table type:** ACTIVITY  
**Primary key:** _(not published — see note)_  
**Columns:** 14

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ACTION_DT_TM` | DATETIME | NOT NULL |  | Indicates the date and time the action was taken on the regimen detail |
| 2 | `ACTION_PRSNL_ID` | DOUBLE | NOT NULL | FK→ | Indicates the person who took the action on the regimen detail |
| 3 | `ACTION_REASON_CD` | DOUBLE | NOT NULL |  | Indicates the codified action reason on the regimen detail |
| 4 | `ACTION_TYPE_CD` | DOUBLE | NOT NULL |  | Indicates the type of action taken on the regimen detail |
| 5 | `ACTION_TZ` | DOUBLE | NOT NULL |  | Action time zone |
| 6 | `LONG_TEXT_ID` | DOUBLE | NOT NULL | FK→ | Indicates the action comment on the regimen detail. Pointer to the long text table entry. |
| 7 | `REGIMEN_DETAIL_ACTION_ID` | DOUBLE | NOT NULL |  | sequence name: CareNet_seq Unique identifier for the REGIMEN_DETAIL_ACTION table. |
| 8 | `REGIMEN_DETAIL_ID` | DOUBLE | NOT NULL | FK→ | sequence name: CareNet_seq Unique identifier for the REGIMEN_DETAIL table. |
| 9 | `REGIMEN_ID` | DOUBLE | NOT NULL | FK→ | sequence name: CareNet_seq Unique identifier for the REGIMEN table. |
| 10 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 11 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 12 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 13 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 14 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `ACTION_PRSNL_ID` | [PRSNL](PRSNL.md) | `PERSON_ID` |
| `LONG_TEXT_ID` | [LONG_TEXT](LONG_TEXT.md) | `LONG_TEXT_ID` |
| `REGIMEN_DETAIL_ID` | [REGIMEN_DETAIL](REGIMEN_DETAIL.md) | `REGIMEN_DETAIL_ID` |
| `REGIMEN_ID` | [REGIMEN](REGIMEN.md) | `REGIMEN_ID` |

