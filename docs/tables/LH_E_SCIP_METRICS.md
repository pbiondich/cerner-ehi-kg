# LH_E_SCIP_METRICS

> This table is used to store SCIP metrics from the Lighthouse eMeasure. This table is at the encounter grain.

**Description:** LH_E_SCIP_METRICS  
**Table type:** ACTIVITY  
**Primary key:** _(not published — see note)_  
**Columns:** 187

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ACH_DISCH_DT_TM` | DATETIME |  |  | Identifies the date/time that the patient was discharged from the acute care facility |
| 2 | `ACH_DISCH_UTC_DT_TM` | DATETIME |  |  | Identifies the date/time that the patient was discharged from the acute care facility normalized to GMT |
| 3 | `ACTIVE_IND` | DOUBLE |  |  | The table row is active or inactive. A row is generally active unless it is in an inactive state such as logically deleted, combined away, pending purge, etc. |
| 4 | `ACUTE_CARE_LOS_3_DAYS_IND` | DOUBLE |  |  | Identifies if the length of stay at the acute care facility was >= 3 days |
| 5 | `ADMIT_DT_TM` | DATETIME |  |  | The date/time on which the patient was admitted |
| 6 | `ADMIT_UTC_DT_TM` | DATETIME |  |  | The date/time on which the patient was admitted normalized to GMT. |
| 7 | `AMINOGLYCOSIDES_DT_TM` | DATETIME |  |  | Identifies the date/time that aminoglycosides were ordered |
| 8 | `AMINOGLYCOSIDES_UTC_DT_TM` | DATETIME |  |  | Identifies the date/time that aminoglycosides were ordered normalized to GMT |
| 9 | `ANESTHESIA_END_DT_TM` | DATETIME |  |  | Identifies the end date/time of anesthesia |
| 10 | `ANESTHESIA_END_UTC_DT_TM` | DATETIME |  |  | Identifies the end date/time of anesthesia normalized to GMT |
| 11 | `ANESTHESIA_PROC_DT_TM` | DATETIME |  |  | Identifies the date/time of the procedure that required anesthesia |
| 12 | `ANESTHESIA_PROC_UTC_DT_TM` | DATETIME |  |  | Identifies the date/time of the procedure that required anesthesia normalized to GMT |
| 13 | `ANESTHESIA_START_DT_TM` | DATETIME |  |  | Identifies the start date/time of anesthesia |
| 14 | `ANESTHESIA_START_UTC_DT_TM` | DATETIME |  |  | Identifies the start date/time of anesthesia normalized to GMT |
| 15 | `ANTIMIC_IV_IM_PO_DT_TM` | DATETIME |  |  | Identifies if the patient had an Antimicrobial medication administered via IV, IM or PO |
| 16 | `ANTIMIC_IV_IM_PO_UTC_DT_TM` | DATETIME |  |  | Identifies if the patient had an Antimicrobial medication administered via IV, IM or PO normalized to GMT |
| 17 | `AZTREONAM_DT_TM` | DATETIME |  |  | Identifies the date/time that aztreonam was ordered |
| 18 | `AZTREONAM_UTC_DT_TM` | DATETIME |  |  | Identifies the date/time that aminoglycosides were ordered normalized to GMT |
| 19 | `BETA_LACTAM_ALLERGY_IND` | DOUBLE |  |  | Identifies if there is a documented allergy for beta lactams |
| 20 | `CARDIAC_VALVE_SURGERY_IND` | DOUBLE |  |  | Identifies if there was a cardiac valve surgery during the inpatient encounter |
| 21 | `CARDIC_VASCULAR_ABX_DT_TM` | DATETIME |  |  | Identifies the date/time that cardiac or vascular antibiotics were ordered |
| 22 | `CARDIC_VASCULAR_ABX_UTC_DT_TM` | DATETIME |  |  | Identifies the date/time that cardiac or vascular antibiotics were ordered normalized to GMT |
| 23 | `CATH_REMOVE_DT_TM` | DATETIME |  |  | Identifies the start date/time of a suprapubic catheter |
| 24 | `CATH_REMOVE_UTC_DT_TM` | DATETIME |  |  | Identifies the start date/time of a suprapubic catheter normalized to GMT |
| 25 | `CHRONIC_WOUND_CARE_IND` | DOUBLE |  |  | Identifies if there is an intervention performed for Chronic Wound Care |
| 26 | `CLINDAMYCIN_DT_TM` | DATETIME |  |  | Identifies the date/time that clindamycin was ordered |
| 27 | `CLINDAMYCIN_UTC_DT_TM` | DATETIME |  |  | Identifies the date/time that clindamycin was ordered normalized to GMT |
| 28 | `CLINICAL_TRIAL_IND` | DOUBLE |  |  | Identifies if the patient is a clinical trial participant |
| 29 | `COMM_MRN_TXT` | VARCHAR(50) |  |  | Identifies the community medical record number of the patient. |
| 30 | `DEFIB_DEVICE_DT_TM` | DATETIME |  |  | Identifies the date/time that the pacemaker or implantable defibrillator device was applied |
| 31 | `DEFIB_DEVICE_UTC_DT_TM` | DATETIME |  |  | Identifies the date/time that the pacemaker or implantable defibrillator device was applied normalized to GMT |
| 32 | `DEFIB_PROC_DT_TM` | DATETIME |  |  | Identifies the date/time that the pacemaker or implantable defibrillator procedure was performed |
| 33 | `DEFIB_PROC_UTC_DT_TM` | DATETIME |  |  | Identifies the date/time that the pacemaker or implantable defibrillator procedure was performed normalized to GMT |
| 34 | `DISCHARGE_DT_TM` | DATETIME |  |  | The date/time on which the patient was discharged. |
| 35 | `DISCHARGE_UTC_DT_TM` | DATETIME |  |  | The date/time on which the patient was discharged normalized to GMT. |
| 36 | `DIURETICS_IND` | DOUBLE |  |  | Identifies if the patient had diuretics ordered within 2 days of SCIP major surgery |
| 37 | `D_ADMIT_BUILDING_ID` | DOUBLE | NOT NULL | FK→ | The building to which the patient was admitted. |
| 38 | `D_ADMIT_FACILITY_ID` | DOUBLE | NOT NULL | FK→ | The facility to which the patient was admitted. |
| 39 | `D_ADMIT_NURSE_UNIT_ID` | DOUBLE | NOT NULL | FK→ | The nurse unit to which the patient was admitted. |
| 40 | `D_ADMIT_SRC_ID` | DOUBLE | NOT NULL | FK→ | Identifies the place from which the patient came before being admitted. |
| 41 | `D_ADMIT_TYPE_ID` | DOUBLE | NOT NULL | FK→ | Indicates the circumstances under which the patient was admitted. |
| 42 | `D_ATTEND_PRSNL_ID` | DOUBLE | NOT NULL | FK→ | Identifies the final attending physician associated to the encounter. |
| 43 | `D_BR_CCN_ID` | DOUBLE | NOT NULL | FK→ | CMS Certification Number. |
| 44 | `D_BR_HCO_ID` | DOUBLE | NOT NULL | FK→ | Healthcare organization Number. |
| 45 | `D_DISCHARGE_BUILDING_ID` | DOUBLE | NOT NULL | FK→ | The building from which the patient was discharged |
| 46 | `D_DISCHARGE_FACILITY_ID` | DOUBLE | NOT NULL | FK→ | The facility from which the patient was discharged |
| 47 | `D_DISCHARGE_NURSE_UNIT_ID` | DOUBLE | NOT NULL | FK→ | The nurse unit from which the patient was discharged |
| 48 | `D_DISCH_DISP_ID` | DOUBLE | NOT NULL | FK→ | Defines the discharge disposition of the encounter. |
| 49 | `D_ENCNTR_TYPE_ID` | DOUBLE | NOT NULL | FK→ | Categorizes the encounter into a logical group or type. |
| 50 | `D_MED_SERVICE_ID` | DOUBLE | NOT NULL | FK→ | The type or category of medical service that the patient is receiving in relation to their encounter. The category may be treatment type surgery general resources or others. |
| 51 | `D_METRIC_1_ID` | DOUBLE | NOT NULL | FK→ | Identifies the metric identifier for the Lighthouse metric |
| 52 | `D_METRIC_2_ID` | DOUBLE | NOT NULL | FK→ | Identifies the metric identifier for the Lighthouse metric |
| 53 | `D_METRIC_3_ID` | DOUBLE | NOT NULL | FK→ | Identifies the metric identifier for the Lighthouse metric |
| 54 | `D_METRIC_4_ID` | DOUBLE | NOT NULL | FK→ | Identifies the metric identifier for the Lighthouse metric |
| 55 | `D_PERSON_ID` | DOUBLE | NOT NULL | FK→ | The person that qualified for the quality metric. |
| 56 | `ENCNTR_ID` | DOUBLE | NOT NULL |  | Identifies the encounter against which the quality measure is associated. Foreign key to the ENCOUNTER table. |
| 57 | `ERYTHROMYCIN_DT_TM` | DATETIME |  |  | Identifies the date/time that ERYTHROMYCIN was ordered |
| 58 | `ERYTHROMYCIN_UTC_DT_TM` | DATETIME |  |  | Identifies the date/time that aminoglycosides were ordered normalized to GMT |
| 59 | `EXCLUDE_9_IND` | DOUBLE | NOT NULL |  | Identifies if the encounter is Excluded for Inf-9 |
| 60 | `EXCLUDE_INF_1_1_IND` | DOUBLE | NOT NULL |  | Identifies if the encounter is excluded for Inf-1 Subpopulation 1 |
| 61 | `EXCLUDE_INF_1_2_IND` | DOUBLE | NOT NULL |  | Identifies if the encounter is excluded for Inf-1 Subpopulation 2 |
| 62 | `EXCLUDE_INF_1_3_IND` | DOUBLE | NOT NULL |  | Identifies if the encounter is excluded for Inf-1 Subpopulation 3 |
| 63 | `EXCLUDE_INF_1_4_IND` | DOUBLE | NOT NULL |  | Identifies if the encounter is excluded for Inf-1 Subpopulation 4 |
| 64 | `EXCLUDE_INF_1_5_IND` | DOUBLE | NOT NULL |  | Identifies if the encounter is excluded for Inf-1 Subpopulation 5 |
| 65 | `EXCLUDE_INF_1_6_IND` | DOUBLE | NOT NULL |  | Identifies if the encounter is excluded for Inf-1 Subpopulation 6 |
| 66 | `EXCLUDE_INF_1_7_IND` | DOUBLE | NOT NULL |  | Identifies if the encounter is excluded for Inf-1 Subpopulation 7 |
| 67 | `EXCLUDE_INF_1_8_IND` | DOUBLE | NOT NULL |  | Identifies if the encounter is excluded for Inf-1 Subpopulation 8 |
| 68 | `EXCLUDE_INF_2_1_IND` | DOUBLE | NOT NULL |  | Identifies if the encounter is excluded for Inf-2 Subpopulation 1 |
| 69 | `EXCLUDE_INF_2_2_IND` | DOUBLE | NOT NULL |  | Identifies if the encounter is excluded for Inf-2 Subpopulation 2 |
| 70 | `EXCLUDE_INF_2_3_IND` | DOUBLE | NOT NULL |  | Identifies if the encounter is excluded for Inf-2 Subpopulation 3 |
| 71 | `EXCLUDE_INF_2_4_IND` | DOUBLE | NOT NULL |  | Identifies if the encounter is excluded for Inf-2 Subpopulation 4 |
| 72 | `EXCLUDE_INF_2_5_IND` | DOUBLE | NOT NULL |  | Identifies if the encounter is excluded for Inf-2 Subpopulation 5 |
| 73 | `EXCLUDE_INF_2_6_IND` | DOUBLE | NOT NULL |  | Identifies if the encounter is excluded for Inf-2 Subpopulation 6 |
| 74 | `EXCLUDE_INF_2_7_IND` | DOUBLE | NOT NULL |  | Identifies if the encounter is excluded for Inf-2 Subpopulation 7 |
| 75 | `EXCLUDE_INF_2_8_IND` | DOUBLE | NOT NULL |  | Identifies if the encounter is excluded for Inf-2 Subpopulation 8 |
| 76 | `EXPIRED_DT_TM` | DATETIME |  |  | Identifies the date/time that the patient expired |
| 77 | `EXPIRED_UTC_DT_TM` | DATETIME |  |  | Identifies the date/time that the patient expired normalized to GMT |
| 78 | `EXTRACT_DT_TM` | DATETIME |  |  | The date/time that the record was extracted from the source system. |
| 79 | `FINANCIAL_NBR_TXT` | VARCHAR(50) |  |  | The financial number alias associated to the encounter. |
| 80 | `FIRST_PROCESS_DT_TM` | DATETIME |  |  | The date/time the record was first loaded into the table. |
| 81 | `GEN_NEURAXIAL_IND` | DOUBLE |  |  | Identifies if there was evidence of a surgery procedure requiring general or neuraxial anesthesia |
| 82 | `HEALTH_SYSTEM_ID` | DOUBLE | NOT NULL |  | Identifies the delivery network responsible for supplying the data. |
| 83 | `HEALTH_SYSTEM_SOURCE_ID` | DOUBLE | NOT NULL | FK→ | Identifies the unique source within the delivery network responsible for supplying the data. |
| 84 | `HEMO_PERI_DIALYSIS_IND` | DOUBLE |  |  | Identifies if the patient has had a procedure of Hemodialysis or Peritoneal Dialysis within 1 year of the procedure |
| 85 | `HYSTERECTOMY_ABX_DT_TM` | DATETIME |  |  | Identifies the date/time that hysterectomy antibiotics were ordered |
| 86 | `HYSTERECTOMY_ABX_UTC_DT_TM` | DATETIME |  |  | Identifies the date/time that hysterectomy antibiotics were ordered normalized to GMT |
| 87 | `HYST_QUINOLONES_DT_TM` | DATETIME |  |  | Identifies the date/time that hysterectomy/colon quinolones were ordered |
| 88 | `HYST_QUINOLONES_UTC_DT_TM` | DATETIME |  |  | Identifies the date/time that hysterectomy/colon quinolones were ordered normalized to GMT |
| 89 | `ICU_LOC_IND` | DOUBLE |  |  | Identifies if the patient was in an ICU location within 2 days of having SCIP Major Surgery |
| 90 | `INDWELL_CATH_END_DT_TM` | DATETIME |  |  | Identifies the end date/time of the indwelling urinary catheter |
| 91 | `INDWELL_CATH_END_UTC_DT_TM` | DATETIME |  |  | Identifies the end date/time of the indwelling urinary catheter normalized to GMT |
| 92 | `INDWELL_CATH_START_DT_TM` | DATETIME |  |  | Identifies the start date/time of the indwelling urinary catheter |
| 93 | `INDWELL_CATH_START_UTC_DT_TM` | DATETIME |  |  | Identifies the start date/time of the indwelling urinary catheter normalized to GMT |
| 94 | `INFECTION_DX_DT_TM` | DATETIME |  |  | Identifies the date/time of the diagnosis of any infection |
| 95 | `INFECTION_DX_UTC_DT_TM` | DATETIME |  |  | Identifies the date/time of the diagnosis of any infection normalized to GMT |
| 96 | `INOTROPIC_IND` | DOUBLE |  |  | Identifies if the patient had inotropic and vasopressor agents given within 2 days of SCIP major surgery |
| 97 | `INTERMITTENT_CATH_DT_TM` | DATETIME |  |  | Identifies the start date/time of an intermittent catheter |
| 98 | `INTERMITTENT_CATH_UTC_DT_TM` | DATETIME |  |  | Identifies the start date/time of an intermittent catheter normalized to GMT |
| 99 | `IV_ANTIMICROBIAL_DT_TM` | DATETIME |  |  | Identifies the date/time that IV Antimicrobial were ordered |
| 100 | `IV_ANTIMICROBIAL_UTC_DT_TM` | DATETIME |  |  | Identifies the date/time that IV Antimicrobial were ordered normalized to GMT |
| 101 | `IV_ARTH_COLON_ABX_DT_TM` | DATETIME |  |  | Identifies the date/time that IV Arthroplasty/Colon Antibiotics was ordered |
| 102 | `IV_ARTH_COLON_ABX_UTC_DT_TM` | DATETIME |  |  | Identifies the date/time that IV Arthroplasty/Colon Antibiotics was ordered normalized to GMT |
| 103 | `IV_COLON_ABX_DT_TM` | DATETIME |  |  | Identifies the date/time that IV Colon Antibiotics was ordered |
| 104 | `IV_COLON_ABX_UTC_DT_TM` | DATETIME |  |  | Identifies the date/time that IV Colon Antibiotics was ordered normalized to GMT |
| 105 | `IV_ERTAPENEM_ABX_DT_TM` | DATETIME |  |  | Identifies the date/time that IV Ertapenem was ordered |
| 106 | `IV_ERTAPENEM_ABX_UTC_DT_TM` | DATETIME |  |  | Identifies the date/time that IV Ertapenem was ordered normalized to GMT |
| 107 | `IV_METRONIDAZOLE_DT_TM` | DATETIME |  |  | Identifies the date/time that IV metronidazole was ordered |
| 108 | `IV_METRONIDAZOLE_UTC_DT_TM` | DATETIME |  |  | Identifies the date/time that IV metronidazole was ordered normalized to GMT |
| 109 | `LAST_PROCESS_DT_TM` | DATETIME |  |  | The date/time the record was last loaded into the table. |
| 110 | `LH_E_SCIP_METRICS_ID` | DOUBLE | NOT NULL |  | Unique generated number that identifies a single row on the LH_E_SCIP_METRICS table. |
| 111 | `LOGICAL_DOMAIN_ID` | DOUBLE | NOT NULL |  | The unique identifier for a logical domain. This identifier allows the data to be grouped by logical domain. For example, if you assign clients a logical_domain_id, this would allow you to store data for multiple clients on this table. |
| 112 | `MRSA_DX_IND` | DOUBLE |  |  | Identifies if there is an active diagnosis of MRSA colonization or infection |
| 113 | `NEOMYCIN_DT_TM` | DATETIME |  |  | Identifies the date/time that NEOMYCIN was ordered |
| 114 | `NEOMYCIN_UTC_DT_TM` | DATETIME |  |  | Identifies the date/time that aminoglycosides were ordered normalized to GMT |
| 115 | `NOT_IN_DEN_INF_1_1_IND` | DOUBLE | NOT NULL |  | Identifies if the encounter is not in denominator for Inf-1 Subpopulation 1 |
| 116 | `NOT_IN_DEN_INF_1_2_IND` | DOUBLE | NOT NULL |  | Identifies if the encounter is not in denominator for Inf-1 Subpopulation 2 |
| 117 | `NOT_IN_DEN_INF_1_3_IND` | DOUBLE | NOT NULL |  | Identifies if the encounter is not in denominator for Inf-1 Subpopulation 3 |
| 118 | `NOT_IN_DEN_INF_1_4_IND` | DOUBLE | NOT NULL |  | Identifies if the encounter is not in denominator for Inf-1 Subpopulation 4 |
| 119 | `NOT_IN_DEN_INF_1_5_IND` | DOUBLE | NOT NULL |  | Identifies if the encounter is not in denominator for Inf-1 Subpopulation 5 |
| 120 | `NOT_IN_DEN_INF_1_6_IND` | DOUBLE | NOT NULL |  | Identifies if the encounter is not in denominator for Inf-1 Subpopulation 6 |
| 121 | `NOT_IN_DEN_INF_1_7_IND` | DOUBLE | NOT NULL |  | Identifies if the encounter is not in denominator for Inf-1 Subpopulation 7 |
| 122 | `NOT_IN_DEN_INF_1_8_IND` | DOUBLE | NOT NULL |  | Identifies if the encounter is not in denominator for Inf-1 Subpopulation 8 |
| 123 | `NOT_IN_DEN_INF_2_1_IND` | DOUBLE | NOT NULL |  | Identifies if the encounter is not in denominator for Inf-2 Subpopulation 1 |
| 124 | `NOT_IN_DEN_INF_2_2_IND` | DOUBLE | NOT NULL |  | Identifies if the encounter is not in denominator for Inf-2 Subpopulation 2 |
| 125 | `NOT_IN_DEN_INF_2_3_IND` | DOUBLE | NOT NULL |  | Identifies if the encounter is not in denominator for Inf-2 Subpopulation 3 |
| 126 | `NOT_IN_DEN_INF_2_4_IND` | DOUBLE | NOT NULL |  | Identifies if the encounter is not in denominator for Inf-2 Subpopulation 4 |
| 127 | `NOT_IN_DEN_INF_2_5_IND` | DOUBLE | NOT NULL |  | Identifies if the encounter is not in denominator for Inf-2 Subpopulation 5 |
| 128 | `NOT_IN_DEN_INF_2_6_IND` | DOUBLE | NOT NULL |  | Identifies if the encounter is not in denominator for Inf-2 Subpopulation 6 |
| 129 | `NOT_IN_DEN_INF_2_7_IND` | DOUBLE | NOT NULL |  | Identifies if the encounter is not in denominator for Inf-2 Subpopulation 7 |
| 130 | `NOT_IN_DEN_INF_2_8_IND` | DOUBLE | NOT NULL |  | Identifies if the encounter is not in denominator for Inf-2 Subpopulation 8 |
| 131 | `NOT_IN_DEN_INF_9_IND` | DOUBLE | NOT NULL |  | Identifies if the encounter is Not in Denominator for Inf-9 |
| 132 | `NO_CATH_MED_REASON_DT_TM` | DATETIME |  |  | Identifies when it was documented that a catheter wasn't given due to a medical reason |
| 133 | `NO_CATH_MED_REASON_UTC_DT_TM` | DATETIME |  |  | Identifies when it was documented that a catheter wasn't given due to a medical reason normalized to GMT |
| 134 | `NUMERATOR_9_IND` | DOUBLE | NOT NULL |  | Identifies if the encounter is in the numerator for Inf-9 |
| 135 | `NUMERATOR_INF_1_1_IND` | DOUBLE | NOT NULL |  | Identifies if the encounter is in the numerator for Inf-1 Subpopulation 1 |
| 136 | `NUMERATOR_INF_1_2_IND` | DOUBLE | NOT NULL |  | Identifies if the encounter is in the numerator for Inf-1 Subpopulation 2 |
| 137 | `NUMERATOR_INF_1_3_IND` | DOUBLE | NOT NULL |  | Identifies if the encounter is in the numerator for Inf-1 Subpopulation 3 |
| 138 | `NUMERATOR_INF_1_4_IND` | DOUBLE | NOT NULL |  | Identifies if the encounter is in the numerator for Inf-1 Subpopulation 4 |
| 139 | `NUMERATOR_INF_1_5_IND` | DOUBLE | NOT NULL |  | Identifies if the encounter is in the numerator for Inf-1 Subpopulation 5 |
| 140 | `NUMERATOR_INF_1_6_IND` | DOUBLE | NOT NULL |  | Identifies if the encounter is in the numerator for Inf-1 Subpopulation 6 |
| 141 | `NUMERATOR_INF_1_7_IND` | DOUBLE | NOT NULL |  | Identifies if the encounter is in the numerator for Inf-1 Subpopulation 7 |
| 142 | `NUMERATOR_INF_1_8_IND` | DOUBLE | NOT NULL |  | Identifies if the encounter is in the numerator for Inf-1 Subpopulation 8 |
| 143 | `NUMERATOR_INF_2_1_IND` | DOUBLE | NOT NULL |  | Identifies if the encounter is in the numerator for Inf-2 Subpopulation 1 |
| 144 | `NUMERATOR_INF_2_2_IND` | DOUBLE | NOT NULL |  | Identifies if the encounter is in the numerator for Inf-2 Subpopulation 2 |
| 145 | `NUMERATOR_INF_2_3_IND` | DOUBLE | NOT NULL |  | Identifies if the encounter is in the numerator for Inf-2 Subpopulation 3 |
| 146 | `NUMERATOR_INF_2_4_IND` | DOUBLE | NOT NULL |  | Identifies if the encounter is in the numerator for Inf-2 Subpopulation 4 |
| 147 | `NUMERATOR_INF_2_5_IND` | DOUBLE | NOT NULL |  | Identifies if the encounter is in the numerator for Inf-2 Subpopulation 5 |
| 148 | `NUMERATOR_INF_2_6_IND` | DOUBLE | NOT NULL |  | Identifies if the encounter is in the numerator for Inf-2 Subpopulation 6 |
| 149 | `NUMERATOR_INF_2_7_IND` | DOUBLE | NOT NULL |  | Identifies if the encounter is in the numerator for Inf-2 Subpopulation 7 |
| 150 | `NUMERATOR_INF_2_8_IND` | DOUBLE | NOT NULL |  | Identifies if the encounter is in the numerator for Inf-2 Subpopulation 8 |
| 151 | `NURSING_HOME_DISCH_DT_TM` | DATETIME |  |  | Identifies the date/time that the patient was discharged from a nursing home or extended care facility |
| 152 | `NURSING_HOME_DISCH_UTC_DT_TM` | DATETIME |  |  | Identifies the date/time that the patient was discharged from a nursing home or extended care facility normalized to GMT |
| 153 | `NURSING_HOME_IND` | DOUBLE |  |  | Identifies if the admission source for the encounter was a nursing home or extended care facility |
| 154 | `ORAL_METRONIDAZOLE_DT_TM` | DATETIME |  |  | Identifies the date/time that ORAL_METRONIDAZOLE was ordered |
| 155 | `ORAL_METRONIDAZOLE_UTC_DT_TM` | DATETIME |  |  | Identifies the date/time that aminoglycosides were ordered normalized to GMT |
| 156 | `ORG_MRN_TXT` | VARCHAR(50) |  |  | Identifies the medical record number of the patient. |
| 157 | `PARALYTIC_AGENT_IND` | DOUBLE |  |  | Identifies if the patient had paralytic agents given within 2 days of SCIP major surgery |
| 158 | `PARTITION_DT_TM` | DATETIME |  |  | The date/time the encounter was discharged from the facility |
| 159 | `PAYER_CODE_TXT` | VARCHAR(20) |  |  | identifies the payer code value that is associated to the patient for QRDA file payer information. |
| 160 | `PHYSICAN_REQUEST_IND` | DOUBLE |  |  | Identifies if vancoymicin was ordered at the request of a physician |
| 161 | `POPULATION_IND` | DOUBLE |  |  | Identifies if the patient is in the population for the SCIP Metric |
| 162 | `PRINCIPAL_PROC_FLAG` | DOUBLE | NOT NULL |  | Identifies the principal procedure during the inpatient encounter |
| 163 | `PRIN_DX_INFECTION_IND` | DOUBLE |  |  | Identifies if the principal diagnosis was infection |
| 164 | `PRIN_PROC_CSECTION_IND` | DOUBLE |  |  | Identifies if the principal procedure performed during the inpatient encounter was a C-Section |
| 165 | `PRIOR_INPT_1_YEAR_IND` | DOUBLE |  |  | Identifies if the patient has had an inpatient encounter within the previous year |
| 166 | `PROCEDURE_DT_TM` | DATETIME |  |  | Identifies when the procedure started |
| 167 | `PROCEDURE_UTC_DT_TM` | DATETIME |  |  | Identifies when the procedure started normalized to GMT |
| 168 | `QUINOLONES_DT_TM` | DATETIME |  |  | Identifies the date/time that quinolones were ordered |
| 169 | `QUINOLONES_UTC_DT_TM` | DATETIME |  |  | Identifies the date/time that quinolones were ordered normalized to GMT |
| 170 | `SCIP_MAJOR_SURG_IND` | DOUBLE |  |  | Identifies if the principal procedure performed during the encounter was a SCIP Major Surgical Procedure |
| 171 | `SUPRAPUBIC_CATH_DT_TM` | DATETIME |  |  | Identifies the start date/time of a suprapubic catheter |
| 172 | `SUPRAPUBIC_CATH_UTC_DT_TM` | DATETIME |  |  | Identifies the start date/time of a suprapubic catheter normalized to GMT |
| 173 | `SURGERY_END_DT_TM` | DATETIME |  |  | Identifies when surgery ended |
| 174 | `SURGERY_END_UTC_DT_TM` | DATETIME |  |  | Identifies when surgery ended normalized to GMT |
| 175 | `SURGERY_START_DT_TM` | DATETIME |  |  | Identifies when surgery started |
| 176 | `SURGERY_START_UTC_DT_TM` | DATETIME |  |  | Identifies when surgery started normalized to GMT |
| 177 | `TRANS_FROM_ACUTE_CARE_IND` | DOUBLE |  |  | Identifies if the patient was transferred from an Acute Care Hospital |
| 178 | `UPDT_CNT` | DOUBLE |  |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 179 | `UPDT_DT_TM` | DATETIME |  |  | The date and time the row was last inserted or updated. |
| 180 | `UPDT_SOURCE` | VARCHAR(50) |  |  | The script name responsible for updating the record. |
| 181 | `UPDT_TASK` | VARCHAR(50) |  |  | The registered (assigned) task number for the process that inserted or updated the row. |
| 182 | `URETHRA_IND` | DOUBLE |  |  | Identifies if the anatomical structure was urethra for the catheter |
| 183 | `URINARY_DIVERSION_IND` | DOUBLE |  |  | Identifies if there was a finding of urinary division during a physical exam more than 1 minute after surgery started |
| 184 | `URINARY_DIVERSION_PROC_IND` | DOUBLE |  |  | Identifies if there was a procedure for urinary diversion |
| 185 | `URO_PROC_IND` | DOUBLE |  |  | Identifies if the principal procedure during the inpatient encounter was a urological procedure with need for a catheter |
| 186 | `VANCOMYCIN_DT_TM` | DATETIME |  |  | Identifies the date/time that vancomycin were ordered |
| 187 | `VANCOMYCIN_UTC_DT_TM` | DATETIME |  |  | Identifies the date/time that vancomycin were ordered normalized to GMT |

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
| `D_METRIC_3_ID` | [LH_D_METRIC](LH_D_METRIC.md) | `D_METRIC_ID` |
| `D_METRIC_4_ID` | [LH_D_METRIC](LH_D_METRIC.md) | `D_METRIC_ID` |
| `D_PERSON_ID` | [LH_D_PERSON](LH_D_PERSON.md) | `D_PERSON_ID` |
| `HEALTH_SYSTEM_SOURCE_ID` | [LH_D_ADMIT_SRC](LH_D_ADMIT_SRC.md) | `HEALTH_SYSTEM_SOURCE_ID` |
| `HEALTH_SYSTEM_SOURCE_ID` | [LH_D_ADMIT_TYPE](LH_D_ADMIT_TYPE.md) | `HEALTH_SYSTEM_SOURCE_ID` |
| `HEALTH_SYSTEM_SOURCE_ID` | [LH_D_BR_CCN](LH_D_BR_CCN.md) | `HEALTH_SYSTEM_SOURCE_ID` |
| `HEALTH_SYSTEM_SOURCE_ID` | [LH_D_BR_HCO](LH_D_BR_HCO.md) | `HEALTH_SYSTEM_SOURCE_ID` |
| `HEALTH_SYSTEM_SOURCE_ID` | [LH_D_BUILDING](LH_D_BUILDING.md) | `HEALTH_SYSTEM_SOURCE_ID` |
| `HEALTH_SYSTEM_SOURCE_ID` | [LH_D_BUILDING](LH_D_BUILDING.md) | `HEALTH_SYSTEM_SOURCE_ID` |
| `HEALTH_SYSTEM_SOURCE_ID` | [LH_D_DISCH_DISP](LH_D_DISCH_DISP.md) | `HEALTH_SYSTEM_SOURCE_ID` |
| `HEALTH_SYSTEM_SOURCE_ID` | [LH_D_ENCNTR_TYPE](LH_D_ENCNTR_TYPE.md) | `HEALTH_SYSTEM_SOURCE_ID` |
| `HEALTH_SYSTEM_SOURCE_ID` | [LH_D_FACILITY](LH_D_FACILITY.md) | `HEALTH_SYSTEM_SOURCE_ID` |
| `HEALTH_SYSTEM_SOURCE_ID` | [LH_D_FACILITY](LH_D_FACILITY.md) | `HEALTH_SYSTEM_SOURCE_ID` |
| `HEALTH_SYSTEM_SOURCE_ID` | [LH_D_MED_SERVICE](LH_D_MED_SERVICE.md) | `HEALTH_SYSTEM_SOURCE_ID` |
| `HEALTH_SYSTEM_SOURCE_ID` | [LH_D_METRIC](LH_D_METRIC.md) | `HEALTH_SYSTEM_SOURCE_ID` |
| `HEALTH_SYSTEM_SOURCE_ID` | [LH_D_METRIC](LH_D_METRIC.md) | `HEALTH_SYSTEM_SOURCE_ID` |
| `HEALTH_SYSTEM_SOURCE_ID` | [LH_D_METRIC](LH_D_METRIC.md) | `HEALTH_SYSTEM_SOURCE_ID` |
| `HEALTH_SYSTEM_SOURCE_ID` | [LH_D_METRIC](LH_D_METRIC.md) | `HEALTH_SYSTEM_SOURCE_ID` |
| `HEALTH_SYSTEM_SOURCE_ID` | [LH_D_NURSE_UNIT](LH_D_NURSE_UNIT.md) | `HEALTH_SYSTEM_SOURCE_ID` |
| `HEALTH_SYSTEM_SOURCE_ID` | [LH_D_NURSE_UNIT](LH_D_NURSE_UNIT.md) | `HEALTH_SYSTEM_SOURCE_ID` |
| `HEALTH_SYSTEM_SOURCE_ID` | [LH_D_PERSON](LH_D_PERSON.md) | `HEALTH_SYSTEM_SOURCE_ID` |
| `HEALTH_SYSTEM_SOURCE_ID` | [LH_D_PERSONNEL](LH_D_PERSONNEL.md) | `HEALTH_SYSTEM_SOURCE_ID` |

