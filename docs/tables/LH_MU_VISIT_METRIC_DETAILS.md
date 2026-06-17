# LH_MU_VISIT_METRIC_DETAILS

> Fact table for Meaningful Use Functional Reporting

**Description:** LH_MU_VISIT_METRIC_DETAILS  
**Table type:** ACTIVITY  
**Primary key:** _(not published — see note)_  
**Columns:** 17

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `BR_ELIGIBLE_PROVIDER_ID` | DOUBLE | NOT NULL |  | Foreign key to BR_ELIGIBLE_PROVIDER table |
| 2 | `EVENT_DT_TM` | DATETIME |  |  | The date and time of the event |
| 3 | `EXTRACT_DT_TM` | DATETIME |  |  | The date/time that the record was extracted from the source system. |
| 4 | `FIRST_PROCESS_DT_TM` | DATETIME |  |  | The date/time the record was first loaded into the table. |
| 5 | `HEALTH_SYSTEM_ID` | DOUBLE | NOT NULL |  | Identifies the delivery network responsible for supplying the data. |
| 6 | `HEALTH_SYSTEM_SOURCE_ID` | DOUBLE | NOT NULL |  | Identifies the unique source within the delivery network responsible for supplying the data. |
| 7 | `LAST_PROCESS_DT_TM` | DATETIME |  |  | The date/time the record was last loaded into the table. |
| 8 | `LH_MU_FX_VISIT_METRICS_ID` | DOUBLE | NOT NULL |  | Foreign key to LH_MU_FX_VISIT_METRICS table |
| 9 | `LH_MU_VISIT_METRIC_DETAILS_ID` | DOUBLE | NOT NULL |  | Unique generated number that identifies a single row on the LH_MU_VISIT_METRIC_DETAILS table. |
| 10 | `METRIC_TYPE` | VARCHAR(50) |  |  | Identifies the type of metric for the row |
| 11 | `NUMERATOR_IND` | DOUBLE |  |  | Identifies whether or not the row belongs in the numerator |
| 12 | `PARENT_ENTITY_ID` | DOUBLE | NOT NULL |  | The unique ID of the table that the row on this table is a child of |
| 13 | `PARENT_ENTITY_NAME` | VARCHAR(50) |  |  | The name of the table that the row on this table is a child of |
| 14 | `UPDT_CNT` | DOUBLE |  |  | The number of times the row has been updated |
| 15 | `UPDT_DT_TM` | DATETIME |  |  | The last time the row was updated |
| 16 | `UPDT_SOURCE` | VARCHAR(50) |  |  | The source of the update |
| 17 | `UPDT_TASK` | VARCHAR(50) |  |  | The task of the update |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

