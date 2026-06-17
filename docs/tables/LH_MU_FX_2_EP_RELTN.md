# LH_MU_FX_2_EP_RELTN

> Fact table to store the relationships betwen MU FX steage 2 ecnounter and BR Eligible

**Description:** LH_MU_FX_2_EP_RELTN  
**Table type:** ACTIVITY  
**Primary key:** _(not published — see note)_  
**Columns:** 16

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `BR_ELIGIBLE_PROVIDER_ID` | DOUBLE | NOT NULL |  | Foreign key to BR_ELIGIBLE_PROVIDER table |
| 2 | `D_EP_PRSNL_ID` | DOUBLE | NOT NULL | FK→ | Identifies the eligible provider with the quality measure. Foreign key to the LH_D_PERSONNAL table. |
| 3 | `EC_IND` | DOUBLE |  |  | Indicator used to show that an inpatient qualified for an EC. |
| 4 | `ENCNTR_PRSNL_R_CD` | DOUBLE | NOT NULL |  | Identifies the type of encounter personnel relationship |
| 5 | `EXTRACT_DT_TM` | DATETIME |  |  | The date/time that the record was extracted from the source system. |
| 6 | `FIRST_PROCESS_DT_TM` | DATETIME |  |  | The date/time that the first ETL process started that created this record. |
| 7 | `HEALTH_SYSTEM_ID` | DOUBLE | NOT NULL |  | Identifies the delivery network responsible for supplying the data. |
| 8 | `HEALTH_SYSTEM_SOURCE_ID` | DOUBLE | NOT NULL | FK→ | Identifies the unique source within the delivery network responsible for supplying the data. |
| 9 | `LAST_PROCESS_DT_TM` | DATETIME |  |  | The date/time that the last ETL process started that updated this record. |
| 10 | `LH_MU_FX_2_EP_RELTN_ID` | DOUBLE | NOT NULL |  | Unique generated number that identifies a single row on the LH_MU_FX_2_EP_RELTN table. |
| 11 | `LH_MU_FX_2_METRICS_ID` | DOUBLE | NOT NULL | FK→ | Foreign key to LH_MU_FX_2_METRICS table |
| 12 | `LOGICAL_DOMAIN_ID` | DOUBLE | NOT NULL |  | The unique identifier for a logical domain. This identifier allows the data to be grouped by logical domain. For example, If you assign clients a logical_domain_id this would allow you to store data for multiple clients on this table. |
| 13 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 14 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 15 | `UPDT_SOURCE` | VARCHAR(50) | NOT NULL |  | The source of the update |
| 16 | `UPDT_TASK` | VARCHAR(50) | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `D_EP_PRSNL_ID` | [LH_D_PERSONNEL](LH_D_PERSONNEL.md) | `D_PRSNL_ID` |
| `HEALTH_SYSTEM_SOURCE_ID` | [LH_D_PERSONNEL](LH_D_PERSONNEL.md) | `HEALTH_SYSTEM_SOURCE_ID` |
| `HEALTH_SYSTEM_SOURCE_ID` | [LH_MU_FX_2_METRICS](LH_MU_FX_2_METRICS.md) | `HEALTH_SYSTEM_SOURCE_ID` |
| `LH_MU_FX_2_METRICS_ID` | [LH_MU_FX_2_METRICS](LH_MU_FX_2_METRICS.md) | `LH_MU_FX_2_METRICS_ID` |

