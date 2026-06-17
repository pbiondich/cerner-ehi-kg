# LH_CNT_IC_PATIENT_INFO

> The table stores the patient demographic information

**Description:** LH CNT IC PATIENT INFO  
**Table type:** ACTIVITY  
**Primary key:** _(not published — see note)_  
**Columns:** 23

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ACTIVE_IND` | DOUBLE | NOT NULL |  | The table row is active or inactive. A row is generally active unless it is in an inactive state such as logically deleted, combined away, pending purge, etc. |
| 2 | `ADMIT_DT_TM` | DATETIME |  |  | Admit date/time of the patient |
| 3 | `AGE_DISPLAY` | VARCHAR(100) |  |  | The textual representation of the patient's age including unit of measure display. Ex: 50 years old. |
| 4 | `ALTERNATE_ALIAS` | VARCHAR(200) |  |  | The patients alternate alias such as community MRN. |
| 5 | `DECEASED_IND` | DOUBLE | NOT NULL |  | 0=Not deceased, 1=Deceased |
| 6 | `DISCH_DT_TM` | DATETIME |  |  | Patient's discharge date/time |
| 7 | `DOB_DT_TM` | DATETIME |  |  | Patient's date of birth |
| 8 | `FIN_DISPLAY` | VARCHAR(200) |  |  | The patients FIN number |
| 9 | `GENDER_DISPLAY` | VARCHAR(40) |  |  | Patient's gender |
| 10 | `LENGTH_OF_STAY` | DOUBLE | NOT NULL |  | Length of stay for this encounter |
| 11 | `LH_CNT_IC_PATIENT_INFO_ID` | DOUBLE | NOT NULL |  | Unique generated number that identifies a single row on the LH_CNT_IC_PATIENT_INFO table. |
| 12 | `LH_CNT_IC_PATIENT_POP_ID` | DOUBLE | NOT NULL | FK→ | Foreign key to lh_cnt_ic_patient_pop. |
| 13 | `LOCATION_DISPLAY` | VARCHAR(255) |  |  | The location for this patient's encounter |
| 14 | `MRN_DISPLAY` | VARCHAR(200) |  |  | The patients MRN number |
| 15 | `NAME_FULL_FORMATTED` | VARCHAR(100) |  |  | Full name of the patient |
| 16 | `PCP_NAME` | VARCHAR(100) |  |  | The patient's primary care physician |
| 17 | `REASON_FOR_VISIT` | VARCHAR(255) |  |  | The description of reason for visit. Otherwise known as admitting symptom, presenting symptom, etc. It is a brief description of why the person has presented for examination or treatment and may be the patient described symptom. |
| 18 | `RECURRING_IND` | DOUBLE | NOT NULL |  | Indicator to determine if the patient's encounter is recurring. 0=Not recurring, 1=Recurring. |
| 19 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 20 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 21 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 22 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 23 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `LH_CNT_IC_PATIENT_POP_ID` | [LH_CNT_IC_PATIENT_POP](LH_CNT_IC_PATIENT_POP.md) | `LH_CNT_IC_PATIENT_POP_ID` |

