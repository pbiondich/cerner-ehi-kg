# LH_F_IC_ANTIBGRM_METRICS

> This fact table is used to store Infection Control Antibiogram Lighthouse Report.

**Description:** LH_F_IC_ANTIBGRM_METRICS  
**Table type:** ACTIVITY  
**Primary key:** _(not published — see note)_  
**Columns:** 32

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ACTIVE_IND` | DOUBLE |  |  | The table row is active or inactive. A row is generally active unless it is in an inactive state such as logically deleted, combined away, pending purge, etc. |
| 2 | `ADMIT_DT_TM` | DATETIME |  |  | The date/time on which the patient was admitted |
| 3 | `ADMIT_UTC_DT_TM` | DATETIME |  |  | The date/time on which the patient was admitted normalized to GMT. |
| 4 | `COLLECT_DT_TM` | DATETIME |  |  | Date and time of the specimen source collected for the organism |
| 5 | `COLLECT_UTC_DT_TM` | DATETIME |  |  | Date and time of the specimen source collected for the organism; normalized to GMT. |
| 6 | `COMM_MRN_TXT` | VARCHAR(50) |  |  | Identifies the community medical record number of the patient. |
| 7 | `DISCHARGE_DT_TM` | DATETIME |  |  | The date/time on which the patient was discharged. |
| 8 | `DISCHARGE_UTC_DT_TM` | DATETIME |  |  | The date/time on which the patient was discharged normalized to GMT. |
| 9 | `D_COLL_BUILDING_ID` | DOUBLE | NOT NULL | FK→ | Identifies the building of specimen source collected for the organism. |
| 10 | `D_COLL_ENCNTR_TYPE_ID` | DOUBLE | NOT NULL | FK→ | Identifies the encounter type of specimen source collected for the organism. |
| 11 | `D_COLL_FACILITY_ID` | DOUBLE | NOT NULL | FK→ | Identifies the facility of specimen source collected for the organism. |
| 12 | `D_COLL_NURSE_UNIT_ID` | DOUBLE | NOT NULL | FK→ | Identifies the nurse unit of specimen source collected for the organism. |
| 13 | `D_ORGANISM_ID` | DOUBLE | NOT NULL | FK→ | Identifies the reported organism |
| 14 | `D_PERSON_ID` | DOUBLE | NOT NULL |  | The person that qualified for the quality metric. |
| 15 | `D_SOURCE_ID` | DOUBLE | NOT NULL | FK→ | Identifies the body site for the organism. |
| 16 | `ENCNTR_ID` | DOUBLE | NOT NULL |  | Identifies the encounter against which the quality measure is associated. Foreign key to the ENCOUNTER table. |
| 17 | `EVENT_ID` | DOUBLE | NOT NULL |  | The event_id (from clinical_event) associated with the organism result. |
| 18 | `EXTRACT_DT_TM` | DATETIME |  |  | The date/time that the record was extracted from the source system. |
| 19 | `FINANCIAL_NBR_TXT` | VARCHAR(50) |  |  | The financial number alias associated to the encounter. |
| 20 | `FIRST_PROCESS_DT_TM` | DATETIME |  |  | The date/time that the first ETL process started that created this record. |
| 21 | `HEALTH_SYSTEM_ID` | DOUBLE | NOT NULL |  | Identifies the delivery network responsible for supplying the data. |
| 22 | `HEALTH_SYSTEM_SOURCE_ID` | DOUBLE | NOT NULL | FK→ | Identifies the unique source within the delivery network responsible for supplying the data. |
| 23 | `LAST_PROCESS_DT_TM` | DATETIME |  |  | The date/time that the last ETL process started that updated this record. |
| 24 | `LH_F_IC_ANTIBGRM_METRICS_ID` | DOUBLE | NOT NULL |  | Unique generated number that identifies a single row on the LH_F_IC_ANTIBGRM_METRICS table. |
| 25 | `LOGICAL_DOMAIN_ID` | DOUBLE | NOT NULL |  | The unique identifier for a logical domain. This identifier allows the data to be grouped by logical domain. For example, If you assign clients a logical_domain_id this would allow you to store data for multiple clients on this table. |
| 26 | `MICRO_SEQ_NBR` | DOUBLE |  |  | The sequence of the microbiology result; 0 if serology. |
| 27 | `ORG_MRN_TXT` | VARCHAR(50) |  |  | Identifies the medical record number of the patient. |
| 28 | `PARTITION_DT_TM` | DATETIME |  |  | The date/time the encounter was discharged from the facility |
| 29 | `UPDT_CNT` | DOUBLE |  |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 30 | `UPDT_DT_TM` | DATETIME |  |  | The date and time the row was last inserted or updated. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 31 | `UPDT_SOURCE` | VARCHAR(50) |  |  | The script name responsible for updating the record. |
| 32 | `UPDT_TASK` | VARCHAR(50) |  |  | The registered (assigned) task number for the process that inserted or updated the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `D_COLL_BUILDING_ID` | [LH_D_BUILDING](LH_D_BUILDING.md) | `D_BUILDING_ID` |
| `D_COLL_ENCNTR_TYPE_ID` | [LH_D_ENCNTR_TYPE](LH_D_ENCNTR_TYPE.md) | `D_ENCNTR_TYPE_ID` |
| `D_COLL_FACILITY_ID` | [LH_D_FACILITY](LH_D_FACILITY.md) | `D_FACILITY_ID` |
| `D_COLL_NURSE_UNIT_ID` | [LH_D_NURSE_UNIT](LH_D_NURSE_UNIT.md) | `D_NURSE_UNIT_ID` |
| `D_ORGANISM_ID` | [LH_D_ORGANISM](LH_D_ORGANISM.md) | `D_ORGANISM_ID` |
| `D_SOURCE_ID` | [LH_D_SOURCE](LH_D_SOURCE.md) | `D_SOURCE_ID` |
| `HEALTH_SYSTEM_SOURCE_ID` | [LH_D_BUILDING](LH_D_BUILDING.md) | `HEALTH_SYSTEM_SOURCE_ID` |
| `HEALTH_SYSTEM_SOURCE_ID` | [LH_D_ENCNTR_TYPE](LH_D_ENCNTR_TYPE.md) | `HEALTH_SYSTEM_SOURCE_ID` |
| `HEALTH_SYSTEM_SOURCE_ID` | [LH_D_FACILITY](LH_D_FACILITY.md) | `HEALTH_SYSTEM_SOURCE_ID` |
| `HEALTH_SYSTEM_SOURCE_ID` | [LH_D_NURSE_UNIT](LH_D_NURSE_UNIT.md) | `HEALTH_SYSTEM_SOURCE_ID` |
| `HEALTH_SYSTEM_SOURCE_ID` | [LH_D_ORGANISM](LH_D_ORGANISM.md) | `HEALTH_SYSTEM_SOURCE_ID` |
| `HEALTH_SYSTEM_SOURCE_ID` | [LH_D_SOURCE](LH_D_SOURCE.md) | `HEALTH_SYSTEM_SOURCE_ID` |

