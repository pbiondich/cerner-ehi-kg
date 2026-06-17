# THERAPEUTIC_CAT

> Stores therapeutic category reference content across multiple vocabularies. A therapeutic category is a categorization of further sub therapeutic categories and/or drugs that pertain to a particiular therapy.

**Description:** Therapautic Category  
**Table type:** REFERENCE  
**Primary key:** `THERAPEUTIC_CAT_ID`  
**Columns:** 14  
**Referenced by:** 2 columns

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ACTIVE_IND` | DOUBLE | NOT NULL |  | The table row is active or inactive. A row is generally active unless it is in an inactive state such as logically deleted, combined away, pending purge, etc. |
| 2 | `EXTERNAL_IDENT` | VARCHAR(255) | NOT NULL |  | External identifier defined by source creating a therapeutic category. This value uniquely identifies a record when compared against the source. It will allow us to create a 'key' to identify rows outside the current domain. In our current scenario, the external_ident is composed on SNOMED CT concept values. |
| 3 | `SOURCE_VOCABULARY_CD` | DOUBLE | NOT NULL |  | The source vocabulary from which the therapeutic category originated from. |
| 4 | `SYNONYM_ID` | DOUBLE | NOT NULL |  | If this therapeutic category also represents a synonym, this will be the id of the synonym. As an example, therapeutic categories in SNOMED can represent synonyms which are also drugs. This column will allow the identification of those folders which are also drugs themselves. |
| 5 | `THERAPEUTIC_CAT_ID` | DOUBLE | NOT NULL | PK | The primary key for the Therapeutic_Cat table |
| 6 | `THERAPEUTIC_CAT_NAME` | VARCHAR(255) | NOT NULL |  | The name of the therapeutic category. |
| 7 | `THERAPEUTIC_CAT_NAME_KEY` | VARCHAR(255) | NOT NULL |  | The name of the therapeutic category converted to upper case and stripped of all non-alpha characters. |
| 8 | `THERAPEUTIC_CAT_NAME_KEY_A_NLS` | VARCHAR(1020) |  |  | THERAPEUTIC_CAT_NAME_KEY_A_NLS column |
| 9 | `THERAPEUTIC_CAT_NAME_KEY_NLS` | VARCHAR(512) | NOT NULL |  | The i18n name of the therapeutic category converted to upper case and stripped of all non-alpha characters. |
| 10 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 11 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 12 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 13 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 14 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Referenced by (2)

| From table | Column |
|------------|--------|
| [THERAPEUTIC_CAT_ITEM](THERAPEUTIC_CAT_ITEM.md) | `SUB_THERAPEUTIC_CAT_ID` |
| [THERAPEUTIC_CAT_ITEM](THERAPEUTIC_CAT_ITEM.md) | `THERAPEUTIC_CAT_ID` |

