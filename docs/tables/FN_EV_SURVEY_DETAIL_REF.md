# FN_EV_SURVEY_DETAIL_REF

> DETAILS FOR SURVEY REFERENCE

**Description:** FN_EV_SURVEY_DETAIL_REF  
**Table type:** REFERENCE  
**Primary key:** `FN_EV_SURVEY_DETAIL_REF_ID`  
**Columns:** 9  
**Referenced by:** 1 columns

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `CREATE_DT_TM` | DATETIME |  |  | DATE and TIME Survey details were created |
| 2 | `FN_EV_SURVEY_DETAIL_REF_ID` | DOUBLE | NOT NULL | PK | PRIMARY KEY |
| 3 | `FN_EV_SURVEY_REF_ID` | DOUBLE |  | FK→ | FK value for the parent table survey id |
| 4 | `INSTANCE_NBR` | DOUBLE |  |  | the instance number of the survey reference |
| 5 | `UPDT_APPLCTX` | DOUBLE |  |  | The application context number from the record info block. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 6 | `UPDT_CNT` | DOUBLE |  |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 7 | `UPDT_DT_TM` | DATETIME |  |  | The date and time the row was last inserted or updated. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 8 | `UPDT_ID` | DOUBLE |  |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 9 | `UPDT_TASK` | DOUBLE |  |  | The registered (assigned) task number for the process that inserted or updated the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `FN_EV_SURVEY_REF_ID` | [FN_EV_SURVEY_REF](FN_EV_SURVEY_REF.md) | `FN_EV_SURVEY_REF_ID` |

## Referenced by (1)

| From table | Column |
|------------|--------|
| [FN_EV_SURVEY_ELEMENT_REF](FN_EV_SURVEY_ELEMENT_REF.md) | `FN_EV_SURVEY_DETAIL_REF_ID` |

