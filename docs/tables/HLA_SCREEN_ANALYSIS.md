# HLA_SCREEN_ANALYSIS

> Stores the activity data related to the modified antibody screen analysis.

**Description:** HLA Antibody Screen Analysis  
**Table type:** ACTIVITY  
**Primary key:** `CRITERIA_ID`  
**Columns:** 14  
**Referenced by:** 1 columns

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ANALYSIS_DESC` | VARCHAR(250) | NOT NULL |  | A textual string entered by a user when the analysis was saved. |
| 2 | `ANALYSIS_DT_TM` | DATETIME | NOT NULL |  | Current date and time the analysis was saved to the table. Used to display when selecting to load a saved analysis. |
| 3 | `BATCH_ID` | DOUBLE | NOT NULL | FK→ | Relationship identifier from HLA_AB_SCREEN_BATCH, which relates a unique HLA antibody screen batch number to the inventory lot and HLA antibody screen tray map selected for the batch. |
| 4 | `CRITERIA_ID` | DOUBLE | NOT NULL | PK | Unique identifier for a modified antibody screen analysis. |
| 5 | `CROSS_SPECIMEN_ID` | DOUBLE | NOT NULL | FK→ | Identifies the relationship to the information to HLA_X_SPECIMEN_ANALYSIS, which is a saved cross specimen analysis. |
| 6 | `CUTOFF_TYPE_FLAG` | DOUBLE | NOT NULL |  | Identifies what the cutoff value is holding: 1 = inclusion percentage, 2 = r-value 3 = chi square |
| 7 | `CUTOFF_VALUE` | DOUBLE | NOT NULL |  | Value to use as the CUTOFF when displaying the r-value and tail analysis views in the antibody screen analysis. Holds either the inclusion percentage, r-value or chi square cut off value. |
| 8 | `POSITIVE_DEFINITION_CD` | DOUBLE | NOT NULL |  | Value of the positive score cutoff. |
| 9 | `REMOVE_PERSON_ANTIGEN_IND` | DOUBLE | NOT NULL |  | Indicates whether to remove the persons HLA typing antigens from the analysis automatically. |
| 10 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 11 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 12 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 13 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 14 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `BATCH_ID` | [HLA_AB_SCREEN_BATCH](HLA_AB_SCREEN_BATCH.md) | `BATCH_ID` |
| `CROSS_SPECIMEN_ID` | [HLA_X_SPECIMEN_ANALYSIS](HLA_X_SPECIMEN_ANALYSIS.md) | `CROSS_SPECIMEN_ID` |

## Referenced by (1)

| From table | Column |
|------------|--------|
| [HLA_SCREEN_ANALYSIS_DETAIL](HLA_SCREEN_ANALYSIS_DETAIL.md) | `CRITERIA_ID` |

