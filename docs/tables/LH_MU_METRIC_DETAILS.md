# LH_MU_METRIC_DETAILS

> Fact table for Meaningful Use Lighthouse Report

**Description:** LH_MU_METRIC_DETAILS  
**Table type:** ACTIVITY  
**Primary key:** _(not published — see note)_  
**Columns:** 20

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `BR_ELIGIBLE_PROVIDER_ID` | DOUBLE | NOT NULL | FK→ | BR ELIGIBLE PROVIDER |
| 2 | `EVENT_DESCRIPTION` | VARCHAR(1000) |  |  | The description of the event. |
| 3 | `EVENT_DT_TM` | DATETIME |  |  | The date and time of the event. |
| 4 | `EXTRACT_DT_TM` | DATETIME |  |  | The date/time that the record was extracted from the source system. |
| 5 | `FIRST_PROCESS_DT_TM` | DATETIME |  |  | The date/time the record was first loaded into the table. |
| 6 | `HEALTH_SYSTEM_ID` | DOUBLE | NOT NULL |  | Identifies the delivery network responsible for supplying the data. |
| 7 | `HEALTH_SYSTEM_SOURCE_ID` | DOUBLE | NOT NULL |  | Identifies the unique source within the delivery network responsible for supplying the data. |
| 8 | `LAST_PROCESS_DT_TM` | DATETIME |  |  | The date/time the record was last loaded into the table. |
| 9 | `LH_MU_FX_METRICS_ID` | DOUBLE | NOT NULL |  | Foreign key to lh_mu_fx_metrics table. |
| 10 | `LH_MU_METRIC_DETAILS_ID` | DOUBLE | NOT NULL |  | Unique generated number that identifies a single row on the LH_MU_METRIC_DETAILS table. |
| 11 | `METRIC_TYPE` | VARCHAR(50) |  |  | Identifies the type of metric for the row. |
| 12 | `NUMERATOR_IND` | DOUBLE | NOT NULL |  | Identifies whether or not the row belongs in the numerator. |
| 13 | `ORDER_PROVIDER_ID` | DOUBLE |  |  | This column will provide the name of the ordering provider who placed the order on the patient. |
| 14 | `PARENT_ENTITY_ID` | DOUBLE | NOT NULL |  | The name of the table that the row on this table is a child of. |
| 15 | `PARENT_ENTITY_NAME` | VARCHAR(50) | NOT NULL |  | The name of the table that the row on this table is a child of. |
| 16 | `SUB_METRIC_TYPE` | VARCHAR(50) |  |  | This field is used to identify the TYPE of metric for the row |
| 17 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 18 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 19 | `UPDT_SOURCE` | VARCHAR(50) |  |  | The source of the update. |
| 20 | `UPDT_TASK` | VARCHAR(50) |  |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `BR_ELIGIBLE_PROVIDER_ID` | [BR_ELIGIBLE_PROVIDER](BR_ELIGIBLE_PROVIDER.md) | `BR_ELIGIBLE_PROVIDER_ID` |

