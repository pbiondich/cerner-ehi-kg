# REGIMEN_CATALOG

> Main table defining each regimen stored in the database. The table will hold high-level attributes such as display name and description.

**Description:** Regimen Catalog  
**Table type:** REFERENCE  
**Primary key:** `REGIMEN_CATALOG_ID`  
**Columns:** 16  
**Referenced by:** 7 columns

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ACTIVE_IND` | DOUBLE | NOT NULL |  | The table row is active or inactive. A row is generally active unless it is in an inactive state such as logically deleted, combined away, pending purge, etc. |
| 2 | `ADD_PLAN_IND` | DOUBLE | NOT NULL |  | ADD PLAN INDICATOR |
| 3 | `BEG_EFFECTIVE_DT_TM` | DATETIME | NOT NULL |  | The date and time for which this table row becomes effective. Normally, this will be the date and time the row is added, but could be a past or future date and time. |
| 4 | `END_EFFECTIVE_DT_TM` | DATETIME | NOT NULL |  | The date/time after which the row is no longer valid as active current data. This may be valued with the date that the row became inactive. |
| 5 | `EXTEND_TREATMENT_IND` | DOUBLE | NOT NULL |  | Indicates the ability to extend treatment of a regimen |
| 6 | `GROUP_REGIMEN_CATALOG_ID` | DOUBLE | NOT NULL | FK→ | sequence name: reference_seq Uniquely defines a regimen within the REGIMEN_CATALOG table. The REGIMEN_CATALOG_GROUP_ID can be associated with multiple regimen instances. When a new regimen is added to the REGIMEN_CATALOG table the REGIMEN_CATALOG_GROUP_ID is assigned to the REGIMEN_CATALOG_ ID |
| 7 | `REGIMEN_CATALOG_ID` | DOUBLE | NOT NULL | PK | sequence name: reference_seq Unique identifier for the REGIMEN_CATALOG table. Each change or revision made to a regimen creates a new regimen instance. |
| 8 | `REGIMEN_DESCRIPTION` | VARCHAR(1000) | NOT NULL |  | REGIMEN_DESCRIPTION is a longer and more descriptive version of the regimen name summarizing the treatment encapsulated by the regimen. |
| 9 | `REGIMEN_NAME` | VARCHAR(100) | NOT NULL |  | REGIMEN_NAME refers to the display name for the regimen. |
| 10 | `REGIMEN_NAME_KEY` | VARCHAR(100) | NOT NULL |  | Regimen Name key of the field Regimen Name. This field has all capital letters and punctuation removed. It is used for indexing and searching for a regimen catalog. |
| 11 | `REGIMEN_NAME_KEY_A_NLS` | VARCHAR(400) |  |  | REGIMEN NAME KEY VALUE WHEN National Language Support is required for Boolean operations. |
| 12 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 13 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 14 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 15 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 16 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `GROUP_REGIMEN_CATALOG_ID` | [REGIMEN_CATALOG](REGIMEN_CATALOG.md) | `REGIMEN_CATALOG_ID` |

## Referenced by (7)

| From table | Column |
|------------|--------|
| [REGIMEN](REGIMEN.md) | `REGIMEN_CATALOG_ID` |
| [REGIMEN_CATALOG](REGIMEN_CATALOG.md) | `GROUP_REGIMEN_CATALOG_ID` |
| [REGIMEN_CAT_ATTRIBUTE_R](REGIMEN_CAT_ATTRIBUTE_R.md) | `REGIMEN_CATALOG_ID` |
| [REGIMEN_CAT_DETAIL](REGIMEN_CAT_DETAIL.md) | `REGIMEN_CATALOG_ID` |
| [REGIMEN_CAT_DETAIL_R](REGIMEN_CAT_DETAIL_R.md) | `REGIMEN_CATALOG_ID` |
| [REGIMEN_CAT_FACILITY_R](REGIMEN_CAT_FACILITY_R.md) | `REGIMEN_CATALOG_ID` |
| [REGIMEN_CAT_SYNONYM](REGIMEN_CAT_SYNONYM.md) | `REGIMEN_CATALOG_ID` |

