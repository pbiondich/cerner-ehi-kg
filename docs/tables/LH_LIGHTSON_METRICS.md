# LH_LIGHTSON_METRICS

> This table is used to store Lighthouse metrics for LightsOn Aggregation. This table is aggregated to the nurse_unit per month per year and stores multiple Condition/Metrics.

**Description:** LH_LIGHTSON_METRICS  
**Table type:** REFERENCE  
**Primary key:** _(not published — see note)_  
**Columns:** 20

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `BUILDING` | VARCHAR(40) |  |  | The building from which the patient was discharged. |
| 2 | `CLIENT_TARGET` | DOUBLE |  |  | Client target value for the metric. |
| 3 | `CONDITION` | VARCHAR(50) |  |  | Lighthouse Condition title. |
| 4 | `CONDITION_MEANING` | VARCHAR(50) | NOT NULL |  | Unique string for a Condition. |
| 5 | `DENOMINATOR` | DOUBLE |  |  | The denominator for the Metric. This will represent the records that qualify for the metric. |
| 6 | `DISCHARGE_MONTH` | DOUBLE |  |  | The Month the records were discharged. |
| 7 | `DISCHARGE_YEAR` | DOUBLE |  |  | The Year the records were discharged. |
| 8 | `FACILITY` | VARCHAR(40) |  |  | The facility from which the patient was discharged. |
| 9 | `LH_LIGHTSON_AGGR_ID` | DOUBLE | NOT NULL |  | Unique identifier for the Lighthouse Condition/Metric |
| 10 | `LIGHTHOUSE_GOAL` | DOUBLE |  |  | Lighthouse goal value for the metric. |
| 11 | `LOGICAL_DOMAIN_ID` | DOUBLE | NOT NULL |  | The unique identifier for the logical domain. This identifier allows the data to be grouped by logical domain. |
| 12 | `METRIC_NAME` | VARCHAR(100) |  |  | A measurement within a Condition. |
| 13 | `METRIC_NAME_MEANING` | VARCHAR(100) | NOT NULL |  | Unique string for each Metric within a Condition. |
| 14 | `NUMERATOR` | DOUBLE |  |  | The numerator for the Metric. This will represent the records that meet the metric. |
| 15 | `NURSE_UNIT` | VARCHAR(40) |  |  | The nurse unit from which the patient was discharged. |
| 16 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 17 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 18 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 19 | `UPDT_TASK` | VARCHAR(50) | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |
| 20 | `VERSION` | DOUBLE |  |  | The Version of the script loading this table. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

