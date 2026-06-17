# LH_QRDA_RESULT

> This table is used to store elements that are used to create the Result Section in the body of a QRDA file for submission

**Description:** LH_QRDA_RESULT  
**Table type:** ACTIVITY  
**Primary key:** _(not published — see note)_  
**Columns:** 39

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ACTIVE_IND` | DOUBLE | NOT NULL |  | The table row is active or inactive. A row is generally active unless it is in an inactive state such as logically deleted, combined away, pending purge, etc. |
| 2 | `EFFECTIVE_DT_TM` | DATETIME |  |  | The date and time on which the status of the problem was changed |
| 3 | `EFFECTIVE_OFFSET_UTC` | VARCHAR(6) |  |  | EFFECTIVE_OFFSET_UTC stores UTC offset for EFFECTIVE_DT_TM |
| 4 | `END_EFFECTIVE_DT_TM` | DATETIME |  |  | The date/time after which the row is no longer valid as active current data. This may be valued with the date that the row became inactive. |
| 5 | `END_EFFECTIVE_OFFSET_UTC` | VARCHAR(6) |  |  | END_EFFECTIVE_OFFSET_UTC stores UTC offset for END_EFFECTIVE_DT_TM |
| 6 | `EXTRACT_DT_TM` | DATETIME |  |  | The date/time that the record was extracted from the source system. |
| 7 | `FIRST_PROCESS_DT_TM` | DATETIME |  |  | The date/time that the first ETL process started that created this record. |
| 8 | `HEALTH_SYSTEM_ID` | DOUBLE | NOT NULL |  | Identifies the delivery network responsible for supplying the data. |
| 9 | `HEALTH_SYSTEM_SOURCE_ID` | DOUBLE | NOT NULL |  | Identifies the unique source within the delivery network responsible for supplying the data. |
| 10 | `LAST_PROCESS_DT_TM` | DATETIME |  |  | The date/time that the last ETL process started that updated this record. |
| 11 | `LH_QRDA_RESULT_ID` | DOUBLE | NOT NULL |  | Unique generated number that identifies a single row on the LH_QRDA_RESULT table. |
| 12 | `LOGICAL_DOMAIN_ID` | DOUBLE | NOT NULL |  | The unique identifier for a logical domain. This identifier allows the data to be grouped by logical domain. For example, If you assign clients a logical_domain_id this would allow you to store data for multiple clients on this table. |
| 13 | `NEGATION_IND` | DOUBLE |  |  | Indicates whether a negation exists or not |
| 14 | `OBSERVATION_CODE` | VARCHAR(50) |  |  | Code derived from Appendix_F-Results tab of Downloadable Resources Table |
| 15 | `OBSERVATION_CODE_SYSTEM` | VARCHAR(50) |  |  | The code system from which observation_code was derived from |
| 16 | `OBS_CODE_DISPLAY` | VARCHAR(500) |  |  | Text representation of the result |
| 17 | `OBS_CODE_DISPLAY_NEG` | VARCHAR(500) |  |  | Text representation of the result (negation) |
| 18 | `OBS_CODE_NEG` | VARCHAR(50) |  |  | Represents a given code value (not Cerner's code value) from obs_cd_system (negation) |
| 19 | `OBS_CODE_SYSTEM_NAME` | VARCHAR(50) |  |  | The name of the result's code system (e.g. SNMCT) |
| 20 | `OBS_CODE_SYSTEM_NAME_NEG` | VARCHAR(50) |  |  | The name of the result's code system (negation) (e.g. SNMCT) |
| 21 | `OBS_CODE_SYSTEM_NEG` | VARCHAR(50) |  |  | Represents the codeSystem string of the code node (negation) |
| 22 | `OBS_CODE_SYSTEM_SDTC` | VARCHAR(50) |  |  | The OID of the code system's value set |
| 23 | `OBS_CODE_SYSTEM_SDTC_NEG` | VARCHAR(50) |  |  | The OID of the code system's value set (negation) |
| 24 | `PARENT_ENTITY_ID` | DOUBLE | NOT NULL |  | The value of the primary identifier of the table to which the Result section is related (i.e. lh_qrda_pqrs_id) |
| 25 | `PARENT_ENTITY_ID2` | DOUBLE | NOT NULL |  | The value of the primary identifier of the table to which the Result section is related (i.e. lh_qrda_pqrs_id) |
| 26 | `PARENT_ENTITY_NAME` | VARCHAR(50) |  |  | The name of the table this Result section is related (i.e. LH_QRDA_PQRS) |
| 27 | `PARENT_ENTITY_NAME2` | VARCHAR(50) | NOT NULL |  | The name of the table this Result section is related (i.e. LH_QRDA_PQRS) |
| 28 | `REPORTING_YEAR` | DOUBLE |  |  | Stores the reporting year. |
| 29 | `RESULT_CODE` | VARCHAR(50) |  |  | The code associated with a result |
| 30 | `RESULT_DISPLAY` | VARCHAR(500) |  |  | Text description of the result |
| 31 | `RESULT_ID` | DOUBLE | NOT NULL |  | Unique result id |
| 32 | `RESULT_TEMPLATE` | VARCHAR(50) |  |  | The name of the template the result corresponds to |
| 33 | `RESULT_TYPE` | VARCHAR(50) |  |  | The type of code associated with a given result (e.g. SNOMED CT / CPT-4 / LOINC) |
| 34 | `RESULT_UNIT` | VARCHAR(50) |  |  | Represents the unit (e.g. %) for a result_value |
| 35 | `RESULT_VALUE` | VARCHAR(255) |  |  | Represents the value that is within the range of values for the chosen observation_cd |
| 36 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 37 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 38 | `UPDT_SOURCE` | VARCHAR(50) | NOT NULL |  | The script name responsible for updating the record. |
| 39 | `UPDT_TASK` | VARCHAR(50) | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

