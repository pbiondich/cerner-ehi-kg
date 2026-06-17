# MIC_STAT_SUS_GROUP

> This statistical reference table contains criteria information for susceptibility result grouping so the more meaningful antibiogram reports can be generated. This is a parent table of mic_stat_sus_group_result and mic_stat_sus_group_numeric.

**Description:** Micro Susceptibility Result Grouping  
**Table type:** REFERENCE  
**Primary key:** `SUS_GROUP_ID`  
**Columns:** 11  
**Referenced by:** 2 columns

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ANTIBIOTIC_CD` | DOUBLE | NOT NULL |  | This field contains the code_value of the antibiotic used to define result group criteria. |
| 2 | `ORGANISM_CD` | DOUBLE | NOT NULL |  | This field contains the code_value of the organism used to define result group criteria. |
| 3 | `SERVICE_RESOURCE_CD` | DOUBLE | NOT NULL |  | This field contains the code_value of the service resource used to define result group criteria. |
| 4 | `SOURCE_CD` | DOUBLE | NOT NULL |  | This field contains the code_value of the source used to define result group criteria. |
| 5 | `SUS_DETAIL_CD` | DOUBLE | NOT NULL |  | This field contains the code_value of the susceptibility detail used to define result group criteria. |
| 6 | `SUS_GROUP_ID` | DOUBLE | NOT NULL | PK | This field contains a unique value that identifies sus group criteria. This value is used to join to mic_stat_sus_group_result and mic_stat_sus_group_numeric tables. |
| 7 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 8 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 9 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 10 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 11 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Referenced by (2)

| From table | Column |
|------------|--------|
| [MIC_STAT_SUS_GROUP_NUMERIC](MIC_STAT_SUS_GROUP_NUMERIC.md) | `SUS_GROUP_ID` |
| [MIC_STAT_SUS_GROUP_RESULT](MIC_STAT_SUS_GROUP_RESULT.md) | `SUS_GROUP_ID` |

