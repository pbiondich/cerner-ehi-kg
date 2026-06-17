# OMF_CENSUS_SMRY_ST

> Summary table comprised of records extracted from omf_encntr_st to provide the daily census analysis data through PowerVision.

**Description:** Daily census extract.  
**Table type:** ACTIVITY  
**Primary key:** _(not published — see note)_  
**Columns:** 42

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ALT_LEVEL_OF_CARE_DISCH_CNT` | DOUBLE |  |  | The total number of encounters that were discharged from an Alternate Level of Care status between 00:00 and 23:59 on the census date. |
| 2 | `ALT_LEVEL_OF_CARE_WAIT_DAYS` | DOUBLE |  |  | For encounters that were discharged during the day from an Alternate Level of Care status on the census date: the total number of days that patients were in and Alternate Level of Care Status. This is the difference between the Alternate Level of Care Date/Time and the Discharge Date/Time. |
| 3 | `CENSUS_DT_NBR` | DOUBLE |  |  | The Julian date on which the census was taken. |
| 4 | `CENSUS_DT_TM` | DATETIME |  |  | The date/time on which the census was taken. |
| 5 | `CENSUS_TZ` | DOUBLE |  |  | Time zone associated with the corresponding DT_TM column. |
| 6 | `CURR_MTH_DISCH_PD` | DOUBLE |  |  | The number of person days for patients discharged on the given date. |
| 7 | `DISCH_CNT` | DOUBLE |  |  | The total number of encounters that were discharged during the census date. If a patient expired during their encounter they will not be counted as a discharge. |
| 8 | `ENCNTR_TYPE_CD` | DOUBLE | NOT NULL |  | The code value for the encounter type. |
| 9 | `EXPIRED_CNT` | DOUBLE |  |  | The total number of persons that expired during the census date. |
| 10 | `EXTENDED_LOA_RETURN_CNT` | DOUBLE |  |  | The total number of patients that returned from an extended leave of absence during the census date. |
| 11 | `FIN_CLASS_CD` | DOUBLE | NOT NULL |  | Financial class code value. |
| 12 | `INPATIENT_CNT` | DOUBLE |  |  | The number of inpatients that have not been discharged as of 11:59pm on the census date. |
| 13 | `INPATIENT_PD` | DOUBLE |  |  | The total number of patient days for patients that had not been discharged as of 11:59pm on the census date. |
| 14 | `ISOLATION_CD` | DOUBLE | NOT NULL |  | The isolation code indicates that some level of isolation or restricted access is required or in place for this patient indicating special procedure or consideration to be used when dealing with the patient. |
| 15 | `LOA_CNT` | DOUBLE |  |  | The total number of encounters that are on leave of absence on the census date at 23:59. |
| 16 | `LOC_BUILDING_CD` | DOUBLE | NOT NULL |  | The code value for the building. |
| 17 | `LOC_FACILITY_CD` | DOUBLE | NOT NULL |  | The code value for the facility. |
| 18 | `LOC_NURSE_UNIT_CD` | DOUBLE | NOT NULL |  | The code value for the nurse unit. |
| 19 | `MED_SERVICE_CD` | DOUBLE | NOT NULL |  | The code value for the medical service. |
| 20 | `NEW_EXTENDED_LOA_CNT` | DOUBLE |  |  | The total number of encounters that were placed on extended leave of absence during the census date. |
| 21 | `NEW_PEND_ARRIVAL_CNT` | DOUBLE |  |  | The total number of encounters that were placed on pending arrival during the census date. |
| 22 | `NEW_PEND_DISCH_CNT` | DOUBLE |  |  | The total number of encounters that were placed on pending discharge during the census date. |
| 23 | `OCCUPIED_BED_CNT` | DOUBLE |  |  | The total number of beds occupied by patients that had not been discharged as of 11:59pm on the census date. |
| 24 | `OCCUPIED_BED_PD` | DOUBLE |  |  | The total number of patient days for patients that had not been discharged as of 11:59pm on the census date. |
| 25 | `OMF_CENSUS_SMRY_ST_ID` | DOUBLE | NOT NULL |  | The unique identifier for the omf_census_smry_st summary table. |
| 26 | `ONE_DAY_STAY_CNT` | DOUBLE |  |  | The total number of encounters that were both admitted and discharged on the census date. |
| 27 | `PEND_ARRIVAL_ADMIT_CNT` | DOUBLE |  |  | The total number of encounters that were admitted from a Pending Arrival status during the census date. |
| 28 | `PEND_ARRIVAL_ADMIT_WAIT_DAYS` | DOUBLE |  |  | For encounters that were admitted during the census date from a pending arrival status: the total number of days they waited. This is the difference between the encounter's Pending Date/Time and the Registration Date/Time. |
| 29 | `PEND_DISCH_DISCH_CNT` | DOUBLE |  |  | The total number of encounters that were discharged during the day from a pending discharge status. |
| 30 | `PEND_DISCH_DISCH_WAIT_DAYS` | DOUBLE |  |  | For encounters that were discharged from a pending discharge status on the census date: the total number of days they waited. This is the difference between the encounters Pending Date/Time (Discharge) and the Discharge Date/Time. |
| 31 | `TOT_ADMIT_CNT` | DOUBLE |  |  | The total number of encounters that were admitted on the census date. |
| 32 | `TOT_ALT_LEVEL_OF_CARE_CNT` | DOUBLE |  |  | The total number of encounters that are in an Alternate Level of Care and are occupying beds at 23:59 of the census date. |
| 33 | `TOT_EXTENDED_LOA_CNT` | DOUBLE |  |  | The total number of encounters that are on extended leave of absence at 23:59 of the census date. |
| 34 | `TOT_PEND_ARRIVAL_CNT` | DOUBLE |  |  | The total number of encounters that are in a pending arrival status at 23:59 of the census date. |
| 35 | `TOT_PEND_DISCH_CNT` | DOUBLE |  |  | The total number of encounters that are in a pending discharge status at 23:59 of the census date. |
| 36 | `TRANSFER_IN_CNT` | DOUBLE |  |  | The total number of encounters that were transferred into the nurse unit on the census date. |
| 37 | `TRANSFER_OUT_CNT` | DOUBLE |  |  | The total number of encounters that were transferred out of the nurse unit on the census date. |
| 38 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 39 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 40 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 41 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 42 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

