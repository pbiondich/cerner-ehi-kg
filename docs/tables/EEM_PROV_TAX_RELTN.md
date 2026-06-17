# EEM_PROV_TAX_RELTN

> Relation from Provider (physician/org/service resource) to provider taxonomy

**Description:** Provider to taxonomy relationship  
**Table type:** REFERENCE  
**Primary key:** `EEM_PROV_TAX_RELTN_ID`  
**Columns:** 17  
**Referenced by:** 1 columns

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ACTIVE_IND` | DOUBLE |  |  | The table row is active or inactive. A row is generally active unless it is in an inactive state such as logically deleted, combined away, pending purge, etc. |
| 2 | `ACTIVE_STATUS_CD` | DOUBLE | NOT NULL |  | Indicates the status of the row itself (not the data in the row) such as active, inactive, combined away, pending purge, etc. |
| 3 | `ACTIVE_STATUS_DT_TM` | DATETIME |  |  | The date and time that the active_status_cd was set. |
| 4 | `ACTIVE_STATUS_PRSNL_ID` | DOUBLE | NOT NULL |  | The person who caused the active_status_cd to be set or change. |
| 5 | `BEG_EFFECTIVE_DT_TM` | DATETIME |  |  | The date and time for which this table row becomes effective. Normally, this will be the date and time the row is added, but could be a past or future date and time. |
| 6 | `EEM_PROV_TAX_RELTN_ID` | DOUBLE | NOT NULL | PK | Primary Key |
| 7 | `END_EFFECTIVE_DT_TM` | DATETIME |  |  | The date/time after which the row is no longer valid as active current data. This may be valued with the date that the row became inactive. |
| 8 | `LONG_TEXT_ID` | DOUBLE | NOT NULL | FK→ | Long Text Id used to store comments. |
| 9 | `PARENT_ENTITY_ID` | DOUBLE | NOT NULL |  | Primary Key of the Id. |
| 10 | `PARENT_ENTITY_NAME` | VARCHAR(32) |  |  | Parent Table for relation. |
| 11 | `SEQ_NBR` | DOUBLE | NOT NULL |  | Future Use. |
| 12 | `TAXONOMY_ID` | DOUBLE | NOT NULL | FK→ | Taxonomy Id (NOMENCLATURE) |
| 13 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 14 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 15 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 16 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 17 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `LONG_TEXT_ID` | [LONG_TEXT](LONG_TEXT.md) | `LONG_TEXT_ID` |
| `TAXONOMY_ID` | [PROVIDER_TAXONOMY](PROVIDER_TAXONOMY.md) | `TAXONOMY_ID` |

## Referenced by (1)

| From table | Column |
|------------|--------|
| [EEM_ENTITY_PROV_TAX_RELTN](EEM_ENTITY_PROV_TAX_RELTN.md) | `EEM_PROV_TAX_RELTN_ID` |

