# RAD_PROTOCOL_DEFINITION

> Stores instructions about how to perform tasks related to an orderable.

**Description:** RadNet Protocol Definition  
**Table type:** REFERENCE  
**Primary key:** `RAD_PROTOCOL_DEFINITION_ID`  
**Columns:** 9  
**Referenced by:** 3 columns

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ACTIVE_IND` | DOUBLE | NOT NULL |  | The table row is active or inactive. A row is generally active unless it is in an inactive state such as logically deleted, combined away, pending purge, etc. |
| 2 | `PROTOCOL_DESC_TXT` | VARCHAR(512) | NOT NULL |  | Description of the protocol. |
| 3 | `PROTOCOL_NAME` | VARCHAR(40) | NOT NULL |  | The name of the protocol. |
| 4 | `RAD_PROTOCOL_DEFINITION_ID` | DOUBLE | NOT NULL | PK | Unique, generated number that identifies a single row on the RAD_PROTOCOL_DEFINITION table. |
| 5 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 6 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 7 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 8 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 9 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Referenced by (3)

| From table | Column |
|------------|--------|
| [RAD_PROTOCOL_ACT](RAD_PROTOCOL_ACT.md) | `PROTOCOL_ID` |
| [RAD_PROTOCOL_ACT_HIST](RAD_PROTOCOL_ACT_HIST.md) | `PROTOCOL_ID` |
| [RAD_PROTOCOL_CATALOG_R](RAD_PROTOCOL_CATALOG_R.md) | `RAD_PROTOCOL_DEFINITION_ID` |

