# RAD_MAMMO_STUDY_ASSESS_MGMT_R

> The RAD_MAMMO_STUDY_ASSESS_MGMT_R table contains assessment, management information for a study

**Description:** Mammography Study Assessment and Management Relation  
**Table type:** ACTIVITY  
**Primary key:** _(not published — see note)_  
**Columns:** 12

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `FINAL_ASSESS_IND` | DOUBLE | NOT NULL |  | Indicates if this row is the final assessment for an exam. 0 = no, 1 = yes |
| 2 | `FOLLOW_UP_FIELD_ID` | DOUBLE | NOT NULL | FK→ | The management step associated to this Mammo Study. |
| 3 | `MODALITY_TYPE_FLAG` | DOUBLE | NOT NULL |  | Indicates the type of modality group. |
| 4 | `RADIOLOGIST_ID` | DOUBLE |  | FK→ | For the assessments documented by the double read radiologist ID(Physician Identifier 2 or Physician Identifier 3) stores their Id for a given study |
| 5 | `RAD_MAMMOSTUDY_ASSESSMGMT_R_ID` | DOUBLE | NOT NULL |  | Unique, generated number that identifies a single row on the RAD_MAMMO_STUDY_ASSESS_MGMT_R table. |
| 6 | `SPECIAL_PROCESS_FLAG` | DOUBLE | NOT NULL |  | Special processing flag used by case maintenance |
| 7 | `STUDY_ID` | DOUBLE | NOT NULL | FK→ | The study that this assessment management relates to. |
| 8 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 9 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 10 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 11 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 12 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `FOLLOW_UP_FIELD_ID` | [RAD_FOL_UP_FIELD](RAD_FOL_UP_FIELD.md) | `FOLLOW_UP_FIELD_ID` |
| `RADIOLOGIST_ID` | [PRSNL](PRSNL.md) | `PERSON_ID` |
| `STUDY_ID` | [MAMMO_STUDY](MAMMO_STUDY.md) | `STUDY_ID` |

