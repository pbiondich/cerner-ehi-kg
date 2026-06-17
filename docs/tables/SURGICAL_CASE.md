# SURGICAL_CASE

> Contains the attributes of a surgical case, including patient, start and stop date/time, OR, primary surgeon, etc.

**Description:** Surgical Case  
**Table type:** ACTIVITY  
**Primary key:** `SURG_CASE_ID`  
**Columns:** 79  
**Referenced by:** 24 columns

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ACTIVE_IND` | DOUBLE |  |  | The table row is active or inactive. A row is generally active unless it is in an inactive state such as logically deleted, combined away, pending purge, etc. |
| 2 | `ACTIVE_STATUS_CD` | DOUBLE | NOT NULL |  | Indicates the status of the row itself (not the data in the row) such as active, inactive, combined away, pending purge, etc. |
| 3 | `ACTIVE_STATUS_DT_TM` | DATETIME |  |  | The date and time that the active_status_cd was set. |
| 4 | `ACTIVE_STATUS_PRSNL_ID` | DOUBLE | NOT NULL |  | The person who caused the active_status_cd to be set or change. |
| 5 | `ADDL_SUPPLIES_IND` | DOUBLE |  |  | Indicates that additional supplies have been requested by the Surgeon. |
| 6 | `ADD_ON_IND` | DOUBLE |  |  | Indicates that the Case is an "add-on" i.e. case is scheduled after the schedule has been finalized. |
| 7 | `ANESTH_PRSNL_ID` | DOUBLE | NOT NULL | FK→ | The primary anesthesiologist associated with this surgical case |
| 8 | `ANESTH_TYPE_CD` | DOUBLE | NOT NULL |  | *** OBSOLETE ***Column |
| 9 | `APPT_ID` | DOUBLE | NOT NULL |  | *** OBSOLETE ***Column |
| 10 | `ASA_CLASS_CD` | DOUBLE | NOT NULL |  | Used for Surgery Mgmt Reporting -- indicates the ASA class assoc. w/ this case |
| 11 | `CANCEL_DT_TM` | DATETIME |  |  | The date and time this case was cancelled |
| 12 | `CANCEL_REASON_CD` | DOUBLE | NOT NULL |  | The reason this surgical case was cancelled |
| 13 | `CANCEL_REQ_BY_ID` | DOUBLE | NOT NULL | FK→ | The person responsible for requesting the cancel of this case |
| 14 | `CANCEL_REQ_BY_TEXT` | VARCHAR(100) |  |  | The free-text name of the person responsible for requesting the cancel of this case (when not on prsnl table) |
| 15 | `CANCEL_TZ` | DOUBLE |  |  | Time zone associated with the corresponding DT_TM column. |
| 16 | `CASE_LEVEL_CD` | DOUBLE | NOT NULL |  | Used for Surgery Mgmt Reporting -- indicates the case level assoc. w/ this case |
| 17 | `CHECKIN_BY_ID` | DOUBLE | NOT NULL | FK→ | This is the person_id of the user that checked in the case. |
| 18 | `CHECKIN_DT_TM` | DATETIME |  |  | This is the date/time that the user checked in the case. |
| 19 | `CHECKIN_TZ` | DOUBLE |  |  | Time zone associated with the corresponding DT_TM column. |
| 20 | `CREATE_APPLCTX` | DOUBLE |  |  | Context of the application creating the row |
| 21 | `CREATE_DT_TM` | DATETIME |  |  | Creation Date and Time for this row |
| 22 | `CREATE_PRSNL_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the creation of the row in the table. |
| 23 | `CREATE_TASK` | DOUBLE |  |  | The registered (assigned) task number for the process that created the row. |
| 24 | `CURR_CASE_STATUS_CD` | DOUBLE | NOT NULL |  | The current status of this case, i.e. Patient In Holding, Patient In OR, etc. |
| 25 | `CURR_CASE_STATUS_DT_TM` | DATETIME |  |  | The date and time the current status of this case became effective |
| 26 | `DEPT_CD` | DOUBLE | NOT NULL |  | Used for Surgery Mgmt Reporting -- indicates the department assoc. w/ this case |
| 27 | `ENCNTR_ID` | DOUBLE | NOT NULL | FK→ | This is the value of the unique primary identifier of the encounter table. It is an internal system assigned number. |
| 28 | `ENHANCED_UI_IND` | DOUBLE | NOT NULL |  | Stores the preference indicator(0/1) which would help differentiate whether patient chart(surgical case) documentation should occur with enhanced workflows support or not. |
| 29 | `INST_CD` | DOUBLE | NOT NULL |  | Used for Surgery Mgmt Reporting -- indicates the institution assoc. w/ this case |
| 30 | `OR_SHIFT_CD` | DOUBLE | NOT NULL |  | Used for Surgery Mgmt Reporting -- indicates the shift that the start of this case falls in |
| 31 | `PAT_TYPE_CD` | DOUBLE | NOT NULL |  | Used for Surgery Mgmt Reporting -- indicates the patient type assoc. with this case |
| 32 | `PERSON_ID` | DOUBLE | NOT NULL | FK→ | This is the value of the unique primary identifier of the person table. It is an internal system assigned number. |
| 33 | `POSTOP_DIAG_TEXT_ID` | DOUBLE | NOT NULL |  | Postop Diagonosis Text Id |
| 34 | `PREOP_DIAG_TEXT_ID` | DOUBLE | NOT NULL |  | Preop Diagonosis Text IdColumn |
| 35 | `SCHED_ANESTH_PRSNL_ID` | DOUBLE | NOT NULL | FK→ | Used for Surgery Mgmt Reporting -- the anesthesiologist scheduled for this case |
| 36 | `SCHED_CASE_NBR_LOCN_CD` | DOUBLE | NOT NULL |  | Scheduled Case Number Location CodeColumn |
| 37 | `SCHED_CASE_TYPE_CD` | DOUBLE | NOT NULL |  | Scheduled Case Type |
| 38 | `SCHED_CLEANUP_DUR` | DOUBLE | NOT NULL |  | Scheduled Cleanup DurationColumn |
| 39 | `SCHED_DUR` | DOUBLE |  |  | Scheduled Case DurationColumn |
| 40 | `SCHED_OP_LOC_CD` | DOUBLE | NOT NULL |  | Scheduled Operating Room Location Code |
| 41 | `SCHED_OR_SHIFT_CD` | DOUBLE | NOT NULL |  | Used for Surgery Mgmt Reporting -- indicates the OR Shift assoc. w/ this case |
| 42 | `SCHED_PAT_TYPE_CD` | DOUBLE | NOT NULL |  | Scheduled Patient Type CodeColumn |
| 43 | `SCHED_QTY` | DOUBLE |  |  | Used for Surgery Mgmt Reporting -- indicates that this case has been scheduled |
| 44 | `SCHED_SETUP_DUR` | DOUBLE |  |  | Scheduled setup durationColumn |
| 45 | `SCHED_START_DAY` | DOUBLE |  |  | Used for Surgery Mgmt Reporting -- indicates the day of the week this case is scheduled to start on |
| 46 | `SCHED_START_DT_TM` | DATETIME |  |  | Scheduled Start Date TimeColumn |
| 47 | `SCHED_START_HOUR` | DOUBLE |  |  | Used for Surgery Mgmt Reporting -- indicates the hour of the day this case is scheduled to start on |
| 48 | `SCHED_START_MONTH` | DOUBLE |  |  | Used for Surgery Mgmt Reporting -- indicates the month this case is scheduled to start on |
| 49 | `SCHED_START_TZ` | DOUBLE |  |  | Time zone associated with the corresponding DT_TM column. |
| 50 | `SCHED_SURG_AREA_CD` | DOUBLE | NOT NULL |  | Scheduled Surgical Area CodeColumn |
| 51 | `SCHED_SURG_SPECIALTY_ID` | DOUBLE | NOT NULL |  | *** OBSOLETE *** |
| 52 | `SCHED_TYPE_CD` | DOUBLE | NOT NULL |  | Scheduled Type CodeColumn |
| 53 | `SCH_EVENT_ID` | DOUBLE | NOT NULL | FK→ | Scheduled Event IdColumn |
| 54 | `SURGEON_PRSNL_ID` | DOUBLE | NOT NULL | FK→ | The primary surgeon associated with this surgical case |
| 55 | `SURG_AREA_CD` | DOUBLE | NOT NULL |  | The surgical area associated with this surgical case |
| 56 | `SURG_CASE_ID` | DOUBLE | NOT NULL | PK | The primary key, uniquely identifying a surgical case |
| 57 | `SURG_CASE_NBR_CNT` | DOUBLE |  |  | The last portion of the OR Case Number, i.e. MAIN-1997- XXXXX. This number is incremented by 1 for each case, starting at 1 for the first case scheduled in a given year. |
| 58 | `SURG_CASE_NBR_FORMATTED` | VARCHAR(100) |  |  | The formatted Surgical case number |
| 59 | `SURG_CASE_NBR_LOCN_CD` | DOUBLE | NOT NULL |  | The surgical area associated with this case, used to retrieve the accession site prefix to be use in the OR Case Number, i.e. MAIN-xxxx-xxxx. |
| 60 | `SURG_CASE_NBR_YR` | DOUBLE |  |  | The middle portion of the OR Case Number, i.e. xxxx-1997-xxxx. The value is the year the case was scheduled IN, not the year the case was scheduled FOR. |
| 61 | `SURG_COMPLETE_QTY` | DOUBLE |  |  | Used for Surgery Mgmt Reporting -- indicates the completion of this case |
| 62 | `SURG_DUR_MIN` | DOUBLE |  |  | Used for Surgery Mgmt Reporting -- indicates the duration of this case |
| 63 | `SURG_OP_LOC_CD` | DOUBLE | NOT NULL |  | Used for Surgery Mgmt Reporting -- indicates the OR Number assoc. w/ this case |
| 64 | `SURG_SPECIALTY_ID` | DOUBLE | NOT NULL | FK→ | Used for Surgery Mgmt Reporting -- indicates the surgical specialty assoc. w/ this case |
| 65 | `SURG_START_DAY` | DOUBLE |  |  | Used for Surgery Mgmt Reporting -- indicates the day of the week this case was started |
| 66 | `SURG_START_DT_TM` | DATETIME |  |  | The date and time the surgical case started. |
| 67 | `SURG_START_HOUR` | DOUBLE |  |  | Used for Surgery Mgmt Reporting -- indicates the hour of the day this case was started |
| 68 | `SURG_START_MONTH` | DOUBLE |  |  | Used for Surgery Mgmt Reporting -- indicates the month this case was started |
| 69 | `SURG_START_TZ` | DOUBLE |  |  | Time zone associated with the corresponding DT_TM column. |
| 70 | `SURG_STOP_DT_TM` | DATETIME |  |  | The surgery stop date and time. |
| 71 | `SURG_STOP_TZ` | DOUBLE |  |  | Time zone associated with the corresponding DT_TM column. |
| 72 | `TURNOVER_DUR` | DOUBLE |  |  | Used for Surgery Mgmt Reporting -- the turnover duration for this case |
| 73 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 74 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 75 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 76 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 77 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |
| 78 | `UPDT_TZ` | DOUBLE |  |  | Time zone associated with the corresponding DT_TM column. |
| 79 | `WOUND_CLASS_CD` | DOUBLE | NOT NULL |  | Used for Surgery Mgmt Reporting -- indicates the wound class assoc. w/ this case |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `ANESTH_PRSNL_ID` | [PRSNL](PRSNL.md) | `PERSON_ID` |
| `CANCEL_REQ_BY_ID` | [PRSNL](PRSNL.md) | `PERSON_ID` |
| `CHECKIN_BY_ID` | [PRSNL](PRSNL.md) | `PERSON_ID` |
| `ENCNTR_ID` | [ENCOUNTER](ENCOUNTER.md) | `ENCNTR_ID` |
| `PERSON_ID` | [PERSON](PERSON.md) | `PERSON_ID` |
| `SCHED_ANESTH_PRSNL_ID` | [PRSNL](PRSNL.md) | `PERSON_ID` |
| `SCH_EVENT_ID` | [SCH_EVENT](SCH_EVENT.md) | `SCH_EVENT_ID` |
| `SURGEON_PRSNL_ID` | [PRSNL](PRSNL.md) | `PERSON_ID` |
| `SURG_SPECIALTY_ID` | [PRSNL_GROUP](PRSNL_GROUP.md) | `PRSNL_GROUP_ID` |

