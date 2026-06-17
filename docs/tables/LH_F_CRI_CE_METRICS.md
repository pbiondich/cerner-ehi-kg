# LH_F_CRI_CE_METRICS

> This table is used to store metrics for the Lighthouse CRI quality measure.

**Description:** LH_F_CRI_CE_METRICS  
**Table type:** ACTIVITY  
**Primary key:** _(not published — see note)_  
**Columns:** 45

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ACTIVE_IND` | DOUBLE | NOT NULL |  | The table row is active or inactive. A row is generally active unless it is in an inactive state such as logically deleted, combined away, pending purge, etc. |
| 2 | `ACT_ART_IND` | DOUBLE |  |  | Identifies if the row refers to an arterial line. |
| 3 | `ACT_IABP_IND` | DOUBLE |  |  | Identifies if the row refers to a IABP line . |
| 4 | `ACT_LA_IND` | DOUBLE |  |  | Identifies if the row refers to a left atrial line . |
| 5 | `ACT_PA_IND` | DOUBLE |  |  | Identifies if the row refers to a pulmonary artery line . |
| 6 | `ACT_PERIPH_IND` | DOUBLE |  |  | Identifies if the row refers to a peripheral IV line . |
| 7 | `CVL_ASSESS_24H_IND` | DOUBLE |  |  | Identifies if the central venous line was assessed within 24 hours of insertion. |
| 8 | `CVL_ASSESS_DAILY_IND` | DOUBLE |  |  | Identifies if the central venous line was assessed on a daily basis. |
| 9 | `CVL_DIALYSIS_IND` | DOUBLE |  |  | Identifies if the row refers to a dialysis central line . |
| 10 | `CVL_IMP_PORT_IND` | DOUBLE |  |  | Identifies if the row refers to a implanted prot central line . |
| 11 | `CVL_IND` | DOUBLE |  |  | Identifies if the row is associated with a central venous line. |
| 12 | `CVL_INT_SHEATH_IND` | DOUBLE |  |  | Identifies if the row refers to a introducer sheath central line . |
| 13 | `CVL_PICC_IND` | DOUBLE |  |  | Identifies if the row refers to a PICC central line . |
| 14 | `CVL_TUNNEL_IND` | DOUBLE |  |  | Identifies if the row refers to a tunneled type central line . |
| 15 | `D_CRI_BUILDING_ID` | DOUBLE | NOT NULL | FK→ | The building in which the patient received an invasive line. |
| 16 | `D_CRI_FACILITY_ID` | DOUBLE | NOT NULL | FK→ | The facility in which the patient received an invasive line. |
| 17 | `D_CRI_NURSE_UNIT_ID` | DOUBLE | NOT NULL | FK→ | The nurse unit in which the patient had received an invasive line. |
| 18 | `ENCNTR_ID` | DOUBLE | NOT NULL |  | Identifies the encounter against which the quality measure is associated. Foreign key to the ENCOUNTER table. |
| 19 | `EVENT_ID` | DOUBLE | NOT NULL |  | Identifies the clinical event against which the quality measure is associated. Foreign key to the CLINICAL_EVENT table. |
| 20 | `EXTRACT_DT_TM` | DATETIME |  |  | The date/time that the record was extracted from the source system. |
| 21 | `FIRST_PROCESS_DT_TM` | DATETIME |  |  | The date/time that the first ETL process started that created this record. |
| 22 | `FOLEY_ASSESS_24H_IND` | DOUBLE |  |  | Identifies if the foley catheter has been assessed within 24 hours of hospital insertion. |
| 23 | `FOLEY_ASSESS_DAILY_IND` | DOUBLE |  |  | Identifies if the foley catheter has been assessed daily. |
| 24 | `FOLEY_DOC_INDICATION_IND` | DOUBLE |  |  | Identifies if foley insertions that had appropriate indication documented at the time of insertion. |
| 25 | `FOLEY_IND` | DOUBLE |  |  | Identifies if the row is associated with an indwelling urinary catheter. |
| 26 | `FOLEY_POA_IND` | DOUBLE |  |  | Identifies if the row is a foley catheter present upon admission. |
| 27 | `F_CRI_CE_METRICS_ID` | DOUBLE | NOT NULL |  | Unique identifier for the lighthouse CRI line metrics. |
| 28 | `F_CRI_ENCNTR_METRICS_ID` | DOUBLE | NOT NULL | FK→ | Identifier for the lighthouse CRI encounter metrics. |
| 29 | `HEALTH_SYSTEM_ID` | DOUBLE | NOT NULL |  | Identifies the delivery network responsible for supplying the data. |
| 30 | `HEALTH_SYSTEM_SOURCE_ID` | DOUBLE | NOT NULL | FK→ | Identifies the unique source within the delivery network responsible for supplying the data. |
| 31 | `INSERT_DT_TM` | DATETIME |  |  | The date/time on which the catheter was inserted. |
| 32 | `INSERT_UTC_DT_TM` | DATETIME |  |  | The date/time on which the catheter was inserted; normalized to GMT. |
| 33 | `LAST_PROCESS_DT_TM` | DATETIME |  |  | The date/time that the last ETL process started that updated this record. |
| 34 | `LOGICAL_DOMAIN_ID` | DOUBLE | NOT NULL |  | The unique identifier for a logical domain. This identifier allows the data to be grouped by logical domain. For example, If you assign clients a logical_domain_id this would allow you to store data for multiple clients on this table. |
| 35 | `PARTITION_DT_TM` | DATETIME |  |  | The date/time the encounter was discharged from the facility |
| 36 | `PREV_BSI_DT_TM` | DATETIME |  |  | Identifies the date/time of the last blood stream infection incident. |
| 37 | `PREV_BSI_UTC_DT_TM` | DATETIME |  |  | Identifies the date/time of the last blood stream infection incident normalized to GMT. |
| 38 | `PREV_UTI_DT_TM` | DATETIME |  |  | Identifies the date/time of the last urinary tract infection incident. |
| 39 | `PREV_UTI_UTC_DT_TM` | DATETIME |  |  | Identifies the date/time of the last urinary tract infection incident normalized to GMT. |
| 40 | `REMOVE_DT_TM` | DATETIME |  |  | The date/time on which the catheter was removed. |
| 41 | `REMOVE_UTC_DT_TM` | DATETIME |  |  | The date/time on which the catheter was removed; normalized to GMT. |
| 42 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 43 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 44 | `UPDT_SOURCE` | VARCHAR(50) | NOT NULL |  | The script name responsible for updating the record. |
| 45 | `UPDT_TASK` | VARCHAR(50) | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `D_CRI_BUILDING_ID` | [LH_D_BUILDING](LH_D_BUILDING.md) | `D_BUILDING_ID` |
| `D_CRI_FACILITY_ID` | [LH_D_FACILITY](LH_D_FACILITY.md) | `D_FACILITY_ID` |
| `D_CRI_NURSE_UNIT_ID` | [LH_D_NURSE_UNIT](LH_D_NURSE_UNIT.md) | `D_NURSE_UNIT_ID` |
| `F_CRI_ENCNTR_METRICS_ID` | [LH_F_CRI_ENCNTR_METRICS](LH_F_CRI_ENCNTR_METRICS.md) | `F_CRI_ENCNTR_METRICS_ID` |
| `HEALTH_SYSTEM_SOURCE_ID` | [LH_D_BUILDING](LH_D_BUILDING.md) | `HEALTH_SYSTEM_SOURCE_ID` |
| `HEALTH_SYSTEM_SOURCE_ID` | [LH_D_FACILITY](LH_D_FACILITY.md) | `HEALTH_SYSTEM_SOURCE_ID` |
| `HEALTH_SYSTEM_SOURCE_ID` | [LH_D_NURSE_UNIT](LH_D_NURSE_UNIT.md) | `HEALTH_SYSTEM_SOURCE_ID` |
| `HEALTH_SYSTEM_SOURCE_ID` | [LH_F_CRI_ENCNTR_METRICS](LH_F_CRI_ENCNTR_METRICS.md) | `HEALTH_SYSTEM_SOURCE_ID` |

