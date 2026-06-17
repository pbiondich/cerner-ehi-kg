# OEN_INTERFACE_ERR_R

> Relates the interface to an error.

**Description:** OEN INTERFACE ERR R  
**Table type:** REFERENCE  
**Primary key:** _(not published — see note)_  
**Columns:** 12

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ACTIVE_IND` | DOUBLE |  |  | The table row is active or inactive. A row is generally active unless it is in an inactive state such as logically deleted, combined away, pending purge, etc. |
| 2 | `ENHANCED_IND` | DOUBLE |  |  | Use enhanced error logic? |
| 3 | `ERROR_ID` | DOUBLE | NOT NULL | FK→ | error_idColumn |
| 4 | `ERROR_SEQ_ID` | DOUBLE | NOT NULL |  | unique id |
| 5 | `INTERFACE_ID` | DOUBLE | NOT NULL | FK→ | interface_idColumn |
| 6 | `MAX_RETRY_NBR` | DOUBLE |  |  | Maximum number of retries |
| 7 | `SEQUENCE_ID` | DOUBLE | NOT NULL | FK→ | Sequence_id |
| 8 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 9 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 10 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 11 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 12 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `ERROR_ID` | [OEN_ERROR](OEN_ERROR.md) | `ERROR_ID` |
| `INTERFACE_ID` | [OEN_INTERFACE](OEN_INTERFACE.md) | `INTERFACE_ID` |
| `SEQUENCE_ID` | [OEN_SEQUENCE](OEN_SEQUENCE.md) | `SEQUENCE_ID` |

