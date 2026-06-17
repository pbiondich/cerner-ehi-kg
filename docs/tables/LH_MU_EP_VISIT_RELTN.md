# LH_MU_EP_VISIT_RELTN

> Fact table for Meaningful Use Functional Reporting

**Description:** LH_MU_EP_VISIT_RELTN  
**Table type:** ACTIVITY  
**Primary key:** _(not published — see note)_  
**Columns:** 12

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `BR_ELIGIBLE_PROVIDER_ID` | DOUBLE | NOT NULL |  | Foreign key to BR_ELIGIBLE_PROVIDER table |
| 2 | `EXTRACT_DT_TM` | DATETIME |  |  | The date/time that the record was extracted from the source system. |
| 3 | `FIRST_PROCESS_DT_TM` | DATETIME |  |  | The date/time the record was first loaded into the table. |
| 4 | `HEALTH_SYSTEM_ID` | DOUBLE | NOT NULL |  | Identifies the delivery network responsible for supplying the data. |
| 5 | `HEALTH_SYSTEM_SOURCE_ID` | DOUBLE | NOT NULL |  | Identifies the unique source within the delivery network responsible for supplying the data. |
| 6 | `LAST_PROCESS_DT_TM` | DATETIME |  |  | The date/time the record was last loaded into the table. |
| 7 | `LH_MU_EP_VISIT_RELTN_ID` | DOUBLE | NOT NULL |  | Unique generated number that identifies a single row on the LH_MU_EP_VISIT_RELTN table. |
| 8 | `LH_MU_FX_VISIT_METRICS_ID` | DOUBLE | NOT NULL |  | Foreign key to LH_MU_FX_VISIT_METRICS table |
| 9 | `UPDT_CNT` | DOUBLE |  |  | The number of times the row has been updated |
| 10 | `UPDT_DT_TM` | DATETIME |  |  | The last time the row was updated |
| 11 | `UPDT_SOURCE` | VARCHAR(50) |  |  | The source of the update |
| 12 | `UPDT_TASK` | VARCHAR(50) |  |  | The task of the update |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

