# HF_F_CLINICAL_EVENT

> This is the fact table that contain all clinical events for patients for given encounter (visit)

**Description:** HF_F_CLINICAL_EVENT  
**Table type:** REFERENCE  
**Primary key:** _(not published — see note)_  
**Columns:** 50

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ACCESSION_NBR` | VARCHAR(100) |  |  | This is the accession or order number associated with this order. Allows access to events/groups of events via Accession Number. Scope and use of Accession Number is application-specific |
| 2 | `CLINICAL_EVENT_FACT_ID` | DOUBLE | NOT NULL |  | The unique identifier for the clinical event fact row. |
| 3 | `CLINICAL_SEQ` | DOUBLE |  |  | This field describes the sequence of an event in a series. For example, 1,2,3 is one sequence or Post Op 1, Post Op2, Post Op3 could be another separate sequence. Used to indicate what sequence clinical events took place in if they're all ensured together. |
| 4 | `CLINSIG_UPDT_DT_ID` | DOUBLE |  |  | The clinically significant date key is used to join the clinical event fact table to the date dimension table. |
| 5 | `CLINSIG_UPDT_DT_TM` | DATETIME |  |  | Clinical Significant date and time |
| 6 | `CRITICAL_HIGH` | VARCHAR(20) |  |  | Critical high value |
| 7 | `CRITICAL_LOW` | VARCHAR(20) |  |  | Critical low value |
| 8 | `ENCOUNTER_ID` | DOUBLE |  |  | The visit identifier for the encounter |
| 9 | `EQUATION_TXT` | VARCHAR(2000) |  |  | This field stores the equation used to calculate the result. Ex. MAP = SAP + (DAP x 2)/3 |
| 10 | `EVENT_CLASS_ID` | DOUBLE |  |  | Coded value which specifies how the event is stored in and retrieved from the event table's sub-tables. For example, Event_Class_CDs identify events as numeric results, textual results, calculations, medications, etc. |
| 11 | `EVENT_CODE_ID` | DOUBLE |  |  | It is the code that identifies the most basic unit of the storage, i.e. RBC, discharge summary, image |
| 12 | `EVENT_END_DT_ID` | DOUBLE |  |  | The event end date key used to join the clinical event fact table to the date dimension table. |
| 13 | `EVENT_END_DT_TM` | DATETIME |  |  | Clinical date time for the end of the event. In the cases where results do not associate an Event Time range, then the event_start_dt_tm = event_end_dt_tm |
| 14 | `EVENT_EXPIRATION_DT_ID` | DOUBLE |  |  | The event expiration date key used to join the clinical event fact table to the date dimension table. |
| 15 | `EVENT_EXPIRATION_DT_TM` | DATETIME |  |  | The date on which the result no longer becomes clinically relevant. Indicates when a result can no longer be used to make clinical decisions. The result still has historical significance, but cannot be used to make decisions on the administration of care. Example: A blood bank cross match is only valid for 24-48 hours. If after that time they need a cross-match, they must do another one. |
| 16 | `EVENT_NK` | VARCHAR(100) |  |  | The source event system identifier. This is used to link multiple clinical events through the parent_event_nk. |
| 17 | `EVENT_NOMRALCY_ID` | DOUBLE |  |  | States whether the result is normal. This can be used to determine whether to display the event tag in different color on the flowsheet. For group results, this represents an ""overall"" normalcy. i.e. Is any result in the group abnormal? |
| 18 | `EVENT_NORMALCY_METHOD_ID` | DOUBLE |  |  | The method used to interpret normalcy |
| 19 | `EVENT_RELTN_ID` | DOUBLE |  |  | To indicate whether this event is a parent event of another event or a child event of another event or an orphan event where it is not parent or child of another event |
| 20 | `EVENT_SOURCE_ID` | DOUBLE |  |  | Source from which this result value originated. For example the source can be father or mother or calculated |
| 21 | `EVENT_START_DT_ID` | DOUBLE |  |  | The event start date key used to join the clinical event fact table to the date dimension table. |
| 22 | `EVENT_START_DT_TM` | DATETIME |  |  | The Clinical date and time for the start of this event |
| 23 | `HOSPITAL_ID` | DOUBLE |  |  | The dim table key for the hospital that this record's encounter is attached to |
| 24 | `LAB_PROCEDURE_ID` | DOUBLE |  |  | The unique identifier for the orderable within the Cerner Health Facts Data Warehouse |
| 25 | `NORMAL_HIGH` | VARCHAR(20) |  |  | Normal high value |
| 26 | `NORMAL_LOW` | VARCHAR(20) |  |  | Normal low value |
| 27 | `PARENT_EVENT_NK` | VARCHAR(100) |  |  | The source event system identifier. This is used to link multiple clinical events through the event_nk. |
| 28 | `PARTITION_DT_TM` | DATETIME |  |  | Indicates which partition of the table this record is in. Matches the partition date/time of the parent encounter |
| 29 | `PATIENT_ID` | DOUBLE |  |  | The patient unique identifier used within the Cerner Health Facts Data Warehouse. |
| 30 | `PERFORMED_DT_ID` | DOUBLE |  |  | The performed date key used to join the clinical event fact table to the date dimension table. |
| 31 | `PERFORMED_DT_TM` | DATETIME |  |  | The date and time when this event was performed |
| 32 | `PERFORMED_PRSNL_ID` | DOUBLE |  |  | The personnel who performed this result |
| 33 | `REFERENCE_NBR` | VARCHAR(100) |  |  | The combination of the reference nbr and the contributor system code provides a unique identifier to the origin of the data. |
| 34 | `RESULT_FEASIBLE_IND` | DOUBLE |  |  | Indicates whether or not the result is within feasible limits. |
| 35 | `RESULT_INACCURATE_IND` | DOUBLE |  |  | Indicate whether the result value is outside of the measuring instruments accurate limits. |
| 36 | `RESULT_NORMALCY_FLG` | DOUBLE |  |  | Indicates Whether A Areult Is Abnormal Or Not. A Value Of: 2 Indicates An Abnormal Result; 1 Indicates A Normal Result 0 - indicates undefined or unknown -1 - N/A |
| 37 | `RESULT_TIME_UNIT_ID` | DOUBLE |  |  | If the result refers to a rate, this field is the time component of the rate |
| 38 | `RESULT_UNITS_ID` | DOUBLE |  |  | The unit of measure of the event / result |
| 39 | `RESULT_VALUE` | VARCHAR(255) |  |  | The value of the result |
| 40 | `RESULT_VALUE_DT_ID` | DOUBLE |  |  | The result date key used to join the clinical event fact table to the date dimension table. |
| 41 | `RESULT_VALUE_DT_TM` | DATETIME |  |  | The actual date and time result value |
| 42 | `RESULT_VALUE_NUM` | DOUBLE |  |  | The actual numeric result |
| 43 | `RESULT_VALUE_TXT` | VARCHAR(255) |  |  | The actual result value in text |
| 44 | `SECTION_ID` | DOUBLE |  |  | The section where the event is performed. e.g. For Microbiology event, the bench will be stored here. |
| 45 | `UPDT_DT_TM` | DATETIME |  |  | The date and time the row was last inserted or updated. |
| 46 | `UPDT_TASK` | VARCHAR(40) |  |  | The registered (assigned) task number for the process that inserted or updated the row. |
| 47 | `UPDT_USER` | VARCHAR(40) |  |  | The user who last modified this record |
| 48 | `VERIFIED_DT_ID` | DOUBLE |  |  | The verified date key used to join the clinical event fact table to the date dimension table. |
| 49 | `VERIFIED_DT_TM` | DATETIME |  |  | Date and time this result / event is verified |
| 50 | `VERIFIED_PRSNL_ID` | DOUBLE |  |  | The personnel who verified this result / event |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

