# ALLERGY_EXT_DATA

> To temporarily hold untrested data that has come from an external source (e.g. FHIR)

**Description:** External staging table for Allergy concept  
**Table type:** ACTIVITY  
**Primary key:** `ALLERGY_EXT_DATA_ID`  
**Columns:** 28  
**Referenced by:** 1 columns

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ACTION_DT_TM` | DATETIME |  |  | The date and time of the action. |
| 2 | `ACTION_PRSNL_ID` | DOUBLE | NOT NULL | FK→ | The personnel who performed the action. |
| 3 | `ACTION_STATUS_CD` | DOUBLE | NOT NULL |  | Action status indicates a level of authenticity of the row data. Typically this will either be AUTHENTICATED or UNAUTHENTICATED. |
| 4 | `ACTIVE_IND` | DOUBLE | NOT NULL |  | The table row is active or inactive. A row is generally active unless it is in an inactive state such as logically deleted, combined away, pending purge, etc. |
| 5 | `ACTIVE_STATUS_CD` | DOUBLE | NOT NULL |  | Indicates the status of the row itself (not the data in the row) such as active, inactive, combined away, pending purge, etc. |
| 6 | `ACTIVE_STATUS_DT_TM` | DATETIME | NOT NULL |  | The date and time that the active_status_cd was set. |
| 7 | `ACTIVE_STATUS_PRSNL_ID` | DOUBLE | NOT NULL |  | The person who caused the active_status_cd to be set or change. |
| 8 | `ALLERGY_EXT_BLOB` | LONGBLOB |  |  | The data that has come from an external interface. |
| 9 | `ALLERGY_EXT_DATA_ID` | DOUBLE | NOT NULL | PK | PRIMARY KEY |
| 10 | `ALLERGY_ID` | DOUBLE | NOT NULL |  | This value comes from the ALLERGY_ID field on the ALLERGY table and not from the PK for ALLERGY. |
| 11 | `CLIENT_IDENT` | VARCHAR(255) |  |  | The client identifier that represents the client who wrote the data to the system. |
| 12 | `CMB_ALLERGY_EXT_DATA_ID` | DOUBLE | NOT NULL | FK→ | Field to store the combined from ALLERGY_EXT_DATA_ID. This will be useful for tracking back to the combined row of staged allergy. |
| 13 | `CMB_DT_TM` | DATETIME |  |  | Filed to store the date/time when the combine occurred. |
| 14 | `CMB_PERSON_ID` | DOUBLE | NOT NULL | FK→ | Field to store the combined from PERSON_ID. This will be useful for tracking back to the combined person_id of staged allergy. |
| 15 | `CMB_PRSNL_ID` | DOUBLE | NOT NULL | FK→ | Field to store the person who performed combine |
| 16 | `DATA_LOB_ENCODING_STR` | VARCHAR(10) |  |  | The encoding of the ALLERGY_EXT_BLOB column. |
| 17 | `ENCNTR_ID` | DOUBLE | NOT NULL | FK→ | This value comes from the ENCNTR_ID on the ENCOUNTER table |
| 18 | `EXT_BLOB_VERSION` | DOUBLE |  |  | The version of the external data |
| 19 | `NOMENCLATURE_FT` | VARCHAR(255) |  |  | FREE TEXT FOR THE NOMENCLATURE |
| 20 | `NOMENCLATURE_ID` | DOUBLE | NOT NULL | FK→ | Identifier of the row referenced in the NOMENCLATURE table |
| 21 | `PERSON_ID` | DOUBLE | NOT NULL | FK→ | The PERSON related to the external data |
| 22 | `REQUESTED_ACTION_CD` | DOUBLE | NOT NULL |  | Action requested for the data |
| 23 | `SUBMITTED_DT_TM` | DATETIME |  |  | The date and time this external data was added to the staging tables. |
| 24 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 25 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 26 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 27 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 28 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `ACTION_PRSNL_ID` | [PRSNL](PRSNL.md) | `PERSON_ID` |
| `CMB_ALLERGY_EXT_DATA_ID` | [ALLERGY_EXT_DATA](ALLERGY_EXT_DATA.md) | `ALLERGY_EXT_DATA_ID` |
| `CMB_PERSON_ID` | [PERSON](PERSON.md) | `PERSON_ID` |
| `CMB_PRSNL_ID` | [PRSNL](PRSNL.md) | `PERSON_ID` |
| `ENCNTR_ID` | [ENCOUNTER](ENCOUNTER.md) | `ENCNTR_ID` |
| `NOMENCLATURE_ID` | [NOMENCLATURE](NOMENCLATURE.md) | `NOMENCLATURE_ID` |
| `PERSON_ID` | [PERSON](PERSON.md) | `PERSON_ID` |

## Referenced by (1)

| From table | Column |
|------------|--------|
| [ALLERGY_EXT_DATA](ALLERGY_EXT_DATA.md) | `CMB_ALLERGY_EXT_DATA_ID` |

