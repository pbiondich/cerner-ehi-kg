# LH_IMPORT_QRDA_ATTRIB

> Stores attribute information for data on the LH_IMPORT_QRDA table.

**Description:** LH_IMPORT_QRDA_ATTRIB  
**Table type:** ACTIVITY  
**Primary key:** _(not published — see note)_  
**Columns:** 28

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `CODE_DISPLAY` | VARCHAR(300) |  |  | The human readable display of the code. |
| 2 | `CODE_SYSTEM` | VARCHAR(40) |  |  | The OID of the coding system the code is in. |
| 3 | `CODE_SYSTEM_NAME` | VARCHAR(40) |  |  | The name of the coding system the code is in. |
| 4 | `CODE_SYSTEM_SDTC` | VARCHAR(100) |  |  | The OID of the value set the code is in. |
| 5 | `CODE_TXT` | VARCHAR(50) |  |  | The qualifying code for the record. |
| 6 | `COMP_CODE` | VARCHAR(50) |  |  | The component code for an encounter attribute(Example: POA-Present On Admission component for a diagnosis). |
| 7 | `COMP_DISPLAY` | VARCHAR(300) |  |  | The component display name for an encounter attribute(Example: POA-Present On Admission component for a diagnosis). |
| 8 | `EFFECTIVE_HIGH_DT_TM` | DATETIME |  |  | The high (end) date time associated to the record |
| 9 | `EFFECTIVE_HIGH_UTC_OFFSET` | VARCHAR(5) |  |  | Contains the UTC offset for the effective_high_dt_tm (e.g. -0500). |
| 10 | `EFFECTIVE_LOW_DT_TM` | DATETIME |  |  | The low (start) date time associated to the record. |
| 11 | `EFFECTIVE_LOW_UTC_OFFSET` | VARCHAR(5) |  |  | Contains the UTC offset for the effective_low_dt_tm (e.g. -0500). |
| 12 | `EH_CONDITION_MASK` | DOUBLE | NOT NULL |  | A bitmask that identifies what conditions are associated to the record. The conditions correspond to the following numbers: AMI - 1, CAC - 2, ED - 4, EHDI - 8, PC - 16, STK - 32, VTE - 64 |
| 13 | `HL7_TEMPLATE` | VARCHAR(50) |  |  | The template defined by HL7 Implementation guide that encapsulates the record. |
| 14 | `LH_IMPORT_QRDA_ATTRIB_ID` | DOUBLE | NOT NULL |  | Unique generated number that identifies a single row on the LH_IMPORT_QRDA_ATTRIB table. |
| 15 | `LH_IMPORT_QRDA_ID` | DOUBLE | NOT NULL | FK→ | Corresponds to the unique key on the LH_IMPORT_QRDA table. |
| 16 | `LOGICAL_DOMAIN_ID` | DOUBLE | NOT NULL |  | The unique identifier for a logical domain. This identifier allows the data to be grouped by logical domain. For example, If you assign clients a logical_domain_id this would allow you to store data for multiple clients on this table. |
| 17 | `PERSON_ID` | DOUBLE | NOT NULL |  | The primary key of the PERSON table for the person associated to the record. |
| 18 | `QRDA_IMPORT_VERSION` | VARCHAR(10) |  |  | Identifier for which version of Import was used to insert the record. |
| 19 | `RESULT_DT_TM` | DATETIME |  |  | DATE and TIME the reut posted |
| 20 | `RESULT_UNIT` | VARCHAR(40) |  |  | The units of the numeric result value for the record. |
| 21 | `RESULT_UTC_OFFSET` | VARCHAR(5) |  |  | Contains the UTC offset for the result_dt_tm (e.g. -0500). |
| 22 | `RESULT_VALUE` | DOUBLE |  |  | The numeric result value for the record. |
| 23 | `TEMPLATE_IDENT` | VARCHAR(300) |  |  | Data from different sources is stored in different formats (templates). A few template names are Procedure Performed template, Encounter Performed template, Assessment Performed templates, and many more. The data from these templates will be stored in the lh_import_qrda* tables. Each of these templates will have its unique identifier. The template_ident column will store this identifier. |
| 24 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 25 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 26 | `UPDT_SOURCE` | VARCHAR(50) | NOT NULL |  | The name of the program that updated the record last. |
| 27 | `UPDT_TASK` | VARCHAR(50) | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 28 | `VALUE_SET` | VARCHAR(255) |  |  | The name of the value set the record corresponds to. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `LH_IMPORT_QRDA_ID` | [LH_IMPORT_QRDA](LH_IMPORT_QRDA.md) | `LH_IMPORT_QRDA_ID` |

