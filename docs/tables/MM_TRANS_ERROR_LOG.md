# MM_TRANS_ERROR_LOG

> Mat Mgmt Transaction Error Log

**Description:** MM TRANS ERROR LOG  
**Table type:** ACTIVITY  
**Primary key:** _(not published — see note)_  
**Columns:** 15

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `CREATE_APPLCTX` | DOUBLE | NOT NULL |  | Application which created this row |
| 2 | `CREATE_DT_TM` | DATETIME | NOT NULL |  | The date/time this entry was created. |
| 3 | `CREATE_ID` | DOUBLE | NOT NULL |  | User id of person which created this row |
| 4 | `CREATE_TASK` | DOUBLE |  |  | Task which created this row |
| 5 | `ERROR_LOG_ID` | DOUBLE | NOT NULL |  | Unique, generated key for MM_TRANS_ERROR_LOG. |
| 6 | `MM_TRANS_GL_ID` | DOUBLE | NOT NULL | FK→ | Transaction General Ledger ID |
| 7 | `MM_TRANS_LINE_ID` | DOUBLE | NOT NULL | FK→ | Transaction Line ID |
| 8 | `TRANSACTION_ID` | DOUBLE | NOT NULL | FK→ | Transaction ID |
| 9 | `TRANS_COMMENT` | VARCHAR(255) |  |  | Transaction Comment |
| 10 | `TRANS_ERROR_CD` | DOUBLE | NOT NULL |  | Transaction Error Code Value |
| 11 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 12 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 13 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 14 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 15 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `MM_TRANS_GL_ID` | [MM_TRANS_GL](MM_TRANS_GL.md) | `MM_TRANS_GL_ID` |
| `MM_TRANS_LINE_ID` | [MM_TRANS_LINE](MM_TRANS_LINE.md) | `MM_TRANS_LINE_ID` |
| `TRANSACTION_ID` | [MM_TRANS_HEADER](MM_TRANS_HEADER.md) | `TRANSACTION_ID` |

