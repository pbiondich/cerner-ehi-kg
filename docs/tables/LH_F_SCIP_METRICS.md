# LH_F_SCIP_METRICS

> This table is used to store metrics for the Lighthouse Surgical Care Improvement quality measure.

**Description:** LH_F_SCIP_METRICS  
**Table type:** ACTIVITY  
**Primary key:** _(not published — see note)_  
**Columns:** 174

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ABX_EXTEND_REASON_MASK` | DOUBLE |  |  | Identifies the reasons to extend antibiotics |
| 2 | `ABX_RECD_MASK` | DOUBLE |  |  | Identifies when the patient received antibiotics. |
| 3 | `AB_24H_ANES_EXCL_IND` | DOUBLE |  |  | Identified all antibiotic does administrated date/time are more than 24 hours after anesthesia end date. |
| 4 | `AB_ADMIN_IND` | DOUBLE |  |  | Identified patient has antibiotic dose(s) administered |
| 5 | `AB_ALLERGY_FLAG` | DOUBLE |  |  | Identifies patients that have allergies, sensitivities or intolerance to beta-lactam/penicillin antibiotic or cephalosporin medications |
| 6 | `AB_ANES_EXCL_IND` | DOUBLE |  |  | Identifiedall antibiotic does administrated date are not in propertiy days range after anesthesia end date. |
| 7 | `AB_DISC_24H_IND` | DOUBLE |  |  | Identifies if the patient had antibiotics discontinued within 24 hours of the end of surgery. |
| 8 | `AB_DISC_MORE_24H_IND` | DOUBLE |  |  | Identifies patients that had any antibiotics discontinue more than 24 hours of surgery end. |
| 9 | `AB_NAME_3_11_EXCL_IND` | DOUBLE |  |  | Identified patient has antibiotic name on table 3.11 |
| 10 | `AB_RECD_24H_ADM_EXCL_IND` | DOUBLE |  |  | Identifies patients excluded from the SCIP metric. |
| 11 | `AB_RECD_24H_SURG_EXCL_IND` | DOUBLE |  |  | Identifies patients excluded from the SCIP metric. |
| 12 | `AB_RECD_WIN_1H_IND` | DOUBLE |  |  | Identifies if the patient received an antibiotic within 1 hour of surgical incision. |
| 13 | `AB_ROUTE_IM_EXCL_IND` | DOUBLE |  |  | Identified patient all of Antibiotic Administration Route are IM (Intramuscular) or other not oral/IV. |
| 14 | `ACTIVE_IND` | DOUBLE | NOT NULL |  | The table row is active or inactive. A row is generally active unless it is in an inactive state such as logically deleted, combined away, pending purge, etc. |
| 15 | `ACTIVE_WARMING_IND` | DOUBLE |  |  | Identifies patients that had active warming performed intraoperatively. |
| 16 | `ADMIT_DT_TM` | DATETIME |  |  | The date/time on which the patient was admitted. |
| 17 | `ADMIT_UTC_DT_TM` | DATETIME |  |  | The date/time on which the patient was admitted normalized to GMT. |
| 18 | `AGE_EXCL_IND` | DOUBLE |  |  | Identifies patients excluded from the SCIP metric. |
| 19 | `ANES_END_DT_TM` | DATETIME |  |  | The anesthesia end date/time for the principle procedure. |
| 20 | `ANES_END_UTC_DT_TM` | DATETIME |  |  | The anesthesia end date/time for the principle procedure. |
| 21 | `ANES_START_DT_TM` | DATETIME |  |  | The anesthesia start date/time for the principle procedure. |
| 22 | `ANES_START_UTC_DT_TM` | DATETIME |  |  | The anesthesia start date/time for the principle procedure. |
| 23 | `ANES_TYPE_EXCL_IND` | DOUBLE |  |  | Identifies patients excluded from the SCIP metric. |
| 24 | `ANES_TYPE_FLAG` | DOUBLE |  |  | Identifies the type of anesthesia received. |
| 25 | `ARRIVAL_DT_TM` | DATETIME |  |  | The date/time on which the patient arrived at the facility. |
| 26 | `ARRIVAL_UTC_DT_TM` | DATETIME |  |  | The date/time on which the patient arrived at the facility normalized to GMT. |
| 27 | `BASE_POPULATION_IND` | DOUBLE |  |  | Identifies the patients that qualify for the SCIP base population. |
| 28 | `BETA_BLK_PERIOP_FLAG` | DOUBLE |  |  | Identifies patients that received a beta blocker perioperatively. |
| 29 | `BETA_BLK_PERIOP_MASK` | DOUBLE |  |  | Identifies patients that received beta blocker perioperatively. |
| 30 | `BETA_BLK_PREG_FLAG` | DOUBLE |  |  | Identifies female patients that are on a beta blocker during pregnancy. |
| 31 | `BETA_BLK_PRIOR_FLAG` | DOUBLE |  |  | Identifies patients that were on a beta blocker prior to arrival. |
| 32 | `BETA_PERIOP_INCL_IND` | DOUBLE |  |  | Identifies patients that received a beta blocker perioperatively. |
| 33 | `BETA_PREG_EXCL_IND` | DOUBLE |  |  | Identifies patients excluded from the SCIP metric. |
| 34 | `BETA_PRIOR_ADMIT_INCL_IND` | DOUBLE |  |  | Identifies patients that were on a beta blocker prior to arrival. |
| 35 | `BURN_DX_EXCL_IND` | DOUBLE |  |  | Identifies patients excluded from the SCIP metric. |
| 36 | `CARD_2_REJECT_IND` | DOUBLE |  |  | Identifies if the patient record was rejected from the SCIP metric due to missing data. |
| 37 | `CARD_PROC_IND` | DOUBLE |  |  | Identifies patients that had cardiac procedures performed. |
| 38 | `CLIN_TRIAL_EXCL_FLAG` | DOUBLE |  |  | Identifies if the patient is excluded from the measure due to participation in a clinical trial. |
| 39 | `CLIN_TRIAL_EXCL_IND` | DOUBLE |  |  | Identifies patients excluded from the SCIP metric. |
| 40 | `COLON_PROC_ORAL_ABX_FLAG` | DOUBLE |  |  | Identifies color surgery patients that received oral antibiotics |
| 41 | `COMM_MRN_TXT` | VARCHAR(50) |  |  | Identifies the community medical record number of the patient. |
| 42 | `CONTROLLED_GLUCOSE_FLAG` | DOUBLE |  |  | Identifies patients with a controlled post-operative blood glucose level. |
| 43 | `CONTROLLED_GLUCOSE_IND` | DOUBLE |  |  | Identifies patients with controlled glucose levels. |
| 44 | `DISCHARGE_DT_TM` | DATETIME |  |  | The date/time on which the patient was discharged. |
| 45 | `DISCHARGE_UTC_DT_TM` | DATETIME |  |  | The date/time on which the patient was discharged normalized to GMT. |
| 46 | `D_ADMIT_BUILDING_ID` | DOUBLE | NOT NULL | FK→ | The building to which the patient was admitted. |
| 47 | `D_ADMIT_FACILITY_ID` | DOUBLE | NOT NULL | FK→ | The facility to which the patient was admitted. |
| 48 | `D_ADMIT_NURSE_UNIT_ID` | DOUBLE | NOT NULL | FK→ | The nurse unit to which the patient was admitted. |
| 49 | `D_ADMIT_SRC_ID` | DOUBLE | NOT NULL | FK→ | Identifies the place from which the patient came before being admitted. |
| 50 | `D_ADMIT_TYPE_ID` | DOUBLE | NOT NULL | FK→ | Indicates the circumstances under which the patient was admitted. |
| 51 | `D_ATTEND_PRSNL_ID` | DOUBLE | NOT NULL | FK→ | Identifies the final attending physician associated to the encounter. |
| 52 | `D_CARD_2_METRIC_ID` | DOUBLE | NOT NULL | FK→ | The unique identifier for the SCIP metric. |
| 53 | `D_DISCHARGE_BUILDING_ID` | DOUBLE | NOT NULL | FK→ | The building from which the patient was discharged |
| 54 | `D_DISCHARGE_FACILITY_ID` | DOUBLE | NOT NULL | FK→ | The facility from which the patient was discharged |
| 55 | `D_DISCHARGE_NURSE_UNIT_ID` | DOUBLE | NOT NULL | FK→ | The nurse unit from which the patient was discharged |
| 56 | `D_DISCH_DISP_ID` | DOUBLE | NOT NULL | FK→ | The conditions under which the patient left the facility at the time of discharge. |
| 57 | `D_ENCNTR_TYPE_ID` | DOUBLE | NOT NULL | FK→ | Categorizes the encounter into a logical group or type. Foreign key to the CODE_VALUE table. |
| 58 | `D_INF_10_METRIC_ID` | DOUBLE | NOT NULL | FK→ | The unique identifier for the SCIP metric. |
| 59 | `D_INF_1_METRIC_ID` | DOUBLE | NOT NULL | FK→ | The unique identifier for the SCIP metric. |
| 60 | `D_INF_2_METRIC_ID` | DOUBLE | NOT NULL | FK→ | The unique identifier for the SCIP metric. |
| 61 | `D_INF_3_METRIC_ID` | DOUBLE | NOT NULL | FK→ | The unique identifier for the SCIP metric. |
| 62 | `D_INF_4_METRIC_ID` | DOUBLE | NOT NULL | FK→ | The unique identifier for the SCIP metric. |
| 63 | `D_INF_6_METRIC_ID` | DOUBLE | NOT NULL | FK→ | The unique identifier for the SCIP metric. |
| 64 | `D_INF_9_METRIC_ID` | DOUBLE | NOT NULL | FK→ | The unique identifier for the SCIP metric. |
| 65 | `D_MED_SERVICE_ID` | DOUBLE | NOT NULL | FK→ | The type or category of medical service that the patient is receiving in relation to their encounter. The category may be treatment type surgery general resources or others. |
| 66 | `D_PERSON_ID` | DOUBLE | NOT NULL | FK→ | The person that qualified for the quality metric. |
| 67 | `D_PRIN_DIAGNOSIS_ID` | DOUBLE | NOT NULL | FK→ | Identifies the principle diagnosis associated with the encounter. |
| 68 | `D_PRIN_PROCEDURE_ID` | DOUBLE | NOT NULL | FK→ | Identifies the principle procedure associated with the encounter. |
| 69 | `D_PROC_GROUP_ID` | DOUBLE | NOT NULL | FK→ | Identifies the surgical procedure group associated with the principle procedure. |
| 70 | `D_VTE_1_METRIC_ID` | DOUBLE | NOT NULL | FK→ | The unique identifier for the SCIP metric. |
| 71 | `D_VTE_2_METRIC_ID` | DOUBLE | NOT NULL | FK→ | The unique identifier for the SCIP metric. |
| 72 | `ENCNTR_ID` | DOUBLE | NOT NULL |  | Identifies the encounter against which the quality measure is associated. Foreign key to the ENCOUNTER table. |
| 73 | `EXCLUDE_CARD_2_IND` | DOUBLE |  |  | Identifies if the patient is excluded from the measure. |
| 74 | `EXCLUDE_INF_10_IND` | DOUBLE |  |  | Identifies if the patient is excluded from the measure. |
| 75 | `EXCLUDE_INF_1_IND` | DOUBLE |  |  | Identifies if the patient is excluded from the measure. |
| 76 | `EXCLUDE_INF_2_IND` | DOUBLE |  |  | Identifies if the patient is excluded from the measure. |
| 77 | `EXCLUDE_INF_3_IND` | DOUBLE |  |  | Identifies if the patient is excluded from the measure. |
| 78 | `EXCLUDE_INF_4_IND` | DOUBLE |  |  | Identifies if the patient is excluded from the measure. |
| 79 | `EXCLUDE_INF_6_IND` | DOUBLE |  |  | Identifies if the patient is excluded from the measure. |
| 80 | `EXCLUDE_INF_9_IND` | DOUBLE |  |  | Identifies if the patient is excluded from the measure. |
| 81 | `EXCLUDE_VTE_1_IND` | DOUBLE |  |  | Identifies if the patient is excluded from the measure. |
| 82 | `EXCLUDE_VTE_2_IND` | DOUBLE |  |  | Identifies if the patient is excluded from the measure. |
| 83 | `EXTRACT_DT_TM` | DATETIME |  |  | The date/time that the record was extracted from the source system. |
| 84 | `FINANCIAL_NBR_TXT` | VARCHAR(50) |  |  | The financial number alias associated to the encounter. |
| 85 | `FIRST_PROCESS_DT_TM` | DATETIME |  |  | The date/time the record was first loaded into the table. |
| 86 | `F_SCIP_METRICS_ID` | DOUBLE | NOT NULL |  | Unique identifier for the lighthouse PN Metrics |
| 87 | `HAIR_REMOVAL_MASK` | DOUBLE |  |  | Identifies the preoperative hair removal method. |
| 88 | `HAIR_REMOVE_APPROP_IND` | DOUBLE |  |  | Identifies patients that had hair removed via an appropriate method. |
| 89 | `HAIR_REMOVE_PT_EXCL_IND` | DOUBLE |  |  | Identifies patients excluded from the SCIP metric. |
| 90 | `HEALTH_SYSTEM_ID` | DOUBLE | NOT NULL |  | Identifies the delivery network responsible for supplying the data. |
| 91 | `HEALTH_SYSTEM_SOURCE_ID` | DOUBLE | NOT NULL | FK→ | Identifies the unique source within the delivery network responsible for supplying the data. |
| 92 | `HIP_FRAC_DX_IND` | DOUBLE |  |  | Identifies Hip Fracture diagnosis patients. |
| 93 | `HYST_WITH_CSECT_EXCL_IND` | DOUBLE |  |  | Identifies patients excluded from the SCIP metric. |
| 94 | `INF_10_REJECT_IND` | DOUBLE |  |  | Identifies if the patient record was rejected from the SCIP metric due to missing data. |
| 95 | `INF_1_REJECT_IND` | DOUBLE |  |  | Identifies if the patient record was rejected from the SCIP metric due to missing data. |
| 96 | `INF_2_REJECT_IND` | DOUBLE |  |  | Identifies if the patient record was rejected from the SCIP metric due to missing data. |
| 97 | `INF_3_REJECT_IND` | DOUBLE |  |  | Identifies if the patient record was rejected from the SCIP metric due to missing data. |
| 98 | `INF_4_REJECT_IND` | DOUBLE |  |  | Identifies if the patient record was rejected from the SCIP metric due to missing data. |
| 99 | `INF_6_REJECT_IND` | DOUBLE |  |  | Identifies if the patient record was rejected from the SCIP metric due to missing data. |
| 100 | `INF_9_REJECT_IND` | DOUBLE |  |  | Identifies if the patient record was rejected from the SCIP metric due to missing data. |
| 101 | `INF_DISEASE_DX_EXCL_IND` | DOUBLE |  |  | Identifies patients excluded from the SCIP metric. |
| 102 | `INF_PRIOR_ANES_EXCEPT_FLAG` | DOUBLE |  |  | Identifies if a patient has infection exceptions prior to anesthesia documented |
| 103 | `INF_PRIOR_ANES_EXCL_FLAG` | DOUBLE |  |  | Identifies patients that had an infection prior to anesthesia |
| 104 | `INF_PRIOR_ANES_EXCL_IND` | DOUBLE |  |  | Identifies patients excluded from the SCIP metric. |
| 105 | `INTENT_HYPOTHERM_EXCL_FLAG` | DOUBLE |  |  | Identifies patients that had intentional hypothermia documented. |
| 106 | `INTENT_HYPOTHERM_EXCL_IND` | DOUBLE |  |  | Identifies patients excluded from the SCIP metric. |
| 107 | `JOINT_REVISION_EXCL_IND` | DOUBLE |  |  | Identifies patients excluded from the SCIP metric. |
| 108 | `LAPAROSCOPE_EXCL_FLAG` | DOUBLE |  |  | Identifies patients that had the procedure performed entirely by laparoscope. |
| 109 | `LAPAROSCOPE_EXCL_IND` | DOUBLE |  |  | Identifies patients excluded from the SCIP metric. |
| 110 | `LAST_PROCESS_DT_TM` | DATETIME |  |  | The date/time the record was last loaded into the table. |
| 111 | `LOGICAL_DOMAIN_ID` | DOUBLE | NOT NULL |  | The unique identifier for a logical domain. This identifier allows the data to be grouped by logical domain. For example, If you assign clients a logical_domain_id this would allow you to store data for multiple clients on this table. |
| 112 | `LOS_EXCL_IND` | DOUBLE |  |  | Identifies patients excluded from the SCIP metric. |
| 113 | `LVAD_PROC_IND` | DOUBLE |  |  | Identifies patients with Ventricular Assist Devices or Heart Transplantation procedure |
| 114 | `NHIQM_VERSION` | DOUBLE |  |  | Identifies the version of NHIQM for which the row qualifies. |
| 115 | `NO_AB_RECD_EXCL_IND` | DOUBLE |  |  | Identifies patients excluded from the SCIP metric. |
| 116 | `NO_BETA_BLK_REASON_FLAG` | DOUBLE |  |  | Identifies patients with a valid reason documented for not receiving a beta blocker perioperatively. |
| 117 | `NO_BETA_BLK_REASON_MASK` | DOUBLE |  |  | Identifies patients with valid reason documented for not receiving a beta blocker perioperatively. |
| 118 | `NO_BETA_REASON_EXCL_IND` | DOUBLE |  |  | Identifies patients excluded from the SCIP metric. |
| 119 | `NO_PROPH_AB_RECD_EXCL_IND` | DOUBLE |  |  | Identifies patients excluded from the SCIP metric. |
| 120 | `NO_PROPH_RECD_EXCL_IND` | DOUBLE |  |  | Identifies patients excluded from the SCIP metric. |
| 121 | `NO_VTE_MECH_EXCL_IND` | DOUBLE |  |  | Identifies patients excluded from the SCIP metric. |
| 122 | `NO_VTE_PHARM_EXCL_IND` | DOUBLE |  |  | Identifies patients excluded from the SCIP metric. |
| 123 | `NO_VTE_PROPH_REASON_MASK` | DOUBLE |  |  | Identifies the reasons documented for not administering VTE prophylaxis. |
| 124 | `NO_VTE_PROPH_RECD_FLAG` | DOUBLE |  |  | Identifies patients that did not receive VTE prophylaxis. |
| 125 | `NUMERATOR_CARD_2_IND` | DOUBLE |  |  | Identifies if the patient qualifies for the measure. |
| 126 | `NUMERATOR_INF_10_IND` | DOUBLE |  |  | Identifies if the patient qualifies for the measure. |
| 127 | `NUMERATOR_INF_1_IND` | DOUBLE |  |  | Identifies if the patient qualifies for the measure. |
| 128 | `NUMERATOR_INF_2_IND` | DOUBLE |  |  | Identifies if the patient qualifies for the measure. |
| 129 | `NUMERATOR_INF_3_IND` | DOUBLE |  |  | Identifies if the patient qualifies for the measure. |
| 130 | `NUMERATOR_INF_4_IND` | DOUBLE |  |  | Identifies if the patient qualifies for the measure. |
| 131 | `NUMERATOR_INF_6_IND` | DOUBLE |  |  | Identifies if the patient qualifies for the measure. |
| 132 | `NUMERATOR_INF_9_IND` | DOUBLE |  |  | Identifies if the patient qualifies for the measure. |
| 133 | `NUMERATOR_VTE_1_IND` | DOUBLE |  |  | Identifies if the patient qualifies for the measure. |
| 134 | `NUMERATOR_VTE_2_IND` | DOUBLE |  |  | Identifies if the patient qualifies for the measure. |
| 135 | `ORG_MRN_TXT` | VARCHAR(50) |  |  | Identifies the medical record number of the patient. |
| 136 | `OTHER_SURG_PROC_EXCL_FLAG` | DOUBLE |  |  | Identifies patients that had other surgical procedures performed within days of the current procedure. |
| 137 | `OTHER_SURG_PROC_EXCL_IND` | DOUBLE |  |  | Identifies patients excluded from the SCIP metric. |
| 138 | `PARTITION_DT_TM` | DATETIME |  |  | The date/time the encounter was discharged from the facility |
| 139 | `PERIOP_DEATH_EXCL_FLAG` | DOUBLE |  |  | Identifies patients that suffered a perioperative death. |
| 140 | `PERIOP_DEATH_EXCL_IND` | DOUBLE |  |  | Identifies patients excluded from the SCIP metric. |
| 141 | `POSTOP_CATH_EXCL_IND` | DOUBLE |  |  | Identifies patients excluded from the SCIP metric. |
| 142 | `POSTOP_CATH_INCL_IND` | DOUBLE |  |  | Identifies patients that received an indwelling catheter post-op. |
| 143 | `POST_OP_INF_EXCL_IND` | DOUBLE |  |  | Identifies patients excluded from the SCIP metric. |
| 144 | `PREOP_CATH_EXCL_IND` | DOUBLE |  |  | Identifies patients excluded from the SCIP metric. |
| 145 | `PRE_WARFARIN_EXCL_IND` | DOUBLE |  |  | Identifies patients excluded from the SCIP metric. |
| 146 | `PRIN_PROCEDURE_DT_TM` | DATETIME |  |  | The date/time on which the principle procedure was performed. |
| 147 | `PRIN_PROCEDURE_UTC_DT_TM` | DATETIME |  |  | The date/time on which the principle procedure was performed normalized to GMT. |
| 148 | `PROC_GROUP_MEANING` | VARCHAR(50) |  |  | Identifies the Cerner-defined meaning associated with the procedure group. |
| 149 | `PROPH_AB_SELECTED_IND` | DOUBLE |  |  | Identifies if the patient had a prophylactic antibiotic selected. |
| 150 | `SURG_INCISION_DT_TM` | DATETIME |  |  | Identifies if the date/time that the incision for the principal procedure was made |
| 151 | `SURG_INCISION_UTC_DT_TM` | DATETIME |  |  | Identifies if the date/time that the incision for the principal procedure was made |
| 152 | `TEMP_CONTROL_MASK` | DOUBLE |  |  | Identifies how the temperature was controlled during surgery. |
| 153 | `TRANSPLANT_DX_EXCL_IND` | DOUBLE |  |  | Identifies patients excluded from the SCIP metric. |
| 154 | `UC_CONTINUE_REASON_FLAG` | DOUBLE |  |  | Identifies the reasons for continuing the urinary catheter |
| 155 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 156 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 157 | `UPDT_SOURCE` | VARCHAR(50) | NOT NULL |  | The script name responsible for updating the record. |
| 158 | `UPDT_TASK` | VARCHAR(50) | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |
| 159 | `URINARY_ANTI_EXCL_IND` | DOUBLE |  |  | Identifies patients excluded from the SCIP metric. |
| 160 | `URINARY_CATHETER_FLAG` | DOUBLE |  |  | Identifies when the urinary catheter was placed. |
| 161 | `URO_GYN_PROC_EXCL_IND` | DOUBLE |  |  | Identifies patients excluded from the SCIP metric. |
| 162 | `UR_CATH_NO_RMV_EXCL_IND` | DOUBLE |  |  | Identifies patients excluded from the SCIP metric. |
| 163 | `UR_CATH_RMV_DT_TM` | DATETIME |  |  | The date abd time the urinary catheter was removed. |
| 164 | `UR_CATH_RMV_UTC_DT_TM` | DATETIME |  |  | The date abd time the urinary catheter was removed.normalized to GMT. |
| 165 | `VANCOMYCIN_MASK` | DOUBLE |  |  | Identifies the VTE prophylaxis selected. |
| 166 | `VTE_1_REJECT_IND` | DOUBLE |  |  | Identifies if the patient record was rejected from the SCIP metric due to missing data. |
| 167 | `VTE_2_REJECT_IND` | DOUBLE |  |  | Identifies if the patient record was rejected from the SCIP metric due to missing data. |
| 168 | `VTE_PROC` | VARCHAR(50) |  |  | Identifies patients with procedures specific to the VTE metrics. |
| 169 | `VTE_PROC_IND` | DOUBLE |  |  | Identifies if the patient had a principle procedure specific to the VTE metric. |
| 170 | `VTE_PROPHYLAXIS_MASK` | DOUBLE |  |  | Identifies the VTE prophylaxis selected. |
| 171 | `VTE_PROPH_IND` | DOUBLE |  |  | Identifies patients that had VTE prophylaxis ordered and documented. |
| 172 | `VTE_PROPH_RECD_IND` | DOUBLE |  |  | Identifies patients that received VTE prophylaxis. |
| 173 | `VTE_TIMELY_MASK` | DOUBLE |  |  | Identifies VTE prophylaxis selected with timely document |
| 174 | `WARFARIN_PRIOR_ADMIT_FLAG` | DOUBLE |  |  | Identifies patients that were on warfarin prior to admission. |

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
| `D_CARD_2_METRIC_ID` | [LH_D_METRIC](LH_D_METRIC.md) | `D_METRIC_ID` |
| `D_DISCHARGE_BUILDING_ID` | [LH_D_BUILDING](LH_D_BUILDING.md) | `D_BUILDING_ID` |
| `D_DISCHARGE_FACILITY_ID` | [LH_D_FACILITY](LH_D_FACILITY.md) | `D_FACILITY_ID` |
| `D_DISCHARGE_NURSE_UNIT_ID` | [LH_D_NURSE_UNIT](LH_D_NURSE_UNIT.md) | `D_NURSE_UNIT_ID` |
| `D_DISCH_DISP_ID` | [LH_D_DISCH_DISP](LH_D_DISCH_DISP.md) | `D_DISCH_DISP_ID` |
| `D_ENCNTR_TYPE_ID` | [LH_D_ENCNTR_TYPE](LH_D_ENCNTR_TYPE.md) | `D_ENCNTR_TYPE_ID` |
| `D_INF_10_METRIC_ID` | [LH_D_METRIC](LH_D_METRIC.md) | `D_METRIC_ID` |
| `D_INF_1_METRIC_ID` | [LH_D_METRIC](LH_D_METRIC.md) | `D_METRIC_ID` |
| `D_INF_2_METRIC_ID` | [LH_D_METRIC](LH_D_METRIC.md) | `D_METRIC_ID` |
| `D_INF_3_METRIC_ID` | [LH_D_METRIC](LH_D_METRIC.md) | `D_METRIC_ID` |
| `D_INF_4_METRIC_ID` | [LH_D_METRIC](LH_D_METRIC.md) | `D_METRIC_ID` |
| `D_INF_6_METRIC_ID` | [LH_D_METRIC](LH_D_METRIC.md) | `D_METRIC_ID` |
| `D_INF_9_METRIC_ID` | [LH_D_METRIC](LH_D_METRIC.md) | `D_METRIC_ID` |
| `D_MED_SERVICE_ID` | [LH_D_MED_SERVICE](LH_D_MED_SERVICE.md) | `D_MED_SERVICE_ID` |
| `D_PERSON_ID` | [LH_D_PERSON](LH_D_PERSON.md) | `D_PERSON_ID` |
| `D_PRIN_DIAGNOSIS_ID` | [LH_D_DIAGNOSIS](LH_D_DIAGNOSIS.md) | `D_DIAGNOSIS_ID` |
| `D_PRIN_PROCEDURE_ID` | [LH_D_PROCEDURE](LH_D_PROCEDURE.md) | `D_PROCEDURE_ID` |
| `D_PROC_GROUP_ID` | [LH_D_GROUP](LH_D_GROUP.md) | `D_GROUP_ID` |
| `D_VTE_1_METRIC_ID` | [LH_D_METRIC](LH_D_METRIC.md) | `D_METRIC_ID` |
| `D_VTE_2_METRIC_ID` | [LH_D_METRIC](LH_D_METRIC.md) | `D_METRIC_ID` |
| `HEALTH_SYSTEM_SOURCE_ID` | [LH_D_ADMIT_SRC](LH_D_ADMIT_SRC.md) | `HEALTH_SYSTEM_SOURCE_ID` |
| `HEALTH_SYSTEM_SOURCE_ID` | [LH_D_ADMIT_TYPE](LH_D_ADMIT_TYPE.md) | `HEALTH_SYSTEM_SOURCE_ID` |
| `HEALTH_SYSTEM_SOURCE_ID` | [LH_D_BUILDING](LH_D_BUILDING.md) | `HEALTH_SYSTEM_SOURCE_ID` |
| `HEALTH_SYSTEM_SOURCE_ID` | [LH_D_BUILDING](LH_D_BUILDING.md) | `HEALTH_SYSTEM_SOURCE_ID` |
| `HEALTH_SYSTEM_SOURCE_ID` | [LH_D_DIAGNOSIS](LH_D_DIAGNOSIS.md) | `HEALTH_SYSTEM_SOURCE_ID` |
| `HEALTH_SYSTEM_SOURCE_ID` | [LH_D_DISCH_DISP](LH_D_DISCH_DISP.md) | `HEALTH_SYSTEM_SOURCE_ID` |
| `HEALTH_SYSTEM_SOURCE_ID` | [LH_D_ENCNTR_TYPE](LH_D_ENCNTR_TYPE.md) | `HEALTH_SYSTEM_SOURCE_ID` |
| `HEALTH_SYSTEM_SOURCE_ID` | [LH_D_FACILITY](LH_D_FACILITY.md) | `HEALTH_SYSTEM_SOURCE_ID` |
| `HEALTH_SYSTEM_SOURCE_ID` | [LH_D_FACILITY](LH_D_FACILITY.md) | `HEALTH_SYSTEM_SOURCE_ID` |
| `HEALTH_SYSTEM_SOURCE_ID` | [LH_D_GROUP](LH_D_GROUP.md) | `HEALTH_SYSTEM_SOURCE_ID` |
| `HEALTH_SYSTEM_SOURCE_ID` | [LH_D_MED_SERVICE](LH_D_MED_SERVICE.md) | `HEALTH_SYSTEM_SOURCE_ID` |
| `HEALTH_SYSTEM_SOURCE_ID` | [LH_D_METRIC](LH_D_METRIC.md) | `HEALTH_SYSTEM_SOURCE_ID` |
| `HEALTH_SYSTEM_SOURCE_ID` | [LH_D_METRIC](LH_D_METRIC.md) | `HEALTH_SYSTEM_SOURCE_ID` |
| `HEALTH_SYSTEM_SOURCE_ID` | [LH_D_METRIC](LH_D_METRIC.md) | `HEALTH_SYSTEM_SOURCE_ID` |
| `HEALTH_SYSTEM_SOURCE_ID` | [LH_D_METRIC](LH_D_METRIC.md) | `HEALTH_SYSTEM_SOURCE_ID` |
| `HEALTH_SYSTEM_SOURCE_ID` | [LH_D_METRIC](LH_D_METRIC.md) | `HEALTH_SYSTEM_SOURCE_ID` |
| `HEALTH_SYSTEM_SOURCE_ID` | [LH_D_METRIC](LH_D_METRIC.md) | `HEALTH_SYSTEM_SOURCE_ID` |
| `HEALTH_SYSTEM_SOURCE_ID` | [LH_D_METRIC](LH_D_METRIC.md) | `HEALTH_SYSTEM_SOURCE_ID` |
| `HEALTH_SYSTEM_SOURCE_ID` | [LH_D_METRIC](LH_D_METRIC.md) | `HEALTH_SYSTEM_SOURCE_ID` |
| `HEALTH_SYSTEM_SOURCE_ID` | [LH_D_METRIC](LH_D_METRIC.md) | `HEALTH_SYSTEM_SOURCE_ID` |
| `HEALTH_SYSTEM_SOURCE_ID` | [LH_D_METRIC](LH_D_METRIC.md) | `HEALTH_SYSTEM_SOURCE_ID` |
| `HEALTH_SYSTEM_SOURCE_ID` | [LH_D_NURSE_UNIT](LH_D_NURSE_UNIT.md) | `HEALTH_SYSTEM_SOURCE_ID` |
| `HEALTH_SYSTEM_SOURCE_ID` | [LH_D_NURSE_UNIT](LH_D_NURSE_UNIT.md) | `HEALTH_SYSTEM_SOURCE_ID` |
| `HEALTH_SYSTEM_SOURCE_ID` | [LH_D_PERSON](LH_D_PERSON.md) | `HEALTH_SYSTEM_SOURCE_ID` |
| `HEALTH_SYSTEM_SOURCE_ID` | [LH_D_PERSONNEL](LH_D_PERSONNEL.md) | `HEALTH_SYSTEM_SOURCE_ID` |
| `HEALTH_SYSTEM_SOURCE_ID` | [LH_D_PROCEDURE](LH_D_PROCEDURE.md) | `HEALTH_SYSTEM_SOURCE_ID` |

