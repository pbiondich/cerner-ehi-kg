# MAMMO_ASSESSMENT_SERIES

> Table stores series information for mammography procedures that have been addended.

**Description:** Mammography Assessment Series  
**Table type:** ACTIVITY  
**Primary key:** `SERIES_ID`  
**Columns:** 16  
**Referenced by:** 1 columns

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ASSESSMENT_ID` | DOUBLE | NOT NULL | FK→ | The Radiologist's assessment for follow-up (ACR). This is a foreign key to the Rad_Fol_Up_Field table. |
| 2 | `ASSIGNED_DT_TM` | DATETIME | NOT NULL |  | Assigned date and time of the series. |
| 3 | `FOLLOW_UP_PROC_CD` | DOUBLE | NOT NULL |  | The mammography follow up procedure for this instance of a series. |
| 4 | `LETTER_ID` | DOUBLE | NOT NULL |  | This is the letter_id for the mammo letter currently tied to this series. |
| 5 | `RAD_ID` | DOUBLE | NOT NULL | FK→ | Radiologist ID whom signed out an instance of a series |
| 6 | `RECALL_INTERVAL` | DOUBLE | NOT NULL |  | The Recall Interval for the mammography procedure in the series. From the Mammo_study table beforethe series was written. |
| 7 | `SEQUENCE` | DOUBLE | NOT NULL |  | Sequence of the assessment series |
| 8 | `SERIES_ID` | DOUBLE | NOT NULL | PK | Primary key for mammo_assessment_series table |
| 9 | `SERIES_INSTANCE_NBR` | DOUBLE | NOT NULL |  | This is the column that contains the instance number for all the ASSESSMENT_IDs added for a particular series instance. |
| 10 | `SERIES_OPEN_IND` | DOUBLE |  |  | Indicates a series has been added for a specific mammography procedure but the addended report has not been finalized |
| 11 | `STUDY_ID` | DOUBLE | NOT NULL | FK→ | Foreign key to Mammo_Study table |
| 12 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 13 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 14 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 15 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 16 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `ASSESSMENT_ID` | [RAD_FOL_UP_FIELD](RAD_FOL_UP_FIELD.md) | `FOLLOW_UP_FIELD_ID` |
| `RAD_ID` | [PRSNL](PRSNL.md) | `PERSON_ID` |
| `STUDY_ID` | [MAMMO_STUDY](MAMMO_STUDY.md) | `STUDY_ID` |

## Referenced by (1)

| From table | Column |
|------------|--------|
| [MAMMO_RECOMMEND_SERIES](MAMMO_RECOMMEND_SERIES.md) | `SERIES_ID` |

