# RAD_STG_DATA

> To temporarily hold untrusted data that has come from an external source (e.g. FHIR).

**Description:** Radiology Staging Data  
**Table type:** ACTIVITY  
**Primary key:** `RAD_STG_DATA_ID`  
**Columns:** 25  
**Referenced by:** 2 columns

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ACTIVE_IND` | DOUBLE |  |  | The table row is active or inactive. A row is generally active unless it is in an inactive state such as logically deleted, combined away, pending purge, etc. |
| 2 | `AUTHORIZING_ORG_ID` | DOUBLE |  | FK→ | Organisation id of the authorizing Organisation. |
| 3 | `CLIENT_IDENT` | VARCHAR(80) |  |  | Represents the client who wrote the data to the system. |
| 4 | `CORRELATION_IDENT` | VARCHAR(80) |  |  | Uppercase, hyphenated GUID that identifies the transaction that updated this row. |
| 5 | `EFFECTIVE_DT_TM` | DATETIME |  |  | The clinicaly significant date time of this document. |
| 6 | `ENCNTR_ID` | DOUBLE |  | FK→ | The encounter related to the external data. |
| 7 | `EVENT_CD` | DOUBLE |  |  | Code value that represents the event code associated for the diagnostic report. |
| 8 | `EVENT_CD_STD_CD_ID` | DOUBLE |  | FK→ | Unique identifier for the event code standard code. |
| 9 | `EVENT_ID` | DOUBLE |  |  | The id of the clinical event associated to this radiology result. |
| 10 | `ISSUED_DT_TM` | DATETIME |  |  | The date and time this external document was reviewed or verified. |
| 11 | `JSON_VRSN_TXT` | VARCHAR(20) |  |  | Stores the version of Json that is used in the CLOB column. |
| 12 | `LOGICAL_DOMAIN_ID` | DOUBLE |  | FK→ | The unique identifier for a logical domain. This identifier allows the data to be grouped by logical domain. For example, If you assign clients a logical_domain_id this would allow you to store data for multiple clients on this table. |
| 13 | `PARENT_RAD_STG_DATA_ID` | DOUBLE |  | FK→ | This unique identifier is used to indicate the parent external data that groups this external data row is related to. |
| 14 | `PERSON_ID` | DOUBLE |  | FK→ | The person related to the external data; |
| 15 | `RAD_EXT_CLOB` | LONGTEXT |  |  | External JSON content |
| 16 | `RAD_STG_DATA_ID` | DOUBLE | NOT NULL | PK | Unique, generated number that identifies a single row on the RAD_STG_DATA table. |
| 17 | `REPORT_STATUS_CD` | DOUBLE |  |  | Code value that represents the status of the diagnostic report. |
| 18 | `REPORT_STATUS_STD_CD_ID` | DOUBLE |  | FK→ | Unique identifier for the report status standard code. |
| 19 | `STG_STATUS_CD` | DOUBLE |  |  | Code value that represents the status of the imported document. |
| 20 | `TRANSMITTING_ORG_ID` | DOUBLE |  | FK→ | Organisation id of the transmitting Organization. |
| 21 | `UPDT_APPLCTX` | DOUBLE |  |  | The application context number from the record info block. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 22 | `UPDT_CNT` | DOUBLE |  |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 23 | `UPDT_DT_TM` | DATETIME |  |  | The date and time the row was last inserted or updated. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 24 | `UPDT_ID` | DOUBLE |  |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 25 | `UPDT_TASK` | DOUBLE |  |  | The registered (assigned) task number for the process that inserted or updated the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `AUTHORIZING_ORG_ID` | [ORGANIZATION](ORGANIZATION.md) | `ORGANIZATION_ID` |
| `ENCNTR_ID` | [ENCOUNTER](ENCOUNTER.md) | `ENCNTR_ID` |
| `EVENT_CD_STD_CD_ID` | [RAD_STG_STANDARD_CODE](RAD_STG_STANDARD_CODE.md) | `RAD_STG_STANDARD_CODE_ID` |
| `LOGICAL_DOMAIN_ID` | [LOGICAL_DOMAIN](LOGICAL_DOMAIN.md) | `LOGICAL_DOMAIN_ID` |
| `PARENT_RAD_STG_DATA_ID` | [RAD_STG_DATA](RAD_STG_DATA.md) | `RAD_STG_DATA_ID` |
| `PERSON_ID` | [PERSON](PERSON.md) | `PERSON_ID` |
| `REPORT_STATUS_STD_CD_ID` | [RAD_STG_STANDARD_CODE](RAD_STG_STANDARD_CODE.md) | `RAD_STG_STANDARD_CODE_ID` |
| `TRANSMITTING_ORG_ID` | [ORGANIZATION](ORGANIZATION.md) | `ORGANIZATION_ID` |

## Referenced by (2)

| From table | Column |
|------------|--------|
| [RAD_STG_DATA](RAD_STG_DATA.md) | `PARENT_RAD_STG_DATA_ID` |
| [RAD_STG_EXT_IDENTIFIER](RAD_STG_EXT_IDENTIFIER.md) | `RAD_STG_DATA_ID` |

