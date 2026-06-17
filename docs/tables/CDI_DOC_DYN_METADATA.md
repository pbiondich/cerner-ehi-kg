# CDI_DOC_DYN_METADATA

> This table contains the dynamic (client defined) metadata, such as person and encounter aliases, used to index CPDI images into Millennium. The dynamic nature of the table allows for clients to choose which aliases will be used during the batch indexing process to identify the document's parent.

**Description:** CDI Document Dynamic Metadata  
**Table type:** ACTIVITY  
**Primary key:** _(not published — see note)_  
**Columns:** 10

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ALIAS_TYPE_CD` | DOUBLE | NOT NULL |  | Specifies the alias type for this data. The code set for this field can vary. It is stored in column ALIAS_TYPE_CODESET. |
| 2 | `ALIAS_TYPE_CODESET` | DOUBLE | NOT NULL |  | Specifies the code set for the ALIAS_TYPE_CDcolumn. |
| 3 | `CDI_DOC_DYN_METADATA_ID` | DOUBLE | NOT NULL |  | The unique primary key for this table. It is internally assigned by Cerner. |
| 4 | `CDI_PENDING_DOCUMENT_ID` | DOUBLE | NOT NULL | FK→ | The ID of the pending document that this metadata is associated with. |
| 5 | `FIELD_VALUE` | VARCHAR(200) |  |  | The value of the data for this alias. |
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

