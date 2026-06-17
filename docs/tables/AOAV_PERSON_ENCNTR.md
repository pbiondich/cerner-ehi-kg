# AOAV_PERSON_ENCNTR

> This table has all the person and encounter related information of retrieved patients

**Description:** AOAV_PERSON_ENCNTR  
**Table type:** ACTIVITY  
**Primary key:** _(not published — see note)_  
**Columns:** 27

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ACTIVE_IND` | DOUBLE | NOT NULL |  | The table row is active or inactive. A row is generally active unless it is in an inactive state such as logically deleted, combined away, pending purge, etc. |
| 2 | `ACTIVE_STATUS_CD` | DOUBLE |  |  | Indicates the status of the row itself (not the data in the row) such as active, inactive, combined away, pending purge, etc. |
| 3 | `ACTIVE_STATUS_DT_TM` | DATETIME |  |  | The date and time that the active_status_cd was set. |
| 4 | `ACTIVE_STATUS_PRSNL_ID` | DOUBLE |  |  | The person who caused the active_status_cd to be set or change. |
| 5 | `AOAV_DISCH_LOC_TYPE_CD` | DOUBLE | NOT NULL |  | AOAV persons discharge location mapped to location codes from code set 20 |
| 6 | `AOAV_PERSON_ENCNTR_ID` | DOUBLE | NOT NULL |  | PRIMARY KEY |
| 7 | `AOAV_PRIOR_LOC_TYPE_CD` | DOUBLE | NOT NULL |  | AOAV persons prior location mapped to location codes from code set 2 |
| 8 | `AOAV_RACE_CD` | DOUBLE | NOT NULL |  | Race code of the person mapped to code values from code set 282 |
| 9 | `AOAV_SEX_CD` | DOUBLE | NOT NULL |  | Gender code of the person mapped to code values from code set 57 |
| 10 | `BIRTH_DT_TM` | DATETIME |  |  | Date of birth of the person |
| 11 | `CALCULATED_FLAG` | DOUBLE | NOT NULL |  | The calculated flag giving the state of the person-encounter data. 0 = needs to be calculated 1 = calculation in progress 2 = calculation done 3 = Calculation ready to summarize 4 = Calculation summarized 5 = Calculation Failed |
| 12 | `CALC_BIT_MASK_NBR` | DOUBLE |  |  | Bits determine which calculations need to be performed for the person |
| 13 | `DECEASED_DT_TM` | DATETIME |  |  | DATE AND TIME PERSON WAS DECEASED |
| 14 | `DECEASED_IND` | DOUBLE | NOT NULL |  | Deceased indicator 0=Not deceased, 1=Deceased |
| 15 | `ENCNTR_ID` | DOUBLE | NOT NULL | FK→ | Unique identifier for the Encounter |
| 16 | `FIRST_LEVEL_OF_CARE_DT_TM` | DATETIME |  |  | The admit date time to the first AOAV level of care in the encounter |
| 17 | `HOSP_ADMIT_DT_TM` | DATETIME |  |  | Hospital admit date time of the encounter |
| 18 | `HOSP_DISCH_DT_TM` | DATETIME |  |  | Hospital discharge date time of the encounter |
| 19 | `HOSP_DISCH_IND` | DOUBLE | NOT NULL |  | Indicator to indicate if the hospital encounter has been discharged. |
| 20 | `LOC_FACILITY_CD` | DOUBLE | NOT NULL |  | Location facility code |
| 21 | `PERSON_ID` | DOUBLE | NOT NULL | FK→ | Unique identifier for the Person |
| 22 | `PREV_ENCNTR_CNT` | DOUBLE |  |  | Number of previous encounters for the person |
| 23 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 24 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 25 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 26 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 27 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `ENCNTR_ID` | [ENCOUNTER](ENCOUNTER.md) | `ENCNTR_ID` |
| `PERSON_ID` | [PERSON](PERSON.md) | `PERSON_ID` |

