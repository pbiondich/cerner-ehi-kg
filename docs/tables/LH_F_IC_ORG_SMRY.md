# LH_F_IC_ORG_SMRY

> Infection control organism summary metrics.

**Description:** LH_F_IC_ORG_SMRY  
**Table type:** ACTIVITY  
**Primary key:** _(not published — see note)_  
**Columns:** 37

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ACTIVE_IND` | DOUBLE |  |  | The table row is active or inactive. A row is generally active unless it is in an inactive state such as logically deleted, combined away, pending purge, etc. |
| 2 | `BODY_SITE_CD` | DOUBLE | NOT NULL |  | The body site associated with the organism. |
| 3 | `CAI_IND` | DOUBLE |  |  | Community Associated Infection Indicator |
| 4 | `CDI_DESIGNATION_FLAG` | DOUBLE |  |  | The CDI Designation: 1=Recurrent, 2=Indeterminate, 3=CO-HC Facility Associated, 4=HO-HC Facility Associated, 5=Community Associated |
| 5 | `COLLECT_BED_CD` | DOUBLE | NOT NULL |  | The location of the patient at the time that the specimen was collected. |
| 6 | `COLLECT_BUILDING_CD` | DOUBLE | NOT NULL |  | The location of the patient at the time that the specimen was collected. |
| 7 | `COLLECT_DT_TM` | DATETIME |  |  | The date/time on which the specimen was collected. |
| 8 | `COLLECT_FACILITY_CD` | DOUBLE | NOT NULL |  | The location of the patient at the time that the specimen was collected. |
| 9 | `COLLECT_NURSE_UNIT_CD` | DOUBLE | NOT NULL |  | The location of the patient at the time that the specimen was collected. |
| 10 | `COLLECT_PREV_BED_CD` | DOUBLE | NOT NULL |  | The location of the patient just prior to the time that the specimen was collected. |
| 11 | `COLLECT_PREV_BUILDING_CD` | DOUBLE | NOT NULL |  | The location of the patient just prior to the time that the specimen was collected. |
| 12 | `COLLECT_PREV_FACILITY_CD` | DOUBLE | NOT NULL |  | The location of the patient just prior to the time that the specimen was collected. |
| 13 | `COLLECT_PREV_NURSE_UNIT_CD` | DOUBLE | NOT NULL |  | The location of the patient just prior to the time that the specimen was collected. |
| 14 | `COLLECT_PREV_ROOM_CD` | DOUBLE | NOT NULL |  | The location of the patient just prior to the time that the specimen was collected. |
| 15 | `COLLECT_ROOM_CD` | DOUBLE | NOT NULL |  | The location of the patient at the time that the specimen was collected. |
| 16 | `COLLECT_UTC_DT_TM` | DATETIME |  |  | The date/time on which the specimen was collected. |
| 17 | `ENCNTR_ID` | DOUBLE | NOT NULL |  | Identifies the encounter against which the quality measure is associated. |
| 18 | `EVENT_ID` | DOUBLE | NOT NULL |  | The event identifier associated with the organism. From the clinical_event table. |
| 19 | `EXTRACT_DT_TM` | DATETIME |  |  | The date/time the record was extracted from the source system. |
| 20 | `FIRST_PROCESS_DT_TM` | DATETIME |  |  | The date/time that the first ETL process started that created this record. |
| 21 | `F_IC_METRICS_ID` | DOUBLE | NOT NULL |  | Unique identifier for the infection control metrics. |
| 22 | `F_IC_ORG_SMRY_ID` | DOUBLE | NOT NULL |  | Unique identifier for the infection control organism summary metrics. |
| 23 | `HAI_IND` | DOUBLE |  |  | Healthcare Associated Infection Indicator |
| 24 | `HEALTH_SYSTEM_ID` | DOUBLE | NOT NULL |  | Identifies the delivery network responsible for supplying the data. |
| 25 | `HEALTH_SYSTEM_SOURCE_ID` | DOUBLE | NOT NULL |  | Identifies the unique source within the delivery network responsible for supplying the data. |
| 26 | `LAST_PROCESS_DT_TM` | DATETIME |  |  | The date/time that the last ETL process started that updated this record. |
| 27 | `MDRO_TYPE_FLAG` | DOUBLE |  |  | The type of MDRO: 0=Non MDRO, 1=MDRO, 2=MRSA, 3=VRE, 4=CDIFF, 5=Other |
| 28 | `MICRO_SEQ_NBR` | DOUBLE | NOT NULL |  | The microbiology sequence number associated with the organism. |
| 29 | `ORGANISM_CNT` | DOUBLE |  |  | Identifies the number of organisms. |
| 30 | `ORGANISM_ENTITY_ID` | DOUBLE | NOT NULL |  | The unique identifier associated with the organism. |
| 31 | `ORGANISM_ENTITY_NAME` | VARCHAR(50) |  |  | Identifies whether the organism is part of a Serology or not. |
| 32 | `PARTITION_DT_TM` | DATETIME |  |  | The date/time the encounter was discharged from the facility. |
| 33 | `SPECIMEN_SOURCE_CD` | DOUBLE | NOT NULL |  | The specimen source associated with the organism. |
| 34 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 35 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 36 | `UPDT_SOURCE` | VARCHAR(50) | NOT NULL |  | The script name responsible for updating the record. |
| 37 | `UPDT_TASK` | VARCHAR(50) | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

