# MM_XFI_CNTRCT_ACTION

> Table used to store relationships between contracts and action periods. Data is moved from this table to MM_CNTRCT_ACTION.

**Description:** MM XFI CNTRCT ACTION  
**Table type:** REFERENCE  
**Primary key:** _(not published — see note)_  
**Columns:** 22

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ACTION_DT_TM` | DATETIME |  |  | Action date/time |
| 2 | `ACTION_FLAG` | DOUBLE |  |  | Action flag for the action |
| 3 | `ACTION_ID` | DOUBLE | NOT NULL | FK→ | action identifier |
| 4 | `ACTION_PERIOD` | VARCHAR(60) |  |  | Action period |
| 5 | `ACTION_PERIOD_CD` | DOUBLE | NOT NULL |  | Action period code value |
| 6 | `ACTION_REASON` | VARCHAR(60) |  |  | Action reason |
| 7 | `ACTION_REASON_CD` | DOUBLE | NOT NULL |  | Action reason code value |
| 8 | `ACTION_USER` | VARCHAR(60) |  |  | Action user |
| 9 | `ACTION_USER_ID` | DOUBLE | NOT NULL | FK→ | Action user key |
| 10 | `CONTRIBUTOR_CD` | DOUBLE | NOT NULL |  | Contributor Source Code value |
| 11 | `CREATE_APPLCTX` | DOUBLE |  |  | The application context number from the record info block. |
| 12 | `CREATE_DT_TM` | DATETIME |  |  | The date and time the record was created |
| 13 | `CREATE_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 14 | `CREATE_TASK` | DOUBLE |  |  | The registered (assigned) task number for the process that inserted the row. |
| 15 | `PROCESS_FLAG` | DOUBLE |  |  | process flag |
| 16 | `TRANSACTION_ID` | DOUBLE | NOT NULL |  | Primary key |
| 17 | `TRANS_PARENT_ID` | DOUBLE | NOT NULL | FK→ | transaction parent identifier |
| 18 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 19 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 20 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 21 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 22 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `ACTION_ID` | [MM_CNTRCT_ACTION](MM_CNTRCT_ACTION.md) | `ACTION_ID` |
| `ACTION_USER_ID` | [PRSNL](PRSNL.md) | `PERSON_ID` |
| `TRANS_PARENT_ID` | [MM_XFI_CNTRCT_HDR](MM_XFI_CNTRCT_HDR.md) | `TRANSACTION_ID` |

