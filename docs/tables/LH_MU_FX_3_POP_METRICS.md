# LH_MU_FX_3_POP_METRICS

> This table will have all the persons based and encounter based measures population

**Description:** LH_MU_FX_3_POP_METRICS  
**Table type:** ACTIVITY  
**Primary key:** `HEALTH_SYSTEM_SOURCE_ID`, `LH_MU_FX_3_POP_METRICS_ID`  
**Columns:** 48  
**Referenced by:** 4 columns

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ACTIVE_IND` | DOUBLE |  |  | The table row is active or inactive. A row is generally active unless it is in an inactive state such as logically deleted, combined away, pending purge, etc. |
| 2 | `ADMIT_DT_TM` | DATETIME |  |  | Registration date and time for the encounter |
| 3 | `ADMIT_LOC_DT_TM` | DATETIME |  |  | The local version of the ADMIT_DT_TM column. |
| 4 | `APPT_TYPE_CD` | DOUBLE | NOT NULL |  | Scheduling appointment type for encounter |
| 5 | `APPT_TYPE_TEXT` | VARCHAR(50) |  |  | The display for the appt_type_cd coming from code value table |
| 6 | `BIRTH_DT_TM` | DATETIME |  |  | Birth date and time for the person |
| 7 | `BIRTH_LOC_DT_TM` | DATETIME |  |  | The local version of the BIRTH_DT_TM column |
| 8 | `CCN_IND` | DOUBLE |  |  | will signify an inpatient encounter or an observation encounter |
| 9 | `DIRECT_EMAIL` | VARCHAR(100) |  |  | Displays Direct provider email address. |
| 10 | `DISCH_DISPOSITION_CD` | DOUBLE |  |  | The conditions under which the patient left the facility at the time of discharge. From the Encounter table. |
| 11 | `DISCH_DISPOSITION_TEXT` | VARCHAR(50) |  |  | Display of Discharge Disposition code. |
| 12 | `DISCH_DT_TM` | DATETIME |  |  | Discharge date and time for the encounter |
| 13 | `DISCH_LOC_DT_TM` | DATETIME |  |  | The local version of the DISCH_DT_TM column. |
| 14 | `D_DISCHARGE_BUILDING_ID` | DOUBLE | NOT NULL | FK→ | Value comes from lh_d_building |
| 15 | `D_DISCHARGE_FACILITY_ID` | DOUBLE | NOT NULL | FK→ | Value comes from lh_d_facility |
| 16 | `D_DISCHARGE_NURSE_UNIT_ID` | DOUBLE | NOT NULL | FK→ | Value comes from lh_d_nurse_unit |
| 17 | `D_ENCNTR_TYPE_ID` | DOUBLE | NOT NULL | FK→ | Value comes from lh_d_encntr_type |
| 18 | `D_MED_SERVICE_ID` | DOUBLE | NOT NULL | FK→ | Value comes from lh_d_med_service |
| 19 | `D_PERSON_ID` | DOUBLE | NOT NULL | FK→ | Contains d_person_id for each person coming form lh_d_person table |
| 20 | `EC_IND` | DOUBLE | NOT NULL |  | Indicator used to show that an inpatient qualified for an EC. |
| 21 | `ENCNTR_ID` | DOUBLE | NOT NULL |  | Encntr_id of the person |
| 22 | `EP_IND` | DOUBLE |  |  | Will signify an outpatient encounter or an observation encounter |
| 23 | `EXTRACT_DT_TM` | DATETIME |  |  | Date and time the row was extracted into the table |
| 24 | `FINANCIAL_NBR_TXT` | VARCHAR(200) |  |  | Fin number for the encounter |
| 25 | `FIRST_PROCESS_DT_TM` | DATETIME |  |  | The date/time that the first ETL process started that created this record. |
| 26 | `HEALTH_SYSTEM_ID` | DOUBLE | NOT NULL |  | Identifies the delivery network responsible for supplying the data. |
| 27 | `HEALTH_SYSTEM_SOURCE_ID` | DOUBLE | NOT NULL | PK FK→ | Identifies the unique source within the delivery network responsible for supplying the data. |
| 28 | `LAST_PROCESS_DT_TM` | DATETIME |  |  | The date/time that the last ETL process started that updated this record. |
| 29 | `LH_MU_FX_3_POP_METRICS_ID` | DOUBLE | NOT NULL | PK | Unique generated number that identifies a single row on the LH_MU_FX_3_POP_METRICS table. |
| 30 | `LOGICAL_DOMAIN_ID` | DOUBLE | NOT NULL |  | The unique identifier for a logical domain. This identifier allows the data to be grouped by logical domain. For example, If you assign clients a logical_domain_id this would allow you to store data for multiple clients on this table. |
| 31 | `METRIC_TYPE` | VARCHAR(50) |  |  | The measure mean for which the row qualified |
| 32 | `ORG_MRN_TXT` | VARCHAR(200) |  |  | MRN for the person |
| 33 | `PARENT_ENTITY_ID` | DOUBLE | NOT NULL |  | This column signifies unique value for which the row qualifies. Values will be either of one clinical_event_id/encntr_id/appt_id/ etc |
| 34 | `PARENT_ENTITY_NAME` | VARCHAR(30) |  |  | Will contain name of the table for which the row qualifies |
| 35 | `PERSON_ID` | DOUBLE | NOT NULL |  | Person id for the person |
| 36 | `POP_DESCRIPTION` | VARCHAR(100) |  |  | Detailed description for the qualification of the row |
| 37 | `POP_QUAL_DT_TM` | DATETIME |  |  | will hold admit_dt_tm/order_action_dt_tm/clinical_event_dt_tm/appointment_dt_tm depending on which query the row qualifies for. The value should be in accordance with the parent_entity_name and parent_entity_id columns. |
| 38 | `POP_QUAL_LOC_DT_TM` | DATETIME |  |  | The local version of the POP_QUAL_DT_TM column. |
| 39 | `QUALIFY_CCD` | DOUBLE |  |  | QUALIFY_CCD column will store the latest CCD Document Number. |
| 40 | `QUAL_SOURCE` | VARCHAR(50) |  |  | Displays why the patient is included in the denominator (referral source code, appointment, referred, clinical event code, etc.). |
| 41 | `QUAL_VALUE` | DOUBLE |  |  | Displays the value number of the qualifying source. |
| 42 | `QUERY_MEAN` | VARCHAR(50) |  |  | The name of the query for which the row qualified |
| 43 | `REF_ORDER_ID` | DOUBLE | NOT NULL |  | Will contain referral order id and will be used for TOC measure |
| 44 | `SUB_METRIC_TYPE` | VARCHAR(50) |  |  | More detailed information for which the row qualified |
| 45 | `UPDT_CNT` | DOUBLE |  |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 46 | `UPDT_DT_TM` | DATETIME |  |  | The date and time the row was last inserted or updated. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 47 | `UPDT_SOURCE` | VARCHAR(50) |  |  | The source which update/inserted the row |
| 48 | `UPDT_TASK` | VARCHAR(50) |  |  | The registered (assigned) task number for the process that inserted or updated the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `D_DISCHARGE_BUILDING_ID` | [LH_D_BUILDING](LH_D_BUILDING.md) | `D_BUILDING_ID` |
| `D_DISCHARGE_FACILITY_ID` | [LH_D_FACILITY](LH_D_FACILITY.md) | `D_FACILITY_ID` |
| `D_DISCHARGE_NURSE_UNIT_ID` | [LH_D_NURSE_UNIT](LH_D_NURSE_UNIT.md) | `D_NURSE_UNIT_ID` |
| `D_ENCNTR_TYPE_ID` | [LH_D_ENCNTR_TYPE](LH_D_ENCNTR_TYPE.md) | `D_ENCNTR_TYPE_ID` |
| `D_MED_SERVICE_ID` | [LH_D_MED_SERVICE](LH_D_MED_SERVICE.md) | `D_MED_SERVICE_ID` |
| `D_PERSON_ID` | [LH_D_PERSON](LH_D_PERSON.md) | `D_PERSON_ID` |
| `HEALTH_SYSTEM_SOURCE_ID` | [LH_D_BUILDING](LH_D_BUILDING.md) | `HEALTH_SYSTEM_SOURCE_ID` |
| `HEALTH_SYSTEM_SOURCE_ID` | [LH_D_ENCNTR_TYPE](LH_D_ENCNTR_TYPE.md) | `HEALTH_SYSTEM_SOURCE_ID` |
| `HEALTH_SYSTEM_SOURCE_ID` | [LH_D_FACILITY](LH_D_FACILITY.md) | `HEALTH_SYSTEM_SOURCE_ID` |
| `HEALTH_SYSTEM_SOURCE_ID` | [LH_D_MED_SERVICE](LH_D_MED_SERVICE.md) | `HEALTH_SYSTEM_SOURCE_ID` |
| `HEALTH_SYSTEM_SOURCE_ID` | [LH_D_NURSE_UNIT](LH_D_NURSE_UNIT.md) | `HEALTH_SYSTEM_SOURCE_ID` |
| `HEALTH_SYSTEM_SOURCE_ID` | [LH_D_PERSON](LH_D_PERSON.md) | `HEALTH_SYSTEM_SOURCE_ID` |

## Referenced by (4)

| From table | Column |
|------------|--------|
| [LH_MU_FX_3_DETAILS](LH_MU_FX_3_DETAILS.md) | `HEALTH_SYSTEM_SOURCE_ID` |
| [LH_MU_FX_3_DETAILS](LH_MU_FX_3_DETAILS.md) | `LH_MU_FX_3_POP_METRICS_ID` |
| [LH_MU_FX_3_EP_CCN_RELTN](LH_MU_FX_3_EP_CCN_RELTN.md) | `HEALTH_SYSTEM_SOURCE_ID` |
| [LH_MU_FX_3_EP_CCN_RELTN](LH_MU_FX_3_EP_CCN_RELTN.md) | `LH_MU_FX_3_POP_METRICS_ID` |

