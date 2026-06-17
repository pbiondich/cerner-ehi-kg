# LH_ABS_HBIPS_PATIENTS

> Holds relation information between an encounter/person and an HBIPS event

**Description:** LH_ABS_HBIPS_PATIENTS  
**Table type:** ACTIVITY  
**Primary key:** _(not published — see note)_  
**Columns:** 24

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ARRIVE_DT_TM` | DATETIME |  |  | When the patient arrived to the pysch location |
| 2 | `ARRIVE_UTC_DT_TM` | DATETIME |  |  | When the patient arrived to the pysch location |
| 3 | `DEPART_DT_TM` | DATETIME |  |  | When the patient departed from the pysch location |
| 4 | `DEPART_UTC_DT_TM` | DATETIME |  |  | When the patient departed from the pysch location |
| 5 | `D_BR_CCN_ID` | DOUBLE | NOT NULL | FK→ | CMS Certification Number |
| 6 | `D_BR_HCO_ID` | DOUBLE | NOT NULL | FK→ | Healthcare Organization Number |
| 7 | `D_BUILDING_ID` | DOUBLE | NOT NULL | FK→ | The building to which the patient was admitted |
| 8 | `D_FACILITY_ID` | DOUBLE | NOT NULL | FK→ | The facility to which the patient was admitted |
| 9 | `D_NURSE_UNIT_ID` | DOUBLE | NOT NULL | FK→ | The nurse unit to which the patient was admitted |
| 10 | `D_PERSON_ID` | DOUBLE | NOT NULL | FK→ | The person that qualifies for the quality metric |
| 11 | `ENCNTR_ID` | DOUBLE | NOT NULL |  | Identifies the encounter for the qualify measure |
| 12 | `EXTRACT_DT_TM` | DATETIME |  |  | The date/time that the record was extracted from the source system. |
| 13 | `FIRST_PROCESS_DT_TM` | DATETIME |  |  | The date/time that the first ETL process started that created this record. |
| 14 | `HEALTH_SYSTEM_ID` | DOUBLE | NOT NULL |  | Identifies the delivery network responsible for supplying the data. |
| 15 | `HEALTH_SYSTEM_SOURCE_ID` | DOUBLE | NOT NULL | FK→ | Identifies the unique source within the delivery network responsible for supplying the data. |
| 16 | `LAST_PROCESS_DT_TM` | DATETIME |  |  | The date/time that the last ETL process started that updated this record. |
| 17 | `LEAVE_IND` | DOUBLE | NOT NULL |  | Indicator used to determine if the table row is psych day row or psych leave row. 0 - psych day row, 1 - psych leave row. |
| 18 | `LH_ABS_HBIPS_PATIENTS_ID` | DOUBLE | NOT NULL |  | Unique generated number that identifies a single row on the LH_ABS_HBIPS_PATIENTS table. |
| 19 | `PAYMENT_SOURCE_FLAG` | DOUBLE | NOT NULL |  | Identifies if the patient has a medicare payment source. |
| 20 | `STRATUM_TITLE` | VARCHAR(50) |  |  | The stratum title of the condition. |
| 21 | `UPDT_CNT` | DOUBLE |  |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 22 | `UPDT_DT_TM` | DATETIME |  |  | The date and time the row was last inserted or updated. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 23 | `UPDT_SOURCE` | VARCHAR(50) |  |  | The script name responsible for updating the record. |
| 24 | `UPDT_TASK` | VARCHAR(50) |  |  | The registered (assigned) task number for the process that inserted or updated the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `D_BR_CCN_ID` | [LH_D_BR_CCN](LH_D_BR_CCN.md) | `D_BR_CCN_ID` |
| `D_BR_HCO_ID` | [LH_D_BR_HCO](LH_D_BR_HCO.md) | `D_BR_HCO_ID` |
| `D_BUILDING_ID` | [LH_D_BUILDING](LH_D_BUILDING.md) | `D_BUILDING_ID` |
| `D_FACILITY_ID` | [LH_D_FACILITY](LH_D_FACILITY.md) | `D_FACILITY_ID` |
| `D_NURSE_UNIT_ID` | [LH_D_NURSE_UNIT](LH_D_NURSE_UNIT.md) | `D_NURSE_UNIT_ID` |
| `D_PERSON_ID` | [LH_D_PERSON](LH_D_PERSON.md) | `D_PERSON_ID` |
| `HEALTH_SYSTEM_SOURCE_ID` | [LH_D_BR_CCN](LH_D_BR_CCN.md) | `HEALTH_SYSTEM_SOURCE_ID` |
| `HEALTH_SYSTEM_SOURCE_ID` | [LH_D_BR_HCO](LH_D_BR_HCO.md) | `HEALTH_SYSTEM_SOURCE_ID` |
| `HEALTH_SYSTEM_SOURCE_ID` | [LH_D_BUILDING](LH_D_BUILDING.md) | `HEALTH_SYSTEM_SOURCE_ID` |
| `HEALTH_SYSTEM_SOURCE_ID` | [LH_D_FACILITY](LH_D_FACILITY.md) | `HEALTH_SYSTEM_SOURCE_ID` |
| `HEALTH_SYSTEM_SOURCE_ID` | [LH_D_NURSE_UNIT](LH_D_NURSE_UNIT.md) | `HEALTH_SYSTEM_SOURCE_ID` |
| `HEALTH_SYSTEM_SOURCE_ID` | [LH_D_PERSON](LH_D_PERSON.md) | `HEALTH_SYSTEM_SOURCE_ID` |

