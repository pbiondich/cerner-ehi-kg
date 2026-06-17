# OS_RBLD_MSG

> Log table for order sentence rebuild utility

**Description:** OS_RBLD_MSG  
**Table type:** ACTIVITY  
**Primary key:** _(not published — see note)_  
**Columns:** 12

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `MESSAGE_SEQUENCE` | DOUBLE | NOT NULL |  | The sequence of the message |
| 2 | `MESSAGE_TXT` | VARCHAR(500) | NOT NULL |  | The message text |
| 3 | `OS_RBLD_MSG_ID` | DOUBLE | NOT NULL |  | Unique generated number that identifies a single row on the OS_RBLD_MSG table. |
| 4 | `OS_RBLD_ORD_SENT_DET_ID` | DOUBLE | NOT NULL | FK→ | The identifier of the rebuilt order sentence detail this detail record belongs to. |
| 5 | `OS_RBLD_ORD_SENT_ID` | DOUBLE | NOT NULL | FK→ | The identifier of the rebuilt order sentence this detail record belongs to. |
| 6 | `SEVERITY_FLAG` | DOUBLE | NOT NULL |  | The severity of the message. 1=informational 2=warning 3=error |
| 7 | `TYPE_FLAG` | DOUBLE | NOT NULL |  | Indicates where the message was generated. 1=rebuild 2=ensure |
| 8 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 9 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 10 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 11 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 12 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `OS_RBLD_ORD_SENT_DET_ID` | [OS_RBLD_ORD_SENT_DET](OS_RBLD_ORD_SENT_DET.md) | `OS_RBLD_ORD_SENT_DET_ID` |
| `OS_RBLD_ORD_SENT_ID` | [OS_RBLD_ORD_SENT](OS_RBLD_ORD_SENT.md) | `OS_RBLD_ORD_SENT_ID` |

