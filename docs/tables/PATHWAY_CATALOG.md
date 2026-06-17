# PATHWAY_CATALOG

> Pathway Catalog contains all of the pathway reference definitions.

**Description:** PATHWAY CATALOG  
**Table type:** REFERENCE  
**Primary key:** `PATHWAY_CATALOG_ID`  
**Columns:** 71  
**Referenced by:** 21 columns

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ACTIVE_IND` | DOUBLE |  |  | The table row is active or inactive. A row is generally active unless it is in an inactive state such as logically deleted, combined away, pending purge, etc. |
| 2 | `AGE_UNITS_CD` | DOUBLE | NOT NULL |  | The default time unit of measure used for time frames associated with this pathway. |
| 3 | `ALERTS_ON_PLAN_IND` | DOUBLE | NOT NULL |  | Phase level attribute to indicate whether to show alerts upon signing of a phase into a planned phase. Alerts include Interaction Checking, Discern Alerts and Dose Calculator. |
| 4 | `ALERTS_ON_PLAN_UPD_IND` | DOUBLE | NOT NULL |  | Phase level attribute to indicate whether to show alerts upon subsequent phase signing of a phase into a planned phase. Alerts include Interaction Checking, Discern Alerts and Dose Calculator. |
| 5 | `ALLOW_COPY_FORWARD_IND` | DOUBLE | NOT NULL |  | Used to indicate whether a plan is eligible to be copied forward from previous administration |
| 6 | `AUTO_INITIATE_IND` | DOUBLE | NOT NULL |  | Phase level attribute to indicate whether to initiate the phase of the plan upon signing of a phase for the first time. |
| 7 | `BEG_EFFECTIVE_DT_TM` | DATETIME |  |  | The date and time for which this table row becomes effective. Normally, this will be the date and time the row is added, but could be a past or future date and time. |
| 8 | `COMP_FORMS_REF_ID` | DOUBLE | NOT NULL | FK→ | Id from the dcp_forms_ref table of the form that will be used to capture component level variances for this pathway. |
| 9 | `CONCEPT_CKI` | VARCHAR(255) |  |  | Unique CKI identifier |
| 10 | `CROSS_ENCNTR_IND` | DOUBLE | NOT NULL |  | Indicates the pathway is designed to be activated across multiple encounters. These pathways will not automatically be discontinued upon discharge of the patient. |
| 11 | `CYCLE_BEGIN_NBR` | DOUBLE | NOT NULL |  | Indicates number to be used to default for the begin cycle number while ordering the plan if the same plan is not ordered on the patient within 180 days. If this is valued, cycle_end_nbr will also be valued. |
| 12 | `CYCLE_DISPLAY_END_IND` | DOUBLE | NOT NULL |  | Indicates whether users can see the Standard Cycle Number or End Value in the application while ordering or modifying the plan cycle information. |
| 13 | `CYCLE_END_NBR` | DOUBLE | NOT NULL |  | Indicates number to be used to default for the end cycle number while ordering the plan if the same plan is not ordered on the patient within 180 days. If this is valued, cycle_begin_nbr will also be valued. |
| 14 | `CYCLE_INCREMENT_NBR` | DOUBLE | NOT NULL |  | Indicates number to be used to increment plan cycle number instead of the default value of one. |
| 15 | `CYCLE_IND` | DOUBLE | NOT NULL |  | This field is used to prompt the user for a cycle number for the plan when it is ordered. |
| 16 | `CYCLE_LABEL_CD` | DOUBLE | NOT NULL |  | Indicates the default "Cycle" label to show client defined values such as Week, Course, Etc |
| 17 | `CYCLE_LOCK_END_IND` | DOUBLE | NOT NULL |  | Indicates whether users can modify the Standard Cycle Number or End Value in the application while ordering or modifying the plan cycle information. This field can have the value of one only when the cycle_display_end_ind is set. |
| 18 | `DEFAULT_ACTION_INPT_FUTURE_CD` | DOUBLE | NOT NULL |  | Indicates default phase action to be used while selecting plan for the inpatient encounter type for future visit type. When optional_ind is set on the Phase, values can be Order now, Plan for later, Order for future visit and Do not order. When optional_ind is not set on the Phase or is a single phase plan, values can be Order now, Plan for later, and Order for future visit. Do not order is not available. Code Set is 4002320. |
| 19 | `DEFAULT_ACTION_INPT_NOW_CD` | DOUBLE | NOT NULL |  | Indicates default phase action to be used while selecting plan for the inpatient encounter type for this visit type. When optional_ind is set on the Phase, values can be Order now, Plan for later and Do not order. When optional_ind is not set on the Phase or is a single phase plan, values can be Order now, Plan for later. Do not order is not available. Code Set is 4002320. |
| 20 | `DEFAULT_ACTION_OUTPT_FUTURE_CD` | DOUBLE | NOT NULL |  | Indicates default phase action to be used while selecting plan for the outpatient encounter type for future visit type. When optional_ind is set on the Phase, values can be Order now, Plan for later, Order for future visit and Do not order. When optional_ind is not set on the Phase or is a single phase plan, values can be Order now, Plan for later, and Order for future visit. Do not order is not available. Code Set is 4002320. |
| 21 | `DEFAULT_ACTION_OUTPT_NOW_CD` | DOUBLE | NOT NULL |  | Indicates default phase action to be used while selecting plan for the outpatient encounter type for this visit type. When optional_ind is set on the Phase, values can be Order now, Plan for later and Do not order. When optional_ind is not set on the Phase or is a single phase plan, values can be Order now, Plan for later. Do not order is not available. Code Set is 4002320. |
| 22 | `DEFAULT_START_TIME_TXT` | VARCHAR(10) |  |  | THE DEFAULT START TIME FOR THE PHASE |
| 23 | `DEFAULT_VIEW_MEAN` | VARCHAR(12) | NOT NULL |  | This field is used to set the default view for the plan in the application. |
| 24 | `DEFAULT_VISIT_TYPE_FLAG` | DOUBLE | NOT NULL |  | Defaults Phase actions during plan selection based on the visit type 0 - None 1 - This Visit 2 - Future Inpatient 3 - Future Outpatient |
| 25 | `DESCRIPTION` | VARCHAR(100) | NOT NULL |  | description of the pathway |
| 26 | `DESCRIPTION_KEY` | VARCHAR(100) | NOT NULL |  | Description key |
| 27 | `DESCRIPTION_KEY_A_NLS` | VARCHAR(400) |  |  | DESCRIPTION_KEY_A_NLS column |
| 28 | `DESCRIPTION_KEY_NLS` | VARCHAR(202) |  |  | Description key used for international sites |
| 29 | `DIAGNOSIS_CAPTURE_IND` | DOUBLE | NOT NULL |  | This field is used to prompt the user to enter the diagnosis for the plan. |
| 30 | `DISABLE_ACTIVATE_ALL_IND` | DOUBLE | NOT NULL |  | This column indicates whether the Activate All button for DoT phases needs to be enabled or disabled. |
| 31 | `DISPLAY_DESCRIPTION` | VARCHAR(100) |  |  | User visible display value of plan name |
| 32 | `DISPLAY_METHOD_CD` | DOUBLE | NOT NULL |  | Code value field used to flex plan component display in the application. |
| 33 | `DURATION_QTY` | DOUBLE |  |  | Duration quantity for plans and phases that have a specified duration. |
| 34 | `DURATION_UNIT_CD` | DOUBLE | NOT NULL |  | Identifies the duration unit (Minutes, Hours, Days). |
| 35 | `END_EFFECTIVE_DT_TM` | DATETIME | NOT NULL |  | The date/time after which the row is no longer valid as active current data. This may be valued with the date that the row became inactive. |
| 36 | `FUTURE_IND` | DOUBLE | NOT NULL |  | FUTURE INDICATOR |
| 37 | `HIDE_FLEXED_COMP_IND` | DOUBLE | NOT NULL |  | This indicator controls whether or not components that are unavailable for current encounter due to facility flexing are loaded by the application |
| 38 | `LINKED_PHASE_IND` | DOUBLE | NOT NULL |  | This indicator synchronizes the start date-time of the phases within a multi-phase plan. i.e.changing the start date-time of a linked phase within the multi-phase plan will update the start date-time of the another linked phase within the same plan. |
| 39 | `LONG_TEXT_ID` | DOUBLE | NOT NULL |  | Id of the textual comments associated with this pathway |
| 40 | `OPEN_BY_DEFAULT_IND` | DOUBLE | NOT NULL |  | The column indicates whether all the phases, or a phase, is open by default. |
| 41 | `OPTIONAL_IND` | DOUBLE | NOT NULL |  | Indicates that phase can be removed from the plan in the application during plan selection. |
| 42 | `OVERRIDE_MRD_ON_PLAN_IND` | DOUBLE | NOT NULL |  | Indicates to allow missing required detail upon signing of a plan into a planned status when the preference: planmissingrequireddetailswarnonsign is set to 2 |
| 43 | `PATHWAY_CATALOG_ID` | DOUBLE | NOT NULL | PK | Unique id of this pathway catalog entry |
| 44 | `PATHWAY_CLASS_CD` | DOUBLE | NOT NULL |  | Code value field used to group pathways according to user-defined classification |
| 45 | `PATHWAY_TYPE_CD` | DOUBLE | NOT NULL |  | Code value field used to group pathways according to user-defined types |
| 46 | `PATHWAY_UUID` | VARCHAR(255) | NOT NULL |  | The pathway unique universal identifier |
| 47 | `PERIOD_CUSTOM_LABEL` | VARCHAR(40) |  |  | The custom label used to create the description of any treatment periods belonging to this phase. |
| 48 | `PERIOD_NBR` | DOUBLE | NOT NULL |  | The period number for a treatment period phase. |
| 49 | `PRIMARY_IND` | DOUBLE | NOT NULL |  | indicates which phase of a multiphase plan will be the primary phase in the plan prompt dialog. The target for the start date time control in the plan prompt. |
| 50 | `PROMPT_ON_SELECTION_IND` | DOUBLE | NOT NULL |  | Indicates whether to prompt user for plan start information on plan selection |
| 51 | `PROVIDER_PROMPT_IND` | DOUBLE | NOT NULL |  | Indicator to prompt for ordering provider. |
| 52 | `PW_FORMS_REF_ID` | DOUBLE | NOT NULL | FK→ | Id from the dcp_forms_ref table of the form that will be used to capture PW level variances for this pathway. |
| 53 | `REF_OWNER_PERSON_ID` | DOUBLE | NOT NULL |  | Unique id from the person table that identifies the personnel who created and owns the reference plan from the pathway_catalog table. |
| 54 | `RESCHEDULE_REASON_ACCEPT_FLAG` | DOUBLE | NOT NULL |  | This value indicates whether the capture of a phase/treatment period reschedule reason will be: 0 - Off, 1 - Optional, or 2 - Required |
| 55 | `RESTRICTED_ACTIONS_BITMASK` | DOUBLE | NOT NULL |  | The bitmask for the restricted actions for a plan. The following values are supported: 0x0 - No restriction, 0x1 - Restricted from being ordered as a plan proposal, 0x2 - Restricted from being saved as favorite on the profile, ;0x4 - Restricted from being searched. |
| 56 | `RESTRICT_CC_ADD_IND` | DOUBLE |  |  | Indicator used to restrict the ability to add categories of care to the pathway when the pathway is being ordered on a patient |
| 57 | `RESTRICT_COMP_ADD_IND` | DOUBLE |  |  | Indicator used to restrict the ability to add components to the pathway when the pathway is being ordered on a patient |
| 58 | `RESTRICT_TF_ADD_IND` | DOUBLE |  |  | Indicator used to restrict the ability to add time frames to the pathway when the pathway is being ordered on a patient |
| 59 | `REVIEW_REQUIRED_SIG_COUNT` | DOUBLE | NOT NULL |  | The number of signatures that will be required to complete protocol review for this phase. |
| 60 | `ROUTE_FOR_REVIEW_IND` | DOUBLE | NOT NULL |  | ** OBSOLETE ** - 0 - for no routing is needed for the phase 1 - routing is required** THIS COLUMN BECOMES OBSOLETE WHEN COLUMN REVIEW_REQUIRED_SIG_COUNT IS ADDED TO THE TABLE. (June 2016) |
| 61 | `STANDARD_CYCLE_NBR` | DOUBLE | NOT NULL |  | This field is used to validate the cycle number entered by the user against the standard. |
| 62 | `SUB_PHASE_IND` | DOUBLE | NOT NULL |  | This indicator signals whether or not a single phase plan can be used as a sub phase in another plan. |
| 63 | `TYPE_MEAN` | VARCHAR(12) |  |  | Meaning that indicates the type of entry on the pathway catalog table. |
| 64 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 65 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 66 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 67 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 68 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 69 | `VERSION` | DOUBLE | NOT NULL |  | Number used to indicate the version of the pathway. Everytime the pathway catalog entry is modified the version is incremented. |
| 70 | `VERSION_PW_CAT_ID` | DOUBLE | NOT NULL |  | The id of the pathway catalog entry that this entry is a past version of. This will only be filled out for entries that are past versions of a pathway catalog entry. |
| 71 | `VERSION_TEXT_ID` | DOUBLE | NOT NULL |  | User entered description of the changes made to a reference pathway when creating a new version. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `COMP_FORMS_REF_ID` | [DCP_FORMS_REF](DCP_FORMS_REF.md) | `DCP_FORM_INSTANCE_ID` |
| `PW_FORMS_REF_ID` | [DCP_FORMS_REF](DCP_FORMS_REF.md) | `DCP_FORM_INSTANCE_ID` |

## Referenced by (21)

| From table | Column |
|------------|--------|
| [ALT_SEL_LIST](ALT_SEL_LIST.md) | `PATHWAY_CATALOG_ID` |
| [ORDERS](ORDERS.md) | `PATHWAY_CATALOG_ID` |
| [PATHWAY](PATHWAY.md) | `PATHWAY_CATALOG_ID` |
| [PATHWAY](PATHWAY.md) | `PW_CAT_GROUP_ID` |
| [PATHWAY_ACTION](PATHWAY_ACTION.md) | `PATHWAY_CATALOG_ID` |
| [PATHWAY_COMP](PATHWAY_COMP.md) | `PATHWAY_CATALOG_ID` |
| [PATHWAY_CUSTOMIZED_NOTIFY](PATHWAY_CUSTOMIZED_NOTIFY.md) | `PATHWAY_CATALOG_ID` |
| [PATHWAY_CUSTOMIZED_NOTIFY](PATHWAY_CUSTOMIZED_NOTIFY.md) | `VERSION_PW_CAT_ID` |
| [PATHWAY_CUSTOMIZED_PLAN](PATHWAY_CUSTOMIZED_PLAN.md) | `PATHWAY_CATALOG_ID` |
| [PRECOMPONENT_ORDER_RELTN](PRECOMPONENT_ORDER_RELTN.md) | `VERSION_PW_CAT_ID` |
| [PW_CAT_FLEX](PW_CAT_FLEX.md) | `PATHWAY_CATALOG_ID` |
| [PW_CAT_RELTN](PW_CAT_RELTN.md) | `PW_CAT_S_ID` |
| [PW_CAT_RELTN](PW_CAT_RELTN.md) | `PW_CAT_T_ID` |
| [PW_CAT_SYNONYM](PW_CAT_SYNONYM.md) | `PATHWAY_CATALOG_ID` |
| [PW_COMP_CAT_RELTN](PW_COMP_CAT_RELTN.md) | `PATHWAY_CATALOG_ID` |
| [PW_COMP_GROUP](PW_COMP_GROUP.md) | `PATHWAY_CATALOG_ID` |
| [PW_COMP_RELTN](PW_COMP_RELTN.md) | `PATHWAY_CATALOG_ID` |
| [PW_EVIDENCE_RELTN](PW_EVIDENCE_RELTN.md) | `PATHWAY_CATALOG_ID` |
| [PW_MAINTENANCE_CRITERIA](PW_MAINTENANCE_CRITERIA.md) | `VERSION_PW_CAT_ID` |
| [PW_PT_RELTN](PW_PT_RELTN.md) | `PATHWAY_CATALOG_ID` |
| [SURG_REQ_PLAN_R](SURG_REQ_PLAN_R.md) | `PATHWAY_CATALOG_ID` |

