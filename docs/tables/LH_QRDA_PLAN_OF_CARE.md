# LH_QRDA_PLAN_OF_CARE

> This table is used to store elements that are used to create the Plan of Care Section in the body of a QRDA file for submission

**Description:** LH_QRDA_PLAN_OF_CARE  
**Table type:** ACTIVITY  
**Primary key:** _(not published — see note)_  
**Columns:** 22

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `EXTRACT_DT_TM` | DATETIME |  |  | The date/time that the record was extracted from the source system. |
| 2 | `FIRST_PROCESS_DT_TM` | DATETIME |  |  | The date/time that the first ETL process started that created this record. |
| 3 | `HEALTH_SYSTEM_ID` | DOUBLE | NOT NULL |  | Identifies the delivery network responsible for supplying the data. |
| 4 | `HEALTH_SYSTEM_SOURCE_ID` | DOUBLE | NOT NULL |  | Identifies the unique source within the delivery network responsible for supplying the data. |
| 5 | `LAST_PROCESS_DT_TM` | DATETIME |  |  | The date/time that the last ETL process started that updated this record. |
| 6 | `LH_QRDA_PLAN_OF_CARE_ID` | DOUBLE | NOT NULL |  | Unique generated number that identifies a single row on the LH_QRDA_PLAN_OF_CARE table. |
| 7 | `LOGICAL_DOMAIN_ID` | DOUBLE | NOT NULL |  | The unique identifier for a logical domain. This identifier allows the data to be grouped by logical domain. For example, If you assign clients a logical_domain_id this would allow you to store data for multiple clients on this table. |
| 8 | `PARENT_ENTITY_ID` | DOUBLE | NOT NULL |  | The value of the primary identifier of the table to which the Plan of Care section is related (i.e. lh_qrda_pqrs_id) |
| 9 | `PARENT_ENTITY_ID2` | DOUBLE | NOT NULL |  | The value of the primary identifier of millennium source table |
| 10 | `PARENT_ENTITY_NAME` | VARCHAR(50) |  |  | The name of the table this Plan of Care section is related (i.e. LH_QRDA_PQRS) |
| 11 | `PARENT_ENTITY_NAME2` | VARCHAR(50) | NOT NULL |  | The name of millennium source table |
| 12 | `POC_CODE` | VARCHAR(50) |  |  | Represents a given code value (not Cerner's code_value) from poc_cd system |
| 13 | `POC_CODE_DISPLAY` | VARCHAR(500) |  |  | Description of Plan Of Care Code |
| 14 | `POC_CODE_SYSTEM` | VARCHAR(50) |  |  | Represents the codeSystem string of the observation/code/@codesystem |
| 15 | `POC_CODE_SYSTEM_NAME` | VARCHAR(100) |  |  | String Representation of Plan Of Care Code OID |
| 16 | `POC_DT_TM` | DATETIME |  |  | The date and time of when the plan of care activity was written |
| 17 | `POC_ID` | DOUBLE | NOT NULL |  | Unique plan of care id |
| 18 | `POC_STATUS_CODE` | VARCHAR(50) |  |  | String representation of the current status of the plan of care |
| 19 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 20 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 21 | `UPDT_SOURCE` | VARCHAR(50) | NOT NULL |  | The script name responsible for updating the record. |
| 22 | `UPDT_TASK` | VARCHAR(50) | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

