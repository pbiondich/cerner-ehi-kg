# LH_F_IC_HAI

> Infection control hospital associated infection metrics.

**Description:** LH_F_IC_HAI  
**Table type:** ACTIVITY  
**Primary key:** _(not published — see note)_  
**Columns:** 34

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ACTIVE_IND` | DOUBLE |  |  | The table row is active or inactive. A row is generally active unless it is in an inactive state such as logically deleted, combined away, pending purge, etc. |
| 2 | `BSI_DEVICE_LATERALITY` | VARCHAR(100) |  |  | The location/laterality of the device. |
| 3 | `COLLECT_DT_TM` | DATETIME |  |  | The specimen collection date/time associated with the infection. |
| 4 | `COLLECT_LOCATION` | VARCHAR(255) |  |  | The location of the patient at the time of the specimen collection. |
| 5 | `COLLECT_UTC_DT_TM` | DATETIME |  |  | The specimen collection date/time associated with the infection. |
| 6 | `DEVICE_INSERT_DAYS` | DOUBLE |  |  | The total number of days from device insertion to infection. |
| 7 | `DEVICE_INSERT_DT_TM` | DATETIME |  |  | The date/time on which the device associated with the HAI event was inserted. |
| 8 | `DEVICE_INSERT_UTC_DT_TM` | DATETIME |  |  | The date/time on which the device associated with the HAI event was inserted. |
| 9 | `ENCNTR_ID` | DOUBLE | NOT NULL |  | Identifies the encounter against which the quality measure is associated. |
| 10 | `EVENT_DT_TM` | DATETIME |  |  | The date/time of the HAI event. |
| 11 | `EVENT_LOCATION` | VARCHAR(255) |  |  | The location of the patient at the time of the HAI event. |
| 12 | `EVENT_UTC_DT_TM` | DATETIME |  |  | The date/time of the HAI event. |
| 13 | `EXTRACT_DT_TM` | DATETIME |  |  | The date/time the record was extracted from the source system. |
| 14 | `FIRST_PROCESS_DT_TM` | DATETIME |  |  | The date/time that the first ETL process started that created this record. |
| 15 | `F_IC_HAI_ID` | DOUBLE | NOT NULL |  | Unique identifier for the infection control HAI metrics. |
| 16 | `F_IC_METRICS_ID` | DOUBLE | NOT NULL |  | Unique identifier for the infection control metrics. |
| 17 | `HAI_EVENT_ID` | DOUBLE | NOT NULL |  | The clinical event associated with the HAI event. |
| 18 | `HAI_SUBTYPE` | VARCHAR(100) |  |  | Identifies the sub-type of infection. |
| 19 | `HAI_TYPE` | VARCHAR(50) |  |  | Identifies the type of infection. |
| 20 | `HEALTH_SYSTEM_ID` | DOUBLE | NOT NULL |  | Identifies the delivery network responsible for supplying the data. |
| 21 | `HEALTH_SYSTEM_SOURCE_ID` | DOUBLE | NOT NULL |  | Identifies the unique source within the delivery network responsible for supplying the data. |
| 22 | `LAST_PROCESS_DT_TM` | DATETIME |  |  | The date/time that the last ETL process started that updated this record. |
| 23 | `ORGANISM` | VARCHAR(255) |  |  | The organisms associated with the HAI event. |
| 24 | `PARTITION_DT_TM` | DATETIME |  |  | The date/time the encounter was discharged from the facility. |
| 25 | `SPECIMEN_SOURCE` | VARCHAR(100) |  |  | The specimen source for the HAI. |
| 26 | `SSI_NHSN_PROC_DESC` | VARCHAR(50) |  |  | The NHSN procedure code associated with the SSI infection. |
| 27 | `SSI_ORGAN` | VARCHAR(100) |  |  | The organ identified for the SSI infection type of organ/space. |
| 28 | `SSI_PROC_CODE` | VARCHAR(50) |  |  | The NHSN procedure code associated with the SSI infection. |
| 29 | `SSI_PROC_DESC` | VARCHAR(100) |  |  | The surgical procedure associated with the SSI infection. |
| 30 | `SURGEON_NAME` | VARCHAR(100) |  |  | The surgeon associated with the SSI infection. |
| 31 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 32 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 33 | `UPDT_SOURCE` | VARCHAR(50) | NOT NULL |  | The script name responsible for updating the record. |
| 34 | `UPDT_TASK` | VARCHAR(50) | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

