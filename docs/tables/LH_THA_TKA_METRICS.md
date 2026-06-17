# LH_THA_TKA_METRICS

> This table contains encounter information for THA/TKA measures.

**Description:** Lighthouse Total Hip Arthroplasty and Total Knee Arthroplasty Metrics  
**Table type:** ACTIVITY  
**Primary key:** _(not published — see note)_  
**Columns:** 104

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ADMSN_DT_TM` | DATETIME |  |  | The date and time (local) when patient admission is documented. |
| 2 | `ADMSN_UTC_DT_TM` | DATETIME |  |  | The date and time (UTC) when patient admission is documented. |
| 3 | `BACK_PAIN_FLAG` | DOUBLE |  |  | Identifies patient reported back pain. None (= 0), Mild (=1), Moderate (=2), Severe (=3), Very Severe (=4) , Worst Imaginable (=5) report. |
| 4 | `BACK_PAIN_TXT` | VARCHAR(50) |  |  | Identifies if the patient has back pain. |
| 5 | `BMI_NBR` | DOUBLE |  |  | Identifies the Body Mass Index of the patient. |
| 6 | `BR_DATAMART_CATEGORY_ID` | DOUBLE |  |  | Identifies the Category (i.e. Inpatient THA/TKA PRO-PM). Foreign Key to BR_DATAMART_CATEGORY |
| 7 | `COLLECTION_DT_TM` | DATETIME |  |  | Survey collection date and time (local) of the patient encounter. |
| 8 | `COLLECTION_MD_FLAG` | DOUBLE |  |  | Identifies mode of collection Paper (= 0), Telephone (=1), Electronic (=3) and None(= 999) report. |
| 9 | `COLLECTION_MD_TXT` | VARCHAR(100) |  |  | Identifies the mode of survey collection for the patient. |
| 10 | `COLLECTION_UTC_DT_TM` | DATETIME |  |  | Survey collection date and time (UTC) of the patient encounter. |
| 11 | `DATE_OF_BIRTH` | DATETIME |  |  | Birth date and time of the patient. |
| 12 | `D_ATTEND_PRSNL_ID` | DOUBLE | NOT NULL | FK→ | SEQUENCE NAME:REFERENCE_SEQ Identifies the final attending physician associated to the patient encounter. |
| 13 | `D_BR_CCN_ID` | DOUBLE | NOT NULL | FK→ | SEQUENCE NAME:REFERENCE_SEQ CMS Certification Number. Foreign key to LH_D_BR_CCN. |
| 14 | `D_BR_HCO_ID` | DOUBLE | NOT NULL | FK→ | SEQUENCE NAME:REFERENCE_SEQ Healthcare Organization Number. Foreign key to LH_D_BR_HCO. |
| 15 | `D_DISCH_BUILDING_ID` | DOUBLE | NOT NULL | FK→ | SEQUENCE NAME:REFERENCE_SEQ The building from which the patient encounterwas discharged. |
| 16 | `D_DISCH_FACILITY_ID` | DOUBLE | NOT NULL | FK→ | SEQUENCE NAME:REFERENCE_SEQ The facility from which the patient encounter was discharged. |
| 17 | `D_DISCH_NURSE_UNIT_ID` | DOUBLE | NOT NULL | FK→ | SEQUENCE NAME:REFERENCE_SEQ The nurse unit from which the patient encounter was discharged. |
| 18 | `D_PERSON_ID` | DOUBLE | NOT NULL | FK→ | SEQUENCE NAME:REFERENCE_SEQ Identifies the person associated with the quality measure. Foreign key to the LH_D_PERSON. |
| 19 | `ENCNTR_ID` | DOUBLE | NOT NULL |  | SEQUENCE NAME:ENCOUNTER_ONLY_SEQ Identifies the encounter against which the quality measure is associated. Foreign key to the ENCOUNTER table. |
| 20 | `ENC_TYPE_TXT` | VARCHAR(50) |  |  | Discharge encounter type of the patient encounter. |
| 21 | `ETHNICITY_TXT` | VARCHAR(50) |  |  | Ethniticy/Ethnicities of the patient. |
| 22 | `EXTRACT_DT_TM` | DATETIME |  |  | the date/time that the record was extracted from the source system. |
| 23 | `FINANCIAL_NBR_TXT` | VARCHAR(50) |  |  | The financial number alias associated to the encounter. |
| 24 | `GENDER_TXT` | VARCHAR(50) |  |  | Gender of the patient. |
| 25 | `GEN_PROM_FLAG` | DOUBLE |  |  | Identifies Generic prom version VR-12 (= 1), PROMIS-Global version 1.1 (=2), PROMIS-Global version 1.12 (=3) and None(= 999) report. |
| 26 | `GEN_PROM_TXT` | VARCHAR(100) |  |  | Identifies the generic prom version of the patient. |
| 27 | `HEALTH_SYSTEM_ID` | DOUBLE | NOT NULL |  | Identifies the delivery network responsible for supplying the data. |
| 28 | `HEALTH_SYSTEM_SOURCE_ID` | DOUBLE | NOT NULL | FK→ | Identifies the unique source within the delivery network responsible for supplying the data. |
| 29 | `HEIGHT_NBR` | DOUBLE |  |  | Identifies the height of the patient. |
| 30 | `HLTH_LITERACY_FLAG` | DOUBLE |  |  | Identifies health litracy screeneing questionnaire response Not at all (= 0), A little bit (=1), Somewhat (=2), Quite a bit (=3), Extremely (=4) and None(= 999) report. |
| 31 | `HLTH_LITERACY_TXT` | VARCHAR(50) |  |  | Identifies the health literacy of the person who takes the survey. |
| 32 | `HOOSJRQ1_STAIRS_FLAG` | DOUBLE |  |  | Identifies hip pain when going up and down in stairs. None (= 0), Mild (=1), Moderate (=2), Severe (=3), Extreme (=4) report. |
| 33 | `HOOSJRQ1_STAIRS_TXT` | VARCHAR(50) |  |  | Identifies if the patient has hip pain in the last week going up or down stairs. |
| 34 | `HOOSJRQ2_WALKING_FLAG` | DOUBLE |  |  | Identifies hip pain when walking. None (= 0), Mild (=1), Moderate (=2), Severe (=3), Extreme (=4) report. |
| 35 | `HOOSJRQ2_WALKING_TXT` | VARCHAR(50) |  |  | Identifies if the patient has hip pain in the last week walking on an uneven surafce. |
| 36 | `HOOSJRQ3_RISING_FLAG` | DOUBLE |  |  | Identifies hip pain when rising. None (= 0), Mild (=1), Moderate (=2), Severe (=3), Extreme (=4) report. |
| 37 | `HOOSJRQ3_RISING_TXT` | VARCHAR(50) |  |  | Identifies if the patient has hip pain in the last week when rising from sitting. |
| 38 | `HOOSJRQ4_BEND_FLAG` | DOUBLE |  |  | Identifies hip pain when bending. None (= 0), Mild (=1), Moderate (=2), Severe (=3), Extreme (=4) report. |
| 39 | `HOOSJRQ4_BEND_TXT` | VARCHAR(50) |  |  | Identifies if the patient has hip pain in the last week when bending. |
| 40 | `HOOSJRQ5_LYINGBED_TXT` | VARCHAR(50) |  |  | Identifies if the patient has hip pain in the last week when lying in bed. |
| 41 | `HOOSJRQ5_LYINGINBED_FLAG` | DOUBLE |  |  | Identifies hip pain when lying in bed. None (= 0), Mild (=1), Moderate (=2), Severe (=3), Extreme (=4) report. |
| 42 | `HOOSJRQ6_SITTING_FLAG` | DOUBLE |  |  | Identifies hip pain when sitting. None (= 0), Mild (=1), Moderate (=2), Severe (=3), Extreme (=4) report. |
| 43 | `HOOSJRQ6_SITTING_TXT` | VARCHAR(50) |  |  | Identifies if the patient has hip pain in the last week when sitting. |
| 44 | `ICD_10_PCS_CDE_TXT` | VARCHAR(50) |  |  | Identifies the procedure code added to the patient. |
| 45 | `KOOSJRQ1_STIFF_FLAG` | DOUBLE |  |  | Identifies knee joint stiffness. None (= 0), Mild (=1), Moderate (=2), Severe (=3), Extreme (=4) report. |
| 46 | `KOOSJRQ1_STIFF_TXT` | VARCHAR(50) |  |  | Identifies if the patient has knee joint stiffness pain in the last week. |
| 47 | `KOOSJRQ2_TWIST_FLAG` | DOUBLE |  |  | Identifies knee pain when twisting. None (= 0), Mild (=1), Moderate (=2), Severe (=3), Extreme (=4) report. |
| 48 | `KOOSJRQ2_TWIST_TXT` | VARCHAR(50) |  |  | Identifies if the patient has knee pain in the last week when twisting. |
| 49 | `KOOSJRQ3_STRAIGHTEN_FLAG` | DOUBLE |  |  | Identifies knee pain when straightening. None (= 0), Mild (=1), Moderate (=2), Severe (=3), Extreme (=4) report. |
| 50 | `KOOSJRQ3_STRAIGHTEN_TXT` | VARCHAR(50) |  |  | Identifies if the patient has knee pain in the last week when straightening the knees. |
| 51 | `KOOSJRQ4_STAIRS_FLAG` | DOUBLE |  |  | Identifies knee pain when going up and down stairs. None (= 0), Mild (=1), Moderate (=2), Severe (=3), Extreme (=4) report. |
| 52 | `KOOSJRQ4_STAIRS_TXT` | VARCHAR(50) |  |  | Identifies if the patient has knee pain in the last week when going up or down stairs. |
| 53 | `KOOSJRQ5_UPRIGHT_FLAG` | DOUBLE |  |  | Identifies knee pain when standing upright. None (= 0), Mild (=1), Moderate (=2), Severe (=3), Extreme (=4) report. |
| 54 | `KOOSJRQ5_UPRIGHT_TXT` | VARCHAR(50) |  |  | Identifies if the patient has knee pain in the last week when standing upright. |
| 55 | `KOOSJRQ6_SITTING_FLAG` | DOUBLE |  |  | Identifies knee pain when sitting. None (= 0), Mild (=1), Moderate (=2), Severe (=3), Extreme (=4) report. |
| 56 | `KOOSJRQ6_SITTING_TXT` | VARCHAR(50) |  |  | Identifies if the patient has knee pain in the last week when sitting. |
| 57 | `KOOSJRQ7_BENDING_FLAG` | DOUBLE |  |  | Identifies knee pain when bending. None (= 0), Mild (=1), Moderate (=2), Severe (=3), Extreme (=4) report. |
| 58 | `KOOSJRQ7_BENDING_TXT` | VARCHAR(50) |  |  | Identifies if the patient has knee pain in the last week when bending. |
| 59 | `LH_THA_TKA_METRICS_ID` | DOUBLE | NOT NULL |  | Unique generated number that identifies a single row on the LH_THA_TKA_METRICS table. |
| 60 | `LOGICAL_DOMAIN_ID` | DOUBLE | NOT NULL | FK→ | The unique identifier for a logical domain. This identifier allows the data to be grouped by logical domain. For example, If you assign clients a logical_domain_id this would allow you to store data for multiple clients on this table. |
| 61 | `MBI_TXT` | VARCHAR(50) |  |  | Medicare Beneficiary Identifier (MBI) number for the patient. |
| 62 | `NARCOTIC_USE_FLAG` | DOUBLE |  |  | Identifies chronic use of narcotics. No (= 0), Yes (=1) and None(= 999) report. |
| 63 | `NARCOTIC_USE_TXT` | VARCHAR(50) |  |  | Identifies if the patient is using any chronic narcotics. |
| 64 | `ORG_MRN_TXT` | VARCHAR(50) |  |  | Identifies the medical record number of the patient. |
| 65 | `OTHER_JOINT_PAIN_FLAG` | DOUBLE |  |  | Identifies patient reported pain. None (= 0), Mild (=1), Moderate (=2), Severe (=3), Extreme (=4) report. |
| 66 | `OTHER_JOINT_PAIN_TXT` | VARCHAR(50) |  |  | Identifies if the patient has any other joint pain. |
| 67 | `PAYER_TXT` | VARCHAR(50) |  |  | Payment source of the patient encounter. |
| 68 | `PRE_POST_FLAG` | DOUBLE |  |  | Identifies if the patient encounter is considered for Preoperative (= 1), Postoperative (=2) or None(= 999) survey. |
| 69 | `PROC_DT_TM` | DATETIME |  |  | Procedure date and time (local) of the patient encounter. |
| 70 | `PROC_UTC_DT_TM` | DATETIME |  |  | Procedure date and time (UTC) of the patient encounter. |
| 71 | `PROMISGLQ10R_ANXIOUS_FLAG` | DOUBLE |  |  | Identifies the patients is feeling anxious. Never(=1) ,Rarely(=2),Sometimes(=3),Often(=4), Always(=5) if version 1.1 else Always(=1), Often(=2), Sometimes(=3),Rarely (=4), Never (=5). |
| 72 | `PROMISGLQ10R_ANXIOUS_TXT` | VARCHAR(50) |  |  | Identifies the emotional problems of the patient. |
| 73 | `PROMISGLQ2_QUALITYLIFE_FLAG` | DOUBLE |  |  | Identifies the patients quality of life. Poor(=1) ,Fair(=2),Good(=3),Very Good(=4), Excellent(=5). |
| 74 | `PROMISGLQ2_QUALITYLIFE_TXT` | VARCHAR(50) |  |  | Identifies the quality of life of the patient. |
| 75 | `PROMISGLQ4_MENTALHEALTH_FLAG` | DOUBLE |  |  | Identifies the patients mental health. Poor(=1) ,Fair(=2),Good(=3),Very Good(=4), Excellent(=5). |
| 76 | `PROMISGLQ4_MENTALHEALTH_TXT` | VARCHAR(50) |  |  | Identifies the mental health of the patient. |
| 77 | `PROMISGLQ5_ACTIVITIES_FLAG` | DOUBLE |  |  | Identifies the patients satisfaction with social activities. Poor(=1) ,Fair(=2),Good(=3),Very Good(=4), Excellent(=5). |
| 78 | `PROMISGLQ5_ACTIVITIES_TXT` | VARCHAR(50) |  |  | Identifies the satisfaction ratings of the social activities of the patient. |
| 79 | `P_TYPE_FLAG` | DOUBLE |  |  | Identifies procedure type. Left Hip Replacement (= 1), Right Hip Replacement (=2), Left knee Replacement (=3), Right Knee Replacement (=4) and None(= 999) report. |
| 80 | `P_TYPE_TXT` | VARCHAR(50) |  |  | Identifies the procedure type for the patient. |
| 81 | `RACE_TXT` | VARCHAR(50) |  |  | Race(s) of the patient. |
| 82 | `RESPONDER_FLAG` | DOUBLE |  |  | Identifies person collecting survey. Self (= 0), Surrogate (=1) and None(= 999) report. |
| 83 | `RESPONDER_TXT` | VARCHAR(50) |  |  | Identifies the person who completed the survey. |
| 84 | `SAMPLE_IND` | DOUBLE |  |  | Identifies if the case is sampled. |
| 85 | `S_TYPE_FLAG` | DOUBLE |  |  | Identifies if the patient encounter is considered for Preoperative (= 1), Postoperative (=2) or None(= 999) survey. |
| 86 | `S_TYPE_TXT` | VARCHAR(50) |  |  | Identifies the patient encounter survey type. |
| 87 | `UPDT_CNT` | DOUBLE |  |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 88 | `UPDT_DT_TM` | DATETIME |  |  | The date and time the row was last inserted or updated. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 89 | `UPDT_ID` | DOUBLE |  |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 90 | `UPDT_SOURCE` | VARCHAR(50) |  |  | The script name responsible for updating the record. |
| 91 | `UPDT_TASK` | VARCHAR(50) |  |  | The registered (assigned) task number for the process that inserted or updated the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 92 | `VR_12Q4A_ACCOMPLISH_FLAG` | DOUBLE |  |  | Identifies if patient accomplished less work No, none of the time (= 1), Yes, a little of the time (=2), Yes, some of the time (=3), Yes, most of the time (=4), Yes, all of the time (=5). |
| 93 | `VR_12Q4A_ACCOMPLISH_TXT` | VARCHAR(50) |  |  | Identifies if the patient has accomplished less work in the last 4 weeks. |
| 94 | `VR_12Q4B_CAREFUL_FLAG` | DOUBLE |  |  | Identifies if patient was able to do work carefully. No, none of the time (= 1), Yes, a little of the time (=2), Yes, some of the time (=3), Yes, most of the time (=4), Yes, all of the time (=5). |
| 95 | `VR_12Q4B_CAREFUL_TXT` | VARCHAR(50) |  |  | Identifies if the patient has not carefully worked as usual in the last 4 weeks. |
| 96 | `VR_12Q6A_CALM_FLAG` | DOUBLE |  |  | Identifies if patient was calm. All of the time (= 1), Most of the time (=2), A good bit of the time (=3), A little of the time (=4), None of the time (=5). |
| 97 | `VR_12Q6A_CALM_TXT` | VARCHAR(50) |  |  | Identifies for how much time the patient is clam and peaceful in the last 4 weeks. |
| 98 | `VR_12Q6B_ENERGY_FLAG` | DOUBLE |  |  | Identifies if patient was full of energy. All of the time (= 1), Most of the time (=2), A good bit of the time (=3), Some of the time (=4),A little of the time (=5), None of the time (=6). |
| 99 | `VR_12Q6B_ENERGY_TXT` | VARCHAR(50) |  |  | Identifies for how much time the patient had a lot of energy in the last 4 weeks. |
| 100 | `VR_12Q6C_DOWN_FLAG` | DOUBLE |  |  | Identifies if patient was downhearted. All of the time (= 1), Most of the time (=2), A good bit of the time (=3), Some of the time (=4),A little of the time (=5), None of the time (=6). |
| 101 | `VR_12Q6C_DOWN_TXT` | VARCHAR(50) |  |  | Identifies for how much time the patient felt downhearted and blue in the last 4 weeks. |
| 102 | `VR_12Q7_SOCLACT_FLAG` | DOUBLE |  |  | Identifies if patient's physical health interfered with social activities. All of the time (= 1), Most of the time (=2), Some of the time (=3),A little of the time (=4), None of the time (=5). |
| 103 | `VR_12Q7_SOCLACT_TXT` | VARCHAR(50) |  |  | Identifies for how much time physical or emotional health of the patient interfered with social activities in the last 4 weeks. |
| 104 | `WEIGHT_NBR` | DOUBLE |  |  | Identifies the weight of the patient. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `D_ATTEND_PRSNL_ID` | [LH_D_PERSONNEL](LH_D_PERSONNEL.md) | `D_PRSNL_ID` |
| `D_BR_CCN_ID` | [LH_D_BR_CCN](LH_D_BR_CCN.md) | `D_BR_CCN_ID` |
| `D_BR_HCO_ID` | [LH_D_BR_HCO](LH_D_BR_HCO.md) | `D_BR_HCO_ID` |
| `D_DISCH_BUILDING_ID` | [LH_D_BUILDING](LH_D_BUILDING.md) | `D_BUILDING_ID` |
| `D_DISCH_FACILITY_ID` | [LH_D_FACILITY](LH_D_FACILITY.md) | `D_FACILITY_ID` |
| `D_DISCH_NURSE_UNIT_ID` | [LH_D_NURSE_UNIT](LH_D_NURSE_UNIT.md) | `D_NURSE_UNIT_ID` |
| `D_PERSON_ID` | [LH_D_PERSON](LH_D_PERSON.md) | `D_PERSON_ID` |
| `HEALTH_SYSTEM_SOURCE_ID` | [LH_D_BR_CCN](LH_D_BR_CCN.md) | `HEALTH_SYSTEM_SOURCE_ID` |
| `HEALTH_SYSTEM_SOURCE_ID` | [LH_D_BR_HCO](LH_D_BR_HCO.md) | `HEALTH_SYSTEM_SOURCE_ID` |
| `HEALTH_SYSTEM_SOURCE_ID` | [LH_D_BUILDING](LH_D_BUILDING.md) | `HEALTH_SYSTEM_SOURCE_ID` |
| `HEALTH_SYSTEM_SOURCE_ID` | [LH_D_FACILITY](LH_D_FACILITY.md) | `HEALTH_SYSTEM_SOURCE_ID` |
| `HEALTH_SYSTEM_SOURCE_ID` | [LH_D_NURSE_UNIT](LH_D_NURSE_UNIT.md) | `HEALTH_SYSTEM_SOURCE_ID` |
| `HEALTH_SYSTEM_SOURCE_ID` | [LH_D_PERSON](LH_D_PERSON.md) | `HEALTH_SYSTEM_SOURCE_ID` |
| `HEALTH_SYSTEM_SOURCE_ID` | [LH_D_PERSONNEL](LH_D_PERSONNEL.md) | `HEALTH_SYSTEM_SOURCE_ID` |
| `LOGICAL_DOMAIN_ID` | [LOGICAL_DOMAIN](LOGICAL_DOMAIN.md) | `LOGICAL_DOMAIN_ID` |

