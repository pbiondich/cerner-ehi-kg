# PDM_RANGES

> Stores the range specific information for Patient Data Monitoring.

**Description:** Patient Data Monitoring Ranges  
**Table type:** REFERENCE  
**Primary key:** `PDM_RANGE_ID`  
**Columns:** 21  
**Referenced by:** 2 columns

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ACTIVE_IND` | DOUBLE | NOT NULL |  | The table row is active or inactive. A row is generally active unless it is in an inactive state such as logically deleted, combined away, pending purge, etc. |
| 2 | `AGE_FROM_MINUTES` | DOUBLE | NOT NULL |  | Defines the beginning age range used to determine if a patient's result should be included or excluded in the calculation of the quality control result. |
| 3 | `AGE_FROM_UNITS_CD` | DOUBLE | NOT NULL |  | A unique code value that identifies the units of age for the beginning age range. |
| 4 | `AGE_TO_MINUTES` | DOUBLE | NOT NULL |  | Defines the ending age range used to determine if a patient's result should be included or excluded in the calculation of the quality control result. |
| 5 | `AGE_TO_UNITS_CD` | DOUBLE | NOT NULL |  | A unique code value that identifies the units of age for the ending age range. |
| 6 | `BEG_EFFECTIVE_DT_TM` | DATETIME |  |  | The date and time for which this table row becomes effective. Normally, this will be the date and time the row is added, but could be a past or future date and time. |
| 7 | `END_EFFECTIVE_DT_TM` | DATETIME |  |  | The date/time after which the row is no longer valid as active current data. This may be valued with the date that the row became inactive. |
| 8 | `MEAN` | DOUBLE | NOT NULL |  | Defines the expected quality control mean for the defined range parameters. |
| 9 | `PDM_PARAM_ID` | DOUBLE | NOT NULL | FK→ | A unique, internal, system-assigned number that identifies the specific patient data monitoring parameters associated with the patient data monitoring ranges. |
| 10 | `PDM_RANGE_ID` | DOUBLE | NOT NULL | PK | A unique, internal, system-assigned number that identifies specific patient data monitoring range parameters. Ranges are defined by the combination of species, gender, and age range. |
| 11 | `RESULT_HIGH` | DOUBLE | NOT NULL |  | Defines the high end of the trimming range. Results greater than the result high value will not be used to create the quality control result. |
| 12 | `RESULT_LOW` | DOUBLE | NOT NULL |  | Defines the low end of the trimming range. Results less than the result low value will not be used to create the quality control result. |
| 13 | `SEQUENCE` | DOUBLE | NOT NULL |  | Stores the sequence of the ranges for a set of patient data monitoring parameters. |
| 14 | `SEX_CD` | DOUBLE | NOT NULL |  | A unique code value that identifies the gender used to determine if a patient's result should be included or excluded in the calculation of the quality control result. |
| 15 | `SPECIES_CD` | DOUBLE | NOT NULL |  | A unique code value that identifies the species used to determine if a patient's result should be included or excluded in the calculation of the quality control result. |
| 16 | `STD_DEV` | DOUBLE | NOT NULL |  | Defines the expected standard deviation for the given patient data monitoring range. |
| 17 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 18 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 19 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 20 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 21 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `PDM_PARAM_ID` | [PDM_PARAMS](PDM_PARAMS.md) | `PDM_PARAM_ID` |

## Referenced by (2)

| From table | Column |
|------------|--------|
| [QC_RESULT](QC_RESULT.md) | `PDM_RANGE_ID` |
| [QC_STAT_PERIOD](QC_STAT_PERIOD.md) | `PDM_RANGE_ID` |

