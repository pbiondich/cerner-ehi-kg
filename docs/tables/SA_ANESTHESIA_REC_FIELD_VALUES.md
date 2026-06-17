# SA_ANESTHESIA_REC_FIELD_VALUES

> Stores field values for anesthesia record

**Description:** SA Anesthesia Record Field Values  
**Table type:** ACTIVITY  
**Primary key:** _(not published — see note)_  
**Columns:** 25

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ACTIVE_IND` | DOUBLE | NOT NULL |  | The table row is active or inactive. A row is generally active unless it is in an inactive state such as logically deleted, combined away, pending purge, etc. |
| 2 | `ACTIVE_STATUS_CD` | DOUBLE | NOT NULL |  | Indicates the status of the row itself (not the data in the row) such as active, inactive, combined away, pending purge, etc. |
| 3 | `ACTIVE_STATUS_DT_TM` | DATETIME | NOT NULL |  | The date and time that the active_status_cd was set. |
| 4 | `ACTIVE_STATUS_PRSNL_ID` | DOUBLE | NOT NULL |  | The person who caused the active_status_cd to be set or change. |
| 5 | `ADMIT_REASON` | VARCHAR(255) |  |  | Reason For Admit |
| 6 | `ANESTHESIA_TYPE_CD` | DOUBLE | NOT NULL |  | Anesthesia Type Code |
| 7 | `ANESTHESIOLOGIST_ID` | DOUBLE | NOT NULL | FK→ | Anesthesiologist ID |
| 8 | `ASA_CLASS_CD` | DOUBLE | NOT NULL |  | ASA Class Code |
| 9 | `CARDIOLOGIST_ID` | DOUBLE | NOT NULL | FK→ | Cardiologist ID |
| 10 | `DIAGNOSIS_NOMENCLATURE_ID` | DOUBLE | NOT NULL | FK→ | Diagnosis Nomenclature |
| 11 | `ENCNTR_ID` | DOUBLE | NOT NULL | FK→ | ENCOUNTER ID |
| 12 | `NPO_DT_TM` | DATETIME |  |  | NPO Date / Time |
| 13 | `OR_CD` | DOUBLE | NOT NULL |  | Operating Room Code |
| 14 | `PERSON_ID` | DOUBLE | NOT NULL | FK→ | Person ID |
| 15 | `PHYSICIAN_ID` | DOUBLE | NOT NULL | FK→ | Physician ID |
| 16 | `PRE_OP_DIAGNOSIS_TXT` | VARCHAR(255) |  |  | Pre Op Diagnosis TEXT |
| 17 | `PROBLEM_NOMENCLATURE_ID` | DOUBLE | NOT NULL | FK→ | Problem Nomenclature |
| 18 | `PROCEDURE_NOMENCLATURE_ID` | DOUBLE | NOT NULL | FK→ | Procedure Nomenclature |
| 19 | `SA_ANESTHESIA_RECORD_ID` | DOUBLE | NOT NULL | FK→ | SA Anesthesia Record Id |
| 20 | `SA_ANESTHESIA_REC_FIELD_VAL_ID` | DOUBLE | NOT NULL |  | Unique identifier |
| 21 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 22 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 23 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 24 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 25 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `ANESTHESIOLOGIST_ID` | [PRSNL](PRSNL.md) | `PERSON_ID` |
| `CARDIOLOGIST_ID` | [PRSNL](PRSNL.md) | `PERSON_ID` |
| `DIAGNOSIS_NOMENCLATURE_ID` | [NOMENCLATURE](NOMENCLATURE.md) | `NOMENCLATURE_ID` |
| `ENCNTR_ID` | [ENCOUNTER](ENCOUNTER.md) | `ENCNTR_ID` |
| `PERSON_ID` | [PERSON](PERSON.md) | `PERSON_ID` |
| `PHYSICIAN_ID` | [PRSNL](PRSNL.md) | `PERSON_ID` |
| `PROBLEM_NOMENCLATURE_ID` | [NOMENCLATURE](NOMENCLATURE.md) | `NOMENCLATURE_ID` |
| `PROCEDURE_NOMENCLATURE_ID` | [NOMENCLATURE](NOMENCLATURE.md) | `NOMENCLATURE_ID` |
| `SA_ANESTHESIA_RECORD_ID` | [SA_ANESTHESIA_RECORD](SA_ANESTHESIA_RECORD.md) | `SA_ANESTHESIA_RECORD_ID` |

