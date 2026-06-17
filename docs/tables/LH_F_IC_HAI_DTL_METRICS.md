# LH_F_IC_HAI_DTL_METRICS

> This table is used to store Infection Control HAI metrics from the Lighthouse Abstractor (eQuality Check). This table is at the encounter grain.

**Description:** LH_F_IC_HAI_DTL_METRICS  
**Table type:** ACTIVITY  
**Primary key:** _(not published — see note)_  
**Columns:** 36

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ACTIVE_IND` | DOUBLE |  |  | The table row is active or inactive. A row is generally active unless it is in an inactive state such as logically deleted, combined away, pending purge, etc. |
| 2 | `COLLECT_DT_TM` | DATETIME |  |  | Date/Time when the organism was collected |
| 3 | `COLLECT_FACILITY_TXT` | VARCHAR(100) |  |  | Where the patient was located when the specimen was collected |
| 4 | `COLLECT_NURSE_UNIT_TXT` | VARCHAR(100) |  |  | Where the patient was located when the specimen was collected |
| 5 | `COLLECT_UTC_DT_TM` | DATETIME |  |  | Date/Time when the organism was collected |
| 6 | `ENCNTR_ID` | DOUBLE | NOT NULL |  | Identifies the encounter against which the quality measure is associated. Foreign key to the ENCOUNTER table. |
| 7 | `EVENT_DT_TM` | DATETIME |  |  | Date/Time when the event occurred |
| 8 | `EVENT_FACILITY_TXT` | VARCHAR(100) |  |  | Where the event took place |
| 9 | `EVENT_ID` | DOUBLE | NOT NULL |  | ID of the Advisor Event. From the clinical_event table. |
| 10 | `EVENT_NURSE_UNIT_TXT` | VARCHAR(100) |  |  | Where the event took place |
| 11 | `EVENT_UTC_DT_TM` | DATETIME |  |  | Date/Time when the event occurred |
| 12 | `EXTRACT_DT_TM` | DATETIME |  |  | The date/time that the record was extracted from the source system. |
| 13 | `FIRST_PROCESS_DT_TM` | DATETIME |  |  | The date/time that the first ETL process started that created this record. |
| 14 | `HAI_CATEGORY_TXT` | VARCHAR(100) |  |  | BSI/UTI/PN/SSI |
| 15 | `HEALTH_SYSTEM_ID` | DOUBLE | NOT NULL |  | Identifies the delivery network responsible for supplying the data. |
| 16 | `HEALTH_SYSTEM_SOURCE_ID` | DOUBLE | NOT NULL |  | Identifies the unique source within the delivery network responsible for supplying the data. |
| 17 | `ICD9_CODE_DESC_TXT` | VARCHAR(100) |  |  | SSI Only: ICD9 Procedure Code Description |
| 18 | `ICD9_CODE_TXT` | VARCHAR(100) |  |  | SSI Only: ICD9 Procedure Code |
| 19 | `INSERT_DT_TM` | DATETIME |  |  | BSI/UTI/PN Only: Line insertion date/time |
| 20 | `INSERT_UTC_DT_TM` | DATETIME |  |  | BSI/UTI/PN Only: Line insertion date/time |
| 21 | `LAST_PROCESS_DT_TM` | DATETIME |  |  | The date/time that the last ETL process started that updated this record. |
| 22 | `LH_F_IC_HAI_DTL_METRICS_ID` | DOUBLE | NOT NULL |  | Unique generated number that identifies a single row on the LH_F_IC_HAI_DTL_METRICS table. |
| 23 | `LOCATION_LATERALITY_TXT` | VARCHAR(100) |  |  | BSI/UTI/PN Only: Location and Laterality of Line (i.e. Hand R) |
| 24 | `NBR_DAYS_INSERT_INFECT` | DOUBLE |  |  | BSI/UTI/PN Only: Number of days from insertion of line to infection |
| 25 | `ORGANISM_TXT` | VARCHAR(100) |  |  | Organism Name |
| 26 | `ORGAN_TYPE_TXT` | VARCHAR(100) |  |  | SSI Only: Organ being operated on |
| 27 | `PARTITION_DT_TM` | DATETIME |  |  | The date/time the encounter was discharged from the facility |
| 28 | `SPECIFIC_HAI_TXT` | VARCHAR(100) |  |  | Specific HAI (Central Line, Other, Procedure, etc.) |
| 29 | `SPECIMEN_SOURCE_TXT` | VARCHAR(100) |  |  | How the specimen was collected (i.e. Blood) |
| 30 | `SSI_NHSN_PROC_TXT` | VARCHAR(100) |  |  | COLO, HYST, KSPRO, HPRO, CBGC |
| 31 | `SURGEON_NAME_TXT` | VARCHAR(100) |  |  | SSI Only: Surgeon performing operation |
| 32 | `UNIT_OF_ORIGIN_TXT` | VARCHAR(100) |  |  | BSI/UTI/PN Only: Patient Location When Line was Inserted |
| 33 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 34 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 35 | `UPDT_SOURCE` | VARCHAR(50) | NOT NULL |  | The script name responsible for updating the record. |
| 36 | `UPDT_TASK` | VARCHAR(50) | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

