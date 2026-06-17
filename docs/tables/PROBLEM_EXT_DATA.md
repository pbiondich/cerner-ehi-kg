# PROBLEM_EXT_DATA

> To temporarily hold untrusted data that has come from an external source (e.g. FHIR)

**Description:** External staging table for Problems concept  
**Table type:** ACTIVITY  
**Primary key:** _(not published — see note)_  
**Columns:** 27

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ACTION_DT_TM` | DATETIME |  |  | The date and time of the action |
| 2 | `ACTION_PRSNL_ID` | DOUBLE | NOT NULL | FK→ | The personnel who performed the action. |
| 3 | `ACTIVE_IND` | DOUBLE | NOT NULL |  | The table row is active or inactive. A row is generally active unless it is in an inactive state such as logically deleted, combined away, pending purge, etc. |
| 4 | `ACTIVE_STATUS_CD` | DOUBLE | NOT NULL |  | Indicates the status of the row itself (not the data in the row) such as active, inactive, combined away, pending purge, etc. |
| 5 | `ACTIVE_STATUS_DT_TM` | DATETIME | NOT NULL |  | The date and time that the active_status_cd was set. |
| 6 | `ACTIVE_STATUS_PRSNL_ID` | DOUBLE | NOT NULL |  | The person who caused the active_status_cd to be set or change. |
| 7 | `CLIENT_IDENT` | VARCHAR(255) |  |  | The client identifier that represents the client who wrote the data to the system. |
| 8 | `CORRELATION_IDENT` | VARCHAR(80) | NOT NULL |  | Uppercase, hyphenated GUID that identifies the transaction that updated this row. |
| 9 | `DATA_LOB_ENCODING_STR` | VARCHAR(10) | NOT NULL |  | The encoding of the external data |
| 10 | `DATA_STATUS_CD` | DOUBLE | NOT NULL |  | Data status indicates a level of authenticity of the row data. |
| 11 | `ENCNTR_ID` | DOUBLE | NOT NULL | FK→ | The encounter ID associated to the problem external data. |
| 12 | `LIFE_CYCLE_STATUS_CD` | DOUBLE | NOT NULL |  | The encoding of the external data. |
| 13 | `ORIGINATING_NOMENCLATURE_ID` | DOUBLE | NOT NULL | FK→ | The term that was searched by a user to add the condition. |
| 14 | `PERSON_ID` | DOUBLE | NOT NULL | FK→ | The person related to the external data. |
| 15 | `PROBLEM_DISPLAY_KEYCAP` | VARCHAR(255) | NOT NULL |  | This field is used to sort and search by the display of the external problem data. This is character data and is all CAPS. It can contain embedded special characters. |
| 16 | `PROBLEM_EXT_BLOB` | LONGBLOB |  |  | The data that has come from an external interface. |
| 17 | `PROBLEM_EXT_DATA_ID` | DOUBLE | NOT NULL |  | PRIMARY KEY |
| 18 | `PROBLEM_ID` | DOUBLE | NOT NULL | FK→ | ID from the PROBLEM table - the problem being acted on |
| 19 | `REQUESTED_ACTION_CD` | DOUBLE | NOT NULL |  | Action requested for the data. |
| 20 | `SUBMITTED_DT_TM` | DATETIME |  |  | The date and time this external data was added to the staging tables. |
| 21 | `TARGET_NOMENCLATURE_ID` | DOUBLE | NOT NULL | FK→ | The nomenclature id for the target of the condition if it is an ongoing condition. |
| 22 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 23 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 24 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 25 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 26 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 27 | `VERSION_NBR` | DOUBLE |  |  | The version of the external data. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `ACTION_PRSNL_ID` | [PRSNL](PRSNL.md) | `PERSON_ID` |
| `ENCNTR_ID` | [ENCOUNTER](ENCOUNTER.md) | `ENCNTR_ID` |
| `ORIGINATING_NOMENCLATURE_ID` | [NOMENCLATURE](NOMENCLATURE.md) | `NOMENCLATURE_ID` |
| `PERSON_ID` | [PERSON](PERSON.md) | `PERSON_ID` |
| `PROBLEM_ID` | [PROBLEM](PROBLEM.md) | `PROBLEM_INSTANCE_ID` |
| `TARGET_NOMENCLATURE_ID` | [NOMENCLATURE](NOMENCLATURE.md) | `NOMENCLATURE_ID` |

