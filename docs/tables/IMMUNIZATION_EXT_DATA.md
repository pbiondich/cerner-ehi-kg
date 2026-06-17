# IMMUNIZATION_EXT_DATA

> To temporarily hold untrusted data that has come from an external source (e.g. FHIR)

**Description:** External staging data table for Immunizations concept  
**Table type:** ACTIVITY  
**Primary key:** _(not published — see note)_  
**Columns:** 24

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ACTION_DT_TM` | DATETIME |  |  | The date and time of the action. |
| 2 | `ACTION_PRSNL_ID` | DOUBLE | NOT NULL | FK→ | The personnel who performed the action. |
| 3 | `ACTIVE_IND` | DOUBLE | NOT NULL |  | The table row is active or inactive. A row is generally active unless it is in an inactive state such as logically deleted, combined away, pending purge, etc. |
| 4 | `ACTIVE_STATUS_CD` | DOUBLE | NOT NULL |  | Indicates the status of the row itself (not the data in the row) such as active, inactive, combined away, pending purge, etc. |
| 5 | `ACTIVE_STATUS_DT_TM` | DATETIME | NOT NULL |  | The date and time that the active_status_cd was set. |
| 6 | `ACTIVE_STATUS_PRSNL_ID` | DOUBLE | NOT NULL |  | The person who caused the active_status_cd to be set or change. |
| 7 | `ADMIN_DT_TM_TXT` | VARCHAR(30) | NOT NULL |  | The date and time for the administrative action in ISO 8601 format. Date and Time will be local. |
| 8 | `CLIENT_IDENT` | VARCHAR(255) | NOT NULL |  | An unique string representing the registration information provided by the client |
| 9 | `CORRELATION_IDENT` | VARCHAR(80) | NOT NULL |  | Upper case hyphenated GUID that identifies the transaction that updated this row. |
| 10 | `DATA_STATUS_CD` | DOUBLE | NOT NULL |  | Data status indicates a level of authenticity of the row data. |
| 11 | `ENCNTR_ID` | DOUBLE | NOT NULL | FK→ | The encounter related to the external data. |
| 12 | `EVENT_CD` | DOUBLE | NOT NULL |  | The event code for the immunization. |
| 13 | `EVENT_ID` | DOUBLE | NOT NULL |  | An EVENT_ID from tha CLINICAL_EVENT table. Identifies the CLINICAL EVENT/s associated to this immunization |
| 14 | `IMMUNIZATION_EXT_CLOB_ID` | DOUBLE | NOT NULL | FK→ | The associated data that came from an external interface. |
| 15 | `IMMUNIZATION_EXT_DATA_ID` | DOUBLE | NOT NULL |  | PRIMARY KEY |
| 16 | `PERSONA_TXT` | VARCHAR(40) |  |  | The persona is part of the OAuth2 token, and indicates the type of user contacting the service. |
| 17 | `PERSON_ID` | DOUBLE | NOT NULL | FK→ | The PERSON related to the external data |
| 18 | `REQUESTED_ACTION_CD` | DOUBLE | NOT NULL |  | Action requested for the data. |
| 19 | `SUBMITTED_DT_TM` | DATETIME |  |  | The date and time this external data was added to the staging tables. |
| 20 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 21 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 22 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 23 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 24 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `ACTION_PRSNL_ID` | [PRSNL](PRSNL.md) | `PERSON_ID` |
| `ENCNTR_ID` | [ENCOUNTER](ENCOUNTER.md) | `ENCNTR_ID` |
| `IMMUNIZATION_EXT_CLOB_ID` | [IMMUNIZATION_EXT_CLOB](IMMUNIZATION_EXT_CLOB.md) | `IMMUNIZATION_EXT_CLOB_ID` |
| `PERSON_ID` | [PERSON](PERSON.md) | `PERSON_ID` |

