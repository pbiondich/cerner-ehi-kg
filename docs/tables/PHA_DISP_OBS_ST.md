# PHA_DISP_OBS_ST

> Observation set of PharmNet's activity data at the order dispense level. Used to generate Drug Utilization Evaluation (DUE) reports.

**Description:** pha_disp_obs_st  
**Table type:** ACTIVITY  
**Primary key:** _(not published — see note)_  
**Columns:** 267

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ACTION_DT_NBR` | DOUBLE |  |  | the Julian value of the action date of an order |
| 2 | `ACTION_DT_TM` | DATETIME |  |  | the action date/time of an order |
| 3 | `ACTION_MIN_NBR` | DOUBLE |  |  | the time value in minutes of the action time of an order |
| 4 | `ACTION_PRSNL_ID` | DOUBLE | NOT NULL |  | the personnel identifier of the user performing the action |
| 5 | `ACTION_QUAL_CD` | DOUBLE |  |  | A codified value that helps describe the action that occurred. |
| 6 | `ACTION_REJECTED_IND` | DOUBLE |  |  | indicates whether the action performed is a reject |
| 7 | `ACTION_SEQ` | DOUBLE | NOT NULL |  | sequence of the action |
| 8 | `ACTION_TYPE_CD` | DOUBLE | NOT NULL |  | Action that is requested |
| 9 | `ACTION_TZ` | DOUBLE |  |  | Time zone associated with the corresponding DT_TM column. |
| 10 | `CANCEL_REASON_CD` | DOUBLE | NOT NULL |  | reason that an action was cancelled |
| 11 | `CHARGE_IND` | DOUBLE |  |  | indicates if the order has been or is to be charged |
| 12 | `CKI` | VARCHAR(255) |  |  | CKI value |
| 13 | `CONTRIBUTOR_SYSTEM_CD` | DOUBLE | NOT NULL |  | Contributor system identifies the source feed of data from which a row was populated. This is mainly used to determine how to update a set of data that may have originated from more than one source feed. |
| 14 | `COPAY` | DOUBLE |  |  | copay value |
| 15 | `COSIGN_OVERRIDE_OPTION_CD` | DOUBLE | NOT NULL |  | Determines if Physician Cosign is required for external order entry systems. |
| 16 | `COSIGN_OVERRIDE_REASON_CD` | DOUBLE | NOT NULL |  | The reason Physician Cosign has been overridden from the system determined value. |
| 17 | `COST` | DOUBLE |  |  | Total cost for the dispense |
| 18 | `CUR_DEPT_STATUS_CD` | DOUBLE | NOT NULL |  | current departmental status of an order |
| 19 | `CUR_ORDER_STATUS_CD` | DOUBLE | NOT NULL |  | ** OBSOLETE - NO LONGER USED **cur_order_status_cd |
| 20 | `CUR_START_DT_NBR` | DOUBLE |  |  | the Julian date of an order's start date |
| 21 | `CUR_START_DT_TM` | DATETIME |  |  | The start dt/tm of this order |
| 22 | `CUR_START_MIN_NBR` | DOUBLE |  |  | the time value in minutes of the start time of an order |
| 23 | `CUR_START_TZ` | DOUBLE |  |  | Time zone associated with the corresponding DT_TM column. |
| 24 | `DAW_CD` | DOUBLE | NOT NULL |  | dispense as written code |
| 25 | `DC_REASON_CD` | DOUBLE | NOT NULL |  | reason that an order was discontinued |
| 26 | `DEPT_MISC_LINE` | VARCHAR(255) |  |  | text filled by department |
| 27 | `DEPT_STATUS_CD` | DOUBLE | NOT NULL |  | departmental status of the order |
| 28 | `DISCONTINUE_EFF_DT_NBR` | DOUBLE |  |  | the Julian value of the discontinue date of an order |
| 29 | `DISCONTINUE_EFF_DT_TM` | DATETIME |  |  | date and time the discontinue action should become effective for the order |
| 30 | `DISCONTINUE_EFF_MIN_NBR` | DOUBLE |  |  | the time value in minutes of the discontinue time |
| 31 | `DISCONTINUE_EFF_TZ` | DOUBLE |  |  | Time zone associated with the corresponding DT_TM column. |
| 32 | `DISCONTINUE_IND` | DOUBLE |  |  | indicator on whether this order has been discontinued |
| 33 | `DISCONTINUE_TYPE_CD` | DOUBLE | NOT NULL |  | Code set 4038: Indicates what method the order was discontinued |
| 34 | `DISPENSE_HX_ID` | DOUBLE | NOT NULL | FK→ | the id from dispense_hx for an order's dispense event |
| 35 | `DISP_CATEGORY_CD` | DOUBLE | NOT NULL |  | Code set 4008: Indicates the method to calculate dispense doses and charging method |
| 36 | `DISP_DT_NBR` | DOUBLE |  |  | the Julian date of an order's dispense date |
| 37 | `DISP_DT_TM` | DATETIME |  |  | the dispense dt/tm of an order's dispense |
| 38 | `DISP_EVENT_TYPE_CD` | DOUBLE | NOT NULL |  | the dispense type of an order's event |
| 39 | `DISP_FROM_LOC_CD` | DOUBLE | NOT NULL |  | the dispense location of an order's dispense |
| 40 | `DISP_FROM_SR_CD` | DOUBLE | NOT NULL |  | the service resource code value associated to the dispense from location |
| 41 | `DISP_MIN_NBR` | DOUBLE |  |  | the time value in minutes of a dispense |
| 42 | `DISP_PERS_BED_CD` | DOUBLE | NOT NULL |  | the bed code value of the patient's location |
| 43 | `DISP_PERS_BLD_CD` | DOUBLE | NOT NULL |  | the building code value of the patient's location |
| 44 | `DISP_PERS_FAC_CD` | DOUBLE | NOT NULL |  | the facility code value of the patient's location |
| 45 | `DISP_PERS_NU2_GRP_CD` | DOUBLE | NOT NULL |  | The nurse unit grouping code |
| 46 | `DISP_PERS_NU_CD` | DOUBLE | NOT NULL |  | the nurse unit code value of the patient's location |
| 47 | `DISP_PERS_NU_GRP_CD` | DOUBLE | NOT NULL |  | The nurse unit grouping code |
| 48 | `DISP_PERS_ROOM_CD` | DOUBLE | NOT NULL |  | the room code value of the patient's location |
| 49 | `DISP_PRIORITY_CD` | DOUBLE | NOT NULL |  | the priority code of an order |
| 50 | `DISP_QTY` | DOUBLE |  |  | the amount to dispense for an order |
| 51 | `DISP_QTY_UNIT_CD` | DOUBLE | NOT NULL |  | the unit of the amount to dispense |
| 52 | `DISP_SHIFT2_GRP_CD` | DOUBLE | NOT NULL |  | Pharmacy shifts |
| 53 | `DISP_SHIFT_GRP_CD` | DOUBLE | NOT NULL |  | The shift grouping code |
| 54 | `DISP_SR_CD` | DOUBLE | NOT NULL |  | the service resource code value associated to the dispense from location |
| 55 | `DISP_TZ` | DOUBLE |  |  | Time zone associated with the corresponding DT_TM column. For inpatient rows, this is the time zone of the encounter. For Retail Pharmacy, it is the time zone of the pharmacy's facility. |
| 56 | `DOSES` | DOUBLE |  |  | number of doses dispensed |
| 57 | `EARLY_REASON_CD` | DOUBLE | NOT NULL |  | Reason for an early refill |
| 58 | `EFFECTIVE_DT_NBR` | DOUBLE |  |  | Effective Date Number value |
| 59 | `EFFECTIVE_DT_TM` | DATETIME |  |  | Effective Date and Time value |
| 60 | `EFFECTIVE_MIN_NBR` | DOUBLE |  |  | Effective Minute number value |
| 61 | `EFFECTIVE_TZ` | DOUBLE |  |  | Time zone associated with the corresponding DT_TM column. |
| 62 | `ENCNTR_ID` | DOUBLE | NOT NULL | FK→ | This is the value of the unique primary identifier of the encounter table. It is an internal system assigned number. |
| 63 | `EXPIRE_DT_NBR` | DOUBLE |  |  | the Julian value of the expire date of the order |
| 64 | `EXPIRE_DT_TM` | DATETIME |  |  | expire date and time value |
| 65 | `EXPIRE_MIN_NBR` | DOUBLE |  |  | the time value in minutes of the expire time of an order |
| 66 | `EXPIRE_TZ` | DOUBLE |  |  | Time zone associated with the corresponding DT_TM column. |
| 67 | `EXTRA_REASON_CD` | DOUBLE | NOT NULL |  | the reason for an extra dose event |
| 68 | `FILL_NBR` | DOUBLE |  |  | Retail Fill number for dispense transaction |
| 69 | `FIRST_DOSE_DT_NBR` | DOUBLE |  |  | the Julian date of a first dose event |
| 70 | `FIRST_DOSE_DT_TM` | DATETIME |  |  | the date/time of a first dose event |
| 71 | `FIRST_DOSE_MIN_NBR` | DOUBLE |  |  | the time value in minutes of a first dose event |
| 72 | `FIRST_DOSE_TZ` | DOUBLE |  |  | Time zone associated with the corresponding DT_TM column. |
| 73 | `FLOORSTOCK_IND` | DOUBLE |  |  | indicates if the order is dispensed from the floor |
| 74 | `FLOORSTOCK_OVERRIDE_IND` | DOUBLE |  |  | indicates if the user changed the dispense location to a floorstock (1) or non-floorstock (2) |
| 75 | `FREQ_CD` | DOUBLE | NOT NULL |  | the frequency code value associated to an order |
| 76 | `HEALTH_PLAN_ID` | DOUBLE | NOT NULL | FK→ | health_plan_id |
| 77 | `ICD9_NOMEN_ID` | DOUBLE | NOT NULL | FK→ | Diagnosis Nomenclature Identifier |
| 78 | `IGNORE_IND` | DOUBLE |  |  | indicates if the order is to not qualify on the fill list; 1 = ignore, 0 = fill as instructed |
| 79 | `INACTIVE_FLAG` | DOUBLE |  |  | Identifies if the order is inactive |
| 80 | `INCOMPLETE_ORDER_IND` | DOUBLE |  |  | indicates the order is missing required details |
| 81 | `INGREDIENT_IND` | DOUBLE | NOT NULL |  | an indicator on whether this order has multiple ingredients. |
| 82 | `LAST_FILL_STATUS_CD` | DOUBLE | NOT NULL |  | The code for the last fill batch status. |
| 83 | `LAST_REFILL_DT_NBR` | DOUBLE |  |  | the Julian date of when the order was last refilled |
| 84 | `LAST_REFILL_DT_TM` | DATETIME |  |  | the date and time of when the order was last refilled |
| 85 | `LAST_REFILL_MIN_NBR` | DOUBLE |  |  | the time in minutes of when the order was last refilled |
| 86 | `LAST_REFILL_TZ` | DOUBLE |  |  | Time zone associated with the corresponding DT_TM column. |
| 87 | `LAST_UPDT_PROVIDER_ID` | DOUBLE | NOT NULL |  | the personnel identifier of the provider that last updated the order |
| 88 | `LATE_REASON_CD` | DOUBLE | NOT NULL |  | later_reason_cd |
| 89 | `LEGAL_STATUS_CD` | DOUBLE | NOT NULL |  | Legal Status Code value |
| 90 | `MED_ORDER_TYPE_CD` | DOUBLE | NOT NULL |  | the medication order type code value of the order |
| 91 | `MED_SERVICE_CD` | DOUBLE | NOT NULL |  | The type or category of medical service that the patient is receiving in relation to their encounter. The category may be of treatment type, surgery, general resources, or others. |
| 92 | `NEED_RX_CLIN_REVIEW_FLAG` | DOUBLE |  |  | Flag for identifying whether the order's clinical review has been completed or not. |
| 93 | `NEED_RX_PROD_ASSIGN_FLAG` | DOUBLE |  |  | Flag for identifying whether the order's product assignment has been completed or not. |
| 94 | `NEED_RX_VERIFY_IND` | DOUBLE |  |  | indicates if the order needs verification from pharmacist |
| 95 | `NEED_VERIFY_IND` | DOUBLE |  |  | indicates if the order has been verified |
| 96 | `NEXT_DISP_DT_NBR` | DOUBLE |  |  | The next dispense date in number of days |
| 97 | `NEXT_DISP_DT_TM` | DATETIME |  |  | The next dispense date and time in calendar format |
| 98 | `NEXT_DISP_MIN_NBR` | DOUBLE |  |  | The next dispense time in minutes |
| 99 | `NEXT_DISP_TZ` | DOUBLE |  |  | Time zone associated with the corresponding DT_TM column. For inpatient rows, this is the time zone of the encounter. For Retail Pharmacy, it is the time zone of the pharmacy's facility. |
| 100 | `ORDERABLE_TYPE_FLAG` | DOUBLE |  |  | indicates what type of orderable procedure the item has been assigned |
| 101 | `ORDERING_PROVIDER_ID` | DOUBLE | NOT NULL |  | the personnel id of the provider of the order |
| 102 | `ORDER_CATALOG_CD` | DOUBLE | NOT NULL |  | The catalog code associated to the order |
| 103 | `ORDER_CATALOG_TYPE_CD` | DOUBLE | NOT NULL |  | Internal code for catalog type. |
| 104 | `ORDER_ID` | DOUBLE | NOT NULL | FK→ | Order Id from the orders table |
| 105 | `ORDER_INCOMP_ORDER_IND` | DOUBLE |  |  | indicates if a required detail is missing on an order |
| 106 | `ORDER_LOC_CD` | DOUBLE | NOT NULL |  | Location code of an order |
| 107 | `ORDER_PRIOIRTY_CD` | DOUBLE | NOT NULL |  | order_priority_cd |
| 108 | `ORDER_PRIORITY_CD` | DOUBLE | NOT NULL |  | ORDER_PRIORITY_CD |
| 109 | `ORDER_STATUS_CD` | DOUBLE | NOT NULL |  | status code value of an order |
| 110 | `ORDER_TYPE_FLAG` | DOUBLE |  |  | the medication order type of the order |
| 111 | `ORD_PERS_AGE_DAYS` | DOUBLE |  |  | number of days a person's age is |
| 112 | `ORD_PERS_AGE_YEARS` | DOUBLE |  |  | number of years a person's age is |
| 113 | `ORD_PERS_BED_CD` | DOUBLE | NOT NULL |  | the bed code value of the patient's location |
| 114 | `ORD_PERS_BLD_CD` | DOUBLE | NOT NULL |  | the building code value of the patient's location |
| 115 | `ORD_PERS_FAC_CD` | DOUBLE | NOT NULL |  | the facility code value of the patient's location |
| 116 | `ORD_PERS_NU_CD` | DOUBLE | NOT NULL |  | the nurse unit code value of the patient's location |
| 117 | `ORD_PERS_NU_GRP2_CD` | DOUBLE | NOT NULL |  | The nurse unit grouping code |
| 118 | `ORD_PERS_NU_GRP_CD` | DOUBLE | NOT NULL |  | The nurse unit grouping code |
| 119 | `ORD_PERS_ROOM_CD` | DOUBLE | NOT NULL |  | the room code value of the patient's location |
| 120 | `ORD_PERS_ZIP` | VARCHAR(25) |  |  | the zip code of a patient's address |
| 121 | `ORGANIZATION_ID` | DOUBLE | NOT NULL | FK→ | organization_id |
| 122 | `ORIG_ORDER_DT_NBR` | DOUBLE |  |  | the Julian value of the order date |
| 123 | `ORIG_ORDER_DT_TM` | DATETIME |  |  | the date time the order was created |
| 124 | `ORIG_ORDER_MIN_NBR` | DOUBLE |  |  | the time value of the order time in minutes |
| 125 | `ORIG_ORDER_TZ` | DOUBLE |  |  | Time zone associated with the corresponding DT_TM column. |
| 126 | `ORIG_ORD_AS_FLAG` | DOUBLE | NOT NULL |  | the flag show how this order was originally placed. |
| 127 | `PAR_DOSES` | DOUBLE |  |  | the PRN or PAR doses of an order |
| 128 | `PERSON_ID` | DOUBLE | NOT NULL | FK→ | This is the value of the unique primary identifier of the person table. It is an internal system assigned number. |
| 129 | `PERSON_OWE_QTY` | DOUBLE | NOT NULL |  | Amount owed for a person for a product of an order. |
| 130 | `PHARM_ORDER_TYPE_FLAG` | DOUBLE |  |  | The order type of an order |
| 131 | `PHARM_TYPE_CD` | DOUBLE | NOT NULL |  | The pharm_type_cd |
| 132 | `PHYSICIAN_DEA_TXT` | VARCHAR(200) |  |  | DEA number of the prescribing physician |
| 133 | `PREV_DISP_DT_NBR` | DOUBLE |  |  | The previous dispense date in number of days |
| 134 | `PREV_DISP_DT_TM` | DATETIME |  |  | The previous dispense date/time in calendar format |
| 135 | `PREV_DISP_MIN_NBR` | DOUBLE |  |  | The previous dispense time in minutes |
| 136 | `PREV_DISP_TZ` | DOUBLE |  |  | Time zone associated with the corresponding DT_TM column. For inpatient rows, this is the time zone of the encounter. For Retail Pharmacy, it is the time zone of the pharmacy's facility. |
| 137 | `PRICE` | DOUBLE |  |  | Total price for the dispense |
| 138 | `PRICE_CODE_CD` | DOUBLE | NOT NULL |  | The price schedule code value of an order |
| 139 | `PRN_IND` | DOUBLE |  |  | Indicates that the order is PRN |
| 140 | `PROD_VLDTN_DT_TM` | DATETIME |  |  | Identifies the most recent validation date/time. |
| 141 | `PROD_VLDTN_ERROR_IND` | DOUBLE | NOT NULL |  | Indicates if an error occurred during scanning. |
| 142 | `PROD_VLDTN_IND` | DOUBLE | NOT NULL |  | Indicator to determine if product validation occurred on a dispense. |
| 143 | `PROD_VLDTN_OVERRIDE_IND` | DOUBLE | NOT NULL |  | Indicator to determine if the user overrides a scan failure. |
| 144 | `PROD_VLDTN_OVERRIDE_REASON_CD` | DOUBLE | NOT NULL |  | Identifies the reason a user selects to override a validation event. |
| 145 | `PROD_VLDTN_PRSNL_ID` | DOUBLE | NOT NULL | FK→ | The user who last performed a validation event. |
| 146 | `PROD_VLDTN_RPH_IND` | DOUBLE | NOT NULL |  | Indicates if any events were performed by a pharmacist. |
| 147 | `PROD_VLDTN_TECH_IND` | DOUBLE | NOT NULL |  | Indicates if any events were performed by a pharmacy technician. |
| 148 | `PROD_VLDTN_TZ` | DOUBLE | NOT NULL |  | The time zone associated with PROD_VLDTN_DT_TM. |
| 149 | `PROJECTED_STOP_DT_NBR` | DOUBLE |  |  | The projected stop date in number of days |
| 150 | `PROJECTED_STOP_DT_TM` | DATETIME |  |  | The projected stop date and time in calendar format |
| 151 | `PROJECTED_STOP_MIN_NBR` | DOUBLE |  |  | The projected stop time in number of minutes |
| 152 | `PROJECTED_STOP_TZ` | DOUBLE |  |  | Time zone associated with the corresponding DT_TM column. |
| 153 | `QTY_REMAINING` | DOUBLE |  |  | The remaining quantity of an order |
| 154 | `REASON_CD` | DOUBLE | NOT NULL |  | reason_cd |
| 155 | `REFILLS_REMAINING` | DOUBLE |  |  | number of refills remaining |
| 156 | `REFILL_QTY` | DOUBLE |  |  | the amount to refill for a retail order |
| 157 | `REIMBURSEMENT_AMT` | DOUBLE |  |  | Reimbursement Amount for this dispense transaction |
| 158 | `RENEW_REASON_CD` | DOUBLE | NOT NULL |  | the reason a renew action occurred |
| 159 | `REPLACE_EVERY` | DOUBLE |  |  | the replace every value of an order |
| 160 | `REPLACE_EVERY_CD` | DOUBLE | NOT NULL |  | the unit of measure for the replace every value of an order |
| 161 | `REQ_START_DT_NBR` | DOUBLE |  |  | the Julian date of an order's requested start |
| 162 | `REQ_START_DT_TM` | DATETIME |  |  | the requested start date/time of an order |
| 163 | `REQ_START_MIN_NBR` | DOUBLE |  |  | the time value in minutes for an order's start time |
| 164 | `REQ_START_TZ` | DOUBLE |  |  | Time zone associated with the corresponding DT_TM column. |
| 165 | `RESUME_DT_NBR` | DOUBLE |  |  | the Julian date of an order's resume action |
| 166 | `RESUME_DT_TM` | DATETIME |  |  | the date/time of an order's resume action |
| 167 | `RESUME_EFF_DT_NBR` | DOUBLE |  |  | the Julian date of an order's effective resume action date |
| 168 | `RESUME_EFF_DT_TM` | DATETIME |  |  | the date/time of an order's effective resume action date/time |
| 169 | `RESUME_EFF_MIN_NBR` | DOUBLE |  |  | the time value in minutes of an order's effective resume action time |
| 170 | `RESUME_EFF_TZ` | DOUBLE |  |  | Time zone associated with the corresponding DT_TM column. |
| 171 | `RESUME_MIN_NBR` | DOUBLE |  |  | the time value in minutes of an order's resume action |
| 172 | `RESUME_REASON_CD` | DOUBLE | NOT NULL |  | the reason a resume action occurs |
| 173 | `RESUME_TZ` | DOUBLE |  |  | Time zone associated with the corresponding DT_TM column. |
| 174 | `RUN_USER_ID` | DOUBLE | NOT NULL |  | ID of the user generating the dispense event |
| 175 | `RXA_AUTH_NBR_TXT` | VARCHAR(250) |  |  | Last Authorization number received from health plan |
| 176 | `RXA_BACKWARD_ORDER_ID` | DOUBLE |  |  | Indicates the order based on which the current order was placed |
| 177 | `RXA_BILL_QTY` | DOUBLE |  |  | Indicates the quantity billed for the current fill |
| 178 | `RXA_CHECK_RPH_ID` | DOUBLE |  |  | Person_id, of the pharmacist that checked the dispense, from prsnl table |
| 179 | `RXA_CHRG_CDM` | VARCHAR(250) |  |  | CDM number used in charging the dispense |
| 180 | `RXA_CHRG_DISPENSE_HX_ID` | DOUBLE |  |  | The dispense record that is being cancelled by the current dispense |
| 181 | `RXA_CLAIM_FLAG` | DOUBLE |  |  | Indicates whether the current fill has been claimed 0,"None",1,"Non-Adjudicated",2,"Adjudicated" |
| 182 | `RXA_CLAIM_STATUS_CD` | DOUBLE |  |  | Indicates the status of the claim transaction for last health plan |
| 183 | `RXA_COB_FLAG` | DOUBLE |  |  | Indicates whether co-ordination of benefits was used in claiming this fill 0, "None", 1,"Non-COB", 2,"COB" |
| 184 | `RXA_COMPLETED_USER_ID` | DOUBLE |  |  | Person_id, of the user that completed the dispense, from prsnl table |
| 185 | `RXA_CONTROL_NBR_TXT` | VARCHAR(250) |  |  | Control number for the script |
| 186 | `RXA_CRDT_DISPENSE_HX_ID` | DOUBLE |  |  | The dispense record that credited the current dispense PHA_PRODUCT_DISPENSE_HX_ST |
| 187 | `RXA_DAYS_SUPPLY` | DOUBLE |  |  | Indicates the days for which the current fill will last |
| 188 | `RXA_DISCOUNT_AMT` | DOUBLE |  |  | RXA Discount Amount |
| 189 | `RXA_DISPENSE_FEE` | DOUBLE |  |  | RXA Dispense Fee |
| 190 | `RXA_DISP_COMPLETE_FLAG` | DOUBLE |  |  | Indicates whether a dispense is complete. 0, "In-Complete",1, "Complete" |
| 191 | `RXA_DISP_PRIORITY_DT_TM` | DATETIME |  |  | Priority Date/Time for the dispense |
| 192 | `RXA_DISP_PRIORITY_DT_TZ` | DOUBLE |  |  | Priority Date/Time for the dispense |
| 193 | `RXA_DISP_STAT_CD` | DOUBLE |  |  | Latest dispense status of the dispense. |
| 194 | `RXA_DUR_FLAG` | DOUBLE |  |  | Indicates whether last health plan performed drug utilization review 0,"None",1, "NO DUR Performed", 2, "DUR Performed" |
| 195 | `RXA_EXPANDED_SIG_ID` | DOUBLE |  |  | Order comment of type "PHARMSIG". Long_text_id from long_text table |
| 196 | `RXA_FILL_DEVICE_SR_CD` | DOUBLE |  |  | To store the pharmacy filling device value. |
| 197 | `RXA_FILL_LOCATION_SR_CD` | DOUBLE |  |  | To store the pharmacy filling location value |
| 198 | `RXA_FILL_RPH_ID` | DOUBLE |  |  | Person_id. of the pharmacist that filled the dispense, from prsnl table |
| 199 | `RXA_FORWARD_ORDER_ID` | DOUBLE |  |  | Indicates the order that was placed based off of the current order |
| 200 | `RXA_HEALTH_PLAN_SEQ` | DOUBLE |  |  | The sequence of the last health plan in the list of health plans used for this prescription |
| 201 | `RXA_INCENTIVE_AMT` | DOUBLE |  |  | RXA Incentive Amount |
| 202 | `RXA_LEVEL5_CD` | DOUBLE |  |  | work station that requested the event |
| 203 | `RXA_ORG_ACTION_SEQ` | DOUBLE |  |  | The action sequence based on which the dispense was originally created |
| 204 | `RXA_OWE_QTY` | DOUBLE |  |  | Indicates the quantity owed on the current fill |
| 205 | `RXA_PARENT_ORDER_ID` | DOUBLE |  |  | This field contains the order_id of the prescription placed in easy script that was used to create the current order. |
| 206 | `RXA_PARENT_ORIG_ORD_AS_FLAG` | DOUBLE | NOT NULL |  | To store the parent order orig_ord_as_flag value |
| 207 | `RXA_PARTIAL_FILL_FLAG` | DOUBLE |  |  | Indicates the type of partial fill 0,"Complete Fills",1, "Partial Fills" |
| 208 | `RXA_PF_REASON_CD` | DOUBLE |  |  | Indicates the reason for partial fill |
| 209 | `RXA_PF_TYPE_CD` | DOUBLE |  |  | Indicates if a health plan supports NCPDP 51 partial fill submission process. |
| 210 | `RXA_PRICE_SCHED_ID` | DOUBLE |  |  | Indicates the price schedule used for the fill |
| 211 | `RXA_PROXY_PRESCRIBER_ID` | DOUBLE |  |  | Indicates the proxy prescriber of the order |
| 212 | `RXA_REVIEWED_PARENT_ACTION_SEQ` | DOUBLE |  |  | This field contains the action sequence of the parent order that was reviewed by the user that performed the latest fill on the current order. |
| 213 | `RXA_SALES_TAX` | DOUBLE |  |  | RXA Sales Tax |
| 214 | `RXA_SCRIPT_ORIGIN_CD` | DOUBLE |  |  | Indicates how the script originated |
| 215 | `RXA_SOURCE_PARENT_ACTION_SEQ` | DOUBLE |  |  | This field contains the action sequence of the parent order that was used as the source to create the current order. |
| 216 | `RXA_TOTAL_REFILLS` | DOUBLE |  |  | Total refills authorized for the prescription |
| 217 | `RXA_TRANSFER_FLAG` | DOUBLE |  |  | Indicates the type of transfer performed on the order. 0, "None",1, "Internal Transfer-in", 2,"External Transfer-in",3,"External Transfer-out" |
| 218 | `RXA_UC_PRICE` | DOUBLE |  |  | Usual and Customary price |
| 219 | `RXA_VERIFY_RPH_ID` | DOUBLE |  |  | Person_id, of the pharmacist that verified the dispense, from prsnl table |
| 220 | `RXA_XFER_ORDER_ID` | DOUBLE |  |  | Indicates the order that the current order was transferred from/to |
| 221 | `RXA_XFER_SERVICE_RESOURCE_CD` | DOUBLE |  |  | Indicates the service-resource that the current order was transferred from/to |
| 222 | `RXA_XFER_TRANSFER_CD` | DOUBLE |  |  | Indicates the transfer-location that the current order was transferred from/to |
| 223 | `RX_DISP_QTY` | DOUBLE |  |  | The retail quantity dispensed |
| 224 | `RX_EXPIRE_DT_NBR` | DOUBLE |  |  | the Julian date of an order's expire date |
| 225 | `RX_EXPIRE_DT_TM` | DATETIME |  |  | the date/time of an order's expire date/time |
| 226 | `RX_EXPIRE_MIN_NBR` | DOUBLE |  |  | the time value in minutes of an order's expire time |
| 227 | `RX_EXPIRE_TZ` | DOUBLE |  |  | Time zone associated with the corresponding DT_TM column. |
| 228 | `RX_MASK` | DOUBLE |  |  | pharmacy mask showing how this order was placed |
| 229 | `RX_NBR` | DOUBLE |  |  | retail number |
| 230 | `RX_NBR_CD` | DOUBLE | NOT NULL |  | Prescription number |
| 231 | `RX_NBR_STR` | VARCHAR(100) |  |  | Formatted Prescription Number |
| 232 | `RX_PAY_METHOD_CD` | DOUBLE | NOT NULL |  | The retail payment method. |
| 233 | `RX_QTY` | DOUBLE |  |  | Intial Quantity Prescribed |
| 234 | `RX_ROUTE_CD` | DOUBLE | NOT NULL |  | the pharmacy route associated to an order |
| 235 | `SERVICE_CATEGORY_CD` | DOUBLE | NOT NULL |  | Codified field, which identifies the current category of service the patient is receiving for this encounter. |
| 236 | `SIG` | VARCHAR(255) |  |  | dosing and administering instructions |
| 237 | `SOFT_STOP_DT_NBR` | DOUBLE |  |  | the Julian date of an order's soft stop date |
| 238 | `SOFT_STOP_DT_TM` | DATETIME |  |  | the stop date/time of an order's soft stop |
| 239 | `SOFT_STOP_MIN_NBR` | DOUBLE |  |  | the time value in minutes for an order's soft stop time |
| 240 | `SOFT_STOP_TZ` | DOUBLE |  |  | Time zone associated with the corresponding DT_TM column. |
| 241 | `STATUS_PRSNL_ID` | DOUBLE | NOT NULL |  | Id of the prsnl row that updated the status. |
| 242 | `STOP_DT_NBR` | DOUBLE |  |  | the Julian date of an order's stop date |
| 243 | `STOP_DT_TM` | DATETIME |  |  | the stop date/time of an order |
| 244 | `STOP_MIN_NBR` | DOUBLE |  |  | the time value in minutes of an order's stop time |
| 245 | `STOP_TYPE_CD` | DOUBLE | NOT NULL |  | the stop type policy of an order |
| 246 | `STOP_TZ` | DOUBLE |  |  | Time zone associated with the corresponding DT_TM column. |
| 247 | `STRENGTH_DOSE` | DOUBLE |  |  | the strength of an order |
| 248 | `STRENGTH_DOSE_UNIT_CD` | DOUBLE | NOT NULL |  | the strength unit of measure of an order |
| 249 | `SUSPEND_DT_NBR` | DOUBLE |  |  | the Julian date of an order's suspend |
| 250 | `SUSPEND_DT_TM` | DATETIME |  |  | the date/time of an order's suspend action |
| 251 | `SUSPEND_EFF_DT_NBR` | DOUBLE |  |  | the Julian date of an order's effective suspend action |
| 252 | `SUSPEND_EFF_DT_TM` | DATETIME |  |  | the date/time of an order's effective suspend action |
| 253 | `SUSPEND_EFF_MIN_NBR` | DOUBLE |  |  | the time value in minutes of an order's effective suspend time |
| 254 | `SUSPEND_EFF_TZ` | DOUBLE |  |  | Time zone associated with the corresponding DT_TM column. |
| 255 | `SUSPEND_IND` | DOUBLE |  |  | indicates if the order is suspended |
| 256 | `SUSPEND_MIN_NBR` | DOUBLE |  |  | the time value in minutes of an order's suspend time |
| 257 | `SUSPEND_TZ` | DOUBLE |  |  | Time zone associated with the corresponding DT_TM column. |
| 258 | `SYNONYM_ID` | DOUBLE | NOT NULL | FK→ | The synonym_id from the order_catalog_synonym table. |
| 259 | `TOTAL_RX_QTY` | DOUBLE |  |  | Total Quantity Prescribed |
| 260 | `TRACK_NBR` | DOUBLE |  |  | A number to track a dispensed prescription |
| 261 | `TRACK_NBR_CD` | DOUBLE | NOT NULL |  | CODE VALUE FROM CODE SET 4502 |
| 262 | `TRANSFER_CNT` | DOUBLE |  |  | The number of times a prescription got transferred |
| 263 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 264 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 265 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 266 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 267 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `DISPENSE_HX_ID` | [DISPENSE_HX](DISPENSE_HX.md) | `DISPENSE_HX_ID` |
| `ENCNTR_ID` | [ENCOUNTER](ENCOUNTER.md) | `ENCNTR_ID` |
| `HEALTH_PLAN_ID` | [HEALTH_PLAN](HEALTH_PLAN.md) | `HEALTH_PLAN_ID` |
| `ICD9_NOMEN_ID` | [NOMENCLATURE](NOMENCLATURE.md) | `NOMENCLATURE_ID` |
| `ORDER_ID` | [ORDERS](ORDERS.md) | `ORDER_ID` |
| `ORGANIZATION_ID` | [ORGANIZATION](ORGANIZATION.md) | `ORGANIZATION_ID` |
| `PERSON_ID` | [PERSON](PERSON.md) | `PERSON_ID` |
| `PROD_VLDTN_PRSNL_ID` | [PRSNL](PRSNL.md) | `PERSON_ID` |
| `SYNONYM_ID` | [ORDER_CATALOG_SYNONYM](ORDER_CATALOG_SYNONYM.md) | `SYNONYM_ID` |

