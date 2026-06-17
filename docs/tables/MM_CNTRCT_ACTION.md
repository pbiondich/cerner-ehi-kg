# MM_CNTRCT_ACTION

> Contract Action

**Description:** MM CNTRCT ACTION  
**Table type:** REFERENCE  
**Primary key:** `ACTION_ID`  
**Columns:** 16  
**Referenced by:** 1 columns

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ACTION_DT_TM` | DATETIME |  |  | Action date/time |
| 2 | `ACTION_ID` | DOUBLE | NOT NULL | PK | action identifier |
| 3 | `CNTRCT_ID` | DOUBLE | NOT NULL | FK→ | Contract number key |
| 4 | `CREATE_APPLCTX` | DOUBLE |  |  | The application context number from the record info block. |
| 5 | `CREATE_DT_TM` | DATETIME |  |  | The date and time the row was inserted. |
| 6 | `CREATE_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) who inserted the row in to the table. |
| 7 | `CREATE_TASK` | DOUBLE |  |  | Task which created this row |
| 8 | `NOTIFICATION_IND` | DOUBLE |  |  | notification indicator |
| 9 | `PERIOD_CD` | DOUBLE | NOT NULL |  | %etc |
| 10 | `PRSNL_ID` | DOUBLE | NOT NULL | FK→ | Foreign key, the prsnl_id of the person from the personnel table (prsnl) |
| 11 | `REASON_CD` | DOUBLE | NOT NULL |  | Reason Code Value |
| 12 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 13 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 14 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 15 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 16 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `CNTRCT_ID` | [MM_CNTRCT_HDR](MM_CNTRCT_HDR.md) | `CNTRCT_ID` |
| `PRSNL_ID` | [PRSNL](PRSNL.md) | `PERSON_ID` |

## Referenced by (1)

| From table | Column |
|------------|--------|
| [MM_XFI_CNTRCT_ACTION](MM_XFI_CNTRCT_ACTION.md) | `ACTION_ID` |

