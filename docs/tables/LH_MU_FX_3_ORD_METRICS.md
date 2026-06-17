# LH_MU_FX_3_ORD_METRICS

> This table will contain the populated persons for the order based measures

**Description:** LH_MU_FX_3_ORD_METRICS  
**Table type:** ACTIVITY  
**Primary key:** `HEALTH_SYSTEM_SOURCE_ID`, `LH_MU_FX_3_ORD_METRICS_ID`  
**Columns:** 59  
**Referenced by:** 2 columns

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ACTION_PERSONNEL_ID` | DOUBLE | NOT NULL |  | Person who performs the action of placing the order ( could be anyone) |
| 2 | `ACTIVE_IND` | DOUBLE |  |  | The table row is active or inactive. A row is generally active unless it is in an inactive state such as logically deleted, combined away, pending purge, etc. |
| 3 | `ADMIT_DT_TM` | DATETIME |  |  | Registration date and time for the encounter |
| 4 | `ADMIT_LOC_DT_TM` | DATETIME |  |  | The local version of the ADMIT_DT_TM column. |
| 5 | `APPT_TYPE_CD` | DOUBLE | NOT NULL |  | Scheduling appointment type for encounter |
| 6 | `APPT_TYPE_TEXT` | VARCHAR(50) |  |  | The display for the appt_type_cd coming from code value table |
| 7 | `BIRTH_DT_TM` | DATETIME |  |  | Birth date and time for the person |
| 8 | `BIRTH_LOC_DT_TM` | DATETIME |  |  | The local version of the BIRTH_DT_TM column |
| 9 | `CCN_IND` | DOUBLE |  |  | will signify an inpatient encounter or an observation encounter |
| 10 | `COMMUNICATION_TYPE_CD` | DOUBLE | NOT NULL |  | The code represting the method of communication for the order action |
| 11 | `COMMUNICATION_TYPE_TEXT` | VARCHAR(50) |  |  | The string representing the method of communication for the order action |
| 12 | `DISCH_DT_TM` | DATETIME |  |  | Discharge date and time for the encounter |
| 13 | `DISCH_LOC_DT_TM` | DATETIME |  |  | The local version of the DISCH_DT_TM column. |
| 14 | `DISPENSE_IND` | DOUBLE |  |  | Order is dispensed in retail pharmet. 1= Yes 0 = No |
| 15 | `D_DISCHARGE_BUILDING_ID` | DOUBLE | NOT NULL | FK→ | Value comes from lh_d_building |
| 16 | `D_DISCHARGE_FACILITY_ID` | DOUBLE | NOT NULL | FK→ | Value comes from lh_d_facility |
| 17 | `D_DISCHARGE_NURSE_UNIT_ID` | DOUBLE | NOT NULL | FK→ | Value comes from lh_d_nurse_unit |
| 18 | `D_ENCNTR_TYPE_ID` | DOUBLE | NOT NULL | FK→ | Value comes from lh_d_encntr_type |
| 19 | `D_MED_SERVICE_ID` | DOUBLE | NOT NULL | FK→ | Value comes from lh_d_med_service |
| 20 | `D_PERSON_ID` | DOUBLE | NOT NULL | FK→ | Contains d_person_id for each person coming form lh_d_person table |
| 21 | `EC_IND` | DOUBLE | NOT NULL |  | Indicator used to show that an inpatient qualified for an EC. |
| 22 | `ENCNTR_ID` | DOUBLE | NOT NULL |  | Encntr_id of the person |
| 23 | `EP_IND` | DOUBLE |  |  | Will signify an outpatient encounter or an observation encounter |
| 24 | `EVENT_DESCRIPTION` | VARCHAR(100) |  |  | The description of the event. |
| 25 | `EVENT_DT_TM` | DATETIME |  |  | The date and time of the event (utc). |
| 26 | `EVENT_LOC_DT_TM` | DATETIME |  |  | The date and time of the event (local). |
| 27 | `EXTRACT_DT_TM` | DATETIME |  |  | Date and time the row was extracted into the table |
| 28 | `FINANCIAL_NBR_TXT` | VARCHAR(50) |  |  | Fin number for the encounter |
| 29 | `FIRST_PROCESS_DT_TM` | DATETIME |  |  | The date/time that the first ETL process started that created this record. |
| 30 | `FORMULARY_ENABLED_IND` | DOUBLE |  |  | Indicates if the formulary benefit was on/off |
| 31 | `HEALTH_SYSTEM_ID` | DOUBLE | NOT NULL |  | Identifies the delivery network responsible for supplying the data. |
| 32 | `HEALTH_SYSTEM_SOURCE_ID` | DOUBLE | NOT NULL | PK FK→ | Identifies the unique source within the delivery network responsible for supplying the data. |
| 33 | `IS_PRESCRIBED_IND` | DOUBLE |  |  | Indicates if the order was electronically prescribed |
| 34 | `LAST_PROCESS_DT_TM` | DATETIME |  |  | The date/time that the last ETL process started that updated this record. |
| 35 | `LH_MU_FX_3_ORD_METRICS_ID` | DOUBLE | NOT NULL | PK | Unique generated number that identifies a single row on the LH_MU_FX_3_ORD_METRICS table. |
| 36 | `LOGICAL_DOMAIN_ID` | DOUBLE | NOT NULL |  | The unique identifier for a logical domain. This identifier allows the data to be grouped by logical domain. For example, If you assign clients a logical_domain_id this would allow you to store data for multiple clients on this table. |
| 37 | `METRIC_TYPE` | VARCHAR(50) |  |  | The measure mean for which the row qualified |
| 38 | `NUMERATOR_IND` | DOUBLE |  |  | Indicates if the row qualifies for MET outcome |
| 39 | `ORDERING_PROVIDER_ID` | DOUBLE | NOT NULL |  | Provider who places the order |
| 40 | `ORDER_DETAIL_LINE` | VARCHAR(255) |  |  | Detailed description for the order |
| 41 | `ORDER_ID` | DOUBLE | NOT NULL |  | Unique value for each order coming from orders table |
| 42 | `ORG_MRN_TXT` | VARCHAR(50) |  |  | MRN for the person |
| 43 | `OUTCOME_DETAIL` | VARCHAR(100) |  |  | Reason for the outcome |
| 44 | `PERSON_ID` | DOUBLE | NOT NULL |  | Person id for the person |
| 45 | `POP_DESCRIPTION` | VARCHAR(100) |  |  | Detailed description for the qualification of the row |
| 46 | `POP_QUAL_DT_TM` | DATETIME |  |  | will hold admit_dt_tm/order_action_dt_tm/clinical_event_dt_tm/appointment_dt_tm depending on which query the row qualifies for. The value should be in accordance with the parent_entity_name and parent_entity_id columns. |
| 47 | `POP_QUAL_LOC_DT_TM` | DATETIME |  |  | The local version of the POP_QUAL_DT_TM column. |
| 48 | `POSITION_CD` | DOUBLE | NOT NULL |  | The position of the person placing the order ( e.g. dba no dta) |
| 49 | `POSITION_TEXT` | VARCHAR(50) |  |  | The string representing the position of the person placing the order coming from code_value table |
| 50 | `QUERY_MEAN` | VARCHAR(50) |  |  | The name of the query for which the row qualified |
| 51 | `SOURCE_CD` | DOUBLE | NOT NULL |  | Source of the order coming from orders table |
| 52 | `SOURCE_TEXT` | VARCHAR(50) |  |  | The String representing the source of the order coming from code_value table |
| 53 | `START_DT_TM` | DATETIME |  |  | Date and time when the order started |
| 54 | `START_LOC_DT_TM` | DATETIME |  |  | The local version of the START_DT_TM column. |
| 55 | `SUB_METRIC_TYPE` | VARCHAR(50) |  |  | More detailed information for which the row qualified |
| 56 | `UPDT_CNT` | DOUBLE |  |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 57 | `UPDT_DT_TM` | DATETIME |  |  | The date and time the row was last inserted or updated. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 58 | `UPDT_SOURCE` | VARCHAR(50) |  |  | The source which update/inserted the row |
| 59 | `UPDT_TASK` | VARCHAR(50) |  |  | The registered (assigned) task number for the process that inserted or updated the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |

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

## Referenced by (2)

| From table | Column |
|------------|--------|
| [LH_MU_FX_3_EP_CCN_RELTN](LH_MU_FX_3_EP_CCN_RELTN.md) | `HEALTH_SYSTEM_SOURCE_ID` |
| [LH_MU_FX_3_EP_CCN_RELTN](LH_MU_FX_3_EP_CCN_RELTN.md) | `LH_MU_FX_3_ORD_METRICS_ID` |

