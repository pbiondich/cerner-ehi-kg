# PM_POST_DOC_ORG_RELTN

> Stores the relationships between post documents records and organizations to limit which organizations a particular post document is created for.

**Description:** Person Management Post Document Organization Relation  
**Table type:** REFERENCE  
**Primary key:** _(not published — see note)_  
**Columns:** 8

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ORGANIZATION_ID` | DOUBLE | NOT NULL | FK→ | This is the value of the unique primary identifier of the organization table. It is an internal system assigned number. |
| 2 | `PM_POST_DOC_ORG_RELTN_ID` | DOUBLE | NOT NULL |  | This is the value of the unique primary identifier of this table. It is an internal system assigned number. |
| 3 | `PM_POST_DOC_REF_ID` | DOUBLE | NOT NULL | FK→ | This is the value of the unique primary identifier of the pm_post_doc_ref table. It is an internal system assigned number. |
| 4 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 5 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 6 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 7 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 8 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `ORGANIZATION_ID` | [ORGANIZATION](ORGANIZATION.md) | `ORGANIZATION_ID` |
| `PM_POST_DOC_REF_ID` | [PM_POST_DOC_REF](PM_POST_DOC_REF.md) | `PM_POST_DOC_REF_ID` |

