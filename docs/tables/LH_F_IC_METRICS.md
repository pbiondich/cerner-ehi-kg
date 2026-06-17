# LH_F_IC_METRICS

> Infection control metrics.

**Description:** LH_F_IC_METRICS  
**Table type:** ACTIVITY  
**Primary key:** _(not published — see note)_  
**Columns:** 72

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ACTIVE_IND` | DOUBLE | NOT NULL |  | The table row is active or inactive. A row is generally active unless it is in an inactive state such as logically deleted, combined away, pending purge, etc. |
| 2 | `ADMIT_BED_CD` | DOUBLE | NOT NULL |  | Identifies the bed to which the patient was admitted. |
| 3 | `ADMIT_BUILDING_CD` | DOUBLE | NOT NULL |  | Identifies the building to which the patient was admitted. |
| 4 | `ADMIT_DT_TM` | DATETIME |  |  | The date/time on which the patient was admitted to the facility. |
| 5 | `ADMIT_FACILITY_CD` | DOUBLE | NOT NULL |  | Identifies the facility to which the patient was admitted. |
| 6 | `ADMIT_NURSE_UNIT_CD` | DOUBLE | NOT NULL |  | Identifies the nurse unit to which the patient was admitted. |
| 7 | `ADMIT_ROOM_CD` | DOUBLE | NOT NULL |  | Identifies the room to which the patient was admitted. |
| 8 | `ADMIT_UTC_DT_TM` | DATETIME |  |  | The date/time on which the patient was admitted to the facility. |
| 9 | `ARRIVAL_DT_TM` | DATETIME |  |  | The date/time on which the patient arrived at the facility. |
| 10 | `ARRIVAL_UTC_DT_TM` | DATETIME |  |  | The date/time on which the patient arrived at the facility. |
| 11 | `COMM_MRN_TXT` | VARCHAR(50) |  |  | Identifies the community medical record number of the patient. |
| 12 | `DISCHARGE_DT_TM` | DATETIME |  |  | The date/time on which the patient was discharged from the facility. |
| 13 | `DISCHARGE_UTC_DT_TM` | DATETIME |  |  | The date/time on which the patient was discharged from the facility. |
| 14 | `DISC_BED_CD` | DOUBLE | NOT NULL |  | Identifies the bed from which the patient was discharged. |
| 15 | `DISC_BUILDING_CD` | DOUBLE | NOT NULL |  | Identifies the building from which the patient was discharged. |
| 16 | `DISC_FACILITY_CD` | DOUBLE | NOT NULL |  | Identifies the facility from which the patient was discharged. |
| 17 | `DISC_NURSE_UNIT_CD` | DOUBLE | NOT NULL |  | Identifies the nurse unit from which the patient was discharged. |
| 18 | `DISC_ROOM_CD` | DOUBLE | NOT NULL |  | Identifies the room from which the patient was discharged. |
| 19 | `D_PERSON_ID` | DOUBLE | NOT NULL | FK→ | Identifies the person associated with the quality measure. |
| 20 | `ENCNTR_ID` | DOUBLE | NOT NULL |  | Identifies the encounter against which the quality measure is associated. |
| 21 | `ENCNTR_TYPE_FLAG` | DOUBLE |  |  | The type of encounter: 1=Inpatient, 2=Outpatient |
| 22 | `EXTRACT_DT_TM` | DATETIME |  |  | The date/time the record was extracted from the source system. |
| 23 | `FINANCIAL_NBR_TXT` | VARCHAR(50) | NOT NULL |  | Identifies the financial number of the patient. |
| 24 | `FIRST_PROCESS_DT_TM` | DATETIME |  |  | The date/time that the first ETL process started that created this record. |
| 25 | `F_IC_METRICS_ID` | DOUBLE | NOT NULL |  | Unique identifier for the infection control metrics. |
| 26 | `HAI_BSI_CL_CNT` | DOUBLE |  |  | Identifies the number of central line related bloodstream infections. |
| 27 | `HAI_BSI_CNT` | DOUBLE |  |  | Identifies the number of bloodstream infections for the patient. |
| 28 | `HAI_BSI_LAB_CNT` | DOUBLE |  |  | Identifies the number of lab confirmed blood stream infections. |
| 29 | `HAI_BSI_SEP_CNT` | DOUBLE |  |  | Identifies the number of sepsis related bloodstream infections. |
| 30 | `HAI_ON_ADMIT_IND` | DOUBLE |  |  | Identifies if the patient had a hospital associated infection on admission. |
| 31 | `HAI_PN_ASP_CNT` | DOUBLE |  |  | Identifies the number of aspiration pneumonia infections. |
| 32 | `HAI_PN_CNT` | DOUBLE |  |  | Identifies the number of pneumonia infections for the patient. |
| 33 | `HAI_PN_HAP_CNT` | DOUBLE |  |  | Identifies the number of hospital associated pneumonia infections. |
| 34 | `HAI_PN_PROC_CNT` | DOUBLE |  |  | Identifies the number of procedure related pneumonia infections. |
| 35 | `HAI_PN_VAP_CNT` | DOUBLE |  |  | Identifies the number of ventilator associated pneumonia infections. |
| 36 | `HAI_SSI_CNT` | DOUBLE |  |  | Identifies the number of surgical site infections. |
| 37 | `HAI_SSI_DIP_CNT` | DOUBLE |  |  | Identifies the number of deep incision primary infections. |
| 38 | `HAI_SSI_DIS_CNT` | DOUBLE |  |  | Identifies the number of deep incision secondary infections. |
| 39 | `HAI_SSI_ORGAN_CNT` | DOUBLE |  |  | Identifies the number of organ/space infections. |
| 40 | `HAI_SSI_SIP_CNT` | DOUBLE |  |  | Identifies the number of superficial incision primary infections. |
| 41 | `HAI_SSI_SIS_CNT` | DOUBLE |  |  | Identifies the number of superficial incision secondary infections. |
| 42 | `HAI_UTI_ASYMP_CNT` | DOUBLE |  |  | Identifies the number of asymptomatic urinary tract infections. |
| 43 | `HAI_UTI_CATH_CNT` | DOUBLE |  |  | Identifies the number of catheter related urinary tract infections. |
| 44 | `HAI_UTI_CNT` | DOUBLE |  |  | Identifies the number of urinary tract infections for the patient. |
| 45 | `HAI_UTI_OTHER_CNT` | DOUBLE |  |  | Identifies the number of other urinary tract infections. |
| 46 | `HAI_UTI_SYMP_CNT` | DOUBLE |  |  | Identifies the number of symptomatic urinary tract infections. |
| 47 | `HEALTH_SYSTEM_ID` | DOUBLE | NOT NULL |  | Identifies the delivery network responsible for supplying the data. |
| 48 | `HEALTH_SYSTEM_SOURCE_ID` | DOUBLE | NOT NULL | FK→ | Identifies the unique source within the delivery network responsible for supplying the data. |
| 49 | `ISOLATION_IND` | DOUBLE |  |  | Identifies if the patient was in isolation during their visit. |
| 50 | `LAST_PROCESS_DT_TM` | DATETIME |  |  | The date/time that the last ETL process started that updated this record. |
| 51 | `LOGICAL_DOMAIN_ID` | DOUBLE | NOT NULL |  | The unique identifier for a logical domain. This identifier allows the data to be grouped by logical domain. For example, If you assign clients a logical_domain_id this would allow you to store data for multiple clients on this table. |
| 52 | `ORGANISM_IND` | DOUBLE |  |  | Identifies if the patient is to be included in the organism summary. |
| 53 | `ORG_MRN_TXT` | VARCHAR(50) |  |  | Identifies the medical record number of the patient. |
| 54 | `PARTITION_DT_TM` | DATETIME |  |  | The date/time the encounter was discharged from the facility. |
| 55 | `PERSON_ID` | DOUBLE | NOT NULL |  | Identifiers the person against which the quality measure is associated. |
| 56 | `REPORTABLE_CONDITION_IND` | DOUBLE |  |  | Identifies if the patient had a reportable condition. |
| 57 | `TB_COLLECT_BED_CD` | DOUBLE | NOT NULL |  | Identifies the location of the patient when the TB specimen was collected. |
| 58 | `TB_COLLECT_BUILDING_CD` | DOUBLE | NOT NULL |  | Identifies the location of the patient when the TB specimen was collected. |
| 59 | `TB_COLLECT_DT_TM` | DATETIME |  |  | Identifies the date/time on which the tb specimen was collected. |
| 60 | `TB_COLLECT_FACILITY_CD` | DOUBLE | NOT NULL |  | Identifies the location of the patient when the TB specimen was collected. |
| 61 | `TB_COLLECT_NURSE_UNIT_CD` | DOUBLE | NOT NULL |  | Identifies the location of the patient when the TB specimen was collected. |
| 62 | `TB_COLLECT_ROOM_CD` | DOUBLE | NOT NULL |  | Identifies the location of the patient when the TB specimen was collected. |
| 63 | `TB_COLLECT_UTC_DT_TM` | DATETIME |  |  | Identifies the date/time on which the tb specimen was collected. |
| 64 | `TB_EVENT_ID` | DOUBLE | NOT NULL |  | Identifies the clinical event record associated with the TB result. |
| 65 | `TB_FLAG` | DOUBLE |  |  | Identifies if the patient had a positive result for TB. |
| 66 | `TB_RESULT_DT_TM` | DATETIME |  |  | Identifies the date/time of the positive result. |
| 67 | `TB_RESULT_UTC_DT_TM` | DATETIME |  |  | Identifies the date/time of the positive result. |
| 68 | `TB_SPECIMEN_SOURCE_CD` | DOUBLE | NOT NULL |  | Identifies the code value associated with the tb specimen source. |
| 69 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 70 | `UPDT_DT_TM` | DATETIME |  |  | The date and time the row was last inserted or updated. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 71 | `UPDT_SOURCE` | VARCHAR(50) | NOT NULL |  | The script name responsible for updating the record. |
| 72 | `UPDT_TASK` | VARCHAR(50) | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `D_PERSON_ID` | [LH_D_PERSON](LH_D_PERSON.md) | `D_PERSON_ID` |
| `HEALTH_SYSTEM_SOURCE_ID` | [LH_D_PERSON](LH_D_PERSON.md) | `HEALTH_SYSTEM_SOURCE_ID` |

