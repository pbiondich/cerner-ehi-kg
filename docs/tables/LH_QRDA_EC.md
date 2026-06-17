# LH_QRDA_EC

> This table is used to store elements that are used to create the EC Stage 2 QRDA file for submission. This table contains one row for each QRDA file that gets created (one file per person per reporting physician).

**Description:** LH_QRDA_EC  
**Table type:** ACTIVITY  
**Primary key:** `HEALTH_SYSTEM_SOURCE_ID`, `LH_QRDA_EC_ID`  
**Columns:** 61  
**Referenced by:** 2 columns

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ACTIVE_IND` | DOUBLE |  |  | The table row is active or inactive. A row is generally active unless it is in an inactive state such as logically deleted, combined away, pending purge, etc. |
| 2 | `BEG_RPT_DT_TM` | DATETIME |  |  | The date and time of the beginning of reporting period. |
| 3 | `BEG_RPT_OFFSET_UTC` | VARCHAR(6) |  |  | BEG_RPT_OFFSET_UTC stores UTC offset for BEG_RPT_DT_TM |
| 4 | `BR_CPC_ID` | DOUBLE | NOT NULL |  | Primary Key of BR_CPC table |
| 5 | `BR_CPC_PRACTICE_IDENT` | VARCHAR(50) |  |  | CPC practice identifier defined in bedrock wizard |
| 6 | `BR_CPC_PRACTICE_NAME` | VARCHAR(255) |  |  | CPC practice name defined in bedrock wizard |
| 7 | `BR_GPRO_ID` | DOUBLE | NOT NULL |  | Primary Key of BR_GPRO table |
| 8 | `BR_GPRO_NAME` | VARCHAR(255) |  |  | Group practice name defined in bedrock wizard |
| 9 | `BR_GPRO_SUB_ID` | DOUBLE |  |  | Unique generated number that identifies a single row on the BR_GPRO_SUB table. |
| 10 | `BR_GPRO_SUB_NAME` | VARCHAR(255) |  |  | The name given to the subgroup by a client. |
| 11 | `BR_GPRO_SUB_NBR_TXT` | VARCHAR(50) |  |  | User-entered alphanumeric value for the subgroup number. |
| 12 | `CMS_PAYER_GROUP` | VARCHAR(20) |  |  | Indicates the cms payer grouping |
| 13 | `CMS_PROGRAM` | VARCHAR(100) |  |  | Type of submission program: 'MU_ONLY' 'PQRS_MU_INDIVIDUAL' 'PQRS_MU_GROUP' 'CPC' |
| 14 | `CPC_TAX_ID_NBR_TXT` | VARCHAR(50) |  |  | CPC practice tax identification number defined in bedrock wizard |
| 15 | `D_FACILITY_ID` | DOUBLE | NOT NULL | FK→ | Identifies the organization associated with the attribution. |
| 16 | `D_PERSON_ID` | DOUBLE | NOT NULL | FK→ | Identifies the person associated with the quality measure. Foreign key to the PERSON |
| 17 | `D_PPR_ID` | DOUBLE | NOT NULL | FK→ | Identifies the primary care provider associated with the patient. |
| 18 | `D_PRSNL_ID` | DOUBLE | NOT NULL | FK→ | Identifies the provider associated with the patient. |
| 19 | `ENCNTR_ID` | DOUBLE | NOT NULL |  | To store encounter id of qualifying patients. |
| 20 | `END_RPT_DT_TM` | DATETIME |  |  | The date and time of the end of reporting period. |
| 21 | `END_RPT_OFFSET_UTC` | VARCHAR(6) |  |  | END_RPT_OFFSET_UTC stores UTC offset for END_RPT_DT_TM |
| 22 | `EXTRACT_DT_TM` | DATETIME |  |  | The date/time that the record was extracted from the source system. |
| 23 | `FIRST_PROCESS_DT_TM` | DATETIME |  |  | The date/time that the first ETL process started that created this record. |
| 24 | `GPRO_TAX_ID_NBR_TXT` | VARCHAR(50) |  |  | Group practice tax identification number defined in bedrock |
| 25 | `HEALTH_INS_NBR_TXT` | VARCHAR(50) |  |  | Represents the patient's member or subscriber identifier with respect to the payer |
| 26 | `HEALTH_SYSTEM_ID` | DOUBLE | NOT NULL |  | Identifies the delivery network responsible for supplying the data. |
| 27 | `HEALTH_SYSTEM_SOURCE_ID` | DOUBLE | NOT NULL | PK FK→ | Identifies the unique source within the delivery network responsible for supplying the |
| 28 | `LAST_PROCESS_DT_TM` | DATETIME |  |  | The date/time that the last ETL process started that updated this record. |
| 29 | `LH_CQM_REPORT_TYPE_TFLG` | VARCHAR(5) |  |  | Determines the reporting type as MIPs or MVPs. |
| 30 | `LH_QRDA_EC_ID` | DOUBLE | NOT NULL | PK | Primary key of the LH_QRDA_EC table. |
| 31 | `LOAD_UTC_OFFSET` | VARCHAR(5) |  |  | Stores the offset value for the timezone. eg: -0600/+0600 |
| 32 | `LOGICAL_DOMAIN_ID` | DOUBLE | NOT NULL |  | The unique identifier for a logical domain. This identifier allows the data to be grouped by logical domain. For example, If you assign clients a logical_domain_id this would allow you to store data for multiple clients on this table. |
| 33 | `MRN_TXT` | VARCHAR(50) |  |  | Used To store MRN for the patient in this table. |
| 34 | `NATIONAL_PROVIDER_NBR_TXT` | VARCHAR(200) |  |  | National Provider Identifier for an EC |
| 35 | `PERSON_ETHNIC_CODE` | VARCHAR(50) |  |  | The code representing the patient's ethnicity |
| 36 | `PERSON_ETHNIC_CODE_DISPLAY` | VARCHAR(500) |  |  | The textual representation of the patient's ethnicity |
| 37 | `PERSON_ETHNIC_CODE_SYSTEM` | VARCHAR(50) |  |  | The code system of the patient's ethnicity |
| 38 | `PERSON_ETHNIC_CODE_SYSTEM_NAME` | VARCHAR(50) |  |  | The name of the patient's ethnicity code system |
| 39 | `PERSON_GENDER_CODE` | VARCHAR(50) |  |  | The code representing the patient's gender. |
| 40 | `PERSON_GENDER_CODE_DISPLAY` | VARCHAR(500) |  |  | The textual representation of the patient's gender. |
| 41 | `PERSON_GENDER_CODE_SYSTEM` | VARCHAR(50) |  |  | The code system of the patient's gender |
| 42 | `PERSON_GENDER_CODE_SYSTEM_NAME` | VARCHAR(50) |  |  | The name of the patient's gender code system |
| 43 | `PERSON_PAYER_CODE` | VARCHAR(50) |  |  | The policy or program coverage role type (e.g. 'Self'). |
| 44 | `PERSON_PAYER_CODE_DISPLAY` | VARCHAR(500) |  |  | Text description of the policy type. |
| 45 | `PERSON_PAYER_CODE_SYSTEM` | VARCHAR(50) |  |  | String representation of the code system that policy was derived from. |
| 46 | `PERSON_PAYER_CODE_SYSTEM_NAME` | VARCHAR(50) |  |  | The name of the policy code system. |
| 47 | `PERSON_RACE_CODE` | VARCHAR(50) |  |  | The code representing the patient's race. |
| 48 | `PERSON_RACE_CODE_DISPLAY` | VARCHAR(500) |  |  | The textual representation of the patient's race |
| 49 | `PERSON_RACE_CODE_SYSTEM` | VARCHAR(50) |  |  | The code system of the patient's race |
| 50 | `PERSON_RACE_CODE_SYSTEM_NAME` | VARCHAR(50) |  |  | The name of the patient's race code system |
| 51 | `PERSON_TELECOM` | VARCHAR(50) |  |  | The patient's phone number |
| 52 | `REPORTING_CATEGORY` | DOUBLE |  |  | Indicates if the report category is QRDA 1 or QRDA 3. |
| 53 | `REPORTING_YEAR` | DOUBLE |  |  | Stores the reporting year. |
| 54 | `SRC_UPDT_DT_TM` | DATETIME |  |  | Indicates the actual time when the row was inserted or updated at the source |
| 55 | `SRC_UPDT_SOURCE` | VARCHAR(50) |  |  | This column is updated with the name of the source program that loaded these rows into this table in Quality Clearinghouse when the Power Insight extracts were executed. |
| 56 | `TAX_ID_NBR_TXT` | VARCHAR(200) |  |  | Tax identifier number for an EC |
| 57 | `TIME_ZONE_INDEX` | DOUBLE |  |  | Stores the time zone index of the local time zone. |
| 58 | `UPDT_CNT` | DOUBLE |  |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 59 | `UPDT_DT_TM` | DATETIME |  |  | The date and time the row was last inserted or updated. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 60 | `UPDT_SOURCE` | VARCHAR(50) |  |  | The script name responsible for updating the record. |
| 61 | `UPDT_TASK` | VARCHAR(50) |  |  | The registered (assigned) task number for the process that inserted or updated the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `D_FACILITY_ID` | [LH_D_FACILITY](LH_D_FACILITY.md) | `D_FACILITY_ID` |
| `D_PERSON_ID` | [LH_D_PERSON](LH_D_PERSON.md) | `D_PERSON_ID` |
| `D_PPR_ID` | [LH_D_PERSONNEL](LH_D_PERSONNEL.md) | `D_PRSNL_ID` |
| `D_PRSNL_ID` | [LH_D_PERSONNEL](LH_D_PERSONNEL.md) | `D_PRSNL_ID` |
| `HEALTH_SYSTEM_SOURCE_ID` | [LH_D_FACILITY](LH_D_FACILITY.md) | `HEALTH_SYSTEM_SOURCE_ID` |
| `HEALTH_SYSTEM_SOURCE_ID` | [LH_D_PERSON](LH_D_PERSON.md) | `HEALTH_SYSTEM_SOURCE_ID` |
| `HEALTH_SYSTEM_SOURCE_ID` | [LH_D_PERSONNEL](LH_D_PERSONNEL.md) | `HEALTH_SYSTEM_SOURCE_ID` |
| `HEALTH_SYSTEM_SOURCE_ID` | [LH_D_PERSONNEL](LH_D_PERSONNEL.md) | `HEALTH_SYSTEM_SOURCE_ID` |

## Referenced by (2)

| From table | Column |
|------------|--------|
| [LH_QRDA_EC_DETAIL](LH_QRDA_EC_DETAIL.md) | `HEALTH_SYSTEM_SOURCE_ID` |
| [LH_QRDA_EC_DETAIL](LH_QRDA_EC_DETAIL.md) | `LH_QRDA_EC_ID` |

