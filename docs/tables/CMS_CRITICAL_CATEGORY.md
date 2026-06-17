# CMS_CRITICAL_CATEGORY

> CMS (Centers for Medicare and Medicaid Services) - Content represents the therapeutic drug categories which are designated by clients as time critical for schedule administrations based on location.

**Description:** CMS CRITICAL CATEGORY  
**Table type:** REFERENCE  
**Primary key:** _(not published — see note)_  
**Columns:** 8

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `CMS_CRITICAL_CATEGORY_ID` | DOUBLE | NOT NULL |  | Unique generated number that identifies a single row on the CMS_Critical_Category table. |
| 2 | `CMS_CRITICAL_LOCATION_ID` | DOUBLE | NOT NULL | FK→ | LOCATION foreign key value from the CMS_CRITICAL_LOCATION table |
| 3 | `MULTUM_CATEGORY_ID` | DOUBLE | NOT NULL | FK→ | The Multum drug classification category identifier. |
| 4 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 5 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 6 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 7 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 8 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `CMS_CRITICAL_LOCATION_ID` | [CMS_CRITICAL_LOCATION](CMS_CRITICAL_LOCATION.md) | `CMS_CRITICAL_LOCATION_ID` |
| `MULTUM_CATEGORY_ID` | [MLTM_DRUG_CATEGORIES](MLTM_DRUG_CATEGORIES.md) | `MULTUM_CATEGORY_ID` |

