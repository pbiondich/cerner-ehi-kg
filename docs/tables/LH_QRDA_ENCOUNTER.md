# LH_QRDA_ENCOUNTER

> This table is used to store elements that are used to create the Encounter Section in the body of a QRDA file for submission

**Description:** LH_QRDA_ENCOUNTER  
**Table type:** ACTIVITY  
**Primary key:** _(not published — see note)_  
**Columns:** 36

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ACTIVE_IND` | DOUBLE | NOT NULL |  | The table row is active or inactive. A row is generally active unless it is in an inactive state such as logically deleted, combined away, pending purge, etc. |
| 2 | `ENCNTR_CODE_ID` | DOUBLE | NOT NULL |  | Primary key of the encounter table |
| 3 | `ENCNTR_DT_TM` | DATETIME |  |  | The date and time the encounter was registered on |
| 4 | `ENCNTR_END_DT_TM` | DATETIME |  |  | The date and time the encounter was discharged or departed. |
| 5 | `ENCNTR_END_OFFSET_UTC` | VARCHAR(6) |  |  | ENCNTR_END_OFFSET_UTC stores UTC offset for ENCNTR_END_DT_TM |
| 6 | `ENCNTR_OFFSET_UTC` | VARCHAR(6) |  |  | ENCNTR_OFFSET_UTC stores UTC offset for ENCNTR_DT_TM |
| 7 | `ENCNTR_TEMPLATE` | VARCHAR(50) |  |  | The name of the template the encounter corresponds to |
| 8 | `ENCNTR_TYPE_CODE` | VARCHAR(50) |  |  | The code associated with the type of an encounter |
| 9 | `ENCNTR_TYPE_DISPLAY` | VARCHAR(500) |  |  | Text description of the encounter type |
| 10 | `ENC_CODE` | VARCHAR(100) |  |  | The encounter code that will be displayed in the documentation of node. |
| 11 | `ENC_CODE_DISPLAY` | VARCHAR(500) |  |  | Coding system name |
| 12 | `ENC_CODE_DISPLAY_NEG` | VARCHAR(500) |  |  | Text representation of a negation reason of a problem |
| 13 | `ENC_CODE_NEG` | VARCHAR(50) |  |  | The problem value code associated with a negation reason for a problem |
| 14 | `ENC_CODE_SYSTEM` | VARCHAR(100) |  |  | The encounter code system that will be displayed in the documentation of node. |
| 15 | `ENC_CODE_SYSTEM_NAME` | VARCHAR(100) |  |  | The encounter code system name that will be displayed in the documentation of node. |
| 16 | `ENC_CODE_SYSTEM_NAME_NEG` | VARCHAR(50) |  |  | Coding system name of negation reason |
| 17 | `ENC_CODE_SYSTEM_NEG` | VARCHAR(50) |  |  | The codeSystem from which the negation reason of a problem_value was derived from |
| 18 | `ENC_CODE_SYSTEM_SDTC` | VARCHAR(50) |  |  | OID of value set |
| 19 | `ENC_CODE_SYSTEM_SDTC_NEG` | VARCHAR(50) |  |  | OID of value set of negation reason |
| 20 | `EXTRACT_DT_TM` | DATETIME |  |  | The date/time that the record was extracted from the source system. |
| 21 | `FIRST_PROCESS_DT_TM` | DATETIME |  |  | The date/time that the first ETL process started that created this record. |
| 22 | `HEALTH_SYSTEM_ID` | DOUBLE | NOT NULL |  | Identifies the delivery network responsible for supplying the data. |
| 23 | `HEALTH_SYSTEM_SOURCE_ID` | DOUBLE | NOT NULL |  | Identifies the unique source within the delivery network responsible for supplying the data. |
| 24 | `LAST_PROCESS_DT_TM` | DATETIME |  |  | The date/time that the last ETL process started that updated this record. |
| 25 | `LH_QRDA_ENCOUNTER_ID` | DOUBLE | NOT NULL |  | Unique generated number that identifies a single row on the LH_QRDA_ENCOUNTER table. |
| 26 | `LOGICAL_DOMAIN_ID` | DOUBLE | NOT NULL |  | The unique identifier for a logical domain. This identifier allows the data to be grouped by logical domain. For example, If you assign clients a logical_domain_id this would allow you to store data for multiple clients on this table. |
| 27 | `NEGATION_IND` | DOUBLE |  |  | Indicates whether a negation exists or not |
| 28 | `PARENT_ENTITY_ID` | DOUBLE | NOT NULL |  | The value of the primary identifier of the table to which the Plan of Care section is related (i.e. lh_qrda_pqrs_id) |
| 29 | `PARENT_ENTITY_ID2` | DOUBLE | NOT NULL |  | The value of the primary identifier of millennium source table |
| 30 | `PARENT_ENTITY_NAME` | VARCHAR(50) | NOT NULL |  | The name of the table this Plan of Care section is related (i.e. LH_QRDA_PQRS) |
| 31 | `PARENT_ENTITY_NAME2` | VARCHAR(50) | NOT NULL |  | The name of millennium source table |
| 32 | `REPORTING_YEAR` | DOUBLE |  |  | Stores the reporting year. |
| 33 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 34 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 35 | `UPDT_SOURCE` | VARCHAR(50) | NOT NULL |  | The script name responsible for updating the record. |
| 36 | `UPDT_TASK` | VARCHAR(50) | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

