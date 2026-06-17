# RCM_TLC_FACILITY

> Facilities returned from the TLC service.

**Description:** RevWorks Care Management - Total Living Choices Facility  
**Table type:** REFERENCE  
**Primary key:** `RCM_TLC_FACILITY_ID`  
**Columns:** 15  
**Referenced by:** 7 columns

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `CITY_NAME` | VARCHAR(100) | NOT NULL |  | Contains the name of the city. |
| 2 | `COUNTRY_NAME` | VARCHAR(100) | NOT NULL |  | Name of the country. |
| 3 | `DELIVER_TO_TXT` | VARCHAR(100) | NOT NULL |  | Contains the attention line of the address. |
| 4 | `PHONE` | VARCHAR(100) | NOT NULL |  | Contains the phone number. |
| 5 | `POSTAL_CODE` | VARCHAR(25) | NOT NULL |  | Contains the postal code. |
| 6 | `RCM_TLC_FACILITY_ID` | DOUBLE | NOT NULL | PK | Uniquely identifies facility data on the table will represent long term care facilities that Total Living Choices (TLC) is using to place patients. |
| 7 | `STATE_NAME` | VARCHAR(100) | NOT NULL |  | Contains the state name. |
| 8 | `STREET_NAME` | VARCHAR(100) | NOT NULL |  | Contains the name of the street. |
| 9 | `TLC_FACILITY_IDENT` | VARCHAR(100) | NOT NULL |  | Identifies data coming from a third party. |
| 10 | `TLC_FACILITY_NAME` | VARCHAR(100) | NOT NULL |  | Name of the facility returned from TLC. |
| 11 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 12 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 13 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 14 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 15 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Referenced by (7)

| From table | Column |
|------------|--------|
| [ENCNTR_AVOIDABLE_DAYS](ENCNTR_AVOIDABLE_DAYS.md) | `TLC_FACILITY_ID` |
| [ENCNTR_READMIT_ASSESS](ENCNTR_READMIT_ASSESS.md) | `TLC_FACILITY_ID` |
| [RCM_TLC_FAC_TYPE_FAC_R](RCM_TLC_FAC_TYPE_FAC_R.md) | `RCM_TLC_FACILITY_ID` |
| [RCM_TLC_PLACEMENT](RCM_TLC_PLACEMENT.md) | `FINAL_TLC_FACILITY_ID` |
| [RCM_TLC_PLACEMENT_FAC_R](RCM_TLC_PLACEMENT_FAC_R.md) | `RCM_TLC_FACILITY_ID` |
| [RCM_TLC_SERVICE](RCM_TLC_SERVICE.md) | `FINAL_TLC_FACILITY_ID` |
| [RCM_TLC_SERVICE_FAC_R](RCM_TLC_SERVICE_FAC_R.md) | `RCM_TLC_FACILITY_ID` |

