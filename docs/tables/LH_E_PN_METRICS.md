# LH_E_PN_METRICS

> This table is used to store Pneumonia metrics from the Lighthouse eMeasure. This table is at the encounter grain.

**Description:** LH_E_PN_METRICS  
**Table type:** ACTIVITY  
**Primary key:** _(not published — see note)_  
**Columns:** 139

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ACTIVE_IND` | DOUBLE | NOT NULL |  | The table row is active or inactive. A row is generally active unless it is in an inactive state such as logically deleted, combined away, pending purge, etc. |
| 2 | `ADMIT_DT_TM` | DATETIME |  |  | The date/time on which the patient was admitted |
| 3 | `ADMIT_SOURCE_FLAG` | DOUBLE |  |  | Identifies where the patient was transferred from |
| 4 | `ADMIT_UTC_DT_TM` | DATETIME |  |  | The date/time on which the patient was admitted normalized to GMT. |
| 5 | `ANY_INFECTION_DX_DT_TM` | DATETIME |  |  | Identifies the end date/time of the diagnosis of any infection on the encounter |
| 6 | `ANY_INFECTION_DX_UTC_DT_TM` | DATETIME |  |  | Identifies the end date/time of the diagnosis of any infection on the encounter normalized to GMT |
| 7 | `BRONCHIECTASIS_IND` | DOUBLE |  |  | Identifies if there is a diagnosis of bronchiectasis that occurred before the inpatient encounter started |
| 8 | `CHEST_CT_DT_TM` | DATETIME |  |  | Identifies the date/time of the chest CT |
| 9 | `CHEST_CT_NORMAL_DT_TM` | DATETIME |  |  | Identifies the date/time of the chest CT normal reading |
| 10 | `CHEST_CT_NORMAL_UTC_DT_TM` | DATETIME |  |  | Identifies the date/time of the chest CT normal reading normalized to GMT |
| 11 | `CHEST_CT_UTC_DT_TM` | DATETIME |  |  | Identifies the date/time of the chest CT normalized to GMT |
| 12 | `CHEST_XRAY_DT_TM` | DATETIME |  |  | Identifies the date/time of the chest X-Ray |
| 13 | `CHEST_XRAY_NORMAL_DT_TM` | DATETIME |  |  | Identifies the date/time of the chest X-Ray normal reading |
| 14 | `CHEST_XRAY_NORMAL_UTC_DT_TM` | DATETIME |  |  | Identifies the date/time of the chest X-Ray normal reading normalized to GMT |
| 15 | `CHEST_XRAY_UTC_DT_TM` | DATETIME |  |  | Identifies the date/time of the chest X-Ray normalized to GMT |
| 16 | `CHRONIC_BRONCHITIS_DX_IND` | DOUBLE |  |  | Identifies if there is a diagnosis of Chronic Bronchitis that occurred before the inpatient encounter started |
| 17 | `CLINICAL_TRIAL_IND` | DOUBLE |  |  | Identifies if the patient was enrolled in a clinical trial |
| 18 | `CMO_DT_TM` | DATETIME |  |  | Identifies the date/time of comfort measures only |
| 19 | `CMO_UTC_DT_TM` | DATETIME |  |  | Identifies the date/time of comfort measures only normalized to GMT |
| 20 | `COMM_MRN_TXT` | VARCHAR(50) |  |  | Identifies the community medical record number of the patient. |
| 21 | `COPD_DX_IND` | DOUBLE |  |  | Identifies if there is a diagnosis of COPD that occurred before the inpatient encounter started |
| 22 | `CORTICOSTEROIDS_DT_TM` | DATETIME |  |  | Identifies the first administration of IV, IM or PO corticosteroids |
| 23 | `CORTICOSTEROIDS_UTC_DT_TM` | DATETIME |  |  | Identifies the first administration of IV, IM or PO corticosteroids normalized to GMT |
| 24 | `CYSTIC_FIBROSIS_IND` | DOUBLE |  |  | Identifies if there is a diagnosis of cystic fibrosis |
| 25 | `DISCHARGE_DT_TM` | DATETIME |  |  | The date/time on which the patient was discharged. |
| 26 | `DISCHARGE_UTC_DT_TM` | DATETIME |  |  | The date/time on which the patient was discharged normalized to GMT. |
| 27 | `D_ADMIT_BUILDING_ID` | DOUBLE | NOT NULL | FK→ | The building to which the patient was admitted. |
| 28 | `D_ADMIT_FACILITY_ID` | DOUBLE | NOT NULL | FK→ | The facility to which the patient was admitted. |
| 29 | `D_ADMIT_NURSE_UNIT_ID` | DOUBLE | NOT NULL | FK→ | The nurse unit to which the patient was admitted. |
| 30 | `D_ADMIT_SRC_ID` | DOUBLE | NOT NULL | FK→ | Identifies the place from which the patient came before being admitted. |
| 31 | `D_ADMIT_TYPE_ID` | DOUBLE | NOT NULL | FK→ | Indicates the circumstances under which the patient was admitted. |
| 32 | `D_ATTEND_PRSNL_ID` | DOUBLE | NOT NULL | FK→ | Identifies the final attending physician associated to the encounter. |
| 33 | `D_BR_CCN_ID` | DOUBLE | NOT NULL | FK→ | CMS Certification Number. |
| 34 | `D_BR_HCO_ID` | DOUBLE | NOT NULL | FK→ | Healthcare organization Number. |
| 35 | `D_DISCHARGE_BUILDING_ID` | DOUBLE | NOT NULL | FK→ | The building from which the patient was discharged |
| 36 | `D_DISCHARGE_FACILITY_ID` | DOUBLE | NOT NULL | FK→ | The facility from which the patient was discharged |
| 37 | `D_DISCHARGE_NURSE_UNIT_ID` | DOUBLE | NOT NULL | FK→ | The nurse unit from which the patient was discharged |
| 38 | `D_DISCH_DISP_ID` | DOUBLE | NOT NULL | FK→ | Defines the discharge disposition of the encounter. |
| 39 | `D_ENCNTR_TYPE_ID` | DOUBLE | NOT NULL | FK→ | Categorizes the encounter into a logical group or type. |
| 40 | `D_MED_SERVICE_ID` | DOUBLE | NOT NULL | FK→ | The type or category of medical service that the patient is receiving in relation to their encounter. The category may be treatment type surgery general resources or others. |
| 41 | `D_METRIC_1_ID` | DOUBLE | NOT NULL | FK→ | Identifies the metric identifier for the Lighthouse metric |
| 42 | `D_METRIC_2_ID` | DOUBLE | NOT NULL | FK→ | Identifies the metric identifier for the Lighthouse metric |
| 43 | `D_PERSON_ID` | DOUBLE | NOT NULL | FK→ | The person that qualified for the quality metric. |
| 44 | `D_PRIN_DX_ID` | DOUBLE | NOT NULL | FK→ | Identifies the principal diagnosis code of the encounter |
| 45 | `ED_ARRIVAL_DT_TM` | DATETIME |  |  | Identifies when the patient arrived in the ED |
| 46 | `ED_ARRIVAL_UTC_DT_TM` | DATETIME |  |  | Identifies when the patient arrived in the ED normalized to GMT |
| 47 | `ED_DEPART_DT_TM` | DATETIME |  |  | Identifies when the patient left the ED |
| 48 | `ED_DEPART_UTC_DT_TM` | DATETIME |  |  | Identifies when the patient left the ED normalized to GMT |
| 49 | `ED_ENCNTR_ID` | DOUBLE | NOT NULL |  | Identifies the emergency encounter |
| 50 | `EMPHYSEMA_DX_IND` | DOUBLE |  |  | Identifies if there is a diagnosis of Emphysema that occurred before the inpatient encounter started |
| 51 | `ENCNTR_ID` | DOUBLE | NOT NULL |  | Identifies the encounter against which the quality measure is associated. Foreign key to the ENCOUNTER table. |
| 52 | `EXCLUDE_1_IND` | DOUBLE |  |  | Identifies if the encounter is considered Excluded for Population 1 |
| 53 | `EXCLUDE_2_IND` | DOUBLE |  |  | Identifies if the encounter is considered Excluded for Population 2 |
| 54 | `EXTRACT_DT_TM` | DATETIME |  |  | The date/time that the record was extracted from the source system. |
| 55 | `FINANCIAL_NBR_TXT` | VARCHAR(50) |  |  | The financial number alias associated to the encounter. |
| 56 | `FIRST_PROCESS_DT_TM` | DATETIME |  |  | The date/time the record was first loaded into the table. |
| 57 | `FRACISELLA_DX_DT_TM` | DATETIME |  |  | Identifies the date/time of the Fracisella diagnosis |
| 58 | `FRACISELLA_DX_UTC_DT_TM` | DATETIME |  |  | Identifies the date/time of the Fracisella diagnosis normalized to GMT |
| 59 | `HCAP_IND` | DOUBLE |  |  | Identifies if there is an active diagnosis of HCAP |
| 60 | `HEALTH_SYSTEM_ID` | DOUBLE | NOT NULL |  | Identifies the delivery network responsible for supplying the data. |
| 61 | `HEALTH_SYSTEM_SOURCE_ID` | DOUBLE | NOT NULL | FK→ | Identifies the unique source within the delivery network responsible for supplying the data. |
| 62 | `HEMO_PERI_DIALYSIS_IND` | DOUBLE |  |  | Identifies if there was a procedure performed: hemodialysis or peritoneal dialysis |
| 63 | `ICU_ARRIVAL_DT_TM` | DATETIME |  |  | Identifies when the patient arrived in the ICU |
| 64 | `ICU_ARRIVAL_UTC_DT_TM` | DATETIME |  |  | Identifies when the patient arrived in the ICU normalized to GMT |
| 65 | `ICU_DEPART_DT_TM` | DATETIME |  |  | Identifies when the patient left the ICU |
| 66 | `ICU_DEPART_UTC_DT_TM` | DATETIME |  |  | Identifies when the patient left the ICU normalized to GMT |
| 67 | `IMMUNOCOMPROMISED_COND_IND` | DOUBLE |  |  | Identifies if there is a diagnosis active for: Immunocompromised Conditions |
| 68 | `IMMUNOCOMPROMISED_THER_IND` | DOUBLE |  |  | Identifies if there is a diagnosis active for: Immunocompromised Therapies |
| 69 | `IMMUNODEFICIENT_COND_IND` | DOUBLE |  |  | Identifies if there is an active diagnosis of immunodeficient conditions |
| 70 | `IMMUNOSUPPRESSSIVE_MED_IND` | DOUBLE |  |  | Identifies if there is a medication active for Immunosuppressives |
| 71 | `INTERSTITIAL_LUNG_DX_IND` | DOUBLE |  |  | Identifies if there is a diagnosis of Interstitial Lung Disease that occurred before the inpatient encounter started |
| 72 | `IV_AMINOGLYCOSIDES_DT_TM` | DATETIME |  |  | Identifies the first administration of IV Aminoglycosides |
| 73 | `IV_AMINOGLYCOSIDES_UTC_DT_TM` | DATETIME |  |  | Identifies the first administration of IV Aminoglycosides normalized to GMT |
| 74 | `IV_ANTIPSEU_QUIN_DT_TM` | DATETIME |  |  | Identifies the first administration date/time of IV Antipseudomonal Quinolones |
| 75 | `IV_ANTIPSEU_QUIN_UTC_DT_TM` | DATETIME |  |  | Identifies the first administration date/time of IV Antipseudomonal Quinolones normalized to GMT |
| 76 | `IV_ANTIPSUEDOMONAL_DT_TM` | DATETIME |  |  | Identifies the first administration of IV Antipneumoccal/Antipseudomonal medications |
| 77 | `IV_ANTIPSUEDOMONAL_UTC_DT_TM` | DATETIME |  |  | Identifies the first administration of IV Antipneumoccal/Antipseudomonal medications normalized to GMT |
| 78 | `IV_BETA_LACTAM_DT_TM` | DATETIME |  |  | Identifies the first administration of IV beta lactam |
| 79 | `IV_BETA_LACTAM_UTC_DT_TM` | DATETIME |  |  | Identifies the first administration of IV beta lactam normalized to GMT |
| 80 | `IV_IM_AZTREONAM_DT_TM` | DATETIME |  |  | Identifies the first administration of IV/IM Beta Lactams |
| 81 | `IV_IM_AZTREONAM_UTC_DT_TM` | DATETIME |  |  | Identifies the first administration of IV/IM Beta Lactams normalized to GMT |
| 82 | `IV_IM_BETA_LACTAMS_DT_TM` | DATETIME |  |  | Identifies the first administration of IV/IM Beta Lactams |
| 83 | `IV_IM_BETA_LACTAMS_UTC_DT_TM` | DATETIME |  |  | Identifies the first administration of IV/IM Beta Lactams normalized to GMT |
| 84 | `IV_IM_PO_ANTIMIC_MED_DT_TM` | DATETIME |  |  | Identifies the date/time that IV/IM/PO Antimicrobial medication was administered |
| 85 | `IV_IM_PO_ANTIMIC_MED_UTC_DT_TM` | DATETIME |  |  | Identifies the date/time that IV/IM/PO Antimicrobial medication was administered normalized to GMT |
| 86 | `IV_MACROLIDES_DT_TM` | DATETIME |  |  | Identifies the first administration of IV Macrolides |
| 87 | `IV_MACROLIDES_UTC_DT_TM` | DATETIME |  |  | Identifies the first administration of IV Macrolides normalized to GMT |
| 88 | `IV_PO_LEVOFLOXACIN_DT_TM` | DATETIME |  |  | Identifies the first administration of IV/IM Beta Lactams |
| 89 | `IV_PO_LEVOFLOXACIN_UTC_DT_TM` | DATETIME |  |  | Identifies the first administration of IV/IM Beta Lactams normalized to GMT |
| 90 | `IV_PO_MACROLIDES_DT_TM` | DATETIME |  |  | Identifies the first administration of IV/PO Macrolides |
| 91 | `IV_PO_MACROLIDES_UTC_DT_TM` | DATETIME |  |  | Identifies the first administration of IV/PO Macrolides normalized to GMT |
| 92 | `IV_PO_QUINOLONES_DT_TM` | DATETIME |  |  | Identifies the first administration date/time of IV /PO Quinolones |
| 93 | `IV_PO_QUINOLONES_UTC_DT_TM` | DATETIME |  |  | Identifies the first administration date/time of IV/PO Quinolones normalized to GMT |
| 94 | `IV_PO_TETRACYCLINE_DT_TM` | DATETIME |  |  | Identifies the first administration of IV/PO tetracycline |
| 95 | `IV_PO_TETRACYCLINE_UTC_DT_TM` | DATETIME |  |  | Identifies the first administration of IV/PO tetracycline normalized to GMT |
| 96 | `IV_QUINOLONES_DT_TM` | DATETIME |  |  | Identifies the first administration of IV Quinolones |
| 97 | `IV_QUINOLONES_UTC_DT_TM` | DATETIME |  |  | Identifies the first administration of IV Quinolones normalized to GMT |
| 98 | `IV_TETRACYCLINE_DT_TM` | DATETIME |  |  | Identifies the first administration of IV tetracycline |
| 99 | `IV_TETRACYCLINE_UTC_DT_TM` | DATETIME |  |  | Identifies the first administration of IV tetracycline normalized to GMT |
| 100 | `IV_TIGECYCLINE_DT_TM` | DATETIME |  |  | Identifies the first administration of IV/IM Beta Lactams |
| 101 | `IV_TIGECYCLINE_UTC_DT_TM` | DATETIME |  |  | Identifies the first administration of IV/IM Beta Lactams normalized to GMT |
| 102 | `LAST_PROCESS_DT_TM` | DATETIME |  |  | The date/time the record was last loaded into the table. |
| 103 | `LH_E_PN_METRICS_ID` | DOUBLE | NOT NULL |  | Unique generated number that identifies a single row on the LH_E_PN_METRICS table. |
| 104 | `LOGICAL_DOMAIN_ID` | DOUBLE | NOT NULL |  | The unique identifier for a logical domain. This identifier allows the data to be grouped by logical domain. For example, if you assign clients a logical_domain_id, this would allow you to store data for multiple clients on this table. |
| 105 | `MED_ALLERGY_BETA_LACTAMS_IND` | DOUBLE |  |  | Identifies if the patient has a medication allergy to Beta Lactams |
| 106 | `NEUTROPHIL_500_IND` | DOUBLE |  |  | Identifies if there is a lab test >= 500 for Neutrophil Count |
| 107 | `NON_ICU_ARRIVAL_DT_TM` | DATETIME |  |  | Identifies when the patient arrived in a non-ICU location |
| 108 | `NON_ICU_ARRIVAL_UTC_DT_TM` | DATETIME |  |  | Identifies when the patient arrived in a non-ICU location normalized to GMT |
| 109 | `NON_ICU_DEPART_DT_TM` | DATETIME |  |  | Identifies when the patient left the non-ICU location |
| 110 | `NON_ICU_DEPART_UTC_DT_TM` | DATETIME |  |  | Identifies when the patient left the non-ICU location normalized to GMT |
| 111 | `NOT_IN_DEN_1_IND` | DOUBLE |  |  | Identifies if the encounter is considered Not In Denominator for Population 1 |
| 112 | `NOT_IN_DEN_2_IND` | DOUBLE |  |  | Identifies if the encounter is considered Not In Denominator for Population 2 |
| 113 | `NUMERATOR_1_IND` | DOUBLE |  |  | Identifies if the encounter is considered in the Numerator for Population 1 |
| 114 | `NUMERATOR_2_IND` | DOUBLE |  |  | Identifies if the encounter is considered in the Numerator for Population 2 |
| 115 | `ORGAN_TRANSPLANT_IND` | DOUBLE |  |  | Identifies if there was a procedure performed for Organ Transplant |
| 116 | `ORG_MRN_TXT` | VARCHAR(50) |  |  | Identifies the medical record number of the patient. |
| 117 | `PARTITION_DT_TM` | DATETIME |  |  | The date/time the encounter was discharged from the facility |
| 118 | `PAYER_CODE_TXT` | VARCHAR(20) | NOT NULL |  | identifies the payer code value that is associated to the patient for QRDA file payer information. |
| 119 | `PN_DX_IND` | DOUBLE |  |  | Identifies if the there was a diagnosis of Pneumonia on the encounter |
| 120 | `POPULATION_IND` | DOUBLE |  |  | Identifies if the patient is in the population for the Pneumonia Metric |
| 121 | `PRESUMPTIVE_PN_DX_DT_TM` | DATETIME |  |  | Identifies the date/time of a diagnosis of presumptive pneumonia |
| 122 | `PRESUMPTIVE_PN_DX_ED_IND` | DOUBLE |  |  | Identifies if the encounter had a presumptive PN diagnosis associated to the ED encounter. |
| 123 | `PRESUMPTIVE_PN_DX_INPT_IND` | DOUBLE |  |  | Identifies if the encounter had a presumptive PN diagnosis associated to the Inpatient encounter |
| 124 | `PRESUMPTIVE_PN_DX_UTC_DT_TM` | DATETIME |  |  | Identifies the date/time of a diagnosis of presumptive pneumonia normalized to GMT |
| 125 | `PRINCIPAL_PN_DX_IND` | DOUBLE |  |  | Identifies if the final, principal diagnosis for the encounter is Pneumonia |
| 126 | `PRINCIPAL_RESP_FAIL_DX_IND` | DOUBLE |  |  | Identifies if the final, principal diagnosis for the encounter is Respiratory Failure |
| 127 | `PRINCIPAL_SEPTICEMIA_DX_IND` | DOUBLE |  |  | Identifies if the final, principal diagnosis for the encounter is Septicemia |
| 128 | `PROLONGED_QT_DX_IND` | DOUBLE |  |  | Identifies if there is a diagnosis of prolonged QT on the encounter |
| 129 | `RESPIRATORY_INFECTION_DX_IND` | DOUBLE |  |  | Identifies if there is a diagnosis of respiratory infection on the encounter |
| 130 | `RESTRICTIVE_LUNG_DX_IND` | DOUBLE |  |  | Identifies if there is a diagnosis of Restrictive Lung Disease that occurred before the inpatient encounter started |
| 131 | `STRUCTURAL_LUNG_DX_IND` | DOUBLE |  |  | Identifies if there is a diagnosis of Structural Lung Disease that occurred before the inpatient encounter started |
| 132 | `SYSTEMIC_STERIOD_MED_IND` | DOUBLE |  |  | Identifies if there is a medication active for Systemic Steroids |
| 133 | `TRACHEOSTOMY_IND` | DOUBLE |  |  | Identifies if there was a procedure performed: tracheostomy |
| 134 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 135 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 136 | `UPDT_SOURCE` | VARCHAR(50) | NOT NULL |  | The script name responsible for updating the record. |
| 137 | `UPDT_TASK` | VARCHAR(50) | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |
| 138 | `VENTILATOR_IND` | DOUBLE |  |  | Identifies if there was a procedure performed: ventilator |
| 139 | `WOUND_CARE_IND` | DOUBLE |  |  | Identifies if there was a wound care intervention performed |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `D_ADMIT_BUILDING_ID` | [LH_D_BUILDING](LH_D_BUILDING.md) | `D_BUILDING_ID` |
| `D_ADMIT_FACILITY_ID` | [LH_D_FACILITY](LH_D_FACILITY.md) | `D_FACILITY_ID` |
| `D_ADMIT_NURSE_UNIT_ID` | [LH_D_NURSE_UNIT](LH_D_NURSE_UNIT.md) | `D_NURSE_UNIT_ID` |
| `D_ADMIT_SRC_ID` | [LH_D_ADMIT_SRC](LH_D_ADMIT_SRC.md) | `D_ADMIT_SRC_ID` |
| `D_ADMIT_TYPE_ID` | [LH_D_ADMIT_TYPE](LH_D_ADMIT_TYPE.md) | `D_ADMIT_TYPE_ID` |
| `D_ATTEND_PRSNL_ID` | [LH_D_PERSONNEL](LH_D_PERSONNEL.md) | `D_PRSNL_ID` |
| `D_BR_CCN_ID` | [LH_D_BR_CCN](LH_D_BR_CCN.md) | `D_BR_CCN_ID` |
| `D_BR_HCO_ID` | [LH_D_BR_HCO](LH_D_BR_HCO.md) | `D_BR_HCO_ID` |
| `D_DISCHARGE_BUILDING_ID` | [LH_D_BUILDING](LH_D_BUILDING.md) | `D_BUILDING_ID` |
| `D_DISCHARGE_FACILITY_ID` | [LH_D_FACILITY](LH_D_FACILITY.md) | `D_FACILITY_ID` |
| `D_DISCHARGE_NURSE_UNIT_ID` | [LH_D_NURSE_UNIT](LH_D_NURSE_UNIT.md) | `D_NURSE_UNIT_ID` |
| `D_DISCH_DISP_ID` | [LH_D_DISCH_DISP](LH_D_DISCH_DISP.md) | `D_DISCH_DISP_ID` |
| `D_ENCNTR_TYPE_ID` | [LH_D_ENCNTR_TYPE](LH_D_ENCNTR_TYPE.md) | `D_ENCNTR_TYPE_ID` |
| `D_MED_SERVICE_ID` | [LH_D_MED_SERVICE](LH_D_MED_SERVICE.md) | `D_MED_SERVICE_ID` |
| `D_METRIC_1_ID` | [LH_D_METRIC](LH_D_METRIC.md) | `D_METRIC_ID` |
| `D_METRIC_2_ID` | [LH_D_METRIC](LH_D_METRIC.md) | `D_METRIC_ID` |
| `D_PERSON_ID` | [LH_D_PERSON](LH_D_PERSON.md) | `D_PERSON_ID` |
| `D_PRIN_DX_ID` | [LH_D_DIAGNOSIS](LH_D_DIAGNOSIS.md) | `D_DIAGNOSIS_ID` |
| `HEALTH_SYSTEM_SOURCE_ID` | [LH_D_ADMIT_SRC](LH_D_ADMIT_SRC.md) | `HEALTH_SYSTEM_SOURCE_ID` |
| `HEALTH_SYSTEM_SOURCE_ID` | [LH_D_ADMIT_TYPE](LH_D_ADMIT_TYPE.md) | `HEALTH_SYSTEM_SOURCE_ID` |
| `HEALTH_SYSTEM_SOURCE_ID` | [LH_D_BR_CCN](LH_D_BR_CCN.md) | `HEALTH_SYSTEM_SOURCE_ID` |
| `HEALTH_SYSTEM_SOURCE_ID` | [LH_D_BR_HCO](LH_D_BR_HCO.md) | `HEALTH_SYSTEM_SOURCE_ID` |
| `HEALTH_SYSTEM_SOURCE_ID` | [LH_D_BUILDING](LH_D_BUILDING.md) | `HEALTH_SYSTEM_SOURCE_ID` |
| `HEALTH_SYSTEM_SOURCE_ID` | [LH_D_BUILDING](LH_D_BUILDING.md) | `HEALTH_SYSTEM_SOURCE_ID` |
| `HEALTH_SYSTEM_SOURCE_ID` | [LH_D_DIAGNOSIS](LH_D_DIAGNOSIS.md) | `HEALTH_SYSTEM_SOURCE_ID` |
| `HEALTH_SYSTEM_SOURCE_ID` | [LH_D_DISCH_DISP](LH_D_DISCH_DISP.md) | `HEALTH_SYSTEM_SOURCE_ID` |
| `HEALTH_SYSTEM_SOURCE_ID` | [LH_D_ENCNTR_TYPE](LH_D_ENCNTR_TYPE.md) | `HEALTH_SYSTEM_SOURCE_ID` |
| `HEALTH_SYSTEM_SOURCE_ID` | [LH_D_FACILITY](LH_D_FACILITY.md) | `HEALTH_SYSTEM_SOURCE_ID` |
| `HEALTH_SYSTEM_SOURCE_ID` | [LH_D_FACILITY](LH_D_FACILITY.md) | `HEALTH_SYSTEM_SOURCE_ID` |
| `HEALTH_SYSTEM_SOURCE_ID` | [LH_D_MED_SERVICE](LH_D_MED_SERVICE.md) | `HEALTH_SYSTEM_SOURCE_ID` |
| `HEALTH_SYSTEM_SOURCE_ID` | [LH_D_METRIC](LH_D_METRIC.md) | `HEALTH_SYSTEM_SOURCE_ID` |
| `HEALTH_SYSTEM_SOURCE_ID` | [LH_D_METRIC](LH_D_METRIC.md) | `HEALTH_SYSTEM_SOURCE_ID` |
| `HEALTH_SYSTEM_SOURCE_ID` | [LH_D_NURSE_UNIT](LH_D_NURSE_UNIT.md) | `HEALTH_SYSTEM_SOURCE_ID` |
| `HEALTH_SYSTEM_SOURCE_ID` | [LH_D_NURSE_UNIT](LH_D_NURSE_UNIT.md) | `HEALTH_SYSTEM_SOURCE_ID` |
| `HEALTH_SYSTEM_SOURCE_ID` | [LH_D_PERSON](LH_D_PERSON.md) | `HEALTH_SYSTEM_SOURCE_ID` |
| `HEALTH_SYSTEM_SOURCE_ID` | [LH_D_PERSONNEL](LH_D_PERSONNEL.md) | `HEALTH_SYSTEM_SOURCE_ID` |

