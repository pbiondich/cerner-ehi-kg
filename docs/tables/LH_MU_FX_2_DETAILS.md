# LH_MU_FX_2_DETAILS

> Fact table is to store metric details for Meaningful Use Functional Stage 2 Reporting

**Description:** LH_MU_FX_2_DETAILS  
**Table type:** ACTIVITY  
**Primary key:** _(not published — see note)_  
**Columns:** 23

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `BR_ELIGIBLE_PROVIDER_ID` | DOUBLE | NOT NULL |  | Foreign key to BR_ELIGIBLE_PROVIDER table |
| 2 | `D_EP_PRSNL_ID` | DOUBLE | NOT NULL | FK→ | Identifies the eligible provider with the quality measure. Foreign key to the LH_D_PERSONNAL table. |
| 3 | `EVENT_DESCRIPTION` | VARCHAR(1000) |  |  | The description of the event |
| 4 | `EVENT_DT_TM` | DATETIME |  |  | The date and time of the event |
| 5 | `EVENT_UTC_DT_TM` | DATETIME |  |  | The date and time of the event |
| 6 | `EXTRACT_DT_TM` | DATETIME |  |  | The date/time that the record was extracted from the source system. |
| 7 | `FIRST_PROCESS_DT_TM` | DATETIME |  |  | The date/time that the first ETL process started that created this record. |
| 8 | `HEALTH_SYSTEM_ID` | DOUBLE | NOT NULL |  | Identifies the delivery network responsible for supplying the data. |
| 9 | `HEALTH_SYSTEM_SOURCE_ID` | DOUBLE | NOT NULL | FK→ | Identifies the unique source within the delivery network responsible for supplying the data. |
| 10 | `LAST_PROCESS_DT_TM` | DATETIME |  |  | The date/time that the last ETL process started that updated this record. |
| 11 | `LH_MU_FX_2_DETAILS_ID` | DOUBLE | NOT NULL |  | Unique generated number that identifies a single row on the LH_MU_FX_2_DETAILS table. |
| 12 | `LH_MU_FX_2_METRICS_ID` | DOUBLE | NOT NULL | FK→ | Foreign key to LH_MU_FX_VISIT_METRICS table |
| 13 | `METRIC_TYPE` | VARCHAR(50) |  |  | Identifies the type of metric for the row |
| 14 | `MSG_SENDER_ID` | DOUBLE | NOT NULL |  | Indicates the person_id of who sent the secure message to the patient. |
| 15 | `NUMERATOR_IND` | DOUBLE | NOT NULL |  | Identifies whether or not the row belongs in the numerator |
| 16 | `ORDER_PROVIDER_ID` | DOUBLE |  |  | This column will provide the name of the ordering provider who placed the order on the patient. |
| 17 | `PARENT_ENTITY_ID` | DOUBLE | NOT NULL |  | The unique ID of the table that the row on this table is a child of |
| 18 | `PARENT_ENTITY_NAME` | VARCHAR(50) | NOT NULL |  | The name of the table that the row on this table is a child of |
| 19 | `SUB_METRIC_TYPE` | VARCHAR(50) |  |  | Identifies the type of metric for the row |
| 20 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 21 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 22 | `UPDT_SOURCE` | VARCHAR(50) | NOT NULL |  | The source of the update |
| 23 | `UPDT_TASK` | VARCHAR(50) | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `D_EP_PRSNL_ID` | [LH_D_PERSONNEL](LH_D_PERSONNEL.md) | `D_PRSNL_ID` |
| `HEALTH_SYSTEM_SOURCE_ID` | [LH_D_PERSONNEL](LH_D_PERSONNEL.md) | `HEALTH_SYSTEM_SOURCE_ID` |
| `HEALTH_SYSTEM_SOURCE_ID` | [LH_MU_FX_2_METRICS](LH_MU_FX_2_METRICS.md) | `HEALTH_SYSTEM_SOURCE_ID` |
| `LH_MU_FX_2_METRICS_ID` | [LH_MU_FX_2_METRICS](LH_MU_FX_2_METRICS.md) | `LH_MU_FX_2_METRICS_ID` |

