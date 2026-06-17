# CMS_CRITICAL_LOCATION

> CMS (Centers for Medicare and Medicaid Services) - Content represents the LOCATIONS for therapeutic drug categories which are designated by clients as time critical for schedule administrations.

**Description:** CR CRITICAL LOCATION  
**Table type:** REFERENCE  
**Primary key:** `CMS_CRITICAL_LOCATION_ID`  
**Columns:** 8  
**Referenced by:** 1 columns

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `CMS_CRITICAL_LOCATION_ID` | DOUBLE | NOT NULL | PK | Unique generated number that identifies a single row on the CMS_Critical_Location table. |
| 2 | `LOCATION_CD` | DOUBLE | NOT NULL | FK→ | The location code value designating where the category is considered critical. |
| 3 | `ORGANIZATION_ID` | DOUBLE | NOT NULL | FK→ | The unique location organization identifier. |
| 4 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 5 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 6 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 7 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 8 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `LOCATION_CD` | [LOCATION](LOCATION.md) | `LOCATION_CD` |
| `ORGANIZATION_ID` | [ORGANIZATION](ORGANIZATION.md) | `ORGANIZATION_ID` |

## Referenced by (1)

| From table | Column |
|------------|--------|
| [CMS_CRITICAL_CATEGORY](CMS_CRITICAL_CATEGORY.md) | `CMS_CRITICAL_LOCATION_ID` |

