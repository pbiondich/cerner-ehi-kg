# AOAV_ICU_STAY

> This table is for AOAV reporting. This table defines the AOAV ICU stay (time patient is in an AOAV ICU mapped level of care) for a patient transferred to an AOAV ICU.

**Description:** AOAV ICU STAY  
**Table type:** ACTIVITY  
**Primary key:** `AOAV_ICU_STAY_ID`  
**Columns:** 17  
**Referenced by:** 1 columns

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ACTIVE_IND` | DOUBLE | NOT NULL |  | The table row is active or inactive. A row is generally active unless it is in an inactive state such as logically deleted, combined away, pending purge, etc. |
| 2 | `ACTIVE_STATUS_CD` | DOUBLE | NOT NULL |  | Indicates the status of the row itself (not the data in the row) such as active, inactive, combined away, pending purge, etc. |
| 3 | `ACTIVE_STATUS_DT_TM` | DATETIME | NOT NULL |  | The date and time that the active_status_cd was set. |
| 4 | `ACTIVE_STATUS_PRSNL_ID` | DOUBLE | NOT NULL |  | The person who caused the active_status_cd to be set or change. |
| 5 | `AOAV_ICU_STAY_ID` | DOUBLE | NOT NULL | PK | PRIMARY KEY |
| 6 | `ENCNTR_ID` | DOUBLE | NOT NULL | FK→ | The Encounter identifier from the ENCOUNTER record |
| 7 | `ICU_ADMIT_DT_TM` | DATETIME |  |  | ICU Admit Date and Time |
| 8 | `ICU_DECEASED_IND` | DOUBLE | NOT NULL |  | ICU Deceased Indicator |
| 9 | `ICU_DISCH_DT_TM` | DATETIME |  |  | ICU discharge date time |
| 10 | `ICU_VENT_DURATION_ACTUAL_VALUE` | DOUBLE |  |  | ICU vent duration actual value |
| 11 | `INITIAL_LOC_NURSE_UNIT_CD` | DOUBLE | NOT NULL | FK→ | Initial location nurse unit code |
| 12 | `PERSON_ID` | DOUBLE | NOT NULL |  | ** OBSOLETE ** This field is no longer used - DBARCHDTL-23349 |
| 13 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 14 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 15 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 16 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 17 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `ENCNTR_ID` | [ENCOUNTER](ENCOUNTER.md) | `ENCNTR_ID` |
| `INITIAL_LOC_NURSE_UNIT_CD` | [LOCATION](LOCATION.md) | `LOCATION_CD` |

## Referenced by (1)

| From table | Column |
|------------|--------|
| [AOAV_ICU_OUTCOMES](AOAV_ICU_OUTCOMES.md) | `AOAV_ICU_STAY_ID` |

