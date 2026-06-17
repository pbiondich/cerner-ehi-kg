# PROCEDURE_EXT_DATA

> To temporarily hold untrested data that has come from an external source (e.g. FHIR)

**Description:** External staging table for Procedures concept  
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
| 7 | `CLIENT_IDENT` | VARCHAR(100) |  |  | A string value used to represent a specific client. |
| 8 | `DATA_LOB_ENCODING_STR` | VARCHAR(10) | NOT NULL |  | Used for the encoding of the external data. |
| 9 | `DATA_STATUS_CD` | DOUBLE | NOT NULL |  | Data status indicates a level of authenticity of the row data. |
| 10 | `ENCNTR_ID` | DOUBLE | NOT NULL | FK→ | The encounter related to the external procedure |
| 11 | `NOMENCLATURE_ID` | DOUBLE | NOT NULL | FK→ | The term that was searched by a user to add the condition. |
| 12 | `PERSON_ID` | DOUBLE | NOT NULL | FK→ | The person related to the external data. |
| 13 | `PROCEDURE_DISPLAY` | VARCHAR(255) |  |  | The display value to be used for describing the procedure performed. |
| 14 | `PROCEDURE_EXT_BLOB` | LONGBLOB |  |  | The data that has come from an external interface. |
| 15 | `PROCEDURE_EXT_DATA_ID` | DOUBLE | NOT NULL |  | PRIMARY KEY |
| 16 | `PROCEDURE_ID` | DOUBLE | NOT NULL | FK→ | ID of the procedure row in the PROCEDURE table |
| 17 | `REQUESTED_ACTION_CD` | DOUBLE | NOT NULL |  | Action requested for the data. |
| 18 | `SUBMITTED_DT_TM` | DATETIME |  |  | The date and time this external data was added to the staging tables. |
| 19 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 20 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 21 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 22 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 23 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 24 | `VERSION_NBR` | DOUBLE |  |  | The version of the external data. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `ACTION_PRSNL_ID` | [PRSNL](PRSNL.md) | `PERSON_ID` |
| `ENCNTR_ID` | [ENCOUNTER](ENCOUNTER.md) | `ENCNTR_ID` |
| `NOMENCLATURE_ID` | [NOMENCLATURE](NOMENCLATURE.md) | `NOMENCLATURE_ID` |
| `PERSON_ID` | [PERSON](PERSON.md) | `PERSON_ID` |
| `PROCEDURE_ID` | [PROCEDURE](PROCEDURE.md) | `PROCEDURE_ID` |

