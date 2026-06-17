# PATHWAY

> Pathway activity table

**Description:** Pathway  
**Table type:** ACTIVITY  
**Primary key:** `PATHWAY_ID`  
**Columns:** 75  
**Referenced by:** 13 columns

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ACTIVE_IND` | DOUBLE |  |  | The table row is active or inactive. A row is generally active unless it is in an inactive state such as logically deleted, combined away, pending purge, etc. |
| 2 | `ACTUAL_END_DT_TM` | DATETIME |  |  | Date and time the pathway ended. |
| 3 | `AGE_UNITS_CD` | DOUBLE | NOT NULL |  | The default time unit of measure used for time frames associated with this pathway. |
| 4 | `ALERTS_ON_PLAN_IND` | DOUBLE | NOT NULL |  | Phase level attribute to indicate whether to show alerts upon signing of a phase into a planned phase. Alerts include Interaction Checking, Discern Alerts and Dose Calculator. |
| 5 | `ALERTS_ON_PLAN_UPD_IND` | DOUBLE | NOT NULL |  | Phase level attribute to indicate whether to show alerts upon subsequent phase signing of a phase into a planned phase. Alerts include Interaction Checking, Discern Alerts and Dose Calculator. |
| 6 | `BEG_EFFECTIVE_DT_TM` | DATETIME |  |  | The date and time for which this table row becomes effective. Normally, this will be the date and time the row is added, but could be a past or future date and time. |
| 7 | `CALC_END_DT_TM` | DATETIME |  |  | Calculated end date and time of the pathway. |
| 8 | `CALC_END_ESTIMATED_IND` | DOUBLE | NOT NULL |  | To indicate whether the phase end date time is estimated or precise. |
| 9 | `CALC_END_TZ` | DOUBLE |  |  | Time zone associated with the corresponding dt_tm column. |
| 10 | `COMP_FORMS_REF_ID` | DOUBLE | NOT NULL | FK→ | Id from the dcp_forms_ref table of the form that will be used to capture component level variances for this pathway. |
| 11 | `COPY_SOURCE_PATHWAY_ID` | DOUBLE | NOT NULL | FK→ | copy of source pathway id originated from copy DoT. This value only populates when Pathway row is being created from Copy Dot workflow. For all other cases the COPY_SOURCE_PATHWAY_ID will be zero. |
| 12 | `CROSS_ENCNTR_IND` | DOUBLE | NOT NULL |  | Indicates the pathway is designed to be activated across multiple encounters. These pathways will not automatically be discontinued upon discharge of the patient. |
| 13 | `CYCLE_END_NBR` | DOUBLE | NOT NULL |  | Indicates number to be used to default for the end cycle number while ordering the plan if the same plan is not ordered on the patient within 180 days. |
| 14 | `CYCLE_LABEL_CD` | DOUBLE | NOT NULL |  | Indicates the default "Cycle" label to show client defined values such as Week, Course, Etc. Code set 4002313 |
| 15 | `CYCLE_NBR` | DOUBLE | NOT NULL |  | This field is used to store the cycle number for the plan. |
| 16 | `DC_REASON_CD` | DOUBLE | NOT NULL |  | Pathway discontinue reason code |
| 17 | `DC_TEXT_ID` | DOUBLE | NOT NULL |  | Id of the text that represents the free textdiscontinue reason. |
| 18 | `DEFAULT_VIEW_MEAN` | VARCHAR(12) | NOT NULL |  | This field is used to store the default view for the plan. |
| 19 | `DESCRIPTION` | VARCHAR(1000) | NOT NULL |  | Pathway description |
| 20 | `DIAGNOSIS_CAPTURE_IND` | DOUBLE | NOT NULL |  | This field is used to prompt the user to enter the diagnosis for the plan. |
| 21 | `DISCONTINUED_DT_TM` | DATETIME |  |  | Date and time the pathway was discontinued |
| 22 | `DISCONTINUED_IND` | DOUBLE |  |  | Indicates the pathway is dicontinued |
| 23 | `DISCONTINUED_TZ` | DOUBLE |  |  | Time zone associated with the corresponding dt_tm column. |
| 24 | `DISPLAY_METHOD_CD` | DOUBLE | NOT NULL |  | Code value field used to flex plan component display in the application. |
| 25 | `DURATION_QTY` | DOUBLE |  |  | Duration quantity for plans and phases that have a specified duration. |
| 26 | `DURATION_UNIT_CD` | DOUBLE | NOT NULL |  | Identifies the duration unit (Minutes, Hours, Days). |
| 27 | `ENCNTR_ID` | DOUBLE | NOT NULL | FK→ | This is the value of the unique primary identifier of the encounter table. It is an internal system assigned number. |
| 28 | `ENDED_IND` | DOUBLE |  |  | Indicates the pathway has ended |
| 29 | `END_EFFECTIVE_DT_TM` | DATETIME | NOT NULL |  | The date/time after which the row is no longer valid as active current data. This may be valued with the date that the row became inactive. |
| 30 | `FUTURE_LOCATION_FACILITY_CD` | DOUBLE | NOT NULL |  | FUTURE LOCATION |
| 31 | `FUTURE_LOCATION_NURSE_UNIT_CD` | DOUBLE | NOT NULL |  | FUTURE NURSE LOCATION |
| 32 | `LAST_ACTION_SEQ` | DOUBLE |  |  | Sequence of the last action for the pathway |
| 33 | `LINKED_PHASE_IND` | DOUBLE | NOT NULL |  | This indicator synchronizes the start date-time of the phases within a multi-phase plan. i.e.changing the start date-time of a linked phase within the multi-phase plan will update the start date-time of the another linked phase within the same plan. |
| 34 | `LONG_TEXT_ID` | DOUBLE | NOT NULL |  | Id of the textual comments associated with this pathway |
| 35 | `ORDER_DT_TM` | DATETIME |  |  | Date and time the pathway was ordered |
| 36 | `ORDER_TZ` | DOUBLE |  |  | Time zone associated with the corresponding dt_tm column. |
| 37 | `PARENT_PHASE_DESC` | VARCHAR(100) |  |  | This field is used to store the display description of a parent phase for a sub phase. |
| 38 | `PATHWAY_CATALOG_ID` | DOUBLE | NOT NULL | FK→ | Id of the pathway catalog this pathway was created from |
| 39 | `PATHWAY_CLASS_CD` | DOUBLE | NOT NULL |  | Code value field used to group pathways according to user-defined classification |
| 40 | `PATHWAY_CUSTOMIZED_PLAN_ID` | DOUBLE | NOT NULL | FK→ | The unique identifier of the customized plan used to create the pathway |
| 41 | `PATHWAY_GROUP_ID` | DOUBLE | NOT NULL | FK→ | The pathway_id of the phase group's parent. |
| 42 | `PATHWAY_ID` | DOUBLE | NOT NULL | PK | Unique id of the pathway |
| 43 | `PATHWAY_TYPE_CD` | DOUBLE | NOT NULL |  | Code value field used to group pathways according to user-defined types |
| 44 | `PERIOD_CUSTOM_LABEL` | VARCHAR(40) |  |  | The custom label used to create the description of any treatment periods belonging to this phase. |
| 45 | `PERIOD_NBR` | DOUBLE | NOT NULL |  | The period number for a treatment period phase. |
| 46 | `PERSON_ID` | DOUBLE | NOT NULL | FK→ | This is the value of the unique primary identifier of the person table. It is an internal system assigned number. |
| 47 | `PW_CAT_GROUP_ID` | DOUBLE | NOT NULL | FK→ | Pathway catalog id for the group level pathway row on the pathway_catalog table. |
| 48 | `PW_CAT_VERSION` | DOUBLE |  |  | The version of the pathway catalog used to create this instance of the pathway on the activity table. |
| 49 | `PW_FORMS_REF_ID` | DOUBLE | NOT NULL | FK→ | Id from the dcp_forms_ref table of the form that will be used to capture PW level variances for this pathway. |
| 50 | `PW_GROUP_DESC` | VARCHAR(1000) |  |  | Description of the group level pathway. |
| 51 | `PW_GROUP_NBR` | DOUBLE |  |  | Unique id used to group multiple phases as a group to form a multi-phase pathway. |
| 52 | `PW_STATUS_CD` | DOUBLE | NOT NULL |  | Status code of the pathway |
| 53 | `REF_OWNER_PERSON_ID` | DOUBLE | NOT NULL |  | Unique id from the person table that identifies the personnel who created and owns the reference plan from the pathway_catalog table. |
| 54 | `RESTRICT_CC_ADD_IND` | DOUBLE |  |  | Indicator used to restrict the ability to add categories of care to the pathway when the pathway is being ordered on a patient |
| 55 | `RESTRICT_COMP_ADD_IND` | DOUBLE |  |  | Indicator used to restrict the ability to add components to the pathway when the pathway is being ordered on a patient |
| 56 | `RESTRICT_TF_ADD_IND` | DOUBLE |  |  | Indicator used to restrict the ability to add time frames to the pathway when the pathway is being ordered on a patient |
| 57 | `REVIEW_REQUIRED_SIG_COUNT` | DOUBLE | NOT NULL |  | The number of signatures that will be required to complete protocol review for this phase. |
| 58 | `REVIEW_STATUS_FLAG` | DOUBLE | NOT NULL |  | 0 - None 1 - Pending 2 - Completed 3 - Rejected 4 - Opt-Out 5 - Planning |
| 59 | `STARTED_IND` | DOUBLE |  |  | Indicates that the pathway has been started |
| 60 | `START_DT_TM` | DATETIME |  |  | Date and time the pathway was started |
| 61 | `START_ESTIMATED_IND` | DOUBLE | NOT NULL |  | To indicate whether the phase start date time is estimated or precise. |
| 62 | `START_TZ` | DOUBLE |  |  | Time zone associated with the corresponding dt_tm column. |
| 63 | `STATUS_DT_TM` | DATETIME | NOT NULL |  | Date and time the status was set to it's current value |
| 64 | `STATUS_PRSNL_ID` | DOUBLE | NOT NULL |  | Id of the person who last changed the status of the pathway |
| 65 | `STATUS_TZ` | DOUBLE |  |  | Time zone associated with the corresponding dt_tm column. |
| 66 | `SYNONYM_NAME` | VARCHAR(200) |  |  | Plan Synonym used when the pathway entry was added |
| 67 | `TYPE_MEAN` | VARCHAR(12) |  |  | Meaning that indicates the type of entry on the pathway table. |
| 68 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 69 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 70 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 71 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 72 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 73 | `VERSION` | DOUBLE |  |  | Version number of the pathway |
| 74 | `VERSION_PATHWAY_ID` | DOUBLE | NOT NULL |  | The id of the pathway that this entry is a past version of. This will only be filled out for entries that are past versions of a pathway. |
| 75 | `WARNING_LEVEL_BIT` | DOUBLE | NOT NULL |  | A bitmask which indicates if the phase has a warning associated to it. If the bitmask is 0, no warning is associated to the phase. If the mask is valued, it indicates that a warning is associated to the phase. The 0th bit represents the presence of data separated by the encounter move process. Other bits will be defined in future releases. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `COMP_FORMS_REF_ID` | [DCP_FORMS_REF](DCP_FORMS_REF.md) | `DCP_FORM_INSTANCE_ID` |
| `COPY_SOURCE_PATHWAY_ID` | [PATHWAY](PATHWAY.md) | `PATHWAY_ID` |
| `ENCNTR_ID` | [ENCOUNTER](ENCOUNTER.md) | `ENCNTR_ID` |
| `PATHWAY_CATALOG_ID` | [PATHWAY_CATALOG](PATHWAY_CATALOG.md) | `PATHWAY_CATALOG_ID` |
| `PATHWAY_CUSTOMIZED_PLAN_ID` | [PATHWAY_CUSTOMIZED_PLAN](PATHWAY_CUSTOMIZED_PLAN.md) | `PATHWAY_CUSTOMIZED_PLAN_ID` |
| `PATHWAY_GROUP_ID` | [PATHWAY](PATHWAY.md) | `PATHWAY_ID` |
| `PERSON_ID` | [PERSON](PERSON.md) | `PERSON_ID` |
| `PW_CAT_GROUP_ID` | [PATHWAY_CATALOG](PATHWAY_CATALOG.md) | `PATHWAY_CATALOG_ID` |
| `PW_FORMS_REF_ID` | [DCP_FORMS_REF](DCP_FORMS_REF.md) | `DCP_FORM_INSTANCE_ID` |

## Referenced by (13)

| From table | Column |
|------------|--------|
| [ACT_PW_COMP](ACT_PW_COMP.md) | `PATHWAY_ID` |
| [ACT_PW_COMP_G](ACT_PW_COMP_G.md) | `PATHWAY_ID` |
| [ACT_PW_COMP_R](ACT_PW_COMP_R.md) | `PATHWAY_ID` |
| [PATHWAY](PATHWAY.md) | `COPY_SOURCE_PATHWAY_ID` |
| [PATHWAY](PATHWAY.md) | `PATHWAY_GROUP_ID` |
| [PATHWAY_ACTION](PATHWAY_ACTION.md) | `PATHWAY_ID` |
| [PATHWAY_NOTIFICATION](PATHWAY_NOTIFICATION.md) | `PATHWAY_ID` |
| [PATHWAY_RELTN](PATHWAY_RELTN.md) | `PATHWAY_S_ID` |
| [PATHWAY_RELTN](PATHWAY_RELTN.md) | `PATHWAY_T_ID` |
| [PATHWAY_REVIEW](PATHWAY_REVIEW.md) | `PATHWAY_ID` |
| [PW_COMP_ACT_RELTN](PW_COMP_ACT_RELTN.md) | `PATHWAY_ID` |
| [PW_PROCESSING_ACTION](PW_PROCESSING_ACTION.md) | `PATHWAY_ID` |
| [PW_VARIANCE_RELTN](PW_VARIANCE_RELTN.md) | `PATHWAY_ID` |

