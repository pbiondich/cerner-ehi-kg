# REGIMEN_CAT_SYNONYM

> Display name synonyms for regimen catalog

**Description:** Regimen Synonym  
**Table type:** REFERENCE  
**Primary key:** `REGIMEN_CAT_SYNONYM_ID`  
**Columns:** 10  
**Referenced by:** 1 columns

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `PRIMARY_IND` | DOUBLE | NOT NULL |  | Indicates whether the entry is a primary synonym entry |
| 2 | `REGIMEN_CATALOG_ID` | DOUBLE | NOT NULL | FK→ | The unique identifier for a REGIMEN_CATALOG. It will be used to uniquely identify a regimen. foreign key from REGIMEN_CATALOG |
| 3 | `REGIMEN_CAT_SYNONYM_ID` | DOUBLE | NOT NULL | PK | sequence name: reference_seq Unique identifier for the REGIMEN_CAT_SYNONYM table. |
| 4 | `SYNONYM_DISPLAY` | VARCHAR(100) | NOT NULL |  | DISPLAY NAME FOR THE SYNONYM |
| 5 | `SYNONYM_KEY` | VARCHAR(100) | NOT NULL |  | Synonym key of the field synonym. This field has all capital letters and punctuation removed. It is used for indexing and searching for a regimen catalog. |
| 6 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 7 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 8 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 9 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 10 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `REGIMEN_CATALOG_ID` | [REGIMEN_CATALOG](REGIMEN_CATALOG.md) | `REGIMEN_CATALOG_ID` |

## Referenced by (1)

| From table | Column |
|------------|--------|
| [ALT_SEL_LIST](ALT_SEL_LIST.md) | `REGIMEN_CAT_SYNONYM_ID` |

