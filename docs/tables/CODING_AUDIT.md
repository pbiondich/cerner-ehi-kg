# CODING_AUDIT

> Used to store information on Coding Audits that have taken place.

**Description:** Coding Audit  
**Table type:** ACTIVITY  
**Primary key:** _(not published — see note)_  
**Columns:** 24

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ACTIVE_IND` | DOUBLE | NOT NULL |  | The table row is active or inactive. A row is generally active unless it is in an inactive state such as logically deleted, combined away, pending purge, etc. |
| 2 | `AUDIT_PRSNL_ID` | DOUBLE | NOT NULL | FK→ | The personnel identifier of the user that performed the audit of the coding row. It is an internal, system-assigned number. |
| 3 | `BEG_EFFECTIVE_DT_TM` | DATETIME |  |  | The date and time for which this table row becomes effective. Normally, this will be the date and time the row is added, but could be a past or future date and time. |
| 4 | `CODING_AUDIT_ID` | DOUBLE | NOT NULL |  | This is the unique identifier for a coding audit row. It is an internal, system-assigned number. |
| 5 | `CODING_AUDIT_TRIGGER_ID` | DOUBLE | NOT NULL | FK→ | This field is a unique identifier for the coding audit trigger table. |
| 6 | `CODING_PRSNL_ID` | DOUBLE | NOT NULL | FK→ | The personnel identifier of the user that initially coded the row. It is an internal, system-assigned number. |
| 7 | `ENCNTR_ID` | DOUBLE | NOT NULL | FK→ | This is the value of the unique identifier of the encounter table. It is an internal, system-assigned number. |
| 8 | `ENCNTR_SLICE_ID` | DOUBLE | NOT NULL | FK→ | Identifies an Encounter as it relates to a time slice. |
| 9 | `END_EFFECTIVE_DT_TM` | DATETIME |  |  | The date/time after which the row is no longer valid as active current data. This may be valued with the date that the row became inactive. |
| 10 | `ERROR_SOURCE_IDENT` | VARCHAR(50) | NOT NULL |  | The identifier of the error source. |
| 11 | `ERROR_SOURCE_TYPE_CD` | DOUBLE | NOT NULL |  | The type of error source. Examples are Charge, Diagnosis, Grouper, Procedure, etc. |
| 12 | `EXTERNAL_AUDIT_MSG` | VARCHAR(4000) | NOT NULL |  | The external audit message for the coding audit trigger. The specific reason for the audit. |
| 13 | `OUTCOME_CD` | DOUBLE | NOT NULL |  | The outcome of the coding audit. |
| 14 | `PARENT_ENTITY_ID` | DOUBLE | NOT NULL |  | Primary key ID from the parent table. |
| 15 | `PARENT_ENTITY_NAME` | VARCHAR(30) | NOT NULL |  | Parent table name. |
| 16 | `PERSON_ID` | DOUBLE | NOT NULL | FK→ | This is the value of the primary identifier of the person table. It is an internal, system-assigned number. |
| 17 | `SEVERITY_CD` | DOUBLE | NOT NULL |  | The edit severity. Examples are Error and Warning. |
| 18 | `SVC_CAT_HIST_ID` | DOUBLE | NOT NULL | FK→ | This field is a unique identifier for the service category history table. |
| 19 | `TASK_ID` | DOUBLE | NOT NULL | FK→ | An identifier from a row on the task_activity table that is related to the coding audit row. |
| 20 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 21 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 22 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 23 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 24 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `AUDIT_PRSNL_ID` | [PRSNL](PRSNL.md) | `PERSON_ID` |
| `CODING_AUDIT_TRIGGER_ID` | [CODING_AUDIT_TRIGGER](CODING_AUDIT_TRIGGER.md) | `CODING_AUDIT_TRIGGER_ID` |
| `CODING_PRSNL_ID` | [PRSNL](PRSNL.md) | `PERSON_ID` |
| `ENCNTR_ID` | [ENCOUNTER](ENCOUNTER.md) | `ENCNTR_ID` |
| `ENCNTR_SLICE_ID` | [ENCNTR_SLICE](ENCNTR_SLICE.md) | `ENCNTR_SLICE_ID` |
| `PERSON_ID` | [PERSON](PERSON.md) | `PERSON_ID` |
| `SVC_CAT_HIST_ID` | [SERVICE_CATEGORY_HIST](SERVICE_CATEGORY_HIST.md) | `SVC_CAT_HIST_ID` |
| `TASK_ID` | [TASK_ACTIVITY](TASK_ACTIVITY.md) | `TASK_ID` |

