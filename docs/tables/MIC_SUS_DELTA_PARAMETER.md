# MIC_SUS_DELTA_PARAMETER

> Contains antibiotic and parameter information for susceptibility delta checking.

**Description:** Microbiology Susceptibility Delta Checking Parameter Antibiotic  
**Table type:** REFERENCE  
**Primary key:** `ANTIBIOTIC_CD`, `SUS_DELTA_PARAM_ID`  
**Columns:** 13  
**Referenced by:** 2 columns

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ACROSS_ENCOUNTER_IND` | DOUBLE |  |  | This field indicates if delta checking should occur within encounters or across encounters. Default 0 = delta checking should be within encounters. 1 = delta checking should be across encounters. |
| 2 | `ACROSS_SOURCE_IND` | DOUBLE |  |  | This field indicates if delta checking should occur within the same source or across sources. Default 0 = delta checking should be within sources. 1 = delta checking should be across sources. |
| 3 | `ANTIBIOTIC_CD` | DOUBLE | NOT NULL | PK | Code_value of the antibiotic used to define susceptibility delta checking parameter criteria. |
| 4 | `LOOKBACK_HOURS_NBR` | DOUBLE | NOT NULL |  | How many days to look back for delta checking from the update date and time of the current susceptibility method. This column will only be valued if the across_encounter_ind = 1. |
| 5 | `REQUIRE_FOOTNOTE_IND` | DOUBLE |  |  | Indicates if a delta checking failure requires the user to enter a footnote. Default 0 = no footnote required. 1= footnote required. |
| 6 | `SHOW_MESSAGE_IND` | DOUBLE |  |  | Indicates if the delta checking warning message should be displayed when a failure occurs. Default 0 = do not show warning message. 1 = show warning message. |
| 7 | `SUS_DELTA_PARAM_ID` | DOUBLE | NOT NULL | PK FK→ | Unique value that identifies susceptibility delta checking parameter criteria. |
| 8 | `TOLERANCE_LIMIT_NBR` | DOUBLE | NOT NULL |  | The tolerance limit for the delta checking values. |
| 9 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 10 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 11 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 12 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 13 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `SUS_DELTA_PARAM_ID` | [MIC_SUS_DELTA_PARAM_CRITERIA](MIC_SUS_DELTA_PARAM_CRITERIA.md) | `SUS_DELTA_PARAM_ID` |

## Referenced by (2)

| From table | Column |
|------------|--------|
| [MIC_SUS_DELTA_XREF](MIC_SUS_DELTA_XREF.md) | `ANTIBIOTIC_CD` |
| [MIC_SUS_DELTA_XREF](MIC_SUS_DELTA_XREF.md) | `SUS_DELTA_PARAM_ID` |

