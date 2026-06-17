# HIM_SYSTEM_PARAMS

> Holds ProFile system parameters such as assigned allocation date ind.

**Description:** Profile system parameters  
**Table type:** REFERENCE  
**Primary key:** _(not published — see note)_  
**Columns:** 49

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ACTIVE_IND` | DOUBLE |  |  | The table row is active or inactive. A row is generally active unless it is in an inactive state such as logically deleted, combined away, pending purge, etc. |
| 2 | `ACTIVE_STATUS_CD` | DOUBLE | NOT NULL |  | Indicates the status of the row itself (not the data in the row) such as active, inactive, combined away, pending purge, etc. |
| 3 | `ACTIVE_STATUS_DT_TM` | DATETIME |  |  | The date and time that the active_status_cd was set. |
| 4 | `ACTIVE_STATUS_PRSNL_ID` | DOUBLE | NOT NULL |  | The person who caused the active_status_cd to be set or change. |
| 5 | `ALPHA_TRACKING_IND` | DOUBLE | NOT NULL |  | Indicates if client intends to upload alpha numeric tracking media identifiers. |
| 6 | `ASSIGN_ALLOCATION_DT_CD` | DOUBLE | NOT NULL |  | Used to determine which event is used to set the allocation date and time |
| 7 | `AUTO_MATCH_IND` | DOUBLE |  |  | When using Imaging, determines whether we use auto-matching logic when scanning in documents. |
| 8 | `BEG_EFFECTIVE_DT_TM` | DATETIME |  |  | The date and time for which this table row becomes effective. Normally, this will be the date and time the row is added, but could be a past or future date and time. |
| 9 | `CMPL_AUTO_HOLD_IND` | DOUBLE |  |  | This indicates if we put a visit on hold for a physician when all deficient documents are in a pending transcription state |
| 10 | `COSIGNATURE_IND` | DOUBLE |  |  | Indicates if we are using the cosign logic |
| 11 | `DAYS_TO_DELINQUENT` | DOUBLE |  |  | Number of days before a deficiency is considered delinquent |
| 12 | `DAYS_TO_QUALIFY_ORDER` | DOUBLE |  |  | Days elapsed after the ordered date before the order will no longer qualify for a letter. |
| 13 | `DAYS_TO_SUSPEND` | DOUBLE |  |  | Number of days before a delinquency is a candidate for suspension. |
| 14 | `DOCAGING_IND` | DOUBLE |  |  | This indicator is used to determine if a facility is using document-level aging metrics to track against physicians for dictation and signature completion. |
| 15 | `DOCAGING_PHYS_HOLD_IND` | DOUBLE |  |  | Indicator specifying whether we stop the document aging process when a physician is currently on hold. |
| 16 | `DOCAGING_VISIT_HOLD_IND` | DOUBLE |  |  | Indicator specifying whether we stop the document aging process when a visit is currently on hold. |
| 17 | `DOCUMENTS_IND` | DOUBLE |  |  | The indicator of documents |
| 18 | `ELECTRONIC_OP_MODE_IND` | DOUBLE |  |  | Indicates if this sight is electronic or using paper |
| 19 | `END_EFFECTIVE_DT_TM` | DATETIME |  |  | The date/time after which the row is no longer valid as active current data. This may be valued with the date that the row became inactive. |
| 20 | `FACILITY_LOGIC_IND` | DOUBLE |  |  | Is this group of facilities using facility logic? |
| 21 | `HIM_SYSTEM_PARAMS_ID` | DOUBLE | NOT NULL |  | Unique identifier for this table |
| 22 | `LOADING_LETTERS_IND` | DOUBLE |  |  | Indicates whether a load of letters is being performed. |
| 23 | `LOADING_POWERVISION_IND` | DOUBLE |  |  | Indicates whether a load of the PowerVision summary table is taking place. |
| 24 | `MANUAL_ALLOC_DT_UPDT_IND` | DOUBLE |  |  | Indicates if we allow use to manually update the allocation date |
| 25 | `MULTIPLE_PATIENTS_IND` | DOUBLE |  |  | An indicator that distinguishes between allowing one or multiple patients per Patient Information Request (PIR). Possible values: 0 -- Multiple Patients can be in one PIR 1 -- Only one patient allowed in a PIR. |
| 26 | `MULTI_ORG_ENCNTR_DISP_IND` | DOUBLE |  |  | Applies only when multiple institution logic is enabled. An indicator that determines how and if encounters/visits from institutions other than the requestor's institution are displayed. Possible values: 0 -- Those encounters/visits are hidden 1 -- They are displayed as read-only. |
| 27 | `ORDER_DELINQUENT_DAYS` | DOUBLE | NOT NULL |  | This is the number of days before an unsigned order qualifies the physician to be delinquent. |
| 28 | `ORDER_SUSPENSION_DAYS` | DOUBLE | NOT NULL |  | This is the number of days before an unsigned order qualifies the physician to be suspended. |
| 29 | `ORDER_TRACKING_IND` | DOUBLE | NOT NULL |  | Indicates whether or not to track orders. |
| 30 | `PAT_INFO_REQ_IND` | DOUBLE |  |  | Is facility using Patient Information Request module |
| 31 | `PENDING_SIGNS_IND` | DOUBLE | NOT NULL |  | Indicates if the site is using pending signs functionality. This flag is not visible in himSystemParams.exe and cannot be turned off once it is turned on via the conversion script. |
| 32 | `PUBLISH_IND` | DOUBLE |  |  | Indicates whether anticipated documents should be published in powerchart. |
| 33 | `REQUEST_NOTIFY_IND` | DOUBLE |  |  | Indicator to whether site wants to be notified of outstanding requests when checking charts in. |
| 34 | `ROI_CREDIT_CARD_IND` | DOUBLE | NOT NULL |  | ROI credit card indicator |
| 35 | `ROI_DEFAULT_ADDR_TYPE_CD` | DOUBLE | NOT NULL |  | This is the primary address type used to get the facilities address that will be printed on the ROI Invoice |
| 36 | `ROI_IND` | DOUBLE |  |  | Is facility using the Release of Information module |
| 37 | `ROI_INVOICE_IND` | DOUBLE |  |  | Is this institution using the request of information invoices? |
| 38 | `ROI_PRIMARY_ADDR_TYPE_CD` | DOUBLE | NOT NULL |  | This is the address type that will be defaulted to if the primary does not exist for printing the facility address on the Invoice. |
| 39 | `SINGLE_SCAN_IND` | DOUBLE |  |  | Determines whether using document imaging capability in Completion applications |
| 40 | `TAG_COLOR_ACTIVE_IND` | DOUBLE |  |  | Indicates if we are using tag colors. |
| 41 | `TAG_COLOR_COMMON_IND` | DOUBLE |  |  | Indicator to whether site is maintaining same tag color for a physician across all patient's visits. |
| 42 | `TASK_PLAN_ACTIVE_IND` | DOUBLE |  |  | Indicates if task plans are used |
| 43 | `TRACK_AUTO_HOLD_IND` | DOUBLE |  |  | Indicate if auto holds are used for the tracking module |
| 44 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 45 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 46 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 47 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 48 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 49 | `VISITAGING_IND` | DOUBLE |  |  | This indicator is used to determine if a facility is using visit-level aging metrics to track against physicians for signature of all relevant documents |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

