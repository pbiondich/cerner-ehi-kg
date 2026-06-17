# LH_HINT

> This table will hold reference data regarding the hints that queries should be using in the Lighthouse Reporting data model

**Description:** LH_HINT  
**Table type:** REFERENCE  
**Primary key:** _(not published — see note)_  
**Columns:** 13

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ACTIVE_IND` | DOUBLE | NOT NULL |  | The table row is active or inactive. A row is generally active unless it is in an inactive state such as logically deleted, combined away, pending purge, etc. |
| 2 | `CUSTOM_IND` | DOUBLE | NOT NULL |  | Identifies if the row has been updated manually on an individual client site |
| 3 | `EXTRACT_DT_TM` | DATETIME |  |  | The date/time that the program running the extracts was started. This filed should be the same across all files and across all records within a file for a given extraction run. This time should be in UTC time. |
| 4 | `HEALTH_SYSTEM_SOURCE_ID` | DOUBLE | NOT NULL |  | Identifies the unique source within the delivery network responsible for supplying the data |
| 5 | `HINT_TXT` | VARCHAR(2000) |  |  | The exact hint text that we want to use for the script + measure |
| 6 | `LH_HINT_ID` | DOUBLE | NOT NULL |  | Unique generated number that identifies a single row on the LH_HINT table. |
| 7 | `MEASURE_NAME` | VARCHAR(50) | NOT NULL |  | The specific measure/query that is going to be hinted |
| 8 | `PROCESS_DT_TM` | DATETIME |  |  | The date/time the record wad first loaded into the table. |
| 9 | `SCRIPT_NAME` | VARCHAR(40) | NOT NULL |  | The script name that is associated to the Measure |
| 10 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 11 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 12 | `UPDT_SOURCE` | VARCHAR(50) | NOT NULL |  | The script name responsible for updating the record. |
| 13 | `UPDT_TASK` | VARCHAR(50) | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

