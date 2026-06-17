# MIC_SUS_DELTA_VALUE

> This reference table contains criteria information for susceptibility results delta checking values.

**Description:** Microbiology Susceptibility Delta Checking Value  
**Table type:** REFERENCE  
**Primary key:** `SUS_DELTA_VALUE_ID`  
**Columns:** 10  
**Referenced by:** 2 columns

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ORGANISM_CD` | DOUBLE | NOT NULL |  | The code_value of the organism used to define susceptibility delta checking value criteria. |
| 2 | `SERVICE_RESOURCE_CD` | DOUBLE | NOT NULL |  | This field contains the code_value of the service resource used to define susceptibility delta checking value criteria. |
| 3 | `SOURCE_CD` | DOUBLE | NOT NULL |  | The code_value of the source used to define susceptibility delta checking value criteria. |
| 4 | `SUS_DELTA_VALUE_ID` | DOUBLE | NOT NULL | PK | This field contains a unique value that identifies the susceptibility delta checking value criteria. |
| 5 | `SUS_DETAIL_CD` | DOUBLE | NOT NULL |  | The code_value of the source used to define susceptibility delta checking value criteria. |
| 6 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 7 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 8 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 9 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 10 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Referenced by (2)

| From table | Column |
|------------|--------|
| [MIC_SUS_DELTA_NUMERIC_RESULT](MIC_SUS_DELTA_NUMERIC_RESULT.md) | `SUS_DELTA_VALUE_ID` |
| [MIC_SUS_DELTA_RESULT](MIC_SUS_DELTA_RESULT.md) | `SUS_DELTA_VALUE_ID` |

