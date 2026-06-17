# MSG_DOC_FAVORITES

> To store document type ids at user or position level

**Description:** MSG DOC FAVORITES  
**Table type:** ACTIVITY  
**Primary key:** _(not published — see note)_  
**Columns:** 10

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `MSGTYPE_CD` | DOUBLE | NOT NULL |  | Message Type code for (Message/Reminder/Consult/Letter) |
| 2 | `MSG_DOC_FAVORITES_ID` | DOUBLE | NOT NULL |  | Unique generated number that identifies a single row on the MSG_DOC_FAVORITES table. |
| 3 | `NOTE_ID` | DOUBLE | NOT NULL | FK→ | Favorite document type ID for this Personnel or Position |
| 4 | `POSITION_CD` | DOUBLE | NOT NULL |  | Position Code of the Personnel |
| 5 | `PRSNL_ID` | DOUBLE | NOT NULL | FK→ | Personnel ID |
| 6 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 7 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 8 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 9 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 10 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `NOTE_ID` | [NOTE_TYPE](NOTE_TYPE.md) | `NOTE_TYPE_ID` |
| `PRSNL_ID` | [PRSNL](PRSNL.md) | `PERSON_ID` |

