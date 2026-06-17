# REVISION

> Tables stores information about Revisions created on an amendment

**Description:** REVISION  
**Table type:** REFERENCE  
**Primary key:** `REVISION_ID`  
**Columns:** 10  
**Referenced by:** 1 columns

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `PROT_AMENDMENT_ID` | DOUBLE | NOT NULL | FK→ | The amendment for which this revision belongs to |
| 2 | `REVISION_DESCRIPTION` | VARCHAR(255) | NOT NULL |  | Free Text description of the reason for the revision |
| 3 | `REVISION_DT_TM` | DATETIME | NOT NULL |  | This field contains the date and time on which the revision was made. |
| 4 | `REVISION_ID` | DOUBLE | NOT NULL | PK | Primary Key |
| 5 | `REVISION_NBR` | DOUBLE | NOT NULL |  | This field contains the number of the revision (1-first revision, 2-second revision, 3-third revision, etc.). A revision is a minor change to the protocol document such as correction of a spelling error or typographic error. |
| 6 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 7 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 8 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 9 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 10 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `PROT_AMENDMENT_ID` | [PROT_AMENDMENT](PROT_AMENDMENT.md) | `PROT_AMENDMENT_ID` |

## Referenced by (1)

| From table | Column |
|------------|--------|
| [CT_DOCUMENT_VERSION](CT_DOCUMENT_VERSION.md) | `REVISION_ID` |

