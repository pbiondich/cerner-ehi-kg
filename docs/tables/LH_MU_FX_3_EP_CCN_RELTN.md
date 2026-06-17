# LH_MU_FX_3_EP_CCN_RELTN

> This table holds data for identifying ep or ccn patients

**Description:** LH_MU_FX_3_EP_CCN_RELTN  
**Table type:** ACTIVITY  
**Primary key:** _(not published — see note)_  
**Columns:** 23

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ACTIVE_IND` | DOUBLE |  |  | The table row is active or inactive. A row is generally active unless it is in an inactive state such as logically deleted, combined away, pending purge, etc. |
| 2 | `ATTRIBUTION_OPTION` | DOUBLE |  |  | Ep Option set in the dm_info table ( MUSE_EP_POPULATION) |
| 3 | `BILL_EP_IND` | DOUBLE |  |  | Will signify if the Billing Logic is used |
| 4 | `CCN_POS_NBR` | DOUBLE |  |  | pos value coming from bedrock configuration settings ( 21/22/23) |
| 5 | `CHARGE_RELTN_CD` | DOUBLE | NOT NULL |  | charge reltn cd coming from charge table |
| 6 | `CHARGE_RELTN_TEXT` | VARCHAR(50) |  |  | display for the charge_reltn_cd column coming from code_value table |
| 7 | `ED_RPT_METHOD_FLAG` | DOUBLE |  |  | The value will indicate if the patient is an observation services patient. Value will be set to 1 if this is true. Default value = 0. |
| 8 | `ENCNTR_PRSNL_R_CD` | DOUBLE | NOT NULL |  | Encounter Prsnl Reltn code |
| 9 | `ENCNTR_PRSNL_R_TEXT` | VARCHAR(50) |  |  | Display for the encntr_prsnl_reltn_cd column coming from code_value table |
| 10 | `EXTRACT_DT_TM` | DATETIME |  |  | Date and time when the row was last extracted |
| 11 | `FIRST_PROCESS_DT_TM` | DATETIME |  |  | The date/time that the first ETL process started that created this record. |
| 12 | `HEALTH_SYSTEM_ID` | DOUBLE | NOT NULL |  | Identifies the delivery network responsible for supplying the data. |
| 13 | `HEALTH_SYSTEM_SOURCE_ID` | DOUBLE | NOT NULL | FK→ | Identifies the unique source within the delivery network responsible for supplying the data. |
| 14 | `LAST_PROCESS_DT_TM` | DATETIME |  |  | The date/time that the last ETL process started that updated this record. |
| 15 | `LH_MU_FX_3_EP_CCN_RELTN_ID` | DOUBLE | NOT NULL |  | Unique generated number that identifies a single row on the LH_MU_FX_3_EP_CCN_RELTN table. |
| 16 | `LH_MU_FX_3_ORD_METRICS_ID` | DOUBLE | NOT NULL | FK→ | Foreign key column coming from lh_mu_fx_3_ord_metrics |
| 17 | `LH_MU_FX_3_POP_METRICS_ID` | DOUBLE | NOT NULL | FK→ | Foreign key column coming from lh_mu_fx_3_pop_metrics |
| 18 | `PARENT_ENTITY_ID` | DOUBLE | NOT NULL |  | will hold br_cnn_id/br_eligible_provider_id |
| 19 | `PARENT_ENTITY_NAME` | VARCHAR(30) |  |  | Will hold BR_CCN / BR_ELIGIBLE_PROVIDER values to signify ccn or ep patient |
| 20 | `UPDT_CNT` | DOUBLE |  |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 21 | `UPDT_DT_TM` | DATETIME |  |  | The date and time the row was last inserted or updated. |
| 22 | `UPDT_SOURCE` | VARCHAR(50) |  |  | Source which updated the row |
| 23 | `UPDT_TASK` | VARCHAR(50) |  |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `HEALTH_SYSTEM_SOURCE_ID` | [LH_MU_FX_3_ORD_METRICS](LH_MU_FX_3_ORD_METRICS.md) | `HEALTH_SYSTEM_SOURCE_ID` |
| `HEALTH_SYSTEM_SOURCE_ID` | [LH_MU_FX_3_POP_METRICS](LH_MU_FX_3_POP_METRICS.md) | `HEALTH_SYSTEM_SOURCE_ID` |
| `LH_MU_FX_3_ORD_METRICS_ID` | [LH_MU_FX_3_ORD_METRICS](LH_MU_FX_3_ORD_METRICS.md) | `LH_MU_FX_3_ORD_METRICS_ID` |
| `LH_MU_FX_3_POP_METRICS_ID` | [LH_MU_FX_3_POP_METRICS](LH_MU_FX_3_POP_METRICS.md) | `LH_MU_FX_3_POP_METRICS_ID` |