## Referenced by (24)

| From table | Column |
|------------|--------|
| [CASE_ATTENDANCE](CASE_ATTENDANCE.md) | `SURG_CASE_ID` |
| [CASE_CART](CASE_CART.md) | `SURG_CASE_ID` |
| [CASE_CART_PICK_LIST](CASE_CART_PICK_LIST.md) | `SURG_CASE_ID` |
| [CASE_TIMES](CASE_TIMES.md) | `SURG_CASE_ID` |
| [LH_CNT_IC_ADV_SURG_DATA](LH_CNT_IC_ADV_SURG_DATA.md) | `SURG_CASE_ID` |
| [MM_SUPPLY_CABINET](MM_SUPPLY_CABINET.md) | `SURG_CASE_ID` |
| [PERIOPERATIVE_DOCUMENT](PERIOPERATIVE_DOCUMENT.md) | `SURG_CASE_ID` |
| [RXS_ITEM_GROUP_ACT](RXS_ITEM_GROUP_ACT.md) | `SURG_CASE_ID` |
| [RXS_LOCATION_TASK](RXS_LOCATION_TASK.md) | `SURG_CASE_ID` |
| [SA_ANESTHESIA_RECORD](SA_ANESTHESIA_RECORD.md) | `SURGICAL_CASE_ID` |
| [SCHED_CASE_PICK_LIST](SCHED_CASE_PICK_LIST.md) | `SURG_CASE_ID` |
| [SN_ACUITY_LEVEL](SN_ACUITY_LEVEL.md) | `SURG_CASE_ID` |
| [SN_CASE_LONG_TEXT](SN_CASE_LONG_TEXT.md) | `SURG_CASE_ID` |
| [SN_CASE_TRACKING](SN_CASE_TRACKING.md) | `SURG_CASE_ID` |
| [SN_CHARGE_HEADER](SN_CHARGE_HEADER.md) | `SURG_CASE_ID` |
| [SN_CHARGE_ITEM](SN_CHARGE_ITEM.md) | `SURG_CASE_ID` |
| [SN_CHARGE_QUEUE](SN_CHARGE_QUEUE.md) | `SURG_CASE_ID` |
| [SN_IMPLANT_LOG_ST](SN_IMPLANT_LOG_ST.md) | `SURG_CASE_ID` |
| [SN_NOMEN_ST](SN_NOMEN_ST.md) | `SURG_CASE_ID` |
| [SN_PICKLIST](SN_PICKLIST.md) | `SURG_CASE_ID` |
| [SN_SURG_CASE_ST](SN_SURG_CASE_ST.md) | `SURG_CASE_ID` |
| [STAFF_ACTIVITY](STAFF_ACTIVITY.md) | `SURG_CASE_ID` |
| [SURGICAL_DELAY](SURGICAL_DELAY.md) | `SURG_CASE_ID` |
| [SURG_CASE_PROCEDURE](SURG_CASE_PROCEDURE.md) | `SURG_CASE_ID` |

