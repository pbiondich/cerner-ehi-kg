# GEN_LAB_EXT_DATA

> To temporarily hold untrested data that has come from an external source (e.g. FHIR)

**Description:** Gen Lab External Data  
**Table type:** ACTIVITY  
**Primary key:** `GEN_LAB_EXT_DATA_ID`  
**Columns:** 26  
**Referenced by:** 2 columns

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
| 7 | `CLIENT_IDENT` | VARCHAR(80) |  |  | The identifier of the client who last updated the document. |
| 8 | `CLIN_SIG_DT_TM` | DATETIME |  |  | The clinically significant date and time of this lab result. |
| 9 | `CORRELATION_IDENT` | VARCHAR(80) | NOT NULL |  | Uppercase, hyphenated GUID that identifies the transaction that updated this row. |
| 10 | `DATA_STATUS_CD` | DOUBLE | NOT NULL |  | Data status indicates a level of authenticity of the row data. |
| 11 | `DATA_TYPE_FLAG` | DOUBLE |  |  | Identifies the type of external data. |
| 12 | `ENCNTR_ID` | DOUBLE | NOT NULL | FK→ | The encounter related to the external data. |
| 13 | `EVENT_CD` | DOUBLE |  |  | Identifies the event code for the result, indicating which test the result describes. |
| 14 | `EVENT_ID` | DOUBLE | NOT NULL |  | The id of the clinical event associated to this lab result. |
| 15 | `GEN_LAB_EXT_BLOB` | LONGBLOB |  |  | The data that has come from an external interface. |
| 16 | `GEN_LAB_EXT_DATA_ID` | DOUBLE | NOT NULL | PK | Unique generated number that identifies a single row on the GEN_LAB_EXT_DATA table. |
| 17 | `LOGICAL_DOMAIN_ID` | DOUBLE | NOT NULL | FK→ | The unique identifier for a logical domain. This identifier allows the data to be grouped by logical domain. For example, If you assign clients a logical_domain_id this would allow you to store data for multiple clients on this table. |
| 18 | `PARENT_EXT_DATA_ID` | DOUBLE | NOT NULL | FK→ | This unique identifier is used to indicate the parent external data that groups this external data row is related to. |
| 19 | `PERSON_ID` | DOUBLE | NOT NULL | FK→ | The person related to the external data. |
| 20 | `REQUESTED_ACTION_CD` | DOUBLE | NOT NULL |  | Action requested for the data. |
| 21 | `SUBMITTED_DT_TM` | DATETIME |  |  | The date and time this external data was added to the staging tables. |
| 22 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 23 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 24 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 25 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 26 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `ACTION_PRSNL_ID` | [PRSNL](PRSNL.md) | `PERSON_ID` |
| `ENCNTR_ID` | [ENCOUNTER](ENCOUNTER.md) | `ENCNTR_ID` |
| `LOGICAL_DOMAIN_ID` | [LOGICAL_DOMAIN](LOGICAL_DOMAIN.md) | `LOGICAL_DOMAIN_ID` |
| `PARENT_EXT_DATA_ID` | [GEN_LAB_EXT_DATA](GEN_LAB_EXT_DATA.md) | `GEN_LAB_EXT_DATA_ID` |
| `PERSON_ID` | [PERSON](PERSON.md) | `PERSON_ID` |

## Referenced by (2)

| From table | Column |
|------------|--------|
| [GEN_LAB_EXT_DATA](GEN_LAB_EXT_DATA.md) | `PARENT_EXT_DATA_ID` |
| [LAB_EXT_IDENTIFIER](LAB_EXT_IDENTIFIER.md) | `GEN_LAB_EXT_DATA_ID` |

