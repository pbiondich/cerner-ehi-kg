# CDI_DOC_ENTITY_RELTN

> Table that relates cdi_pending_document id's to parent entity data for a document.

**Description:** CDI_DOC_ENTITY_RELTN  
**Table type:** ACTIVITY  
**Primary key:** _(not published — see note)_  
**Columns:** 10

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `CDI_DOC_ENTITY_RELTN_ID` | DOUBLE | NOT NULL |  | Unique generated number that identifies a single row on the CDI_DOC_ENTITY_RELTN table. |
| 2 | `CDI_PENDING_DOCUMENT_ID` | DOUBLE | NOT NULL | FK→ | ID for batch class as defined on the CDI_AC_BATCHCLASS_ID table. |
| 3 | `PARENT_ENTITY_ALIAS` | VARCHAR(200) |  |  | Parent Entity Alias for associated pending document. There may be cases where the ID is not available. For example, ACCESSION_ID may not be available on the document but the ACCESSION string is. The string is what would be stored in this column. |
| 4 | `PARENT_ENTITY_ID` | DOUBLE | NOT NULL |  | Parent Entity Id for associated pending document. |
| 5 | `PARENT_ENTITY_NAME` | VARCHAR(30) |  |  | Parent Entity Name for associated pending document. |
| 6 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 7 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 8 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 9 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 10 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `CDI_PENDING_DOCUMENT_ID` | [CDI_PENDING_DOCUMENT](CDI_PENDING_DOCUMENT.md) | `CDI_PENDING_DOCUMENT_ID` |

