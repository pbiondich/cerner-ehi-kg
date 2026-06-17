# LH_IMPORT_QRDA

> Stores data from QRDA Category 1 files being imported.

**Description:** LH_IMPORT_QRDA  
**Table type:** ACTIVITY  
**Primary key:** `LH_IMPORT_QRDA_ID`  
**Columns:** 24  
**Referenced by:** 1 columns

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `AUTHOR_DT_TM` | DATETIME |  |  | The Date/Time the documentation was authored. Some examples of documentation may be procedures, med administrations, orders, diagnoses, and lab results, etc. People who might author the documentation may be nurses, doctors, clinicians, and lab techs or anyone authorized. We are getting the date/time from an xml from an external vendor. |
| 2 | `CODE_DISPLAY` | VARCHAR(300) |  |  | The human readable display of the code. |
| 3 | `CODE_SYSTEM` | VARCHAR(40) |  |  | The OID of the coding system the code is in. |
| 4 | `CODE_SYSTEM_NAME` | VARCHAR(40) |  |  | The name of the coding system the code is in. |
| 5 | `CODE_SYSTEM_SDTC` | VARCHAR(100) |  |  | The OID of the value set the code is in. |
| 6 | `CODE_TXT` | VARCHAR(50) |  |  | The qualifying code for the record. |
| 7 | `EC_IND` | DOUBLE | NOT NULL |  | Indicator for whether this measure was imported from an EC QRDA file. |
| 8 | `EFFECTIVE_HIGH_DT_TM` | DATETIME |  |  | The high (end) date time associated to the record |
| 9 | `EFFECTIVE_HIGH_UTC_OFFSET` | VARCHAR(5) |  |  | Contains the UTC offset for the effective_high_dt_tm (e.g. -0500). |
| 10 | `EFFECTIVE_LOW_DT_TM` | DATETIME |  |  | The low (start) date time associated to the record. |
| 11 | `EFFECTIVE_LOW_UTC_OFFSET` | VARCHAR(5) |  |  | Contains the UTC offset for the effective_low_dt_tm (e.g. -0500). |
| 12 | `EH_CONDITION_MASK` | DOUBLE | NOT NULL |  | A bitmask that identifies what conditions are associated to the record. The conditions correspond to the following numbers: AMI - 1, CAC - 2, ED - 4, EHDI - 8, PC - 16, STK - 32, VTE - 64 |
| 13 | `EH_IND` | DOUBLE | NOT NULL |  | Indicator for whether this measure was imported from an EH QRDA file. |
| 14 | `ENCNTR_ID` | DOUBLE | NOT NULL |  | The unique identifier for new encounters being imported onto the table. |
| 15 | `HL7_TEMPLATE` | VARCHAR(50) |  |  | The template defined by HL7 Implementation guide that encapsulates the record. |
| 16 | `LH_IMPORT_QRDA_ID` | DOUBLE | NOT NULL | PK | Unique generated number that identifies a single row on the LH_IMPORT_QRDA table. |
| 17 | `LOGICAL_DOMAIN_ID` | DOUBLE | NOT NULL |  | The unique identifier for a logical domain. This identifier allows the data to be grouped by logical domain. For example, If you assign clients a logical_domain_id this would allow you to store data for multiple clients on this table. |
| 18 | `PERSON_ID` | DOUBLE | NOT NULL |  | The primary key of the PERSON table for the person associated to the record. |
| 19 | `QRDA_IMPORT_VERSION` | VARCHAR(10) |  |  | Identifier for which version of Import was used to insert the record. |
| 20 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 21 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 22 | `UPDT_SOURCE` | VARCHAR(50) | NOT NULL |  | The name of the program that updated the record last. |
| 23 | `UPDT_TASK` | VARCHAR(50) | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 24 | `VALUE_SET` | VARCHAR(255) |  |  | The name of the value set the record corresponds to. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Referenced by (1)

| From table | Column |
|------------|--------|
| [LH_IMPORT_QRDA_ATTRIB](LH_IMPORT_QRDA_ATTRIB.md) | `LH_IMPORT_QRDA_ID` |

