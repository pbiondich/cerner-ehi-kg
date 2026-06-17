# CDI_DOCUMENT_CHECKOUT

> Tracks user checkouts of CPDI documents.

**Description:** CPDI Document Checkout  
**Table type:** ACTIVITY  
**Primary key:** _(not published — see note)_  
**Columns:** 11

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `AX_APPID` | DOUBLE | NOT NULL |  | The Application Identification from the OTG database for this document. |
| 2 | `AX_DOCID` | DOUBLE | NOT NULL |  | The document Identification from the OTG database for this document. |
| 3 | `BLOB_HANDLE` | VARCHAR(255) | NOT NULL |  | Identifier of the document that is checked out. |
| 4 | `CDI_DOCUMENT_CHECKOUT_ID` | DOUBLE | NOT NULL |  | Unique generated number that identifies a single row on the CDI_DOCUMENT_CHECKOUT table. |
| 5 | `CHECKOUT_DT_TM` | DATETIME |  |  | Date and time the document was checked out. |
| 6 | `PERSON_ID` | DOUBLE | NOT NULL | FK→ | ID of the person who has the document checked out. |
| 7 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 8 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 9 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 10 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 11 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `PERSON_ID` | [PRSNL](PRSNL.md) | `PERSON_ID` |

