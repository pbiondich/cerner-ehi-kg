# RAD_REPORT

> The Rad_Report table contains general information about a radiology report.

**Description:** Rad Report  
**Table type:** ACTIVITY  
**Primary key:** `RAD_REPORT_ID`  
**Columns:** 39  
**Referenced by:** 8 columns

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ADDENDUM_IND` | DOUBLE |  |  | The Addendum_Ind field indicates if this row represents an addendum to a report. |
| 2 | `BATCH_SIGN_IND` | DOUBLE |  |  | This indicator will be set to 1 if the report was signed out in batch by the radiologist. |
| 3 | `CHARGES_SENT_IND` | DOUBLE | NOT NULL |  | This column indicates if professional charges have been sent for a given radiology report. |
| 4 | `CLASSIFICATION_CD` | DOUBLE | NOT NULL |  | the Classification_Cd is used for procedure classification. |
| 5 | `DICTATED_BY_ID` | DOUBLE | NOT NULL | FK→ | The Dictated_By_Id indicates the radiologist/resident that dictated the report. |
| 6 | `DICTATED_DT_TM` | DATETIME |  |  | The Dictated_Dt_tm captures the date and time that the report was dictated. |
| 7 | `DICTATED_TZ` | DOUBLE |  |  | Time zone associated with the corresponding DT_TM column. |
| 8 | `DICTATION_SECONDS` | DOUBLE | NOT NULL |  | This field contains the length in seconds of the voice dictation associated with the Radiology report. |
| 9 | `FINAL_DT_TM` | DATETIME |  |  | The final_dt_tm contains the date and time that the report was finalized or signed out. |
| 10 | `FINAL_TZ` | DOUBLE |  |  | Time zone associated with the corresponding DT_TM column. |
| 11 | `MODIFIED_IND` | DOUBLE |  |  | The Modified_Ind indicates whether or not the canned normal report has been modified or not. |
| 12 | `NO_PROXY_IND` | DOUBLE |  |  | The No_Proxy_Ind indicates if the radiologist/resident will allow this specific case to be proxied or not. |
| 13 | `ORDER_ID` | DOUBLE | NOT NULL | FK→ | The Order_Id is a foreign key to the Order_Radiology table. It identifies the master order for the report. |
| 14 | `ORIGINAL_TRANS_DT_TM` | DATETIME |  |  | The Original_Trans_Dt_Tm captures the date and time that the report was first transcribed. |
| 15 | `ORIGINAL_TRANS_TZ` | DOUBLE |  |  | Time zone associated with the corresponding DT_TM column. |
| 16 | `PERF_LOC_CD` | DOUBLE | NOT NULL | FK→ | The location where the report was created. |
| 17 | `POSTED_FINAL_DT_TM` | DATETIME |  |  | This column contains the date/time that the report was updated to authenticated on the clinical_event table. |
| 18 | `POSTED_FINAL_TZ` | DOUBLE |  |  | Time zone associated with the corresponding DT_TM column. |
| 19 | `PREV_OWNER_ID` | DOUBLE | NOT NULL | FK→ | The Prev_Owner_Id identifies who the report was queued to last. |
| 20 | `RAD_REPORT_ID` | DOUBLE | NOT NULL | PK | The Rad_Report_Id uniquely identifies a row in the Rad_Report table. It serves no other purpose other than to uniquely identify the row. |
| 21 | `RAD_RPT_REFERENCE_NBR` | VARCHAR(40) |  |  | The Rad_Rpt_Reference_Nbr serves as a tie to the clinical event row that represents the report. |
| 22 | `REDICTATE_IND` | DOUBLE |  |  | The Re-dictate_Ind indicates if the report has been re-dictated or not. |
| 23 | `REPORTING_PRIORITY_CD` | DOUBLE | NOT NULL |  | No longer used. Moved to Order_radiology table. |
| 24 | `REPORT_CREATION_MTHD_CD` | DOUBLE | NOT NULL |  | Describes the method in which the report was originally created. |
| 25 | `REPORT_EVENT_ID` | DOUBLE | NOT NULL |  | The Report_Event_Id is a foreign key to the Clinical_Event table. It identifies the report that isstored in the repository. |
| 26 | `RES_MARKUP_QUEUE_READ_IND` | DOUBLE | NOT NULL |  | The res_markup _queue_read_ind indicates if the report is currently in the resident's final markup queue. A value of zero indicates that the report is currently in the resident's final markup queue and a value of 1 means that the report is marked as read. |
| 27 | `RES_QUEUE_IND` | DOUBLE |  |  | the Res_Queue_Ind indicates if the report is currently queued to a resident. |
| 28 | `RES_SIGN_REJECT_MARK_FLAG` | DOUBLE |  |  | The Res_Sign_Reject_Mark_Flag indicates whether or not the resident has marked the report for rejection or signout. |
| 29 | `RET_TO_RES_DT_TM` | DATETIME |  |  | This column contains the date/time that the report was returned to a resident. |
| 30 | `SCD_STORY_ID` | DOUBLE | NOT NULL | FK→ | When a report is a structured report, this is the activity data that will be contained in the report. |
| 31 | `SEQUENCE` | DOUBLE |  |  | The Sequence identifies the order that the addendums, if any, are in. |
| 32 | `SIGN_REJECT_MARK_FLAG` | DOUBLE |  |  | The Sign_Reject_Mark_Flag indicates whether or not the radiologist/cosigner has marked the report for rejection or signout. |
| 33 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 34 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 35 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 36 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 37 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |
| 38 | `VOICE_DEL_ATMT_DT_TM` | DATETIME |  |  | The field stores the first time that an attempt was made to delete the voice file. Field is null if the report is not a DD or VR report. |
| 39 | `VOICE_DEL_SUCC_DT_TM` | DATETIME |  |  | The field stores the date and time when the voice file was successfully deleted from the server. Field is null if the report is not a DD or VR report. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `DICTATED_BY_ID` | [PRSNL](PRSNL.md) | `PERSON_ID` |
| `ORDER_ID` | [ORDER_RADIOLOGY](ORDER_RADIOLOGY.md) | `ORDER_ID` |
| `PERF_LOC_CD` | [LOCATION](LOCATION.md) | `LOCATION_CD` |
| `PREV_OWNER_ID` | [PRSNL](PRSNL.md) | `PERSON_ID` |
| `SCD_STORY_ID` | [SCD_STORY](SCD_STORY.md) | `SCD_STORY_ID` |

## Referenced by (8)

| From table | Column |
|------------|--------|
| [OMF_RADREPORT_ST](OMF_RADREPORT_ST.md) | `RAD_REPORT_ID` |
| [OMF_RADTRANS_ORDER_ST](OMF_RADTRANS_ORDER_ST.md) | `RAD_REPORT_ID` |
| [RAD_OPS_EXCEPTION](RAD_OPS_EXCEPTION.md) | `RAD_REPORT_ID` |
| [RAD_PEER_REVIEW](RAD_PEER_REVIEW.md) | `RAD_REPORT_ID` |
| [RAD_REPORT_DETAIL](RAD_REPORT_DETAIL.md) | `RAD_REPORT_ID` |
| [RAD_REPORT_PRSNL](RAD_REPORT_PRSNL.md) | `RAD_REPORT_ID` |
| [RAD_RPT_PRSNL_HIST](RAD_RPT_PRSNL_HIST.md) | `RAD_REPORT_ID` |
| [RAD_TRANS_STATS](RAD_TRANS_STATS.md) | `RAD_REPORT_ID` |

