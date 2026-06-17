# LH_MU_FX_STATUS

> Display Meaningful Use compliance status for a given person and encounter

**Description:** LH_MU_FX_STATUS  
**Table type:** ACTIVITY  
**Primary key:** _(not published — see note)_  
**Columns:** 33

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `CLIN_REC_S3_IND` | DOUBLE |  |  | The indicator shows if the MU Stage 3 Clinical Reconcilation is met or not |
| 2 | `CLIN_SUMM_IND` | DOUBLE |  |  | Whether or not Clinical Summaries was met for this encounter. |
| 3 | `ENCNTR_ID` | DOUBLE | NOT NULL |  | Foreign key from the ENCOUNTER table |
| 4 | `EXTRACT_DT_TM` | DATETIME |  |  | The date and time when the row was extracted |
| 5 | `FAM_HIST_IND` | DOUBLE |  |  | Whether or not Family History was met for this encounter. |
| 6 | `FIRST_PROCESS_DT_TM` | DATETIME |  |  | The date/time that the first ETL process started that created this record. |
| 7 | `HEALTH_SYSTEM_ID` | DOUBLE | NOT NULL |  | Identifies the delivery network responsible for supplying the data. |
| 8 | `HEALTH_SYSTEM_SOURCE_ID` | DOUBLE | NOT NULL |  | Identifies the unique source within the delivery network responsible for supplying the data. |
| 9 | `INC_DATA_S3_IND` | DOUBLE |  |  | The indicator shows if the MU Stage 3 Incorporate Data is met or not |
| 10 | `LAST_PROCESS_DT_TM` | DATETIME |  |  | The date/time that the last ETL process started that updated this record. |
| 11 | `LH_MU_FX_STATUS_ID` | DOUBLE | NOT NULL |  | Unique generated number that identifies a single row on the LH_MU_FX_STATUS table. |
| 12 | `LOGICAL_DOMAIN_ID` | DOUBLE | NOT NULL |  | The unique identifier for a logical domain. This identifier allows the data to be grouped by logical domain. For example, If you assign clients a logical_domain_id this would allow you to store data for multiple clients on this table. |
| 13 | `MED_ALL_IND` | DOUBLE |  |  | Whether or not the Medication Allergies measure was met for this encounter. |
| 14 | `MED_LIST_IND` | DOUBLE |  |  | Whether or not Medication List was met for this encounter. |
| 15 | `MED_REC_IND` | DOUBLE |  |  | Whether or not Medication Reconciliation was met for this encounter. |
| 16 | `MU_STAGE_FLAG` | DOUBLE |  |  | What Meaningful Use stage this row corresponds to.1 - This row represents Meaningful Use Stage 12 - This row represents Meaningful Use Stage 2 |
| 17 | `PAT_ACC_S3_IND` | DOUBLE |  |  | The indicator shows if the MU Stage 3 Patient Access is met or not |
| 18 | `PAT_DEMO_IND` | DOUBLE |  |  | Whether or not Patient Demographics was met for this encounter. |
| 19 | `PAT_ED_IND` | DOUBLE |  |  | Whether or not Patient Education was met for this encounter. |
| 20 | `PAT_ED_S3_IND` | DOUBLE |  |  | The indicator shows if the MU Stage 3 Patient Education is met or not |
| 21 | `PERSON_ID` | DOUBLE | NOT NULL |  | Foreign key from the PERSON table |
| 22 | `PGHI_S3_IND` | DOUBLE |  |  | The indicatior shows if the MU Stage 3 Patient generated health Info measure is met or not |
| 23 | `POSITION_CD` | DOUBLE | NOT NULL |  | The position is used to determine the applications and tasks the personnel is authorized to use. |
| 24 | `PROB_LIST_IND` | DOUBLE |  |  | Whether or not Problem List was met for this encounter. |
| 25 | `PROG_NOTE_IND` | DOUBLE |  |  | Whether or not Progress Note was met for this encounter. |
| 26 | `PROVIDER_ID` | DOUBLE | NOT NULL |  | Foreign key on PERSON_ID from the PRSNL table |
| 27 | `SEC_MSG_S3_IND` | DOUBLE |  |  | The indicator shows if the MU Stage 3 Secure Messaging is met or not |
| 28 | `SMOKING_IND` | DOUBLE |  |  | Whether or not Smoking Status was met for this encounter. |
| 29 | `UPDT_CNT` | DOUBLE |  |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 30 | `UPDT_DT_TM` | DATETIME |  |  | The date and time the row was last inserted or updated. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 31 | `UPDT_SOURCE` | VARCHAR(50) |  |  | The script name responsible for updating the record. |
| 32 | `UPDT_TASK` | VARCHAR(50) |  |  | The registered (assigned) task number for the process that inserted or updated the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 33 | `VITAL_SIGNS_IND` | DOUBLE |  |  | Whether or not Vital Signs was met for this encounter. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

