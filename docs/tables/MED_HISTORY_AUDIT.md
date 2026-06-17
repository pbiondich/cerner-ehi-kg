# MED_HISTORY_AUDIT

> This table will be used to audit incoming external medical history transactions. This auditing table will provide troubleshooting capabilities.

**Description:** Medical History Audit  
**Table type:** ACTIVITY  
**Primary key:** `MED_HISTORY_AUDIT_ID`  
**Columns:** 20  
**Referenced by:** 1 columns

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `AUDIT_DT_TM` | DATETIME | NOT NULL |  | The time at which this entry was logged for the transaction |
| 2 | `CONTRIBUTOR_SYSTEM_CD` | DOUBLE | NOT NULL |  | Contributor system identifies the source feed of data from which a row was populated. This is mainly used to determine how to update a set of data that may have originated from more than one source feed. |
| 3 | `ENCNTR_ID` | DOUBLE | NOT NULL | FK→ | The unique identifier to the encounter table. When populated, medication history was requested during the given encounter. |
| 4 | `FACILITY_ORGANIZATION_ID` | DOUBLE | NOT NULL | FK→ | The unique identifier to the organization table. Defines the facility where the patient was located at the time medication history was requested. |
| 5 | `MED_HISTORY_AUDIT_ID` | DOUBLE | NOT NULL | PK | Unique generated number that identifies a single row on the med_history_audit table. |
| 6 | `MESSAGE_TXT` | VARCHAR(255) |  |  | The message corresponding to the provided status for the transaction |
| 7 | `ORIGIN_MED_HISTORY_AUDIT_ID` | DOUBLE | NOT NULL | FK→ | The unique identifier to the med_history_audit table. Identifies the initial transaction to link together medication history transactions that are a part of a group. |
| 8 | `PERSON_ID` | DOUBLE | NOT NULL | FK→ | The person_id corresponding to the external medications to be imported. |
| 9 | `PRESCRIBER_PRSNL_ID` | DOUBLE | NOT NULL | FK→ | The unique identifier of the patient's prescribing provider. |
| 10 | `PRSNL_ID` | DOUBLE | NOT NULL | FK→ | The ID of the person who originally requested the transaction. |
| 11 | `REASON_CD` | DOUBLE | NOT NULL |  | Further defines the reason for the status of the transaction. |
| 12 | `REQUEST_IDENT` | VARCHAR(36) | NOT NULL |  | The Universally Unique Identifier(UUId) assigned to all database entries for the transaction. |
| 13 | `RESPONSE_DT_TM` | DATETIME |  |  | The date and time the response to the request for medication history was received inbound. |
| 14 | `STATUS_CD` | DOUBLE | NOT NULL |  | The status of the external med history transaction. |
| 15 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 16 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 17 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 18 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 19 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 20 | `VENUE_TYPE_CD` | DOUBLE | NOT NULL |  | Defines the venue from where the transaction was submitted. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `ENCNTR_ID` | [ENCOUNTER](ENCOUNTER.md) | `ENCNTR_ID` |
| `FACILITY_ORGANIZATION_ID` | [ORGANIZATION](ORGANIZATION.md) | `ORGANIZATION_ID` |
| `ORIGIN_MED_HISTORY_AUDIT_ID` | [MED_HISTORY_AUDIT](MED_HISTORY_AUDIT.md) | `MED_HISTORY_AUDIT_ID` |
| `PERSON_ID` | [PERSON](PERSON.md) | `PERSON_ID` |
| `PRESCRIBER_PRSNL_ID` | [PRSNL](PRSNL.md) | `PERSON_ID` |
| `PRSNL_ID` | [PRSNL](PRSNL.md) | `PERSON_ID` |

## Referenced by (1)

| From table | Column |
|------------|--------|
| [MED_HISTORY_AUDIT](MED_HISTORY_AUDIT.md) | `ORIGIN_MED_HISTORY_AUDIT_ID` |

