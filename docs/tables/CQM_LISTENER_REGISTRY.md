# CQM_LISTENER_REGISTRY

> The CQM listener registry table identifies the trigger explosion (or transaction routing) dynamics. This table associated the CQM routing parameters to listener applications that are presented in the CQM listener configuration table.

**Description:** CQM Listener Registry  
**Table type:** REFERENCE  
**Primary key:** _(not published — see note)_  
**Columns:** 15

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `CLASS` | VARCHAR(15) |  |  | Identifies the trigger explosion class of the transaction. |
| 2 | `CREATE_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was inserted. |
| 3 | `DEBUG_IND` | DOUBLE |  |  | Defines whether debugging is active or inactive for the trigger explosion routing identified by this row |
| 4 | `LISTENER_ID` | DOUBLE | NOT NULL | FK→ | This is the value of the unique primary identifier of the CQM listener configuration table. It is an internal system assigned number. |
| 5 | `REGISTRY_ID` | DOUBLE | NOT NULL |  | This is the value of the unique primary identifier of the CQM listener registry table. It is an internal system assigned number. |
| 6 | `SUBTYPE` | VARCHAR(15) |  |  | Identifies the trigger explosion subtype of the transaction. |
| 7 | `SUBTYPE_DETAIL` | VARCHAR(15) |  |  | Identifies the trigger explosion subtype detail of the transaction. |
| 8 | `TARGET_PRIORITY` | DOUBLE |  |  | Identifies the priority of a target transaction row in the listener trigger table for the trigger explosion routing identified in this row. The value range for priority is 1 throug 99, highest to lowest, respectively. |
| 9 | `TYPE` | VARCHAR(15) |  |  | Identifies the trigger explosion type of the transaction. |
| 10 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 11 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 12 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 13 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 14 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |
| 15 | `VERBOSITY_FLAG` | DOUBLE |  |  | Defines the verbosity level during debugging for the trigger explosion routing identified in this row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `LISTENER_ID` | [CQM_LISTENER_CONFIG](CQM_LISTENER_CONFIG.md) | `LISTENER_ID` |

