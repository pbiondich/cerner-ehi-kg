# PW_MAINTENANCE_CRITERIA

> Stores the maintenance criteria for PowerPlans.

**Description:** Pathway maintenance criteria  
**Table type:** REFERENCE  
**Primary key:** _(not published — see note)_  
**Columns:** 11

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ENCOUNTER_TYPE_FLAG` | DOUBLE | NOT NULL |  | Denotes the encounter type that this criterion applies to 0 - All 1 - Inpatient 2 - Non-Inpatient |
| 2 | `PW_MAINTENANCE_CRITERIA_ID` | DOUBLE | NOT NULL |  | Primary Key |
| 3 | `TIME_QTY` | DOUBLE | NOT NULL |  | Denotes the amount of time for a criterion. |
| 4 | `TIME_UNIT_CD` | DOUBLE | NOT NULL |  | Denotes the time unit for the specified time quantity. Code Set 340 |
| 5 | `TYPE_MEAN` | VARCHAR(12) | NOT NULL |  | Indicates the type of maintenance criterion |
| 6 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 7 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 8 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 9 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 10 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |
| 11 | `VERSION_PW_CAT_ID` | DOUBLE | NOT NULL | FK→ | Identifies all versions of a plan in reference that this criterion applies to. This field corresponds to a version_pw_cat_id from the pathway_catalog table. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `VERSION_PW_CAT_ID` | [PATHWAY_CATALOG](PATHWAY_CATALOG.md) | `PATHWAY_CATALOG_ID` |

