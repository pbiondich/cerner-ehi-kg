# MIC_SUS_DELTA_PARAM_CRITERIA

> This reference table contains criteria information for susceptibility delta checking parameters.

**Description:** Microbiology Susceptibility Delta Checking Parameters  
**Table type:** REFERENCE  
**Primary key:** `SUS_DELTA_PARAM_ID`  
**Columns:** 9  
**Referenced by:** 1 columns

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ORGANISM_CD` | DOUBLE | NOT NULL |  | Code_value of the organism used to define susceptibility delta checking parameter criteria. |
| 2 | `SERVICE_RESOURCE_CD` | DOUBLE | NOT NULL |  | Code_value of the service resource used to define susceptibility delta checking parameter criteria. |
| 3 | `SOURCE_CD` | DOUBLE | NOT NULL |  | Code_value of the source used to define susceptibility delta checking parameter criteria. |
| 4 | `SUS_DELTA_PARAM_ID` | DOUBLE | NOT NULL | PK | Unique value that identifies susceptibility delta checking parameter criteria. |
| 5 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 6 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 7 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 8 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 9 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Referenced by (1)

| From table | Column |
|------------|--------|
| [MIC_SUS_DELTA_PARAMETER](MIC_SUS_DELTA_PARAMETER.md) | `SUS_DELTA_PARAM_ID` |

