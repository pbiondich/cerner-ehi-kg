# DA_DOCUMENT_ORG_RELTN

> The Document Org Relation table contains the organizations associated with the document when it was generated in Discern Analytics 2.0. (A user must be associated with the same organizations in order to view this document). Only used when organizational security is on.

**Description:** Discern Analytics Document Organization Relation  
**Table type:** ACTIVITY  
**Primary key:** _(not published — see note)_  
**Columns:** 8

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `DA_DOCUMENT_ID` | DOUBLE | NOT NULL | FK→ | The document this Organization is related to. |
| 2 | `DA_DOCUMENT_ORG_RELTN_ID` | DOUBLE | NOT NULL |  | Unique, generated number that identifies a single row on the DA_DOCUMENT_ORG_RELTN table. |
| 3 | `ORGANIZATION_ID` | DOUBLE | NOT NULL | FK→ | The organization associated with the personnel when the report was generated. |
| 4 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 5 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 6 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 7 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 8 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `DA_DOCUMENT_ID` | [DA_DOCUMENT](DA_DOCUMENT.md) | `DA_DOCUMENT_ID` |
| `ORGANIZATION_ID` | [ORGANIZATION](ORGANIZATION.md) | `ORGANIZATION_ID` |

