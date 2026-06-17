# LH_EH_MAP_ISSUE

> Stores possible errors within the Eligible Hospital Quality Reporting Data Architecture

**Description:** LH_EH_MAP_ISSUE  
**Table type:** ACTIVITY  
**Primary key:** _(not published — see note)_  
**Columns:** 20

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ACTIVE_IND` | DOUBLE |  |  | The table row is active or inactive. A row is generally active unless it is in an inactive state such as logically deleted, combined away, pending purge, etc. |
| 2 | `CODE_DESCRIPTION` | VARCHAR(40) |  |  | The description of the mapped code |
| 3 | `CONDITION_MASK` | DOUBLE |  |  | A bitmask that identifies what conditions are associated to the record. The conditions correspond to the following numbers: AMI - 1, CAC - 2, ED - 4, EHDI - 8, PC - 16, STK - 32, VTE - 64 |
| 4 | `EXTRACT_DT_TM` | DATETIME |  |  | The date/time that the record was extracted from the source system. |
| 5 | `FIRST_PROCESS_DT_TM` | DATETIME |  |  | The date/time that the first ETL process started that created this record. |
| 6 | `HEALTH_SYSTEM_ID` | DOUBLE | NOT NULL |  | Identifier of the health system to which the record belongs. |
| 7 | `HEALTH_SYSTEM_SOURCE_ID` | DOUBLE | NOT NULL |  | Identifier of the health system source to which the record belongs. |
| 8 | `ISSUE_FLAG` | DOUBLE |  |  | Identifies the type of issue. 1 Contradicting encounter mappings - 2=Contradicting discharge disposition mapping 3=Contradicting negation mapping 4= Contradicting device mapping. |
| 9 | `LAST_PROCESS_DT_TM` | DATETIME |  |  | The date/time that the last ETL process started that updated this record. |
| 10 | `LH_EH_MAP_ISSUE_ID` | DOUBLE | NOT NULL |  | Unique generated number that identifies a single row on the LH_EH_MAP_ISSUE table. |
| 11 | `LOGICAL_DOMAIN_ID` | DOUBLE | NOT NULL |  | The unique identifier for a logical domain. This identifier allows the data to be grouped by logical domain. For example, If you assign clients a logical_domain_id this would allow you to store data for multiple clients on this table. |
| 12 | `QRDA_VERSION` | DOUBLE | NOT NULL |  | Identifies the version of the QRDA program that was used to insert/update the record. VERSION = VERSION YEAR + (QRDA VERSION / 100) |
| 13 | `SRC_UPDT_DT_TM` | DATETIME |  |  | Indicates the actual time when the row was inserted or updated at the source |
| 14 | `SRC_UPDT_SOURCE` | VARCHAR(50) |  |  | This column is updated with the name of the source program that loaded these rows into this table in Quality Clearinghouse when the Power Insight extracts were executed |
| 15 | `TEMPLATE_NAME` | VARCHAR(50) |  |  | QRDA template to be used for e-submission, not currently in Millennium. |
| 16 | `UPDT_CNT` | DOUBLE |  |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 17 | `UPDT_DT_TM` | DATETIME |  |  | The date and time the row was last inserted or updated. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 18 | `UPDT_SOURCE` | VARCHAR(50) |  |  | This column is updated with the name of the source program that loaded these rows into this table in Quality Clearinghouse when the Power Insight extracts were executed |
| 19 | `UPDT_TASK` | VARCHAR(50) |  |  | The registered (assigned) task number for the process that inserted or updated the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 20 | `VALUE_SETS` | VARCHAR(400) |  |  | A list of value sets affected by this mapping issue. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

