# LH_F_AMI_METRICS

> This table is used to store metrics for the Lighthouse Acute Myocardial Infarction quality measure.

**Description:** LH_F_AMI_METRICS  
**Table type:** ACTIVITY  
**Primary key:** _(not published — see note)_  
**Columns:** 173

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ACEI_ARB_MASK` | DOUBLE |  |  | Identifies if the patient was prescribed ACEI or ARB at discharge. |
| 2 | `ACTIVE_IND` | DOUBLE | NOT NULL |  | The table row is active or inactive. A row is generally active unless it is in an inactive state such as logically deleted, combined away, pending purge, etc. |
| 3 | `ADMIT_DT_TM` | DATETIME |  |  | The date/time on which the patient was admitted. |
| 4 | `ADMIT_UTC_DT_TM` | DATETIME |  |  | The date/time on which the patient was admitted normalized to GMT. |
| 5 | `ADM_SRC_FLAG` | DOUBLE |  |  | Identifies the admission source for the patient. |
| 6 | `AMI10_REJECT_IND` | DOUBLE |  |  | Identifies if the patient was rejected from the measure. |
| 7 | `AMI1_ADM_SRC_EXCL_IND` | DOUBLE |  |  | Identifies patients that qualify for this AMI metric. |
| 8 | `AMI1_ASA_24H_ARR_IND` | DOUBLE |  |  | Identifies patients that qualify for this AMI metric. |
| 9 | `AMI1_DISC_DISP_EXCL_IND` | DOUBLE |  |  | Identifies patients that qualify for this AMI metric. |
| 10 | `AMI1_NO_ASA_ARR_EXCL_IND` | DOUBLE |  |  | Identifies patients that qualify for this AMI metric. |
| 11 | `AMI1_REJECT_IND` | DOUBLE |  |  | Identifies patients that were rejected for the AMI metric. |
| 12 | `AMI2_ASP_AT_DISC_IND` | DOUBLE |  |  | Identifies patients that qualify for this AMI metric. |
| 13 | `AMI2_DISC_DISP_EXCL_IND` | DOUBLE |  |  | Identifies patients that qualify for this AMI metric. |
| 14 | `AMI2_NO_ASP_DISC_EXCL_IND` | DOUBLE |  |  | Identifies patients that qualify for this AMI metric. |
| 15 | `AMI2_REJECT_IND` | DOUBLE |  |  | Identifies patients that were rejected for the AMI metric. |
| 16 | `AMI3_ACEI_DISC_IND` | DOUBLE |  |  | Identifies patients that qualify for this AMI metric. |
| 17 | `AMI3_ARB_DISC_IND` | DOUBLE |  |  | Identifies patients that qualify for this AMI metric. |
| 18 | `AMI3_DISC_DISP_EXCL_IND` | DOUBLE |  |  | Identifies patients that qualify for this AMI metric. |
| 19 | `AMI3_LVEF_MOD_SEVERE_IND` | DOUBLE |  |  | Identifies patients that qualify for this AMI metric. |
| 20 | `AMI3_NO_ACEI_ARB_EXCL_IND` | DOUBLE |  |  | Identifies patients that qualify for this AMI metric. |
| 21 | `AMI3_REJECT_IND` | DOUBLE |  |  | Identifies patients that were rejected for the AMI metric. |
| 22 | `AMI4_DISC_DISP_EXCL_IND` | DOUBLE |  |  | Identifies patients that qualify for this AMI metric. |
| 23 | `AMI4_REJECT_IND` | DOUBLE |  |  | Identifies patients that were rejected for the AMI metric. |
| 24 | `AMI4_SMOKE_COUNS_IND` | DOUBLE |  |  | Identifies patients that qualify for this AMI metric. |
| 25 | `AMI4_SMOKE_HX_IND` | DOUBLE |  |  | Identifies patients that qualify for this AMI metric. |
| 26 | `AMI5_BETA_DISC_IND` | DOUBLE |  |  | Identifies patients that qualify for this AMI metric. |
| 27 | `AMI5_DISC_DISP_EXCL_IND` | DOUBLE |  |  | Identifies patients that qualify for this AMI metric. |
| 28 | `AMI5_NO_BETA_EXCL_IND` | DOUBLE |  |  | Identifies patients that qualify for this AMI metric. |
| 29 | `AMI5_REJECT_IND` | DOUBLE |  |  | Identifies patients that were rejected for the AMI metric. |
| 30 | `AMI7_ADM_SRC_EXCL_IND` | DOUBLE |  |  | Identifies patients that qualify for this AMI metric. |
| 31 | `AMI7_FIB_DELAY_EXCL_IND` | DOUBLE |  |  | Identifies patients that qualify for this AMI metric. |
| 32 | `AMI7_REJECT_IND` | DOUBLE |  |  | Identifies patients that were rejected for the AMI metric. |
| 33 | `AMI8_ADM_SRC_EXCL_IND` | DOUBLE |  |  | Identifies patients that qualify for this AMI metric. |
| 34 | `AMI8_PCI_DELAY_EXCL_IND` | DOUBLE |  |  | Identifies patients that qualify for this AMI metric. |
| 35 | `AMI8_PCI_PRIM_IND` | DOUBLE |  |  | Identifies patients that qualify for this AMI metric. |
| 36 | `AMI8_PCI_PROC_CODE_IND` | DOUBLE |  |  | Identifies patients that qualify for this AMI metric. |
| 37 | `AMI8_PCI_ST_DT_TM` | DATETIME |  |  | Identifies patients that qualify for this AMI metric. |
| 38 | `AMI8_PCI_ST_UTC_DT_TM` | DATETIME |  |  | Identifies patients that qualify for this AMI metric. |
| 39 | `AMI8_REJECT_IND` | DOUBLE |  |  | Identifies patients that were rejected for the AMI metric. |
| 40 | `AMI9_ADM_SRC_EXCL_IND` | DOUBLE |  |  | Identifies patients that qualify for this AMI metric. |
| 41 | `AMI9_DISC_DISP_EXCL_IND` | DOUBLE |  |  | Identifies patients that qualify for this AMI metric. |
| 42 | `AMI9_DISC_DISP_EXP_IND` | DOUBLE |  |  | Identifies patients that qualify for this AMI metric. |
| 43 | `AMI9_REJECT_IND` | DOUBLE |  |  | Identifies patients rejected for AMI-9 |
| 44 | `AMIT1_DISC_DISP_EXCL_IND` | DOUBLE |  |  | Identifies patients that qualify for this AMI metric. |
| 45 | `AMIT1_LDL_IN_HOSP_IND` | DOUBLE |  |  | Identifies patients that qualify for this AMI metric. |
| 46 | `AMIT1_LDL_ND_EXCL_IND` | DOUBLE |  |  | Identifies patients that qualify for this AMI metric. |
| 47 | `AMIT1_LDL_POST_DISC_IND` | DOUBLE |  |  | Identifies patients that qualify for this AMI metric. |
| 48 | `AMIT1_LDL_PRE_ARR_QL_IND` | DOUBLE |  |  | Identifies patients that qualify for this AMI metric. |
| 49 | `AMIT1_LDL_PRE_ARR_QNT_IND` | DOUBLE |  |  | Identifies patients that qualify for this AMI metric. |
| 50 | `AMIT1_PRE_ARR_EXCL_IND` | DOUBLE |  |  | Identifies patients that qualify for this AMI metric. |
| 51 | `AMIT1_REJECT_IND` | DOUBLE |  |  | Identifies patients that were rejected for the AMI metric. |
| 52 | `AMIT2_DISC_DISP_EXCL_IND` | DOUBLE |  |  | Identifies patients that qualify for this AMI metric. |
| 53 | `AMIT2_LDL_QNT_RESULT` | DOUBLE |  |  | Identifies patients that qualify for this AMI metric. |
| 54 | `AMIT2_LDL_QNT_VLD_IND` | DOUBLE |  |  | Identifies patients that qualify for this AMI metric. |
| 55 | `AMIT2_LDL_RESULT_QL_IND` | DOUBLE |  |  | Identifies patients that qualify for this AMI metric. |
| 56 | `AMIT2_LDL_RX_DISC_IND` | DOUBLE |  |  | Identifies patients that qualify for this AMI metric. |
| 57 | `AMIT2_REASON_EXCL_IND` | DOUBLE |  |  | Identifies patients that qualify for this AMI metric. |
| 58 | `AMIT2_REJECT_IND` | DOUBLE |  |  | Identifies patients that were rejected for the AMI metric. |
| 59 | `AMI_AGE_EXCL_IND` | DOUBLE |  |  | Identifies patients that qualify for this AMI metric. |
| 60 | `AMI_BASE_POPULATION_IND` | DOUBLE |  |  | Identifies patients that qualify for the base AMI population. |
| 61 | `AMI_CLIN_TRIAL_EXCL_IND` | DOUBLE |  |  | Identifies patients that qualify for this AMI metric. |
| 62 | `AMI_CMO_EXCL_IND` | DOUBLE |  |  | Identifies patients that qualify for this AMI metric. |
| 63 | `AMI_ED_TRANS_EXCL_IND` | DOUBLE |  |  | Identifies patients that qualify for this AMI metric. |
| 64 | `AMI_FIB_ADMIN_DT_TM` | DATETIME |  |  | Identifies patients that qualify for this AMI metric. |
| 65 | `AMI_FIB_ADMIN_FLAG` | DOUBLE |  |  | Identifies if the patient has fibrinolytic administration. 0 - False, 1 - True, 999 - Missing. |
| 66 | `AMI_FIB_ADMIN_UTC_DT_TM` | DATETIME |  |  | Identifies patients that qualify for this AMI metric. |
| 67 | `AMI_LOS_EXCL_IND` | DOUBLE |  |  | Identifies patients that qualify for this AMI metric. |
| 68 | `AMI_ST_LBBB_IND` | DOUBLE |  |  | Identifies patients that qualify for this AMI metric. |
| 69 | `ARRIVAL_DT_TM` | DATETIME |  |  | The date/time on which the patient arrived at the facility. |
| 70 | `ARRIVAL_UTC_DT_TM` | DATETIME |  |  | The date/time on which the patient arrived at the facility normalized to GMT. |
| 71 | `ASA_24H_ARR_FLAG` | DOUBLE |  |  | Identifies if the patient received aspirin within 24 hours of arrival. |
| 72 | `ASP_AT_DISC_FLAG` | DOUBLE |  |  | Identifies if the patient was prescribed aspirin at discharge. |
| 73 | `BETA_BLK_DISC_FLAG` | DOUBLE |  |  | Identifies if the patient had a beta blocker at discharge. |
| 74 | `CLIN_TRIAL_EXCL_FLAG` | DOUBLE |  |  | Identifies if the patient is excluded from the measure due to participation in a clinical trial. |
| 75 | `CMO_ORDER_DT_TM` | DATETIME |  |  | Identifies the date/time on which comfort measures were ordered. |
| 76 | `CMO_ORDER_UTC_DT_TM` | DATETIME |  |  | Identifies the date/time on which comfort measures were ordered. |
| 77 | `COMM_MRN_TXT` | VARCHAR(50) |  |  | Identifies the community medical record number of the patient. |
| 78 | `DISCHARGE_DT_TM` | DATETIME |  |  | The date/time on which the patient was discharged. |
| 79 | `DISCHARGE_UTC_DT_TM` | DATETIME |  |  | The date/time on which the patient was discharged normalized to GMT. |
| 80 | `DISC_DISP_FLAG` | DOUBLE |  |  | Identifies the discharge disposition of the patient. |
| 81 | `D_ADMIT_BUILDING_ID` | DOUBLE | NOT NULL | FK→ | The building to which the patient was admitted. |
| 82 | `D_ADMIT_FACILITY_ID` | DOUBLE | NOT NULL | FK→ | The facility to which the patient was admitted. |
| 83 | `D_ADMIT_NURSE_UNIT_ID` | DOUBLE | NOT NULL | FK→ | The nurse unit to which the patient was admitted. |
| 84 | `D_ADMIT_SRC_ID` | DOUBLE | NOT NULL | FK→ | Identifies the place from which the patient came before being admitted. |
| 85 | `D_ADMIT_TYPE_ID` | DOUBLE | NOT NULL | FK→ | Indicates the circumstances under which the patient was admitted. |
| 86 | `D_AMI10_METRIC_ID` | DOUBLE | NOT NULL |  | The unique identifier for the measure. |
| 87 | `D_AMI1_METRIC_ID` | DOUBLE | NOT NULL | FK→ | Identifies the patient population associated with the AMI1 metric. |
| 88 | `D_AMI2_METRIC_ID` | DOUBLE | NOT NULL | FK→ | Identifies the patient population associated with the AMI2 metric. |
| 89 | `D_AMI3_METRIC_ID` | DOUBLE | NOT NULL | FK→ | Identifies the patient population associated with the AMI3 metric. |
| 90 | `D_AMI4_METRIC_ID` | DOUBLE | NOT NULL | FK→ | Identifies the patient population associated with the AMI4 metric. |
| 91 | `D_AMI5_METRIC_ID` | DOUBLE | NOT NULL | FK→ | Identifies the patient population associated with the AMI5 metric. |
| 92 | `D_AMI7A_METRIC_ID` | DOUBLE | NOT NULL | FK→ | Identifies the patient population associated with the AMI7A metric. |
| 93 | `D_AMI7_METRIC_ID` | DOUBLE | NOT NULL | FK→ | Identifies the patient population associated with the AMI7 metric. |
| 94 | `D_AMI8A_METRIC_ID` | DOUBLE | NOT NULL | FK→ | Identifies the patient population associated with the AMI8A metric. |
| 95 | `D_AMI8_METRIC_ID` | DOUBLE | NOT NULL | FK→ | Identifies the patient population associated with the AMI8 metric. |
| 96 | `D_AMI9_METRIC_ID` | DOUBLE | NOT NULL | FK→ | Identifies the patient population associated with the AMI9 metric. |
| 97 | `D_AMIT1_METRIC_ID` | DOUBLE | NOT NULL | FK→ | Identifies the patient population associated with the AMIT1A metric. |
| 98 | `D_AMIT2_METRIC_ID` | DOUBLE | NOT NULL | FK→ | Identifies the patient population associated with the AMIT2 metric. |
| 99 | `D_ATTEND_PRSNL_ID` | DOUBLE | NOT NULL | FK→ | Identifies the final attending physician associated to the encounter. |
| 100 | `D_DISCHARGE_BUILDING_ID` | DOUBLE | NOT NULL | FK→ | The building from which the patient was discharged |
| 101 | `D_DISCHARGE_FACILITY_ID` | DOUBLE | NOT NULL | FK→ | The facility from which the patient was discharged |
| 102 | `D_DISCHARGE_NURSE_UNIT_ID` | DOUBLE | NOT NULL | FK→ | The nurse unit from which the patient was discharged |
| 103 | `D_DISCH_DISP_ID` | DOUBLE | NOT NULL | FK→ | The conditions under which the patient left the facility at the time of discharge. |
| 104 | `D_ENCNTR_TYPE_ID` | DOUBLE | NOT NULL | FK→ | Categorizes the encounter into a logical group or type. Foreign key to the CODE_VALUE table. |
| 105 | `D_MED_SERVICE_ID` | DOUBLE | NOT NULL | FK→ | The type or category of medical service that the patient is receiving in relation to their encounter. The category may be treatment type surgery general resources or others. |
| 106 | `D_PERSON_ID` | DOUBLE | NOT NULL | FK→ | The person that qualified for the quality metric. |
| 107 | `D_PRIN_DIAGNOSIS_ID` | DOUBLE | NOT NULL | FK→ | Identifies the principle diagnosis associated with the encounter. |
| 108 | `D_PRIN_PROCEDURE_ID` | DOUBLE | NOT NULL | FK→ | Identifies the principle procedure associated with the encounter. |
| 109 | `ED_TRANS_EXCL_FLAG` | DOUBLE |  |  | Identifies if the patient is excluded from the measure due to a transfer from an ED. |
| 110 | `ENCNTR_ID` | DOUBLE | NOT NULL |  | Identifies the encounter against which the quality measure is associated. Foreign key to the ENCOUNTER table. |
| 111 | `EXCLUDE_10_IND` | DOUBLE |  |  | Identifies if the patient was excluded from the measure. |
| 112 | `EXCLUDE_1_IND` | DOUBLE |  |  | Identifies patients excluded from AMI-1 |
| 113 | `EXCLUDE_2_IND` | DOUBLE |  |  | Identifies patients excluded from AMI-2 |
| 114 | `EXCLUDE_3_IND` | DOUBLE |  |  | Identifies patients excluded from AMI-3 |
| 115 | `EXCLUDE_4_IND` | DOUBLE |  |  | Identifies patients excluded from AMI-4 |
| 116 | `EXCLUDE_5_IND` | DOUBLE |  |  | Identifies patients excluded from AMI-5 |
| 117 | `EXCLUDE_7_IND` | DOUBLE |  |  | Identifies patients excluded from AMI-7 and AMI-7a |
| 118 | `EXCLUDE_8_IND` | DOUBLE |  |  | Identifies patients excluded from AMI-8 and AMI-8a |
| 119 | `EXCLUDE_9_IND` | DOUBLE |  |  | Identifies patients excluded from AMI-9 |
| 120 | `EXCLUDE_T1A_IND` | DOUBLE |  |  | Identifies patients excluded from AMI-T1a |
| 121 | `EXCLUDE_T2_IND` | DOUBLE |  |  | Identifies patients excluded from AMI-T2 |
| 122 | `EXTRACT_DT_TM` | DATETIME |  |  | The date/time that the record was extracted from the source system. |
| 123 | `FIB_DELAY_EXCL_FLAG` | DOUBLE |  |  | Identifies if there is a valid reason documented for fibrinolytic delay. |
| 124 | `FINANCIAL_NBR_TXT` | VARCHAR(50) |  |  | The financial number alias associated to the encounter. |
| 125 | `FIRST_PROCESS_DT_TM` | DATETIME |  |  | The date/time the record was first loaded into the table. |
| 126 | `F_AMI_METRICS_ID` | DOUBLE | NOT NULL |  | Unique identifier for the lighthouse AMI metrics |
| 127 | `HEALTH_SYSTEM_ID` | DOUBLE | NOT NULL |  | Identifies the delivery network responsible for supplying the data. |
| 128 | `HEALTH_SYSTEM_SOURCE_ID` | DOUBLE | NOT NULL | FK→ | Identifies the unique source within the delivery network responsible for supplying the data. |
| 129 | `HOSP_TRANSFER_FLAG` | DOUBLE |  |  | Identifies if the patient transferred from another acute care facility. |
| 130 | `INIT_ECG_INTERP_FLAG` | DOUBLE |  |  | Identifies if the patient had an elevated ST-segment or LBBB. |
| 131 | `LAST_PROCESS_DT_TM` | DATETIME |  |  | The date/time the record was last loaded into the table. |
| 132 | `LDL_IN_HOSP_FLAG` | DOUBLE |  |  | Identifies if the patient had an LDL-c during this visit. |
| 133 | `LDL_LT_100_FLAG` | DOUBLE |  |  | Identifies if the patient had an LDL-c result less than 100. |
| 134 | `LDL_ND_EXCL_FLAG` | DOUBLE |  |  | Identifies if there is a valid reason documented for not receiving an LDL-c. |
| 135 | `LDL_POST_DISC_FLAG` | DOUBLE |  |  | Identifies if there is a plan for a post-discharge LDL-c. |
| 136 | `LDL_PRE_ARR_QL_FLAG` | DOUBLE |  |  | Identifies if the patient had a pre-arrival qualitative LDL-c. |
| 137 | `LDL_PRE_ARR_QNT_FLAG` | DOUBLE |  |  | Identifies if the patient had a pre-arrival quantitative LDL-c. |
| 138 | `LDL_RESULT_QL_FLAG` | DOUBLE |  |  | Identifies if there is a qualitative LDL-c result. |
| 139 | `LDL_RX_DISC_FLAG` | DOUBLE |  |  | Identifies if a lipid-lowering agent was prescribed at discharge. |
| 140 | `LOGICAL_DOMAIN_ID` | DOUBLE | NOT NULL |  | The unique identifier for a logical domain. This identifier allows the data to be grouped by logical domain. For example, If you assign clients a logical_domain_id this would allow you to store data for multiple clients on this table. |
| 141 | `LVEF_MOD_SEVERE_FLAG` | DOUBLE |  |  | Identifies if the patient has moderate or severe systolic dysfunction. |
| 142 | `NHIQM_VERSION` | DOUBLE |  |  | Identifies the version of NHIQM for which the patient qualifies |
| 143 | `NO_ACEI_ARB_EXCL_FLAG` | DOUBLE |  |  | Identifies if there is a valid reason for not prescribing ACEI or ARB at discharge. |
| 144 | `NO_ASA_ARR_EXCL_FLAG` | DOUBLE |  |  | Identifies if there is a reason documented for not giving aspirin within 24 hours of arrival. |
| 145 | `NO_ASP_DISC_EXCL_FLAG` | DOUBLE |  |  | Identifies if there is a reason documented for not prescribing aspirin at discharge. |
| 146 | `NO_BETA_BLK_EXCL_FLAG` | DOUBLE |  |  | Identifies if a valid reason was documented for not prescribing a beta blocker at discharge. |
| 147 | `NO_LPD_LOWER_EXCL_FLAG` | DOUBLE |  |  | Identifies if there is a valid reason for not prescribing a lipid-lowering agent. |
| 148 | `NO_STATIN_REASON_FLAG` | DOUBLE |  |  | Identifies if there was a documented reason for not prescribing statin at discharge. |
| 149 | `NUMERATOR_10_IND` | DOUBLE |  |  | Identifies if the patient qualified for the measure. |
| 150 | `NUMERATOR_1_IND` | DOUBLE |  |  | Identifies patients that qualify for AMI-1 |
| 151 | `NUMERATOR_2_IND` | DOUBLE |  |  | Identifies patients that qualify for AMI-2 |
| 152 | `NUMERATOR_3_IND` | DOUBLE |  |  | Identifies patients that qualify for AMI-3 |
| 153 | `NUMERATOR_4_IND` | DOUBLE |  |  | Identifies patients that qualify for AMI-4 |
| 154 | `NUMERATOR_5_IND` | DOUBLE |  |  | Identifies patients that qualify for AMI-4 |
| 155 | `NUMERATOR_7A_IND` | DOUBLE |  |  | Identifies patients that qualify for AMI-4 |
| 156 | `NUMERATOR_8A_IND` | DOUBLE |  |  | Identifies patients that qualify for AMI-4 |
| 157 | `NUMERATOR_9_IND` | DOUBLE |  |  | Identifies patients that qualify for AMI-4 |
| 158 | `NUMERATOR_T1A_IND` | DOUBLE |  |  | Identifies patients that qualify for AMI-4 |
| 159 | `NUMERATOR_T2_IND` | DOUBLE |  |  | Identifies patients that qualify for AMI-4 |
| 160 | `ORG_MRN_TXT` | VARCHAR(50) |  |  | Identifies the medical record number of the patient. |
| 161 | `PARTITION_DT_TM` | DATETIME |  |  | The date/time the encounter was discharged from the facility |
| 162 | `PCI_DELAY_EXCL_FLAG` | DOUBLE |  |  | Identifies if there is a documented reason for delay in PCI. |
| 163 | `PCI_PRIM_EXCL_FLAG` | DOUBLE |  |  | Identifies if the PCI was the primary procedure. |
| 164 | `PRE_ARR_MED_EXCL_FLAG` | DOUBLE |  |  | Identifies if the patient is excluded due to receiving a lipid-lowering agent prior to arrival |
| 165 | `PRIN_PROCEDURE_DT_TM` | DATETIME |  |  | The date/time on which the principle procedure was performed. |
| 166 | `PRIN_PROCEDURE_UTC_DT_TM` | DATETIME |  |  | The date/time on which the principle procedure was performed normalized to GMT. |
| 167 | `SMOKE_COUNS_FLAG` | DOUBLE |  |  | Identifies if the patient received smoking cessation counseling |
| 168 | `SMOKE_HX_FLAG` | DOUBLE |  |  | Identifies if the patient has a history of smoking. |
| 169 | `STATIN_AT_DISC_FLAG` | DOUBLE |  |  | Identifies if the patient was prescribed statin at discharge. |
| 170 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 171 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 172 | `UPDT_SOURCE` | VARCHAR(50) | NOT NULL |  | The script name responsible for updating the record. |
| 173 | `UPDT_TASK` | VARCHAR(50) | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `D_ADMIT_BUILDING_ID` | [LH_D_BUILDING](LH_D_BUILDING.md) | `D_BUILDING_ID` |
| `D_ADMIT_FACILITY_ID` | [LH_D_FACILITY](LH_D_FACILITY.md) | `D_FACILITY_ID` |
| `D_ADMIT_NURSE_UNIT_ID` | [LH_D_NURSE_UNIT](LH_D_NURSE_UNIT.md) | `D_NURSE_UNIT_ID` |
| `D_ADMIT_SRC_ID` | [LH_D_ADMIT_SRC](LH_D_ADMIT_SRC.md) | `D_ADMIT_SRC_ID` |
| `D_ADMIT_TYPE_ID` | [LH_D_ADMIT_TYPE](LH_D_ADMIT_TYPE.md) | `D_ADMIT_TYPE_ID` |
| `D_AMI1_METRIC_ID` | [LH_D_METRIC](LH_D_METRIC.md) | `D_METRIC_ID` |
| `D_AMI2_METRIC_ID` | [LH_D_METRIC](LH_D_METRIC.md) | `D_METRIC_ID` |
| `D_AMI3_METRIC_ID` | [LH_D_METRIC](LH_D_METRIC.md) | `D_METRIC_ID` |
| `D_AMI4_METRIC_ID` | [LH_D_METRIC](LH_D_METRIC.md) | `D_METRIC_ID` |
| `D_AMI5_METRIC_ID` | [LH_D_METRIC](LH_D_METRIC.md) | `D_METRIC_ID` |
| `D_AMI7A_METRIC_ID` | [LH_D_METRIC](LH_D_METRIC.md) | `D_METRIC_ID` |
| `D_AMI7_METRIC_ID` | [LH_D_METRIC](LH_D_METRIC.md) | `D_METRIC_ID` |
| `D_AMI8A_METRIC_ID` | [LH_D_METRIC](LH_D_METRIC.md) | `D_METRIC_ID` |
| `D_AMI8_METRIC_ID` | [LH_D_METRIC](LH_D_METRIC.md) | `D_METRIC_ID` |
| `D_AMI9_METRIC_ID` | [LH_D_METRIC](LH_D_METRIC.md) | `D_METRIC_ID` |
| `D_AMIT1_METRIC_ID` | [LH_D_METRIC](LH_D_METRIC.md) | `D_METRIC_ID` |
| `D_AMIT2_METRIC_ID` | [LH_D_METRIC](LH_D_METRIC.md) | `D_METRIC_ID` |
| `D_ATTEND_PRSNL_ID` | [LH_D_PERSONNEL](LH_D_PERSONNEL.md) | `D_PRSNL_ID` |
| `D_DISCHARGE_BUILDING_ID` | [LH_D_BUILDING](LH_D_BUILDING.md) | `D_BUILDING_ID` |
| `D_DISCHARGE_FACILITY_ID` | [LH_D_FACILITY](LH_D_FACILITY.md) | `D_FACILITY_ID` |
| `D_DISCHARGE_NURSE_UNIT_ID` | [LH_D_NURSE_UNIT](LH_D_NURSE_UNIT.md) | `D_NURSE_UNIT_ID` |
| `D_DISCH_DISP_ID` | [LH_D_DISCH_DISP](LH_D_DISCH_DISP.md) | `D_DISCH_DISP_ID` |
| `D_ENCNTR_TYPE_ID` | [LH_D_ENCNTR_TYPE](LH_D_ENCNTR_TYPE.md) | `D_ENCNTR_TYPE_ID` |
| `D_MED_SERVICE_ID` | [LH_D_MED_SERVICE](LH_D_MED_SERVICE.md) | `D_MED_SERVICE_ID` |
| `D_PERSON_ID` | [LH_D_PERSON](LH_D_PERSON.md) | `D_PERSON_ID` |
| `D_PRIN_DIAGNOSIS_ID` | [LH_D_DIAGNOSIS](LH_D_DIAGNOSIS.md) | `D_DIAGNOSIS_ID` |
| `D_PRIN_PROCEDURE_ID` | [LH_D_PROCEDURE](LH_D_PROCEDURE.md) | `D_PROCEDURE_ID` |
| `HEALTH_SYSTEM_SOURCE_ID` | [LH_D_ADMIT_SRC](LH_D_ADMIT_SRC.md) | `HEALTH_SYSTEM_SOURCE_ID` |
| `HEALTH_SYSTEM_SOURCE_ID` | [LH_D_ADMIT_TYPE](LH_D_ADMIT_TYPE.md) | `HEALTH_SYSTEM_SOURCE_ID` |
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

