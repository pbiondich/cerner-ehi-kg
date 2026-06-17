# CONDITIONAL_DTA

> The DTA that needs enabled or disable

**Description:** Conditional DTA  
**Table type:** REFERENCE  
**Primary key:** `CONDITIONAL_DTA_ID`  
**Columns:** 21  
**Referenced by:** 2 columns

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ACTIVE_IND` | DOUBLE | NOT NULL |  | The table row is active or inactive. A row is generally active unless it is in an inactive state such as logically deleted, combined away, pending purge, etc. |
| 2 | `AGE_FROM_NBR` | DOUBLE | NOT NULL |  | Starting age on a range |
| 3 | `AGE_FROM_UNIT_CD` | DOUBLE | NOT NULL |  | Unit of measure for age from |
| 4 | `AGE_TO_NBR` | DOUBLE | NOT NULL |  | Ending age on a range |
| 5 | `AGE_TO_UNIT_CD` | DOUBLE | NOT NULL |  | Unit of measure for age to |
| 6 | `BEG_EFFECTIVE_DT_TM` | DATETIME | NOT NULL |  | The date and time for which this table row becomes effective. Normally, this will be the date and time the row is added, but could be a past or future date and time. |
| 7 | `CONDITIONAL_ASSAY_CD` | DOUBLE | NOT NULL | FK→ | The dta that needs to enable/diabled |
| 8 | `CONDITIONAL_DTA_ID` | DOUBLE | NOT NULL | PK | Primary key |
| 9 | `COND_EXPRESSION_ID` | DOUBLE | NOT NULL | FK→ | Foreign key on conditional expression |
| 10 | `END_EFFECTIVE_DT_TM` | DATETIME | NOT NULL |  | The date/time after which the row is no longer valid as active current data. This may be valued with the date that the row became inactive. |
| 11 | `GENDER_CD` | DOUBLE | NOT NULL |  | Sex of the patient |
| 12 | `LOCATION_CD` | DOUBLE | NOT NULL |  | Location of the patient |
| 13 | `POSITION_CD` | DOUBLE | NOT NULL |  | Position_cd of documented user |
| 14 | `PREV_CONDITIONAL_DTA_ID` | DOUBLE | NOT NULL | FK→ | Unique identifier or Original conditional dta id |
| 15 | `REQUIRED_IND` | DOUBLE | NOT NULL |  | DTA needs documented |
| 16 | `UNKNOWN_AGE_IND` | DOUBLE | NOT NULL |  | UNKNOWN AGE INDICATOR. Age of the patient is unknown. |
| 17 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 18 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 19 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 20 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 21 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `CONDITIONAL_ASSAY_CD` | [DISCRETE_TASK_ASSAY](DISCRETE_TASK_ASSAY.md) | `TASK_ASSAY_CD` |
| `COND_EXPRESSION_ID` | [COND_EXPRESSION](COND_EXPRESSION.md) | `COND_EXPRESSION_ID` |
| `PREV_CONDITIONAL_DTA_ID` | [CONDITIONAL_DTA](CONDITIONAL_DTA.md) | `CONDITIONAL_DTA_ID` |

## Referenced by (2)

| From table | Column |
|------------|--------|
| [CNT_CONDITIONAL_DTA_KEY](CNT_CONDITIONAL_DTA_KEY.md) | `DCP_COND_DTA_REF_ID` |
| [CONDITIONAL_DTA](CONDITIONAL_DTA.md) | `PREV_CONDITIONAL_DTA_ID` |

