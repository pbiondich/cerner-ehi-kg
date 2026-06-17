# LH_QRDA_PQRS

> This table is used to store elements that er used to create the PQRS QRDA file for submission.

**Description:** LH_QRDA_PQRS  
**Table type:** ACTIVITY  
**Primary key:** _(not published — see note)_  
**Columns:** 80

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `BEG_RPT_DT_TM` | DATETIME |  |  | The date and time of the beginning of reporting period. |
| 2 | `D_FACILITY_ID` | DOUBLE | NOT NULL |  | Identifies the organization associated with the attribution. |
| 3 | `D_PERSON_ID` | DOUBLE | NOT NULL |  | Identifies the person associated with the quality measure. Foreign key to the PERSON table. |
| 4 | `D_PPR_ID` | DOUBLE | NOT NULL |  | The d_prsnl_id of the PPR Physician for the d_person_id attached to this row. |
| 5 | `D_PRSNL_ID` | DOUBLE | NOT NULL |  | Identifies the provider associated with the patient. |
| 6 | `END_RPT_DT_TM` | DATETIME |  |  | The date and time of the end of reporting period. |
| 7 | `ERX_VISIT_DATE` | DATETIME |  |  | The visit date on which the eRx was executed, this will only be populated when pqrs_erx_ind is set to 1 |
| 8 | `EXTRACT_DT_TM` | DATETIME |  |  | The date/time that the record was extracted from the source system. |
| 9 | `FAC_CITY` | VARCHAR(100) |  |  | The city field is the text name of the city associated with the address row. |
| 10 | `FAC_STATE` | VARCHAR(100) |  |  | The state field is the text name of the state or province associated with the facility. |
| 11 | `FAC_STREET_ADDR` | VARCHAR(100) |  |  | This is the first line of the street address for the facility. |
| 12 | `FAC_STREET_ADDR2` | VARCHAR(100) |  |  | This is the second line of the street address for the facility. |
| 13 | `FAC_ZIPCODE` | VARCHAR(25) |  |  | This field contains the postal code for the street address for the facility. |
| 14 | `FIRST_PROCESS_DT_TM` | DATETIME |  |  | The date/time that the first ETL process started that created this record. |
| 15 | `HEALTH_INS_NBR_TXT` | VARCHAR(200) |  |  | Represents the patient's member or subscriber identifier with respect to the payer |
| 16 | `HEALTH_SYSTEM_ID` | DOUBLE | NOT NULL |  | Identifies the delivery network responsible for supplying the data. |
| 17 | `HEALTH_SYSTEM_SOURCE_ID` | DOUBLE | NOT NULL |  | Identifies the unique source within the delivery network responsible for supplying the data. |
| 18 | `LAST_PROCESS_DT_TM` | DATETIME |  |  | The date/time that the last ETL process started that updated this record. |
| 19 | `LH_QRDA_PQRS_ID` | DOUBLE | NOT NULL |  | Unique generated number that identifies a single row on the LH_QRDA_PQRS table. |
| 20 | `LOGICAL_DOMAIN_ID` | DOUBLE | NOT NULL |  | The unique identifier for a logical domain. This identifier allows the data to be grouped by logical domain. For example, If you assign clients a logical_domain_id this would allow you to store data for multiple clients on this table. |
| 21 | `NPI` | VARCHAR(200) |  |  | National Provider Identifier for an EP |
| 22 | `PERSON_ETHNIC_CODE` | VARCHAR(10) |  |  | CMS defined ethnicity identifier for the given d_person_id |
| 23 | `PERSON_RACE_CODE` | VARCHAR(10) |  |  | CMS defined race identifier for the given d_person_id |
| 24 | `PQRS_102_IND` | DOUBLE |  |  | The PQRS 102 measure is active or inactive. An active measure indicates that the patient has qualified for the measure |
| 25 | `PQRS_110_IND` | DOUBLE |  |  | The PQRS 110 measure is active or inactive. An active measure indicates that the patient has qualified for the measure |
| 26 | `PQRS_111_IND` | DOUBLE |  |  | The PQRS 111 measure is active or inactive. An active measure indicates that the patient has qualified for the measure |
| 27 | `PQRS_112_IND` | DOUBLE |  |  | The PQRS 112 measure is active or inactive. An active measure indicates that the patient has qualified for the measure |
| 28 | `PQRS_113_IND` | DOUBLE |  |  | The PQRS 113 measure is active or inactive. An active measure indicates that the patient has qualified for the measure |
| 29 | `PQRS_117_IND` | DOUBLE |  |  | The PQRS 117 measure is active or inactive. An active measure indicates that the patient has qualified for the measure |
| 30 | `PQRS_119_IND` | DOUBLE |  |  | The PQRS 119 measure is active or inactive. An active measure indicates that the patient has qualified for the measure |
| 31 | `PQRS_128_IND` | DOUBLE |  |  | The PQRS 128 measure is active or inactive. An active measure indicates that the patient has qualified for the measure |
| 32 | `PQRS_12_IND` | DOUBLE |  |  | The PQRS 12 measure is active or inactive. An active measure indicates that the patient has qualified for the measure |
| 33 | `PQRS_163_IND` | DOUBLE |  |  | The PQRS 163 measure is active or inactive. An active measure indicates that the patient has qualified for the measure |
| 34 | `PQRS_173_IND` | DOUBLE |  |  | The PQRS 173 measure is active or inactive. An active measure indicates that the patient has qualified for the measure |
| 35 | `PQRS_18_IND` | DOUBLE |  |  | The PQRS 18 measure is active or inactive. An active measure indicates that the patient has qualified for the measure |
| 36 | `PQRS_197_IND` | DOUBLE |  |  | The PQRS 197 measure is active or inactive. An active measure indicates that the patient has qualified for the measure |
| 37 | `PQRS_19_IND` | DOUBLE |  |  | The PQRS 19 measure is active or inactive. An active measure indicates that the patient has qualified for the measure |
| 38 | `PQRS_1_IND` | DOUBLE |  |  | The PQRS 1 measure is active or inactive. An active measure indicates that the patient has qualified for the measure |
| 39 | `PQRS_200_IND` | DOUBLE |  |  | The PQRS 200 measure is active or inactive. An active measure indicates that the patient has qualified for the measure |
| 40 | `PQRS_201_IND` | DOUBLE |  |  | The PQRS 201 measure is active or inactive. An active measure indicates that the patient has qualified for the measure |
| 41 | `PQRS_204_IND` | DOUBLE |  |  | The PQRS 204 measure is active or inactive. An active measure indicates that the patient has qualified for the measure |
| 42 | `PQRS_226_IND` | DOUBLE |  |  | The PQRS 226 measure is active or inactive. An active measure indicates that the patient has qualified for the measure |
| 43 | `PQRS_236_IND` | DOUBLE |  |  | The PQRS 236 measure is active or inactive. An active measure indicates that the patient has qualified for the measure |
| 44 | `PQRS_237_IND` | DOUBLE |  |  | The PQRS 237 measure is active or inactive. An active measure indicates that the patient has qualified for the measure |
| 45 | `PQRS_238_IND` | DOUBLE |  |  | The PQRS 238 measure is active or inactive. An active measure indicates that the patient has qualified for the measure |
| 46 | `PQRS_239_IND` | DOUBLE |  |  | The PQRS 239 measure is active or inactive. An active measure indicates that the patient has qualified for the measure |
| 47 | `PQRS_240_IND` | DOUBLE |  |  | The PQRS 240 measure is active or inactive. An active measure indicates that the patient has qualified for the measure |
| 48 | `PQRS_241_IND` | DOUBLE |  |  | The PQRS 241 measure is active or inactive. An active measure indicates that the patient has qualified for the measure |
| 49 | `PQRS_2_IND` | DOUBLE |  |  | The PQRS 2 measure is active or inactive. An active measure indicates that the patient has qualified for the measure |
| 50 | `PQRS_305_IND` | DOUBLE |  |  | The PQRS 305 measure is active or inactive. An active measure indicates that the patient has qualified for the measure |
| 51 | `PQRS_306_IND` | DOUBLE |  |  | The PQRS 306 measure is active or inactive. An active measure indicates that the patient has qualified for the measure |
| 52 | `PQRS_307_IND` | DOUBLE |  |  | The PQRS 307 measure is active or inactive. An active measure indicates that the patient has qualified for the measure |
| 53 | `PQRS_308_IND` | DOUBLE |  |  | The PQRS 308 measure is active or inactive. An active measure indicates that the patient has qualified for the measure |
| 54 | `PQRS_309_IND` | DOUBLE |  |  | The PQRS 309 measure is active or inactive. An active measure indicates that the patient has qualified for the measure |
| 55 | `PQRS_310_IND` | DOUBLE |  |  | The PQRS 310 measure is active or inactive. An active measure indicates that the patient has qualified for the measure |
| 56 | `PQRS_311_IND` | DOUBLE |  |  | The PQRS 311 measure is active or inactive. An active measure indicates that the patient has qualified for the measure |
| 57 | `PQRS_312_IND` | DOUBLE |  |  | The PQRS 312 measure is active or inactive. An active measure indicates that the patient has qualified for the measure |
| 58 | `PQRS_313_IND` | DOUBLE |  |  | The PQRS 313 measure is active or inactive. An active measure indicates that the patient has qualified for the measure |
| 59 | `PQRS_316_IND` | DOUBLE |  |  | The PQRS 316 measure is active or inactive. An active measure indicates that the patient has qualified for the measure |
| 60 | `PQRS_317_IND` | DOUBLE |  |  | The PQRS 317 measure is active or inactive. An active measure indicates that the patient has qualified for the measure |
| 61 | `PQRS_39_IND` | DOUBLE |  |  | The PQRS 39 measure is active or inactive. An active measure indicates that the patient has qualified for the measure |
| 62 | `PQRS_3_IND` | DOUBLE |  |  | The PQRS 3 measure is active or inactive. An active measure indicates that the patient has qualified for the measure |
| 63 | `PQRS_47_IND` | DOUBLE |  |  | The PQRS 47 measure is active or inactive. An active measure indicates that the patient has qualified for the measure |
| 64 | `PQRS_48_IND` | DOUBLE |  |  | The PQRS 48 measure is active or inactive. An active measure indicates that the patient has qualified for the measure |
| 65 | `PQRS_53_IND` | DOUBLE |  |  | The PQRS 53 measure is active or inactive. An active measure indicates that the patient has qualified for the measure |
| 66 | `PQRS_5_IND` | DOUBLE |  |  | The PQRS 5 measure is active or inactive. An active measure indicates that the patient has qualified for the measure |
| 67 | `PQRS_64_IND` | DOUBLE |  |  | The PQRS 64 measure is active or inactive. An active measure indicates that the patient has qualified for the measure |
| 68 | `PQRS_66_IND` | DOUBLE |  |  | The PQRS 66 measure is active or inactive. An active measure indicates that the patient has qualified for the measure |
| 69 | `PQRS_6_IND` | DOUBLE |  |  | The PQRS 6 measure is active or inactive. An active measure indicates that the patient has qualified for the measure |
| 70 | `PQRS_71_IND` | DOUBLE |  |  | The PQRS 71 measure is active or inactive. An active measure indicates that the patient has qualified for the measure |
| 71 | `PQRS_72_IND` | DOUBLE |  |  | The PQRS 72 measure is active or inactive. An active measure indicates that the patient has qualified for the measure |
| 72 | `PQRS_7_IND` | DOUBLE |  |  | The PQRS 7 measure is active or inactive. An active measure indicates that the patient has qualified for the measure |
| 73 | `PQRS_8_IND` | DOUBLE |  |  | The PQRS 8 measure is active or inactive. An active measure indicates that the patient has qualified for the measure |
| 74 | `PQRS_9_IND` | DOUBLE |  |  | The PQRS 9 measure is active or inactive. An active measure indicates that the patient has qualified for the measure |
| 75 | `PQRS_ERX_IND` | DOUBLE |  |  | The PQRS ERX measure is active or inactive. An active measure indicates that the patient has qualified for the measure. |
| 76 | `TAX_ID_NBR_TXT` | VARCHAR(50) |  |  | Stores the eligible provider's tax id number. |
| 77 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 78 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 79 | `UPDT_SOURCE` | VARCHAR(50) | NOT NULL |  | The script name responsible for updating the record. |
| 80 | `UPDT_TASK` | VARCHAR(50) | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

