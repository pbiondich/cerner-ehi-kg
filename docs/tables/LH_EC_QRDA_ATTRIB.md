# LH_EC_QRDA_ATTRIB

> This table is used to store elements that are used to create the encounter attribute Section in the body of a QRDA file for submission

**Description:** LH_EC_QRDA_ATTRIB  
**Table type:** ACTIVITY  
**Primary key:** _(not published — see note)_  
**Columns:** 28

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ACTIVE_IND` | DOUBLE |  |  | The table row is active or inactive. A row is generally active unless it is in an inactive state such as logically deleted, combined away, pending purge, etc. |
| 2 | `ATTRIB_CODE` | VARCHAR(50) |  |  | Identifies the value set code for qualifying documentation. |
| 3 | `ATTRIB_CODE_DISPLAY` | VARCHAR(500) |  |  | Identifies the display description of value set code for qualifying documentation. |
| 4 | `ATTRIB_CODE_SYSTEM` | VARCHAR(50) |  |  | Identifies the system of value set code for qualifying documentation. |
| 5 | `ATTRIB_CODE_SYSTEM_NAME` | VARCHAR(50) |  |  | Identifies the system name of value set code for qualifying documentation. |
| 6 | `ATTRIB_CODE_SYSTEM_SDTC` | VARCHAR(50) |  |  | Identifies the sdtc code of value set code for qualifying documentation. |
| 7 | `ATTRIB_TEMPLATE` | VARCHAR(50) |  |  | QRDA tamplate name to identify type of documentation |
| 8 | `EFFECTIVE_DT_TM` | DATETIME |  |  | Identifies the start date and time of dcumentation. |
| 9 | `EFFECTIVE_OFFSET_UTC` | VARCHAR(6) |  |  | EFFECTIVE_OFFSET_UTC stores UTC offset for EFFECTIVE_DT_TM |
| 10 | `END_EFFECTIVE_DT_TM` | DATETIME |  |  | The date/time after which the row is no longer valid as active current data. This may be valued with the date that the row became inactive. |
| 11 | `END_EFFECTIVE_OFFSET_UTC` | VARCHAR(6) |  |  | END_EFFECTIVE_OFFSET_UTC stores UTC offset for END_EFFECTIVE_DT_TM |
| 12 | `EXTRACT_DT_TM` | DATETIME |  |  | The date/time that the program running the extracts was started. |
| 13 | `FIRST_PROCESS_DT_TM` | DATETIME |  |  | The date/time that the first ETL process started that created this record. |
| 14 | `HEALTH_SYSTEM_ID` | DOUBLE | NOT NULL |  | Identifies the delivery network responsible for supplying the data. |
| 15 | `HEALTH_SYSTEM_SOURCE_ID` | DOUBLE | NOT NULL |  | Identifies the unique source within the delivery network responsible for supplying the data. |
| 16 | `LAST_PROCESS_DT_TM` | DATETIME |  |  | The date/time that the last ETL process started that updated this record. |
| 17 | `LH_EC_QRDA_ATTRIB_ID` | DOUBLE | NOT NULL |  | Unique generated number that identifies a single row on the LH_EC_QRDA_ATTRIB table. |
| 18 | `LH_QRDA_TABLE_ID` | DOUBLE | NOT NULL |  | The ID of the event type from lh_qrda_table_name. |
| 19 | `LH_QRDA_TABLE_NAME` | VARCHAR(30) |  |  | The table name of the lh_qrda_table_id source. |
| 20 | `LOGICAL_DOMAIN_ID` | DOUBLE | NOT NULL |  | The unique identifier for a logical domain. This identifier allows the data to be grouped by logical domain. For example, If you assign clients a logical_domain_id this would allow you to store data for multiple clients on this table. |
| 21 | `PARENT_ENTITY_ID` | DOUBLE | NOT NULL |  | The ID of the event type from parent_entity_name. |
| 22 | `PARENT_ENTITY_ID2` | DOUBLE | NOT NULL |  | Identifies the key field of repective millenium table for which this row is qualifying |
| 23 | `PARENT_ENTITY_NAME` | VARCHAR(30) |  |  | The table name of the parent_entity_id source. |
| 24 | `PARENT_ENTITY_NAME2` | VARCHAR(30) |  |  | Identifies the repective millenium table for which this row is qualifying |
| 25 | `UPDT_CNT` | DOUBLE |  |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 26 | `UPDT_DT_TM` | DATETIME |  |  | The date and time the row was last inserted or updated. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 27 | `UPDT_SOURCE` | VARCHAR(50) |  |  | Identifies when a record was updated |
| 28 | `UPDT_TASK` | VARCHAR(50) |  |  | The registered (assigned) task number for the process that inserted or updated the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

