# PHA_ORD_ACT_OBS_ST

> Observation set of PharmNet's activity data at the order dispense level. Used to generate workload reports.

**Description:** pha_ord_act_obs_st  
**Table type:** ACTIVITY  
**Primary key:** _(not published — see note)_  
**Columns:** 193

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
| 9 | `ACT_SHIFT_GRP2_CD` | DOUBLE | NOT NULL |  | Shifts for Pharmacy |
| 10 | `ACT_SHIFT_GRP_CD` | DOUBLE | NOT NULL |  | Shifts for Pharmacy |
| 11 | `CANCEL_REASON_CD` | DOUBLE | NOT NULL |  | reason that an action was cancelled |
| 12 | `CKI` | VARCHAR(255) |  |  | CKI value |
| 13 | `CONTRIBUTOR_SYSTEM_CD` | DOUBLE | NOT NULL |  | Contributor system identifies the source feed of data from which a row was populated. This is mainly used to determine how to update a set of data that may have originated from more than one source feed. |
| 14 | `COSIGN_OVERRIDE_OPTION_CD` | DOUBLE | NOT NULL |  | Determines if Physician Cosign is required for external order entry systems. |
| 15 | `COSIGN_OVERRIDE_REASON_CD` | DOUBLE | NOT NULL |  | The reason Physician Cosign has been overridden from the system determined value. |
| 16 | `COST` | DOUBLE |  |  | Order Cost |
| 17 | `CUR_DEPT_STATUS_CD` | DOUBLE | NOT NULL |  | current departmental status code of an order |
| 18 | `CUR_ORDER_STATUS_CD` | DOUBLE | NOT NULL |  | ** OBSOLETE - NO LONGER USED **cur_order_status_cd |
| 19 | `CUR_START_DT_NBR` | DOUBLE |  |  | the Julian value of the start date of an order |
| 20 | `CUR_START_DT_TM` | DATETIME |  |  | The start dt/tm of this order |
| 21 | `CUR_START_MIN_NBR` | DOUBLE |  |  | the time value in minutes of the start time of an order |
| 22 | `CUR_START_TZ` | DOUBLE |  |  | Time zone associated with the corresponding DT_TM column. |
| 23 | `DAW_CD` | DOUBLE | NOT NULL |  | dispense as written code |
| 24 | `DAY_OF_TREATMENT_IND` | DOUBLE | NOT NULL |  | Indicates if this order is a day of treatment order. |
| 25 | `DC_REASON_CD` | DOUBLE | NOT NULL |  | reason that an order was discontinued |
| 26 | `DEPT_MISC_LINE` | VARCHAR(255) |  |  | text filled by department |
| 27 | `DEPT_STATUS_CD` | DOUBLE | NOT NULL |  | departmental status of the order |
| 28 | `DISCONTINUE_EFF_DT_NBR` | DOUBLE |  |  | the Julian value of the discontinue date of an order |
| 29 | `DISCONTINUE_EFF_DT_TM` | DATETIME |  |  | date and time the discontinue action should become effective for the order |
| 30 | `DISCONTINUE_EFF_MIN_NBR` | DOUBLE |  |  | the time value in minutes of the discontinue time |
| 31 | `DISCONTINUE_EFF_TZ` | DOUBLE |  |  | Time zone associated with the corresponding DT_TM column. |
| 32 | `DISCONTINUE_IND` | DOUBLE |  |  | indicator on whether this order has been discontinued |
| 33 | `DISCONTINUE_TYPE_CD` | DOUBLE | NOT NULL |  | Code set 4038: Indicates what method the order was discontinued |
| 34 | `DISP_CATEGORY_CD` | DOUBLE | NOT NULL |  | Code set 4008: Indicates the method to calculate dispense doses and charging method |
| 35 | `DISP_FROM_LOC_CD` | DOUBLE | NOT NULL |  | Code set 220: the location the order is to dispense from |
| 36 | `DISP_FROM_SR_CD` | DOUBLE | NOT NULL |  | Code set 221: the service resource code value that is associated to the dispense from location |
| 37 | `DISP_PRIORITY_CD` | DOUBLE | NOT NULL |  | Code set 4513: the dispense priority of an order |
| 38 | `EFFECTIVE_DT_NBR` | DOUBLE |  |  | Effective Date Number value |
| 39 | `EFFECTIVE_DT_TM` | DATETIME |  |  | Effective Date and Time value |
| 40 | `EFFECTIVE_MIN_NBR` | DOUBLE |  |  | Effective Minute number value |
| 41 | `ENCNTR_ID` | DOUBLE | NOT NULL | FK→ | This is the value of the unique primary identifier of the encounter table. It is an internal system assigned number. |
| 42 | `EXPIRE_DT_NBR` | DOUBLE |  |  | the Julian value of the expire date of the order |
| 43 | `EXPIRE_DT_TM` | DATETIME |  |  | expire date and time value |
| 44 | `EXPIRE_MIN_NBR` | DOUBLE |  |  | the time value in minutes of the expire time of an order |
| 45 | `EXPIRE_TZ` | DOUBLE |  |  | Time zone associated with the corresponding DT_TM column. |
| 46 | `FILL_NBR` | DOUBLE |  |  | Indicates the Fill Number that is being filled out of the total available fills. |
| 47 | `FLOORSTOCK_IND` | DOUBLE |  |  | indicates if the order is dispensed from the floor |
| 48 | `FLOORSTOCK_OVERRIDE_IND` | DOUBLE |  |  | indicates if the user has changed the dispense from location to a floorstock (1) or non-floorstock location (2) |
| 49 | `FREQ_CD` | DOUBLE | NOT NULL |  | code value of the frequency associated to order |
| 50 | `FUTURE_LOC_FACILITY_CD` | DOUBLE | NOT NULL | FK→ | Pharmacy future facility |
| 51 | `FUTURE_LOC_NURSE_UNIT_CD` | DOUBLE | NOT NULL | FK→ | Pharmacy future nurse unit |
| 52 | `HEALTH_PLAN_ID` | DOUBLE | NOT NULL | FK→ | health_plan_id |
| 53 | `ICD9_NOMEN_ID` | DOUBLE | NOT NULL | FK→ | Diagnosis Nomenclature Identifier |
| 54 | `IGNORE_IND` | DOUBLE |  |  | used to temporarily mark an order to not qualify on the fill list; 1 = ignore, 0 = fill as instructed |
| 55 | `INACTIVE_FLAG` | DOUBLE |  |  | inactive_flag |
| 56 | `INCOMPLETE_ORDER_IND` | DOUBLE |  |  | indicates the order is missing required details |
| 57 | `INGREDIENT_IND` | DOUBLE | NOT NULL |  | an indicator on whether this order has multiple ingredients. |
| 58 | `LAST_FILL_STATUS_CD` | DOUBLE | NOT NULL |  | Order status when the last fill was run. From the Order_dispense table. |
| 59 | `LAST_REFILL_DT_NBR` | DOUBLE |  |  | the Julian date of when the order was last refilled |
| 60 | `LAST_REFILL_DT_TM` | DATETIME |  |  | the date and time of when the order was last refilled |
| 61 | `LAST_REFILL_MIN_NBR` | DOUBLE |  |  | the time in minutes of when the order was last refilled |
| 62 | `LAST_REFILL_TZ` | DOUBLE |  |  | Time zone associated with the corresponding DT_TM column. |
| 63 | `LAST_UPDT_PROVIDER_ID` | DOUBLE | NOT NULL |  | the personnel identifier of the provider that last updated the order |
| 64 | `LEGAL_STATUS_CD` | DOUBLE | NOT NULL |  | Legal Status Code value |
| 65 | `MED_ORDER_TYPE_CD` | DOUBLE | NOT NULL |  | the medication order type code value of the order |
| 66 | `MED_SERVICE_CD` | DOUBLE | NOT NULL |  | The type or category of medical service that the patient is receiving in relation to their encounter. The category may be of treatment type, surgery, general resources, or others. |
| 67 | `NEED_RX_CLIN_REVIEW_FLAG` | DOUBLE |  |  | Flag for identifying whether the order's clinical review has been completed or not. |
| 68 | `NEED_RX_PROD_ASSIGN_FLAG` | DOUBLE |  |  | Flag for identifying whether the order's product assignment has been completed or not. |
| 69 | `NEED_RX_VERIFY_IND` | DOUBLE |  |  | indicates if the order needs verification from pharmacist |
| 70 | `NEED_VERIFY_IND` | DOUBLE |  |  | indicates if the order has been verified |
| 71 | `ORDERABLE_TYPE_FLAG` | DOUBLE |  |  | indicates what type of orderable procedure the item has been assigned |
| 72 | `ORDERING_PROVIDER_ID` | DOUBLE | NOT NULL |  | the personnel id of the provider of the order |
| 73 | `ORDER_CATALOG_CD` | DOUBLE | NOT NULL |  | The order catalog code value for this medication |
| 74 | `ORDER_CATALOG_TYPE_CD` | DOUBLE | NOT NULL |  | A grouping mechanism to bring order catalogs together. |
| 75 | `ORDER_ID` | DOUBLE | NOT NULL | FK→ | Order Id from the orders table |
| 76 | `ORDER_INCOMP_ORDER_IND` | DOUBLE |  |  | indicates if a required detail is missing on an order |
| 77 | `ORDER_LOC_CD` | DOUBLE | NOT NULL |  | The order location of this action. |
| 78 | `ORDER_PRIORITY_CD` | DOUBLE | NOT NULL |  | Taken from order_detail. Values from code set 4010. |
| 79 | `ORDER_STATUS_CD` | DOUBLE | NOT NULL |  | Order status code value such as 'CANCELED' and 'COMPLETED'. |
| 80 | `ORDER_TYPE_FLAG` | DOUBLE |  |  | The medication order type of the order. |
| 81 | `ORD_PERS_AGE_DAYS` | DOUBLE |  |  | number of days a person's age is |
| 82 | `ORD_PERS_AGE_YEARS` | DOUBLE |  |  | number of years a person's age is |
| 83 | `ORD_PERS_BED_CD` | DOUBLE | NOT NULL |  | The bed code value of the patient's location. |
| 84 | `ORD_PERS_BLD_CD` | DOUBLE | NOT NULL |  | The building code value of the patient's location. |
| 85 | `ORD_PERS_FAC_CD` | DOUBLE | NOT NULL |  | The facility Code value of the patient's location. |
| 86 | `ORD_PERS_NU_CD` | DOUBLE | NOT NULL |  | The Nurse Unit code value of the patient's location. |
| 87 | `ORD_PERS_NU_GRP2_CD` | DOUBLE | NOT NULL |  | The nurse unit grouping code |
| 88 | `ORD_PERS_NU_GRP_CD` | DOUBLE | NOT NULL |  | Grouping of nurse unit the person was located at the time of the order |
| 89 | `ORD_PERS_ROOM_CD` | DOUBLE | NOT NULL |  | The room code value of the patient's location. |
| 90 | `ORD_PERS_ZIP` | VARCHAR(25) |  |  | the zip code of the patient's address |
| 91 | `ORGANIZATION_ID` | DOUBLE | NOT NULL | FK→ | organization_id |
| 92 | `ORIG_ORDER_DT_NBR` | DOUBLE |  |  | The Julian value of the order date. |
| 93 | `ORIG_ORDER_DT_TM` | DATETIME |  |  | the date time the order was created |
| 94 | `ORIG_ORDER_MIN_NBR` | DOUBLE |  |  | the time value of the order time in minutes |
| 95 | `ORIG_ORDER_TZ` | DOUBLE |  |  | Time zone associated with the corresponding DT_TM column. |
| 96 | `ORIG_ORD_AS_FLAG` | DOUBLE | NOT NULL |  | the flag show how this order was originally placed. |
| 97 | `PAR_DOSES` | DOUBLE |  |  | the PRN or PAR doses of an order |
| 98 | `PERSON_ID` | DOUBLE | NOT NULL | FK→ | This is the value of the unique primary identifier of the person table. It is an internal system assigned number. |
| 99 | `PERSON_OWN_MEDS_IND` | DOUBLE | NOT NULL |  | Indicates that the patient brought in their own supply of the medication. |
| 100 | `PHARM_ORDER_TYPE_FLAG` | DOUBLE |  |  | Identifies the type of order that is placed in phamedmgr (medication, continuous, intermittent) |
| 101 | `PHARM_TYPE_CD` | DOUBLE | NOT NULL |  | The pharmacy type cd |
| 102 | `PHYSICIAN_DEA_TXT` | VARCHAR(200) |  |  | DEA number of the prescribing physician |
| 103 | `PRICE` | DOUBLE |  |  | Order Price |
| 104 | `PRICE_CODE_CD` | DOUBLE | NOT NULL |  | the price schedule associated to an order |
| 105 | `PRN_IND` | DOUBLE |  |  | indicates if the order is PRN |
| 106 | `PROJECTED_STOP_DT_NBR` | DOUBLE |  |  | the Julian date of the order's stop date |
| 107 | `PROJECTED_STOP_DT_TM` | DATETIME |  |  | the stop date/time of an order |
| 108 | `PROJECTED_STOP_MIN_NBR` | DOUBLE |  |  | the time value of the order's stop time in minutes |
| 109 | `PROJECTED_STOP_TZ` | DOUBLE |  |  | Time zone associated with the corresponding DT_TM column. |
| 110 | `QTY_REMAINING` | DOUBLE |  |  | Contains the remaining quantity of the order. |
| 111 | `REFILLS_REMAINING` | DOUBLE |  |  | refills_remaining |
| 112 | `REFILL_QTY` | DOUBLE |  |  | the amount to refill for a retail order |
| 113 | `RENEW_REASON_CD` | DOUBLE | NOT NULL |  | the reason a renew action occurred |
| 114 | `REPLACE_EVERY` | DOUBLE |  |  | the replace every value of an order |
| 115 | `REPLACE_EVERY_CD` | DOUBLE | NOT NULL |  | the unit of measure for the replace every value of an order |
| 116 | `REQ_START_DT_NBR` | DOUBLE |  |  | the Julian date of an order's requested start |
| 117 | `REQ_START_DT_TM` | DATETIME |  |  | the requested start date/time of an order |
| 118 | `REQ_START_MIN_NBR` | DOUBLE |  |  | the time value in minutes for an order's start time |
| 119 | `REQ_START_TZ` | DOUBLE |  |  | Time zone associated with the corresponding DT_TM column. |
| 120 | `RESUME_DT_NBR` | DOUBLE |  |  | the Julian date of an order's resume action |
| 121 | `RESUME_DT_TM` | DATETIME |  |  | the date/time of an order's resume action |
| 122 | `RESUME_EFF_DT_NBR` | DOUBLE |  |  | the Julian date of an order's effective resume action date |
| 123 | `RESUME_EFF_DT_TM` | DATETIME |  |  | the date/time of an order's effective resume action date/time |
| 124 | `RESUME_EFF_MIN_NBR` | DOUBLE |  |  | the time value in minutes of an order's effective resume action time |
| 125 | `RESUME_EFF_TZ` | DOUBLE |  |  | Time zone associated with the corresponding DT_TM column. |
| 126 | `RESUME_MIN_NBR` | DOUBLE |  |  | the time value in minutes of an order's resume action |
| 127 | `RESUME_REASON_CD` | DOUBLE | NOT NULL |  | the reason a resume action occurs |
| 128 | `RESUME_TZ` | DOUBLE |  |  | Time zone associated with the corresponding DT_TM column. |
| 129 | `RXA_BACKWARD_ORDER_ID` | DOUBLE |  |  | Indicates the order based on which the current order was placed |
| 130 | `RXA_COB_FLAG` | DOUBLE |  |  | Indicates whether co-ordination of benefits was used in claiming this fill 0, "None", 1,"Non-COB", 2,"COB" |
| 131 | `RXA_CONTROL_NBR_TXT` | VARCHAR(250) |  |  | Control number for the script |
| 132 | `RXA_DAYS_SUPPLY` | DOUBLE |  |  | Indicates the days for which the current fill will last |
| 133 | `RXA_DISP_PRIORITY_DT_TM` | DATETIME |  |  | Priority Date/Time for the dispense |
| 134 | `RXA_DISP_PRIORITY_DT_TZ` | DOUBLE |  |  | Priority Date/Time Zone for the dispense |
| 135 | `RXA_DISP_QTY_UNIT_CD` | DOUBLE |  |  | Quantity Unit dispensed for the fill |
| 136 | `RXA_EXPANDED_SIG_ID` | DOUBLE |  |  | Order comment of type PHARMSIG. Long Text ID from the LONG_TEXT table. |
| 137 | `RXA_FILL_DEVICE_SR_CD` | DOUBLE |  |  | To store the pharmacy filling device value. |
| 138 | `RXA_FILL_LOCATION_SR_CD` | DOUBLE |  |  | To store the pharmacy filling location value |
| 139 | `RXA_FORWARD_ORDER_ID` | DOUBLE |  |  | Indicates the order that was placed based off of the current order |
| 140 | `RXA_HEALTH_PLAN_SEQ` | DOUBLE |  |  | The sequence of the last health plan in the list of health plans used for this prescription |
| 141 | `RXA_PARENT_ORDER_ID` | DOUBLE |  |  | This field contains the order_id of the prescription placed in easy script that was used to create the current order. |
| 142 | `RXA_PARENT_ORIG_ORD_AS_FLAG` | DOUBLE | NOT NULL |  | To store the parent order orig_ord_as_flag value |
| 143 | `RXA_PF_TYPE_CD` | DOUBLE |  |  | Indicates if a health plan supports NCPDP 51 partial fill submission process. |
| 144 | `RXA_PRICE_SCHED_ID` | DOUBLE |  |  | Indicates the price schedule used for the fill |
| 145 | `RXA_PROXY_PRESCRIBER_ID` | DOUBLE |  |  | Indicates the proxy prescriber of the order |
| 146 | `RXA_REVIEWED_PARENT_ACTION_SEQ` | DOUBLE |  |  | This field contains the action sequence of the parent order that was reviewed by the user that performed the latest fill on the current order. |
| 147 | `RXA_SCRIPT_ORIGIN_CD` | DOUBLE |  |  | Indicates how the script originated |
| 148 | `RXA_SOURCE_PARENT_ACTION_SEQ` | DOUBLE |  |  | This field contains the action sequence of the parent order that was used as the source to create the current order. |
| 149 | `RXA_TOTAL_REFILLS` | DOUBLE |  |  | Total refills authorized for the prescription |
| 150 | `RXA_TRANSFER_FLAG` | DOUBLE |  |  | Indicates the type of transfer performed on the order. 0, "None",1, "Internal Transfer-in", 2,"External Transfer-in",3,"External Transfer-out" |
| 151 | `RX_DISP_QTY` | DOUBLE |  |  | The retail quantity dispensed |
| 152 | `RX_EXPIRE_DT_NBR` | DOUBLE |  |  | the Julian date of an order's expire date |
| 153 | `RX_EXPIRE_DT_TM` | DATETIME |  |  | the date/time of an order's expire date/time |
| 154 | `RX_EXPIRE_MIN_NBR` | DOUBLE |  |  | the time value in minutes of an order's expire time |
| 155 | `RX_EXPIRE_TZ` | DOUBLE |  |  | Time zone associated with the corresponding DT_TM column. |
| 156 | `RX_MASK` | DOUBLE |  |  | pharmacy mask showing how this order was placed |
| 157 | `RX_NBR` | DOUBLE |  |  | retail number |
| 158 | `RX_NBR_CD` | DOUBLE | NOT NULL |  | Prescription number |
| 159 | `RX_NBR_STR` | VARCHAR(100) |  |  | rx_nbr_st |
| 160 | `RX_PAY_METHOD_CD` | DOUBLE | NOT NULL |  | The retail payment method. |
| 161 | `RX_QTY` | DOUBLE |  |  | Intial Quantity Prescribed |
| 162 | `RX_ROUTE_CD` | DOUBLE | NOT NULL |  | the pharmacy route associated to an order |
| 163 | `SERVICE_CATEGORY_CD` | DOUBLE | NOT NULL |  | Codified field, which identifies the current category of service the patient is receiving for this encounter. |
| 164 | `SIG` | VARCHAR(255) |  |  | dosing and administering instructions |
| 165 | `SOFT_STOP_DT_NBR` | DOUBLE |  |  | the Julian date of an order's soft stop date |
| 166 | `SOFT_STOP_DT_TM` | DATETIME |  |  | the stop date/time of an order's soft stop |
| 167 | `SOFT_STOP_MIN_NBR` | DOUBLE |  |  | the time value in minutes for an order's soft stop time |
| 168 | `SOFT_STOP_TZ` | DOUBLE |  |  | Time zone associated with the corresponding DT_TM column. |
| 169 | `STATUS_PRSNL_ID` | DOUBLE | NOT NULL |  | Id of the prsnl row that updated the status. |
| 170 | `STOP_DT_NBR` | DOUBLE |  |  | the Julian date of an order's stop date |
| 171 | `STOP_DT_TM` | DATETIME |  |  | the stop date/time of an order |
| 172 | `STOP_MIN_NBR` | DOUBLE |  |  | the time value in minutes of an order's stop time |
| 173 | `STOP_TYPE_CD` | DOUBLE | NOT NULL |  | the stop type policy of an order |
| 174 | `STOP_TZ` | DOUBLE |  |  | Time zone associated with the corresponding DT_TM column. |
| 175 | `STRENGTH_DOSE` | DOUBLE |  |  | the strength of an order |
| 176 | `STRENGTH_DOSE_UNIT_CD` | DOUBLE | NOT NULL |  | the strength unit of measure of an order |
| 177 | `SUSPEND_DT_NBR` | DOUBLE |  |  | the Julian date of an order's suspend |
| 178 | `SUSPEND_DT_TM` | DATETIME |  |  | the date/time of an order's suspend action |
| 179 | `SUSPEND_EFF_DT_NBR` | DOUBLE |  |  | the Julian date of an order's effective suspend action |
| 180 | `SUSPEND_EFF_DT_TM` | DATETIME |  |  | the date/time of an order's effective suspend action |
| 181 | `SUSPEND_EFF_MIN_NBR` | DOUBLE |  |  | the time value in minutes of an order's effective suspend time |
| 182 | `SUSPEND_EFF_TZ` | DOUBLE |  |  | Time zone associated with the corresponding DT_TM column. |
| 183 | `SUSPEND_IND` | DOUBLE |  |  | indicates if the order is suspended |
| 184 | `SUSPEND_MIN_NBR` | DOUBLE |  |  | the time value in minutes of an order's suspend time |
| 185 | `SUSPEND_TZ` | DOUBLE |  |  | Time zone associated with the corresponding DT_TM column. |
| 186 | `SYNONYM_ID` | DOUBLE | NOT NULL | FK→ | The synonym_id from the order_catalog_synonym table. |
| 187 | `TOTAL_RX_QTY` | DOUBLE |  |  | Total Quantity Prescribed |
| 188 | `TRANSFER_CNT` | DOUBLE |  |  | The number of times a prescription got transferred |
| 189 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 190 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 191 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 192 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 193 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `ENCNTR_ID` | [ENCOUNTER](ENCOUNTER.md) | `ENCNTR_ID` |
| `FUTURE_LOC_FACILITY_CD` | [LOCATION](LOCATION.md) | `LOCATION_CD` |
| `FUTURE_LOC_NURSE_UNIT_CD` | [LOCATION](LOCATION.md) | `LOCATION_CD` |
| `HEALTH_PLAN_ID` | [HEALTH_PLAN](HEALTH_PLAN.md) | `HEALTH_PLAN_ID` |
| `ICD9_NOMEN_ID` | [NOMENCLATURE](NOMENCLATURE.md) | `NOMENCLATURE_ID` |
| `ORDER_ID` | [ORDERS](ORDERS.md) | `ORDER_ID` |
| `ORGANIZATION_ID` | [ORGANIZATION](ORGANIZATION.md) | `ORGANIZATION_ID` |
| `PERSON_ID` | [PERSON](PERSON.md) | `PERSON_ID` |
| `SYNONYM_ID` | [ORDER_CATALOG_SYNONYM](ORDER_CATALOG_SYNONYM.md) | `SYNONYM_ID` |

