# LOCATION

> The location table is a reference of all locations in the system. Examples of some types of locations include facility (institution), building, nurse unit, room bed, outpatient, inventory, lab, pharmacy, etc.

**Description:** Location  
**Table type:** REFERENCE  
**Primary key:** `LOCATION_CD`  
**Columns:** 34  
**Referenced by:** 273 columns

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ACTIVE_IND` | DOUBLE |  |  | The table row is active or inactive. A row is generally active unless it is in an inactive state such as logically deleted, combined away, pending purge, etc. |
| 2 | `ACTIVE_STATUS_CD` | DOUBLE | NOT NULL |  | Indicates the status of the row itself (not the data in the row) such as active, inactive, combined away, pending purge, etc. |
| 3 | `ACTIVE_STATUS_DT_TM` | DATETIME |  |  | The date and time that the active_status_cd was set. |
| 4 | `ACTIVE_STATUS_PRSNL_ID` | DOUBLE | NOT NULL |  | The person who caused the active_status_cd to be set or change. |
| 5 | `APACHE_RELTN_FLAG` | DOUBLE | NOT NULL |  | Defines a relationship to be considered by Cerner Apache integrated Risk Adjustment software.0 - No defined relationship to Cerner Apache integrated Risk Adjustment software, 1 - Temporary procedural location used by Cerner Apache integrated Risk Adjustment software. A temporary procedural location is where a patient in an APACHE location may transfer to without being discharged from the current ICU encounter. An example of this is an operating room or a recovery room. |
| 6 | `BEG_EFFECTIVE_DT_TM` | DATETIME | NOT NULL |  | The date and time for which this table row becomes effective. Normally, this will be the date and time the row is added, but could be a past or future date and time. |
| 7 | `CENSUS_IND` | DOUBLE |  |  | Set to TRUE, if this location is be included on the patient census report. Otherwise, set to FALSE. |
| 8 | `CHART_FORMAT_ID` | DOUBLE |  | FK→ | Temporary mechanism to denote the chart format to be used for expedites when results should print at the location's printer |
| 9 | `CONTRIBUTOR_SOURCE_CD` | DOUBLE |  |  | The code value for the contributing system |
| 10 | `CONTRIBUTOR_SYSTEM_CD` | DOUBLE | NOT NULL |  | Contributor system identifies the source feed of data from which a row was populated. This is mainly used to determine how to update a set of data that may have originated from more than one source feed. |
| 11 | `DATA_STATUS_CD` | DOUBLE | NOT NULL |  | Data status indicates a level of authenticity of the row data. Typically this will either be AUTHENTICATED or UNAUTHENTICATED. |
| 12 | `DATA_STATUS_DT_TM` | DATETIME |  |  | The date and time that the data_status_cd was set. |
| 13 | `DATA_STATUS_PRSNL_ID` | DOUBLE | NOT NULL |  | The person who caused the data_status_cd to be set or change. |
| 14 | `DISCIPLINE_TYPE_CD` | DOUBLE | NOT NULL |  | Used with Service Area locations. Indicates the discipline (lab, rad, etc.) of the service area. |
| 15 | `END_EFFECTIVE_DT_TM` | DATETIME | NOT NULL |  | The date/time after which the row is no longer valid as active current data. This may be valued with the date that the row became inactive. |
| 16 | `EXP_LVL_CD` | DOUBLE |  |  | Temporary means to indicate when the expedite should be triggered (i.e., upon any result verification or only when the order is complete). |
| 17 | `FACILITY_ACCN_PREFIX_CD` | DOUBLE | NOT NULL |  | Used on facility location rows. Indicates the accession prefix (site prefix). |
| 18 | `ICU_IND` | DOUBLE |  |  | Indicates if this location should be considered an ICU location if/when the Cerner Apache integrated Risk Adjustment software is being used. |
| 19 | `LOCATION_CD` | DOUBLE | NOT NULL | PK FK→ | The field identifies the current permanent location of the patient. The location for an inpatient will be valued with the lowest level location type in the hierarchy of facility, building, nurse unit, room, bed. |
| 20 | `LOCATION_TYPE_CD` | DOUBLE | NOT NULL | FK→ | Location type defines the kind of location (I.e., nurse unit, room, inventory location, etc.). Location types have Cerner defined meanings in the common data foundation. |
| 21 | `ORGANIZATION_ID` | DOUBLE | NOT NULL | FK→ | This is the value of the unique primary identifier of the organization table. It is an internal system assigned number. |
| 22 | `PATCARE_NODE_IND` | DOUBLE |  |  | Used to filter patient care locations. If the user determines that they need to build facilities for their client organizations, this indicator would allow us to suppress displaying only those facilities that are hospitals. |
| 23 | `REF_LAB_ACCT_NBR` | VARCHAR(20) |  |  | This column is used to store the reference laboratory account number given to a location which uses the reference lab. It will be used for reference lab interfaces. It is a free text field. |
| 24 | `REGISTRATION_IND` | DOUBLE |  |  | Indicates whether it is applicable to register patients to this location at any given point in time. |
| 25 | `RESERVE_IND` | DOUBLE | NOT NULL |  | reserve indicator |
| 26 | `RESOURCE_IND` | DOUBLE |  |  | Set to TRUE, if this location has corresponding row(s) on the service resource table. Otherwise, set to FALSE. |
| 27 | `TRANSFER_DT_TM_IND` | DOUBLE | NOT NULL |  | Filled out for specimen tracking locations. Indicator for the system to know whether to update the culture start date time as transferred date time when the specimens are transferred to the location.Valid values:0 - Culture date time should be updated with login date time from specimen login application1 - Culture date time should be updated with transfer date time from transfer specimen application. |
| 28 | `TRANSMIT_OUTBOUND_ORDER_IND` | DOUBLE |  |  | Filled out for specimen tracking locations. Indicator for the system to know whether an outbound order should be triggered when specimens are transferred to the location (i.e., PTOP type of transaction). |
| 29 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 30 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 31 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 32 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 33 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 34 | `VIEW_TYPE_CD` | DOUBLE | NOT NULL | FK→ | OBSOLETE - Precursor to root_loc_cd on the LOCATION_GROUP table. Needed for the conversion utility "LOC_CONVERT_VIEW_TYPES". Once this utility has been executed, the attribute is not used and will be removed. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `CHART_FORMAT_ID` | [CHART_FORMAT](CHART_FORMAT.md) | `CHART_FORMAT_ID` |
| `LOCATION_CD` | [CODE_VALUE](CODE_VALUE.md) | `CODE_VALUE` |
| `LOCATION_TYPE_CD` | [CODE_VALUE](CODE_VALUE.md) | `CODE_VALUE` |
| `ORGANIZATION_ID` | [ORGANIZATION](ORGANIZATION.md) | `ORGANIZATION_ID` |
| `VIEW_TYPE_CD` | [CODE_VALUE](CODE_VALUE.md) | `CODE_VALUE` |

## Referenced by (273)

| From table | Column |
|------------|--------|
| [AC_CLASS_PERSON_RELTN](AC_CLASS_PERSON_RELTN.md) | `LOCATION_CD` |
| [AOAV_FACILITY_PREF](AOAV_FACILITY_PREF.md) | `LOC_FACILITY_CD` |
| [AOAV_FACILITY_REF](AOAV_FACILITY_REF.md) | `LOC_FACILITY_CD` |
| [AOAV_ICU_STAY](AOAV_ICU_STAY.md) | `INITIAL_LOC_NURSE_UNIT_CD` |
| [BB_SHIPMENT](BB_SHIPMENT.md) | `INVENTORY_AREA_CD` |
| [BB_SHIPMENT](BB_SHIPMENT.md) | `OWNER_AREA_CD` |
| [BED](BED.md) | `LOCATION_CD` |
| [BH_GROUP_DOC](BH_GROUP_DOC.md) | `LOCATION_CD` |
| [BR_ADO_DETAIL](BR_ADO_DETAIL.md) | `FACILITY_CD` |
| [BR_CCN_LOC_RELTN](BR_CCN_LOC_RELTN.md) | `LOCATION_CD` |
| [BR_CPC_LOC_RELTN](BR_CPC_LOC_RELTN.md) | `LOCATION_CD` |
| [BR_HCO_LOC_RELTN](BR_HCO_LOC_RELTN.md) | `LOCATION_CD` |
| [BR_MDRO_CAT_EVENT](BR_MDRO_CAT_EVENT.md) | `LOCATION_CD` |
| [BR_MDRO_CAT_ORGANISM](BR_MDRO_CAT_ORGANISM.md) | `LOCATION_CD` |
| [BR_MDRO_OUTBREAK](BR_MDRO_OUTBREAK.md) | `LOCATION_CD` |
| [BR_SETUP_WIZARD_LOC_RELTN](BR_SETUP_WIZARD_LOC_RELTN.md) | `LOCATION_CD` |
| [CDI_FORM_FACILITY_RELTN](CDI_FORM_FACILITY_RELTN.md) | `FACILITY_CD` |
| [CDI_PENDING_DOCUMENT](CDI_PENDING_DOCUMENT.md) | `LOCATION_CD` |
| [CE_MED_ADMIN_IDENT](CE_MED_ADMIN_IDENT.md) | `INV_FILL_LOCATION_CD` |
| [CHART_SEQ_GROUP_RELTN](CHART_SEQ_GROUP_RELTN.md) | `LOCATION_CD` |
| [CMS_CRITICAL_LOCATION](CMS_CRITICAL_LOCATION.md) | `LOCATION_CD` |
| [CNT_WV_KEY](CNT_WV_KEY.md) | `LOCATION_CD` |
| [CONTRIBUTOR_SYSTEM](CONTRIBUTOR_SYSTEM.md) | `LOC_FACILITY_CD` |
| [CR_STATIC_REGION_LOC_RELTN](CR_STATIC_REGION_LOC_RELTN.md) | `LOCATION_CD` |
| [DCP_SHIFT_ASSIGNMENT](DCP_SHIFT_ASSIGNMENT.md) | `LOC_BED_CD` |
| [DCP_SHIFT_ASSIGNMENT](DCP_SHIFT_ASSIGNMENT.md) | `LOC_BUILDING_CD` |
| [DCP_SHIFT_ASSIGNMENT](DCP_SHIFT_ASSIGNMENT.md) | `LOC_FACILITY_CD` |
| [DCP_SHIFT_ASSIGNMENT](DCP_SHIFT_ASSIGNMENT.md) | `LOC_ROOM_CD` |
| [DCP_SHIFT_ASSIGNMENT](DCP_SHIFT_ASSIGNMENT.md) | `LOC_UNIT_CD` |
| [DISPENSE_HX](DISPENSE_HX.md) | `DISP_LOC_CD` |
| [EEM_ABN_CHECK](EEM_ABN_CHECK.md) | `LOCATION_CD` |
| [EEM_ABN_LINK](EEM_ABN_LINK.md) | `LOCATION_CD` |
| [EEM_MOH_DETAIL](EEM_MOH_DETAIL.md) | `LOCATION_CD` |
| [EEM_PROFILE_LOCATION](EEM_PROFILE_LOCATION.md) | `LOCATION_CD` |
| [EKS_ADVSR_EVENT](EKS_ADVSR_EVENT.md) | `LOCATION_CD` |
| [ENCNTR_DOMAIN](ENCNTR_DOMAIN.md) | `LOC_BED_CD` |
| [ENCNTR_DOMAIN](ENCNTR_DOMAIN.md) | `LOC_BUILDING_CD` |
| [ENCNTR_DOMAIN](ENCNTR_DOMAIN.md) | `LOC_FACILITY_CD` |
| [ENCNTR_DOMAIN](ENCNTR_DOMAIN.md) | `LOC_NURSE_UNIT_CD` |
| [ENCNTR_DOMAIN](ENCNTR_DOMAIN.md) | `LOC_ROOM_CD` |
| [ENCNTR_LOCATION](ENCNTR_LOCATION.md) | `LOCATION_CD` |
| [ENCNTR_LOCATION](ENCNTR_LOCATION.md) | `LOC_BED_CD` |
| [ENCNTR_LOCATION](ENCNTR_LOCATION.md) | `LOC_BUILDING_CD` |
| [ENCNTR_LOCATION](ENCNTR_LOCATION.md) | `LOC_FACILITY_CD` |
| [ENCNTR_LOCATION](ENCNTR_LOCATION.md) | `LOC_NURSE_UNIT_CD` |
| [ENCNTR_LOCATION](ENCNTR_LOCATION.md) | `LOC_ROOM_CD` |
| [ENCNTR_LOC_HIST](ENCNTR_LOC_HIST.md) | `LOCATION_CD` |
| [ENCNTR_LOC_HIST](ENCNTR_LOC_HIST.md) | `LOC_BED_CD` |
| [ENCNTR_LOC_HIST](ENCNTR_LOC_HIST.md) | `LOC_BUILDING_CD` |
| [ENCNTR_LOC_HIST](ENCNTR_LOC_HIST.md) | `LOC_FACILITY_CD` |
| [ENCNTR_LOC_HIST](ENCNTR_LOC_HIST.md) | `LOC_NURSE_UNIT_CD` |
| [ENCNTR_LOC_HIST](ENCNTR_LOC_HIST.md) | `LOC_ROOM_CD` |
| [ENCNTR_PENDING](ENCNTR_PENDING.md) | `PEND_BED_CD` |
| [ENCNTR_PENDING](ENCNTR_PENDING.md) | `PEND_BUILDING_CD` |
| [ENCNTR_PENDING](ENCNTR_PENDING.md) | `PEND_FACILITY_CD` |
| [ENCNTR_PENDING](ENCNTR_PENDING.md) | `PEND_NURSE_UNIT_CD` |
| [ENCNTR_PENDING](ENCNTR_PENDING.md) | `PEND_ROOM_CD` |
| [ENCNTR_PENDING_HIST](ENCNTR_PENDING_HIST.md) | `PEND_BED_CD` |
| [ENCNTR_PENDING_HIST](ENCNTR_PENDING_HIST.md) | `PEND_BUILDING_CD` |
| [ENCNTR_PENDING_HIST](ENCNTR_PENDING_HIST.md) | `PEND_FACILITY_CD` |
| [ENCNTR_PENDING_HIST](ENCNTR_PENDING_HIST.md) | `PEND_NURSE_UNIT_CD` |
| [ENCNTR_PENDING_HIST](ENCNTR_PENDING_HIST.md) | `PEND_ROOM_CD` |
| [ENCOUNTER](ENCOUNTER.md) | `LOCATION_CD` |
| [ENCOUNTER](ENCOUNTER.md) | `LOC_BED_CD` |
| [ENCOUNTER](ENCOUNTER.md) | `LOC_BUILDING_CD` |
| [ENCOUNTER](ENCOUNTER.md) | `LOC_FACILITY_CD` |
| [ENCOUNTER](ENCOUNTER.md) | `LOC_NURSE_UNIT_CD` |
| [ENCOUNTER](ENCOUNTER.md) | `LOC_ROOM_CD` |
| [EXPEDITE_TRIGGER](EXPEDITE_TRIGGER.md) | `LOCATION_CD` |
| [FILL_BATCH](FILL_BATCH.md) | `LOC_FACILITY_CD` |
| [GL_TRANS_QUALIFIER](GL_TRANS_QUALIFIER.md) | `LOC_BED_CD` |
| [GL_TRANS_QUALIFIER](GL_TRANS_QUALIFIER.md) | `LOC_BUILDING_CD` |
| [GL_TRANS_QUALIFIER](GL_TRANS_QUALIFIER.md) | `LOC_FACILITY_CD` |
| [GL_TRANS_QUALIFIER](GL_TRANS_QUALIFIER.md) | `LOC_NURSE_UNIT_CD` |
| [GL_TRANS_QUALIFIER](GL_TRANS_QUALIFIER.md) | `LOC_ROOM_CD` |
| [HIM_UNSIGNED_ORDERS](HIM_UNSIGNED_ORDERS.md) | `FACILITY_CD` |
| [HP_FINANCIAL](HP_FINANCIAL.md) | `LOCATION_CD` |
| [ITEM_SR_LOC_R](ITEM_SR_LOC_R.md) | `LOCATION_CD` |
| [LABEL_PRINTER_DEF](LABEL_PRINTER_DEF.md) | `LOCATION_CD` |
| [LH_CNT_IC_LOC_HIST](LH_CNT_IC_LOC_HIST.md) | `BED_LOC_CD` |
| [LH_CNT_IC_LOC_HIST](LH_CNT_IC_LOC_HIST.md) | `BUILD_LOC_CD` |
| [LH_CNT_IC_LOC_HIST](LH_CNT_IC_LOC_HIST.md) | `FAC_LOC_CD` |
| [LH_CNT_IC_LOC_HIST](LH_CNT_IC_LOC_HIST.md) | `NU_LOC_CD` |
| [LH_CNT_IC_LOC_HIST](LH_CNT_IC_LOC_HIST.md) | `ROOM_LOC_CD` |
| [LH_CNT_IC_VAE](LH_CNT_IC_VAE.md) | `EVENT_LOC_CD` |
| [LH_CNT_IC_VAE](LH_CNT_IC_VAE.md) | `LOCATION_CD` |
| [LH_CNT_IC_VAE](LH_CNT_IC_VAE.md) | `MV_LOC_CD` |
| [LH_CNT_LTD_DATA](LH_CNT_LTD_DATA.md) | `INSERT_LOC_BED_CD` |
| [LH_CNT_LTD_DATA](LH_CNT_LTD_DATA.md) | `INSERT_LOC_FAC_CD` |
| [LH_CNT_LTD_DATA](LH_CNT_LTD_DATA.md) | `INSERT_LOC_NURSE_UNIT_CD` |
| [LH_CNT_LTD_DATA](LH_CNT_LTD_DATA.md) | `INSERT_LOC_ROOM_CD` |
| [LH_CNT_NHSN_EVENT_METRIC](LH_CNT_NHSN_EVENT_METRIC.md) | `LOC_FACILITY_CD` |
| [LH_CNT_NHSN_EVENT_METRIC](LH_CNT_NHSN_EVENT_METRIC.md) | `LOC_UNIT_CD` |
| [LOCATION_GROUP](LOCATION_GROUP.md) | `CHILD_LOC_CD` |
| [LOCATION_GROUP](LOCATION_GROUP.md) | `PARENT_LOC_CD` |
| [LOCATION_INV_INFO](LOCATION_INV_INFO.md) | `LOCATION_CD` |
| [LOC_RESOURCE_R](LOC_RESOURCE_R.md) | `LOCATION_CD` |
| [MM_APPROVAL_QUEUE](MM_APPROVAL_QUEUE.md) | `FILL_LOCATION_CD` |
| [MM_DISCREPANCY](MM_DISCREPANCY.md) | `CLUSTER_CD` |
| [MM_DISCREPANCY](MM_DISCREPANCY.md) | `FACILITY_CD` |
| [MM_DISCREPANCY](MM_DISCREPANCY.md) | `LOCATION_CD` |
| [MM_DISCREPANCY](MM_DISCREPANCY.md) | `LOCATOR_CD` |
| [MM_ITEM_ORG_COST_HIST](MM_ITEM_ORG_COST_HIST.md) | `ORG_LOCATION_CD` |
| [MM_PRICE_FORMULA_LOC_RELTN](MM_PRICE_FORMULA_LOC_RELTN.md) | `LOCATION_CD` |
| [MM_SUPPLY_CABINET](MM_SUPPLY_CABINET.md) | `LOC_CD` |
| [MM_TEMPLATE](MM_TEMPLATE.md) | `LOCATION_CD` |
| [MM_TRANS_LINE](MM_TRANS_LINE.md) | `PERFORMING_LOC_CD` |
| [MM_XFI_INSTANCE](MM_XFI_INSTANCE.md) | `STORAGE_LOCATION_CD` |
| [NURSE_UNIT](NURSE_UNIT.md) | `LOCATION_CD` |
| [NURSE_UNIT](NURSE_UNIT.md) | `LOC_BUILDING_CD` |
| [NURSE_UNIT](NURSE_UNIT.md) | `LOC_FACILITY_CD` |
| [OMF_RADMGMT_ORDER_ST](OMF_RADMGMT_ORDER_ST.md) | `BED_AT_EXAM_CMPLT_CD` |
| [OMF_RADMGMT_ORDER_ST](OMF_RADMGMT_ORDER_ST.md) | `LOC_AT_EXAM_CMPLT_CD` |
| [OMF_RADMGMT_ORDER_ST](OMF_RADMGMT_ORDER_ST.md) | `ROOM_AT_EXAM_CMPLT_CD` |
| [ORDER_DAILY_REVIEW_RSPNL](ORDER_DAILY_REVIEW_RSPNL.md) | `PATIENT_LOCATION_FACILITY_CD` |
| [ORDER_DAILY_REVIEW_RSPNL](ORDER_DAILY_REVIEW_RSPNL.md) | `PATIENT_LOCATION_NURSE_UNIT_CD` |
| [ORDER_RESULTS_HOLD_CONFIG](ORDER_RESULTS_HOLD_CONFIG.md) | `LOCATION_CD` |
| [ORD_LOC_PHARM_RELTN](ORD_LOC_PHARM_RELTN.md) | `LOC_CD` |
| [OSM_FORM_PRINTING](OSM_FORM_PRINTING.md) | `LOCATION_CD` |
| [OUTCOME_CAT_LOC_RELTN](OUTCOME_CAT_LOC_RELTN.md) | `LOCATION_CD` |
| [PCT_CARE_TEAM](PCT_CARE_TEAM.md) | `FACILITY_CD` |
| [PERSON_DISMISSAL](PERSON_DISMISSAL.md) | `LOCATION_CD` |
| [PFT_ENCNTR](PFT_ENCNTR.md) | `LOC_FACILITY_CD` |
| [PFT_ENCNTR](PFT_ENCNTR.md) | `LOC_NURSE_UNIT_CD` |
| [PFT_ENCNTR_CENSUS_SUMMARY](PFT_ENCNTR_CENSUS_SUMMARY.md) | `LOC_BUILDING_CD` |
| [PFT_ENCNTR_CENSUS_SUMMARY](PFT_ENCNTR_CENSUS_SUMMARY.md) | `LOC_FACILITY_CD` |
| [PFT_ENCNTR_CENSUS_SUMMARY](PFT_ENCNTR_CENSUS_SUMMARY.md) | `LOC_NURSE_UNIT_CD` |
| [PFT_REG_MOD](PFT_REG_MOD.md) | `LOC_FACILITY_CD` |
| [PHA_BATCH_REPORT](PHA_BATCH_REPORT.md) | `LOC_FACILITY_CD` |
| [PHA_ORD_ACT_OBS_ST](PHA_ORD_ACT_OBS_ST.md) | `FUTURE_LOC_FACILITY_CD` |
| [PHA_ORD_ACT_OBS_ST](PHA_ORD_ACT_OBS_ST.md) | `FUTURE_LOC_NURSE_UNIT_CD` |
| [PM_AUTO_DISCH_PARM_SET_R](PM_AUTO_DISCH_PARM_SET_R.md) | `LOC_FACILITY_CD` |
| [PM_LOC_ATTRIB](PM_LOC_ATTRIB.md) | `LOCATION_CD` |
| [PM_LOC_ATTRIB_HIST](PM_LOC_ATTRIB_HIST.md) | `LOCATION_CD` |
| [PM_MOH_INPAT_CENSUS](PM_MOH_INPAT_CENSUS.md) | `LOCATION_CD` |
| [PM_RBC_PARM_SET_R](PM_RBC_PARM_SET_R.md) | `LOC_FACILITY_CD` |
| [PM_RBC_RS_ENCNTR_CHARGE_R](PM_RBC_RS_ENCNTR_CHARGE_R.md) | `LOC_FACILITY_CD` |
| [PM_RBC_RS_ENCNTR_CHARGE_R](PM_RBC_RS_ENCNTR_CHARGE_R.md) | `PERF_LOC_CD` |
| [PM_ROOM_BED_CHARGE](PM_ROOM_BED_CHARGE.md) | `LOC_BED_CD` |
| [PM_ROOM_BED_CHARGE](PM_ROOM_BED_CHARGE.md) | `LOC_BUILDING_CD` |
| [PM_ROOM_BED_CHARGE](PM_ROOM_BED_CHARGE.md) | `LOC_FACILITY_CD` |
| [PM_ROOM_BED_CHARGE](PM_ROOM_BED_CHARGE.md) | `LOC_NURSE_UNIT_CD` |
| [PM_ROOM_BED_CHARGE](PM_ROOM_BED_CHARGE.md) | `LOC_ROOM_CD` |
| [PM_TRANSACTION](PM_TRANSACTION.md) | `N_LOCATION_CD` |
| [PM_TRANSACTION](PM_TRANSACTION.md) | `N_LOC_BED_CD` |
| [PM_TRANSACTION](PM_TRANSACTION.md) | `N_LOC_BUILDING_CD` |
| [PM_TRANSACTION](PM_TRANSACTION.md) | `N_LOC_FACILITY_CD` |
| [PM_TRANSACTION](PM_TRANSACTION.md) | `N_LOC_NURSE_UNIT_CD` |
| [PM_TRANSACTION](PM_TRANSACTION.md) | `N_LOC_ROOM_CD` |
| [PM_TRANSACTION](PM_TRANSACTION.md) | `O_LOCATION_CD` |
| [PM_TRANSACTION](PM_TRANSACTION.md) | `O_LOC_BED_CD` |
| [PM_TRANSACTION](PM_TRANSACTION.md) | `O_LOC_BUILDING_CD` |
| [PM_TRANSACTION](PM_TRANSACTION.md) | `O_LOC_FACILITY_CD` |
| [PM_TRANSACTION](PM_TRANSACTION.md) | `O_LOC_NURSE_UNIT_CD` |
| [PM_TRANSACTION](PM_TRANSACTION.md) | `O_LOC_ROOM_CD` |
| [PM_WAIT_LIST](PM_WAIT_LIST.md) | `LOCATION_CD` |
| [PM_WAIT_LIST](PM_WAIT_LIST.md) | `LOC_BED_CD` |
| [PM_WAIT_LIST](PM_WAIT_LIST.md) | `LOC_BUILDING_CD` |
| [PM_WAIT_LIST](PM_WAIT_LIST.md) | `LOC_FACILITY_CD` |
| [PM_WAIT_LIST](PM_WAIT_LIST.md) | `LOC_NURSE_UNIT_CD` |
| [PM_WAIT_LIST](PM_WAIT_LIST.md) | `LOC_ROOM_CD` |
| [PM_WAIT_LIST_HIST](PM_WAIT_LIST_HIST.md) | `LOCATION_CD` |
| [PM_WAIT_LIST_HIST](PM_WAIT_LIST_HIST.md) | `LOC_BED_CD` |
| [PM_WAIT_LIST_HIST](PM_WAIT_LIST_HIST.md) | `LOC_BUILDING_CD` |
| [PM_WAIT_LIST_HIST](PM_WAIT_LIST_HIST.md) | `LOC_FACILITY_CD` |
| [PM_WAIT_LIST_HIST](PM_WAIT_LIST_HIST.md) | `LOC_NURSE_UNIT_CD` |
| [PM_WAIT_LIST_HIST](PM_WAIT_LIST_HIST.md) | `LOC_ROOM_CD` |
| [PRSNL_CURRENT_LOC](PRSNL_CURRENT_LOC.md) | `LOCATION_CD` |
| [PRSNL_LOCATION_R](PRSNL_LOCATION_R.md) | `LOCATION_CD` |
| [PRSNL_LOC_RELTN](PRSNL_LOC_RELTN.md) | `LOC_BED_CD` |
| [PRSNL_LOC_RELTN](PRSNL_LOC_RELTN.md) | `LOC_BUILDING_CD` |
| [PRSNL_LOC_RELTN](PRSNL_LOC_RELTN.md) | `LOC_FACILITY_CD` |
| [PRSNL_LOC_RELTN](PRSNL_LOC_RELTN.md) | `LOC_NURSE_UNIT_CD` |
| [PRSNL_LOC_RELTN](PRSNL_LOC_RELTN.md) | `LOC_ROOM_CD` |
| [RAD_PROTOCOL_CONFIG](RAD_PROTOCOL_CONFIG.md) | `FACILITY_CD` |
| [RAD_REPORT](RAD_REPORT.md) | `PERF_LOC_CD` |
| [RAD_TRANS_ROOM_REL](RAD_TRANS_ROOM_REL.md) | `LOCATION_CD` |
| [RAD_VDI_PACS_FACILITY](RAD_VDI_PACS_FACILITY.md) | `FACILITY_CD` |
| [RC_CLOUD_SYNC](RC_CLOUD_SYNC.md) | `LOCATION_CD` |
| [REFERRAL](REFERRAL.md) | `REFER_FROM_LOC_CD` |
| [ROBOTICS_ITEMS](ROBOTICS_ITEMS.md) | `LOGIN_LOC_CD` |
| [ROOM](ROOM.md) | `LOCATION_CD` |
| [RXS_ACTIVITY_INDEX](RXS_ACTIVITY_INDEX.md) | `CLUSTER_CD` |
| [RXS_ACTIVITY_INDEX](RXS_ACTIVITY_INDEX.md) | `LOCATION_CD` |
| [RXS_ACTIVITY_INDEX](RXS_ACTIVITY_INDEX.md) | `LOCATOR_CD` |
| [RXS_ALERT](RXS_ALERT.md) | `LOCATOR_CD` |
| [RXS_ALERT](RXS_ALERT.md) | `OWNER_FACILITY_CD` |
| [RXS_ALERT_LOC_RELTN](RXS_ALERT_LOC_RELTN.md) | `SVC_LOC_CD` |
| [RXS_EXTENDED_COUNT_PROP](RXS_EXTENDED_COUNT_PROP.md) | `LOCATION_CD` |
| [RXS_FOREIGN_DEVICE_ALERT](RXS_FOREIGN_DEVICE_ALERT.md) | `DEVICE_LOC_CD` |
| [RXS_FOREIGN_DEVICE_ALERT](RXS_FOREIGN_DEVICE_ALERT.md) | `FACILITY_CD` |
| [RXS_FOREIGN_DEVICE_ALERT](RXS_FOREIGN_DEVICE_ALERT.md) | `NURSE_UNIT_CD` |
| [RXS_GROUP_LOCATION_RELTN](RXS_GROUP_LOCATION_RELTN.md) | `LOCATION_CD` |
| [RXS_ITEM_COUNTBACK](RXS_ITEM_COUNTBACK.md) | `CLUSTER_CD` |
| [RXS_ITEM_COUNTBACK](RXS_ITEM_COUNTBACK.md) | `FACILITY_CD` |
| [RXS_ITEM_COUNTBACK](RXS_ITEM_COUNTBACK.md) | `LOCATION_CD` |
| [RXS_ITEM_COUNTBACK](RXS_ITEM_COUNTBACK.md) | `LOCATOR_CD` |
| [RXS_LAST_LOCATOR_ACTIVITY](RXS_LAST_LOCATOR_ACTIVITY.md) | `CLUSTER_CD` |
| [RXS_LAST_LOCATOR_ACTIVITY](RXS_LAST_LOCATOR_ACTIVITY.md) | `LOCATION_CD` |
| [RXS_LAST_LOCATOR_ACTIVITY](RXS_LAST_LOCATOR_ACTIVITY.md) | `LOCATOR_CD` |
| [RXS_LOCATION_TASK](RXS_LOCATION_TASK.md) | `CLUSTER_CD` |
| [RXS_LOCATION_TASK](RXS_LOCATION_TASK.md) | `FACILITY_CD` |
| [RXS_LOCATION_TASK](RXS_LOCATION_TASK.md) | `FILL_LOCATION_CD` |
| [RXS_LOCATION_TASK](RXS_LOCATION_TASK.md) | `LOCATION_CD` |
| [RXS_LOCATION_TASK](RXS_LOCATION_TASK.md) | `LOCATOR_CD` |
| [RXS_LOCATOR_ENCNTR](RXS_LOCATOR_ENCNTR.md) | `CLUSTER_CD` |
| [RXS_LOCATOR_ENCNTR](RXS_LOCATOR_ENCNTR.md) | `LOCATION_CD` |
| [RXS_LOCATOR_ENCNTR](RXS_LOCATOR_ENCNTR.md) | `LOCATOR_CD` |
| [RXS_LOC_ACCESS_CONFIG](RXS_LOC_ACCESS_CONFIG.md) | `LOC_CD` |
| [RXS_LOC_ATTR](RXS_LOC_ATTR.md) | `LOC_CD` |
| [RXS_LOC_SR_EVENT_RELTN](RXS_LOC_SR_EVENT_RELTN.md) | `LOCATION_CD` |
| [RXS_WORKLIST_LOCATION_R](RXS_WORKLIST_LOCATION_R.md) | `LOC_CD` |
| [RX_EXT_ORD_PRD_SYNC_RUN](RX_EXT_ORD_PRD_SYNC_RUN.md) | `FACILITY_CD` |
| [RX_IMAGE](RX_IMAGE.md) | `DEVICE_FAC_CD` |
| [RX_IMAGE](RX_IMAGE.md) | `DEVICE_LOC_CD` |
| [RX_IMAGE_QUEUE_LOC_RELTN](RX_IMAGE_QUEUE_LOC_RELTN.md) | `LOCATION_CD` |
| [RX_LOC_RESOURCE_RELTN](RX_LOC_RESOURCE_RELTN.md) | `LOCATION_CD` |
| [RX_MED_ORD_DETAIL](RX_MED_ORD_DETAIL.md) | `FACILITY_CD` |
| [RX_PENDING_CREDIT](RX_PENDING_CREDIT.md) | `PATIENT_FACILITY_CD` |
| [RX_PENDING_CREDIT](RX_PENDING_CREDIT.md) | `PATIENT_NURSE_UNIT_CD` |
| [RX_PENDING_REFILL](RX_PENDING_REFILL.md) | `NURSE_UNIT_CD` |
| [RX_PERSON_OWE](RX_PERSON_OWE.md) | `DISPENSE_FROM_CD` |
| [RX_PERSON_OWE](RX_PERSON_OWE.md) | `INVENTORY_LOCATION_CD` |
| [RX_REFILL_HX](RX_REFILL_HX.md) | `NURSE_UNIT_CD` |
| [RX_THERAP_SBSTTN_FROM](RX_THERAP_SBSTTN_FROM.md) | `FACILITY_CD` |
| [RX_VIEW_CONFIG_DETAIL](RX_VIEW_CONFIG_DETAIL.md) | `FACILITY_CD` |
| [RX_WORK_ITEM_QUEUE](RX_WORK_ITEM_QUEUE.md) | `FACILITY_CD` |
| [RX_WORK_ITEM_QUEUE](RX_WORK_ITEM_QUEUE.md) | `NURSE_UNIT_CD` |
| [RX_WS_FAC_RELTN](RX_WS_FAC_RELTN.md) | `FAC_CD` |
| [RX_WS_FAC_RELTN_HX](RX_WS_FAC_RELTN_HX.md) | `FAC_CD` |
| [SCH_ACTION_LOC](SCH_ACTION_LOC.md) | `LOCATION_CD` |
| [SCH_APPT](SCH_APPT.md) | `APPT_LOCATION_CD` |
| [SCH_APPT](SCH_APPT.md) | `TEMPLATE_LOCATION_CD` |
| [SCH_APPT_COMP](SCH_APPT_COMP.md) | `LOCATION_CD` |
| [SCH_APPT_INTER](SCH_APPT_INTER.md) | `LOCATION_CD` |
| [SCH_APPT_LOC](SCH_APPT_LOC.md) | `LOCATION_CD` |
| [SCH_APPT_NOTIFY](SCH_APPT_NOTIFY.md) | `LOCATION_CD` |
| [SCH_APPT_OPTION_CONFIG](SCH_APPT_OPTION_CONFIG.md) | `LOCATION_CD` |
| [SCH_APPT_ROUTING](SCH_APPT_ROUTING.md) | `LOCATION_CD` |
| [SCH_AUTO_MSG](SCH_AUTO_MSG.md) | `LOCATION_CD` |
| [SCH_BOOKING](SCH_BOOKING.md) | `LOCATION_CD` |
| [SCH_CAB_SERVICE](SCH_CAB_SERVICE.md) | `LOCATION_CD` |
| [SCH_COMP_LOC](SCH_COMP_LOC.md) | `COMP_LOCATION_CD` |
| [SCH_COMP_LOC](SCH_COMP_LOC.md) | `LOCATION_CD` |
| [SCH_DEF_APPLY](SCH_DEF_APPLY.md) | `LOCATION_CD` |
| [SCH_DEF_LOC_R](SCH_DEF_LOC_R.md) | `LOCATION_CD` |
| [SCH_GENERIC_LOC](SCH_GENERIC_LOC.md) | `LOCATION_CD` |
| [SCH_LIST_LOC](SCH_LIST_LOC.md) | `LOCATION_CD` |
| [SCH_LOCATION](SCH_LOCATION.md) | `LOCATION_CD` |
| [SCH_LOC_BOOKING](SCH_LOC_BOOKING.md) | `BED_CD` |
| [SCH_LOC_BOOKING](SCH_LOC_BOOKING.md) | `BUILDING_CD` |
| [SCH_LOC_BOOKING](SCH_LOC_BOOKING.md) | `FACILITY_CD` |
| [SCH_LOC_BOOKING](SCH_LOC_BOOKING.md) | `NURSE_UNIT_CD` |
| [SCH_LOC_BOOKING](SCH_LOC_BOOKING.md) | `ROOM_CD` |
| [SCH_LOC_QUOTA](SCH_LOC_QUOTA.md) | `LOCATION_CD` |
| [SCH_MESSAGING](SCH_MESSAGING.md) | `LOCATION_CD` |
| [SCH_ORDER_INTER](SCH_ORDER_INTER.md) | `LOCATION_CD` |
| [SCH_ORDER_LOC](SCH_ORDER_LOC.md) | `LOCATION_CD` |
| [SCH_ORDER_ROLE](SCH_ORDER_ROLE.md) | `LOCATION_CD` |
| [SCH_PEND_APPT](SCH_PEND_APPT.md) | `LOCATION_CD` |
| [SCH_PEND_ENCNTR_DETAIL](SCH_PEND_ENCNTR_DETAIL.md) | `LOCATION_CD` |
| [SCH_PEND_LOC](SCH_PEND_LOC.md) | `LOCATION_CD` |
| [SCH_RESOURCE](SCH_RESOURCE.md) | `ITEM_LOCATION_CD` |
| [SCH_RESOURCE_LIST](SCH_RESOURCE_LIST.md) | `LOCATION_CD` |
| [SCH_UNIT_ACTIVITY](SCH_UNIT_ACTIVITY.md) | `LOCATION_CD` |
| [SCH_UNIT_PHASE_SCHEDULE](SCH_UNIT_PHASE_SCHEDULE.md) | `LOCATION_CD` |
| [SERVICE_RESOURCE](SERVICE_RESOURCE.md) | `LOCATION_CD` |
| [SN_PICKLIST_LOC_STATUS](SN_PICKLIST_LOC_STATUS.md) | `LOCATION_CD` |
| [SN_TISSUE_WORKFLOW](SN_TISSUE_WORKFLOW.md) | `LOCATION_CD` |
| [SPEC_LBL_PRINTER_DEF](SPEC_LBL_PRINTER_DEF.md) | `LOCATION_CD` |
| [TRACKING_ITEM](TRACKING_ITEM.md) | `BASE_LOC_CD` |
| [WF_STFG_HDR](WF_STFG_HDR.md) | `LOCATION_CD` |
| [WF_STFG_REQ](WF_STFG_REQ.md) | `LOCATION_CD` |

