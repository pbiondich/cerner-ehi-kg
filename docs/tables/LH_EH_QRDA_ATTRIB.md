# LH_EH_QRDA_ATTRIB

> Stores attributes to the LH_EH_QRDA data for Eligible Hospital Quality Reporting Data Architecture.

**Description:** LH_EH_QRDA_ATTRIB  
**Table type:** ACTIVITY  
**Primary key:** _(not published — see note)_  
**Columns:** 40

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `CODE_DISPLAY` | VARCHAR(300) |  |  | The human readable display of the code. |
| 2 | `CODE_SYSTEM` | VARCHAR(40) |  |  | The OID of the coding system to which the code belongs. |
| 3 | `CODE_SYSTEM_NAME` | VARCHAR(12) |  |  | The name of the coding system to which the code belongs. |
| 4 | `CODE_SYSTEM_SDTC` | VARCHAR(100) |  |  | The OID of the value set to which the code belongs. |
| 5 | `CODE_TXT` | VARCHAR(50) |  |  | The qualifying code for the record. |
| 6 | `COMP_CODE` | VARCHAR(50) |  |  | The component code for an encounter attribute(Example: POA-Present On Admission component for a diagnosis). |
| 7 | `COMP_DISPLAY` | VARCHAR(300) |  |  | The component display name for an encounter attribute(Example: POA-Present On Admission component for a diagnosis). |
| 8 | `CONDITION_MASK` | DOUBLE |  |  | A bitmask that identifies what conditions are associated to the record. The conditions correspond to the following numbers: AMI - 1, CAC - 2, ED - 4, EHDI - 8, PC - 16, STK - 32, VTE - 64 |
| 9 | `EFFECTIVE_HIGH_DT_TM` | DATETIME |  |  | The high (end) date/time assocaited to the record. |
| 10 | `EFFECTIVE_HIGH_UTC_OFFSET` | VARCHAR(5) |  |  | Stores the UTC offset for the effective_high_dt_tm (e.g. -0500). |
| 11 | `EFFECTIVE_LOW_DT_TM` | DATETIME |  |  | The low (start) date/time associated to the record. |
| 12 | `EFFECTIVE_LOW_UTC_OFFSET` | VARCHAR(5) |  |  | Stores the UTC offset for the effective_low_dt_tm (e.g. -0500). |
| 13 | `ENCNTR_ID` | DOUBLE | NOT NULL |  | Unique generated number that identifies a single row on the ENCOUNTER table. |
| 14 | `EXTRACT_DT_TM` | DATETIME |  |  | The start date/time of the program that collected the record last. |
| 15 | `FIRST_PROCESS_DT_TM` | DATETIME |  |  | The date/time that the first ETL process started that created this record. |
| 16 | `HEALTH_SYSTEM_ID` | DOUBLE | NOT NULL |  | Identifier of the health system to which the record belongs. |
| 17 | `HEALTH_SYSTEM_SOURCE_ID` | DOUBLE | NOT NULL |  | Identifier of the health system source to which the record belongs. |
| 18 | `HL7_TEMPLATE` | VARCHAR(50) |  |  | The HL7 template for the record. |
| 19 | `LAST_PROCESS_DT_TM` | DATETIME |  |  | The date/time that the last ETL process started that updated this record. |
| 20 | `LH_EH_QRDA_ATTRIB_ID` | DOUBLE | NOT NULL |  | Unique generated number that identifies a single row on the LH_EH_QRDA_ATTRIB table. |
| 21 | `LH_EH_QRDA_ID` | DOUBLE | NOT NULL |  | Unique generated number that identifies a single row on the LH_EH_QRDA table. |
| 22 | `LOGICAL_CONDITION_MASK` | DOUBLE |  |  | A bitmask that identifies which conditions the data should be submitted for. Possible values are: AMI - 1, CAC - 2, ED - 4, EHDI - 8, PC - 16, STK - 32, VTE - 64, HWR - 128, PCB - 256, PCM - 512, Opioid - 1024, Hybrid - 2048, HH - 4096, STEMI - 8192, GMCS - 16384, ORAE - 32768 |
| 23 | `LOGICAL_DOMAIN_ID` | DOUBLE | NOT NULL |  | The unique identifier for a logical domain. This identifier allows the data to be grouped by logical domain. For example, If you assign clients a logical_domain_id this would allow you to store data for multiple clients on this table. |
| 24 | `PARENT_ENTITY_ID` | DOUBLE | NOT NULL |  | Unique generated number that identifies a single row on the table identified in PARENT_ENTITY_NAME. |
| 25 | `PARENT_ENTITY_NAME` | VARCHAR(30) |  |  | The name of the table in Millennium from which the record was retrieved. |
| 26 | `PARTITION_DT_TM` | DATETIME |  |  | The date/time corresponding to the qualifying encounters relation to a measurement period. |
| 27 | `PERSON_ID` | DOUBLE | NOT NULL |  | Unique generated number that identifies a single row on the PERSON table. |
| 28 | `QRDA_VERSION` | DOUBLE | NOT NULL |  | Identifies the version of the QRDA program that was used to insert/update the record.VERSION = VERSION YEAR + (QRDA VERSION / 100) |
| 29 | `RANK_NBR` | DOUBLE |  |  | The rank (or priority) of a diagnosis or procedure. |
| 30 | `RESULT_DT_TM` | DATETIME |  |  | The date/time provided as a result of an assessment. |
| 31 | `RESULT_UNIT` | VARCHAR(40) |  |  | The units of the numeric result value for the record. |
| 32 | `RESULT_UTC_OFFSET` | VARCHAR(5) |  |  | Stores the UTC offset for the result_dt_tm (e.g. -0500) |
| 33 | `RESULT_VALUE` | DOUBLE | NOT NULL |  | The numeric result value for the record. |
| 34 | `SRC_UPDT_DT_TM` | DATETIME |  |  | Indicates the actual time when the row was inserted or updated at the source. This column is used only for date extraction and will not be populated on the client site. |
| 35 | `SRC_UPDT_SOURCE` | VARCHAR(50) |  |  | This column is updated with the name of the source program that loaded these rows into this table in Quality Clearinghouse when the Power Insight extracts were executed. This column is used only for date extraction and will not be populated on the client site. |
| 36 | `UPDT_CNT` | DOUBLE |  |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 37 | `UPDT_DT_TM` | DATETIME |  |  | The date and time the row was last inserted or updated. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 38 | `UPDT_SOURCE` | VARCHAR(50) |  |  | The name of the program that updated the record last. |
| 39 | `UPDT_TASK` | VARCHAR(50) |  |  | The registered (assigned) task number for the process that inserted or updated the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 40 | `VALUE_SET` | VARCHAR(255) |  |  | The value set name for the record. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

