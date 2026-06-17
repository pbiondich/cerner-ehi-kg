# LH_F_ACUTE_PAIN_METRICS

> This table is used to store Acute pain Management . This table is at the encounter grain.

**Description:** LH_F_ACUTE_PAIN_METRICS  
**Table type:** ACTIVITY  
**Primary key:** _(not published — see note)_  
**Columns:** 156

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ACCEPT_OUTCOME_IND` | DOUBLE |  |  | Identifies plan of care outcome event indicative of Acceptable Pain Intensity |
| 2 | `ACTIVE_IND` | DOUBLE |  |  | The table row is active or inactive. A row is generally active unless it is in an inactive state such as logically deleted, combined away, pending purge, etc. |
| 3 | `ADMIT_DT_TM` | DATETIME |  |  | The date/time on which the patient was admitted |
| 4 | `ADMIT_UTC_DT_TM` | DATETIME |  |  | The date/time on which the patient was admitted normalized to GMT. |
| 5 | `ADVERSE_INTERVENTION_IND` | DOUBLE |  |  | indicates intervention(s) performed due to opioid adverse effects |
| 6 | `AGE_CRITERIA_FLAG` | DOUBLE |  |  | Age categorized as 1 -Adult, 2-Pediatric, 3-Neonate, 4-Preterm Neonate |
| 7 | `ARRIVAL_DT_TM` | DATETIME |  |  | The date/time on which the patient arrived at the facility. |
| 8 | `ARRIVAL_UTC_DT_TM` | DATETIME |  |  | The date/time on which the patient arrived at the facility normalized to GMT. |
| 9 | `ASMT24H_ARRIVAL_CNT` | DOUBLE |  |  | Number of pain assessments documented within 24 hours of patient admission |
| 10 | `ASMT_BTWN_EPISODE_IND` | DOUBLE |  |  | Identifies if pain present assessments are documented within recommended time interval of pain episode |
| 11 | `BEHAVIOR_REDUCED_IND` | DOUBLE |  |  | Identifies plan of care outcome event indicative of Pain Associated Behaviors Reduced |
| 12 | `CAREGIVER_MED_IND` | DOUBLE |  |  | Identifies plan of care outcome indicative of Caregiver Verbalizes Accurate Medication Admin Routine |
| 13 | `COMM_MRN_TXT` | VARCHAR(50) |  |  | Identifies the community medical record number of the patient. |
| 14 | `COMP24H_ASMT_CNT` | DOUBLE |  |  | Number of comprehensive pain assessments documented by same personnel within 24 hours of patient admission for those who are able to self report pain |
| 15 | `COMP_ASMT_DAYS_CNT` | DOUBLE |  |  | Number of days all comprehensive pain assessments are documented by same personnel for full calendar days when pain is present |
| 16 | `DAILY_ASMT_IND` | DOUBLE |  |  | Identifies if patient was given recommended frequency of pain assessments for full calendar days |
| 17 | `DAILY_PAIN_ASMT_NUM` | DOUBLE |  |  | The recommended frequency of pain assessment for full calendar day based on age of patient |
| 18 | `DEF_COMP_FILTERS_CNT` | DOUBLE |  |  | Number of distinct bedrock filters defined for comprehensive pain assessment |
| 19 | `DENOMINATOR_10_IND` | DOUBLE |  |  | Identifies if the encounter is in the Denominator for metric of patients with actual or suspected pain on opioid therapy who developed an adverse effect |
| 20 | `DENOMINATOR_11_IND` | DOUBLE |  |  | Identifies if the encounter is in the Denominator for metric of patients with actual or suspected pain on opioid therapy who developed an adverse effect requiring intervention |
| 21 | `DENOMINATOR_12_IND` | DOUBLE |  |  | Identifies if the encounter is in the Denominator for metric of patients with actual or suspected pain who were on a pain management plan within X hours of pain-present |
| 22 | `DENOMINATOR_13_IND` | DOUBLE |  |  | Identifies if the encounter is in the Denominator for metric of patients with actual or suspected pain who received pharmacologic and non-pharmacologic therapy per hospital protocol |
| 23 | `DENOMINATOR_14_IND` | DOUBLE |  |  | Identifies if the encounter is in the Denominator for metric of patients on pain plan of care who received pain management education |
| 24 | `DENOMINATOR_15_IND` | DOUBLE |  |  | Identifies if the encounter is in the Denominator for metric of patients on pain plan of care who received pain medication education |
| 25 | `DENOMINATOR_16_IND` | DOUBLE |  |  | Identifies if the encounter is in the Denominator for metric of patients on pain plan of care who self-report pain with acceptable pain intensity |
| 26 | `DENOMINATOR_17_IND` | DOUBLE |  |  | Identifies if the encounter is in the Denominator for metric of patients on pain plan of care who were unable to self report pain with reduction in pain associated behaviors |
| 27 | `DENOMINATOR_18_IND` | DOUBLE |  |  | Identifies if the encounter is in the Denominator for metric of patients on pain plan of care who were unable to self report pain whose caregiver understood discharge medication administration routine |
| 28 | `DENOMINATOR_1_IND` | DOUBLE |  |  | Identifies if the encounter is in the Denominator for metric of patients with actual or suspected pain |
| 29 | `DENOMINATOR_2_IND` | DOUBLE |  |  | Identifies if the encounter is in the Denominator for metric of patients who received a pain assessment X times per day |
| 30 | `DENOMINATOR_3_IND` | DOUBLE |  |  | Identifies if the encounter is in the Denominator for metric of patients with actual or suspected pain who received a daily comprehensive pain assessment |
| 31 | `DENOMINATOR_4_IND` | DOUBLE |  |  | Identifies if the encounter is in the Denominator for metric of patients with actual or suspected pain who were reassessed for pain per hospital protocol |
| 32 | `DENOMINATOR_5_IND` | DOUBLE |  |  | Identifies if the encounter is in the Denominator for metric of non-pharmacological interventions where pain was reassessed per hospital protocol |
| 33 | `DENOMINATOR_6_IND` | DOUBLE |  |  | Identifies if the encounter is in the Denominator for metric of opioid administrations where pain was reassessed per hospital protocol |
| 34 | `DENOMINATOR_7_IND` | DOUBLE |  |  | Identifies if the encounter is in the Denominator for metric of opioid administrations where pain was reassessed per hospital protocol and had effective pharmacological response |
| 35 | `DENOMINATOR_8_IND` | DOUBLE |  |  | Identifies if the encounter is in the Denominator for metric of patients on opioid therapy identified at high risk of opioid induced respiratory depression prior to over sedation |
| 36 | `DENOMINATOR_9_IND` | DOUBLE |  |  | Identifies if the encounter is in the Denominator for metric of patients on opioid therapy identified at high risk of opioid induced respiratory depression who had a sedation and respiratory assessment every 1 hour for the first 12 hours and every 2 hours for the second 12 hours |
| 37 | `DISCHARGE_DT_TM` | DATETIME |  |  | The date/time on which the patient was discharged. |
| 38 | `DISCHARGE_UTC_DT_TM` | DATETIME |  |  | The date/time on which the patient was discharged normalized to GMT. |
| 39 | `D_ADMIT_BUILDING_ID` | DOUBLE | NOT NULL | FK→ | The building to which the patient was admitted. |
| 40 | `D_ADMIT_FACILITY_ID` | DOUBLE | NOT NULL | FK→ | The facility to which the patient was admitted. |
| 41 | `D_ADMIT_NURSE_UNIT_ID` | DOUBLE | NOT NULL | FK→ | The nurse unit to which the patient was admitted. |
| 42 | `D_ADMIT_SRC_ID` | DOUBLE | NOT NULL | FK→ | Identifies the place from which the patient came before being admitted. |
| 43 | `D_ADMIT_TYPE_ID` | DOUBLE | NOT NULL | FK→ | Indicates the circumstances under which the patient was admitted. |
| 44 | `D_ATTEND_PRSNL_ID` | DOUBLE | NOT NULL | FK→ | Identifies the final attending physician associated to the encounter. |
| 45 | `D_DISCHARGE_BUILDING_ID` | DOUBLE | NOT NULL | FK→ | The building from which the patient was discharged |
| 46 | `D_DISCHARGE_FACILITY_ID` | DOUBLE | NOT NULL | FK→ | The facility from which the patient was discharged |
| 47 | `D_DISCHARGE_NURSE_UNIT_ID` | DOUBLE | NOT NULL | FK→ | The nurse unit from which the patient was discharged |
| 48 | `D_DISCH_DISP_ID` | DOUBLE | NOT NULL | FK→ | Identifies the discharge disposition of the encounter |
| 49 | `D_ENCNTR_TYPE_ID` | DOUBLE | NOT NULL | FK→ | Categorizes the encounter into a logical group or type. |
| 50 | `D_FINANCIAL_CLASS_ID` | DOUBLE | NOT NULL | FK→ | Identifies the financial class of the encounter during registration |
| 51 | `D_MED_SERVICE_ID` | DOUBLE | NOT NULL | FK→ | The type or category of medical service that the patient is receiving in relation to their encounter. The category may be treatment type surgery general resources or others. |
| 52 | `D_PERSON_ID` | DOUBLE | NOT NULL | FK→ | The person that qualified for the quality metric. |
| 53 | `ENCNTR_CLASS_FILTER` | VARCHAR(20) |  |  | Identifies if the patient is classified within the category of 'INPATIENT', 'OBSERVATION' and 'EMERGENCY' |
| 54 | `ENCNTR_ID` | DOUBLE | NOT NULL |  | Identifies the encounter against which the quality measure is associated. Foreign key to the ENCOUNTER table. |
| 55 | `END_CAL_DT_TM` | DATETIME |  |  | the date/time of End of the full calendar day (day before discharge or current date) |
| 56 | `EXCLUDE_10_IND` | DOUBLE |  |  | Identifies if the encounter is in the Exclude for metric of patients with actual or suspected pain on opioid therapy who developed an adverse effect |
| 57 | `EXCLUDE_11_IND` | DOUBLE |  |  | Identifies if the encounter is in the Exclude for metric of patients with actual or suspected pain on opioid therapy who developed an adverse effect requiring intervention |
| 58 | `EXCLUDE_12_IND` | DOUBLE |  |  | Identifies if the encounter is in the Exclude for metric of patients with actual or suspected pain who were on a pain management plan within X hours of pain-present |
| 59 | `EXCLUDE_13_IND` | DOUBLE |  |  | Identifies if the encounter is in the Exclude for metric of patients with actual or suspected pain who received pharmacologic and non-pharmacologic therapy per hospital protocol |
| 60 | `EXCLUDE_14_IND` | DOUBLE |  |  | Identifies if the encounter is in the Exclude for metric of patients on pain plan of care who received pain management education |
| 61 | `EXCLUDE_15_IND` | DOUBLE |  |  | Identifies if the encounter is in the Exclude for metric of patients on pain plan of care who received pain medication education |
| 62 | `EXCLUDE_16_IND` | DOUBLE |  |  | Identifies if the encounter is in the Exclude for metric of patients on pain plan of care who self-report pain with acceptable pain intensity |
| 63 | `EXCLUDE_17_IND` | DOUBLE |  |  | Identifies if the encounter is in the Exclude for metric of patients on pain plan of care who were unable to self report pain with reduction in pain associated behaviors |
| 64 | `EXCLUDE_18_IND` | DOUBLE |  |  | Identifies if the encounter is in the Denominator for metric of patients on pain plan of care who were unable to self report pain whose caregiver understood discharge medication administration routine |
| 65 | `EXCLUDE_3_IND` | DOUBLE |  |  | Identifies if the encounter is in the Exclude for metric of patients with actual or suspected pain who received a daily comprehensive pain assessment |
| 66 | `EXCLUDE_4_IND` | DOUBLE |  |  | Identifies if the encounter is in the Exclude for metric of patients with actual or suspected pain who were reassessed for pain per hospital protocol |
| 67 | `EXCLUDE_5_IND` | DOUBLE |  |  | Identifies if the encounter is in the Exclude for metric of non-pharmacological interventions where pain was reassessed per hospital protocol |
| 68 | `EXCLUDE_6_IND` | DOUBLE |  |  | Identifies if the encounter is in the Exclude for metric of opioid administrations where pain was reassessed per hospital protocol |
| 69 | `EXCLUDE_7_IND` | DOUBLE |  |  | Identifies if the encounter is in the Exclude for metric of opioid administrations where pain was reassessed per hospital protocol and had effective pharmacological response |
| 70 | `EXCLUDE_8_IND` | DOUBLE |  |  | Identifies if the encounter is in the Exclude for metric of patients on opioid therapy identified at high risk of opioid induced respiratory depression prior to over sedation |
| 71 | `EXCLUDE_9_IND` | DOUBLE |  |  | Identifies if the encounter is in the Exclude for metric of patients on opioid therapy identified at high risk of opioid induced respiratory depression who had a sedation and respiratory assessment every 1 hour for the first 12 hours and every 2 hours for the second 12 hours |
| 72 | `EXTRACT_DT_TM` | DATETIME |  |  | The date/time that the record was extracted from the source system. |
| 73 | `FINANCIAL_NBR_TXT` | VARCHAR(50) |  |  | The financial number alias associated to the encounter. |
| 74 | `FIRST_PROCESS_DT_TM` | DATETIME |  |  | The date/time that the first ETL process started that created this record. |
| 75 | `FULL_CAL_DAYS` | DOUBLE |  |  | Number of full calendar Days (greater than 2 days) patient stayed in hospital (excluding admit, discharge or current date) |
| 76 | `HEALTH_SYSTEM_ID` | DOUBLE | NOT NULL |  | Identifies the delivery network responsible for supplying the data |
| 77 | `HEALTH_SYSTEM_SOURCE_ID` | DOUBLE | NOT NULL | FK→ | Identifies the unique source within the delivery network responsible for supplying the data. |
| 78 | `IPOC_INITIATED_DT_TM` | DATETIME |  |  | The date/time pain plan of care was initiated for patient |
| 79 | `IPOC_INITIATED_UTC_DT_TM` | DATETIME |  |  | The date/time pain plan of care was initiated for patient normalized to GMT |
| 80 | `LAST_PROCESS_DT_TM` | DATETIME |  |  | The date/time that the last ETL process started that updated this record. |
| 81 | `LAST_SELF_RPT_DT_TM` | DATETIME |  |  | the date/time last able to self report pain response documented for patient |
| 82 | `LAST_SELF_RPT_UTC_DT_TM` | DATETIME |  |  | the date/time last able to self report pain response documented for patient normalized to GMT |
| 83 | `LAST_UNABLE_RPT_DT_TM` | DATETIME |  |  | the date/time last unable to self report pain response documented for patient |
| 84 | `LAST_UNABLE_RPT_UTC_DT_TM` | DATETIME |  |  | the date/time last unable to self report pain response documented for patient normalized to GMT |
| 85 | `LH_F_ACUTE_PAIN_METRICS_ID` | DOUBLE | NOT NULL |  | Unique generated number that identifies a single row on the LH_F_ACUTE_PAIN_METRICS table. |
| 86 | `LOGICAL_DOMAIN_ID` | DOUBLE | NOT NULL |  | The unique identifier for a logical domain. This identifier allows the data to be grouped by logical domain. For example, If you assign clients a logical_domain_id this would allow you to store data for multiple clients on this table. |
| 87 | `MED_EFFECTIVE_IND` | DOUBLE |  |  | Identifies if any medication effective response is documented |
| 88 | `MED_EFFECT_IM_FLAG` | DOUBLE |  |  | Identifies if medication effective response is documented after opioid medication is administered via intramuscular route. 1-any response 2-yes response |
| 89 | `MED_EFFECT_IV_FLAG` | DOUBLE |  |  | Identifies if medication effective response is documented after opioid medication is administered via intraveinal route. 1-response is 'NO', 2-response is 'YES' |
| 90 | `MED_EFFECT_PO_FLAG` | DOUBLE |  |  | Identifies if medication effective response is documented after opioid medication is administered via oral route. 1-any response 2-yes response |
| 91 | `MED_EFFECT_RESPONSE_IND` | DOUBLE |  |  | Identifies if documented medication effective response was yes |
| 92 | `NON_PHARM_COMFORT_CNT` | DOUBLE |  |  | Number of times non pharmacological therapy and comfort measures were documented |
| 93 | `NON_PHARM_COMFORT_IND` | DOUBLE |  |  | identifies if non pharmacological therapy or comfort measures are documented |
| 94 | `NUMERATOR_10_IND` | DOUBLE |  |  | Identifies if the encounter is in the Numerator for metric of patients with actual or suspected pain on opioid therapy who developed an adverse effect |
| 95 | `NUMERATOR_11_IND` | DOUBLE |  |  | Identifies if the encounter is in the Numerator for metric of patients with actual or suspected pain on opioid therapy who developed an adverse effect requiring intervention |
| 96 | `NUMERATOR_12_IND` | DOUBLE |  |  | Identifies if the encounter is in the Numerator for metric of patients with actual or suspected pain who were on a pain management plan within X hours of pain-present |
| 97 | `NUMERATOR_13_IND` | DOUBLE |  |  | Identifies if the encounter is in the Numerator for metric of patients with actual or suspected pain who received pharmacologic and non-pharmacologic therapy per hospital protocol |
| 98 | `NUMERATOR_14_IND` | DOUBLE |  |  | Identifies if the encounter is in the Numerator for metric of patients on pain plan of care who received pain management education |
| 99 | `NUMERATOR_15_IND` | DOUBLE |  |  | Identifies if the encounter is in the Numerator for metric of patients on pain plan of care who received pain medication education |
| 100 | `NUMERATOR_16_IND` | DOUBLE |  |  | Identifies if the encounter is in the Numerator for metric of patients on pain plan of care who self-report pain with acceptable pain intensity |
| 101 | `NUMERATOR_17_IND` | DOUBLE |  |  | Identifies if the encounter is in the Numerator for metric of patients on pain plan of care who were unable to self report pain with reduction in pain associated behaviors |
| 102 | `NUMERATOR_18_IND` | DOUBLE |  |  | Identifies if the encounter is in the Numerator for metric of patients on pain plan of care who were unable to self report pain whose caregiver understood discharge medication administration routine |
| 103 | `NUMERATOR_1_IND` | DOUBLE |  |  | Identifies if the encounter is in the Numerator for metric of patients with actual or suspected pain |
| 104 | `NUMERATOR_2_IND` | DOUBLE |  |  | Identifies if the encounter is in the Numerator for metric of patients who received a pain assessment X times per day |
| 105 | `NUMERATOR_3_IND` | DOUBLE |  |  | Identifies if the encounter is in the Numerator for metric of patients with actual or suspected pain who received a daily comprehensive pain assessment |
| 106 | `NUMERATOR_4_IND` | DOUBLE |  |  | Identifies if the encounter is in the Numerator for metric of patients with actual or suspected pain who were reassessed for pain per hospital protocol |
| 107 | `NUMERATOR_5_IND` | DOUBLE |  |  | Identifies if the encounter is in the Numerator for metric of non-pharmacological interventions where pain was reassessed per hospital protocol |
| 108 | `NUMERATOR_6_IND` | DOUBLE |  |  | Identifies if the encounter is in the Numerator for metric of opioid administrations where pain was reassessed per hospital protocol |
| 109 | `NUMERATOR_7_IND` | DOUBLE |  |  | Identifies if the encounter is in the Numerator for metric of opioid administrations where pain was reassessed per hospital protocol and had effective pharmacological response |
| 110 | `NUMERATOR_8_IND` | DOUBLE |  |  | Identifies if the encounter is in the Numerator for metric of patients on opioid therapy identified at high risk of opioid induced respiratory depression prior to over sedation |
| 111 | `NUMERATOR_9_IND` | DOUBLE |  |  | Identifies if the encounter is in the Numerator for metric of patients on opioid therapy identified at high risk of opioid induced respiratory depression who had a sedation and respiratory assessment every 1 hour for the first 12 hours and every 2 hours for the second 12 hours |
| 112 | `OPIOID_ADMIN_DT_TM` | DATETIME |  |  | The date/time of initial opioid administration to a patient |
| 113 | `OPIOID_ADMIN_UTC_DT_TM` | DATETIME |  |  | The date/time of initial opioid administration to a patient normalized to GMT |
| 114 | `OPIOID_ADVERSE_IND` | DOUBLE |  |  | Identifies if patient developed adverse effects post opioid administration |
| 115 | `OPIOID_IM_ROUTE_IND` | DOUBLE |  |  | Identifies intramuscular route of opioid medication administration to a patient |
| 116 | `OPIOID_IV_ROUTE_IND` | DOUBLE |  |  | Identifies Intraveinal route of opioid medication administration to a patient |
| 117 | `OPIOID_PO_ROUTE_IND` | DOUBLE |  |  | Identifies oral route of opioid medication administration to a patient |
| 118 | `OPIOID_RESP_RISK_CNT` | DOUBLE |  |  | Number of times the event identifying risk for opioid induced respiratory depression occurred before opioid medication administration |
| 119 | `ORG_MRN_TXT` | VARCHAR(50) |  |  | Identifies the medical record number of the patient. |
| 120 | `OVERSEDATION_CNT` | DOUBLE |  |  | Identifies the number of times the patient was over-sedated during the visit. |
| 121 | `OVER_SED_DT_TM` | DATETIME |  |  | The date/time of initial event which indicates over sedation for patient on opioid therapy |
| 122 | `OVER_SED_UTC_DT_TM` | DATETIME |  |  | The date/time of initial event which indicates over sedation for patient on opioid therapy normalized to GMT |
| 123 | `PAIN_ASMT_INTERVAL` | DOUBLE |  |  | Time interval in hours that is recommended for a pain to be reassessed for patient per pain episode |
| 124 | `PAIN_DAYS_CNT` | DOUBLE |  |  | Number of days Pain present assessments documented daily for full calendar days |
| 125 | `PAIN_EPISODE_CNT` | DOUBLE |  |  | Number of pain episodes in an ecounter.Pain episode is the time interval between pain is present date/time and pain not present date/time |
| 126 | `PAIN_MED_EDU_IND` | DOUBLE |  |  | Indicates if the patient, family, or caregiver received pain medication education |
| 127 | `PAIN_MGMT_EDU_IND` | DOUBLE |  |  | Indicates if the patient, family, or caregiver received pain management education |
| 128 | `PAIN_MGMT_ORDER_DT_TM` | DATETIME |  |  | The date/time pain management order was documented for patient |
| 129 | `PAIN_MGMT_ORDER_UTC_DT_TM` | DATETIME |  |  | The date/time pain management order was documented normalized to GMT |
| 130 | `PAIN_NOT_PRESENT_IND` | DOUBLE |  |  | Identifies if the patient has no actual or suspected pain. |
| 131 | `PAIN_PRESENT_DT_TM` | DATETIME |  |  | The initial date/time on which the patient had actual or suspected pain. |
| 132 | `PAIN_PRESENT_IND` | DOUBLE |  |  | Identifies if the patient has actual or suspected pain. |
| 133 | `PAIN_PRESENT_UTC_DT_TM` | DATETIME |  |  | The initial date/time on which the patient had actual or suspected pain normalized to GMT |
| 134 | `PAIN_PRIOR_NON_PHARM_IND` | DOUBLE |  |  | Pain present assessment documented prior to non pharmacological therapy or comfort measures |
| 135 | `PAIN_PRIOR_OPIOID_IM_IND` | DOUBLE |  |  | Pain present assessment documented prior to intramuscular route of opioid administration |
| 136 | `PAIN_PRIOR_OPIOID_IV_IND` | DOUBLE |  |  | Pain present assessment documented prior to Intraveinal route of opioid administration |
| 137 | `PAIN_PRIOR_OPIOID_PO_IND` | DOUBLE |  |  | Pain present assessment documented prior to oral route of opioid administration |
| 138 | `PHARM_THERAPY_CNT` | DOUBLE |  |  | Number of times pharmacological therapy were documented |
| 139 | `PHARM_THERAPY_IND` | DOUBLE |  |  | identifies if pharmacological therapy is documented |
| 140 | `PHARM_WTH_NON_PHARM_IND` | DOUBLE |  |  | Identifies if non pharmacological therapy or comfort measures are documented within a recommended timeframe after each pharmacological therapy |
| 141 | `POPULATION_IND` | DOUBLE |  |  | Identifies if the encounter is qualified initial population for Acute Pain Management |
| 142 | `POSTMENSTRUAL_AGE` | VARCHAR(255) |  |  | The postmenstrual age of preterm neonate patient |
| 143 | `POWER_PLAN_TMFRM` | DOUBLE |  |  | Timeframe in minutes recommended for pain management plan to be initiated once pain present is documented |
| 144 | `REASMT_NON_PHARM_IND` | DOUBLE |  |  | Pain reassessed within recommended timeframe after non pharmacological therapy or comfort measures are given to patient |
| 145 | `REASMT_NON_PHARM_TMFRM` | DOUBLE |  |  | Timeframe in minutes recommended for pain reassessment after non pharmacological therapy or comfort measures are given to patient |
| 146 | `RESP_RISK_DT_TM` | DATETIME |  |  | The date/time of initial event which identifies patient is at high risk of opioid induced respiratory depression |
| 147 | `RESP_RISK_UTC_DT_TM` | DATETIME |  |  | The date/time of initial event which identifies patient is at high risk of opioid induced respiratory depression normalized to GMT |
| 148 | `SEDATION_DAYS_CNT` | DOUBLE |  |  | Identifies the number of sedation days during the visit. |
| 149 | `SED_RESP_ASMT12H_CNT` | DOUBLE |  |  | Number of times recommended sedation and respiratory assessments were documented every 1 hour for the first 12hours after opioid administration |
| 150 | `SED_RESP_ASMT24H_CNT` | DOUBLE |  |  | Number of times recommended sedation and respiratory assessments were documented every 2 hour from 12th to 24th hour after opioid administration |
| 151 | `START_CAL_DT_TM` | DATETIME |  |  | the date/time of Start of the full calendar day (day after admission date) |
| 152 | `UNABLE_RPT_PAIN24H_IND` | DOUBLE |  |  | Pain documented within 24 hours of patient admission for those who are unable to self report |
| 153 | `UPDT_CNT` | DOUBLE |  |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 154 | `UPDT_DT_TM` | DATETIME |  |  | The date and time the row was last inserted or updated. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 155 | `UPDT_SOURCE` | VARCHAR(50) | NOT NULL |  | The script name responsible for updating the record. |
| 156 | `UPDT_TASK` | VARCHAR(50) | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |

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
| `D_DISCHARGE_BUILDING_ID` | [LH_D_BUILDING](LH_D_BUILDING.md) | `D_BUILDING_ID` |
| `D_DISCHARGE_FACILITY_ID` | [LH_D_FACILITY](LH_D_FACILITY.md) | `D_FACILITY_ID` |
| `D_DISCHARGE_NURSE_UNIT_ID` | [LH_D_NURSE_UNIT](LH_D_NURSE_UNIT.md) | `D_NURSE_UNIT_ID` |
| `D_DISCH_DISP_ID` | [LH_D_DISCH_DISP](LH_D_DISCH_DISP.md) | `D_DISCH_DISP_ID` |
| `D_ENCNTR_TYPE_ID` | [LH_D_ENCNTR_TYPE](LH_D_ENCNTR_TYPE.md) | `D_ENCNTR_TYPE_ID` |
| `D_FINANCIAL_CLASS_ID` | [LH_D_FINANCIAL_CLASS](LH_D_FINANCIAL_CLASS.md) | `D_FINANCIAL_CLASS_ID` |
| `D_MED_SERVICE_ID` | [LH_D_MED_SERVICE](LH_D_MED_SERVICE.md) | `D_MED_SERVICE_ID` |
| `D_PERSON_ID` | [LH_D_PERSON](LH_D_PERSON.md) | `D_PERSON_ID` |
| `HEALTH_SYSTEM_SOURCE_ID` | [LH_D_ADMIT_SRC](LH_D_ADMIT_SRC.md) | `HEALTH_SYSTEM_SOURCE_ID` |
| `HEALTH_SYSTEM_SOURCE_ID` | [LH_D_ADMIT_TYPE](LH_D_ADMIT_TYPE.md) | `HEALTH_SYSTEM_SOURCE_ID` |
| `HEALTH_SYSTEM_SOURCE_ID` | [LH_D_BUILDING](LH_D_BUILDING.md) | `HEALTH_SYSTEM_SOURCE_ID` |
| `HEALTH_SYSTEM_SOURCE_ID` | [LH_D_BUILDING](LH_D_BUILDING.md) | `HEALTH_SYSTEM_SOURCE_ID` |
| `HEALTH_SYSTEM_SOURCE_ID` | [LH_D_DISCH_DISP](LH_D_DISCH_DISP.md) | `HEALTH_SYSTEM_SOURCE_ID` |
| `HEALTH_SYSTEM_SOURCE_ID` | [LH_D_ENCNTR_TYPE](LH_D_ENCNTR_TYPE.md) | `HEALTH_SYSTEM_SOURCE_ID` |
| `HEALTH_SYSTEM_SOURCE_ID` | [LH_D_FACILITY](LH_D_FACILITY.md) | `HEALTH_SYSTEM_SOURCE_ID` |
| `HEALTH_SYSTEM_SOURCE_ID` | [LH_D_FACILITY](LH_D_FACILITY.md) | `HEALTH_SYSTEM_SOURCE_ID` |
| `HEALTH_SYSTEM_SOURCE_ID` | [LH_D_FINANCIAL_CLASS](LH_D_FINANCIAL_CLASS.md) | `HEALTH_SYSTEM_SOURCE_ID` |
| `HEALTH_SYSTEM_SOURCE_ID` | [LH_D_MED_SERVICE](LH_D_MED_SERVICE.md) | `HEALTH_SYSTEM_SOURCE_ID` |
| `HEALTH_SYSTEM_SOURCE_ID` | [LH_D_NURSE_UNIT](LH_D_NURSE_UNIT.md) | `HEALTH_SYSTEM_SOURCE_ID` |
| `HEALTH_SYSTEM_SOURCE_ID` | [LH_D_NURSE_UNIT](LH_D_NURSE_UNIT.md) | `HEALTH_SYSTEM_SOURCE_ID` |
| `HEALTH_SYSTEM_SOURCE_ID` | [LH_D_PERSON](LH_D_PERSON.md) | `HEALTH_SYSTEM_SOURCE_ID` |
| `HEALTH_SYSTEM_SOURCE_ID` | [LH_D_PERSONNEL](LH_D_PERSONNEL.md) | `HEALTH_SYSTEM_SOURCE_ID` |

