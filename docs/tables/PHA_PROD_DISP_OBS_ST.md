# PHA_PROD_DISP_OBS_ST

> Observation set of PharmNet's activity data at the product dispense level. Used to generate a summary of doses for patients.

**Description:** pha_prod_disp_obs_st  
**Table type:** ACTIVITY  
**Primary key:** _(not published — see note)_  
**Columns:** 316

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ACTION_DT_NBR` | DOUBLE |  |  | action_dt_nbr column |
| 2 | `ACTION_DT_TM` | DATETIME |  |  | action_dt_tm column |
| 3 | `ACTION_MIN_NBR` | DOUBLE |  |  | action_min_nbr column |
| 4 | `ACTION_PRSNL_ID` | DOUBLE | NOT NULL |  | action_prsnl_id |
| 5 | `ACTION_QUAL_CD` | DOUBLE |  |  | A codified value that helps describe the action that occurred. |
| 6 | `ACTION_REJECTED_IND` | DOUBLE |  |  | action_rejected_ind column |
| 7 | `ACTION_SEQ` | DOUBLE | NOT NULL |  | action_seq column |
| 8 | `ACTION_TYPE_CD` | DOUBLE | NOT NULL |  | Action that is requested |
| 9 | `ACTION_TZ` | DOUBLE |  |  | Time zone associated with the corresponding DT_TM column. |
| 10 | `CANCEL_REASON_CD` | DOUBLE | NOT NULL |  | cancel_reason_cd column |
| 11 | `CHARGE_IND` | DOUBLE |  |  | charge_ind column |
| 12 | `CHARGE_QTY` | DOUBLE |  |  | charge_qty column |
| 13 | `CKI` | VARCHAR(255) |  |  | CKI value |
| 14 | `CONTRIBUTOR_SYSTEM_CD` | DOUBLE |  |  | Contributor system identifies the source feed of data from which a row was populated. This is mainly used to determine how to update a set of data that may have originated from more than one source feed. |
| 15 | `COPAY` | DOUBLE |  |  | copay value |
| 16 | `COSIGN_OVERRIDE_OPTION_CD` | DOUBLE | NOT NULL |  | Determines if Physician Cosign is required for external order entry systems. |
| 17 | `COSIGN_OVERRIDE_REASON_CD` | DOUBLE | NOT NULL |  | The reason Physician Cosign has been overridden from the system determined value. |
| 18 | `COST` | DOUBLE |  |  | cost column |
| 19 | `CREDIT_QTY` | DOUBLE |  |  | credit_qty column |
| 20 | `CUR_DEPT_STATUS_CD` | DOUBLE | NOT NULL |  | cur_dept_status_cd column |
| 21 | `CUR_ORDER_STATUS_CD` | DOUBLE | NOT NULL |  | ** OBSOLETE - NO LONGER USED **cur_order_status_cd column |
| 22 | `CUR_START_DT_NBR` | DOUBLE |  |  | cur_start_dt_nbr column |
| 23 | `CUR_START_DT_TM` | DATETIME |  |  | cur_start_dt_tm column |
| 24 | `CUR_START_MIN_NBR` | DOUBLE |  |  | cur_start_min_nbr column |
| 25 | `CUR_START_TZ` | DOUBLE |  |  | Time zone associated with the corresponding DT_TM column. |
| 26 | `DAW_CD` | DOUBLE | NOT NULL |  | daw_cd column |
| 27 | `DC_REASON_CD` | DOUBLE | NOT NULL |  | dc_reason_cd column |
| 28 | `DEPT_MISC_LINE` | VARCHAR(255) |  |  | dept_misc_line |
| 29 | `DEPT_STATUS_CD` | DOUBLE | NOT NULL |  | dept_status_cd column |
| 30 | `DISCONTINUE_EFF_DT_NBR` | DOUBLE |  |  | discontinue_eff_dt_nbr column |
| 31 | `DISCONTINUE_EFF_DT_TM` | DATETIME |  |  | discontinue_eff_dt_tm column |
| 32 | `DISCONTINUE_EFF_MIN_NBR` | DOUBLE |  |  | discontinue_eff_min_nbr column |
| 33 | `DISCONTINUE_EFF_TZ` | DOUBLE |  |  | Time zone associated with the corresponding DT_TM column. |
| 34 | `DISCONTINUE_IND` | DOUBLE |  |  | discontinue_ind column |
| 35 | `DISCONTINUE_TYPE_CD` | DOUBLE | NOT NULL |  | discontinue_type_cd column |
| 36 | `DISPENSE_HX_ID` | DOUBLE | NOT NULL | FK→ | dispense_hx_id column |
| 37 | `DISP_CATEGORY_CD` | DOUBLE | NOT NULL |  | disp_category_cd column |
| 38 | `DISP_DT_NBR` | DOUBLE |  |  | disp_dt_nbr column |
| 39 | `DISP_DT_TM` | DATETIME |  |  | disp_dt_tm column |
| 40 | `DISP_EVENT_TYPE_CD` | DOUBLE | NOT NULL |  | disp_event_type_cd column |
| 41 | `DISP_FROM_LOC_CD` | DOUBLE | NOT NULL |  | disp_from_loc_cd column |
| 42 | `DISP_FROM_SR_CD` | DOUBLE | NOT NULL |  | disp_from_sr_cd column |
| 43 | `DISP_MIN_NBR` | DOUBLE |  |  | disp_min_nbr column |
| 44 | `DISP_PERS_BED_CD` | DOUBLE | NOT NULL |  | disp_pers_bed_cd |
| 45 | `DISP_PERS_BLD_CD` | DOUBLE | NOT NULL |  | disp_pers_bld_cd |
| 46 | `DISP_PERS_FAC_CD` | DOUBLE | NOT NULL |  | disp_pers_fac_cd |
| 47 | `DISP_PERS_NU2_GRP_CD` | DOUBLE | NOT NULL |  | disp_pers_nu2_grp_cd |
| 48 | `DISP_PERS_NU_CD` | DOUBLE | NOT NULL |  | disp_pers_nu_cd |
| 49 | `DISP_PERS_NU_GRP_CD` | DOUBLE | NOT NULL |  | disp_pers_nu_grp_cd |
| 50 | `DISP_PERS_ROOM_CD` | DOUBLE | NOT NULL |  | disp_pers_room_cd column |
| 51 | `DISP_PRIORITY_CD` | DOUBLE | NOT NULL |  | disp_priority_cd column |
| 52 | `DISP_QTY` | DOUBLE |  |  | disp_qty column |
| 53 | `DISP_QTY_UNIT_CD` | DOUBLE | NOT NULL |  | disp_qty_unit_cd column |
| 54 | `DISP_SHIFT2_GRP_CD` | DOUBLE | NOT NULL |  | For pharmacy shifts |
| 55 | `DISP_SHIFT_GRP_CD` | DOUBLE | NOT NULL |  | For Pharmacy Shifts |
| 56 | `DISP_SR_CD` | DOUBLE | NOT NULL |  | disp_sr_cd column |
| 57 | `DISP_TZ` | DOUBLE |  |  | Time zone associated with the corresponding DT_TM column. For inpatient rows, this is the time zone of the encounter. For Retail Pharmacy, it is the time zone of the pharmacy's facility. |
| 58 | `DOSES` | DOUBLE |  |  | doses column |
| 59 | `DOSE_QUANTITY` | DOUBLE |  |  | dose_quantity column |
| 60 | `DOSE_QUANTITY_UNIT_CD` | DOUBLE | NOT NULL |  | dose_quantity_unit_cd column |
| 61 | `EARLY_REASON_CD` | DOUBLE | NOT NULL |  | early_reason_cd column |
| 62 | `EFFECTIVE_DT_NBR` | DOUBLE |  |  | Effective Date Number value |
| 63 | `EFFECTIVE_DT_TM` | DATETIME |  |  | Effective Date and Time value |
| 64 | `EFFECTIVE_MIN_NBR` | DOUBLE |  |  | Effective Minute number value |
| 65 | `EFFECTIVE_TZ` | DOUBLE |  |  | Time zone associated with the corresponding DT_TM column. |
| 66 | `ENCNTR_ID` | DOUBLE | NOT NULL | FK→ | This is the value of the unique primary identifier of the encounter table. It is an internal system assigned number. |
| 67 | `EXPIRE_DT_NBR` | DOUBLE |  |  | expire_dt_nbr column |
| 68 | `EXPIRE_DT_TM` | DATETIME |  |  | expire date and time value |
| 69 | `EXPIRE_MIN_NBR` | DOUBLE |  |  | expire_min_nbr column |
| 70 | `EXPIRE_TZ` | DOUBLE |  |  | Time zone associated with the corresponding DT_TM column. |
| 71 | `EXTRA_REASON_CD` | DOUBLE | NOT NULL |  | extra_reason_cd column |
| 72 | `FILL_NBR` | DOUBLE |  |  | fill_nbr column |
| 73 | `FIRST_DOSE_DT_NBR` | DOUBLE |  |  | first_dose_dt_nbr column |
| 74 | `FIRST_DOSE_DT_TM` | DATETIME |  |  | first_dose_dt_tm column |
| 75 | `FIRST_DOSE_MIN_NBR` | DOUBLE |  |  | first_dose_min_nbr column |
| 76 | `FLOORSTOCK_IND` | DOUBLE |  |  | floorstock_ind column |
| 77 | `FLOORSTOCK_OVERRIDE_IND` | DOUBLE |  |  | floorstock_override_ind column |
| 78 | `FREQ_CD` | DOUBLE | NOT NULL |  | freq_cd column |
| 79 | `HEALTH_PLAN_ID` | DOUBLE | NOT NULL | FK→ | health_plan_id |
| 80 | `ICD9_NOMEN_ID` | DOUBLE | NOT NULL | FK→ | icd9_nomen_id column |
| 81 | `IGNORE_IND` | DOUBLE |  |  | ignore_ind column |
| 82 | `INACTIVE_FLAG` | DOUBLE |  |  | inactive_flag (future use) |
| 83 | `INCOMPLETE_ORDER_IND` | DOUBLE |  |  | incomplete_order_ind column |
| 84 | `INGREDIENT_IND` | DOUBLE |  |  | an indicator on whether this order has multiple ingredients. |
| 85 | `ING_CATALOG_CD` | DOUBLE | NOT NULL |  | ing_catalog_cd column |
| 86 | `ING_CATALOG_TYPE_CD` | DOUBLE | NOT NULL |  | ing_catalog_type_cd column |
| 87 | `ING_FREETEXT_DOSE` | VARCHAR(255) |  |  | ing_free-text_dose column |
| 88 | `ING_MNEMONIC` | VARCHAR(100) |  |  | ing_mnemonic column |
| 89 | `ING_SEQ` | DOUBLE | NOT NULL |  | ing_seq column |
| 90 | `ING_STRENGTH` | DOUBLE |  |  | ing_strength column |
| 91 | `ING_STRENGTH_UNIT_CD` | DOUBLE | NOT NULL |  | ing_strength_unit_cd column |
| 92 | `ING_SYNONYM_ID` | DOUBLE | NOT NULL | FK→ | ing_synonym_id column |
| 93 | `ING_TYPE_FLAG` | DOUBLE |  |  | ing_type_flag column |
| 94 | `ING_VOLUME` | DOUBLE |  |  | ing_volume column |
| 95 | `ING_VOLUME_UNIT_CD` | DOUBLE | NOT NULL |  | ing_volume_unit_cd column |
| 96 | `ITEM_ID` | DOUBLE | NOT NULL | FK→ | ID value of the Item |
| 97 | `LAST_FILL_STATUS_CD` | DOUBLE | NOT NULL |  | last_fill_status column |
| 98 | `LAST_REFILL_DT_NBR` | DOUBLE |  |  | last_refill_dt_nbr column |
| 99 | `LAST_REFILL_DT_TM` | DATETIME |  |  | last_refill_dt_tm column |
| 100 | `LAST_REFILL_MIN_NBR` | DOUBLE |  |  | last_refill_min_nbr column |
| 101 | `LAST_REFILL_TZ` | DOUBLE |  |  | Time zone associated with the corresponding DT_TM column. |
| 102 | `LAST_UPDT_PROVIDER_ID` | DOUBLE | NOT NULL |  | last_updt_provider_id column |
| 103 | `LATE_REASON_CD` | DOUBLE | NOT NULL |  | late_reason_cd column |
| 104 | `LEGAL_STATUS_CD` | DOUBLE | NOT NULL |  | Legal Status Code value |
| 105 | `MANF_ITEM_ID` | DOUBLE | NOT NULL | FK→ | manf_item_id column |
| 106 | `MANF_NDC_STR` | VARCHAR(200) |  |  | manf_ndc_str column |
| 107 | `MANUFACTURER_CD` | DOUBLE | NOT NULL |  | The Manufacturer Code |
| 108 | `MED_ORDER_TYPE_CD` | DOUBLE | NOT NULL |  | med_order_type_cd column |
| 109 | `MED_SERVICE_CD` | DOUBLE | NOT NULL |  | The type or category of medical service that the patient is receiving in relation to their encounter. The category may be of treatment type, surgery, general resources, or others. |
| 110 | `NDC_STR` | VARCHAR(200) |  |  | ndc_str column |
| 111 | `NEED_RX_CLIN_REVIEW_FLAG` | DOUBLE |  |  | Flag for identifying whether the order's clinical review has be completed or not. |
| 112 | `NEED_RX_PROD_ASSIGN_FLAG` | DOUBLE |  |  | Flag for identifying whether the order's product assignment has been completed or not. |
| 113 | `NEED_RX_VERIFY_IND` | DOUBLE |  |  | need_rx_verify_ind column |
| 114 | `NEED_VERIFY_IND` | DOUBLE |  |  | need_verify_ind column |
| 115 | `NEXT_DISP_DT_NBR` | DOUBLE |  |  | next_disp_dt_nbr column |
| 116 | `NEXT_DISP_DT_TM` | DATETIME |  |  | next_disp_dt_tm column |
| 117 | `NEXT_DISP_MIN_NBR` | DOUBLE |  |  | next_disp_min_nbr column |
| 118 | `NEXT_DISP_TZ` | DOUBLE |  |  | Time zone associated with the corresponding DT_TM column. For inpatient rows, this is the time zone of the encounter. For Retail Pharmacy, it is the time zone of the pharmacy's facility. |
| 119 | `ORDERABLE_TYPE_FLAG` | DOUBLE |  |  | orderable_type_flag column |
| 120 | `ORDERING_PROVIDER_ID` | DOUBLE | NOT NULL |  | ordering_provider_id column |
| 121 | `ORDER_CATALOG_CD` | DOUBLE | NOT NULL |  | order_catalog_cd column |
| 122 | `ORDER_CATALOG_TYPE_CD` | DOUBLE | NOT NULL |  | order_catalog_type_cd column |
| 123 | `ORDER_ID` | DOUBLE | NOT NULL | FK→ | Order Id from the orders table |
| 124 | `ORDER_INCOMP_ORDER_IND` | DOUBLE |  |  | order_incomp_order_ind column |
| 125 | `ORDER_LOC_CD` | DOUBLE | NOT NULL |  | order_loc_cd column |
| 126 | `ORDER_PRIORITY_CD` | DOUBLE | NOT NULL |  | ORDER_PRIORITY_CD |
| 127 | `ORDER_STATUS_CD` | DOUBLE | NOT NULL |  | order_status_cd column |
| 128 | `ORDER_TYPE_FLAG` | DOUBLE |  |  | order_type_flag column |
| 129 | `ORD_PERS_AGE_DAYS` | DOUBLE |  |  | ord_pers_age_days |
| 130 | `ORD_PERS_AGE_YEARS` | DOUBLE |  |  | ord_pers_age_years |
| 131 | `ORD_PERS_BED_CD` | DOUBLE | NOT NULL |  | ord_pers_bed_cd |
| 132 | `ORD_PERS_BLD_CD` | DOUBLE | NOT NULL |  | ord_pers_bld_cd |
| 133 | `ORD_PERS_FAC_CD` | DOUBLE | NOT NULL |  | ord_pers_fac_cd |
| 134 | `ORD_PERS_NU_CD` | DOUBLE | NOT NULL |  | ord_pers_nu_cd |
| 135 | `ORD_PERS_NU_GRP2_CD` | DOUBLE | NOT NULL |  | ord_pers_nu_grp2_cd |
| 136 | `ORD_PERS_NU_GRP_CD` | DOUBLE | NOT NULL |  | ord_pers_nu_grp_cd |
| 137 | `ORD_PERS_ROOM_CD` | DOUBLE | NOT NULL |  | ord_pers_room_cd |
| 138 | `ORD_PERS_ZIP` | VARCHAR(25) |  |  | ord_pers_zip |
| 139 | `ORGANIZATION_ID` | DOUBLE | NOT NULL | FK→ | organization_id |
| 140 | `ORIG_ORDER_DT_NBR` | DOUBLE |  |  | orig_order_dt_nbr column |
| 141 | `ORIG_ORDER_DT_TM` | DATETIME |  |  | orig_order_dt_tm column |
| 142 | `ORIG_ORDER_MIN_NBR` | DOUBLE |  |  | orig_order_min_nbr column |
| 143 | `ORIG_ORDER_TZ` | DOUBLE |  |  | Time zone associated with the corresponding DT_TM column. |
| 144 | `ORIG_ORD_AS_FLAG` | DOUBLE | NOT NULL |  | the flag show how this order was originally placed. |
| 145 | `PARENT_THERAP_CLASS` | VARCHAR(1000) |  |  | parent_therap_class column |
| 146 | `PARENT_THERAP_CLASS_ID` | DOUBLE | NOT NULL | FK→ | parent_therap_class_id column |
| 147 | `PAR_DOSES` | DOUBLE |  |  | par_doses column |
| 148 | `PERSON_ID` | DOUBLE | NOT NULL | FK→ | This is the value of the unique primary identifier of the person table. It is an internal system assigned number. |
| 149 | `PERSON_OWE_QTY` | DOUBLE | NOT NULL |  | Amount owed for a person for a product of an order. |
| 150 | `PHARM_ORDER_TYPE_FLAG` | DOUBLE |  |  | pharm_order_type_flag column |
| 151 | `PHARM_TYPE_CD` | DOUBLE | NOT NULL |  | pharm_type_cd column |
| 152 | `PHYSICIAN_DEA_TXT` | VARCHAR(200) |  |  | DEA number of the prescribing physician |
| 153 | `PREV_DISP_DT_NBR` | DOUBLE |  |  | prev_disp_dt_nbr column |
| 154 | `PREV_DISP_DT_TM` | DATETIME |  |  | prev_disp_dt_tm column |
| 155 | `PREV_DISP_MIN_NBR` | DOUBLE |  |  | prev_disp_min_nbr column |
| 156 | `PREV_DISP_TZ` | DOUBLE |  |  | Time zone associated with the corresponding DT_TM column. For inpatient rows, this is the time zone of the encounter. For Retail Pharmacy, it is the time zone of the pharmacy's facility. |
| 157 | `PRICE` | DOUBLE |  |  | price column |
| 158 | `PRICE_CODE_CD` | DOUBLE | NOT NULL |  | price_code_cd column |
| 159 | `PRN_IND` | DOUBLE |  |  | prn_ind column |
| 160 | `PROD_DISPENSE_HX_ID` | DOUBLE | NOT NULL |  | Unique, generated identifier for a product on a dispense event. |
| 161 | `PROD_VLDTN_DT_TM` | DATETIME |  |  | Identifies the most recent validation date/time. |
| 162 | `PROD_VLDTN_ERROR_IND` | DOUBLE | NOT NULL |  | Indicates if an error occurred during scanning. |
| 163 | `PROD_VLDTN_IND` | DOUBLE | NOT NULL |  | Indicator to determine if product validation occurred on a dispense. |
| 164 | `PROD_VLDTN_OVERRIDE_IND` | DOUBLE | NOT NULL |  | Indicator to determine if the user overrides a scan failure. |
| 165 | `PROD_VLDTN_OVERRIDE_REASON_CD` | DOUBLE | NOT NULL |  | Identifies the reason a user selects to override a validation event. |
| 166 | `PROD_VLDTN_PRSNL_ID` | DOUBLE | NOT NULL | FK→ | The user who last performed a validation event. |
| 167 | `PROD_VLDTN_RPH_IND` | DOUBLE | NOT NULL |  | Indicates if any events were performed by a pharmacist. |
| 168 | `PROD_VLDTN_TECH_IND` | DOUBLE | NOT NULL |  | Indicates if any events were performed by a pharmacy technician. |
| 169 | `PROD_VLDTN_TZ` | DOUBLE | NOT NULL |  | The time zone associated with PROD_VLDTN_DT_TM. |
| 170 | `PROJECTED_STOP_DT_NBR` | DOUBLE |  |  | projected_stop_dt_nbr column |
| 171 | `PROJECTED_STOP_DT_TM` | DATETIME |  |  | projected_stop_dt_tm column |
| 172 | `PROJECTED_STOP_MIN_NBR` | DOUBLE |  |  | projected_stop_min_nbr column |
| 173 | `PROJECTED_STOP_TZ` | DOUBLE |  |  | Time zone associated with the corresponding DT_TM column. |
| 174 | `QTY_REMAINING` | DOUBLE |  |  | qty_remaining column |
| 175 | `REASON_CD` | DOUBLE | NOT NULL |  | reason_cd |
| 176 | `REFILLS_REMAINING` | DOUBLE |  |  | refills_remaining column |
| 177 | `REFILL_QTY` | DOUBLE |  |  | refill_qty column |
| 178 | `REIMBURSEMENT_AMT` | DOUBLE |  |  | reimbursement_amt column |
| 179 | `RENEW_REASON_CD` | DOUBLE | NOT NULL |  | renew_reason_cd column |
| 180 | `REPLACE_EVERY` | DOUBLE |  |  | replace_every column |
| 181 | `REPLACE_EVERY_CD` | DOUBLE | NOT NULL |  | replace_every_cd column |
| 182 | `REQ_START_DT_NBR` | DOUBLE |  |  | req_start_dt_nbr column |
| 183 | `REQ_START_DT_TM` | DATETIME |  |  | req_start_dt_tm column |
| 184 | `REQ_START_MIN_NBR` | DOUBLE |  |  | req_start_min_nbr column |
| 185 | `REQ_START_TZ` | DOUBLE |  |  | Time zone associated with the corresponding DT_TM column. |
| 186 | `RESUME_DT_NBR` | DOUBLE |  |  | resume_dt_nbr column |
| 187 | `RESUME_DT_TM` | DATETIME |  |  | resume_dt_tm column |
| 188 | `RESUME_EFF_DT_NBR` | DOUBLE |  |  | resume_eff_dt_nbr column |
| 189 | `RESUME_EFF_DT_TM` | DATETIME |  |  | resume_eff_dt_tm column |
| 190 | `RESUME_EFF_MIN_NBR` | DOUBLE |  |  | resume_eff_min_nbr column |
| 191 | `RESUME_EFF_TZ` | DOUBLE |  |  | Time zone associated with the corresponding DT_TM column. |
| 192 | `RESUME_MIN_NBR` | DOUBLE |  |  | resume_min_nbr column |
| 193 | `RESUME_REASON_CD` | DOUBLE | NOT NULL |  | resume_reason_cd column |
| 194 | `RESUME_TZ` | DOUBLE |  |  | Time zone associated with the corresponding DT_TM column. |
| 195 | `ROOT_THERAP_CLASS` | VARCHAR(1000) |  |  | root_therap_class column |
| 196 | `ROOT_THERAP_CLASS_ID` | DOUBLE | NOT NULL | FK→ | root_therap_class_id column |
| 197 | `RUN_USER_ID` | DOUBLE | NOT NULL |  | run_user_id column |
| 198 | `RXA_AUTH_NBR_TXT` | VARCHAR(250) |  |  | Last Authorization number received from health plan |
| 199 | `RXA_BACKWARD_ORDER_ID` | DOUBLE |  |  | Indicates the order based on which the current order was placed |
| 200 | `RXA_BILL_QTY` | DOUBLE |  |  | Indicates the quantity billed for the current fill |
| 201 | `RXA_CHECK_RPH_ID` | DOUBLE |  |  | Person_id, of the pharmacist that checked the dispense, from prsnl table |
| 202 | `RXA_CHRG_CDM` | VARCHAR(250) |  |  | CDM number used in charging the dispense |
| 203 | `RXA_CHRG_DISPENSE_HX_ID` | DOUBLE |  |  | The dispense record that is being cancelled by the current dispense |
| 204 | `RXA_CLAIM_FLAG` | DOUBLE |  |  | Indicates whether the current fill has been claimed 0,"None",1,"Non-Adjudicated",2,"Adjudicated" |
| 205 | `RXA_CLAIM_STATUS_CD` | DOUBLE |  |  | Indicates the status of the claim transaction for last health plan |
| 206 | `RXA_COB_FLAG` | DOUBLE |  |  | Indicates whether co-ordination of benefits was used in claiming this fill 0, "None", 1,"Non-COB", 2,"COB" |
| 207 | `RXA_COMPLETED_USER_ID` | DOUBLE |  |  | Person_id, of the user that completed the dispense, from prsnl table |
| 208 | `RXA_COMPOUND_BASE_IND` | DOUBLE |  |  | Indicates if the current drug is a base |
| 209 | `RXA_COMPOUND_FLAG` | DOUBLE |  |  | Indicates if the current drug is a compound parent or child |
| 210 | `RXA_CONTROL_NBR_TXT` | VARCHAR(250) |  |  | Control number for the script |
| 211 | `RXA_CRDT_DISPENSE_HX_ID` | DOUBLE |  |  | The dispense record that credited the current dispense.PHA_PRODUCT_DISPENSE_HX_ST |
| 212 | `RXA_DAYS_SUPPLY` | DOUBLE |  |  | Indicates the days for which the current fill will last |
| 213 | `RXA_DISCOUNT_AMT` | DOUBLE |  |  | RXA Discount Amount |
| 214 | `RXA_DISPENSE_FEE` | DOUBLE |  |  | RXA Dispense Fee |
| 215 | `RXA_DISP_COMPLETE_FLAG` | DOUBLE |  |  | Indicates whether a dispense is complete. 0, "In-Complete",1, "Complete" |
| 216 | `RXA_DISP_PRIORITY_DT_TM` | DATETIME |  |  | Priority Date/Time for the dispense |
| 217 | `RXA_DISP_PRIORITY_DT_TZ` | DOUBLE |  |  | Priority Date/Time for the dispense |
| 218 | `RXA_DISP_STAT_CD` | DOUBLE |  |  | Latest dispense status of the dispense. |
| 219 | `RXA_DUR_FLAG` | DOUBLE |  |  | Indicates whether last health plan performed drug utilization review 0,"None",1, "NO DUR Performed", 2, "DUR Performed" |
| 220 | `RXA_EXPANDED_SIG_ID` | DOUBLE |  |  | Order comment of type "PHARMSIG". Long_text_id from long_text table |
| 221 | `RXA_FILL_DEVICE_SR_CD` | DOUBLE |  |  | To store the pharmacy filling device value. |
| 222 | `RXA_FILL_LOCATION_SR_CD` | DOUBLE |  |  | To store the pharmacy filling location value |
| 223 | `RXA_FILL_RPH_ID` | DOUBLE |  |  | Person_id. of the pharmacist that filled the dispense, from prsnl table |
| 224 | `RXA_FORWARD_ORDER_ID` | DOUBLE |  |  | Indicates the order that was placed based off of the current order |
| 225 | `RXA_HEALTH_PLAN_SEQ` | DOUBLE |  |  | The sequence of the last health plan in the list of health plans used for this prescription |
| 226 | `RXA_INCENTIVE_AMT` | DOUBLE |  |  | RXA Incentive Amount |
| 227 | `RXA_INNER_PKG_QTY` | DOUBLE |  |  | Indicates the inner package quantity of the current manufacturer |
| 228 | `RXA_INNER_PKG_UNIT_CD` | DOUBLE |  |  | Indicates code for the inner package quantity of the current manufacturer |
| 229 | `RXA_LEVEL5_CD` | DOUBLE |  |  | work station that requested the event |
| 230 | `RXA_MED_PRODUCT_ID` | DOUBLE |  |  | Med product used for the current drug (MED_PRODUCT) |
| 231 | `RXA_ORG_ACTION_SEQ` | DOUBLE |  |  | The action sequence based on which the dispense was originally created |
| 232 | `RXA_OWE_QTY` | DOUBLE |  |  | Indicates the quantity owed on the current fill |
| 233 | `RXA_PACKAGE_TYPE_ID` | DOUBLE |  |  | Indicates the package type of the current drug |
| 234 | `RXA_PARENT_ORDER_ID` | DOUBLE |  |  | This field contains the order_id of the prescription placed in easy script that was used to create the current order. |
| 235 | `RXA_PARENT_ORIG_ORD_AS_FLAG` | DOUBLE | NOT NULL |  | To store the parent order orig_ord_as_flag value |
| 236 | `RXA_PARENT_PRODUCT_SEQ` | DOUBLE |  |  | For child products of a compound, this points to the parent order_product. |
| 237 | `RXA_PARTIAL_FILL_FLAG` | DOUBLE |  |  | Indicates the type of partial fill 0,"Complete Fills",1, "Partial Fills" |
| 238 | `RXA_PF_REASON_CD` | DOUBLE |  |  | Indicates the reason for partial fill |
| 239 | `RXA_PF_TYPE_CD` | DOUBLE |  |  | Indicates if a health plan supports NCPDP 51 partial fill submission process. |
| 240 | `RXA_PRICE_SCHED_ID` | DOUBLE |  |  | Indicates the price schedule used for the fill |
| 241 | `RXA_PRIOR_AUTH_NBR_TXT` | VARCHAR(250) |  |  | Last health plan's prior authorization number |
| 242 | `RXA_PRIOR_AUTH_TYPE_CD` | DOUBLE |  |  | Last health plan's prior authorization type code |
| 243 | `RXA_PRODUCT_SEQ` | DOUBLE |  |  | Unique sequence for each product. |
| 244 | `RXA_PROXY_PRESCRIBER_ID` | DOUBLE |  |  | Indicates the proxy prescriber of the order |
| 245 | `RXA_REVIEWED_PARENT_ACTION_SEQ` | DOUBLE |  |  | This field contains the action sequence of the parent order that was reviewed by the user that performed the latest fill on the current order. |
| 246 | `RXA_SALES_TAX` | DOUBLE |  |  | RXA Sales Tax |
| 247 | `RXA_SCRIPT_ORIGIN_CD` | DOUBLE |  |  | Indicates how the script originated |
| 248 | `RXA_SOURCE_PARENT_ACTION_SEQ` | DOUBLE |  |  | This field contains the action sequence of the parent order that was used as the source to create the current order. |
| 249 | `RXA_TOTAL_REFILLS` | DOUBLE |  |  | Total refills authorized for the prescription |
| 250 | `RXA_TRANSFER_FLAG` | DOUBLE |  |  | Indicates the type of transfer performed on the order. 0, "None",1, "Internal Transfer-in", 2,"External Transfer-in",3,"External Transfer-out" |
| 251 | `RXA_UC_PRICE` | DOUBLE |  |  | Usual and Customary price |
| 252 | `RXA_VERIFY_RPH_ID` | DOUBLE |  |  | Person_id, of the pharmacist that verified the dispense, from prsnl table |
| 253 | `RXA_XFER_ORDER_ID` | DOUBLE |  |  | Indicates the order that the current order was transferred from/to |
| 254 | `RXA_XFER_SERVICE_RESOURCE_CD` | DOUBLE |  |  | Indicates the service-resource that the current order was transferred from/to |
| 255 | `RXA_XFER_TRANSFER_CD` | DOUBLE |  |  | Indicates the transfer-location that the current order was transferred from/to |
| 256 | `RX_DISP_QTY` | DOUBLE |  |  | rx_disp_qty column |
| 257 | `RX_EXPIRE_DT_NBR` | DOUBLE |  |  | rx_expire_dt_nbr column |
| 258 | `RX_EXPIRE_DT_TM` | DATETIME |  |  | rx_expire_dt_tm column |
| 259 | `RX_EXPIRE_MIN_NBR` | DOUBLE |  |  | rx_expire_min_nbr column |
| 260 | `RX_EXPIRE_TZ` | DOUBLE |  |  | Time zone associated with the corresponding DT_TM column. |
| 261 | `RX_MASK` | DOUBLE |  |  | rx_mask column |
| 262 | `RX_NBR` | DOUBLE |  |  | rx_nbr column |
| 263 | `RX_NBR_CD` | DOUBLE | NOT NULL |  | rx_nbr_cd column |
| 264 | `RX_NBR_STR` | VARCHAR(100) |  |  | rx_nbr_st |
| 265 | `RX_PAY_METHOD_CD` | DOUBLE | NOT NULL |  | rx_pay_method_cd column |
| 266 | `RX_QTY` | DOUBLE |  |  | rx_qty column |
| 267 | `RX_ROUTE_CD` | DOUBLE | NOT NULL |  | rx_route_cd column |
| 268 | `SERVICE_CATEGORY_CD` | DOUBLE | NOT NULL |  | Codified field, which identifies the current category of service the patient is receiving for this encounter. |
| 269 | `SIG` | VARCHAR(255) |  |  | sig column |
| 270 | `SOFT_STOP_DT_NBR` | DOUBLE |  |  | soft_stop_dt_nbr column |
| 271 | `SOFT_STOP_DT_TM` | DATETIME |  |  | soft_stop_dt_tm column |
| 272 | `SOFT_STOP_MIN_NBR` | DOUBLE |  |  | soft_stop_min_nbr column |
| 273 | `SOFT_STOP_TZ` | DOUBLE |  |  | Time zone associated with the corresponding DT_TM column. |
| 274 | `STATUS_PRSNL_ID` | DOUBLE | NOT NULL |  | status_prsnl_id column |
| 275 | `STOP_DT_NBR` | DOUBLE |  |  | stop_dt_nbr column |
| 276 | `STOP_DT_TM` | DATETIME |  |  | stop_dt_tm column |
| 277 | `STOP_MIN_NBR` | DOUBLE |  |  | stop_min_nbr column |
| 278 | `STOP_TYPE_CD` | DOUBLE | NOT NULL |  | stop_type_cd column |
| 279 | `STOP_TZ` | DOUBLE |  |  | Time zone associated with the corresponding DT_TM column. |
| 280 | `STRENGTH_DOSE` | DOUBLE |  |  | strength_dose column |
| 281 | `STRENGTH_DOSE_UNIT_CD` | DOUBLE | NOT NULL |  | strenght_dose_unit_cd |
| 282 | `SUSPEND_DT_NBR` | DOUBLE |  |  | suspend_dt_nbr column |
| 283 | `SUSPEND_DT_TM` | DATETIME |  |  | suspend_dt_tm column |
| 284 | `SUSPEND_EFF_DT_NBR` | DOUBLE |  |  | suspend_eff_dt_nbr column |
| 285 | `SUSPEND_EFF_DT_TM` | DATETIME |  |  | suspend_eff_dt_tm column |
| 286 | `SUSPEND_EFF_MIN_NBR` | DOUBLE |  |  | suspend_eff_min_nbr column |
| 287 | `SUSPEND_EFF_TZ` | DOUBLE |  |  | Time zone associated with the corresponding DT_TM column. |
| 288 | `SUSPEND_IND` | DOUBLE |  |  | suspend_ind column |
| 289 | `SUSPEND_MIN_NBR` | DOUBLE |  |  | suspend_min_nbr column |
| 290 | `SUSPEND_TZ` | DOUBLE |  |  | Time zone associated with the corresponding DT_TM column. |
| 291 | `SYNONYM_ID` | DOUBLE | NOT NULL | FK→ | The synonym_id from the order_catalog_synonym table. |
| 292 | `THERAP_CLASS` | VARCHAR(1000) |  |  | therap_class column |
| 293 | `THERAP_CLASS_ID` | DOUBLE | NOT NULL | FK→ | therap_class_id column |
| 294 | `THERAP_SUB_ALT_REGIMEN_IND` | DOUBLE | NOT NULL |  | Indicates that the substitution to the new medication was accepted but the specific ordering details were not (dose, route, frequency). |
| 295 | `THERAP_SUB_DOSE_FREE_TXT` | VARCHAR(100) |  |  | Free text of the medication originally ordered. |
| 296 | `THERAP_SUB_DT_TM` | DATETIME |  |  | The date of the substitution. |
| 297 | `THERAP_SUB_FREQ_CD` | DOUBLE | NOT NULL |  | Dosing frequency of the original medication. |
| 298 | `THERAP_SUB_ITEM_ID` | DOUBLE | NOT NULL |  | The item ID of the medication originally ordered. |
| 299 | `THERAP_SUB_OVERRIDE_IND` | DOUBLE | NOT NULL |  | Indicates that the suggested therapeutic substitution was not taken. |
| 300 | `THERAP_SUB_OVERRIDE_RSN_CD` | DOUBLE | NOT NULL |  | The reason that the suggested therapeutic substitution was not taken. |
| 301 | `THERAP_SUB_PERSON_OWN_MEDS_IND` | DOUBLE | NOT NULL |  | Indicates that the substitution was not taken since the patient brought in their own supply of the medication. |
| 302 | `THERAP_SUB_ROUTE_CD` | DOUBLE | NOT NULL |  | Route of administration of the medication originally ordered. |
| 303 | `THERAP_SUB_STRENGTH_UNIT_CD` | DOUBLE | NOT NULL |  | The unit of measure associated with the strength of this medication. |
| 304 | `THERAP_SUB_STRENGTH_VALUE` | DOUBLE | NOT NULL |  | The strength of the medication originally ordered. |
| 305 | `THERAP_SUB_VOLUME_UNIT_CD` | DOUBLE | NOT NULL |  | The unit of measure for the volume of the medication originally ordered. |
| 306 | `THERAP_SUB_VOLUME_VALUE` | DOUBLE | NOT NULL |  | The volume of the medication originally ordered. |
| 307 | `TNF_ID` | DOUBLE | NOT NULL |  | Key to template_non-formulary table |
| 308 | `TOTAL_RX_QTY` | DOUBLE |  |  | total_rx_qty column |
| 309 | `TRACK_NBR` | DOUBLE |  |  | track_nbr column |
| 310 | `TRACK_NBR_CD` | DOUBLE | NOT NULL |  | CODE VALUE FROM CODE SET 4503 |
| 311 | `TRANSFER_CNT` | DOUBLE |  |  | transfer_cnt column |
| 312 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 313 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 314 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 315 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 316 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `DISPENSE_HX_ID` | [DISPENSE_HX](DISPENSE_HX.md) | `DISPENSE_HX_ID` |
| `ENCNTR_ID` | [ENCOUNTER](ENCOUNTER.md) | `ENCNTR_ID` |
| `HEALTH_PLAN_ID` | [HEALTH_PLAN](HEALTH_PLAN.md) | `HEALTH_PLAN_ID` |
| `ICD9_NOMEN_ID` | [NOMENCLATURE](NOMENCLATURE.md) | `NOMENCLATURE_ID` |
| `ING_SYNONYM_ID` | [ORDER_CATALOG_SYNONYM](ORDER_CATALOG_SYNONYM.md) | `SYNONYM_ID` |
| `ITEM_ID` | [ITEM_DEFINITION](ITEM_DEFINITION.md) | `ITEM_ID` |
| `MANF_ITEM_ID` | [MANUFACTURER_ITEM](MANUFACTURER_ITEM.md) | `ITEM_ID` |
| `ORDER_ID` | [ORDERS](ORDERS.md) | `ORDER_ID` |
| `ORGANIZATION_ID` | [ORGANIZATION](ORGANIZATION.md) | `ORGANIZATION_ID` |
| `PARENT_THERAP_CLASS_ID` | [ALT_SEL_CAT](ALT_SEL_CAT.md) | `ALT_SEL_CATEGORY_ID` |
| `PERSON_ID` | [PERSON](PERSON.md) | `PERSON_ID` |
| `PROD_VLDTN_PRSNL_ID` | [PRSNL](PRSNL.md) | `PERSON_ID` |
| `ROOT_THERAP_CLASS_ID` | [ALT_SEL_CAT](ALT_SEL_CAT.md) | `ALT_SEL_CATEGORY_ID` |
| `SYNONYM_ID` | [ORDER_CATALOG_SYNONYM](ORDER_CATALOG_SYNONYM.md) | `SYNONYM_ID` |
| `THERAP_CLASS_ID` | [ALT_SEL_CAT](ALT_SEL_CAT.md) | `ALT_SEL_CATEGORY_ID` |

