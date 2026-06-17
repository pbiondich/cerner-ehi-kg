# SI_EPRESCRIBE_REQ_LOG

> Full log of inbound ePrescribe message data for use in situations where that same data must be echoed back outbound

**Description:** SI ePrescribe Request Log  
**Table type:** ACTIVITY  
**Primary key:** _(not published — see note)_  
**Columns:** 9

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `CREATE_DT_TM` | DATETIME |  |  | Date/Time at which the row was originally written |
| 2 | `LONG_BLOB_ID` | DOUBLE | NOT NULL | FK→ | Link to row on long_blob table |
| 3 | `MESSAGE_IDENT` | VARCHAR(35) | NOT NULL |  | Transaction message identifier |
| 4 | `SI_EPRESCRIBE_REQ_LOG_ID` | DOUBLE | NOT NULL |  | Unique generated number that identifies a single row onthe table ( Primary Key ) |
| 5 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 6 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 7 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 8 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 9 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `LONG_BLOB_ID` | [LONG_BLOB](LONG_BLOB.md) | `LONG_BLOB_ID` |

