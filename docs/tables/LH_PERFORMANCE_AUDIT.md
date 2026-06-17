# LH_PERFORMANCE_AUDIT

> Contains performance data captured during the Lighthouse Reporting load process.

**Description:** LH_PERFORMANCE_AUDIT  
**Table type:** ACTIVITY  
**Primary key:** _(not published — see note)_  
**Columns:** 21

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `CATEGORY_MEAN` | VARCHAR(30) | NOT NULL |  | Unique name given to each Category. This column corresponds to the CATEGORY_MEAN column on the BR_DATAMART_CATEGORY table. |
| 2 | `DATE_RANGE_END_DT_TM` | DATETIME |  |  | The end date/time of the window used to determine the Population for a category |
| 3 | `DATE_RANGE_START_DT_TM` | DATETIME |  |  | The start date/time of the window used to determine the Population for a category |
| 4 | `ELAPSED_TIME` | DOUBLE |  |  | The time (in seconds) it took for the query to complete |
| 5 | `END_DT_TM` | DATETIME |  |  | The date/time the query finished |
| 6 | `EXTRACT_DT_TM` | DATETIME |  |  | The date/time that the record was extracted from the source system. |
| 7 | `FIRST_PROCESS_DT_TM` | DATETIME |  |  | The date/time that the first ETL process started that created this record. |
| 8 | `HEALTH_SYSTEM_ID` | DOUBLE | NOT NULL |  | The identifier of the health system |
| 9 | `HEALTH_SYSTEM_SOURCE_ID` | DOUBLE | NOT NULL |  | The identifier of the source of the health system. |
| 10 | `LAST_PROCESS_DT_TM` | DATETIME |  |  | The date/time that the last ETL process started that updated this record. |
| 11 | `LH_PERFORMANCE_AUDIT_ID` | DOUBLE | NOT NULL |  | Unique identifier for the lighthouse Performance Audit |
| 12 | `LOGICAL_DOMAIN_ID` | DOUBLE | NOT NULL | FK→ | The unique identifier for a logical domain. This identifier allows the data to be grouped by logical domain. For example, If you assign clients a logical_domain_id this would allow you to store data for multiple clients on this table. |
| 13 | `MEASURE_DESC` | VARCHAR(50) | NOT NULL |  | Name given to the query. A category can have numerous queries and this name will be unique per Category |
| 14 | `PROCESS_DT_TM` | DATETIME |  |  | The date/time that the Category started processing. All queries per Category run will have the same process_dt_tm |
| 15 | `RECORD_CNT` | DOUBLE |  |  | The number of records used to drive the query. This will usually be the Population Count of the Category |
| 16 | `START_DT_TM` | DATETIME |  |  | The date/time the query started |
| 17 | `STATUS_FLAG` | DOUBLE |  |  | 1 = Completed Successfully 2 = Completed with Errors 3 = Pending (query has not finished) |
| 18 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 19 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 20 | `UPDT_SOURCE` | VARCHAR(50) | NOT NULL |  | The script name responsible for updating the record. |
| 21 | `UPDT_TASK` | VARCHAR(50) | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `LOGICAL_DOMAIN_ID` | [LOGICAL_DOMAIN](LOGICAL_DOMAIN.md) | `LOGICAL_DOMAIN_ID` |

