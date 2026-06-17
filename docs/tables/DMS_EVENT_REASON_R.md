# DMS_EVENT_REASON_R

> Contains event reason relationship information. It related content types to valid reasons for content retrieval.

**Description:** DMS event reason relationship.  
**Table type:** REFERENCE  
**Primary key:** _(not published — see note)_  
**Columns:** 8

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `DMS_CONTENT_TYPE_ID` | DOUBLE | NOT NULL | FK→ | Refers to a specific content type |
| 2 | `DMS_EVENT_REASON_R_ID` | DOUBLE | NOT NULL |  | Unique identifier for this row |
| 3 | `DMS_REASON_REF_ID` | DOUBLE | NOT NULL | FK→ | Refers to a specific event reason |
| 4 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 5 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 6 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 7 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 8 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `DMS_CONTENT_TYPE_ID` | [DMS_CONTENT_TYPE](DMS_CONTENT_TYPE.md) | `DMS_CONTENT_TYPE_ID` |
| `DMS_REASON_REF_ID` | [DMS_REF](DMS_REF.md) | `DMS_REF_ID` |

