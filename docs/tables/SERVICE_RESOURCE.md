# SERVICE_RESOURCE

> The primary table for person (role), place or thing that performs work. Holds all levels of the hierarchy including Institutions, Departments, Sections, Subsections, and the fifth level which varies dependent upon the discipline.

**Description:** Service Resource  
**Table type:** REFERENCE  
**Primary key:** `SERVICE_RESOURCE_CD`  
**Columns:** 39  
**Referenced by:** 121 columns

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ACCN_SITE_PREFIX` | CHAR(5) |  |  | Used by SurgiNet. Associated with a Surgical Staging Area. Used when generating an OR Case numberwhen a surgical procedure is requested. User defined. |
| 2 | `ACTIVE_IND` | DOUBLE |  |  | The table row is active or inactive. A row is generally active unless it is in an inactive state such as logically deleted, combined away, pending purge, etc. |
| 3 | `ACTIVE_STATUS_CD` | DOUBLE | NOT NULL |  | Indicates the status of the row itself (not the data in the row) such as active, inactive, combined away, pending purge, etc. |
| 4 | `ACTIVE_STATUS_DT_TM` | DATETIME |  |  | The date and time that the active_status_cd was set. |
| 5 | `ACTIVE_STATUS_PRSNL_ID` | DOUBLE | NOT NULL |  | The person who caused the active_status_cd to be set or change. |
| 6 | `ACTIVITY_SUBTYPE_CD` | DOUBLE | NOT NULL |  | A filtering mechanism for service resource cdf_meanings which are used across disciplines (such as subsection). The user selects the subtype when adding the service resource. Programmatically an application can return a subset of resources with a specific subtype. |
| 7 | `ACTIVITY_TYPE_CD` | DOUBLE | NOT NULL |  | A filtering mechanism for service resource cdf_meanings which are used across disciplines (such as section). The user selects the activity type when adding the service resource. Programmatically an application can return a subset of resources with a specific activity type. |
| 8 | `AUTOLOGIN_IND` | DOUBLE |  |  | Determines whether or not to perform a login of the specimen container when results are posting from an MDI. |
| 9 | `AUTO_VERF_IND` | DOUBLE |  |  | Allows the user to indicate whether results posted from this resource should be automatically verified without human intervention or review. |
| 10 | `BEG_EFFECTIVE_DT_TM` | DATETIME | NOT NULL |  | The date and time for which this table row becomes effective. Normally, this will be the date and time the row is added, but could be a past or future date and time. |
| 11 | `CLIA_NUMBER_TXT` | VARCHAR(40) | NOT NULL |  | CLIA Number in text format. The Clinical Laboratory Improvement Act number associated with the service resource. |
| 12 | `COLLECTED_DOWNLOAD_IND` | DOUBLE | NOT NULL |  | Will be used to determine whether an accn will be downloaded to an instrument when it is collected(true) or whether it will be downloaded when it is either logged into lab or dispatched(false) |
| 13 | `CS_LOGIN_LOC_CD` | DOUBLE | NOT NULL |  | Used by PathNet. Determines whether a specimen is 'in lab' and ready for processing. When a specimen is logged in, the login app prompts for a login location. It compares that login location to the resource's login location. If they are different, the specimen isn't considered 'in lab' and will not appear on pending worklists, etc.. |
| 14 | `DATA_STATUS_CD` | DOUBLE | NOT NULL |  | Data status indicates a level of authenticity of the row data. Typically this will either be AUTHENTICATED or UNAUTHENTICATED. |
| 15 | `DATA_STATUS_DT_TM` | DATETIME |  |  | The date and time that the data_status_cd was set. |
| 16 | `DATA_STATUS_PRSNL_ID` | DOUBLE | NOT NULL |  | The person who caused the data_status_cd to be set or change. |
| 17 | `DISCIPLINE_TYPE_CD` | DOUBLE | NOT NULL |  | A filtering mechanism for service resource cdf_meanings which are used across disciplines (such as department). The user selects the discipline when adding the service resource. Programmatically an application can return a subset of resources with a specific discipline. |
| 18 | `DISPATCH_DOWNLOAD_IND` | DOUBLE |  |  | Will be used to determine whether an accn will be downloaded to an instrument when it is dispatched(true) or whether it will be downloaded when it is either logged into lab or in collected status(false). |
| 19 | `END_EFFECTIVE_DT_TM` | DATETIME | NOT NULL |  | The date/time after which the row is no longer valid as active current data. This may be valued with the date that the row became inactive. |
| 20 | `EXCEPT_EXIST_IND` | DOUBLE |  |  | Used to determine whether an exception to the calendar for the resource exists (i.e., down on New Year's Day even though it falls on a Monday which is normally an open day). |
| 21 | `INSTANCE_ID` | DOUBLE | NOT NULL |  | Not currently in use. To be Obsoleted. |
| 22 | `INVENTORY_RESOURCE_CD` | DOUBLE | NOT NULL |  | Filled out for pharmacy subsections. If the pharmacy subsection maintains their inventory at a different service_resource, this indicates which pharmacy has the inventory. |
| 23 | `INV_LOCATION_CD` | DOUBLE | NOT NULL |  | Identifies the related inventory location for a primary service resource. |
| 24 | `LOCATION_CD` | DOUBLE | NOT NULL | FK→ | The physical location of the service resource. A unique internal identifier. |
| 25 | `MEDICAL_DIRECTOR_NAME` | VARCHAR(100) | NOT NULL |  | Medical Dirctor Name associated with the Service Resource. |
| 26 | `OPER_MODE` | CHAR(1) |  |  | Identifies interface functionality with regards to bidirectional, unidirectional or Host Query. B, U, or Q respectively. |
| 27 | `ORGANIZATION_ID` | DOUBLE | NOT NULL | FK→ | A unique internal identifier for the organization to which the service resource is associated. |
| 28 | `PAT_CARE_LOC_IND` | DOUBLE |  |  | Used by pharmacy to indicate that this resource is located in a nurse unit rather than in the pharmacy. |
| 29 | `PHARMACY_TYPE_CD` | DOUBLE | NOT NULL |  | If the service resource is a pharmacy section or subsection, indicates the type of pharmacy from code_set 4500. Currently home infustion, long term care, inpatient, mail order, and retail. |
| 30 | `RUN_TMPLT_CD` | DOUBLE | NOT NULL |  | The rule by which the system will determine how large a (lab) instrument's run can be which will impact how often quality control is run. Examples include: the number of accns, certain number of minutes, by shift, etc. This column is not being used. |
| 31 | `RX_CHARGE_IND` | DOUBLE |  |  | For Unit Based Cabinets this indicates whether the dispense event should always be charged thus overriding the dispense category settings. |
| 32 | `SERVICE_RESOURCE_CD` | DOUBLE | NOT NULL | PK | A unique internal identifier for this service resource. |
| 33 | `SERVICE_RESOURCE_TYPE_CD` | DOUBLE | NOT NULL |  | Service resource type defines the kind of resource (I.e., department, section, exam room. instrument, etc.). Service Resource types have Cerner defined meanings in the common data foundation. |
| 34 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 35 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 36 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 37 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 38 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |
| 39 | `VIEW_TYPE_CD` | DOUBLE | NOT NULL | FK→ | View Type. Archived; Replaced by Root_cd. The conversion utility uses this field though to fill out root_cd. LOC_CONVERT_VIEW_TYPES. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `LOCATION_CD` | [LOCATION](LOCATION.md) | `LOCATION_CD` |
| `ORGANIZATION_ID` | [ORGANIZATION](ORGANIZATION.md) | `ORGANIZATION_ID` |
| `VIEW_TYPE_CD` | [CODE_VALUE](CODE_VALUE.md) | `CODE_VALUE` |

## Referenced by (121)

| From table | Column |
|------------|--------|
| [AP_PREFIX](AP_PREFIX.md) | `SERVICE_RESOURCE_CD` |
| [ASSAY_PROCESSING_R](ASSAY_PROCESSING_R.md) | `LOADED_SERVICE_RESOURCE_CD` |
| [ASSAY_PROCESSING_R](ASSAY_PROCESSING_R.md) | `SERVICE_RESOURCE_CD` |
| [ASSAY_RESOURCE_LIST](ASSAY_RESOURCE_LIST.md) | `SERVICE_RESOURCE_CD` |
| [ASSAY_RESOURCE_LOT](ASSAY_RESOURCE_LOT.md) | `SERVICE_RESOURCE_CD` |
| [AUTO_VERIFY](AUTO_VERIFY.md) | `SERVICE_RESOURCE_CD` |
| [AV_RES_CAT](AV_RES_CAT.md) | `SERVICE_RESOURCE_CD` |
| [BB_INVENTORY_AREA](BB_INVENTORY_AREA.md) | `SERVICE_RESOURCE_CD` |
| [BILL_ONLY_SUBSECT_RELTN](BILL_ONLY_SUBSECT_RELTN.md) | `SERVICE_RESOURCE_CD` |
| [BMDI_ACQUIRED_DATA_TRACK](BMDI_ACQUIRED_DATA_TRACK.md) | `DEVICE_CD` |
| [BMDI_DEVICE_NOMENCLATURE](BMDI_DEVICE_NOMENCLATURE.md) | `DEVICE_CD` |
| [BMDI_DEVICE_PARAMETER](BMDI_DEVICE_PARAMETER.md) | `DEVICE_CD` |
| [BMDI_MONITORED_DEVICE](BMDI_MONITORED_DEVICE.md) | `ALTERNATE_DEVICE_CD` |
| [BMDI_MONITORED_DEVICE](BMDI_MONITORED_DEVICE.md) | `DEVICE_CD` |
| [CALENDAR_EXCEPTION](CALENDAR_EXCEPTION.md) | `SERVICE_RESOURCE_CD` |
| [CONCEPT_IDENTIFIER_DTA](CONCEPT_IDENTIFIER_DTA.md) | `SERVICE_RESOURCE_CD` |
| [CONTAINER_EVENT](CONTAINER_EVENT.md) | `FROM_SERVICE_RESOURCE_CD` |
| [CONTAINER_EVENT](CONTAINER_EVENT.md) | `SERVICE_RESOURCE_CD` |
| [CV_STEP](CV_STEP.md) | `PERF_LOC_CD` |
| [CV_STEP_SCHED](CV_STEP_SCHED.md) | `SCHED_LOC_CD` |
| [CYTO_ALPHA_SECURITY](CYTO_ALPHA_SECURITY.md) | `REQUEUE_SERVICE_RESOURCE_CD` |
| [CYTO_SCREENING_SECURITY](CYTO_SCREENING_SECURITY.md) | `ABNORMAL_SERVICE_RESOURCE_CD` |
| [CYTO_SCREENING_SECURITY](CYTO_SCREENING_SECURITY.md) | `ATYPICAL_SERVICE_RESOURCE_CD` |
| [CYTO_SCREENING_SECURITY](CYTO_SCREENING_SECURITY.md) | `CHR_SERVICE_RESOURCE_CD` |
| [CYTO_SCREENING_SECURITY](CYTO_SCREENING_SECURITY.md) | `NORMAL_SERVICE_RESOURCE_CD` |
| [CYTO_SCREENING_SECURITY](CYTO_SCREENING_SECURITY.md) | `OVER_SERVICE_RESOURCE_CD` |
| [CYTO_SCREENING_SECURITY](CYTO_SCREENING_SECURITY.md) | `UNSAT_SERVICE_RESOURCE_CD` |
| [DEPARTMENT](DEPARTMENT.md) | `SERVICE_RESOURCE_CD` |
| [DEVICE_HL7_MAP](DEVICE_HL7_MAP.md) | `DEVICE_CD` |
| [DI_CLIENT_CONFIG](DI_CLIENT_CONFIG.md) | `SERVICE_RESOURCE_CD` |
| [EXAM_FOLDER](EXAM_FOLDER.md) | `LIB_GROUP_CD` |
| [IMAGE_CLASS_TYPE](IMAGE_CLASS_TYPE.md) | `DEFAULT_RETURN_LOCN_CD` |
| [IMAGE_CLASS_TYPE](IMAGE_CLASS_TYPE.md) | `DEFAULT_TRACKING_POINT_CD` |
| [IMAGE_CLASS_TYPE](IMAGE_CLASS_TYPE.md) | `LIB_GROUP_CD` |
| [IM_DEVICE](IM_DEVICE.md) | `SERVICE_RESOURCE_CD` |
| [INSTR_ACCN_QUEUE](INSTR_ACCN_QUEUE.md) | `SERVICE_RESOURCE_CD` |
| [INTERP_DATA](INTERP_DATA.md) | `SERVICE_RESOURCE_CD` |
| [INTERP_TASK_ASSAY](INTERP_TASK_ASSAY.md) | `SERVICE_RESOURCE_CD` |
| [ITEM_SR_LOC_R](ITEM_SR_LOC_R.md) | `SERVICE_RESOURCE_CD` |
| [LAB_BENCH](LAB_BENCH.md) | `SERVICE_RESOURCE_CD` |
| [LIBRARY_GROUP](LIBRARY_GROUP.md) | `SERVICE_RESOURCE_CD` |
| [LOC_RESOURCE_R](LOC_RESOURCE_R.md) | `SERVICE_RESOURCE_CD` |
| [MAMMO_FOL_UP_LETTER_SECT](MAMMO_FOL_UP_LETTER_SECT.md) | `SERVICE_RESOURCE_CD` |
| [MAMMO_STUDY](MAMMO_STUDY.md) | `SUBSECTION_CD` |
| [MDI_PARAMETER](MDI_PARAMETER.md) | `SERVICE_RESOURCE_CD` |
| [MIC_ABN_ORG_RESPONSE_CODE](MIC_ABN_ORG_RESPONSE_CODE.md) | `SERVICE_RESOURCE_CD` |
| [MIC_ABN_SUS_RESULT](MIC_ABN_SUS_RESULT.md) | `SERVICE_RESOURCE_CD` |
| [MIC_ACT_ANG_SUM_RPT](MIC_ACT_ANG_SUM_RPT.md) | `SERVICE_RESOURCE_CD` |
| [MIC_ANG_AUTOMATED](MIC_ANG_AUTOMATED.md) | `INSTR_RESOURCE_CD` |
| [MIC_ANG_AUTOMATED](MIC_ANG_AUTOMATED.md) | `SERVICE_RESOURCE_CD` |
| [MIC_ANG_TIMES](MIC_ANG_TIMES.md) | `SERVICE_RESOURCE_CD` |
| [MIC_EVENT_LOG](MIC_EVENT_LOG.md) | `SERVICE_RESOURCE_CD` |
| [MIC_GROUP_RESPONSE](MIC_GROUP_RESPONSE.md) | `SERVICE_RESOURCE_CD` |
| [MIC_INSTR_TRANS](MIC_INSTR_TRANS.md) | `SERVICE_RESOURCE_CD` |
| [MIC_LINK_WARNING](MIC_LINK_WARNING.md) | `SERVICE_RESOURCE_CD` |
| [MIC_MEDIA_DEFAULT](MIC_MEDIA_DEFAULT.md) | `SERVICE_RESOURCE_CD` |
| [MIC_ORDER_LAB](MIC_ORDER_LAB.md) | `SERVICE_RESOURCE_CD` |
| [MIC_REF_ANG](MIC_REF_ANG.md) | `SERVICE_RESOURCE_CD` |
| [MIC_REF_BILLING_AB](MIC_REF_BILLING_AB.md) | `SERVICE_RESOURCE_CD` |
| [MIC_REF_BILLING_SUS](MIC_REF_BILLING_SUS.md) | `SERVICE_RESOURCE_CD` |
| [MIC_REF_BIO_FORMAT](MIC_REF_BIO_FORMAT.md) | `SERVICE_RESOURCE_CD` |
| [MIC_REPORT_CORRELATION](MIC_REPORT_CORRELATION.md) | `SERVICE_RESOURCE_CD` |
| [MIC_RPT_PARAMS](MIC_RPT_PARAMS.md) | `SERVICE_RESOURCE_CD` |
| [MIC_STAIN_CORRELATION](MIC_STAIN_CORRELATION.md) | `SERVICE_RESOURCE_CD` |
| [MIC_TASK_LOG](MIC_TASK_LOG.md) | `TASK_LOCATION_CD` |
| [MIC_VALID_SUS_PANEL](MIC_VALID_SUS_PANEL.md) | `SERVICE_RESOURCE_CD` |
| [MIC_WORKCARD_CORRELATION](MIC_WORKCARD_CORRELATION.md) | `SERVICE_RESOURCE_CD` |
| [MM_INSTANCE](MM_INSTANCE.md) | `MFR_CD` |
| [MM_XFI_INSTANCE](MM_XFI_INSTANCE.md) | `MFR_CD` |
| [MM_XFI_QOH](MM_XFI_QOH.md) | `MANUF_CD` |
| [ORGANIZATION_RESOURCE](ORGANIZATION_RESOURCE.md) | `SERVICE_RESOURCE_CD` |
| [PROCESSING_TASK](PROCESSING_TASK.md) | `SERVICE_RESOURCE_CD` |
| [PROFILE_RESOURCE_LIST](PROFILE_RESOURCE_LIST.md) | `SERVICE_RESOURCE_CD` |
| [PULL_LIST_CONTROLS](PULL_LIST_CONTROLS.md) | `SERVICE_RESOURCE_CD` |
| [QC_ALPHA_RESPONSES](QC_ALPHA_RESPONSES.md) | `SERVICE_RESOURCE_CD` |
| [QC_TROUBLE_STEP](QC_TROUBLE_STEP.md) | `SERVICE_RESOURCE_CD` |
| [RAD_DEF_SERV_RES](RAD_DEF_SERV_RES.md) | `DEF_SER_RES_CD` |
| [RAD_DEF_SERV_RES](RAD_DEF_SERV_RES.md) | `SERVICE_RESOURCE_CD` |
| [RAD_EXAM_ROOM](RAD_EXAM_ROOM.md) | `SERVICE_RESOURCE_CD` |
| [RAD_FOLD_TRANS_RULE](RAD_FOLD_TRANS_RULE.md) | `FROM_LIB_CD` |
| [RAD_FOLD_TRANS_RULE](RAD_FOLD_TRANS_RULE.md) | `TO_LIB_CD` |
| [RAD_FOLLOW_UP_PRINT_CTRL](RAD_FOLLOW_UP_PRINT_CTRL.md) | `DEPARTMENT_CD` |
| [RAD_FOLLOW_UP_PRINT_CTRL](RAD_FOLLOW_UP_PRINT_CTRL.md) | `SECTION_CD` |
| [RAD_FOLLOW_UP_PRINT_CTRL](RAD_FOLLOW_UP_PRINT_CTRL.md) | `SUBSECTION_CD` |
| [RAD_FOL_UP_CONTROL_SECT](RAD_FOL_UP_CONTROL_SECT.md) | `SERVICE_RESOURCE_CD` |
| [RAD_IMAGE_SYS_CONTROLS](RAD_IMAGE_SYS_CONTROLS.md) | `SERVICE_RESOURCE_CD` |
| [RAD_PROTOCOL_CATALOG_R](RAD_PROTOCOL_CATALOG_R.md) | `SERVICE_RESOURCE_CD` |
| [RAD_REQ_CONTROLS](RAD_REQ_CONTROLS.md) | `SERVICE_RESOURCE_CD` |
| [RAD_SYS_CONTROLS](RAD_SYS_CONTROLS.md) | `SERVICE_RESOURCE_CD` |
| [RAD_TRACKING_CONTROLS](RAD_TRACKING_CONTROLS.md) | `SERVICE_RESOURCE_CD` |
| [REPORT_TASK](REPORT_TASK.md) | `SERVICE_RESOURCE_CD` |
| [RESOURCE_ACCESSION_R](RESOURCE_ACCESSION_R.md) | `SERVICE_RESOURCE_CD` |
| [RESOURCE_ASSAY_CONTROL](RESOURCE_ASSAY_CONTROL.md) | `SERVICE_RESOURCE_CD` |
| [RESOURCE_GROUP](RESOURCE_GROUP.md) | `CHILD_SERVICE_RESOURCE_CD` |
| [RESOURCE_GROUP](RESOURCE_GROUP.md) | `PARENT_SERVICE_RESOURCE_CD` |
| [RESOURCE_LOT_R](RESOURCE_LOT_R.md) | `SERVICE_RESOURCE_CD` |
| [ROLE](ROLE.md) | `SERVICE_RESOURCE_CD` |
| [RXA_ORD_DISP_HP_OBS_ST](RXA_ORD_DISP_HP_OBS_ST.md) | `DISP_FROM_SR_CD` |
| [RXA_WORK_LOAD_OBS_ST](RXA_WORK_LOAD_OBS_ST.md) | `DISP_FROM_SR_CD` |
| [RXS_ALERT](RXS_ALERT.md) | `RXS_DEVICE_SR_CD` |
| [RXS_ITEM_COUNTBACK](RXS_ITEM_COUNTBACK.md) | `SERVICE_RESOURCE_CD` |
| [RXS_LOCATION_TASK](RXS_LOCATION_TASK.md) | `SERVICE_RESOURCE_CD` |
| [RXS_LOC_SR_EVENT_RELTN](RXS_LOC_SR_EVENT_RELTN.md) | `SERVICE_RESOURCE_CD` |
| [RXS_TASK_SR_HX](RXS_TASK_SR_HX.md) | `SERVICE_RESOURCE_CD` |
| [RX_HEALTH_PLAN_SERV_RES_R](RX_HEALTH_PLAN_SERV_RES_R.md) | `SERVICE_RESOURCE_CD` |
| [RX_LOC_RESOURCE_RELTN](RX_LOC_RESOURCE_RELTN.md) | `SERVICE_RESOURCE_CD` |
| [RX_SCRIPT_TRANSFER_HX](RX_SCRIPT_TRANSFER_HX.md) | `SERVICE_RESOURCE_CD` |
| [RX_SCRIPT_TRANSFER_HX](RX_SCRIPT_TRANSFER_HX.md) | `XFER_SERVICE_RESOURCE_CD` |
| [SCH_APPT](SCH_APPT.md) | `SERVICE_RESOURCE_CD` |
| [SCH_RESOURCE](SCH_RESOURCE.md) | `SERVICE_RESOURCE_CD` |
| [SECTION](SECTION.md) | `SERVICE_RESOURCE_CD` |
| [SERVICE_RESOURCE_LAB_TYPE_R](SERVICE_RESOURCE_LAB_TYPE_R.md) | `SERVICE_RESOURCE_CD` |
| [SERV_RES_EXT_PHARM](SERV_RES_EXT_PHARM.md) | `SERVICE_RESOURCE_CD` |
| [SERV_RES_IDENTIFIER](SERV_RES_IDENTIFIER.md) | `SERVICE_RESOURCE_CD` |
| [SUB_SECTION](SUB_SECTION.md) | `SERVICE_RESOURCE_CD` |
| [SUB_SECTION](SUB_SECTION.md) | `TRANSCRIPT_QUE_CD` |
| [SURG_RESOURCE_STATUS](SURG_RESOURCE_STATUS.md) | `SERVICE_RESOURCE_CD` |
| [TECHNIQUE_DEFAULTS](TECHNIQUE_DEFAULTS.md) | `DEPARTMENT_CD` |
| [TECHNIQUE_DEFAULTS](TECHNIQUE_DEFAULTS.md) | `EXAM_ROOM_CD` |
| [TRACK_PT_LIBRARY](TRACK_PT_LIBRARY.md) | `SERVICE_RESOURCE_CD` |
| [VENDOR](VENDOR.md) | `SERVICE_RESOURCE_CD` |

