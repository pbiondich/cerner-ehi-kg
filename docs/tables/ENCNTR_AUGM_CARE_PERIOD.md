# ENCNTR_AUGM_CARE_PERIOD

> Represents augmeneted care periods within an encounter.

**Description:** Encounter Augmented Care Period  
**Table type:** ACTIVITY  
**Primary key:** `ENCNTR_AUGM_CARE_PERIOD_ID`  
**Columns:** 22  
**Referenced by:** 1 columns

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ACTIVE_IND` | DOUBLE | NOT NULL |  | The table row is active or inactive. A row is generally active unless it is in an inactive state such as logically deleted, combined away, pending purge, etc. |
| 2 | `ACTIVE_STATUS_CD` | DOUBLE | NOT NULL |  | Indicates the status of the row itself (not the data in the row) such as active, inactive, combined away, pending purge, etc. |
| 3 | `ACTIVE_STATUS_DT_TM` | DATETIME | NOT NULL |  | The date and time that the active_status_cd was set. |
| 4 | `ACTIVE_STATUS_PRSNL_ID` | DOUBLE | NOT NULL |  | The person who caused the active_status_cd to be set or change. |
| 5 | `AUGM_CARE_PERIOD_DISPOSAL_CD` | DOUBLE | NOT NULL |  | The encounter's disposition of their respective augmented care period. |
| 6 | `AUGM_CARE_PERIOD_PLAN_CD` | DOUBLE | NOT NULL |  | An indication of whether any of an augmented care period was initiated as a planned event. |
| 7 | `AUGM_CARE_PERIOD_SOURCE_CD` | DOUBLE | NOT NULL |  | The source of the augmented care period. |
| 8 | `AUGM_MEDICAL_SERVICE_CD` | DOUBLE | NOT NULL |  | The type or category of medical service that the patient is receiving in relation to their augmented care period. The category may be of treatment type, surgery, general resources, or other. |
| 9 | `BEG_EFFECTIVE_DT_TM` | DATETIME |  |  | The date and time for which this table row becomes effective. Normally, this will be the date and time the row is added, but could be a past or future date and time. |
| 10 | `ENCNTR_AUGM_CARE_PERIOD_ID` | DOUBLE | NOT NULL | PK | Unique identifier for this table. |
| 11 | `ENCNTR_ID` | DOUBLE | NOT NULL | FK→ | The identifier of the encounter for the augmented care period. |
| 12 | `ENCNTR_SLICE_ID` | DOUBLE | NOT NULL | FK→ | Identifies an Encounter as it relates to a time slice. |
| 13 | `END_EFFECTIVE_DT_TM` | DATETIME |  |  | The date/time after which the row is no longer valid as active current data. This may be valued with the date that the row became inactive. |
| 14 | `HIGH_DEPEND_CARE_LVL_DAYS` | DOUBLE |  |  | The number of days the patient received high dependency care within an augmented care period. |
| 15 | `INTENSIVE_CARE_LVL_DAYS` | DOUBLE |  |  | The number of days the patient received intensive care within an augmented care period. |
| 16 | `NUM_ORGAN_SYS_SUPPORT_NBR` | DOUBLE |  |  | The maximum number of organ systems supported during an augmented care period at any one time. |
| 17 | `PERSON_ID` | DOUBLE | NOT NULL |  | OBSOLETE - This column no longer used. |
| 18 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 19 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 20 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 21 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 22 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `ENCNTR_ID` | [ENCOUNTER](ENCOUNTER.md) | `ENCNTR_ID` |
| `ENCNTR_SLICE_ID` | [ENCNTR_SLICE](ENCNTR_SLICE.md) | `ENCNTR_SLICE_ID` |

## Referenced by (1)

| From table | Column |
|------------|--------|
| [ENCNTR_ACP_HIST](ENCNTR_ACP_HIST.md) | `ENCNTR_AUGM_CARE_PERIOD_ID` |

