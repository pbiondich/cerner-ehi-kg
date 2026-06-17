# TRACING_TICKET

> This table stores tracing/logging information among the services we own. The number of rows on this table is managed internally by Cerner and the default maximum size is 10. million.

**Description:** tracing_ticket  
**Table type:** ACTIVITY  
**Primary key:** `TRACING_TICKET_ID`  
**Columns:** 11  
**Referenced by:** 1 columns

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `CREATION_DT_TM` | DATETIME | NOT NULL |  | The date/time at which the ticket was created. |
| 2 | `GROUP_VALUE` | DOUBLE | NOT NULL |  | This field is used to organize tickets into logical groups. |
| 3 | `PARENT_TICKET_ID` | DOUBLE | NOT NULL | FK→ | This field allows recursive association between parent and child rows. A value of zero indicates a parent ticket row, while a positive value indicates a child ticket row. |
| 4 | `TICKET_SEQ` | DOUBLE | NOT NULL |  | This field indicates the depth of a ticket in a chain of services. A value of zero indicates a parent ticket row. |
| 5 | `TRACING_MSG_TXT` | VARCHAR(4000) | NOT NULL |  | This field stores tracing message for child ticket rows. |
| 6 | `TRACING_TICKET_ID` | DOUBLE | NOT NULL | PK | Unique generated number that identifies a single row on the tracing_ticket table. |
| 7 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 8 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 9 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 10 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 11 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `PARENT_TICKET_ID` | [TRACING_TICKET](TRACING_TICKET.md) | `TRACING_TICKET_ID` |

## Referenced by (1)

| From table | Column |
|------------|--------|
| [TRACING_TICKET](TRACING_TICKET.md) | `PARENT_TICKET_ID` |

