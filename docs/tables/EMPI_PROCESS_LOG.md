# EMPI_PROCESS_LOG

> Person managements conversation options.

**Description:** EMPI PROCESS LOG  
**Table type:** ACTIVITY  
**Primary key:** _(not published — see note)_  
**Columns:** 11

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `AUTO_RECONCILES_CNT` | DOUBLE |  |  | Number of Auto Reconciles. |
| 2 | `CREATE_DT_TM` | DATETIME | NOT NULL |  | Date and time row was created. |
| 3 | `EMPI_PROCESS` | DOUBLE | NOT NULL |  | EMPI Process which created the row. |
| 4 | `EMPI_PROCESS_LOG_ID` | DOUBLE | NOT NULL |  | Unique identifier for the Empi_process_log table. |
| 5 | `MATCHES_CNT` | DOUBLE |  |  | Number of matches. |
| 6 | `PERSON_ID` | DOUBLE | NOT NULL | FK→ | This is the value of the unique primary identifier of the person table. It is an internal system assigned number. |
| 7 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 8 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 9 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 10 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 11 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `PERSON_ID` | [PERSON](PERSON.md) | `PERSON_ID` |

