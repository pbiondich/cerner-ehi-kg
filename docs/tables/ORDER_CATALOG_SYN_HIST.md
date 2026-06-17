# ORDER_CATALOG_SYN_HIST

> History- Used to store all valid synonyms and their associated information for a given order catalog item - TABLE should be in ORDERS BUILD data model

**Description:** Order catalog synonym - hist  
**Table type:** REFERENCE  
**Primary key:** _(not published — see note)_  
**Columns:** 63

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ACTION_DT_TM` | DATETIME |  |  | date and time when the Action (delete/update) was taken |
| 2 | `ACTION_TAKEN_TFLG` | VARCHAR(30) |  |  | The action taken by the user (delete/update) |
| 3 | `ACTION_USER_ID` | DOUBLE |  |  | user id of the person who took the action (delete/update) |
| 4 | `ACTIVE_IND` | DOUBLE |  |  | The table row is active or inactive. A row is generally active unless it is in an inactive state such as logically deleted, combined away, pending purge, etc. |
| 5 | `ACTIVE_STATUS_CD` | DOUBLE | NOT NULL |  | Indicates the status of the row itself (not the data in the row) such as active, inactive, combined away, pending purge, etc. |
| 6 | `ACTIVE_STATUS_DT_TM` | DATETIME |  |  | The date and time that the active_status_cd was set. |
| 7 | `ACTIVE_STATUS_PRSNL_ID` | DOUBLE | NOT NULL |  | The person who caused the active_status_cd to be set or change. |
| 8 | `ACTIVITY_SUBTYPE_CD` | DOUBLE | NOT NULL |  | Stores the code value for the activity sub-type that is used to filter order catalog items within activity type |
| 9 | `ACTIVITY_TYPE_CD` | DOUBLE | NOT NULL |  | Stores the code value for the activity type that is used to filter order catalog items within catalog type |
| 10 | `AUTHORIZATION_REVIEW_FLAG` | DOUBLE | NOT NULL |  | Used to store the flag that indicates what kind of stop type is assigned to the orderable.0 - None.1 - Indicator Only - No Status Updates. 2 - Indicator Only - With Status Updates (Current: No Alerts - Indicator Only). 3 - Alert - No Override Required. 4 - Alert - Override required. 5 - Authorization Required Prior to Start. |
| 11 | `AUTOPROG_SYN_IND` | DOUBLE | NOT NULL |  | Indicator if set symbolized that auto programming will happen at synonym level. If not set auto programming will happen at Catalog code level. |
| 12 | `CATALOG_CD` | DOUBLE | NOT NULL |  | Order catalog number |
| 13 | `CATALOG_TYPE_CD` | DOUBLE | NOT NULL |  | Used to store the internal code for the catalog type. Used as a filtering mechanism for rows on the order catalog table |
| 14 | `CKI` | VARCHAR(255) |  |  | For meds process |
| 15 | `CONCENTRATION_STRENGTH` | DOUBLE |  |  | The strength value of the concentration ratio. |
| 16 | `CONCENTRATION_STRENGTH_UNIT_CD` | DOUBLE | NOT NULL |  | The code value that represents the unit of measure for the concentration strength attribute. |
| 17 | `CONCENTRATION_VOLUME` | DOUBLE |  |  | The volume value of the concentration ratio. |
| 18 | `CONCENTRATION_VOLUME_UNIT_CD` | DOUBLE | NOT NULL |  | The code value that represents the unit of measure for the concentration volume attribute. |
| 19 | `CONCEPT_CKI` | VARCHAR(255) |  |  | Concept CKI is the functional Concept Identifier; it is the codified means within Millennium to identify key medical concepts to support information processing - clinical decision support - executable knowledge and knowledge presentation. |
| 20 | `CS_INDEX_CD` | DOUBLE | NOT NULL |  | CareSet Index code |
| 21 | `DCP_CLIN_CAT_CD` | DOUBLE | NOT NULL |  | The clinical category of this orderable. |
| 22 | `DISPLAY_ADDITIVES_FIRST_IND` | DOUBLE | NOT NULL |  | Indicates whether or not this synonym (additive) should be displayed prior to the diluents in an IV. |
| 23 | `FILTERED_OD_IND` | DOUBLE |  |  | Indicates if any filtered order details have been set up against this synonym. |
| 24 | `HEALTH_PLAN_VIEW` | VARCHAR(255) |  |  | Each character in the field represent one health plan. The offset of the health plans is defined in dcp_entity_reltn table. The possible values for each char are: G (Green) - W (White) - Yellow (Y)- R (Red). |
| 25 | `HIDE_FLAG` | DOUBLE |  |  | Flag indicating whether or not to hide this synonym |
| 26 | `HIGH_ALERT_IND` | DOUBLE | NOT NULL |  | A customized message that alerts the user when the order is being added to scratchpad. |
| 27 | `HIGH_ALERT_LONG_TEXT_ID` | DOUBLE | NOT NULL |  | A pointer to the text displayed if this is a High Alert orderable. |
| 28 | `HIGH_ALERT_REQUIRED_NTFY_IND` | DOUBLE |  |  | Indicates if the high alert text should be presented to the user automatically. |
| 29 | `HRT_MEDICATION_IND` | DOUBLE |  |  | Indicates whether this synonym is used for Hormone Replacement Therapy. |
| 30 | `IGNORE_HIDE_CONVERT_IND` | DOUBLE | NOT NULL |  | Indicates if the hide flag can be ignored for convert to inpatient. |
| 31 | `INGREDIENT_RATE_CONVERSION_IND` | DOUBLE | NOT NULL |  | If the ingredient is eligible to have ingredient rate to total bag rate conversions and vice versa. If the indicator is set to 1 - then orders that have this ingredient will be shown on the interactive view with an additive rate row and a total bag rate row. Similarly |
| 32 | `INTERMITTENT_IND` | DOUBLE | NOT NULL |  | Indicates whether or not a synonym can be placed as an intermittent order. |
| 33 | `ITEM_ID` | DOUBLE | NOT NULL |  | The associated id of the item for this synonym. |
| 34 | `LAST_ADMIN_DISP_BASIS_FLAG` | DOUBLE | NOT NULL |  | Specifies at what level the med interval warnings should be performed at. 0 - Use System Default - 1 - Order Level - 2 - Event Code Level. |
| 35 | `LOCK_TARGET_DOSE_IND` | DOUBLE | NOT NULL |  | Lock target dose indicator. An indicator to lock the target dose in the dose calculator. |
| 36 | `MAX_DOSE_CALC_BSA_VALUE` | DOUBLE | NOT NULL |  | Contains the reference (upper-limit) for the BSA value for the synonym and is always measured in meter-squared. Has a (default) value of 0.0 denoting the absence of a reference. |
| 37 | `MAX_FINAL_DOSE` | DOUBLE | NOT NULL |  | Contains the reference (upper-limit) on the final-dose for the synonym. Has a (default) value of 0.0 denoting the absence of a reference. |
| 38 | `MAX_FINAL_DOSE_UNIT_CD` | DOUBLE | NOT NULL |  | Contains the unit of measurement for the reference (upper-limit) defined in MAX_FINAL_DOSE. Has a value of 0.0 if MAX_FINAL_DOSE contains 0.0. |
| 39 | `MED_INTERVAL_WARN_FLAG` | DOUBLE | NOT NULL |  | Specifies if med interval warnings should be displayed when a result is within the defined time range. 0 - Use System Default - 1 - Order Level - 2 - Event Code Level. |
| 40 | `MNEMONIC` | VARCHAR(200) |  |  | The display mnemonic of this orderable. |
| 41 | `MNEMONIC_KEY_CAP` | VARCHAR(200) |  |  | The key version of the mnemonic for this orderable. |
| 42 | `MNEMONIC_KEY_CAP_A_NLS` | VARCHAR(400) |  |  | MNEMONIC_KEY_CAP_A_NLS column |
| 43 | `MNEMONIC_KEY_CAP_NLS` | VARCHAR(405) |  |  | NLS Sort column for internationalization. |
| 44 | `MNEMONIC_TYPE_CD` | DOUBLE | NOT NULL |  | The type of mnemonic this is. |
| 45 | `MULTIPLE_ORD_SENT_IND` | DOUBLE |  |  | Indicator on whether or not this synonym has multiple order sentences associated with it. |
| 46 | `NOT_FOR_EPRESCRIBING_IND` | DOUBLE |  |  | Indicator to determine if this synonym should be restricted for eprescribing. |
| 47 | `OE_FORMAT_ID` | DOUBLE | NOT NULL |  | Used to store the internal identifier for the order entry format to be used by order entry applications |
| 48 | `ORDERABLE_TYPE_FLAG` | DOUBLE |  |  | Used to store the flag that indicates what type of orderable procedure the item has been assigned |
| 49 | `ORDER_CATALOG_SYN_HIST_ID` | DOUBLE | NOT NULL |  | Primary Key |
| 50 | `ORDER_SENTENCE_ID` | DOUBLE | NOT NULL |  | The id for the order sentence associate with this synonym |
| 51 | `PREFERRED_DOSE_FLAG` | DOUBLE | NOT NULL |  | This defines whether strength or volume dose is preferred when both doses are available for an order. 0 - None - 1 - Strength. |
| 52 | `REF_TEXT_MASK` | DOUBLE |  |  | Value that shows what parts of the online reference manual have been associated with the synonym |
| 53 | `ROUNDING_RULE_CD` | DOUBLE |  |  | This field contains the rounding rule that will default into the dose calculator for this synonym. This field is only applicable to medication synonyms. |
| 54 | `RX_MASK` | DOUBLE |  |  | Stores the different sub-lists the synonym belongs in - i.e. should it display with diluents - with additives - with medications - or any combination of the above. |
| 55 | `SYNONYM_ID` | DOUBLE | NOT NULL |  | The id of this synonym. |
| 56 | `TEMPLATE_MNEMONIC_FLAG` | DOUBLE | NOT NULL |  | NOT USED |
| 57 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 58 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 59 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 60 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 61 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 62 | `VIRTUAL_VIEW` | VARCHAR(100) |  |  | The offset used to determine whether to show the orderable or not for a facility. |
| 63 | `WITNESS_FLAG` | DOUBLE | NOT NULL |  | Witness_flag indicates if the witness field is required when Medication Administration events are Charted. 0 indicates that a witness is not required. 1 indicates that a witness is required. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

