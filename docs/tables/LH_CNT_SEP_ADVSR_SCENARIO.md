# LH_CNT_SEP_ADVSR_SCENARIO

> This table is used to store scenarios that are used to create the Recommended Antibiotics section for the Sepsis Advisor 2020

**Description:** LH_CNT_SEP_ADVSR_SCENARIO  
**Table type:** REFERENCE  
**Primary key:** _(not published — see note)_  
**Columns:** 27

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `AGE_1` | DOUBLE |  |  | First age restriction, given in MINUTES |
| 2 | `AGE_1_OP` | VARCHAR(2) |  |  | The operator that goes along with Age_1 column |
| 3 | `AGE_2` | DOUBLE |  |  | Second age restriction, given in MINUTES |
| 4 | `AGE_2_OP` | VARCHAR(2) |  |  | The operator that goes along with Age_2 column |
| 5 | `CRCL_1` | DOUBLE |  |  | First CrCl restriction, given in mL/min |
| 6 | `CRCL_1_OP` | VARCHAR(2) |  |  | The operator that goes along with Crcl_1 column |
| 7 | `CRCL_2` | DOUBLE |  |  | Second CrCl restriction, given in mL/min |
| 8 | `CRCL_2_OP` | VARCHAR(2) |  |  | The operator that goes along with Crcl_2 column |
| 9 | `EST_GEST_AGE_1` | DOUBLE |  |  | First estimated gestational age restriction. * Obsolete Column **. Column no longer used after enhancement to solution Sepsis Advisor |
| 10 | `EST_GEST_AGE_1_OP` | VARCHAR(2) |  |  | The operator that goes along with est_gest_age_1 column. * Obsolete Column **. Column no longer used after enhancement to solution Sepsis Advisor |
| 11 | `EST_GEST_AGE_2` | DOUBLE |  |  | Second estimated gestational age restriction. * Obsolete Column **. Column no longer used after enhancement to solution Sepsis Advisor |
| 12 | `EST_GEST_AGE_2_OP` | VARCHAR(2) |  |  | The operator that goes along with est_gest_age_2 column. * Obsolete Column **. Column no longer used after enhancement to solution Sepsis Advisor |
| 13 | `FILTER_MEAN` | VARCHAR(30) |  |  | Bedrock filter mean for the order scenario number |
| 14 | `INFECTION_FACTOR` | VARCHAR(100) |  |  | Infection factor for the scenario |
| 15 | `INFECTION_SOURCE` | VARCHAR(100) |  |  | Infection source for the scenario |
| 16 | `LH_CNT_SEP_ADVSR_SCENARIO_ID` | DOUBLE | NOT NULL |  | Unique generated number that identifies a single row on the LH_CNT_SEP_ADVSR_SCENARIO table. |
| 17 | `SCENARIO_NUMBER` | DOUBLE | NOT NULL |  | Unique number that represents a specific scenario in the advisor |
| 18 | `SPECIAL_DOSING` | VARCHAR(30) |  |  | Special dosing restriction (e.g. Single Dose) |
| 19 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 20 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 21 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 22 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 23 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 24 | `WEIGHT_1` | DOUBLE |  |  | First weight restriction, given in GRAMS. * Obsolete Column **. Column no longer used after enhancement to solution Sepsis Advisor |
| 25 | `WEIGHT_1_OP` | VARCHAR(2) |  |  | The operator that goes along with Weight_1 column. * Obsolete Column **. Column no longer used after enhancement to solution Sepsis Advisor |
| 26 | `WEIGHT_2` | DOUBLE |  |  | Second weight restriction, given in GRAMS. * Obsolete Column **. Column no longer used after enhancement to solution Sepsis Advisor |
| 27 | `WEIGHT_2_OP` | VARCHAR(2) |  |  | The operator that goes along with Weight_2 column. * Obsolete Column **. Column no longer used after enhancement to solution Sepsis Advisor |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

