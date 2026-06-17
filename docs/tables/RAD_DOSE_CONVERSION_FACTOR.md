# RAD_DOSE_CONVERSION_FACTOR

> Contains the conversion factors needed to calculate effective dose .

**Description:** Radiology Dose Conversion Factor  
**Table type:** REFERENCE  
**Primary key:** `RAD_DOSE_CONVERSION_FACTOR_ID`  
**Columns:** 16  
**Referenced by:** 1 columns

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ACTIVE_IND` | DOUBLE | NOT NULL |  | The table row is active or inactive. A row is generally active unless it is in an inactive state such as logically deleted, combined away, pending purge, etc. |
| 2 | `ACTIVITY_SUBTYPE_CD` | DOUBLE | NOT NULL |  | This field contains a code that identifies the dose template modality used for this scan. |
| 3 | `BEGIN_AGE_YEARS` | DOUBLE | NOT NULL |  | The begin age for the selected body part and activity sub type for which this dose conversion factor is being added. |
| 4 | `BEG_EFFECTIVE_DT_TM` | DATETIME | NOT NULL |  | The date and time for which this table row becomes effective. Normally, this will be the date and time the row is added, but could be a past or future date and time. |
| 5 | `BODY_PART_CD` | DOUBLE | NOT NULL |  | *** OBSOLETE *** |
| 6 | `BODY_PART_ID` | DOUBLE | NOT NULL | FK→ | The body part the conversion factor applies to. |
| 7 | `CONVERSION_FACTOR_AMT` | DOUBLE | NOT NULL |  | The conversion factor needed to calculate effective dose for the modality and body part. |
| 8 | `END_AGE_YEARS` | DOUBLE | NOT NULL |  | The ending age for the selected body part and activity sub type for which this dose conversion factor is being added. |
| 9 | `END_EFFECTIVE_DT_TM` | DATETIME | NOT NULL |  | The date/time after which the row is no longer valid as active current data. This may be valued with the date that the row became inactive. |
| 10 | `PREV_CONVERSION_FACTOR_ID` | DOUBLE | NOT NULL | FK→ | This is the previous rad dose conversion factor id which is used to maintain the history. |
| 11 | `RAD_DOSE_CONVERSION_FACTOR_ID` | DOUBLE | NOT NULL | PK | Unique generated number that identifies a single row on the rad_dose_conversion_factor table. |
| 12 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 13 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 14 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 15 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 16 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `BODY_PART_ID` | [RAD_DOSE_SNOMED_RT_GLOSSARY](RAD_DOSE_SNOMED_RT_GLOSSARY.md) | `RAD_DOSE_SNOMED_RT_GLOSSARY_ID` |
| `PREV_CONVERSION_FACTOR_ID` | [RAD_DOSE_CONVERSION_FACTOR](RAD_DOSE_CONVERSION_FACTOR.md) | `RAD_DOSE_CONVERSION_FACTOR_ID` |

## Referenced by (1)

| From table | Column |
|------------|--------|
| [RAD_DOSE_CONVERSION_FACTOR](RAD_DOSE_CONVERSION_FACTOR.md) | `PREV_CONVERSION_FACTOR_ID` |

