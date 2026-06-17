# LH_QRDA_NQF

> This table is used to store elements that are used to create the NQF Stage 2 QRDA file for submission. This table contains one row for each QRDA file that gets created (one file per person per reporting physician).

**Description:** LH_QRDA_PQRS  
**Table type:** ACTIVITY  
**Primary key:** _(not published — see note)_  
**Columns:** 172

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ACTIVE_IND` | DOUBLE |  |  | The table row is active or inactive. A row is generally active unless it is in an inactive state such as logically deleted, combined away, pending purge, etc. |
| 2 | `BEG_RPT_DT_TM` | DATETIME |  |  | The date and time of the beginning of reporting period. |
| 3 | `BR_CPC_ID` | DOUBLE | NOT NULL |  | Primary Key of BR_CPC table |
| 4 | `BR_CPC_PRACTICE_IDENT` | VARCHAR(50) |  |  | CPC practice identifier defined in bedrock wizard |
| 5 | `BR_CPC_PRACTICE_NAME` | VARCHAR(255) |  |  | CPC practice name defined in bedrock wizard |
| 6 | `BR_GPRO_ID` | DOUBLE | NOT NULL |  | Primary Key of BR_GPRO table |
| 7 | `BR_GPRO_NAME` | VARCHAR(255) |  |  | Group practice name defined in bedrock wizard |
| 8 | `CMS_0022_IND` | DOUBLE |  |  | The CMS 22 measure is active or inactive. An active measure indicates that the patient has qualified for the measure |
| 9 | `CMS_0050_IND` | DOUBLE |  |  | The CMS 50 measure is active or inactive. An active measure indicates that the patient has qualified for the measure |
| 10 | `CMS_0056_IND` | DOUBLE |  |  | The CMS 56 measure is active or inactive. An active measure indicates that the patient has qualified for the measure |
| 11 | `CMS_0061_IND` | DOUBLE |  |  | The CMS 61 measure is active or inactive. An active measure indicates that the patient has qualified for the measure |
| 12 | `CMS_0062_IND` | DOUBLE |  |  | Indicates if patient qualified for CMS 62. |
| 13 | `CMS_0064_IND` | DOUBLE |  |  | The CMS 64 measure is active or inactive. An active measure indicates that the patient has qualified for the measure |
| 14 | `CMS_0065_IND` | DOUBLE |  |  | The CMS 65 measure is active or inactive. An active measure indicates that the patient has qualified for the measure |
| 15 | `CMS_0066_IND` | DOUBLE |  |  | The CMS 66 measure is active or inactive. An active measure indicates that the patient has qualified for the measure |
| 16 | `CMS_0074_1_IND` | DOUBLE |  |  | To store outcome indicatiore for cms74 pop1 |
| 17 | `CMS_0074_2_IND` | DOUBLE |  |  | To store outcome indicatiore for cms74 pop2 |
| 18 | `CMS_0074_3_IND` | DOUBLE |  |  | To store outcome indicatiore for cms74 pop3 |
| 19 | `CMS_0074_4_IND` | DOUBLE |  |  | To store outcome indicatiore for cms74 pop4 |
| 20 | `CMS_0074_IND` | DOUBLE |  |  | The CMS 74 measure is active or inactive. An active measure indicates that the patient has qualified for the measure |
| 21 | `CMS_0075_IND` | DOUBLE |  |  | The CMS 75 measure is active or inactive. An active measure indicates that the patient has qualified for the measure |
| 22 | `CMS_0077_IND` | DOUBLE |  |  | The CMS 77 measure is active or inactive. An active measure indicates that the patient has qualified for the measure |
| 23 | `CMS_0082_IND` | DOUBLE |  |  | The CMS 82 measure is active or inactive. An active measure indicates that the patient has qualified for the measure |
| 24 | `CMS_0090_IND` | DOUBLE |  |  | The CMS 90 measure is active or inactive. An active measure indicates that the patient has qualified for the measure |
| 25 | `CMS_0125_IND` | DOUBLE |  |  | Indicates if patient qualified for CMS 125 |
| 26 | `CMS_0149_IND` | DOUBLE |  |  | The CMS 149 measure is active or inactive. An active measure indicates that the patient has qualified for the measure |
| 27 | `CMS_0158_IND` | DOUBLE |  |  | Indicates if patient qualified for CMS 158 |
| 28 | `CMS_0163_IND` | DOUBLE |  |  | The CMS 163 measure is active or inactive. An active measure indicates that the patient has qualified for the measure |
| 29 | `CMS_0169_IND` | DOUBLE |  |  | The CMS 169 measure is active or inactive. An active measure indicates that the patient has qualified for the measure |
| 30 | `CMS_0179_IND` | DOUBLE |  |  | The CMS 179 measure is active or inactive. An active measure indicates that the patient has qualified for the measure |
| 31 | `CMS_0182_IND` | DOUBLE |  |  | The CMS 182 measure is active or inactive. An active measure indicates that the patient has qualified for the measure |
| 32 | `CMS_PAYER_GROUP` | VARCHAR(20) |  |  | Indicates the cms payer grouping |
| 33 | `CMS_PROGRAM` | VARCHAR(100) |  |  | Type of submission program: ¿MU_ONLY¿, ¿PQRS_MU_INDIVIDUAL¿, ¿PQRS_MU_GROUP¿, ""CPC"" |
| 34 | `CPC_TAX_ID_NBR_TXT` | VARCHAR(50) |  |  | CPC practice tax identification number defined in bedrock wizard |
| 35 | `D_FACILITY_ID` | DOUBLE | NOT NULL |  | Identifies the organization associated with the attribution. |
| 36 | `D_PERSON_ID` | DOUBLE | NOT NULL |  | Identifies the person associated with the quality measure. Foreign key to the PERSON table. |
| 37 | `D_PPR_ID` | DOUBLE | NOT NULL |  | Identifies the primary care provider associated with the patient. |
| 38 | `D_PRSNL_ID` | DOUBLE | NOT NULL |  | Identifies the provider associated with the patient. |
| 39 | `ENCNTR_ID` | DOUBLE | NOT NULL |  | To store encounter id of qualifying patients |
| 40 | `END_RPT_DT_TM` | DATETIME |  |  | The date and time of the end of reporting period. |
| 41 | `EXTRACT_DT_TM` | DATETIME |  |  | The date/time that the record was extracted from the source system. |
| 42 | `FIRST_PROCESS_DT_TM` | DATETIME |  |  | The date/time that the first ETL process started that created this record. |
| 43 | `GPRO_TAX_ID_NBR_TXT` | VARCHAR(50) |  |  | Group practice tax identification number defined in bedrock |
| 44 | `HEALTH_INS_NBR_TXT` | VARCHAR(50) |  |  | Represents the patient's member or subscriber identifier with respect to the payer |
| 45 | `HEALTH_SYSTEM_ID` | DOUBLE | NOT NULL |  | Identifies the delivery network responsible for supplying the data. |
| 46 | `HEALTH_SYSTEM_SOURCE_ID` | DOUBLE | NOT NULL |  | Identifies the unique source within the delivery network responsible for supplying the data. |
| 47 | `LAST_PROCESS_DT_TM` | DATETIME |  |  | The date/time that the last ETL process started that updated this record. |
| 48 | `LH_QRDA_NQF_ID` | DOUBLE | NOT NULL |  | Unique generated number that identifies a single row on the LH_QRDA_NQF table. |
| 49 | `LOAD_UTC_OFFSET` | VARCHAR(5) |  |  | To store the offset difference between local and utc time. |
| 50 | `LOGICAL_DOMAIN_ID` | DOUBLE | NOT NULL |  | The unique identifier for a logical domain. This identifier allows the data to be grouped by logical domain. For example, If you assign clients a logical_domain_id this would allow you to store data for multiple clients on this table. |
| 51 | `MRN_TXT` | VARCHAR(50) |  |  | Used To store MRN for the patient in this table. |
| 52 | `NATIONAL_PROVIDER_NBR_TXT` | VARCHAR(200) |  |  | National Provider Identifier for an EP |
| 53 | `NQF2_0002_IND` | DOUBLE |  |  | The NQF 2 measure is active or inactive. An active measure indicates that the patient has qualified for the measure |
| 54 | `NQF2_0004_1_1_IND` | DOUBLE |  |  | To store outcome indicatiore for nqf4 pop1.1 |
| 55 | `NQF2_0004_1_2_IND` | DOUBLE |  |  | To store outcome indicatiore for nqf4 pop1.2 |
| 56 | `NQF2_0004_1_3_IND` | DOUBLE |  |  | To store outcome indicatiore for nqf4 pop1.3 |
| 57 | `NQF2_0004_2_1_IND` | DOUBLE |  |  | To store outcome indicatiore for nqf4 pop2.1 |
| 58 | `NQF2_0004_2_2_IND` | DOUBLE |  |  | To store outcome indicatiore for nqf4 pop2.2 |
| 59 | `NQF2_0004_2_3_IND` | DOUBLE |  |  | To store outcome indicatiore for nqf4 pop2.3 |
| 60 | `NQF2_0004_IND` | DOUBLE |  |  | The NQF 4 measure is active or inactive. An active measure indicates that the patient has qualified for the measure |
| 61 | `NQF2_0018_IND` | DOUBLE |  |  | The NQF 18 measure is active or inactive. An active measure indicates that the patient has qualified for the measure |
| 62 | `NQF2_0022_1_IND` | DOUBLE |  |  | To store outcome indicatiore for nqf22 pop1 |
| 63 | `NQF2_0022_2_IND` | DOUBLE |  |  | To store outcome indicatiore for nqf22 pop2 |
| 64 | `NQF2_0022_IND` | DOUBLE |  |  | The NQF 22 measure is active or inactive. An active measure indicates that the patient has qualified for the measure |
| 65 | `NQF2_0024_1_1_IND` | DOUBLE |  |  | To store outcome indicatiore for nqf24 pop1.1 |
| 66 | `NQF2_0024_1_2_IND` | DOUBLE |  |  | To store outcome indicatiore for nqf24 pop1.2 |
| 67 | `NQF2_0024_1_3_IND` | DOUBLE |  |  | To store outcome indicatiore for nqf24 pop1.3 |
| 68 | `NQF2_0024_2_1_IND` | DOUBLE |  |  | To store outcome indicatiore for nqf24 pop2.1 |
| 69 | `NQF2_0024_2_2_IND` | DOUBLE |  |  | To store outcome indicatiore for nqf24 pop2.2 |
| 70 | `NQF2_0024_2_3_IND` | DOUBLE |  |  | To store outcome indicatiore for nqf24 pop2.3 |
| 71 | `NQF2_0024_3_1_IND` | DOUBLE |  |  | To store outcome indicatiore for nqf24 pop3.1 |
| 72 | `NQF2_0024_3_2_IND` | DOUBLE |  |  | To store outcome indicatiore for nqf24 pop3.2 |
| 73 | `NQF2_0024_3_3_IND` | DOUBLE |  |  | To store outcome indicatiore for nqf24 pop3.3 |
| 74 | `NQF2_0024_IND` | DOUBLE |  |  | The NQF 24 measure is active or inactive. An active measure indicates that the patient has qualified for the measure |
| 75 | `NQF2_0028_1_IND` | DOUBLE |  |  | To store outcome indicatiore for nqf28 pop1 |
| 76 | `NQF2_0028_2_IND` | DOUBLE |  |  | To store outcome indicatiore for nqf28 pop2 |
| 77 | `NQF2_0028_3_IND` | DOUBLE |  |  | To store outcome indicatiore for nqf28 pop3 |
| 78 | `NQF2_0028_IND` | DOUBLE |  |  | The NQF 28 measure is active or inactive. An active measure indicates that the patient has qualified for the measure |
| 79 | `NQF2_0031_IND` | DOUBLE |  |  | *** OBSOLETE *** |
| 80 | `NQF2_0032_IND` | DOUBLE |  |  | The NQF 32 measure is active or inactive. An active measure indicates that the patient has qualified for the measure |
| 81 | `NQF2_0033_1_IND` | DOUBLE |  |  | Sub measure NQF2 33_1 stores an outcome mask indicator for measure NQF33 population 1. |
| 82 | `NQF2_0033_2_IND` | DOUBLE |  |  | Sub measure NQF2 33_2 stores an outcome mask indicator for measure NQF33 population 2. |
| 83 | `NQF2_0033_3_IND` | DOUBLE |  |  | Sub measure NQF2 33_3 stores an outcome mask indicator for measure NQF33 population 3. |
| 84 | `NQF2_0033_IND` | DOUBLE |  |  | The NQF 33 measure is active or inactive. An active measure indicates that the patient has qualified for the measure |
| 85 | `NQF2_0034_IND` | DOUBLE |  |  | The NQF 34 measure is active or inactive. An active measure indicates that the patient has qualified for the measure |
| 86 | `NQF2_0036_IND` | DOUBLE |  |  | The NQF 36 measure is active or inactive. An active measure indicates that the patient has qualified for the measure |
| 87 | `NQF2_0038_IND` | DOUBLE |  |  | The NQF 38 measure is active or inactive. An active measure indicates that the patient has qualified for the measure |
| 88 | `NQF2_0041_IND` | DOUBLE |  |  | The NQF 41 measure is active or inactive. An active measure indicates that the patient has qualified for the measure |
| 89 | `NQF2_0043_IND` | DOUBLE |  |  | The NQF 43 measure is active or inactive. An active measure indicates that the patient has qualified for the measure |
| 90 | `NQF2_0052_IND` | DOUBLE |  |  | The NQF 52 measure is active or inactive. An active measure indicates that the patient has qualified for the measure |
| 91 | `NQF2_0055_IND` | DOUBLE |  |  | The NQF 55 measure is active or inactive. An active measure indicates that the patient has qualified for the measure |
| 92 | `NQF2_0056_IND` | DOUBLE |  |  | The NQF 56 measure is active or inactive. An active measure indicates that the patient has qualified for the measure |
| 93 | `NQF2_0059_IND` | DOUBLE |  |  | The NQF 59 measure is active or inactive. An active measure indicates that the patient has qualified for the measure |
| 94 | `NQF2_0060_IND` | DOUBLE |  |  | The NQF 60 measure is active or inactive. An active measure indicates that the patient has qualified for the measure |
| 95 | `NQF2_0062_IND` | DOUBLE |  |  | The NQF 62 measure is active or inactive. An active measure indicates that the patient has qualified for the measure |
| 96 | `NQF2_0064_IND` | DOUBLE |  |  | *** OBSOLETE *** |
| 97 | `NQF2_0068_IND` | DOUBLE |  |  | The NQF 68 measure is active or inactive. An active measure indicates that the patient has qualified for the measure |
| 98 | `NQF2_0069_IND` | DOUBLE |  |  | The NQF 69 measure is active or inactive. An active measure indicates that the patient has qualified for the measure |
| 99 | `NQF2_0070_1_IND` | DOUBLE |  |  | To store outcome indicatiore for nqf70 pop1 |
| 100 | `NQF2_0070_2_IND` | DOUBLE |  |  | To store outcome indicatiore for nqf70 pop2 |
| 101 | `NQF2_0070_IND` | DOUBLE |  |  | The NQF 70 measure is active or inactive. An active measure indicates that the patient has qualified for the measure |
| 102 | `NQF2_0075_IND` | DOUBLE |  |  | *** OBSOLETE *** |
| 103 | `NQF2_0081_1_IND` | DOUBLE |  |  | To store outcome indicatiore for nqf81 pop1 |
| 104 | `NQF2_0081_2_IND` | DOUBLE |  |  | To store outcome indicatiore for nqf81 pop2 |
| 105 | `NQF2_0081_IND` | DOUBLE |  |  | The NQF 81 measure is active or inactive. An active measure indicates that the patient has qualified for the measure |
| 106 | `NQF2_0083_1_IND` | DOUBLE |  |  | To store outcome indicatiore for nqf83 pop1 |
| 107 | `NQF2_0083_2_IND` | DOUBLE |  |  | To store outcome indicatiore for nqf83 pop2 |
| 108 | `NQF2_0083_IND` | DOUBLE |  |  | The NQF 83 measure is active or inactive. An active measure indicates that the patient has qualified for the measure |
| 109 | `NQF2_0086_IND` | DOUBLE |  |  | The NQF 86 measure is active or inactive. An active measure indicates that the patient has qualified for the measure |
| 110 | `NQF2_0088_IND` | DOUBLE |  |  | The NQF 88 measure is active or inactive. An active measure indicates that the patient has qualified for the measure |
| 111 | `NQF2_0089_IND` | DOUBLE |  |  | The NQF 89 measure is active or inactive. An active measure indicates that the patient has qualified for the measure |
| 112 | `NQF2_0101_IND` | DOUBLE |  |  | The NQF 101 measure is active or inactive. An active measure indicates that the patient has qualified for the measure |
| 113 | `NQF2_0104_IND` | DOUBLE |  |  | The NQF 104 measure is active or inactive. An active measure indicates that the patient has qualified for the measure |
| 114 | `NQF2_0105_IND` | DOUBLE |  |  | The NQF 105 measure is active or inactive. An active measure indicates that the patient has qualified for the measure |
| 115 | `NQF2_0108_IND` | DOUBLE |  |  | The NQF 108 measure is active or inactive. An active measure indicates that the patient has qualified for the measure |
| 116 | `NQF2_0110_IND` | DOUBLE |  |  | *** OBSOLETE *** |
| 117 | `NQF2_0384_1_IND` | DOUBLE |  |  | To store outcome indicatiore for nqf384 pop1 |
| 118 | `NQF2_0384_2_IND` | DOUBLE |  |  | To store outcome indicatiore for nqf384 pop2 |
| 119 | `NQF2_0384_IND` | DOUBLE |  |  | The NQF 384 measure is active or inactive. An active measure indicates that the patient has qualified for the measure |
| 120 | `NQF2_0385_IND` | DOUBLE |  |  | The NQF 385 measure is active or inactive. An active measure indicates that the patient has qualified for the measure |
| 121 | `NQF2_0387_IND` | DOUBLE |  |  | The NQF 387 measure is active or inactive. An active measure indicates that the patient has qualified for the measure |
| 122 | `NQF2_0389_IND` | DOUBLE |  |  | The NQF 389 measure is active or inactive. An active measure indicates that the patient has qualified for the measure |
| 123 | `NQF2_0403_IND` | DOUBLE |  |  | *** OBSOLETE *** |
| 124 | `NQF2_0405_IND` | DOUBLE |  |  | The NQF 405 measure is active or inactive. An active measure indicates that the patient has qualified for the measure |
| 125 | `NQF2_0407_IND` | DOUBLE |  |  | *** OBSOLETE *** The NQF 407 measure is active or inactive. An active measure indicates that the patient has qualified for the measure. This column is obsolete. |
| 126 | `NQF2_0418_IND` | DOUBLE |  |  | The NQF 418 measure is active or inactive. An active measure indicates that the patient has qualified for the measure |
| 127 | `NQF2_0419_IND` | DOUBLE |  |  | The NQF 419 measure is active or inactive. An active measure indicates that the patient has qualified for the measure |
| 128 | `NQF2_0421_IND` | DOUBLE |  |  | The NQF 421 measure is active or inactive. An active measure indicates that the patient has qualified for the measure |
| 129 | `NQF2_0564_IND` | DOUBLE |  |  | The NQF 564 measure is active or inactive. An active measure indicates that the patient has qualified for the measure |
| 130 | `NQF2_0565_IND` | DOUBLE |  |  | The NQF 565 measure is active or inactive. An active measure indicates that the patient has qualified for the measure |
| 131 | `NQF2_0608_IND` | DOUBLE |  |  | *** OBSOLETE *** The NQF 608 measure is active or inactive. An active measure indicates that the patient has qualified for the measure |
| 132 | `NQF2_0710_1_IND` | DOUBLE |  |  | To store outcome indicatiore for nqf710 pop1 |
| 133 | `NQF2_0710_2_IND` | DOUBLE |  |  | To store outcome indicatiore for nqf710 pop2 |
| 134 | `NQF2_0710_3_IND` | DOUBLE |  |  | To store outcome indicatiore for nqf710 pop3 |
| 135 | `NQF2_0710_IND` | DOUBLE |  |  | The NQF 710 measure is active or inactive. An active measure indicates that the patient has qualified for the measure |
| 136 | `NQF2_0712_1_1_IND` | DOUBLE |  |  | To store outcome indicatiore for nqf712 pop1.1 |
| 137 | `NQF2_0712_1_2_IND` | DOUBLE |  |  | To store outcome indicatiore for nqf712 pop1.2 |
| 138 | `NQF2_0712_1_3_IND` | DOUBLE |  |  | To store outcome indicatiore for nqf712 pop1.3 |
| 139 | `NQF2_0712_2_1_IND` | DOUBLE |  |  | To store outcome indicatiore for nqf712 pop2.1 |
| 140 | `NQF2_0712_2_2_IND` | DOUBLE |  |  | To store outcome indicatiore for nqf712 pop2.2 |
| 141 | `NQF2_0712_2_3_IND` | DOUBLE |  |  | To store outcome indicatiore for nqf712 pop2.3 |
| 142 | `NQF2_0712_3_1_IND` | DOUBLE |  |  | To store outcome indicatiore for nqf712 pop3.1 |
| 143 | `NQF2_0712_3_2_IND` | DOUBLE |  |  | To store outcome indicatiore for nqf712 pop3.2 |
| 144 | `NQF2_0712_3_3_IND` | DOUBLE |  |  | To store outcome indicatiore for nqf712 pop3.3 |
| 145 | `NQF2_0712_IND` | DOUBLE |  |  | The NQF 712 measure is active or inactive. An active measure indicates that the patient has qualified for the measure |
| 146 | `NQF2_1365_IND` | DOUBLE |  |  | The NQF 1365 measure is active or inactive. An active measure indicates that the patient has qualified for the measure |
| 147 | `NQF2_1401_IND` | DOUBLE |  |  | *** OBSOLETE *** The NQF 1401 measure is active or inactive. An active measure indicates that the patient has qualified for the measure |
| 148 | `PERSON_ETHNIC_CODE` | VARCHAR(50) |  |  | The code representing the patient's ethnicity |
| 149 | `PERSON_ETHNIC_CODE_DISPLAY` | VARCHAR(500) |  |  | The textual representation of the patient's ethnicity |
| 150 | `PERSON_ETHNIC_CODE_SYSTEM` | VARCHAR(50) |  |  | The code system of the patient's ethnicity |
| 151 | `PERSON_ETHNIC_CODE_SYSTEM_NAME` | VARCHAR(50) |  |  | The name of the patient's ethnicity code system |
| 152 | `PERSON_GENDER_CODE` | VARCHAR(50) |  |  | The code representing the patient's gender |
| 153 | `PERSON_GENDER_CODE_DISPLAY` | VARCHAR(500) |  |  | The textual representation of the patient's gender |
| 154 | `PERSON_GENDER_CODE_SYSTEM` | VARCHAR(50) |  |  | The code system of the patient's gender |
| 155 | `PERSON_GENDER_CODE_SYSTEM_NAME` | VARCHAR(50) |  |  | The name of the patient's gender code system |
| 156 | `PERSON_PAYER_CODE` | VARCHAR(50) |  |  | The policy or program coverage role type (e.g. 'Self'). |
| 157 | `PERSON_PAYER_CODE_DISPLAY` | VARCHAR(500) |  |  | Text description of the policy type. |
| 158 | `PERSON_PAYER_CODE_SYSTEM` | VARCHAR(50) |  |  | String representation of the code system that policy was derived from. |
| 159 | `PERSON_PAYER_CODE_SYSTEM_NAME` | VARCHAR(50) |  |  | The name of the policy code system. |
| 160 | `PERSON_RACE_CODE` | VARCHAR(50) |  |  | The code representing the patient's race |
| 161 | `PERSON_RACE_CODE_DISPLAY` | VARCHAR(500) |  |  | The textual representation of the patient's race |
| 162 | `PERSON_RACE_CODE_SYSTEM` | VARCHAR(50) |  |  | The code system of the patient's race |
| 163 | `PERSON_RACE_CODE_SYSTEM_NAME` | VARCHAR(50) |  |  | The name of the patient's race code system |
| 164 | `PERSON_TELECOM` | VARCHAR(50) |  |  | The patient's phone number |
| 165 | `SRC_UPDT_DT_TM` | DATETIME |  |  | Indicates the actual time when the row was inserted or updated at the source |
| 166 | `SRC_UPDT_SOURCE` | VARCHAR(50) | NOT NULL |  | This column is updated with the name of the source program that loaded these rows into this table in Quality Clearinghouse when the Power Insight extracts were executed. |
| 167 | `TAX_ID_NBR_TXT` | VARCHAR(200) |  |  | Tax identifier number for an EP |
| 168 | `TIME_ZONE_INDEX` | DOUBLE |  |  | Stores the time zone index of the local time zone. |
| 169 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 170 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 171 | `UPDT_SOURCE` | VARCHAR(50) | NOT NULL |  | The script name responsible for updating the record. |
| 172 | `UPDT_TASK` | VARCHAR(50) | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

