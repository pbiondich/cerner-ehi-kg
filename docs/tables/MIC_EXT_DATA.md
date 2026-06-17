# MIC_EXT_DATA

> External staging table for MIC concept, to temporarily hold untrusted data that has come from and external source (e.g. FHIR)

**Description:** Microbiology External Data  
**Table type:** ACTIVITY  
**Primary key:** `MIC_EXT_DATA_ID`  
**Columns:** 24  
**Referenced by:** 2 columns

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ACTION_PRSNL_DT_TM` | DATETIME |  |  | The date and time of the action. |
| 2 | `ACTION_PRSNL_ID` | DOUBLE |  | FK→ | The personnel who performed the action.; |
| 3 | `ACTIVE_IND` | DOUBLE |  |  | The table row is active or inactive. A row is generally active unless it is in an inactive state such as logically deleted, combined away, pending purge, etc. |
| 4 | `ACTIVE_STATUS_CD` | DOUBLE |  |  | Indicates the status of the row itself (not the data in the row) such as active, inactive, combined away, pending purge, etc. |
| 5 | `ACTIVE_STATUS_DT_TM` | DATETIME |  |  | The date and time that the active_status_cd was set. |
| 6 | `ACTIVE_STATUS_PRSNL_ID` | DOUBLE |  | FK→ | The person who caused the active_status_cd to be set or change. |
| 7 | `CLIENT_IDENT` | VARCHAR(80) |  |  | The client identifier that represents the client who wrote the data to the system. |
| 8 | `CORRELATION_IDENT` | VARCHAR(80) |  |  | Uppercase, hyphenated GUID that identifies the transaction that updated this row. |
| 9 | `DATA_STATUS_CD` | DOUBLE |  |  | The level of authenticity of the row data. |
| 10 | `EFFECTIVE_DT_TM` | DATETIME |  |  | The clinicaly significant date time of this lab result. |
| 11 | `ENCNTR_ID` | DOUBLE |  | FK→ | The encounter related to the external data. |
| 12 | `EVENT_ID` | DOUBLE |  |  | The id of the clinical event associated to this lab result. |
| 13 | `ISSUE_DT_TM` | DATETIME |  |  | The date and time this external data was added to the staging tables. |
| 14 | `LOGICAL_DOMAIN_ID` | DOUBLE |  | FK→ | The unique identifier for a logical domain. This identifier allows the data to be grouped by logical domain. For example, If you assign clients a logical_domain_id this would allow you to store data for multiple clients on this table. |
| 15 | `MIC_EXT_BLOB` | LONGBLOB |  |  | The dta that has come from an external interface. |
| 16 | `MIC_EXT_DATA_ID` | DOUBLE | NOT NULL | PK | A system generated number to uniquely identify a row on the MIC_EXT_DATA table. |
| 17 | `PARENT_EXT_DATA_ID` | DOUBLE |  | FK→ | This unique identifier is used to indicate the parent external data that groups this external data row is related to. |
| 18 | `PERSON_ID` | DOUBLE |  | FK→ | Ther person related to the external data. |
| 19 | `REQUESTED_ACTION_CD` | DOUBLE |  |  | Actoin requested for the data. |
| 20 | `UPDT_APPLCTX` | DOUBLE |  |  | The application context number from the record info block. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 21 | `UPDT_CNT` | DOUBLE |  |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 22 | `UPDT_DT_TM` | DATETIME |  |  | The date and time the row was last inserted or updated. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 23 | `UPDT_ID` | DOUBLE |  |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 24 | `UPDT_TASK` | DOUBLE |  |  | The registered (assigned) task number for the process that inserted or updated the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `ACTION_PRSNL_ID` | [PRSNL](PRSNL.md) | `PERSON_ID` |
| `ACTIVE_STATUS_PRSNL_ID` | [PRSNL](PRSNL.md) | `PERSON_ID` |
| `ENCNTR_ID` | [ENCOUNTER](ENCOUNTER.md) | `ENCNTR_ID` |
| `LOGICAL_DOMAIN_ID` | [LOGICAL_DOMAIN](LOGICAL_DOMAIN.md) | `LOGICAL_DOMAIN_ID` |
| `PARENT_EXT_DATA_ID` | [MIC_EXT_DATA](MIC_EXT_DATA.md) | `MIC_EXT_DATA_ID` |
| `PERSON_ID` | [PERSON](PERSON.md) | `PERSON_ID` |

## Referenced by (2)

| From table | Column |
|------------|--------|
| [LAB_EXT_IDENTIFIER](LAB_EXT_IDENTIFIER.md) | `MIC_EXT_DATA_ID` |
| [MIC_EXT_DATA](MIC_EXT_DATA.md) | `PARENT_EXT_DATA_ID` |

