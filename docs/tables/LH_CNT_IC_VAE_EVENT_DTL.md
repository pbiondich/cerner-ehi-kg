# LH_CNT_IC_VAE_EVENT_DTL

> Contains event details for a patient on a ventilator

**Description:** LH_CNT_IC_VAE_EVENT_DTL  
**Table type:** ACTIVITY  
**Primary key:** _(not published — see note)_  
**Columns:** 40

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `APRV_IND` | DOUBLE |  |  | Indicates whether the patient has been APRV mode of ventilation for the given mechanical vent date |
| 2 | `FIO2_HL_IND` | DOUBLE |  |  | Indicates that FiO2 was a factor for VAE |
| 3 | `FIO2_MIN_VALUE` | DOUBLE | NOT NULL |  | Daily minimum FiO2 value for the given date |
| 4 | `LH_CNT_IC_VAE_EVENT_DTL_ID` | DOUBLE | NOT NULL |  | Unique generated number that identifies a single row on the LH_CNT_IC_VAE_EVENT_DTL table. |
| 5 | `LH_CNT_IC_VAE_ID` | DOUBLE | NOT NULL | FK→ | Key to LH_CNT_IC_VAE table. |
| 6 | `MECH_VENT_DT_TM` | DATETIME |  |  | Date and Time patient was on a mechanical ventilator |
| 7 | `OFF_VENT_IND` | DOUBLE |  |  | Indicates the patient was off the mechanical ventilator |
| 8 | `ORDER_ID` | DOUBLE | NOT NULL | FK→ | FK value from ORDERS table entry |
| 9 | `PEEP_MIN_HL_IND` | DOUBLE |  |  | Indicates that PEEP Min was a factor for VAE |
| 10 | `PEEP_MIN_VALUE` | DOUBLE | NOT NULL |  | Daily minimum PEEP value for the given date |
| 11 | `POLY_HL_IND` | DOUBLE |  |  | Indicates that Polys was a factor for VAE |
| 12 | `POLY_IND` | DOUBLE |  |  | Indicates if the result for neutrophils met the criteria |
| 13 | `POS_LEGION_HL_IND` | DOUBLE |  |  | Indicates that Pos Legionella or viral pathogen was a factor for VAE |
| 14 | `POS_LEGION_IND` | DOUBLE |  |  | Indicates if there is a positive result of Legionella spp or viral pathogens. |
| 15 | `POS_LUNG_HL_IND` | DOUBLE |  |  | Indicates that Pos Lung Histopathology was a factor for VAE |
| 16 | `POS_PLEURAL_HL_IND` | DOUBLE |  |  | Indicates that Pos Pleural Fluid cx was a factor for VAE |
| 17 | `POS_PLEURAL_IND` | DOUBLE |  |  | Indicates whether the pleural fluid culture is positive or negative |
| 18 | `QADS_HL_IND` | DOUBLE |  |  | Indicates that QADS was a factor for VAE |
| 19 | `QADS_IND` | DOUBLE |  |  | Indicates whether the given date is a qualifying anti microbial drug day |
| 20 | `QUANT_CRIT_HL_IND` | DOUBLE |  |  | Indicates that Quant criteria was a factor for VAE |
| 21 | `QUANT_CRIT_IND` | DOUBLE |  |  | Indicates if the quantitative or semi -quantitative results meet the threshold criteria, for the specimen types |
| 22 | `SPECIMEN_CD` | DOUBLE | NOT NULL |  | Codeset: 2052, Specimen culture type that has been ordered |
| 23 | `SPECIMEN_HL_IND` | DOUBLE |  |  | Indicates that Specimen was a factor for VAE |
| 24 | `SPUTUM_HL_IND` | DOUBLE |  |  | Indicates that Pos Sputum cx or qual cx was factor for VAE |
| 25 | `SPUTUM_IND` | DOUBLE |  |  | Indicates if the qualitative results criteria is met, for the specimen types |
| 26 | `SQUAM_HL_IND` | DOUBLE |  |  | Indicates that Squam Epis was a factor for VAE |
| 27 | `SQUAM_IND` | DOUBLE |  |  | Indicates if the result for squamous epithileal cells met the criteria |
| 28 | `TEMP_MAX_HL_IND` | DOUBLE |  |  | Indicates that Temp Max was a factor for VAE |
| 29 | `TEMP_MAX_TXT` | VARCHAR(255) |  |  | Daily maximum temperature for the given date |
| 30 | `TEMP_MIN_HL_IND` | DOUBLE |  |  | Indicates that Temp Min was a factor for VAE |
| 31 | `TEMP_MIN_TXT` | VARCHAR(255) |  |  | Daily minimum Temperature for the given date |
| 32 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 33 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 34 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 35 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 36 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |
| 37 | `WBC_MAX_HL_IND` | DOUBLE |  |  | Indicates that WBC Max was a factor for VAE |
| 38 | `WBC_MAX_TXT` | VARCHAR(255) |  |  | Daily minimum WBC for the given date |
| 39 | `WBC_MIN_HL_IND` | DOUBLE |  |  | Indicates that WBC Min was a factor for VAE |
| 40 | `WBC_MIN_TXT` | VARCHAR(255) |  |  | Daily minimum WBC for the given date |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `LH_CNT_IC_VAE_ID` | [LH_CNT_IC_VAE](LH_CNT_IC_VAE.md) | `LH_CNT_IC_VAE_ID` |
| `ORDER_ID` | [ORDERS](ORDERS.md) | `ORDER_ID` |

