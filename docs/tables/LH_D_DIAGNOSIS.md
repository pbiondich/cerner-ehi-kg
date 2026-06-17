# LH_D_DIAGNOSIS

> This table is used to store diagnosis reference data for the lighthouse quality metrics.

**Description:** LH_D_DIAGNOSIS  
**Table type:** REFERENCE  
**Primary key:** `D_DIAGNOSIS_ID`, `HEALTH_SYSTEM_SOURCE_ID`  
**Columns:** 19  
**Referenced by:** 64 columns

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ACTIVE_IND` | DOUBLE |  |  | The table row is active or inactive. A row is generally active unless it is in an inactive state such as logically deleted, combined away, pending purge, etc. |
| 2 | `BEG_EFFECTIVE_DT_TM` | DATETIME |  |  | The date and time for which this table row becomes effective. Normally, this will be the date and time the row is added, but could be a past or future date and time. |
| 3 | `CONCEPT_CKI` | VARCHAR(255) |  |  | CKI from the concept table representing the functional concept. |
| 4 | `DIAGNOSIS_CODE` | VARCHAR(50) |  |  | The code associated with the diagnosis. |
| 5 | `D_DIAGNOSIS_ID` | DOUBLE | NOT NULL | PK | Unique identifier for the diagnosis. |
| 6 | `END_EFFECTIVE_DT_TM` | DATETIME |  |  | The date/time after which the row is no longer valid as active current data. This may be valued with the date that the row became inactive. |
| 7 | `EXTRACT_DT_TM` | DATETIME |  |  | The date/time that the program running the extracts was started. This field should be the same across all files and across all records within a file for a given extraction run. This time should be in UTC time. |
| 8 | `HEALTH_SYSTEM_SOURCE_ID` | DOUBLE | NOT NULL | PK | Identifies the unique source within the delivery network responsible for supplying the data. |
| 9 | `LONG_DESCRIPTION` | VARCHAR(255) |  |  | The long description of the diagnosis. |
| 10 | `NOMENCLATURE_ID` | DOUBLE |  |  | Identifies the diagnosis nomenclature associated with the quality measure. Foreign key to the nomenclature table with a diagnosis principle type. |
| 11 | `PROCESS_DT_TM` | DATETIME |  |  | The date/time the record was first loaded into the table. |
| 12 | `SHORT_DESCRIPTION` | VARCHAR(60) |  |  | The short description of the diagnosis. |
| 13 | `SOURCE_VOCABULARY_MEANING` | VARCHAR(40) |  |  | The vocabulary that contributed the diagnosis (i.e. ICD9 ICD10 etc.) |
| 14 | `SRC_BEG_EFFECTIVE_DT_TM` | DATETIME |  |  | The date/time on which the record became effective on the source system. |
| 15 | `SRC_END_EFFECTIVE_DT_TM` | DATETIME |  |  | The date/time on which the record is no longer effective on the source system. |
| 16 | `UPDT_CNT` | DOUBLE |  |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 17 | `UPDT_DT_TM` | DATETIME |  |  | The date and time the row was last inserted or updated. |
| 18 | `UPDT_SOURCE` | VARCHAR(50) |  |  | The script name responsible for updating the record. |
| 19 | `UPDT_TASK` | VARCHAR(50) |  |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Referenced by (64)

| From table | Column |
|------------|--------|
| [LH_E_AMI_METRICS](LH_E_AMI_METRICS.md) | `D_PRIN_DX_ID` |
| [LH_E_AMI_METRICS](LH_E_AMI_METRICS.md) | `HEALTH_SYSTEM_SOURCE_ID` |
| [LH_E_PN_METRICS](LH_E_PN_METRICS.md) | `D_PRIN_DX_ID` |
| [LH_E_PN_METRICS](LH_E_PN_METRICS.md) | `HEALTH_SYSTEM_SOURCE_ID` |
| [LH_F_ACT_INTOL_METRICS](LH_F_ACT_INTOL_METRICS.md) | `D_PRIN_DIAGNOSIS_ID` |
| [LH_F_ACT_INTOL_METRICS](LH_F_ACT_INTOL_METRICS.md) | `HEALTH_SYSTEM_SOURCE_ID` |
| [LH_F_AMI_METRICS](LH_F_AMI_METRICS.md) | `D_PRIN_DIAGNOSIS_ID` |
| [LH_F_AMI_METRICS](LH_F_AMI_METRICS.md) | `HEALTH_SYSTEM_SOURCE_ID` |
| [LH_F_ANEMIA_METRICS](LH_F_ANEMIA_METRICS.md) | `D_PRIN_DIAGNOSIS_ID` |
| [LH_F_ANEMIA_METRICS](LH_F_ANEMIA_METRICS.md) | `HEALTH_SYSTEM_SOURCE_ID` |
| [LH_F_CAC_METRICS](LH_F_CAC_METRICS.md) | `D_PRIN_DIAGNOSIS_ID` |
| [LH_F_CAC_METRICS](LH_F_CAC_METRICS.md) | `HEALTH_SYSTEM_SOURCE_ID` |
| [LH_F_CHF_METRICS](LH_F_CHF_METRICS.md) | `D_PRIN_DIAGNOSIS_ID` |
| [LH_F_CHF_METRICS](LH_F_CHF_METRICS.md) | `HEALTH_SYSTEM_SOURCE_ID` |
| [LH_F_DELIRIUM_METRICS](LH_F_DELIRIUM_METRICS.md) | `D_PRIN_DIAGNOSIS_ID` |
| [LH_F_DELIRIUM_METRICS](LH_F_DELIRIUM_METRICS.md) | `HEALTH_SYSTEM_SOURCE_ID` |
| [LH_F_DEPRESSION_METRICS](LH_F_DEPRESSION_METRICS.md) | `D_PRIN_DIAGNOSIS_ID` |
| [LH_F_DEPRESSION_METRICS](LH_F_DEPRESSION_METRICS.md) | `HEALTH_SYSTEM_SOURCE_ID` |
| [LH_F_DYSPHAGIA_METRICS](LH_F_DYSPHAGIA_METRICS.md) | `D_PRIN_DIAGNOSIS_ID` |
| [LH_F_DYSPHAGIA_METRICS](LH_F_DYSPHAGIA_METRICS.md) | `HEALTH_SYSTEM_SOURCE_ID` |
| [LH_F_FVE_METRICS](LH_F_FVE_METRICS.md) | `D_PRIN_DIAGNOSIS_ID` |
| [LH_F_FVE_METRICS](LH_F_FVE_METRICS.md) | `HEALTH_SYSTEM_SOURCE_ID` |
| [LH_F_GLYCEMIC_METRICS](LH_F_GLYCEMIC_METRICS.md) | `D_PRIN_DIAGNOSIS_ID` |
| [LH_F_GLYCEMIC_METRICS](LH_F_GLYCEMIC_METRICS.md) | `HEALTH_SYSTEM_SOURCE_ID` |
| [LH_F_HOP_AMI_METRICS](LH_F_HOP_AMI_METRICS.md) | `D_PRIN_DIAGNOSIS_ID` |
| [LH_F_HOP_AMI_METRICS](LH_F_HOP_AMI_METRICS.md) | `HEALTH_SYSTEM_SOURCE_ID` |
| [LH_F_HOP_SURG_METRICS](LH_F_HOP_SURG_METRICS.md) | `D_PRIN_DIAGNOSIS_ID` |
| [LH_F_HOP_SURG_METRICS](LH_F_HOP_SURG_METRICS.md) | `HEALTH_SYSTEM_SOURCE_ID` |
| [LH_F_IC_MDRO_METRICS](LH_F_IC_MDRO_METRICS.md) | `D_PRIN_DIAGNOSIS_ID` |
| [LH_F_IC_MDRO_METRICS](LH_F_IC_MDRO_METRICS.md) | `HEALTH_SYSTEM_SOURCE_ID` |
| [LH_F_LHHF_METRICS](LH_F_LHHF_METRICS.md) | `D_PRIN_DIAGNOSIS_ID` |
| [LH_F_LHHF_METRICS](LH_F_LHHF_METRICS.md) | `HEALTH_SYSTEM_SOURCE_ID` |
| [LH_F_LIPID_METRICS](LH_F_LIPID_METRICS.md) | `D_PRIN_DIAGNOSIS_ID` |
| [LH_F_LIPID_METRICS](LH_F_LIPID_METRICS.md) | `HEALTH_SYSTEM_SOURCE_ID` |
| [LH_F_MED_AD_METRICS](LH_F_MED_AD_METRICS.md) | `D_PRIN_DIAGNOSIS_ID` |
| [LH_F_MED_AD_METRICS](LH_F_MED_AD_METRICS.md) | `HEALTH_SYSTEM_SOURCE_ID` |
| [LH_F_MOD_SEDATION_METRICS](LH_F_MOD_SEDATION_METRICS.md) | `D_PRIN_DIAGNOSIS_ID` |
| [LH_F_MOD_SEDATION_METRICS](LH_F_MOD_SEDATION_METRICS.md) | `HEALTH_SYSTEM_SOURCE_ID` |
| [LH_F_NHIQM_VTE_METRICS](LH_F_NHIQM_VTE_METRICS.md) | `D_PRIN_DIAGNOSIS_ID` |
| [LH_F_NHIQM_VTE_METRICS](LH_F_NHIQM_VTE_METRICS.md) | `HEALTH_SYSTEM_SOURCE_ID` |
| [LH_F_PAIN_METRICS](LH_F_PAIN_METRICS.md) | `D_PRIN_DIAGNOSIS_ID` |
| [LH_F_PAIN_METRICS](LH_F_PAIN_METRICS.md) | `HEALTH_SYSTEM_SOURCE_ID` |
| [LH_F_PEDS_MED_AD_METRICS](LH_F_PEDS_MED_AD_METRICS.md) | `D_PRIN_DIAGNOSIS_ID` |
| [LH_F_PEDS_MED_AD_METRICS](LH_F_PEDS_MED_AD_METRICS.md) | `HEALTH_SYSTEM_SOURCE_ID` |
| [LH_F_PEDS_PAIN_METRICS](LH_F_PEDS_PAIN_METRICS.md) | `D_PRIN_DIAGNOSIS_ID` |
| [LH_F_PEDS_PAIN_METRICS](LH_F_PEDS_PAIN_METRICS.md) | `HEALTH_SYSTEM_SOURCE_ID` |
| [LH_F_PEDS_SKIN_METRICS](LH_F_PEDS_SKIN_METRICS.md) | `D_PRIN_DIAGNOSIS_ID` |
| [LH_F_PEDS_SKIN_METRICS](LH_F_PEDS_SKIN_METRICS.md) | `HEALTH_SYSTEM_SOURCE_ID` |
| [LH_F_PN_METRICS](LH_F_PN_METRICS.md) | `D_PRIN_DIAGNOSIS_ID` |
| [LH_F_PN_METRICS](LH_F_PN_METRICS.md) | `HEALTH_SYSTEM_SOURCE_ID` |
| [LH_F_READMIT_METRICS](LH_F_READMIT_METRICS.md) | `D_PRIN_DX_ID` |
| [LH_F_READMIT_METRICS](LH_F_READMIT_METRICS.md) | `HEALTH_SYSTEM_SOURCE_ID` |
| [LH_F_REST_METRICS](LH_F_REST_METRICS.md) | `D_PRIN_DIAGNOSIS_ID` |
| [LH_F_REST_METRICS](LH_F_REST_METRICS.md) | `HEALTH_SYSTEM_SOURCE_ID` |
| [LH_F_RRT_METRICS](LH_F_RRT_METRICS.md) | `D_PRIN_DIAGNOSIS_ID` |
| [LH_F_RRT_METRICS](LH_F_RRT_METRICS.md) | `HEALTH_SYSTEM_SOURCE_ID` |
| [LH_F_SCIP_METRICS](LH_F_SCIP_METRICS.md) | `D_PRIN_DIAGNOSIS_ID` |
| [LH_F_SCIP_METRICS](LH_F_SCIP_METRICS.md) | `HEALTH_SYSTEM_SOURCE_ID` |
| [LH_F_SEPSIS_METRICS](LH_F_SEPSIS_METRICS.md) | `D_PRIN_DIAGNOSIS_ID` |
| [LH_F_SEPSIS_METRICS](LH_F_SEPSIS_METRICS.md) | `HEALTH_SYSTEM_SOURCE_ID` |
| [LH_F_STROKE_METRICS](LH_F_STROKE_METRICS.md) | `D_PRIN_DIAGNOSIS_ID` |
| [LH_F_STROKE_METRICS](LH_F_STROKE_METRICS.md) | `HEALTH_SYSTEM_SOURCE_ID` |
| [LH_F_UI_METRICS](LH_F_UI_METRICS.md) | `D_PRIN_DIAGNOSIS_ID` |
| [LH_F_UI_METRICS](LH_F_UI_METRICS.md) | `HEALTH_SYSTEM_SOURCE_ID` |

