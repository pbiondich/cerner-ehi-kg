# LH_QRDA_PROCEDURE

> This table is used to store elements that are used to create the Procedure Section in the body of a QRDA file for submission

**Description:** LH_QRDA_PROCEDURE  
**Table type:** ACTIVITY  
**Primary key:** _(not published — see note)_  
**Columns:** 41

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ACTIVE_IND` | DOUBLE | NOT NULL |  | The table row is active or inactive. A row is generally active unless it is in an inactive state such as logically deleted, combined away, pending purge, etc. |
| 2 | `EXTRACT_DT_TM` | DATETIME |  |  | The date/time that the record was extracted from the source system. |
| 3 | `FIRST_PROCESS_DT_TM` | DATETIME |  |  | The date/time that the first ETL process started that created this record. |
| 4 | `HEALTH_SYSTEM_ID` | DOUBLE | NOT NULL |  | Identifies the delivery network responsible for supplying the data. |
| 5 | `HEALTH_SYSTEM_SOURCE_ID` | DOUBLE | NOT NULL |  | Identifies the unique source within the delivery network responsible for supplying the data. |
| 6 | `LAST_PROCESS_DT_TM` | DATETIME |  |  | The date/time that the last ETL process started that updated this record. |
| 7 | `LH_QRDA_PROCEDURE_ID` | DOUBLE | NOT NULL |  | Unique generated number that identifies a single row on the LH_QRDA_PROCEDURE table. |
| 8 | `LOGICAL_DOMAIN_ID` | DOUBLE | NOT NULL |  | The unique identifier for a logical domain. This identifier allows the data to be grouped by logical domain. For example, If you assign clients a logical_domain_id this would allow you to store data for multiple clients on this table. |
| 9 | `NEGATION_IND` | DOUBLE |  |  | Indicates whether a negation exists or not |
| 10 | `PARENT_ENTITY_ID` | DOUBLE | NOT NULL |  | The value of the primary identifier of the table to which the Procedure section is related (i.e. lh_qrda_pqrs_id) |
| 11 | `PARENT_ENTITY_ID2` | DOUBLE | NOT NULL |  | The value of the primary identifier of the millennium table to which the Procedure section is related |
| 12 | `PARENT_ENTITY_NAME` | VARCHAR(50) |  |  | The name of the table this Procedure section is related (i.e. LH_QRDA_PQRS) |
| 13 | `PARENT_ENTITY_NAME2` | VARCHAR(50) | NOT NULL |  | The name of the millennium table this Procedure section is related |
| 14 | `PRIORITY_LEVEL` | DOUBLE | NOT NULL |  | Indicates the priority of the procedure. |
| 15 | `PROCEDURE_ID` | DOUBLE | NOT NULL |  | Unique identifier for PROCEDURE table |
| 16 | `PROC_CODE` | VARCHAR(50) |  |  | Represents a given code value (not Cerner's code value) from proc_cd_system |
| 17 | `PROC_CODE_DISPLAY` | VARCHAR(500) |  |  | Text representation of the procedure |
| 18 | `PROC_CODE_DISPLAY_NEG` | VARCHAR(500) |  |  | Text representation of the procedure (negation) |
| 19 | `PROC_CODE_NEG` | VARCHAR(50) |  |  | Represents a given code value (not Cerner's code value) from proc_cd_system (negation) |
| 20 | `PROC_CODE_SYSTEM` | VARCHAR(50) |  |  | Represents the codeSystem string of the code node |
| 21 | `PROC_CODE_SYSTEM_NAME` | VARCHAR(50) |  |  | The name of the procedure's code system (e.g. SNMCT) |
| 22 | `PROC_CODE_SYSTEM_NAME_NEG` | VARCHAR(50) |  |  | The name of the procedure's code system (negation) (e.g. SNMCT) |
| 23 | `PROC_CODE_SYSTEM_NEG` | VARCHAR(50) |  |  | Represents the codeSystem string of the code node (negation) |
| 24 | `PROC_CODE_SYSTEM_SDTC` | VARCHAR(50) |  |  | The OID of the code system's value set |
| 25 | `PROC_CODE_SYSTEM_SDTC_NEG` | VARCHAR(50) |  |  | The OID of the code system's value set (negation) |
| 26 | `PROC_DT_TM` | DATETIME |  |  | The date and time the procedure was performed. |
| 27 | `PROC_END_DT_TM` | DATETIME |  |  | The date/time the record was end date for procedure into the table. |
| 28 | `PROC_END_OFFSET_UTC` | VARCHAR(6) |  |  | PROC_END_OFFSET_UTC stores UTC offset for PROC_END_DT_TM |
| 29 | `PROC_OFFSET_UTC` | VARCHAR(6) |  |  | PROC_OFFSET_UTC stores UTC offset for PROC_DT_TM |
| 30 | `PROC_STATUS_CODE` | VARCHAR(50) |  |  | The status code of the procedure |
| 31 | `PROC_TEMPLATE` | VARCHAR(50) |  |  | The name of the template the procedure corresponds to |
| 32 | `REPORTING_YEAR` | DOUBLE |  |  | Stores the reporting year. |
| 33 | `RESULT_OBS_CODE` | VARCHAR(50) |  |  | Result value set code |
| 34 | `RESULT_OBS_CODE_DISPLAY` | VARCHAR(500) |  |  | Display of value set of result |
| 35 | `RESULT_OBS_CODE_SYSTEM` | VARCHAR(50) |  |  | OID of value set coding system of result |
| 36 | `RESULT_OBS_CODE_SYSTEM_NAME` | VARCHAR(50) |  |  | Value set coding system name of result |
| 37 | `RESULT_OBS_CODE_SYSTEM_SDTC` | VARCHAR(50) |  |  | OID of value set of result |
| 38 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 39 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 40 | `UPDT_SOURCE` | VARCHAR(50) | NOT NULL |  | The script name responsible for updating the record. |
| 41 | `UPDT_TASK` | VARCHAR(50) | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

