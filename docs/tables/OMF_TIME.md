# OMF_TIME

> Denormalized table holding various temporal groupings of minutes. This reference table holds a record for each minute of the day.

**Description:** OMF_TIME  
**Table type:** REFERENCE  
**Primary key:** `MIN_NBR`  
**Columns:** 11  
**Referenced by:** 18 columns

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `AM_IND` | DOUBLE |  |  | Indicates if the minute occurred in the morning, before 12:00 pm. |
| 2 | `HALF_HOUR_IND` | DOUBLE |  |  | Indicates the minute is part of the second half of the hour. |
| 3 | `HOUR` | DOUBLE |  |  | Holds the numeric hour of day the minute falls in. |
| 4 | `HOUR_STR` | VARCHAR(13) |  |  | String representation of the hour the minute falls in. |
| 5 | `MIN_NBR` | DOUBLE | NOT NULL | PK | Minute number of day, 1..1440. |
| 6 | `TIME_STR` | VARCHAR(5) |  |  | String representation of the time the min_nbr represents. |
| 7 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 8 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 9 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 10 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 11 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Referenced by (18)

| From table | Column |
|------------|--------|
| [WHC_F_CHILD](WHC_F_CHILD.md) | `CHILD_BIRTH_TIME_NBR` |
| [WHC_F_CHILD](WHC_F_CHILD.md) | `NEONATE_ADMISSION_TIME_NBR` |
| [WHC_F_CHILD](WHC_F_CHILD.md) | `NEONATE_DISCHARGE_TIME_NBR` |
| [WHC_F_CHILD](WHC_F_CHILD.md) | `SKIN_SKIN_CONTCT_INT_TIME_NBR` |
| [WHC_F_DELIVERY](WHC_F_DELIVERY.md) | `CMPLT_CERV_DIALTN_TIME_NBR` |
| [WHC_F_DELIVERY](WHC_F_DELIVERY.md) | `EPIDURAL_BOLUS_ANES_TIME_NBR` |
| [WHC_F_DELIVERY](WHC_F_DELIVERY.md) | `EPIDURAL_BOLUS_PATNT_TIME_NBR` |
| [WHC_F_DELIVERY](WHC_F_DELIVERY.md) | `EPIDURAL_DISCONTINUED_TIME_NBR` |
| [WHC_F_DELIVERY](WHC_F_DELIVERY.md) | `EPIDURAL_START_TIME_NBR` |
| [WHC_F_DELIVERY](WHC_F_DELIVERY.md) | `EPIDURAL_TEST_DOSE_TIME_NBR` |
| [WHC_F_DELIVERY](WHC_F_DELIVERY.md) | `LABOR_ONSET_TIME_NBR` |
| [WHC_F_DELIVERY_CHILD](WHC_F_DELIVERY_CHILD.md) | `DELIVERY_TIME_NBR` |
| [WHC_F_DELIVERY_CHILD](WHC_F_DELIVERY_CHILD.md) | `PLACENTA_DELIVERY_TIME_NBR` |
| [WHC_F_DELIVERY_CHILD](WHC_F_DELIVERY_CHILD.md) | `ROM_TIME_NBR` |
| [WHC_F_MOTHER_PREGNANCY](WHC_F_MOTHER_PREGNANCY.md) | `ADMIT_TIME_NBR` |
| [WHC_F_MOTHER_PREGNANCY](WHC_F_MOTHER_PREGNANCY.md) | `DISCHARGE_TIME_NBR` |
| [WHC_F_MOTHER_PREGNANCY](WHC_F_MOTHER_PREGNANCY.md) | `PREGNANCY_CLOSE_TIME_NBR` |
| [WHC_F_MOTHER_PREGNANCY](WHC_F_MOTHER_PREGNANCY.md) | `PREGNANCY_ONSET_TIME_NBR` |

