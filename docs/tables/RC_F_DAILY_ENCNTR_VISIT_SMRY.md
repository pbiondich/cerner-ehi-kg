# RC_F_DAILY_ENCNTR_VISIT_SMRY

> This table contains summarized encounter visit data by day.

**Description:** Revenue Cycle Fact Daily Encounter Visit Summary  
**Table type:** ACTIVITY  
**Primary key:** _(not published — see note)_  
**Columns:** 23

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ACTIVITY_DT_NBR` | DOUBLE | NOT NULL | FK→ | A number representing the activity date. References the key in the OMF_DATE table. |
| 2 | `BEG_CENSUS_COUNT` | DOUBLE | NOT NULL |  | The total amount of encounters associated to a particular location at the beginning of the day. |
| 3 | `DAILY_ENCNTR_VISIT_SMRY_ID` | DOUBLE | NOT NULL |  | Uniquely identifies summarized encounter visit data by day. |
| 4 | `END_CENSUS_COUNT` | DOUBLE | NOT NULL |  | The total amount of encounters associated to a particular location at the end of a day. |
| 5 | `FIRST_PROCESS_DT_TM` | DATETIME | NOT NULL |  | The date/time that the first ETL process started that created this record. |
| 6 | `LAST_PROCESS_DT_TM` | DATETIME | NOT NULL |  | The date/time that the last ETL process started that updated this record. |
| 7 | `RC_D_ENCNTR_TYPE_CLASS_ID` | DOUBLE | NOT NULL | FK→ | Uniquely identifies encounter type class information related to this fact row. |
| 8 | `SHR_D_LOCATION_ID` | DOUBLE | NOT NULL | FK→ | Uniquely identifies the patient encounter location at the time of the claim event. |
| 9 | `TOTAL_ADMITTED_ENCNTRS` | DOUBLE | NOT NULL |  | Total number of encounters that have been admitted on a given day. |
| 10 | `TOTAL_ADMITTED_VRFD_ENCNTRS` | DOUBLE | NOT NULL |  | The total number of encounters that have their insurance verified prior to their admission on a given day. |
| 11 | `TOTAL_DISCHARGED_ENCNTRS` | DOUBLE | NOT NULL |  | The total number of encounters that have been discharged on a given day. |
| 12 | `TOTAL_DSCHRG_LENGTH_OF_STAY` | DOUBLE | NOT NULL |  | Sum of the number of days from the admission date to the patient's discharge date on a given day. |
| 13 | `TOTAL_ENCNTRS` | DOUBLE | NOT NULL |  | The total number of encounters aggregated into a given summary row. |
| 14 | `TOTAL_PATIENT_DAYS` | DOUBLE | NOT NULL |  | The total amount of patients that were at the facility on a given day. |
| 15 | `TOTAL_PRE_REG_ENCNTRS` | DOUBLE | NOT NULL |  | Total number of encounters that have been pre-registered on a given day. |
| 16 | `TOTAL_PRE_REG_VRFD_ENCNTRS` | DOUBLE | NOT NULL |  | Total number of encounters that have their insurance verified prior to their pre-registration on a given day. |
| 17 | `TOTAL_TRANSFER_IN_COUNT` | DOUBLE | NOT NULL |  | Total number of encounters who are newly associated to a location. |
| 18 | `TOTAL_TRANSFER_OUT_COUNT` | DOUBLE | NOT NULL |  | Total number of encounters who have transferred out of a location since the previous day. |
| 19 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 20 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 21 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 22 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 23 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `ACTIVITY_DT_NBR` | [OMF_DATE](OMF_DATE.md) | `DT_NBR` |
| `RC_D_ENCNTR_TYPE_CLASS_ID` | [RC_D_ENCNTR_TYPE_CLASS](RC_D_ENCNTR_TYPE_CLASS.md) | `RC_D_ENCNTR_TYPE_CLASS_ID` |
| `SHR_D_LOCATION_ID` | [SHR_D_LOCATION](SHR_D_LOCATION.md) | `SHR_D_LOCATION_ID` |

