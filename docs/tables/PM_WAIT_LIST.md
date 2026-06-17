# PM_WAIT_LIST

> Person Mgmt: Wait list information

**Description:** Person Mgmt Wait list table.  
**Table type:** ACTIVITY  
**Primary key:** `PM_WAIT_LIST_ID`  
**Columns:** 101  
**Referenced by:** 2 columns

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ACTIVE_IND` | DOUBLE |  |  | The table row is active or inactive. A row is generally active unless it is in an inactive state such as logically deleted, combined away, pending purge, etc. |
| 2 | `ACTIVE_STATUS_CD` | DOUBLE | NOT NULL |  | Indicates the status of the row itself (not the data in the row) such as active, inactive, combined away, pending purge, etc. |
| 3 | `ACTIVE_STATUS_DT_TM` | DATETIME |  |  | The date and time that the active_status_cd was set. |
| 4 | `ACTIVE_STATUS_PRSNL_ID` | DOUBLE | NOT NULL |  | The person who caused the active_status_cd to be set or change. |
| 5 | `ADJ_WAITING_START_DT_TM` | DATETIME |  |  | The current adjusted waiting start date and time for an encounter. |
| 6 | `ADMIT_BOOKING_CD` | DOUBLE | NOT NULL |  | The admission booking type. Examples are full booking, partial booking, etc. |
| 7 | `ADMIT_CATEGORY_CD` | DOUBLE | NOT NULL |  | Admission or administrative category of the wait list. An example would be 'private'. or 'NHS'. |
| 8 | `ADMIT_DECISION_DT_TM` | DATETIME |  |  | Date and time the decision to admit was made |
| 9 | `ADMIT_GUARANTEED_DT_TM` | DATETIME |  |  | The guaranteed admission date and time. |
| 10 | `ADMIT_OFFER_OUTCOME_CD` | DOUBLE | NOT NULL |  | Outcome of waiting list admission (ex. patient admitted and treated, patient admitted and suspended, Another appointment given). |
| 11 | `ADMIT_TYPE_CD` | DOUBLE | NOT NULL |  | Type of waiting list admission. (ex. Day case, inpatient) |
| 12 | `ANESTHETIC_CD` | DOUBLE | NOT NULL |  | Waiting list anesthetic code (ex. Local anesthetic, epidural) |
| 13 | `APPOINTMENT_CD` | DOUBLE | NOT NULL |  | Did the patient have an appointment. |
| 14 | `APPT_LOCATION_CD` | DOUBLE | NOT NULL |  | Location where appointment is scheduled to |
| 15 | `APPT_SYNONYM_CD` | DOUBLE | NOT NULL |  | Synonym used to schedule appointment. What the appointment is for. |
| 16 | `APPT_TYPE_CD` | DOUBLE | NOT NULL |  | What the appointment is for. Examples are 'MRI Knee', 'Ortho Consult', etc. |
| 17 | `ATTENDANCE_CD` | DOUBLE | NOT NULL |  | Attendance record of the appontment. Such as 'on time', 'arrived late', etc. |
| 18 | `ATTENDDOC_CLINICAL_SERVICE_CD` | DOUBLE | NOT NULL |  | Attending physician's default clinical service code. |
| 19 | `AUTO_BLOOD_IND` | DOUBLE |  |  | Indicate if the current encounter has autologous blood donation. |
| 20 | `BEG_EFFECTIVE_DT_TM` | DATETIME | NOT NULL |  | The date and time for which this table row becomes effective. Normally, this will be the date and time the row is added, but could be a past or future date and time. |
| 21 | `CANCER_REFERRAL_CD` | DOUBLE | NOT NULL |  | The Cancer Referral Code describes whether the referral is a cancer referral. |
| 22 | `CHG_DT_TM` | DATETIME |  |  | Date and time change was made. |
| 23 | `CHG_ID` | DOUBLE | NOT NULL |  | ID of person who made change. |
| 24 | `COMMENT_LONG_TEXT_ID` | DOUBLE | NOT NULL |  | Waiting list comments |
| 25 | `COMMISSIONER_REFERENCE` | VARCHAR(50) |  |  | Commissioner reference identifier. |
| 26 | `CONTRACT_STATUS_CD` | DOUBLE | NOT NULL |  | Codified field indicating status of a care contract. |
| 27 | `DECLINE_STATUS_CD` | DOUBLE | NOT NULL |  | Field contains a code value that contains a textual reason for a decline. |
| 28 | `DECLINE_STATUS_DT_TM` | DATETIME |  |  | Date and Time Decline Status was set. |
| 29 | `DELAY_STATUS_CD` | DOUBLE | NOT NULL |  | Field that contains a code that refers to a text description of the reason a delay status occurred. |
| 30 | `DELAY_STATUS_DT_TM` | DATETIME |  |  | Date/Time that a delay status was set. |
| 31 | `ENCNTR_ID` | DOUBLE | NOT NULL | FK→ | This is the value of the unique primary identifier of the encounter table. It is an internal system assigned number. |
| 32 | `END_EFFECTIVE_DT_TM` | DATETIME | NOT NULL |  | The date/time after which the row is no longer valid as active current data. This may be valued with the date that the row became inactive. |
| 33 | `EST_ADMIT_DT_TM` | DATETIME |  |  | Estimated Date/Time that a person on the wait list will be admitted. |
| 34 | `EST_LENGTH_PROCEDURE_CD` | DOUBLE | NOT NULL |  | Field that contains a code the refers to a length of time. For example, 10 Mins, 15 Mins, etc. |
| 35 | `FINANCIAL_CLASS_CD` | DOUBLE | NOT NULL |  | The financial classification used for a given encounter. Examples may include Worker's Comp, Self Pay, etc. |
| 36 | `FINANCIAL_CLASS_EFF_DT_TM` | DATETIME |  |  | The date/time that a financial class becomes effective. |
| 37 | `FROM_ED_IND` | DOUBLE | NOT NULL |  | Indicates whether this encounter was transferred from the emergency department. |
| 38 | `FUNCTIONAL_DEFICIENCY_CAUSE_CD` | DOUBLE | NOT NULL |  | The primary presenting cause of functional deficiency. |
| 39 | `FUNCTIONAL_DEFICIENCY_CD` | DOUBLE | NOT NULL |  | Function to be restored, by reference to the affected part of the body, which is the subject of the particular wait list record. |
| 40 | `LAST_DNA_DT_TM` | DATETIME |  |  | Last date and time a DNA was recorded for a waiting list entry |
| 41 | `LOCATION_CD` | DOUBLE | NOT NULL | FK→ | The field contains a code that identifies the current permanent location of the patient. |
| 42 | `LOC_BED_CD` | DOUBLE | NOT NULL | FK→ | This field is the code value for a current patient location with a location type of bed. |
| 43 | `LOC_BUILDING_CD` | DOUBLE | NOT NULL | FK→ | This field is the code value for the current patient location with a location type of building. |
| 44 | `LOC_FACILITY_CD` | DOUBLE | NOT NULL | FK→ | This field is the code value for the current patient location with a location type of facility. |
| 45 | `LOC_NURSE_UNIT_CD` | DOUBLE | NOT NULL | FK→ | This field is the code value for the current patient location with a location type of Nurse Unit. |
| 46 | `LOC_ROOM_CD` | DOUBLE | NOT NULL | FK→ | This field is the code value for the current patient location with a location type of Room. |
| 47 | `MANAGEMENT_CD` | DOUBLE | NOT NULL |  | The wait list management code. Some examples are 'No overnight stay required', 'Panned admission - With overnight'. |
| 48 | `NCEPOD_CD` | DOUBLE | NOT NULL |  | The NCEPOD (National Confidential Enquiry into Patient Outcome and Death) Classification categorizes the urgency of the patient's intervention. |
| 49 | `OPERATION_CD` | DOUBLE | NOT NULL |  | Waiting list operation code (ex. One or more operative procedure carried out, . no operative procedures performed or intended) |
| 50 | `ORIG_REQUEST_RECEIVED_DT_TM` | DATETIME |  |  | Original date and time that the wait list request was received. |
| 51 | `OTHER_MED_CONDITION` | VARCHAR(40) |  |  | Text description of a medical condition. |
| 52 | `PEND_ACCEPTANCE_DT_TM` | DATETIME |  |  | The date and time of the pending acceptance. |
| 53 | `PEND_NOTIFICATION_DT_TM` | DATETIME |  |  | The date and time of the pending notification. |
| 54 | `PEND_PLACE_PRIORITY_CD` | DOUBLE | NOT NULL |  | The level of importance in bed assignment activity in relation to other encounters. |
| 55 | `PEND_PLACE_PRIORITY_DT_TM` | DATETIME |  |  | The level date and time when the pending location placement priority was set. |
| 56 | `PERSON_ID` | DOUBLE | NOT NULL | FK→ | This is the value of the unique primary identifier of the person table. It is an internal system assigned number. |
| 57 | `PLANNED_ADMIT_DT_TM` | DATETIME |  |  | The date/time a patient is planned to be admitted. |
| 58 | `PLANNED_OPERATION_CD` | DOUBLE | NOT NULL |  | A field containing a code value that represents a planned operation. |
| 59 | `PLANNED_PROCEDURE_CD` | DOUBLE | NOT NULL |  | The code value for the planned Procedure for this wait list row. |
| 60 | `PLANNED_PROCEDURE_DT_TM` | DATETIME |  |  | The date/time the procedure is planned to occur. |
| 61 | `PM_WAIT_LIST_ID` | DOUBLE | NOT NULL | PK | This is the unique identifier for a wait list row. |
| 62 | `PREV_PROV_ADMIT_DT_TM` | DATETIME |  |  | The date and time of the admission of the previous provider. |
| 63 | `PRE_ADMIT_ATTEND_IND` | DOUBLE |  |  | Indicates whether the attending physician performed the pre admit. |
| 64 | `PRE_ADMIT_CLIN_APPT_DT_TM` | DATETIME |  |  | Date/Time an appointment was set before admit. |
| 65 | `PROVISIONAL_ADMIT_DT_TM` | DATETIME |  |  | Date/Time the provisional admit was made. |
| 66 | `REASON_FOR_CHANGE_CD` | DOUBLE | NOT NULL |  | Code value for a text description of the reason a change was made. |
| 67 | `REASON_FOR_REMOVAL` | VARCHAR(255) |  |  | A text description of the reason a removal was made. |
| 68 | `REASON_FOR_REMOVAL_CD` | DOUBLE | NOT NULL |  | Code value for a text description of the reason a removal was made. |
| 69 | `RECOMMEND_DT_TM` | DATETIME |  |  | The date/time that removal,etc. was recommended. |
| 70 | `REFERRAL_DT_TM` | DATETIME |  |  | The date and time of the referral. |
| 71 | `REFERRAL_REASON_CD` | DOUBLE | NOT NULL |  | The resaon for the referral. |
| 72 | `REFERRAL_SOURCE_CD` | DOUBLE | NOT NULL |  | The source of the referral. |
| 73 | `REFERRAL_TYPE_CD` | DOUBLE | NOT NULL |  | The type of referral. |
| 74 | `REMOVAL_DT_TM` | DATETIME |  |  | Date/Time that a person was removed from the wait list. |
| 75 | `REQUESTED_DT_TM` | DATETIME |  |  | Represent requested date/time if waitlist encounter in requested state |
| 76 | `REQUESTED_LOCATION_CD` | DOUBLE | NOT NULL |  | Code value representing the location a patient on the wait list requested to be moved to. |
| 77 | `RESCHD_APPT_BY_DT_TM` | DATETIME |  |  | The guaranteed date that the appoinment will be rescheduled by. |
| 78 | `RESOURCE_CD` | DOUBLE | NOT NULL |  | Primary resource the appointment was scheduled with. |
| 79 | `SCHEDULE_DT_TM` | DATETIME |  |  | Represents scheduled date/time if event is scheduled. |
| 80 | `SCH_EVENT_ID` | DOUBLE | NOT NULL | FK→ | Link wait list encounter to scheduling event (appt) |
| 81 | `SERVICE_TYPE_REQUESTED_CD` | DOUBLE | NOT NULL |  | The service type requested. |
| 82 | `STAND_BY_CD` | DOUBLE | NOT NULL |  | Code Value that contains a text description of a wait list stand by. |
| 83 | `STATUS_CD` | DOUBLE | NOT NULL |  | Code value that refers to the status of a wait list row. Examples: Normal, Deferred. |
| 84 | `STATUS_DETAIL_CD` | DOUBLE | NOT NULL |  | This code value represents further detail on the main wait list status. |
| 85 | `STATUS_DT_TM` | DATETIME |  |  | The date/time a status was set. |
| 86 | `STATUS_END_DT_TM` | DATETIME |  |  | The end date and time of the status. |
| 87 | `STATUS_REVIEW_CD` | DOUBLE | NOT NULL |  | Code value for status of a wait list review. |
| 88 | `STATUS_REVIEW_DT_TM` | DATETIME |  |  | The date/time that a wait list status was reviewed. |
| 89 | `SUB_STATUS_CD` | DOUBLE | NOT NULL |  | The code value that identifies the sub status of a wait list row. Some examples are Waiting, Cancelled, Deferred, Removed, etc. |
| 90 | `SUPRA_SERVICE_REQUEST_CD` | DOUBLE | NOT NULL |  | The type of supra service request. |
| 91 | `SUSPENDED_DAYS` | DOUBLE | NOT NULL |  | Total number of days suspended. |
| 92 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 93 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 94 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 95 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 96 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |
| 97 | `URGENCY_CD` | DOUBLE | NOT NULL |  | Code Value for the urgency of patient event on wait list. Example: within 7 days. |
| 98 | `URGENCY_DT_TM` | DATETIME |  |  | The date/time an urgency field was declared for a wait list row. |
| 99 | `WAITING_END_DT_TM` | DATETIME |  |  | The current actual waiting end date and time for an encounter. |
| 100 | `WAITING_START_DT_TM` | DATETIME |  |  | The current actual waiting start date and time for an encounter. |
| 101 | `WAIT_LIST_IND` | DOUBLE |  |  | Indicator to show the conversation type. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `ENCNTR_ID` | [ENCOUNTER](ENCOUNTER.md) | `ENCNTR_ID` |
| `LOCATION_CD` | [LOCATION](LOCATION.md) | `LOCATION_CD` |
| `LOC_BED_CD` | [LOCATION](LOCATION.md) | `LOCATION_CD` |
| `LOC_BUILDING_CD` | [LOCATION](LOCATION.md) | `LOCATION_CD` |
| `LOC_FACILITY_CD` | [LOCATION](LOCATION.md) | `LOCATION_CD` |
| `LOC_NURSE_UNIT_CD` | [LOCATION](LOCATION.md) | `LOCATION_CD` |
| `LOC_ROOM_CD` | [LOCATION](LOCATION.md) | `LOCATION_CD` |
| `PERSON_ID` | [PERSON](PERSON.md) | `PERSON_ID` |
| `SCH_EVENT_ID` | [SCH_EVENT](SCH_EVENT.md) | `SCH_EVENT_ID` |

## Referenced by (2)

| From table | Column |
|------------|--------|
| [PM_WAIT_LIST_HIST](PM_WAIT_LIST_HIST.md) | `PM_WAIT_LIST_ID` |
| [PM_WAIT_LIST_STATUS](PM_WAIT_LIST_STATUS.md) | `PM_WAIT_LIST_ID` |

