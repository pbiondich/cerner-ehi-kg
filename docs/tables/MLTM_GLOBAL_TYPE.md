# MLTM_GLOBAL_TYPE

> Table for holding Multum Global Types

**Description:** MLTM_GLOBAL_TYPE  
**Table type:** REFERENCE  
**Primary key:** `GLOBAL_TYPE_ID`  
**Columns:** 9  
**Referenced by:** 4 columns

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `COUNTRY_ID` | DOUBLE | NOT NULL | FK→ | FK to MLTM_COUNTRY |
| 2 | `DESCRIPTION` | VARCHAR(100) | NOT NULL |  | Description for the global type |
| 3 | `GLOBAL_TYPE_ID` | DOUBLE | NOT NULL | PK | Global Types as defined by external source |
| 4 | `GLOBAL_TYPE_MEAN` | VARCHAR(12) | NOT NULL |  | Abbreviated meaning for the global type for coding purposes |
| 5 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 6 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 7 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 8 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 9 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `COUNTRY_ID` | [MLTM_COUNTRY](MLTM_COUNTRY.md) | `COUNTRY_ID` |

## Referenced by (4)

| From table | Column |
|------------|--------|
| [MLTM_BCB_DRC_UNITS](MLTM_BCB_DRC_UNITS.md) | `GLOBAL_TYPE_ID` |
| [MLTM_DRUG_NAME_GLOBAL_TYPE](MLTM_DRUG_NAME_GLOBAL_TYPE.md) | `GLOBAL_TYPE_ID` |
| [MLTM_NDC_CORE_DESCRIPTION](MLTM_NDC_CORE_DESCRIPTION.md) | `GLOBAL_TYPE_ID` |
| [MLTM_NDC_MAIN_DRUG_CODE](MLTM_NDC_MAIN_DRUG_CODE.md) | `GLOBAL_TYPE_ID` |

