# LH_ABS_IPFQR_INFO

> Holds information for reporting on IPFQR discharged patients

**Description:** LH_ABS_IPFQR_INFO  
**Table type:** ACTIVITY  
**Primary key:** _(not published — see note)_  
**Columns:** 19

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `DISCH_DT_TM` | DATETIME |  |  | The local date/time on which the patient was discharged |
| 2 | `DISCH_UTC_DT_TM` | DATETIME |  |  | The utc date/time on which the patient was discharged |
| 3 | `D_BR_CCN_ID` | DOUBLE | NOT NULL |  | CMS Certification Number. Foreign key to the LH_D_BR_CCN table. |
| 4 | `ENCNTR_ID` | DOUBLE | NOT NULL |  | Unique identifier for the Encounter table. |
| 5 | `EXTRACT_DT_TM` | DATETIME |  |  | The date/time that the record was extracted from the source system. |
| 6 | `FIRST_PROCESS_DT_TM` | DATETIME |  |  | The date/time that the first ETL process started that created this record. |
| 7 | `HEALTH_SYSTEM_ID` | DOUBLE | NOT NULL |  | Identifies the delivery network responsible for supplying the data. |
| 8 | `HEALTH_SYSTEM_SOURCE_ID` | DOUBLE | NOT NULL |  | Identifies the unique source within the delivery network responsible for supplying the data. |
| 9 | `LAST_PROCESS_DT_TM` | DATETIME |  |  | The date/time that the last ETL process started that updated this record. |
| 10 | `LH_ABS_IPFQR_INFO_ID` | DOUBLE | NOT NULL |  | Unique generated number that identifies a single row on the LH_ABS_IPFQR_INFO table. |
| 11 | `LOGICAL_DOMAIN_ID` | DOUBLE | NOT NULL |  | The unique identifier for a logical domain. This identifier allows the data to be grouped by logical domain. For example, If you assign clients a logical_domain_id this would allow you to store data for multiple clients on this table. |
| 12 | `MEDICARE_IND` | DOUBLE |  |  | Indicator to describe the case as medicare or non-medicare |
| 13 | `PAT_DISCH_AGE` | DOUBLE |  |  | Age at discharge of patient, to be used for stratum |
| 14 | `PRIN_DIAG_CAT_FLAG` | DOUBLE |  |  | Category of the principle diagnosis |
| 15 | `SAMPLE_IND` | DOUBLE |  |  | A value of 1 indicates this case is part of the sample. |
| 16 | `UPDT_CNT` | DOUBLE |  |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 17 | `UPDT_DT_TM` | DATETIME |  |  | The date and time the row was last inserted or updated. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 18 | `UPDT_SOURCE` | VARCHAR(50) |  |  | The script name responsible for updating the record. |
| 19 | `UPDT_TASK` | VARCHAR(50) |  |  | The registered (assigned) task number for the process that inserted or updated the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

