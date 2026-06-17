# DCP_PL_STATISTICS

> "Holds statistics related to patient list response time to be used to troubleshoot system problems.And also holds the Organization security and Confididential security information at the time of execution."

**Description:** Holds statistics related to patient list response time to be used to troubleshoo  
**Table type:** ACTIVITY  
**Primary key:** _(not published — see note)_  
**Columns:** 11

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `CONFID_IND` | DOUBLE | NOT NULL |  | Indicates whether confidentiality security was active when the patient list was executed. |
| 2 | `PATIENT_LIST_ID` | DOUBLE | NOT NULL | FK→ | The id of the patient list that was executed |
| 3 | `PATIENT_LIST_TYPE` | VARCHAR(12) | NOT NULL |  | The type of patient list that was executed. |
| 4 | `QUAL` | DOUBLE | NOT NULL |  | The number of patients that were qualified by the patient list |
| 5 | `RESPONSE` | DOUBLE | NOT NULL |  | The number of seconds spent identifying the patients that qualified for the patient list. |
| 6 | `SECURITY_IND` | DOUBLE | NOT NULL |  | Indicates whether organization security was active when the patient list was executed. |
| 7 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 8 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 9 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 10 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 11 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `PATIENT_LIST_ID` | [DCP_PATIENT_LIST](DCP_PATIENT_LIST.md) | `PATIENT_LIST_ID` |

