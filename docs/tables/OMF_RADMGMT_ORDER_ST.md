# OMF_RADMGMT_ORDER_ST

> The main summary table for radiology management.

**Description:** OMF RADMGMT ORDER ST  
**Table type:** ACTIVITY  
**Primary key:** _(not published — see note)_  
**Columns:** 103

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ACCESSION_NBR` | VARCHAR(50) |  |  | The accession number for the order. |
| 2 | `ACT_DICTATE_TRANS` | DOUBLE |  |  | The actual turnaround time from dictate to transcribe. |
| 3 | `ACT_EX_COMP_VIEW` | DOUBLE |  |  | The actual turnaround time from exam complete to view. |
| 4 | `ACT_ORDER_SCHED_CONFIRM` | DOUBLE |  |  | Actual turn around time from order to scheduled confirmed status |
| 5 | `ACT_ORD_START` | DOUBLE |  |  | The actual turnaround time from order to start. |
| 6 | `ACT_OVERALL_TAT` | DOUBLE |  |  | The actual overall turnaround time. |
| 7 | `ACT_REQUEST_START` | DOUBLE |  |  | Actual turnaround time from Request to Start status. |
| 8 | `ACT_SCHED_CONFIRM_REQUEST` | DOUBLE |  |  | Expected Turnaround Time from scheduled confirmed to Request status. |
| 9 | `ACT_START_EX_COMP` | DOUBLE |  |  | Actual turnaround time from start to exam complete. |
| 10 | `ACT_TRANS_FINAL` | DOUBLE |  |  | Actual turnaround time from transcribed to signout. |
| 11 | `ACT_VIEW_DICTATE` | DOUBLE |  |  | Actual turnaround time from view to dictate. |
| 12 | `BED_AT_EXAM_CMPLT_CD` | DOUBLE | NOT NULL | FK→ | Stores the bed the patient was in at the time the exam was completed. |
| 13 | `CANCEL_BY_ID` | DOUBLE | NOT NULL | FK→ | Personnel that cancelled the exam. |
| 14 | `CANCEL_DT_NBR` | DOUBLE | NOT NULL |  | Canceled date number used for calculation of other date related dimensions and filters. |
| 15 | `CANCEL_DT_TM` | DATETIME |  |  | Date the procedure was cancelled. |
| 16 | `CANCEL_MIN_NBR` | DOUBLE | NOT NULL |  | Canceled minute number used for calculation of other time related dimensions and filters. |
| 17 | `CANCEL_REASON_CD` | DOUBLE | NOT NULL |  | Reason the order was cancelled. |
| 18 | `CANCEL_TZ` | DOUBLE | NOT NULL |  | Time Zone associated with the corresponding CANCEL_DT_TM. |
| 19 | `CATALOG_CD` | DOUBLE | NOT NULL |  | The catalog code for the order. |
| 20 | `DICTATE_DT_NBR` | DOUBLE |  |  | Dictate Date Number used to create date related dimensions and filters |
| 21 | `DICTATE_DT_TM` | DATETIME |  |  | The dictate date/time for the order. |
| 22 | `DICTATE_MIN_NBR` | DOUBLE |  |  | Dictate Minute number used to create time related dimensions and filters |
| 23 | `DICTATE_TZ` | DOUBLE |  |  | Time zone associated with the corresponding DT_TM column. |
| 24 | `ENCNTR_ID` | DOUBLE | NOT NULL | FK→ | This is the value of the unique primary identifier of the encounter table. It is an internal system assigned number. |
| 25 | `ENCNTR_TYPE_AT_EXAM_CMPLT_CD` | DOUBLE | NOT NULL |  | Stores the patient's encounter type at exam completion. |
| 26 | `ENCNTR_TYPE_CD` | DOUBLE | NOT NULL |  | The encounter type code for the order. |
| 27 | `EXAM_COMPLETE_DAY` | DOUBLE |  |  | The day of week that the exam was completed. |
| 28 | `EXAM_COMPLETE_DT_NBR` | DOUBLE |  |  | Exam complete date number used for calculation of other date related dimensions and filters |
| 29 | `EXAM_COMPLETE_DT_TM` | DATETIME |  |  | The date/time that the exam was completed. |
| 30 | `EXAM_COMPLETE_HOUR` | DOUBLE |  |  | The hour of day that the exam was completed. |
| 31 | `EXAM_COMPLETE_MIN_NBR` | DOUBLE |  |  | Exam Complete minute number used for the calculation of other time related dimensions and filters |
| 32 | `EXAM_COMPLETE_MONTH` | VARCHAR(10) |  |  | The month of year that the exam was completed. |
| 33 | `EXAM_COMPLETE_QTY` | DOUBLE |  |  | The quantity that has been completed. |
| 34 | `EXAM_COMPLETE_TZ` | DOUBLE |  |  | Time zone associated with the corresponding DT_TM column. |
| 35 | `EXAM_COMP_CREDIT_QTY` | DOUBLE |  |  | Determines if applying a credit to the order from AFC or charge services or if being called from radremove then it's set to 1 otherwise 0. |
| 36 | `EXAM_ROOM_CD` | DOUBLE | NOT NULL |  | The service resource code for the exam room. |
| 37 | `EXP_DICTATE_TRANS` | DOUBLE |  |  | The expected turnaround time from dictate to transcribe. |
| 38 | `EXP_EX_COMP_VIEW` | DOUBLE |  |  | The expected exam complete to view turnaround time. |
| 39 | `EXP_ORDER_SCHED_CONFIRM` | DOUBLE |  |  | Expected turnaround time from Order to scheduled confirmed status. |
| 40 | `EXP_ORD_START` | DOUBLE |  |  | Expected ordered to start turnaround time. |
| 41 | `EXP_OVERALL_TAT` | DOUBLE |  |  | Expected overall turnaround time. |
| 42 | `EXP_REQUEST_START` | DOUBLE |  |  | Expected turnaround time from Request to Start status. |
| 43 | `EXP_SCHED_CONFIRM_REQUEST` | DOUBLE |  |  | Expected turnaround time from scheduled confirmed to Request status. |
| 44 | `EXP_START_EX_COMP` | DOUBLE |  |  | Expected start to exam complete turnaround time. |
| 45 | `EXP_TRANS_FINAL` | DOUBLE |  |  | Expected transcribe to signout turnaround time. |
| 46 | `EXP_VIEW_DICTATE` | DOUBLE |  |  | Expected view to dictate turnaround time. |
| 47 | `FINAL_DT_NBR` | DOUBLE |  |  | Final Date Number used for the calculation of other date related dimensions and filters |
| 48 | `FINAL_DT_TM` | DATETIME |  |  | The date/time that the case signout took place. |
| 49 | `FINAL_MIN_NBR` | DOUBLE |  |  | Final minute number used to calculate other time related dimensions and filters |
| 50 | `FINAL_TZ` | DOUBLE |  |  | Time zone associated with the corresponding DT_TM column. |
| 51 | `LOC_AT_EXAM_CMPLT_CD` | DOUBLE | NOT NULL | FK→ | Stores the patient's location at exam completion. |
| 52 | `NBR_REPORTS` | DOUBLE |  |  | The number of reports completed for this order (1 per order). |
| 53 | `ORDER_DT_NBR` | DOUBLE |  |  | Order Date Number used to calculate other date related dimensions and filters |
| 54 | `ORDER_DT_TM` | DATETIME |  |  | The date/time that the order took place. |
| 55 | `ORDER_ID` | DOUBLE | NOT NULL | FK→ | The unique identification number for the order. |
| 56 | `ORDER_MIN_NBR` | DOUBLE |  |  | Order minute number used to calculate time related dimensions and filters |
| 57 | `ORDER_PHYS_ID` | DOUBLE | NOT NULL | FK→ | The unique identification number for the ordering physician. |
| 58 | `ORDER_PRSNL_ID` | DOUBLE | NOT NULL | FK→ | Stores the personnel that ordered the procedure. |
| 59 | `ORDER_TZ` | DOUBLE |  |  | Time zone associated with the corresponding DT_TM column. |
| 60 | `PATIENT_ID` | DOUBLE | NOT NULL | FK→ | The identification number of the patient for which the order took place. |
| 61 | `PERF_DEPT_CD` | DOUBLE | NOT NULL |  | The performing department in which the order took place. |
| 62 | `PERF_INST_CD` | DOUBLE | NOT NULL |  | The performing institution in which the order took place. |
| 63 | `PRECOMPLETE_CANCEL_IND` | DOUBLE | NOT NULL |  | Indicates the order was cancelled prior to exam completion. |
| 64 | `PRIORITY_CD` | DOUBLE | NOT NULL |  | The Radnet priority for the order. |
| 65 | `PROCEDURE_TYPE_FLAG` | DOUBLE |  |  | This column indicates if the entry represents an Exam Only procedure, a Read Only procedure or a regular procedure. |
| 66 | `RADIOLOGIST_ID` | DOUBLE | NOT NULL | FK→ | The radiologist associated with this case. |
| 67 | `RAD_REPORT_ID` | DOUBLE | NOT NULL |  | The Radnet report identification number associated with this order. |
| 68 | `REQUEST_DT_NBR` | DOUBLE |  |  | Requested date number of order used to calculate other date related dimensions and filters. |
| 69 | `REQUEST_DT_TM` | DATETIME |  |  | Requested date and time of a order. |
| 70 | `REQUEST_MIN_NBR` | DOUBLE |  |  | Requested minute number used to calculate other time related dimensions and filters. |
| 71 | `REQUEST_TZ` | DOUBLE |  |  | Time zone associated with the requested DT_TM column. |
| 72 | `ROOM_AT_EXAM_CMPLT_CD` | DOUBLE | NOT NULL | FK→ | Stores the room the patient was in at the time the exam was completed. |
| 73 | `RULE_ID` | DOUBLE | NOT NULL |  | The identification number of the rule for which this order qualified. |
| 74 | `SCHED_CONFIRM_DT_NBR` | DOUBLE |  |  | Confirmed Date Number of order used to calculate other date related dimensions and filters. |
| 75 | `SCHED_CONFIRM_DT_TM` | DATETIME |  |  | Confirmed date and time of a order. |
| 76 | `SCHED_CONFIRM_MIN_NBR` | DOUBLE |  |  | Confirmed minute number used to calculate other time related dimensions and filters. |
| 77 | `SCHED_CONFIRM_TZ` | DOUBLE |  |  | Time zone associated with the scheduled and confirmed DT_TM column. |
| 78 | `SCHED_DT_NBR` | DOUBLE | NOT NULL |  | Scheduled date number used for calculation of other date related dimensions and filters. |
| 79 | `SCHED_DT_TM` | DATETIME |  |  | Date the procedure was scheduled. |
| 80 | `SCHED_MIN_NBR` | DOUBLE | NOT NULL |  | Scheduled minute number used for calculation of other time related dimensions and filters. |
| 81 | `SCHED_TZ` | DOUBLE |  |  | Time zone associated with the sched_dt_tm field. |
| 82 | `SECTION_CD` | DOUBLE | NOT NULL |  | The section in which the order was performed. |
| 83 | `START_DT_NBR` | DOUBLE |  |  | Start Date Number used to calculate other date related dimensions and filters |
| 84 | `START_DT_TM` | DATETIME |  |  | The date/time in which the order was started. |
| 85 | `START_MIN_NBR` | DOUBLE |  |  | Start minute number used to calculate other time related dimensions and filters |
| 86 | `START_TZ` | DOUBLE |  |  | Time zone associated with the corresponding DT_TM column. |
| 87 | `SUBSECTION_CD` | DOUBLE | NOT NULL |  | The subsection in which the order was performed. |
| 88 | `TAT_QUAL_IND` | DOUBLE |  |  | Did this record qualify for a rule. |
| 89 | `TRANSCRIBE_DT_NBR` | DOUBLE |  |  | Transcribe Date number used to calculate date related dimensions and filters |
| 90 | `TRANSCRIBE_DT_TM` | DATETIME |  |  | The date/time in which the order was transcribed. |
| 91 | `TRANSCRIBE_MIN_NBR` | DOUBLE |  |  | Transcribe minute number used to create time related dimensions and filters |
| 92 | `TRANSCRIBE_TZ` | DOUBLE |  |  | Time zone associated with the corresponding DT_TM column. |
| 93 | `TRANSCRIPTIONIST_ID` | DOUBLE | NOT NULL | FK→ | The identification number of the transcriptionist. |
| 94 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 95 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 96 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 97 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 98 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |
| 99 | `VETTING_DT_NBR` | DOUBLE | NOT NULL |  | Vetting date number used for calculation of other date related dimensions and filters. |
| 100 | `VETTING_DT_TM` | DATETIME |  |  | Date the procedure was vetted. |
| 101 | `VETTING_MIN_NBR` | DOUBLE | NOT NULL |  | Vetting minute number used for calculation of other time related dimensions and filters. |
| 102 | `VETTING_TZ` | DOUBLE |  |  | Time zone associated with the vetting_dt_tm field. |
| 103 | `VIEW_DT_TM` | DATETIME |  |  | The date/time in which the xrays were viewed. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `BED_AT_EXAM_CMPLT_CD` | [LOCATION](LOCATION.md) | `LOCATION_CD` |
| `CANCEL_BY_ID` | [PRSNL](PRSNL.md) | `PERSON_ID` |
| `ENCNTR_ID` | [ENCOUNTER](ENCOUNTER.md) | `ENCNTR_ID` |
| `LOC_AT_EXAM_CMPLT_CD` | [LOCATION](LOCATION.md) | `LOCATION_CD` |
| `ORDER_ID` | [ORDERS](ORDERS.md) | `ORDER_ID` |
| `ORDER_PHYS_ID` | [PRSNL](PRSNL.md) | `PERSON_ID` |
| `ORDER_PRSNL_ID` | [PRSNL](PRSNL.md) | `PERSON_ID` |
| `PATIENT_ID` | [PERSON](PERSON.md) | `PERSON_ID` |
| `RADIOLOGIST_ID` | [PRSNL](PRSNL.md) | `PERSON_ID` |
| `ROOM_AT_EXAM_CMPLT_CD` | [LOCATION](LOCATION.md) | `LOCATION_CD` |
| `TRANSCRIPTIONIST_ID` | [PRSNL](PRSNL.md) | `PERSON_ID` |

