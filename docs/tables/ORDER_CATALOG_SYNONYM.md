# ORDER_CATALOG_SYNONYM

> Used to store all valid synonyms and their associated information for a given order catalog item

**Description:** Order catalog synonym  
**Table type:** REFERENCE  
**Primary key:** `SYNONYM_ID`  
**Columns:** 59  
**Referenced by:** 63 columns

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ACTIVE_IND` | DOUBLE |  |  | The table row is active or inactive. A row is generally active unless it is in an inactive state such as logically deleted, combined away, pending purge, etc. |
| 2 | `ACTIVE_STATUS_CD` | DOUBLE | NOT NULL |  | Indicates the status of the row itself (not the data in the row) such as active, inactive, combined away, pending purge, etc. |
| 3 | `ACTIVE_STATUS_DT_TM` | DATETIME |  |  | The date and time that the active_status_cd was set. |
| 4 | `ACTIVE_STATUS_PRSNL_ID` | DOUBLE | NOT NULL |  | The person who caused the active_status_cd to be set or change. |
| 5 | `ACTIVITY_SUBTYPE_CD` | DOUBLE | NOT NULL |  | Stores the code value for the activity sub-type that is used to filter order catalog items within activity type |
| 6 | `ACTIVITY_TYPE_CD` | DOUBLE | NOT NULL |  | Stores the code value for the activity type that is used to filter order catalog items within catalog type |
| 7 | `AUTHORIZATION_REVIEW_FLAG` | DOUBLE | NOT NULL |  | Used to store the flag that indicates what kind of stop type is assigned to the orderable.0 - None.1 - Indicator Only - No Status Updates. 2 - Indicator Only - With Status Updates (Current: No Alerts, Indicator Only). 3 - Alert - No Override Required. 4 - Alert - Override required. 5 - Authorization Required Prior to Start. |
| 8 | `AUTOPROG_SYN_IND` | DOUBLE | NOT NULL |  | Indicator if set symbolized that auto programming will happen at synonym level. If not set auto programming will happen at Catalog code level. |
| 9 | `CATALOG_CD` | DOUBLE | NOT NULL | FK→ | Order catalog number |
| 10 | `CATALOG_TYPE_CD` | DOUBLE | NOT NULL |  | Used to store the internal code for the catalog type. Used as a filtering mechanism for rows on the order catalog table |
| 11 | `CKI` | VARCHAR(255) |  |  | For meds process |
| 12 | `CONCENTRATION_STRENGTH` | DOUBLE |  |  | The strength value of the concentration ratio. |
| 13 | `CONCENTRATION_STRENGTH_UNIT_CD` | DOUBLE | NOT NULL |  | The code value that represents the unit of measure for the concentration strength attribute. |
| 14 | `CONCENTRATION_VOLUME` | DOUBLE |  |  | The volume value of the concentration ratio. |
| 15 | `CONCENTRATION_VOLUME_UNIT_CD` | DOUBLE | NOT NULL |  | The code value that represents the unit of measure for the concentration volume attribute. |
| 16 | `CONCEPT_CKI` | VARCHAR(255) |  |  | Concept CKI is the functional Concept Identifier; it is the codified means within Millennium to identify key medical concepts to support information processing, clinical decision support, executable knowledge and knowledge presentation. |
| 17 | `CS_INDEX_CD` | DOUBLE | NOT NULL |  | CareSet Index code |
| 18 | `DCP_CLIN_CAT_CD` | DOUBLE | NOT NULL |  | The clinical category of this orderable. |
| 19 | `DISPLAY_ADDITIVES_FIRST_IND` | DOUBLE | NOT NULL |  | Indicates whether or not this synonym (additive) should be displayed prior to the diluents in an IV. |
| 20 | `FILTERED_OD_IND` | DOUBLE |  |  | Indicates if any filtered order details have been set up against this synonym. |
| 21 | `HEALTH_PLAN_VIEW` | VARCHAR(255) |  |  | Each character in the field represent one health plan. The offset of the health plans is defined in dcp_entity_reltn table. The possible values for each char are: G (Green), W (White), Yellow (Y), R (Red). |
| 22 | `HIDE_FLAG` | DOUBLE |  |  | Flag indicating whether or not to hide this synonym |
| 23 | `HIGH_ALERT_IND` | DOUBLE | NOT NULL |  | A customized message that alerts the user when the order is being added to scratchpad. |
| 24 | `HIGH_ALERT_LONG_TEXT_ID` | DOUBLE | NOT NULL | FK→ | A pointer to the text displayed if this is a High Alert orderable. |
| 25 | `HIGH_ALERT_REQUIRED_NTFY_IND` | DOUBLE |  |  | Indicates if the high alert text should be presented to the user automatically. |
| 26 | `HRT_MEDICATION_IND` | DOUBLE |  |  | Indicates whether this synonym is used for Hormone Replacement Therapy. |
| 27 | `IGNORE_HIDE_CONVERT_IND` | DOUBLE | NOT NULL |  | Indicates if the hide flag can be ignored for convert to inpatient. |
| 28 | `INGREDIENT_RATE_CONVERSION_IND` | DOUBLE | NOT NULL |  | If the ingredient is eligible to have ingredient rate to total bag rate conversions and vice versa. If the indicator is set to 1, then orders that have this ingredient will be shown on the interactive view with an additive rate row and a total bag rate row. Similarly, the IV Charting window will require the user to validate the concentration, ingredient dose rate unit, and possibly weight in order to perform the conversions. |
| 29 | `INTERMITTENT_IND` | DOUBLE | NOT NULL |  | Indicates whether or not a synonym can be placed as an intermittent order. |
| 30 | `ITEM_ID` | DOUBLE | NOT NULL |  | The associated id of the item for this synonym. |
| 31 | `LAST_ADMIN_DISP_BASIS_FLAG` | DOUBLE | NOT NULL |  | Specifies at what level the med interval warnings should be performed at. 0 - Use System Default, 1 - Order Level, 2 - Event Code Level. |
| 32 | `LOCK_TARGET_DOSE_IND` | DOUBLE | NOT NULL |  | Lock target dose indicator. An indicator to lock the target dose in the dose calculator. |
| 33 | `MAX_DOSE_CALC_BSA_VALUE` | DOUBLE | NOT NULL |  | Contains the reference (upper-limit) for the BSA value for the synonym and is always measured in meter-squared. Has a (default) value of 0.0 denoting the absence of a reference. |
| 34 | `MAX_FINAL_DOSE` | DOUBLE | NOT NULL |  | Contains the reference (upper-limit) on the final-dose for the synonym. Has a (default) value of 0.0 denoting the absence of a reference. |
| 35 | `MAX_FINAL_DOSE_UNIT_CD` | DOUBLE | NOT NULL |  | Contains the unit of measurement for the reference (upper-limit) defined in MAX_FINAL_DOSE. Has a value of 0.0 if MAX_FINAL_DOSE contains 0.0. |
| 36 | `MED_INTERVAL_WARN_FLAG` | DOUBLE | NOT NULL |  | Specifies if med interval warnings should be displayed when a result is within the defined time range. 0 - Use System Default, 1 - Order Level, 2 - Event Code Level. |
| 37 | `MNEMONIC` | VARCHAR(200) |  |  | The display mnemonic of this orderable. |
| 38 | `MNEMONIC_KEY_CAP` | VARCHAR(200) |  |  | The key version of the mnemonic for this orderable. |
| 39 | `MNEMONIC_KEY_CAP_A_NLS` | VARCHAR(400) |  |  | MNEMONIC_KEY_CAP_A_NLS column |
| 40 | `MNEMONIC_KEY_CAP_NLS` | VARCHAR(405) |  |  | NLS Sort column for internationalization. |
| 41 | `MNEMONIC_TYPE_CD` | DOUBLE | NOT NULL |  | The type of mnemonic this is. |
| 42 | `MULTIPLE_ORD_SENT_IND` | DOUBLE |  |  | Indicator on whether or not this synonym has multiple order sentences associated with it. |
| 43 | `NOT_FOR_EPRESCRIBING_IND` | DOUBLE |  |  | Indicator to determine if this synonym should be restricted for eprescribing. |
| 44 | `OE_FORMAT_ID` | DOUBLE | NOT NULL |  | Used to store the internal identifier for the order entry format to be used by order entry applications |
| 45 | `ORDERABLE_TYPE_FLAG` | DOUBLE |  |  | Used to store the flag that indicates what type of orderable procedure the item has been assigned |
| 46 | `ORDER_SENTENCE_ID` | DOUBLE | NOT NULL |  | The id for the order sentence associate with this synonym |
| 47 | `PREFERRED_DOSE_FLAG` | DOUBLE | NOT NULL |  | This defines whether strength or volume dose is preferred when both doses are available for an order. 0 - None, 1 - Strength. |
| 48 | `REF_TEXT_MASK` | DOUBLE |  |  | Value that shows what parts of the online reference manual have been associated with the synonym |
| 49 | `ROUNDING_RULE_CD` | DOUBLE |  |  | This field contains the rounding rule that will default into the dose calculator for this synonym. This field is only applicable to medication synonyms. |
| 50 | `RX_MASK` | DOUBLE |  |  | Stores the different sub-lists the synonym belongs in, i.e. should it display with diluents, with additives, with medications, or any combination of the above. |
| 51 | `SYNONYM_ID` | DOUBLE | NOT NULL | PK | The id of this synonym. |
| 52 | `TEMPLATE_MNEMONIC_FLAG` | DOUBLE | NOT NULL |  | NOT USED |
| 53 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 54 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 55 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 56 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 57 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 58 | `VIRTUAL_VIEW` | VARCHAR(100) |  |  | The offset used to determine whether to show the orderable or not for a facility. |
| 59 | `WITNESS_FLAG` | DOUBLE | NOT NULL |  | Witness_flag indicates if the witness field is required when Medication Administration events are Charted. 0 indicates that a witness is not required. 1 indicates that a witness is required. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `CATALOG_CD` | [ORDER_CATALOG](ORDER_CATALOG.md) | `CATALOG_CD` |
| `HIGH_ALERT_LONG_TEXT_ID` | [LONG_TEXT](LONG_TEXT.md) | `LONG_TEXT_ID` |

## Referenced by (63)

| From table | Column |
|------------|--------|
| [ALT_SEL_CAT](ALT_SEL_CAT.md) | `IV_SET_SYNONYM_ID` |
| [ALT_SEL_LIST](ALT_SEL_LIST.md) | `ORDERED_AS_SYNONYM_ID` |
| [ALT_SEL_LIST](ALT_SEL_LIST.md) | `SYNONYM_ID` |
| [AUTHORIZATION_ITEM](AUTHORIZATION_ITEM.md) | `ORDER_SYNONYM_ID` |
| [AUTHORIZATION_ITEM_HIST](AUTHORIZATION_ITEM_HIST.md) | `ORDER_SYNONYM_ID` |
| [BB_MOD_NEW_PRODUCT](BB_MOD_NEW_PRODUCT.md) | `SYNONYM_ID` |
| [BR_ADO_ORD_LIST](BR_ADO_ORD_LIST.md) | `SYNONYM_ID` |
| [CHART_GRP_EVNT_SET](CHART_GRP_EVNT_SET.md) | `SYNONYM_ID` |
| [CONVERT_AUDIT_BEST_MATCH](CONVERT_AUDIT_BEST_MATCH.md) | `SYNONYM_ID` |
| [CONVERT_AUDIT_SYNONYM](CONVERT_AUDIT_SYNONYM.md) | `SYNONYM_ID` |
| [CS_COMPONENT](CS_COMPONENT.md) | `COMP_ID` |
| [ENCNTR_PROCEDURE](ENCNTR_PROCEDURE.md) | `SYNONYM_ID` |
| [EXPEDITE_TRIGGER](EXPEDITE_TRIGGER.md) | `SYNONYM_ID` |
| [GS_MED_CLAIM](GS_MED_CLAIM.md) | `PRODUCT_SYNONYM_ID` |
| [IB_RX_REQ_DRUG](IB_RX_REQ_DRUG.md) | `SYNONYM_ID` |
| [MED_ADMIN_MED_EVENT_INGRDNT](MED_ADMIN_MED_EVENT_INGRDNT.md) | `SYNONYM_ID` |
| [MED_OE_DEFAULTS](MED_OE_DEFAULTS.md) | `ORD_AS_SYNONYM_ID` |
| [MRU_LOOKUP_ORDER](MRU_LOOKUP_ORDER.md) | `SYNONYM_ID` |
| [OCS_ATTR_XCPTN](OCS_ATTR_XCPTN.md) | `SYNONYM_ID` |
| [OCS_CONFIDENTIAL_DEFAULTS](OCS_CONFIDENTIAL_DEFAULTS.md) | `SYNONYM_ID` |
| [OCS_CUSTOM_REF_CONTENT](OCS_CUSTOM_REF_CONTENT.md) | `SYNONYM_ID` |
| [OCS_DEF_DOSE_CALC_METHOD](OCS_DEF_DOSE_CALC_METHOD.md) | `SYNONYM_ID` |
| [OCS_FACILITY_FORMULARY_R](OCS_FACILITY_FORMULARY_R.md) | `SYNONYM_ID` |
| [OCS_FACILITY_R](OCS_FACILITY_R.md) | `SYNONYM_ID` |
| [OCS_HANDLING_PRECAUTIONS](OCS_HANDLING_PRECAUTIONS.md) | `SYNONYM_ID` |
| [ORDERS](ORDERS.md) | `IV_SET_SYNONYM_ID` |
| [ORDERS](ORDERS.md) | `SYNONYM_ID` |
| [ORDER_ACTION](ORDER_ACTION.md) | `SYNONYM_ID` |
| [ORDER_CATALOG_ITEM_R](ORDER_CATALOG_ITEM_R.md) | `SYNONYM_ID` |
| [ORDER_INGREDIENT](ORDER_INGREDIENT.md) | `ORDERED_AS_SYNONYM_ID` |
| [ORDER_INGREDIENT](ORDER_INGREDIENT.md) | `SYNONYM_ID` |
| [ORDER_INGREDIENT_HISTORY](ORDER_INGREDIENT_HISTORY.md) | `SYNONYM_ID` |
| [ORDER_PROPOSAL](ORDER_PROPOSAL.md) | `IV_SET_SYNONYM_ID` |
| [ORDER_PROPOSAL](ORDER_PROPOSAL.md) | `SYNONYM_ID` |
| [ORDER_PROPOSAL_INGREDIENT](ORDER_PROPOSAL_INGREDIENT.md) | `SYNONYM_ID` |
| [ORDER_PROPOSAL_INGRED_HST](ORDER_PROPOSAL_INGRED_HST.md) | `SYNONYM_ID` |
| [ORDER_RX_SCRATCHPAD](ORDER_RX_SCRATCHPAD.md) | `SYNONYM_ID` |
| [ORM_ERROR_LOG](ORM_ERROR_LOG.md) | `SYNONYM_ID` |
| [PBS_OCS_MAPPING](PBS_OCS_MAPPING.md) | `SYNONYM_ID` |
| [PHA_DISP_OBS_ST](PHA_DISP_OBS_ST.md) | `SYNONYM_ID` |
| [PHA_ORD_ACT_OBS_ST](PHA_ORD_ACT_OBS_ST.md) | `SYNONYM_ID` |
| [PHA_PROD_DISP_OBS_ST](PHA_PROD_DISP_OBS_ST.md) | `ING_SYNONYM_ID` |
| [PHA_PROD_DISP_OBS_ST](PHA_PROD_DISP_OBS_ST.md) | `SYNONYM_ID` |
| [PL_PC_ORG_TAB_XREF](PL_PC_ORG_TAB_XREF.md) | `SYNONYM_ID` |
| [PRODUCT_INDEX](PRODUCT_INDEX.md) | `SYNONYM_ID` |
| [PROP_ORDER](PROP_ORDER.md) | `SYNONYM_ID` |
| [RAD_MEDS](RAD_MEDS.md) | `SYNONYM_ID` |
| [RAD_MED_CAT_LIST](RAD_MED_CAT_LIST.md) | `SYNONYM_ID` |
| [RC_SLA_RULE](RC_SLA_RULE.md) | `ORDER_SYNONYM_ID` |
| [RX_AUTO_VERIFY_ING_AUDIT](RX_AUTO_VERIFY_ING_AUDIT.md) | `SYNONYM_ID` |
| [RX_PRODUCT_ASSIGN_ITEM_AUDIT](RX_PRODUCT_ASSIGN_ITEM_AUDIT.md) | `SYNONYM_ID` |
| [RX_THERAP_SBSTTN_FROM](RX_THERAP_SBSTTN_FROM.md) | `FROM_SYNONYM_ID` |
| [RX_THERAP_SBSTTN_TO](RX_THERAP_SBSTTN_TO.md) | `TO_SYNONYM_ID` |
| [SCH_APPT_ORD](SCH_APPT_ORD.md) | `SYNONYM_ID` |
| [SCH_BOOKING_ORD](SCH_BOOKING_ORD.md) | `SYNONYM_ID` |
| [SCH_EVENT_ATTACH](SCH_EVENT_ATTACH.md) | `SYNONYM_ID` |
| [SCH_EVENT_RECUR_ORDER](SCH_EVENT_RECUR_ORDER.md) | `ORDER_SYNONYM_ID` |
| [SCH_PEND_ORDER](SCH_PEND_ORDER.md) | `SYNONYM_ID` |
| [STANDARDIZED_ORDER_DOSE](STANDARDIZED_ORDER_DOSE.md) | `SYNONYM_ID` |
| [SURG_CASE_PROCEDURE](SURG_CASE_PROCEDURE.md) | `SYNONYM_ID` |
| [SURG_REQ_PROC](SURG_REQ_PROC.md) | `PROC_SYNONYM_ID` |
| [SYNONYM_ITEM_R](SYNONYM_ITEM_R.md) | `SYNONYM_ID` |
| [THERAPEUTIC_CAT_ITEM](THERAPEUTIC_CAT_ITEM.md) | `SYNONYM_ID` |

