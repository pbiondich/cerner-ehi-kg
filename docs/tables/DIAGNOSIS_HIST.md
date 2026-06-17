# DIAGNOSIS_HIST

> Used to store history of diagnoses in Chart Coding

**Description:** Diagnosis History  
**Table type:** ACTIVITY  
**Primary key:** _(not published — see note)_  
**Columns:** 24

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ACTIVE_IND` | DOUBLE | NOT NULL |  | The table row is active or inactive. A row is generally active unless it is in an inactive state such as logically deleted, combined away, pending purge, etc. |
| 2 | `BEG_EFFECTIVE_DT_TM` | DATETIME |  |  | The date and time for which this table row becomes effective. Normally, this will be the date and time the row is added, but could be a past or future date and time. |
| 3 | `CONTRIBUTOR_SYSTEM_CD` | DOUBLE | NOT NULL |  | Contributor system identifies the source feed of data from which a row was populated. This is mainly used to determine how to update a set of data that may have originated from more than one source feed. |
| 4 | `DIAGNOSIS_HIST_ID` | DOUBLE | NOT NULL |  | This is the unique identifier for a diagnosis history row. It is an internal, system-assigned number. |
| 5 | `DIAGNOSIS_ID` | DOUBLE | NOT NULL |  | This is the unique identifier for the diagnosis. It is an internal, system-assigned number. |
| 6 | `DIAG_DT_TM` | DATETIME |  |  | Date/time when the diagnosis was made. |
| 7 | `DIAG_PRIORITY` | DOUBLE | NOT NULL |  | The priority of the diagnosis. |
| 8 | `DIAG_TYPE_CD` | DOUBLE | NOT NULL |  | The type of diagnosis (final, admitting, reason for visit, etc¿) |
| 9 | `ENCNTR_ID` | DOUBLE | NOT NULL | FK→ | This is the value of the unique identifier of the encounter table. It is an internal, system-assigned number |
| 10 | `ENCNTR_SLICE_ID` | DOUBLE | NOT NULL | FK→ | Identifies an Encounter as it relates to a time slice. |
| 11 | `END_EFFECTIVE_DT_TM` | DATETIME |  |  | The date/time after which the row is no longer valid as active current data. This may be valued with the date that the row became inactive. |
| 12 | `HAC_IND` | DOUBLE | NOT NULL |  | Indicates that the diagnosis was a Hospital Acquired Condition (HAC) and contributed to a change in the grouper that likely resulted in a lower reimbursement. |
| 13 | `NOMENCLATURE_ID` | DOUBLE | NOT NULL | FK→ | This is the value of the primary identifier of the nomenclature table. It is an internal, system-assigned number. |
| 14 | `PAC_CD` | DOUBLE |  |  | Indicates the post acute care coding value assigned to the diagnosis. |
| 15 | `PARENT_ENTITY_ID` | DOUBLE | NOT NULL |  | Primary key ID from the parent table. |
| 16 | `PARENT_ENTITY_NAME` | VARCHAR(30) | NOT NULL |  | Parent table name. |
| 17 | `PERSON_ID` | DOUBLE | NOT NULL | FK→ | This is the value of the primary identifier of the person table. It is an internal, system-assigned number |
| 18 | `PRESENT_ON_ADMIT_CD` | DOUBLE | NOT NULL |  | Identifies whether the diagnosis was present on admission. |
| 19 | `SVC_CAT_HIST_ID` | DOUBLE | NOT NULL | FK→ | This field is a unique identifier for the service category history table. |
| 20 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 21 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 22 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 23 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 24 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `ENCNTR_ID` | [ENCOUNTER](ENCOUNTER.md) | `ENCNTR_ID` |
| `ENCNTR_SLICE_ID` | [ENCNTR_SLICE](ENCNTR_SLICE.md) | `ENCNTR_SLICE_ID` |
| `NOMENCLATURE_ID` | [NOMENCLATURE](NOMENCLATURE.md) | `NOMENCLATURE_ID` |
| `PERSON_ID` | [PERSON](PERSON.md) | `PERSON_ID` |
| `SVC_CAT_HIST_ID` | [SERVICE_CATEGORY_HIST](SERVICE_CATEGORY_HIST.md) | `SVC_CAT_HIST_ID` |

