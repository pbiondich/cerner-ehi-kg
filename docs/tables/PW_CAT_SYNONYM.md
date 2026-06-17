# PW_CAT_SYNONYM

> This table holds the synonyms for a given catalog pathway catalog.

**Description:** Pathway Catalog Synonym  
**Table type:** REFERENCE  
**Primary key:** `PW_CAT_SYNONYM_ID`  
**Columns:** 11  
**Referenced by:** 1 columns

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `PATHWAY_CATALOG_ID` | DOUBLE | NOT NULL | FK→ | Pathway catalog identification. Unique id of the pathway catalog entry referenced by an entry on this table. |
| 2 | `PRIMARY_IND` | DOUBLE | NOT NULL |  | Indicate whether the entry is a primary synonym entry |
| 3 | `PW_CAT_SYNONYM_ID` | DOUBLE | NOT NULL | PK | Primary Key |
| 4 | `SYNONYM_NAME` | VARCHAR(100) | NOT NULL |  | Alternate name for a treatment phase, plan or protocol stored on PATHWAY_CATALOG table. |
| 5 | `SYNONYM_NAME_KEY` | VARCHAR(100) | NOT NULL |  | Synonym key of the field synonym. This field has all capital letters and punctuation removed. It is used for indexing and searching for a pathway catalog. |
| 6 | `SYNONYM_NAME_KEY_A_NLS` | VARCHAR(400) | NOT NULL |  | KEY Value field for NLS support |
| 7 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 8 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 9 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 10 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 11 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `PATHWAY_CATALOG_ID` | [PATHWAY_CATALOG](PATHWAY_CATALOG.md) | `PATHWAY_CATALOG_ID` |

## Referenced by (1)

| From table | Column |
|------------|--------|
| [ALT_SEL_LIST](ALT_SEL_LIST.md) | `PW_CAT_SYNONYM_ID` |

