# RAD_PROTOCOL_CATALOG_R

> Stores the relationship between protocols and the procedures they may be used for in specific exam rooms.

**Description:** RadNet Protocol Catalog Relation  
**Table type:** REFERENCE  
**Primary key:** _(not published — see note)_  
**Columns:** 10

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `CATALOG_CD` | DOUBLE | NOT NULL | FK→ | The orderable that pertains to a specific protocol. |
| 2 | `DEFAULT_IND` | DOUBLE | NOT NULL |  | Indicates that this is the default Protocol for this combination of Orderable and Service Resource. |
| 3 | `RAD_PROTOCOL_CATALOG_R_ID` | DOUBLE | NOT NULL |  | Unique, generated number that identifies a single row on the RAD_PROTOCOL_CATALOG_R table. |
| 4 | `RAD_PROTOCOL_DEFINITION_ID` | DOUBLE | NOT NULL | FK→ | The protocol that pertains to a specific radiology orderable. |
| 5 | `SERVICE_RESOURCE_CD` | DOUBLE | NOT NULL | FK→ | The Service Resource for this orderable/protocol combination. Usually denotes a room. |
| 6 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 7 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 8 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 9 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 10 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `CATALOG_CD` | [SERVICE_DIRECTORY](SERVICE_DIRECTORY.md) | `CATALOG_CD` |
| `RAD_PROTOCOL_DEFINITION_ID` | [RAD_PROTOCOL_DEFINITION](RAD_PROTOCOL_DEFINITION.md) | `RAD_PROTOCOL_DEFINITION_ID` |
| `SERVICE_RESOURCE_CD` | [SERVICE_RESOURCE](SERVICE_RESOURCE.md) | `SERVICE_RESOURCE_CD` |

