# LH_EH_QRDA_ISSUE

> Stores possible errors within the Eligible Hospital Quality Reporting Data Architecture

**Description:** LH_EH_QRDA_ISSUE  
**Table type:** ACTIVITY  
**Primary key:** _(not published — see note)_  
**Columns:** 34

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `CODE_TXT` | VARCHAR(50) |  |  | The qualifying code for the record. |
| 2 | `CONDITION_MASK` | DOUBLE |  |  | A bitmask that identifies what conditions are associated to the record. The conditions correspond to the following numbers: AMI - 1, CAC - 2, ED - 4, EHDI - 8, PC - 16, STK - 32, VTE - 64 |
| 3 | `DISCHARGE_DT_TM` | DATETIME |  |  | The date/time on which the patient was discharged. |
| 4 | `D_ADMIT_NURSE_UNIT_ID` | DOUBLE | NOT NULL | FK→ | The nurse unit to which the patient was admitted. |
| 5 | `D_BR_CCN_ID` | DOUBLE | NOT NULL | FK→ | The CMS Certification Number. |
| 6 | `D_BR_HCO_ID` | DOUBLE | NOT NULL | FK→ | The Healthcare organization Number. |
| 7 | `D_BUILDING_ID` | DOUBLE | NOT NULL | FK→ | The building from which the patient was discharged |
| 8 | `D_DISCHARGE_NURSE_UNIT_ID` | DOUBLE | NOT NULL | FK→ | The nurse unit from which the patient was discharged |
| 9 | `D_FACILITY_ID` | DOUBLE | NOT NULL | FK→ | The facility from which the patient was discharged |
| 10 | `D_PERSON_ID` | DOUBLE | NOT NULL | FK→ | The person that qualified for the quality metric. |
| 11 | `ENCNTR_ID` | DOUBLE | NOT NULL |  | The primary key of the ENCOUNTER table for the encounter associated to the record. |
| 12 | `EXTRACT_DT_TM` | DATETIME |  |  | The date/time that the record was extracted from the source system. |
| 13 | `FINANCIAL_NBR_TXT` | VARCHAR(50) |  |  | The financial number alias associated to the encounter. |
| 14 | `FIRST_PROCESS_DT_TM` | DATETIME |  |  | The date/time that the first ETL process started that created this record. |
| 15 | `HEALTH_SYSTEM_ID` | DOUBLE | NOT NULL |  | Identifier of the health system to which the record belongs. |
| 16 | `HEALTH_SYSTEM_SOURCE_ID` | DOUBLE | NOT NULL | FK→ | Identifier of the health system source to which the record belongs. |
| 17 | `ISSUE_FLAG` | DOUBLE |  |  | Identifies the type of issue. - 1= Patient MRN is missing 2= ED start date is null 3= Entry end is less than start 4= Encounter end equals start 5= Ambiguous documentation date. |
| 18 | `LAST_PROCESS_DT_TM` | DATETIME |  |  | The date/time that the last ETL process started that updated this record. |
| 19 | `LH_EH_QRDA_ISSUE_ID` | DOUBLE | NOT NULL |  | PRIMARY KEY |
| 20 | `LOGICAL_DOMAIN_ID` | DOUBLE | NOT NULL |  | The unique identifier for a logical domain. This identifier allows the data to be grouped by logical domain. For example, If you assign clients a logical_domain_id this would allow you to store data for multiple clients on this table. |
| 21 | `ORG_MRN_TXT` | VARCHAR(50) |  |  | Identifies the medical record number of the patient. |
| 22 | `PARENT_ENTITY_ID` | DOUBLE | NOT NULL |  | The primary key of the table in Millennium from which the record was retrieved. |
| 23 | `PARENT_ENTITY_NAME` | VARCHAR(30) |  |  | The name of the table in Millennium from which the record was retrieved. |
| 24 | `PATIENT_IDENT` | VARCHAR(50) |  |  | The financial number alias associated to the person |
| 25 | `QRDA_VERSION` | DOUBLE | NOT NULL |  | Identifies the version of the QRDA program that was used to insert/update the record. VERSION = VERSION YEAR + (QRDA VERSION / 100) |
| 26 | `SECOND_ENCNTR_ID` | DOUBLE |  |  | The primary key of the ENCOUNTER table for the second encounter associated to the record, for situations where an encounter has potential submission issues because of shared or overlapping data with another encounter. |
| 27 | `SECOND_FINANCIAL_NBR_TXT` | VARCHAR(50) |  |  | The financial number alias associated to the second encounter, for situations where an encounter has potential submission issues because of shared or overlapping data with another encounter. |
| 28 | `SRC_UPDT_DT_TM` | DATETIME |  |  | Indicates the actual time when the row was inserted or updated at the source |
| 29 | `SRC_UPDT_SOURCE` | VARCHAR(50) |  |  | This column is updated with the name of the source program that loaded these rows into this table in Quality Clearinghouse when the Power Insight extracts were executed |
| 30 | `UPDT_CNT` | DOUBLE |  |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 31 | `UPDT_DT_TM` | DATETIME |  |  | The date and time the row was last inserted or updated. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 32 | `UPDT_SOURCE` | VARCHAR(50) |  |  | The name of the program that updated the record last. |
| 33 | `UPDT_TASK` | VARCHAR(50) |  |  | The registered (assigned) task number for the process that inserted or updated the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 34 | `VALUE_SET` | VARCHAR(255) |  |  | The value set name for the record. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `D_ADMIT_NURSE_UNIT_ID` | [LH_D_NURSE_UNIT](LH_D_NURSE_UNIT.md) | `D_NURSE_UNIT_ID` |
| `D_BR_CCN_ID` | [LH_D_BR_CCN](LH_D_BR_CCN.md) | `D_BR_CCN_ID` |
| `D_BR_HCO_ID` | [LH_D_BR_HCO](LH_D_BR_HCO.md) | `D_BR_HCO_ID` |
| `D_BUILDING_ID` | [LH_D_BUILDING](LH_D_BUILDING.md) | `D_BUILDING_ID` |
| `D_DISCHARGE_NURSE_UNIT_ID` | [LH_D_NURSE_UNIT](LH_D_NURSE_UNIT.md) | `D_NURSE_UNIT_ID` |
| `D_FACILITY_ID` | [LH_D_FACILITY](LH_D_FACILITY.md) | `D_FACILITY_ID` |
| `D_PERSON_ID` | [LH_D_PERSON](LH_D_PERSON.md) | `D_PERSON_ID` |
| `HEALTH_SYSTEM_SOURCE_ID` | [LH_D_BR_CCN](LH_D_BR_CCN.md) | `HEALTH_SYSTEM_SOURCE_ID` |
| `HEALTH_SYSTEM_SOURCE_ID` | [LH_D_BR_HCO](LH_D_BR_HCO.md) | `HEALTH_SYSTEM_SOURCE_ID` |
| `HEALTH_SYSTEM_SOURCE_ID` | [LH_D_BUILDING](LH_D_BUILDING.md) | `HEALTH_SYSTEM_SOURCE_ID` |
| `HEALTH_SYSTEM_SOURCE_ID` | [LH_D_FACILITY](LH_D_FACILITY.md) | `HEALTH_SYSTEM_SOURCE_ID` |
| `HEALTH_SYSTEM_SOURCE_ID` | [LH_D_NURSE_UNIT](LH_D_NURSE_UNIT.md) | `HEALTH_SYSTEM_SOURCE_ID` |
| `HEALTH_SYSTEM_SOURCE_ID` | [LH_D_NURSE_UNIT](LH_D_NURSE_UNIT.md) | `HEALTH_SYSTEM_SOURCE_ID` |
| `HEALTH_SYSTEM_SOURCE_ID` | [LH_D_PERSON](LH_D_PERSON.md) | `HEALTH_SYSTEM_SOURCE_ID` |

