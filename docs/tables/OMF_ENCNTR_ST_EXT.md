# OMF_ENCNTR_ST_EXT

> omf_encntr_st_ext

**Description:** Extenstion to the omf_encntr_st.  
**Table type:** ACTIVITY  
**Primary key:** _(not published — see note)_  
**Columns:** 37

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ADMIT_72H_LADMIT_IND` | DOUBLE |  |  | Indicates whether or not the patient has been readmitted w/in 72 hours of a previous visit. |
| 2 | `ADMIT_TZ` | DOUBLE |  |  | Time zone associated with the corresponding DT_TM column. |
| 3 | `BIRTH_DT_NBR` | DOUBLE |  |  | The Julian date of the date on which the patient was born |
| 4 | `BIRTH_MIN_NBR` | DOUBLE |  |  | The minute of the date on which the patient was born |
| 5 | `BIRTH_TZ` | DOUBLE |  |  | Time zone associated with the corresponding DT_TM column. |
| 6 | `CURR_PAT_LOC_ARRIVE_DT_NBR` | DOUBLE |  |  | The Julian date of the date/time at which the patient arrived at the nurse unit |
| 7 | `CURR_PAT_LOC_ARRIVE_MIN_NBR` | DOUBLE |  |  | The minute of the date/time at which the patient arrived at the nurse unit. |
| 8 | `CURR_PAT_LOC_ARRIVE_TZ` | DOUBLE |  |  | Time zone associated with the corresponding DT_TM column. |
| 9 | `DAYS_NEXT_ED_VISIT` | DOUBLE |  |  | The number of days to the next ER visit. |
| 10 | `DEATH_TZ` | DOUBLE |  |  | Time zone associated with the corresponding DT_TM column. |
| 11 | `DISCH_TZ` | DOUBLE |  |  | Time zone associated with the corresponding DT_TM column. |
| 12 | `ENCNTR_ID` | DOUBLE | NOT NULL | FK→ | This is the value of the unique primary identifier of the encounter table. It is an internal system assigned number. |
| 13 | `EXP_PM_DISCH_TZ` | DOUBLE |  |  | Time zone associated with the corresponding DT_TM column. |
| 14 | `ICD9_PRIN_PROC_TZ` | DOUBLE |  |  | Time zone associated with the corresponding DT_TM column. |
| 15 | `LAST_IP_DISCH_TZ` | DOUBLE |  |  | Time zone associated with the corresponding DT_TM column. |
| 16 | `OTHER_INS_BEG_EFFECTIVE_TZ` | DOUBLE |  |  | Time zone associated with the corresponding DT_TM column. |
| 17 | `OTHER_INS_BIRTH_DT_NBR` | DOUBLE |  |  | The Julian date of the other health plan subscriber's birth date/time. |
| 18 | `OTHER_INS_BIRTH_MIN_NBR` | DOUBLE |  |  | The minute of the other health plan subscriber's birth date/time. |
| 19 | `OTHER_INS_BIRTH_TZ` | DOUBLE |  |  | Time zone associated with the corresponding DT_TM column. |
| 20 | `OTHER_INS_END_EFFECTIVE_TZ` | DOUBLE |  |  | Time zone associated with the corresponding DT_TM column. |
| 21 | `PRIM_INS_BEG_EFFECTIVE_TZ` | DOUBLE |  |  | Time zone associated with the corresponding DT_TM column. |
| 22 | `PRIM_INS_BIRTH_DT_NBR` | DOUBLE |  |  | The Julian date of the primary health plan subscriber's birth date/time. |
| 23 | `PRIM_INS_BIRTH_MIN_NBR` | DOUBLE |  |  | The minute of the date of the primary health plan subscriber's birth date/time. |
| 24 | `PRIM_INS_BIRTH_TZ` | DOUBLE |  |  | Time zone associated with the corresponding DT_TM column. |
| 25 | `PRIM_INS_END_EFFECTIVE_TZ` | DOUBLE |  |  | Time zone associated with the corresponding DT_TM column. |
| 26 | `RETURN_ED_GT_72H_IND` | DOUBLE |  |  | Indicates whether or not the patient returned to the ER in greater than 72 hours of a previous visit. |
| 27 | `SEC_INS_BEG_EFFECTIVE_TZ` | DOUBLE |  |  | Time zone associated with the corresponding DT_TM column. |
| 28 | `SEC_INS_BIRTH_DT_NBR` | DOUBLE |  |  | The Julian date of the secondary health plan subscriber's birth date/time. |
| 29 | `SEC_INS_BIRTH_MIN_NBR` | DOUBLE |  |  | The minute of the date of the secondary health plan subscriber's birth date/time. |
| 30 | `SEC_INS_BIRTH_TZ` | DOUBLE |  |  | Time zone associated with the corresponding DT_TM column. |
| 31 | `SEC_INS_END_EFFECTIVE_TZ` | DOUBLE |  |  | Time zone associated with the corresponding DT_TM column. |
| 32 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 33 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 34 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 35 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 36 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |
| 37 | `VISIT_TZ` | DOUBLE |  |  | Time zone associated with the corresponding DT_TM column. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `ENCNTR_ID` | [ENCOUNTER](ENCOUNTER.md) | `ENCNTR_ID` |
| `ENCNTR_ID` | [OMF_ENCNTR_ST](OMF_ENCNTR_ST.md) | `ENCNTR_ID` |

