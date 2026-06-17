# SI_DOCUMENT_IDENTIFIER_R

> This relation table will store identifiers related to a given document from si_document_info

**Description:** SI Document Identifier Relation table  
**Table type:** ACTIVITY  
**Primary key:** _(not published — see note)_  
**Columns:** 10

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `SI_DOCUMENT_IDENTIFIER_R_ID` | DOUBLE | NOT NULL |  | PRIMARY KEY |
| 2 | `SI_DOCUMENT_INFO_ID` | DOUBLE | NOT NULL | FK→ | The document that needs to have entities related to it. |
| 3 | `SOURCE_NAME` | VARCHAR(30) | NOT NULL |  | Name of the identifier related to the document, for example: REFERRAL_ORDER |
| 4 | `SOURCE_TABLE` | VARCHAR(30) |  |  | Table name related to the Source Value, for example: ORDERS |
| 5 | `SOURCE_VALUE` | DOUBLE | NOT NULL |  | Identifier that needs to be related to the given document. Value is related to the table or context identified in SOURCE_NAME |
| 6 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 7 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 8 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 9 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 10 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `SI_DOCUMENT_INFO_ID` | [SI_DOCUMENT_INFO](SI_DOCUMENT_INFO.md) | `SI_DOCUMENT_INFO_ID` |

