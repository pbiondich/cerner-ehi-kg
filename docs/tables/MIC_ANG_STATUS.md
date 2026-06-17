# MIC_ANG_STATUS

> The status of an ANG run.

**Description:** Activity tbl, if a row is added here it means that a ANG run has occured.  
**Table type:** ACTIVITY  
**Primary key:** `ANG_RUN_ID`  
**Columns:** 9  
**Referenced by:** 2 columns

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ANG_ID` | DOUBLE | NOT NULL | FK→ | This field identifies a unique value for each procedure/service resource/source combination. This identifier is then used to uniquely identify the parameters on tables such as mic_ang_ref_report and mic_ang_disqual tables. |
| 2 | `ANG_RUN_ID` | DOUBLE | NOT NULL | PK | Uniquely Identifies an ANG Execution. |
| 3 | `RUN_DT_TM` | DATETIME | NOT NULL |  | Date/Time of the ANG Execution |
| 4 | `RUN_STATUS_IND` | DOUBLE | NOT NULL |  | Determines the status of an ANG run. 0 - Not Started, 1 - In Process, 2 - Successful, 3 - Error. |
| 5 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 6 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 7 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 8 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 9 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `ANG_ID` | [MIC_REF_ANG](MIC_REF_ANG.md) | `ANG_ID` |

## Referenced by (2)

| From table | Column |
|------------|--------|
| [MIC_ACT_ANG_SUM_RPT](MIC_ACT_ANG_SUM_RPT.md) | `ANG_RUN_ID` |
| [MIC_ANG_AUTOMATED](MIC_ANG_AUTOMATED.md) | `ANG_RUN_ID` |

