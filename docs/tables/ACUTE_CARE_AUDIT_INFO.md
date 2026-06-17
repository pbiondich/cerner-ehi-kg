# ACUTE_CARE_AUDIT_INFO

> Contains auditing info about specific events that occurred during Acute Care workflows.

**Description:** ACUTE CARE AUDIT INFO  
**Table type:** ACTIVITY  
**Primary key:** _(not published — see note)_  
**Columns:** 14

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ACUTE_CARE_AUDIT_INFO_ID` | DOUBLE | NOT NULL |  | Primary Key |
| 2 | `AUDIT_EVENT_DT_TM` | DATETIME | NOT NULL |  | Date and time when the audit information was written out into the system. |
| 3 | `AUDIT_EVENT_TYPE_CD` | DOUBLE | NOT NULL |  | Code value that defines the type of audit event that was written out. |
| 4 | `AUDIT_FACILITY_CD` | DOUBLE | NOT NULL |  | Facility code in context when the auditing event occurred |
| 5 | `AUDIT_INFORMATION_TEXT` | VARCHAR(255) |  |  | Additional information for the audit event that occurred. |
| 6 | `AUDIT_PATIENT_ID` | DOUBLE | NOT NULL | FK→ | Person ID of the patient the audit event was performed on. 0 if action was not patient specific. |
| 7 | `AUDIT_PRSNL_ID` | DOUBLE | NOT NULL | FK→ | Person ID of the user logged in when the audit event occurred. |
| 8 | `AUDIT_SOLUTION_CD` | DOUBLE | NOT NULL |  | Code value for the solution the audit was written out from. |
| 9 | `POSITION_CD` | DOUBLE | NOT NULL |  | Position Code of the user logged in when the audit event occurred. |
| 10 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 11 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 12 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 13 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 14 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `AUDIT_PATIENT_ID` | [PERSON](PERSON.md) | `PERSON_ID` |
| `AUDIT_PRSNL_ID` | [PRSNL](PRSNL.md) | `PERSON_ID` |

