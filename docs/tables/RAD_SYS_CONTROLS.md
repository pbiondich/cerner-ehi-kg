# RAD_SYS_CONTROLS

> The Rad_Sys_Controls table contains system level settings for applications throughout RadNet.

**Description:** Rad System Controls  
**Table type:** REFERENCE  
**Primary key:** _(not published — see note)_  
**Columns:** 62

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ACC_LINK_IND` | DOUBLE |  |  | The Acc_Link_Ind indicates if accessio linking is to be used at this site. |
| 2 | `ADDENDUM_POS_FLAG` | DOUBLE |  |  | The Addendum_Pos_Flag indicates whether the Addendum is displayed below (0) or above (1) the report when the user is adding a new addendum/correction-addendum in RadTranscription. 0 is the default. |
| 3 | `ALLOW_CORRECTIONS_IND` | DOUBLE |  |  | The Allow_Corrections_Ind indicates if corrections are allowed to a signed report, or if addendums must be used for this purpose. |
| 4 | `ASSIGN_PRSNL_ROLE_FLAG` | DOUBLE | NOT NULL |  | Determines if the user is required to enter a role when starting or completing exams. |
| 5 | `ASSIGN_TO_READ_FLAG` | DOUBLE | NOT NULL |  | Determines if the user is required to enter an assigned to personnel at exam complete. |
| 6 | `AUTO_ACCEPT_REPLACE_ADDON_IND` | DOUBLE | NOT NULL |  | Indicates whether exam has to be automatically accepted when replace and add-on is performed. Yes = 0, No = 1. |
| 7 | `AUTO_GROUP_VETTBL_ORDER_IND` | DOUBLE | NOT NULL |  | Indicates whether automatic grouping of vettable orders is applicable. No = 0, Yes = 1. |
| 8 | `BATCH_SIGNOUT_IND` | DOUBLE |  |  | Indicates whether batch signout is used. |
| 9 | `BIRADS_EDITION_CHANGE_DT_TM` | DATETIME |  |  | The date/time the new version of the BIRADS system was implemented. The edition number is stored in BIRADS_EDITION_NBR. |
| 10 | `BIRADS_EDITION_NBR` | DOUBLE |  |  | This column represents the latest ACR BI-RADS edition number that the system will be running on for new radiology mammography studies. |
| 11 | `CE_CHUNK_SIZE` | DOUBLE | NOT NULL |  | This field determines the maximum number of reports that will be queried for at a time from the clinical event server. It is used by rad report search. |
| 12 | `CHARACTERS_PER_LINE` | DOUBLE |  |  | Contains the value that will be used in calculating transcription statistics. |
| 13 | `COPY_ACCSN_TO_ORD_FLAG` | DOUBLE | NOT NULL |  | Determines if the user has the option to copy the accession of the old order to the new order during a replace. |
| 14 | `COSIGN_IND` | DOUBLE |  |  | The Cosign_Ind indicates if cosigners are used at this location. |
| 15 | `DEFAULT_EXAM_PRSNL_IND` | DOUBLE | NOT NULL |  | Indicates if the logged in user needs to be automatically added to the personnel list. |
| 16 | `DEFAULT_REPLACE_EXAM_COMM_IND` | DOUBLE |  |  | Denotes the default communication type for Replace Exam. Verbal = 0, Original = 1 |
| 17 | `DEFAULT_VERBAL_COMM_IND` | DOUBLE | NOT NULL |  | This column indicates if the site is using default communication type of verbal or copying it from the original order while doing Accession Addon. |
| 18 | `DOC_IMAGE_COPY_ON_REPLACE_FLAG` | DOUBLE | NOT NULL |  | Indicates if the system will copy document images when an exam is replaced. The values represent the following: 0 - Never, 1 - Prompt, 2 - Always |
| 19 | `EXCLUDE_RES_SGNTR_IND` | DOUBLE | NOT NULL |  | Excludes signing resident's name on signature line if the radiologist finalized the report before resident signed it. 0 = Include, 1 = Exclude |
| 20 | `EX_COMP_PROF_CHRG_IND` | DOUBLE |  |  | This column indicates if the exams completion date and time is to be sent as the service date/time for professional billing instead of the final date/time. |
| 21 | `FLOW_DISP_REQUEST_IND` | DOUBLE | NOT NULL |  | This column indicates if Radiology results in Flowsheet display based on the requested date until exam is completed. |
| 22 | `HIDE_PRELIM_REPORT_IND` | DOUBLE | NOT NULL |  | Indicates if the preliminary report is to be hidden from viewing outside RADNET. |
| 23 | `INIT_READ_CREATED_BY_FLAG` | DOUBLE | NOT NULL |  | Indicates if the Wet Read text should be displayed as a preliminary result if created by certain groups. |
| 24 | `MOD_AFTER_VERIFY_IND` | DOUBLE |  |  | Allows or disallows the modification of order details after the exam has been verified. |
| 25 | `MRN_OPTION_FLAG` | DOUBLE |  |  | This column will display options for patients with multiple active medical record numbers. |
| 26 | `PRELIM_INIT_READ_IND` | DOUBLE | NOT NULL |  | Indicates whether the Wet Read text should be displayed as a preliminary result. 0 = Not Displayed, 1 = Displayed. |
| 27 | `PRINT_ADDR_HIST_FORM_IND` | DOUBLE | NOT NULL |  | Indicates if facility name and mailing address will be printed in mammography patient history sheet. |
| 28 | `PROTOCOL_IND` | DOUBLE | NOT NULL |  | Indicates if the site is using Millennium's solution to providing protocoling (clinical practice guidelines) for radiology orders. |
| 29 | `PROTOCOL_REAS_REQ_IND` | DOUBLE | NOT NULL |  | Indicates if the user must enter a reason when modifying a protocol after an exam is complete. |
| 30 | `PUBLISH_RAD_MEDS_ON_EMAR_IND` | DOUBLE | NOT NULL |  | Setting to determine if medications documented in Radiology should publish to the eMar. |
| 31 | `QUICK_PRINT_CUSTOM_TITLE_TXT` | VARCHAR(40) |  |  | Custom header title used by the quick print report functionality. |
| 32 | `RAD_OVERDUE_INTERVAL` | DOUBLE |  |  | The Rad_Overdue_Interval field contains the number of hours it takes for a report to become overdue while sitting in a radiologists queue. This is used for sorting and reporting purposes. |
| 33 | `RELEVANT_PRIOR_DT_TM_FLAG` | DOUBLE | NOT NULL |  | is the order that was completed or requested prior to the request date and time of the order.Stores the method for determining whether the relevant prior order is determined based on request date time or complete date time. |
| 34 | `REPLACE_GRP_ONLY_IND` | DOUBLE |  |  | This indicates if, when doing a replace, the user should only be allowed to replace from the procedures replacement group rather than with any procedure. |
| 35 | `REQ_PRSNL_AUTH_REPLACE_IND` | DOUBLE | NOT NULL |  | Determines if the user is required to enter the personnel that authorized the replace. |
| 36 | `REQ_REMOVE_REAS_IND` | DOUBLE | NOT NULL |  | If 1, remove reason is a required field. |
| 37 | `REQ_REPLACE_REAS_IND` | DOUBLE | NOT NULL |  | Determines if the user is required to enter a Replace Reason during a replace. |
| 38 | `RESIDENTS_IND` | DOUBLE |  |  | The Residents_Ind indicates if residents exist at this location. |
| 39 | `RES_MARKUP_QUEUE_IND` | DOUBLE | NOT NULL |  | The res_markup_queue_ind indicates if resident final markup queue read functionality is used by Radiology Desktop. |
| 40 | `RES_QUEUE_HR_INTERVAL` | DOUBLE |  |  | The Res_Queue_Hr_Interval indicates the number of hours that reports should be in a residents queue before automatically queueing to the radiologist. |
| 41 | `RET_AUTO_NOTE_IND` | DOUBLE |  |  | This column indicates if the sticky note form should automatically be launched within Radiologist Desktop when a report is returned to resident or transcription. |
| 42 | `RET_TO_RES_INTERVAL` | DOUBLE |  |  | This column indicates the number of hours a report should show in a residents queue before showing up in the radiologists queue after a report has been returned to resident. |
| 43 | `SERVICE_RESOURCE_CD` | DOUBLE | NOT NULL | FK→ | The Service_Resource_Cd is a foreign key to the Service_Resource table. |
| 44 | `SYNC_SIGN_LINE_IND` | DOUBLE | NOT NULL |  | Determines whether preliminary signature lines are saved synchronously (1) or asynchronously (0). 0 is the default |
| 45 | `TECHNIQUE_DOC_IND` | DOUBLE |  |  | This column indicates if technique documentation is to be used. |
| 46 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 47 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 48 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 49 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 50 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 51 | `VALIDATE_REQ_DATE_IND` | DOUBLE | NOT NULL |  | The system shall warn the user when attempting to start and complete an exam on a date other than the requested date for that exam. This check shall be performed only once in the start/complete process. |
| 52 | `VETTBL_FLTR_BY_ORDER_DT_TM_IND` | DOUBLE | NOT NULL |  | *** OBSOLETE *** |
| 53 | `VETTING_IND` | DOUBLE | NOT NULL |  | Determines if Vetting is enabled for the system. |
| 54 | `VETTING_TAB_NAME` | VARCHAR(25) |  |  | Name used for the Vetting tab in Rad Online Worklist. |
| 55 | `VIEW_CANCELLED_FLOW_IND` | DOUBLE | NOT NULL |  | This column indicates if cancelled reports should be viewable on the flowsheet. |
| 56 | `VIEW_ONHOLD_FLOW_IND` | DOUBLE | NOT NULL |  | This column indicates if on hold reports should be viewable on the flowsheet. |
| 57 | `VIEW_PRELIM_FLOW_FLAG` | DOUBLE | NOT NULL |  | View Preliminary Flowsheet Flag 0 - Not viewable 1 - Viewable 2 - Viewable but only after images or text have been acquired |
| 58 | `VIEW_PRELIM_FLOW_IND` | DOUBLE | NOT NULL |  | The View_Prelim_flow_Ind indicates if preliminary reports are to be viewable within inquiries in Flowsheet. |
| 59 | `VIEW_PRELIM_IND` | DOUBLE |  |  | The View_Prelim_Ind indicates if preliminary reports are to be viewable within inquiries in RadNet applications. |
| 60 | `VIEW_REJECTED_FLOW_IND` | DOUBLE | NOT NULL |  | This column indicates if rejected reports should be viewable on the flowsheet. |
| 61 | `VIEW_REMOVED_FLOW_IND` | DOUBLE | NOT NULL |  | This column indicates if removed reports should be viewable on the flowsheet. |
| 62 | `WITHHOLD_RET_TO_RAD_IND` | DOUBLE |  |  | This column indicates if a report that was returned to a resident should stay only in the residents queue until the resident re-accepts the report. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `SERVICE_RESOURCE_CD` | [SERVICE_RESOURCE](SERVICE_RESOURCE.md) | `SERVICE_RESOURCE_CD` |

