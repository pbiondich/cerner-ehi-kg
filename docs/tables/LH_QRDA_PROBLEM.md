# LH_QRDA_PROBLEM

> This table is used to store elements that are used to create the Problem Section in the body of a QRDA file for submission

**Description:** LH_QRDA_PROBLEM  
**Table type:** ACTIVITY  
**Primary key:** _(not published — see note)_  
**Columns:** 41

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ACTIVE_IND` | DOUBLE | NOT NULL |  | The table row is active or inactive. A row is generally active unless it is in an inactive state such as logically deleted, combined away, pending purge, etc. |
| 2 | `EVENT_END_DT_TM` | DATETIME |  |  | This field is to specify the end date time of the event either Diagnosis or Problem |
| 3 | `EVENT_END_OFFSET_UTC` | VARCHAR(6) |  |  | EVENT_END_OFFSET_UTC stores UTC offset for EVENT_END_DT_TM |
| 4 | `EXTRACT_DT_TM` | DATETIME |  |  | The date/time that the record was extracted from the source system. |
| 5 | `FAMILY_MBR_CODE` | VARCHAR(50) |  |  | Family member associated with the patient for family history diagnosis |
| 6 | `FAMILY_MBR_CODE_NAME` | VARCHAR(50) |  |  | Family member associated with the patient for family history diagnosis |
| 7 | `FIRST_PROCESS_DT_TM` | DATETIME |  |  | The date/time that the first ETL process started that created this record. |
| 8 | `HEALTH_SYSTEM_ID` | DOUBLE | NOT NULL |  | Identifies the delivery network responsible for supplying the data. |
| 9 | `HEALTH_SYSTEM_SOURCE_ID` | DOUBLE | NOT NULL |  | Identifies the unique source within the delivery network responsible for supplying the data. |
| 10 | `LAST_PROCESS_DT_TM` | DATETIME |  |  | The date/time that the last ETL process started that updated this record. |
| 11 | `LH_QRDA_PROBLEM_ID` | DOUBLE | NOT NULL |  | Unique generated number that identifies a single row on the LH_QRDA_PROBLEM table. |
| 12 | `LOGICAL_DOMAIN_ID` | DOUBLE | NOT NULL |  | The unique identifier for a logical domain. This identifier allows the data to be grouped by logical domain. For example, If you assign clients a logical_domain_id this would allow you to store data for multiple clients on this table. |
| 13 | `NEGATION_IND` | DOUBLE |  |  | Indicates whether a negation exists or not |
| 14 | `ONSET_DT_TM` | DATETIME |  |  | Indicates the timing of the concern |
| 15 | `ONSET_OFFSET_UTC` | VARCHAR(6) |  |  | ONSET_OFFSET_UTC stores UTC offset for ONSET_DT_TM |
| 16 | `PARENT_ENTITY_ID` | DOUBLE | NOT NULL |  | The value of the primary identifier of the table to which the Problem section is related (i.e. lh_qrda_pqrs_id) |
| 17 | `PARENT_ENTITY_ID2` | DOUBLE | NOT NULL |  | The value of the primary identifier of millennium source table |
| 18 | `PARENT_ENTITY_NAME` | VARCHAR(50) | NOT NULL |  | The name of the table this Problem section is related (i.e. LH_QRDA_PQRS) |
| 19 | `PARENT_ENTITY_NAME2` | VARCHAR(50) | NOT NULL |  | The name of millennium source table |
| 20 | `PRIORITY_LEVEL` | DOUBLE |  |  | Indicates the priority of the diagnosis. |
| 21 | `PROBLEM_INSTANCE_ID` | DOUBLE | NOT NULL |  | Unique identifier for PROBLEM table |
| 22 | `PROBLEM_STATUS_CODE` | VARCHAR(50) |  |  | The code that will be used to represent the @code attribute in value node |
| 23 | `PROBLEM_STATUS_CODE_SYSTEM` | VARCHAR(50) |  |  | The code system from which problem_status_cd was derived from |
| 24 | `PROBLEM_STATUS_DISPLAY` | VARCHAR(500) |  |  | Text representation of the status of a problem |
| 25 | `PROBLEM_STATUS_DT_TM` | DATETIME |  |  | The date and time on which the status of the problem was changed |
| 26 | `PROBLEM_TEMPLATE` | VARCHAR(50) |  |  | The name of the template the problem corresponds to |
| 27 | `PROBLEM_VALUE` | VARCHAR(50) |  |  | The problem value code associated with a problem |
| 28 | `PROBLEM_VALUE_DISPLAY` | VARCHAR(500) |  |  | Text representation of a problem |
| 29 | `PROBLEM_VALUE_DISPLAY_NEG` | VARCHAR(500) |  |  | Text representation of a negation reason of a problem |
| 30 | `PROBLEM_VALUE_NEG` | VARCHAR(50) |  |  | The problem value code associated with a negation reason for a problem |
| 31 | `PROBLEM_VALUE_SYSTEM` | VARCHAR(50) |  |  | The codeSystem from which the problem_value was derived from |
| 32 | `PROBLEM_VALUE_SYSTEM_NAME` | VARCHAR(50) |  |  | Coding system name |
| 33 | `PROBLEM_VALUE_SYSTEM_NAME_NEG` | VARCHAR(50) |  |  | Coding system name of negation reason |
| 34 | `PROBLEM_VALUE_SYSTEM_NEG` | VARCHAR(50) |  |  | The codeSystem from which the negation reason of a problem_value was derived from |
| 35 | `PROBLEM_VALUE_SYSTEM_SDTC` | VARCHAR(50) |  |  | OID of value set |
| 36 | `PROBLEM_VALUE_SYSTEM_SDTC_NEG` | VARCHAR(50) |  |  | OID of value set of negation reason |
| 37 | `REPORTING_YEAR` | DOUBLE |  |  | Stores the reporting year. |
| 38 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 39 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 40 | `UPDT_SOURCE` | VARCHAR(50) | NOT NULL |  | The script name responsible for updating the record. |
| 41 | `UPDT_TASK` | VARCHAR(50) | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

