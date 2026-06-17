# VITALS_EXT_DATA

> Staging table to hold untrusted data sent to be written from an external source (eg. FHIR).

**Description:** Vitals External Data  
**Table type:** ACTIVITY  
**Primary key:** `VITALS_EXT_DATA_ID`  
**Columns:** 26  
**Referenced by:** 3 columns

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ACTION_DT_TM` | DATETIME |  |  | The date and time of the action |
| 2 | `ACTION_PRSNL_ID` | DOUBLE | NOT NULL |  | The personnel who performed the action. |
| 3 | `ACTIVE_IND` | DOUBLE | NOT NULL |  | The table row is active or inactive. A row is generally active unless it is in an inactive state such as logically deleted, combined away, pending purge, etc. |
| 4 | `ACTIVE_STATUS_CD` | DOUBLE | NOT NULL |  | Indicates the status of the row itself (not the data in the row) such as active, inactive, combined away, pending purge, etc. |
| 5 | `ACTIVE_STATUS_DT_TM` | DATETIME | NOT NULL |  | The date and time that the active_status_cd was set. |
| 6 | `ACTIVE_STATUS_PRSNL_ID` | DOUBLE | NOT NULL |  | The person who caused the active_status_cd to be set or change. |
| 7 | `BEG_EFFECTIVE_DT_TM` | DATETIME | NOT NULL |  | The date and time for which this table row becomes effective. Normally, this will be the date and time the row is added, but could be a past or future date and time. |
| 8 | `CORRELATION_IDENT` | VARCHAR(80) |  |  | UUID that identifies the transaction that updated this row. |
| 9 | `DATA_STATUS_CD` | DOUBLE | NOT NULL |  | Data status indicates a level of authenticity of the row data. |
| 10 | `ENCNTR_ID` | DOUBLE | NOT NULL | FK→ |  |
| 11 | `END_EFFECTIVE_DT_TM` | DATETIME | NOT NULL |  | The date/time after which the row is no longer valid as active current data. This may be valued with the date that the row became inactive. |
| 12 | `ISSUED_DT_TM` | DATETIME |  |  | The date and time this external data was made available to providers, typically after the results have been reviewed and verified. |
| 13 | `PERSON_ID` | DOUBLE | NOT NULL | FK→ |  |
| 14 | `REQUEST_ACTION_CD` | DOUBLE | NOT NULL |  | Action requested for the data. |
| 15 | `RESULT_IDENT` | VARCHAR(80) |  |  | the identifier of the result that came through FHIR. The identifier could be a clinical_event_id if the request came from another Millennium domain or an identifier from another system. |
| 16 | `SUBMITTED_DT_TM` | DATETIME |  |  | The date and time this external data was added to the staging table. |
| 17 | `TENANT_IDENT` | VARCHAR(80) |  |  | The identifier of the source of this external data. |
| 18 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 19 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 20 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 21 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 22 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 23 | `VERSION_NBR` | DOUBLE |  |  |  |
| 24 | `VITALS_BLOB` | LONGBLOB |  |  | The data that has come from an external source. |
| 25 | `VITALS_EXT_DATA_ID` | DOUBLE | NOT NULL | PK | PRIMARY KEY |
| 26 | `VITALS_STAGE_ID` | DOUBLE | NOT NULL | FK→ |  |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `ENCNTR_ID` | [ENCOUNTER](ENCOUNTER.md) | `ENCNTR_ID` |
| `PERSON_ID` | [PERSON](PERSON.md) | `PERSON_ID` |
| `VITALS_STAGE_ID` | [VITALS_EXT_DATA](VITALS_EXT_DATA.md) | `VITALS_EXT_DATA_ID` |

## Referenced by (3)

| From table | Column |
|------------|--------|
| [VITALS_EXT_DATA](VITALS_EXT_DATA.md) | `VITALS_STAGE_ID` |
| [VITALS_EXT_IDENTIFIER](VITALS_EXT_IDENTIFIER.md) | `VITALS_EXT_DATA_ID` |
| [VITALS_EXT_STANDARD_CODE](VITALS_EXT_STANDARD_CODE.md) | `VITALS_EXT_DATA_ID` |

