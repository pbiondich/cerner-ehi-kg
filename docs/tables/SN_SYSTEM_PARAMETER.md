# SN_SYSTEM_PARAMETER

> System parameters used by various SurgiNet applications

**Description:** SurgiNet System Parameter  
**Table type:** REFERENCE  
**Primary key:** _(not published — see note)_  
**Columns:** 62

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ALLOW_DB_DELETES_IND` | DOUBLE |  |  | *** OBSOLETE ***Column |
| 2 | `ANESTHESIA_INTERVAL` | DOUBLE |  |  | Default time interval for data collection |
| 3 | `ANEST_OPT_FLAG` | DOUBLE |  |  | Used to determine the type of charge used for anesthesia. |
| 4 | `ANEST_TIME_IND` | DOUBLE |  |  | *** OBSOLETE ***Column |
| 5 | `ASSIGN_DT_RANGE_IND` | DOUBLE |  |  | *** OBSOLETE ***Column |
| 6 | `ASSIGN_GRID_TM_START` | DOUBLE |  |  | *** OBSOLETE ***Column |
| 7 | `ASSIGN_GRID_TM_STOP` | DOUBLE |  |  | *** OBSOLETE ***Column |
| 8 | `ASSIGN_METHOD_FLAG` | DOUBLE |  |  | *** OBSOLETE ***Column |
| 9 | `ASSIGN_SURG_PRSNL_IND` | DOUBLE |  |  | *** OBSOLETE ***Column |
| 10 | `ASSIGN_SURG_ROLE_IND` | DOUBLE |  |  | *** OBSOLETE ***Column |
| 11 | `ASSIGN_TM_RANGE_IND` | DOUBLE |  |  | *** OBSOLETE ***Column |
| 12 | `ASSIGN_TM_RANGE_START_TM` | DOUBLE |  |  | *** OBSOLETE ***Column |
| 13 | `AUTO_GROUP_IND` | DOUBLE |  |  | *** OBSOLETE ***Column |
| 14 | `BY_PROC_DOC_IND` | DOUBLE |  |  | *** OBSOLETE ***Column |
| 15 | `BY_PROC_PICK_LIST_IND` | DOUBLE |  |  | *** OBSOLETE ***Column |
| 16 | `CASE_CART_GEN_DAYS_AHEAD` | DOUBLE |  |  | *** OBSOLETE ***Column |
| 17 | `CHARGE_WASTE_IND` | DOUBLE |  |  | *** OBSOLETE ***Column |
| 18 | `CLEANUP_TIME` | DOUBLE |  |  | Default Cleanup Time for the Procedure |
| 19 | `CNT_NUM_CONFIRM` | DOUBLE |  |  | *** OBSOLETE ***Column |
| 20 | `DEF_CNT_HDG` | VARCHAR(25) |  |  | *** OBSOLETE ***Column |
| 21 | `DEF_GRP_HDG` | VARCHAR(25) |  |  | *** OBSOLETE ***Column |
| 22 | `DEF_POSTOP_DIAG_SAME_IND` | DOUBLE |  |  | *** OBSOLETE ***Column |
| 23 | `DEF_SEG_LIST_ID` | DOUBLE | NOT NULL |  | *** OBSOLETE ***Column |
| 24 | `DEF_SEG_LIST_VER_NBR` | DOUBLE |  |  | *** OBSOLETE ***Column |
| 25 | `DEF_SURG_SPECIALTY_FLAG` | DOUBLE |  |  | Used by Surgical Case Manager -- An indicator of whether the surgical specialty should be defaulted from the primary surgeon's primary specialty (personnel group of "SURGSPEC") or the scheduled procedure's associated specialty |
| 26 | `DEPT_CD` | DOUBLE | NOT NULL |  | The department to be used for department-specific logic. This will eventually be replaced by location-filter logic (when sign-on to a location is available). |
| 27 | `GENERIC_PREF_CARD_DESC` | VARCHAR(30) |  |  | *** OBSOLETE ***Column |
| 28 | `INST_CD` | DOUBLE | NOT NULL |  | The institution to be used for institution-specific logic. This will eventually be replaced by location-filter logic (when sign-on to a location is available). |
| 29 | `INTRAOP_DOC_IND` | DOUBLE |  |  | *** OBSOLETE ***Column |
| 30 | `ITEM_COST_TYPE_CD` | DOUBLE | NOT NULL |  | *** OBSOLETE ***Column |
| 31 | `ITEM_MERGE_OPTION_FLAG` | DOUBLE |  |  | *** OBSOLETE ***Column |
| 32 | `NUM_CASES_REC_AVG` | DOUBLE |  |  | Number of cases to be used for recent average calculation |
| 33 | `NUM_DAYS_ASSIGN_START_DT` | DOUBLE |  |  | *** OBSOLETE ***Column |
| 34 | `NUM_DAYS_EXISTING_ASSIGNS` | DOUBLE |  |  | *** OBSOLETE ***Column |
| 35 | `NUM_DAYS_LOOKBACK` | DOUBLE |  |  | *** OBSOLETE ***Column |
| 36 | `PICK_LIST_DUP_FLAG` | DOUBLE |  |  | *** OBSOLETE ***Column |
| 37 | `PREF_CARD_DETAILS_TAB_IND` | DOUBLE |  |  | *** OBSOLETE ***Column |
| 38 | `PREF_CARD_EMAIL_ADDR` | VARCHAR(100) |  |  | *** OBSOLETE ***Column |
| 39 | `PRINT_OPEN_HOLD_IND` | DOUBLE |  |  | An indicator of whether open and hold quantity or just total requested quantity should print on the Case Pick List. |
| 40 | `PROCEDURE_CHARGE_FLAG` | DOUBLE |  |  | This specifies how the procedure charges are calculated |
| 41 | `QTY_ON_HAND_IND` | DOUBLE |  |  | *** OBSOLETE ***Column |
| 42 | `REPORTS_VERSION_NBR` | VARCHAR(20) |  |  | *** OBSOLETE ***Column |
| 43 | `REPORT_CLASS_INSTANCE_CD` | DOUBLE | NOT NULL |  | *** OBSOLETE ***Column |
| 44 | `ROOM_TIME_OPT_FLAG` | DOUBLE | NOT NULL |  | Time in/out to use for room time charges |
| 45 | `ROOT_LOC_CD` | DOUBLE | NOT NULL |  | *** OBSOLETE ***Column |
| 46 | `SETUP_CLEANUP_IND` | DOUBLE | NOT NULL |  | determine if setup and cleanup times should be included in room charges |
| 47 | `SETUP_TIME` | DOUBLE |  |  | Default Setup Time |
| 48 | `SN_SYS_PARAM_ID` | DOUBLE | NOT NULL |  | The primary key, uniquely identifying a row on this table |
| 49 | `SUB_FOR_ALL_DATES_IND` | DOUBLE |  |  | *** OBSOLETE ***Column |
| 50 | `SUB_WITH_VERIFY_IND` | DOUBLE |  |  | *** OBSOLETE ***Column |
| 51 | `SURG_AREA_CD` | DOUBLE | NOT NULL |  | The surgical area (CDF Meaning = "SURGAREA" on service resource codeset) to be used for surgical area-specific logic. This will eventually be replaced by location-filter logic (when sign-on to a location is available). |
| 52 | `SURG_AREA_NAME_KEY` | VARCHAR(32) |  |  | A unique key used to identify a row on the table; associated with the surgical area |
| 53 | `SURG_CHARGES_IND` | DOUBLE | NOT NULL |  | To determine if charging info should be sent to the AFC server |
| 54 | `SURG_STAGE_CD` | DOUBLE | NOT NULL |  | The surgical staging area to be used for surgical staging area-specific logic. This will eventually be replaced by location-filter logic (when sign-on to a location is available). |
| 55 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 56 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 57 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 58 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 59 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |
| 60 | `USE_CNT_TOTAL_IND` | DOUBLE |  |  | *** OBSOLETE ***Column |
| 61 | `USE_OPTION_FLAG` | DOUBLE |  |  | *** OBSOLETE ***Column |
| 62 | `WOUND_CLASS_DISP_IND` | DOUBLE |  |  | *** OBSOLETE ***Column |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

