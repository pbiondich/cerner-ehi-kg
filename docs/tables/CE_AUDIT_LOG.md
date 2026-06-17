# CE_AUDIT_LOG

> Stores audit information for failed personnel action requests that are executed asynchronously through the clinical event server.

**Description:** Clinical Event Audit Log  
**Table type:** ACTIVITY  
**Primary key:** _(not published — see note)_  
**Columns:** 13

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `CE_AUDIT_LOG_ID` | DOUBLE | NOT NULL |  | Unique, generated number that identifies a single row on the CE_AUDIT_LOG table. |
| 2 | `ERROR_MSG_TXT` | VARCHAR(255) |  |  | The error associated with a transaction failure. |
| 3 | `EVENT_ID` | DOUBLE | NOT NULL |  | Used to identify a clinical event row for the given audit log row. |
| 4 | `OPERATION_DT_TM` | DATETIME | NOT NULL |  | Date the action on the clinical event row failed. |
| 5 | `OPERATION_PRSNL_ID` | DOUBLE | NOT NULL | FK→ | The personnel id of the person executing a failing action on the clinical event row. |
| 6 | `OPERATION_STATUS_CD` | DOUBLE | NOT NULL |  | The status of the row as the clinical event is being updated,. Valid values are Processing and Completed. |
| 7 | `OPERATION_TYPE_CD` | DOUBLE | NOT NULL |  | Identifies the operation that failed on the clinical event row. |
| 8 | `PERSON_ID` | DOUBLE | NOT NULL | FK→ | The person that is associated with the clinical event row that was being updated. |
| 9 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 10 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 11 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 12 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 13 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `OPERATION_PRSNL_ID` | [PRSNL](PRSNL.md) | `PERSON_ID` |
| `PERSON_ID` | [PERSON](PERSON.md) | `PERSON_ID` |

