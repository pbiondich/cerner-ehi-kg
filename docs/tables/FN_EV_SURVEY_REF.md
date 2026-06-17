# FN_EV_SURVEY_REF

> Stores all parent survey reference data versions used by Emergent Event

**Description:** FN_EV_SURVEY_REF  
**Table type:** REFERENCE  
**Primary key:** `FN_EV_SURVEY_REF_ID`  
**Columns:** 11  
**Referenced by:** 1 columns

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `CREATE_DT_TM` | DATETIME |  |  | date and time the survey refernce was created |
| 2 | `FN_EV_SURVEY_REF_ID` | DOUBLE | NOT NULL | PK | PRIMARY KEY |
| 3 | `ORGANIZATION_ID` | DOUBLE |  | FK→ | This is the value of the unique primary identifier of the organization table. it is an internal system assigned number. ; |
| 4 | `SURVEY_KEY_IDENT` | VARCHAR(255) |  |  | Unique identification for a survey |
| 5 | `SURVEY_NAME` | VARCHAR(255) |  |  | Survey name that is displayed to the user. |
| 6 | `SURVEY_TYPE_FLAG` | DOUBLE |  |  | Determines survey is Pre-Hospital - Primary - Secondary - Other |
| 7 | `UPDT_APPLCTX` | DOUBLE |  |  | The application context number from the record info block. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 8 | `UPDT_CNT` | DOUBLE |  |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 9 | `UPDT_DT_TM` | DATETIME |  |  | The date and time the row was last inserted or updated. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 10 | `UPDT_ID` | DOUBLE |  |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 11 | `UPDT_TASK` | DOUBLE |  |  | The registered (assigned) task number for the process that inserted or updated the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `ORGANIZATION_ID` | [ORGANIZATION](ORGANIZATION.md) | `ORGANIZATION_ID` |

## Referenced by (1)

| From table | Column |
|------------|--------|
| [FN_EV_SURVEY_DETAIL_REF](FN_EV_SURVEY_DETAIL_REF.md) | `FN_EV_SURVEY_REF_ID` |

