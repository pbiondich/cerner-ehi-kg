# MIC_STAT_SUS_DC_PARAM

> This statistical reference table contains criteria information for susceptibility results duplicate checking (DC) parameters such as tolerances and across susceptibilities. This is a parent table of mic_stat_sus_cross_ref and mic_stat_sus_limit_tolerance.

**Description:** Micro Susceptibility Duplicating Checking Parameter  
**Table type:** REFERENCE  
**Primary key:** `SUS_DC_PARAM_ID`  
**Columns:** 14  
**Referenced by:** 2 columns

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ACROSS_ENCOUNTER_IND` | DOUBLE |  |  | This field indicates if duplicate checking should occur within encounters or across encounters. Default 0 = duplicate checking should be within encounters. 1 = duplicate checking should be across encounters. |
| 2 | `ACROSS_SOURCE_IND` | DOUBLE |  |  | This field indicates if duplicate checking should occur within sources or across sources. Default 0 = duplicate checking should be within sources. 1 = duplicate checking should be across sources. |
| 3 | `LOOKBACK_HOURS` | DOUBLE | NOT NULL |  | This field indicates how many days to look back for duplicates from the update date and time of the current susceptibility method. |
| 4 | `MATCHING_AB_IND` | DOUBLE |  |  | This field indicates if antibiotic duplicate checking should match on different panels. 0 = if an antibiotic that has duplicate checking parameters defined on it but does not have a match in the second panel, the organism will automatically be considered unique. 1 = allow user to define the number of antibiotics that have to be compared between panels before the organism can be considered a duplicated. |
| 5 | `MATCHING_AB_NBR` | DOUBLE | NOT NULL |  | This field indicates the number of antibiotics that have to match for the panels to be duplicate checked. |
| 6 | `ORGANISM_CD` | DOUBLE | NOT NULL |  | This field contains the code_value of the organism used to define sus DC parameter criteria. |
| 7 | `SERVICE_RESOURCE_CD` | DOUBLE | NOT NULL |  | This field contains the code_value of the service resource used to define sus DC parameter criteria. |
| 8 | `SOURCE_CD` | DOUBLE | NOT NULL |  | This field contains the code_value of the source used to define sus DC parameter criteria. |
| 9 | `SUS_DC_PARAM_ID` | DOUBLE | NOT NULL | PK | This field contains a unique value that identifies sus DC parameter criteria. This value is used to join to mic_stat_sus_cross_ref and mic_stat_sus_tolerance tables. |
| 10 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 11 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 12 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 13 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 14 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Referenced by (2)

| From table | Column |
|------------|--------|
| [MIC_STAT_SUS_CROSS_REF](MIC_STAT_SUS_CROSS_REF.md) | `SUS_DC_PARAM_ID` |
| [MIC_STAT_SUS_LIMIT_TOLERANCE](MIC_STAT_SUS_LIMIT_TOLERANCE.md) | `SUS_DC_PARAM_ID` |

