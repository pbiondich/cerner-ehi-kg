# PM_WAIT_LIST_HIST

> Person Mgmt: History of wait list information

**Description:** Person Management Wait List History  
**Table type:** ACTIVITY  
**Primary key:** _(not published — see note)_  
**Columns:** 104

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ACCOMMODATION_CD` | DOUBLE | NOT NULL |  | Current type of accommodations in which the patient (encounter) has been placed. (e.g. Private, Semi Private, etc.) |
| 2 | `ACTIVE_IND` | DOUBLE |  |  | The table row is active or inactive. A row is generally active unless it is in an inactive state such as logically deleted, combined away, pending purge, etc. |
| 3 | `ACTIVE_STATUS_CD` | DOUBLE | NOT NULL |  | Indicates the status of the row itself (not the data in the row) such as active, inactive, combined away, pending purge, etc. |
| 4 | `ACTIVE_STATUS_DT_TM` | DATETIME |  |  | The date and time that the active_status_cd was set. |
| 5 | `ACTIVE_STATUS_PRSNL_ID` | DOUBLE | NOT NULL |  | The person who caused the active_status_cd to be set or change. |
| 6 | `ADMITTING_PRSNL_ID` | DOUBLE | NOT NULL |  | This is a key from the Personnel(PRSNL) table. It is the personnel that admitted the patient. |
| 7 | `ADMIT_BOOKING_CD` | DOUBLE | NOT NULL |  | The admission booking type. Examples are full booking, partial booking, etc. |
| 8 | `ADMIT_CATEGORY_CD` | DOUBLE | NOT NULL |  | Admission or administrative category of the wait list. An example would be 'private'. or 'NHS'. |
| 9 | `ADMIT_DECISION_DT_TM` | DATETIME |  |  | Date and time the decision to admit was made |
| 10 | `ADMIT_GUARANTEED_DT_TM` | DATETIME |  |  | The guaranteed admission date and time. |
| 11 | `ADMIT_OFFER_OUTCOME_CD` | DOUBLE | NOT NULL |  | Outcome of waiting list admission (ex. patient admitted and treated, patient admitted and suspended, Another appointment given). |
| 12 | `ADMIT_TYPE_CD` | DOUBLE | NOT NULL |  | Admit type indicates the circumstance under which the patient was admit or will be admitted. (i.e., accident, emergent, routine, elective, labor/delivery, etc.) |
| 13 | `ANESTHETIC_CD` | DOUBLE | NOT NULL |  | Waiting list anesthetic code (ex. Local anesthetic, epidural) |
| 14 | `APPOINTMENT_CD` | DOUBLE | NOT NULL |  | Did the patient have an appointment. |
| 15 | `ATTENDANCE_CD` | DOUBLE | NOT NULL |  | Attendance record of the appontment. Such as 'on time', 'arrived late', etc. |
| 16 | `ATTENDDOC_CLINICAL_SERVICE_CD` | DOUBLE | NOT NULL |  | Attending physician's default clinical service code. |
| 17 | `AUTO_BLOOD_IND` | DOUBLE |  |  | Indicate if the current encounter has autologous blood donation. |
| 18 | `BEG_EFFECTIVE_DT_TM` | DATETIME | NOT NULL |  | The date and time for which this table row becomes effective. Normally, this will be the date and time the row is added, but could be a past or future date and time. |
| 19 | `CANCER_REFERRAL_CD` | DOUBLE | NOT NULL |  | The Cancer Referral Code describes whether the referral is a cancer referral. |
| 20 | `CHANGE_2_BIT` | DOUBLE | NOT NULL |  | Identifies which columns have had a change. |
| 21 | `CHANGE_BIT` | DOUBLE | NOT NULL |  | Identifies which columns have had a change. |
| 22 | `CHG_DT_TM` | DATETIME |  |  | Date and time change was made. |
| 23 | `CHG_ID` | DOUBLE | NOT NULL |  | ID of person making change. |
| 24 | `COMMENTS_RE_DISCHARGE` | VARCHAR(255) |  |  | Text comments for a discharge. |
| 25 | `COMMISSIONER_REFERENCE` | VARCHAR(50) |  |  | Commissioner reference identifier. |
| 26 | `CONTRACT_STATUS_CD` | DOUBLE | NOT NULL |  | Codified field indicating status of a care contract. |
| 27 | `DECLINE_STATUS_CD` | DOUBLE | NOT NULL |  | Field contains a code value that contains a textual reason for a decline. |
| 28 | `DECLINE_STATUS_DT_TM` | DATETIME |  |  | Date and Time Decline Status was set. |
| 29 | `DELAY_STATUS_CD` | DOUBLE | NOT NULL |  | Field that contains a code that refers to a text description of the reason a delay status occurred. |
| 30 | `DELAY_STATUS_DT_TM` | DATETIME |  |  | Date/Time that a delay status was set. |
| 31 | `DIAGNOSIS_ID` | DOUBLE | NOT NULL | FK→ | Patient's diagnosis. This is a key field in the Diagnosis table. |
| 32 | `ENCNTR_ID` | DOUBLE | NOT NULL | FK→ | This is the value of the unique primary identifier of the encounter table. It is an internal system assigned number. |
| 33 | `END_EFFECTIVE_DT_TM` | DATETIME | NOT NULL |  | The date/time after which the row is no longer valid as active current data. This may be valued with the date that the row became inactive. |
| 34 | `EST_ADMIT_DT_TM` | DATETIME |  |  | Estimated Date/Time that a person on the wait list will be admitted. |
| 35 | `EST_ARRIVE_DT_TM` | DATETIME |  |  | Estimated Patient Arrival. |
| 36 | `EST_LENGTH_PROCEDURE_CD` | DOUBLE | NOT NULL |  | Field that contains a code the refers to a length of time. For example, 10 Mins, 15 Mins, etc. |
| 37 | `FINANCIAL_CLASS_CD` | DOUBLE | NOT NULL |  | The financial classification used for a given encounter. Examples may include Worker's Comp, Self Pay, etc. |
| 38 | `FINANCIAL_CLASS_EFF_DT_TM` | DATETIME |  |  | The date/time that a financial class becomes effective. |
| 39 | `FROM_ED_IND` | DOUBLE | NOT NULL |  | Indicates whether this encounter was transferred from the emergency department. |
| 40 | `FUNCTIONAL_DEFICIENCY_CAUSE_CD` | DOUBLE | NOT NULL |  | The primary presenting cause of functional deficiency. |
| 41 | `FUNCTIONAL_DEFICIENCY_CD` | DOUBLE | NOT NULL |  | Function to be restored, by reference to the affected part of the body, which is the subject of the particular wait list record. |
| 42 | `HIST_ACTION` | VARCHAR(3) | NOT NULL |  | Action taken. Example: UPT, RMV |
| 43 | `LAST_DNA_DT_TM` | DATETIME |  |  | Last date and time a DNA was recorded for a waiting list entry |
| 44 | `LOCATION_CD` | DOUBLE | NOT NULL | FK→ | The field contains a code that identifies the current permanent location of the patient. |
| 45 | `LOC_BED_CD` | DOUBLE | NOT NULL | FK→ | This field is the code value for a current patient location with a location type of bed. |
| 46 | `LOC_BUILDING_CD` | DOUBLE | NOT NULL | FK→ | This field is the code value for the current patient location with a location type of building. |
| 47 | `LOC_FACILITY_CD` | DOUBLE | NOT NULL | FK→ | This field is the code value for the current patient location with a location type of facility. |
| 48 | `LOC_NURSE_UNIT_CD` | DOUBLE | NOT NULL | FK→ | This field is the code value for the current patient location with a location type of Nurse Unit. |
| 49 | `LOC_ROOM_CD` | DOUBLE | NOT NULL | FK→ | This field is the code value for the current patient location with a location type of Room. |
| 50 | `MANAGEMENT_CD` | DOUBLE | NOT NULL |  | Intended management. |
| 51 | `MED_SERVICE_CD` | DOUBLE | NOT NULL |  | The type or category of medical service that the patient is receiving in relation to their encounter. The category may be of treatment type, surgery, general resources, or others. |
| 52 | `NCEPOD_CD` | DOUBLE | NOT NULL |  | The NCEPOD (National Confidential Enquiry into Patient Outcome and Death) Classification categorizes the urgency of the patient's intervention. |
| 53 | `OPERATION_CD` | DOUBLE | NOT NULL |  | Waiting list operation code (ex. One or more operative procedure carried out, . no operative procedures performed or intended) |
| 54 | `ORIG_REQUEST_RECEIVED_DT_TM` | DATETIME |  |  | Original date and time that the wait list request was received. |
| 55 | `OTHER_MED_CONDITION` | VARCHAR(40) |  |  | Text description of a medical condition. |
| 56 | `PEND_ACCEPTANCE_DT_TM` | DATETIME |  |  | Pending Acceptance Date and Time. |
| 57 | `PEND_NOTIFICATION_DT_TM` | DATETIME |  |  | Pending Notification date and time. |
| 58 | `PEND_PLACE_PRIORITY_CD` | DOUBLE | NOT NULL |  | The level of importance in bed assignment activity in relation to other encounters. |
| 59 | `PEND_PLACE_PRIORITY_DT_TM` | DATETIME |  |  | The level date and time when the pending location placement priority was set. |
| 60 | `PERSON_ID` | DOUBLE | NOT NULL | FK→ | This is the value of the unique primary identifier of the person table. It is an internal system assigned number. |
| 61 | `PLANNED_ADMIT_DT_TM` | DATETIME |  |  | The date/time a patient is planned to be admitted. |
| 62 | `PLANNED_OPERATION_CD` | DOUBLE | NOT NULL |  | A field containing a code value that represents a planned operation. |
| 63 | `PLANNED_PROCEDURE_CD` | DOUBLE | NOT NULL |  | The code value for the planned Procedure for this wait list row. |
| 64 | `PLANNED_PROCEDURE_DT_TM` | DATETIME |  |  | The date/time the procedure is planned to occur. |
| 65 | `PM_HIST_TRACKING_ID` | DOUBLE | NOT NULL | FK→ | This is the value of the unique primary identifier of the pm_hist_tracking table. It is an internal system assigned number. |
| 66 | `PM_WAIT_LIST_HIST_ID` | DOUBLE | NOT NULL |  | This is the unique identifier for a wait list history row. |
| 67 | `PM_WAIT_LIST_ID` | DOUBLE | NOT NULL | FK→ | This is a primary key from the PM_WAIT_LIST table. It is a unique identifier of a wait list row. |
| 68 | `PREV_PROV_ADMIT_DT_TM` | DATETIME |  |  | Previous provider's admission date and time |
| 69 | `PRE_ADMIT_ATTEND_IND` | DOUBLE |  |  | Indicates whether the attending physician performed the pre admit. |
| 70 | `PRE_ADMIT_CLIN_APPT_DT_TM` | DATETIME |  |  | Date/Time an appointment was set before admit. |
| 71 | `PROCEDURE_ID` | DOUBLE | NOT NULL | FK→ | Procedure id is the primary unique identification number of the procedure table. It is an internal system assigned sequence number. |
| 72 | `PROVISIONAL_ADMIT_DT_TM` | DATETIME |  |  | Date/Time the provisional admit was made. |
| 73 | `REASON_FOR_CHANGE_CD` | DOUBLE | NOT NULL |  | Code value for a text description of the reason a change was made. |
| 74 | `REASON_FOR_REMOVAL` | VARCHAR(255) |  |  | A text description of the reason a removal was made. |
| 75 | `REASON_FOR_REMOVAL_CD` | DOUBLE | NOT NULL |  | Code value for a text description of the reason a removal was made. |
| 76 | `RECOMMEND_DT_TM` | DATETIME |  |  | The date/time that removal,etc. was recommended. |
| 77 | `REFERRAL_DT_TM` | DATETIME |  |  | The date and time of the referral. |
| 78 | `REFERRAL_REASON_CD` | DOUBLE | NOT NULL |  | The resaon for the referral. |
| 79 | `REFERRAL_SOURCE_CD` | DOUBLE | NOT NULL |  | Source of referral. |
| 80 | `REFERRAL_TYPE_CD` | DOUBLE | NOT NULL |  | Referral type. |
| 81 | `REMOVAL_DT_TM` | DATETIME |  |  | Date/Time that a person was removed from the wait list. |
| 82 | `REQUESTED_LOCATION_CD` | DOUBLE | NOT NULL |  | Code value representing the location a patient on the wait list requested to be moved to. |
| 83 | `RESCHD_APPT_BY_DT_TM` | DATETIME |  |  | The guaranteed date that the appoinment will be rescheduled by. |
| 84 | `SERVICE_TYPE_REQUESTED_CD` | DOUBLE | NOT NULL |  | Service type requested. |
| 85 | `STAND_BY_CD` | DOUBLE | NOT NULL |  | Code Value that contains a text description of a wait list stand by. |
| 86 | `STATUS_CD` | DOUBLE | NOT NULL |  | Code value that refers to the status of a wait list row. Examples: Normal, Deferred. |
| 87 | `STATUS_DETAIL_CD` | DOUBLE | NOT NULL |  | This code value represents further detail on the main wait list status. |
| 88 | `STATUS_DT_TM` | DATETIME |  |  | The date/time a status was set. |
| 89 | `STATUS_END_DT_TM` | DATETIME |  |  | Status end date time. |
| 90 | `STATUS_REVIEW_CD` | DOUBLE | NOT NULL |  | Code value for status of a wait list review. |
| 91 | `STATUS_REVIEW_DT_TM` | DATETIME |  |  | The date/time that a wait list status was reviewed. |
| 92 | `SUB_STATUS_CD` | DOUBLE | NOT NULL |  | The code value that identifies the sub status of a wait list row. Some examples are Waiting, Cancelled, Deferred, Removed, etc. |
| 93 | `SUPRA_SERVICE_REQUEST_CD` | DOUBLE | NOT NULL |  | The type of supra service request. |
| 94 | `TRACKING_2_BIT` | DOUBLE | NOT NULL |  | Identifies which columns are being tracked for history. |
| 95 | `TRACKING_BIT` | DOUBLE | NOT NULL |  | Identifies which columns are being tracked for history. |
| 96 | `TRANSACTION_DT_TM` | DATETIME |  |  | Date and time the transaction, which triggered the history row, occurred. This field can be system assigned or manually manipulated by users. |
| 97 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 98 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 99 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 100 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 101 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 102 | `URGENCY_CD` | DOUBLE | NOT NULL |  | Code Value for the urgency of patient event on wait list. Example: within 7 days. |
| 103 | `URGENCY_DT_TM` | DATETIME |  |  | The date/time an urgency field was declared for a wait list row. |
| 104 | `WAIT_LIST_IND` | DOUBLE |  |  | Indicator to show the conversation type. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `DIAGNOSIS_ID` | [DIAGNOSIS](DIAGNOSIS.md) | `DIAGNOSIS_ID` |
| `ENCNTR_ID` | [ENCOUNTER](ENCOUNTER.md) | `ENCNTR_ID` |
| `LOCATION_CD` | [LOCATION](LOCATION.md) | `LOCATION_CD` |
| `LOC_BED_CD` | [LOCATION](LOCATION.md) | `LOCATION_CD` |
| `LOC_BUILDING_CD` | [LOCATION](LOCATION.md) | `LOCATION_CD` |
| `LOC_FACILITY_CD` | [LOCATION](LOCATION.md) | `LOCATION_CD` |
| `LOC_NURSE_UNIT_CD` | [LOCATION](LOCATION.md) | `LOCATION_CD` |
| `LOC_ROOM_CD` | [LOCATION](LOCATION.md) | `LOCATION_CD` |
| `PERSON_ID` | [PERSON](PERSON.md) | `PERSON_ID` |
| `PM_HIST_TRACKING_ID` | [PM_HIST_TRACKING](PM_HIST_TRACKING.md) | `PM_HIST_TRACKING_ID` |
| `PM_WAIT_LIST_ID` | [PM_WAIT_LIST](PM_WAIT_LIST.md) | `PM_WAIT_LIST_ID` |
| `PROCEDURE_ID` | [PROCEDURE](PROCEDURE.md) | `PROCEDURE_ID` |

