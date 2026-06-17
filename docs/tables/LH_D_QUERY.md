# LH_D_QUERY

> Dimension table contain query and measure information for Meaningful Use QM and PQRI solutions.

**Description:** LH_D_QUERY  
**Table type:** REFERENCE  
**Primary key:** `D_QUERY_ID`  
**Columns:** 18  
**Referenced by:** 22 columns

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ACTIVE_IND` | DOUBLE |  |  | The table row is active or inactive. A row is generally active unless it is in an inactive state such as logically deleted, combined away, pending purge, etc. |
| 2 | `BEG_EFFECTIVE_DT_TM` | DATETIME |  |  | The date and time for which this table row becomes effective. Normally, this will be the date and time the row is added, but could be a past or future date and time. |
| 3 | `D_QUERY_ID` | DOUBLE | NOT NULL | PK | Unique generated number that identifies a single row on LH_D_QUERY table. |
| 4 | `END_EFFECTIVE_DT_TM` | DATETIME |  |  | The date/time after which the row is no longer valid as active current data. This may be valued with the date that the row became inactive. |
| 5 | `EXECUTION_MODE_FLAG` | DOUBLE | NOT NULL |  | The Oracle optimizer execution mode. 0 = default, 1=RBO, 2=CBO |
| 6 | `EXTRACT_DT_TM` | DATETIME |  |  | The date/time that the program running the extracts was started. This field should be the same across all files and across all records within a file for a given extraction run. This time should be in UTC time. |
| 7 | `HEALTH_SYSTEM_ID` | DOUBLE | NOT NULL |  | Identifies the delivery network responsible for supplying the data. |
| 8 | `HEALTH_SYSTEM_SOURCE_ID` | DOUBLE | NOT NULL |  | Identifies the unique source within the delivery network responsible for supplying the data. |
| 9 | `HINT_NAME` | VARCHAR(200) |  |  | Contains the name of the hint that is to be used for the query. |
| 10 | `LOGICAL_DOMAIN_ID` | DOUBLE | NOT NULL |  | The unique identifier for a logical domain. This identifier allows the data to be grouped by logical domain. For example, If you assign clients a logical_domain_id this would allow you to store data for multiple clients on this table. |
| 11 | `POPULATION_GROUP` | VARCHAR(50) |  |  | Name of the measure. |
| 12 | `PROCESS_DT_TM` | DATETIME |  |  | The date/time the record was first loaded into the table. |
| 13 | `QUERY_NAME` | VARCHAR(100) | NOT NULL |  | Name of the individual queries associated with a measure. |
| 14 | `REPORT_SECTION_GRAIN` | VARCHAR(100) |  |  | This column will be used to store grain of the report_writer_section for all queries. This will allow us to dynamically change the grain of a query. |
| 15 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 16 | `UPDT_DT_TM` | DATETIME |  |  | The date and time the row was last inserted or updated. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 17 | `UPDT_SOURCE` | VARCHAR(50) | NOT NULL |  | The script name responsible for updating the record. |
| 18 | `UPDT_TASK` | VARCHAR(50) | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Referenced by (22)

| From table | Column |
|------------|--------|
| [LH_AMB_EVENT_DATA](LH_AMB_EVENT_DATA.md) | `D_QUERY_ID` |
| [LH_AMB_EVENT_DATA_2016](LH_AMB_EVENT_DATA_2016.md) | `D_QUERY_ID` |
| [LH_AMB_EVENT_DATA_2017](LH_AMB_EVENT_DATA_2017.md) | `D_QUERY_ID` |
| [LH_AMB_EVENT_DATA_2018](LH_AMB_EVENT_DATA_2018.md) | `D_QUERY_ID` |
| [LH_AMB_EVENT_DATA_2019](LH_AMB_EVENT_DATA_2019.md) | `D_QUERY_ID` |
| [LH_AMB_EVENT_DATA_2020](LH_AMB_EVENT_DATA_2020.md) | `D_QUERY_ID` |
| [LH_AMB_EVENT_DATA_2021](LH_AMB_EVENT_DATA_2021.md) | `D_QUERY_ID` |
| [LH_AMB_EVENT_DATA_2022](LH_AMB_EVENT_DATA_2022.md) | `D_QUERY_ID` |
| [LH_AMB_EVENT_DATA_2023](LH_AMB_EVENT_DATA_2023.md) | `D_QUERY_ID` |
| [LH_AMB_EVENT_DATA_2024](LH_AMB_EVENT_DATA_2024.md) | `D_QUERY_ID` |
| [LH_AMB_EVENT_DATA_2025](LH_AMB_EVENT_DATA_2025.md) | `D_QUERY_ID` |
| [LH_AMB_QUAL_ENCNTR](LH_AMB_QUAL_ENCNTR.md) | `D_QUERY_ID` |
| [LH_AMB_QUAL_ENCNTR_2016](LH_AMB_QUAL_ENCNTR_2016.md) | `D_QUERY_ID` |
| [LH_AMB_QUAL_ENCNTR_2017](LH_AMB_QUAL_ENCNTR_2017.md) | `D_QUERY_ID` |
| [LH_AMB_QUAL_ENCNTR_2018](LH_AMB_QUAL_ENCNTR_2018.md) | `D_QUERY_ID` |
| [LH_AMB_QUAL_ENCNTR_2019](LH_AMB_QUAL_ENCNTR_2019.md) | `D_QUERY_ID` |
| [LH_AMB_QUAL_ENCNTR_2020](LH_AMB_QUAL_ENCNTR_2020.md) | `D_QUERY_ID` |
| [LH_AMB_QUAL_ENCNTR_2021](LH_AMB_QUAL_ENCNTR_2021.md) | `D_QUERY_ID` |
| [LH_AMB_QUAL_ENCNTR_2022](LH_AMB_QUAL_ENCNTR_2022.md) | `D_QUERY_ID` |
| [LH_AMB_QUAL_ENCNTR_2023](LH_AMB_QUAL_ENCNTR_2023.md) | `D_QUERY_ID` |
| [LH_AMB_QUAL_ENCNTR_2024](LH_AMB_QUAL_ENCNTR_2024.md) | `D_QUERY_ID` |
| [LH_AMB_QUAL_ENCNTR_2025](LH_AMB_QUAL_ENCNTR_2025.md) | `D_QUERY_ID` |

