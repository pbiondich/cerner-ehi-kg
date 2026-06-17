# FILL_PRINT_ORD_HX

> Order information for pharmacy ouput prior to printing

**Description:** fill_print_ord_hx  
**Table type:** ACTIVITY  
**Primary key:** _(not published — see note)_  
**Columns:** 328

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ACTION_SEQUENCE` | DOUBLE |  |  | which action sequence the comment goes with |
| 2 | `ADMIN_COUNT` | DOUBLE |  |  | counter for number of administrations for this order |
| 3 | `ADMIN_DT_TM` | DATETIME |  |  | administration date and time |
| 4 | `ADMIN_TZ` | DOUBLE |  |  | Time zone associated with the corresponding DT_TM column. |
| 5 | `ADMIT_DT_TM` | DATETIME |  |  | admission date and time |
| 6 | `ADMIT_PHYS_ID` | DOUBLE | NOT NULL |  | Admitting physician ID number |
| 7 | `ADMIT_PHYS_NAME` | VARCHAR(50) |  |  | Name of the admitting physician. |
| 8 | `ADMIT_TZ` | DOUBLE |  |  | Time zone associated with the corresponding DT_TM column. |
| 9 | `ATTEND_PHYS_ID` | DOUBLE | NOT NULL |  | Attending Physicians ID number. |
| 10 | `ATTEND_PHYS_NAME` | VARCHAR(50) |  |  | Name of the attending physician. |
| 11 | `AUTHORIZATION_NBR` | VARCHAR(50) |  |  | Alpha numeric string returned by Claims Processor for Accepted Claims. |
| 12 | `BAG_NBR` | DOUBLE |  |  | Bag number in IV set. |
| 13 | `BASAL_RATE_UNIT_CD` | DOUBLE |  |  | Code value from code set 54 representing the Basal Rate Unit |
| 14 | `BASAL_RATE_UNIT_S` | VARCHAR(40) |  |  | Display value for the Basal Rate Unit. |
| 15 | `BASAL_RATE_VALUE` | DOUBLE |  |  | The amount of drug given as a continuous infusion. |
| 16 | `BED_CD` | DOUBLE | NOT NULL |  | Patients bed code value |
| 17 | `BED_S` | CHAR(40) |  |  | Patients bed description |
| 18 | `BIRTH_DT_TM` | DATETIME |  |  | Patient"s Birth Date |
| 19 | `BIRTH_TZ` | DOUBLE |  |  | Time zone associated with the corresponding DT_TM column. |
| 20 | `BRAND_NAME` | VARCHAR(50) |  |  | Brand name of product |
| 21 | `BSA` | DOUBLE |  |  | Body Surface Area |
| 22 | `BSA_UNIT_CD` | DOUBLE | NOT NULL |  | Unit of measure for body surface area |
| 23 | `BSA_UNIT_S` | VARCHAR(40) |  |  | Display value for BSA unit code |
| 24 | `CDM` | VARCHAR(25) |  |  | A unique number that can be tied to a drug (or other things that may be billed to a patient) in order to associate a charge with it |
| 25 | `CHARGE_QTY` | DOUBLE |  |  | Quantity charged. |
| 26 | `CLINICIAN_DOSE_UNIT_CD` | DOUBLE |  |  | Code value from code set 54 representing the Clinician Dose Unit. |
| 27 | `CLINICIAN_DOSE_UNIT_S` | VARCHAR(40) |  |  | Display value for the Clinician Dose Unit. |
| 28 | `CLINICIAN_DOSE_VALUE` | DOUBLE |  |  | Prescribed dose that can be given at the discretion of the patient care provider. |
| 29 | `COMMENT1_WHERE_TO_PRINT` | DOUBLE |  |  | Specifies whether comment 1 will print on label, MAR, and/or fill. |
| 30 | `COMMENT2_WHERE_TO_PRINT` | DOUBLE |  |  | Specifies whether comment 2 will print on label, MAR, and/or fill. |
| 31 | `COMMUNICATION_TYPE_CD` | DOUBLE | NOT NULL |  | Code value representing the communication type for an order. |
| 32 | `COMMUNICATION_TYPE_S` | VARCHAR(60) |  |  | Description of orders communication type. |
| 33 | `COMPOUND_IND` | DOUBLE |  |  | Indicates that the Order is a compound order (Compounded with multiple ingredients.) |
| 34 | `COMPOUND_TEXT_ID` | DOUBLE | NOT NULL | FK→ | Instructions for compounding |
| 35 | `COMPOUND_TOTAL` | DOUBLE |  |  | Compound Total |
| 36 | `CONCENTRATION` | DOUBLE | NOT NULL |  | For continuous infusions, the amount of a component in a given volume. |
| 37 | `CONCENTRATION_UNIT_CD` | DOUBLE | NOT NULL |  | Concentration unit of measure code value. |
| 38 | `CONCENTRATION_UNIT_S` | VARCHAR(40) |  |  | Display value for concentration unit of measure. |
| 39 | `CONTAINER_SEQ` | DOUBLE |  |  | The sequence of the container this row is associated to. Will only be greater than 0 for rows denoting products of split container dispense events. |
| 40 | `CONTROL_NUMBER` | VARCHAR(25) |  |  | A number Pharmacy uses when dispensing controlled substances. |
| 41 | `COPAY` | DOUBLE |  |  | Co pay amount |
| 42 | `CRCL` | DOUBLE |  |  | Most recent result for serum creatinine |
| 43 | `CRCL_UNIT_CD` | DOUBLE | NOT NULL |  | Unit of measure for creatinine clearance. |
| 44 | `CRCL_UNIT_S` | VARCHAR(40) |  |  | Display value for Creatinine Clearance unit code |
| 45 | `CREDIT_INV_IND` | DOUBLE |  |  | Identifies an Order that was credited during Net Cart event, but wasn't returned in Inventory. |
| 46 | `CREDIT_QTY` | DOUBLE |  |  | Quantity credited. |
| 47 | `CUR_DISP_LOC_CD` | DOUBLE | NOT NULL |  | Dispense from location code for the current event. |
| 48 | `CUR_DISP_LOC_S` | VARCHAR(40) |  |  | Display Value of the location code for the current event. |
| 49 | `DAW_CD` | DOUBLE | NOT NULL |  | Dispense as written code |
| 50 | `DAYS_SUPPLY` | DOUBLE |  |  | Number of days the quantity dispensed (given to the patient) will last. |
| 51 | `DISPENSE_CATEGORY_CD` | DOUBLE | NOT NULL |  | Dispense category code. |
| 52 | `DISPENSE_CATEGORY_S` | CHAR(40) |  |  | Dispense category. |
| 53 | `DISPENSE_COMMENT_TEXT_ID` | DOUBLE |  | FK→ | Long_text_id of the dispense comment. Originally written to the order_comment table with comment_type_cd of "RXADISPNOTE". |
| 54 | `DISPENSE_DEVICE_IND` | DOUBLE |  |  | Dispense device indicator. 0 = this dispense event was not passed to a dispense device; 1 = this dispense event was passed to a dispense device. |
| 55 | `DISPENSE_DT_TM` | DATETIME |  |  | Dispense date and time |
| 56 | `DISPENSE_FROM_CD` | DOUBLE | NOT NULL |  | Code value representing the location that an order is dispensed from. |
| 57 | `DISPENSE_FROM_S` | VARCHAR(60) |  |  | Display value for the location code from which an order is dispensed. |
| 58 | `DISPENSE_ID` | DOUBLE | NOT NULL | FK→ | Dispense Id for this order and dispense |
| 59 | `DISPENSE_LOC_CD` | DOUBLE | NOT NULL |  | Location where the last initial dose came from |
| 60 | `DISPENSE_SR_CD` | DOUBLE | NOT NULL |  | Dispense Service Resource code |
| 61 | `DISPENSE_STATUS_HX_ID` | DOUBLE | NOT NULL | FK→ | Dispense Status Hx id |
| 62 | `DISPENSE_TZ` | DOUBLE |  |  | Time zone associated with the corresponding DT_TM column. For inpatient rows, this is the time zone of the encounter. For Retail Pharmacy, it is the time zone of the pharmacy's facility. |
| 63 | `DISP_PRIORITY_CD` | DOUBLE | NOT NULL |  | dispense Priority Cd |
| 64 | `DISP_PRIORITY_DT_TM` | DATETIME |  |  | Dispense Priority Date and tiem |
| 65 | `DISP_PRIORITY_TZ` | DOUBLE |  |  | Time zone associated with the corresponding DT_TM column. |
| 66 | `DISP_QTY` | DOUBLE |  |  | Dispense Quantity |
| 67 | `DISP_QTY_UNIT_CD` | DOUBLE | NOT NULL |  | dispense quantityunit cd |
| 68 | `DOSES_OMITTED_IND` | DOUBLE | NOT NULL |  | Indicates if there were doses possibly omitted in this print for this order. |
| 69 | `DOSE_FORM_CD` | DOUBLE | NOT NULL |  | Code value representing the type of dose for an order. |
| 70 | `DOSE_FORM_S` | VARCHAR(60) |  |  | Display value for the dose form (e.g.: tab, ea...) of an order. |
| 71 | `DOSE_LIMIT_TIME_UNIT_CD` | DOUBLE |  |  | Code value from code set 54 representing the Dose Limit Time Unit. |
| 72 | `DOSE_LIMIT_TIME_UNIT_S` | VARCHAR(40) |  |  | Display value for the Dose Limit Time Unit. |
| 73 | `DOSE_LIMIT_TIME_VALUE` | DOUBLE |  |  | Time period related to the Dose Limit value. |
| 74 | `DOSE_LIMIT_UNIT_CD` | DOUBLE |  |  | Code value from code set 54 representing the Dose Limit Unit. |
| 75 | `DOSE_LIMIT_UNIT_S` | VARCHAR(40) |  |  | Display value for the Dose Limit Unit. |
| 76 | `DOSE_LIMIT_VALUE` | DOUBLE |  |  | Maximum amount of medication that can be delivered over a specified time period. |
| 77 | `DOSE_QUANTITY` | DOUBLE |  |  | Dose quantity. |
| 78 | `DOSE_QUANTITY_TXT` | VARCHAR(150) |  |  | Textual representation of the dose quantity as received from the device. For use with orders that utilize variable dosing. |
| 79 | `DOSE_QUANTITY_UNIT_CD` | DOUBLE | NOT NULL |  | Dose quantity unit of measure code. |
| 80 | `DOSE_QUANTITY_UNIT_S` | CHAR(40) |  |  | Dose quantity unit of measure. |
| 81 | `DOSING_METHOD_FLAG` | DOUBLE | NOT NULL |  | Indicates the type of dosing that is applied to the order. |
| 82 | `DUR_CONFLICT_CD` | DOUBLE | NOT NULL |  | DUR Conflict Cd |
| 83 | `DUR_INTER_CD` | DOUBLE | NOT NULL |  | Drug Utilization Review Interaction Code |
| 84 | `DUR_OUTCOME_CD` | DOUBLE | NOT NULL |  | DUR Outcome Cd |
| 85 | `EARLY_REASON_CD` | DOUBLE | NOT NULL |  | Early reason cd |
| 86 | `ELIGIBILITY_CLARIFY_CD` | DOUBLE | NOT NULL |  | Clarification Code indicating patient's eligibility for the benefit. |
| 87 | `ENCNTR_ID` | DOUBLE | NOT NULL | FK→ | This is the value of the unique primary identifier of the encounter table. It is an internal system assigned number. |
| 88 | `ENTERED_DT_TM` | DATETIME |  |  | Date and time order was entered into the system |
| 89 | `ENTERED_TZ` | DOUBLE |  |  | Time zone associated with the corresponding DT_TM column. |
| 90 | `ENTER_USER_ID` | DOUBLE | NOT NULL |  | User ID of the person who entered the order |
| 91 | `ENTRY_ID` | DOUBLE | NOT NULL |  | ID of the person entering the order. |
| 92 | `ENTRY_NAME` | VARCHAR(50) |  |  | Name of the person who entered the order. |
| 93 | `ERROR_LOG` | VARCHAR(100) |  |  | Error information, if any. |
| 94 | `EXTRA_REASON_CD` | DOUBLE | NOT NULL |  | extra reason cd |
| 95 | `EXT_COPAY_IND` | DOUBLE |  |  | Used to notify external systems that a patient will be charged a copay for a prescription. |
| 96 | `EXT_DISP_QTY` | DOUBLE |  |  | Dispense quantity used to send to external systems. |
| 97 | `EXT_DISP_QTY_CONV_FACTOR_AMT` | DOUBLE |  |  | Client configurable dispense conversion factor within the Product Tool which is used to maintain the package size to dispense factor ratio by converting the NCPDP quantity to a quantity recognized by external systems. |
| 98 | `EXT_DISP_QTY_UNIT_S` | VARCHAR(60) |  |  | Dispense quantity unit used to send to external systems. |
| 99 | `EXT_DRUG_DESC` | VARCHAR(200) |  |  | Drug description used to send to external systems. |
| 100 | `EXT_DRUG_IDENT` | VARCHAR(200) |  |  | Client configurable drug identifier defined in the Product Tool to be sent outbound to an external system. |
| 101 | `FACILITY_CD` | DOUBLE | NOT NULL |  | Facility code. |
| 102 | `FACILITY_S` | CHAR(40) |  |  | Facility description. |
| 103 | `FILL_ANCHOR_DT_TM` | DATETIME |  |  | Fill date used to calculate the next dispense date/time. |
| 104 | `FILL_NBR` | DOUBLE |  |  | A sequential number indicating the number of times a prescription got filled. |
| 105 | `FILL_NOTE_ID` | DOUBLE | NOT NULL | FK→ | Identifier for fill note. |
| 106 | `FILL_QUANTITY` | DOUBLE |  |  | fill quantity |
| 107 | `FINNBR` | VARCHAR(100) |  |  | Financial number |
| 108 | `FINNBR_ID` | DOUBLE | NOT NULL | FK→ | financial number ID |
| 109 | `FLOORSTOCK_IND` | DOUBLE |  |  | Floorstock indicator - 1 = true, 0 = false. |
| 110 | `FORMULARY_STATUS_CD` | DOUBLE | NOT NULL |  | Formulary status code |
| 111 | `FORMULARY_STATUS_S` | CHAR(40) |  |  | Formulary status description |
| 112 | `FORM_CD` | DOUBLE | NOT NULL |  | Dosage form code. |
| 113 | `FORM_S` | CHAR(40) |  |  | Dosage form description |
| 114 | `FREETEXT_DOSE` | VARCHAR(50) |  |  | Free-text dose information. |
| 115 | `FREETEXT_RATE` | VARCHAR(255) |  |  | Text representing the rate for an order entered by user. |
| 116 | `FREQUENCY_CD` | DOUBLE | NOT NULL |  | Frequency code. |
| 117 | `FREQUENCY_S` | CHAR(40) |  |  | Frequency description |
| 118 | `FUTURE_ORDER_IND` | DOUBLE | NOT NULL |  | Indication of whether or not the order is in a future status at the time the dispense occurred. |
| 119 | `GEN_NAME` | VARCHAR(200) |  |  | Generic name of the product |
| 120 | `HEALTH_PLAN_ID` | DOUBLE | NOT NULL | FK→ | Display name of the health plan. |
| 121 | `HEALTH_PLAN_S` | VARCHAR(40) |  |  | Display (Name) of the Health Plan |
| 122 | `HEIGHT` | DOUBLE |  |  | Patient"s height |
| 123 | `HEIGHT_UNIT_CD` | DOUBLE | NOT NULL |  | Unit of measure patients height is measured in. |
| 124 | `HEIGHT_UNIT_S` | CHAR(40) |  |  | Unit of measure patients height is measured in. |
| 125 | `IBW` | DOUBLE |  |  | Ideal Body Weight |
| 126 | `IBW_UNIT_CD` | DOUBLE | NOT NULL |  | Unit of measure for Ideal Body Weight. |
| 127 | `IBW_UNIT_S` | VARCHAR(40) |  |  | Display value for Ideal Body Weight unit code. |
| 128 | `ICD9_ID` | DOUBLE | NOT NULL | FK→ | Nomenclature ID for the ICD9 code. |
| 129 | `ICD9_S` | VARCHAR(100) |  |  | ICD9_s |
| 130 | `IGNORE_IND` | DOUBLE |  |  | No longer in use. |
| 131 | `INFUSE_OVER` | DOUBLE |  |  | Time the IV will be infused over. |
| 132 | `INFUSE_UNIT_CD` | DOUBLE | NOT NULL |  | Unit of measure code IV infusion time is measured in. |
| 133 | `INFUSE_UNIT_S` | CHAR(40) |  |  | Unit of measure description IV infusion time is measured in. |
| 134 | `INGRED_CNT` | DOUBLE |  |  | Number of ingredients in order. |
| 135 | `INGRED_DESC` | VARCHAR(200) |  |  | Description of ingredient. |
| 136 | `INGRED_SEQ` | DOUBLE |  |  | The identifier for the ingredient |
| 137 | `INS_CD` | DOUBLE | NOT NULL |  | Insurance Code |
| 138 | `INS_POLICY` | CHAR(40) |  |  | Insurance Policy |
| 139 | `ITEM_ID` | DOUBLE | NOT NULL | FK→ | The unique identifier for the product. |
| 140 | `IV_IN_SEQ` | DOUBLE |  |  | IV set rotation, Alternate IV. |
| 141 | `IV_SET_SIZE` | DOUBLE |  |  | Number of bags in IV set. |
| 142 | `LABEL1_ID` | DOUBLE | NOT NULL | FK→ | Identifier for label 1 text |
| 143 | `LABEL2_ID` | DOUBLE | NOT NULL | FK→ | Identifier for label 2 text |
| 144 | `LABEL_DESC` | VARCHAR(200) |  |  | Description for label |
| 145 | `LABEL_REASON_CD` | DOUBLE | NOT NULL |  | Reason for printing label code (fill, reprint, printer jam, etc.). |
| 146 | `LABEL_REASON_S` | CHAR(40) |  |  | Reason for printing label description (fill, reprint, printer jam, etc.). |
| 147 | `LABEL_TYPE_CD` | DOUBLE | NOT NULL |  | Label type that will be created when the row is printed. |
| 148 | `LANGUAGE_CD` | DOUBLE | NOT NULL |  | Patient's Language |
| 149 | `LAST_REFILL_DT_TM` | DATETIME |  |  | Last Refill date and time |
| 150 | `LAST_REFILL_TZ` | DOUBLE |  |  | Time zone associated with the corresponding DT_TM column. |
| 151 | `LATE_REASON_CD` | DOUBLE | NOT NULL |  | late reason cd |
| 152 | `LBL_ID` | DOUBLE | NOT NULL |  | Column Not Used |
| 153 | `LEGAL_STATUS_CD` | DOUBLE | NOT NULL |  | DEA schedule code, etc. |
| 154 | `LEGAL_STATUS_S` | CHAR(40) |  |  | DEA schedule description, etc. |
| 155 | `LOADING_DOSE_UNIT_CD` | DOUBLE |  |  | Code value from code set 54 representing the Loading Dose Unit. |
| 156 | `LOADING_DOSE_UNIT_S` | VARCHAR(40) |  |  | Display value for the Loading Dose Unit. |
| 157 | `LOADING_DOSE_VALUE` | DOUBLE |  |  | Dose ordered to initiate medication treatment. This dose is typically larger than PCA dose |
| 158 | `LOCATION_CD` | DOUBLE | NOT NULL |  | Patient"s location code (nursing station). |
| 159 | `LOCATION_S` | CHAR(40) |  |  | Patient"s location (nursing station). |
| 160 | `LOCKOUT_INT_UNIT_CD` | DOUBLE |  |  | Code value from code set 54 representing the Lockout Interval Unit. |
| 161 | `LOCKOUT_INT_UNIT_S` | VARCHAR(40) |  |  | Display value for the Lockout Interval Unit. |
| 162 | `LOCKOUT_INT_VALUE` | DOUBLE |  |  | The time interval before the pump can provide the next PCA dose. |
| 163 | `LOT_TRACKING_IND` | DOUBLE | NOT NULL |  | Indicates whether or not lot tracking should be required for this item. |
| 164 | `MANF_CD` | DOUBLE | NOT NULL |  | manufacturer code |
| 165 | `MEDREC_NBR` | VARCHAR(100) |  |  | Med rec number |
| 166 | `MEDREC_NBR_ID` | DOUBLE | NOT NULL | FK→ | Med rec number ID |
| 167 | `MED_FIN_IND` | DOUBLE |  |  | Indicator to display med rec number or financial number |
| 168 | `MED_PRODUCT_ID` | DOUBLE | NOT NULL | FK→ | med Product Id |
| 169 | `ML_HR` | DOUBLE |  |  | IV rate |
| 170 | `MULTUM_PIL_IDENT` | VARCHAR(20) |  |  | Identifies the multum DNUM or MMDC identifier based on whether the prescribed drug has patient information leaflet data defined in the multum drug database. If MMDC has PIL information available, MMDC will be written. Otherwise, if DNUM has PIL information available, DNUM will be written. |
| 171 | `NBR_OF_REFILLS` | DOUBLE |  |  | Number of refills allowed |
| 172 | `NDC` | VARCHAR(30) |  |  | NDC Number |
| 173 | `NET_CART_IND` | DOUBLE |  |  | Indication to indicate that a change has occurred to the quantity on the cart. |
| 174 | `NET_CART_QTY` | DOUBLE |  |  | If order is changed, this field will contain the difference the human will need to change the quantity on the cart by. |
| 175 | `NEXT_DISPENSE_DT_TM` | DATETIME |  |  | next dispense date/time |
| 176 | `NEXT_DISPENSE_TZ` | DOUBLE |  |  | Time zone associated with the corresponding DT_TM column. For inpatient rows, this is the time zone of the encounter. For Retail Pharmacy, it is the time zone of the pharmacy's facility. |
| 177 | `NORMALIZED_RATE` | DOUBLE | NOT NULL |  | In the context of a continuous infusion, the amount of a medication to be administered per time unit (e.g., mg/hour), or the amount of a medication to be administered per patient weight unit per time unit (e.g., mcg/kg/minute). |
| 178 | `NORMALIZED_RATE_UNIT_CD` | DOUBLE | NOT NULL |  | Normalized rate unit of measure code value. |
| 179 | `NORMALIZED_RATE_UNIT_S` | VARCHAR(40) |  |  | Display value for normalized rate unit of measure. |
| 180 | `ORDERED_AS_MNEMONIC` | VARCHAR(100) |  |  | Text representing the name by which an ingredient was ordered. |
| 181 | `ORDER_COMMENT_ID` | DOUBLE | NOT NULL | FK→ | Identifier representing the order comment. |
| 182 | `ORDER_ENTRY_LOC_CD` | DOUBLE | NOT NULL |  | not in use |
| 183 | `ORDER_ID` | DOUBLE | NOT NULL | FK→ | Order identifier |
| 184 | `ORDER_PRIORITY_CD` | DOUBLE | NOT NULL |  | Code value representing the order priority. |
| 185 | `ORDER_PRIORITY_S` | VARCHAR(60) |  |  | Display value for the order priority. |
| 186 | `ORDER_ROW_SEQ` | DOUBLE | NOT NULL |  | Sequence counter for the rows included with this order |
| 187 | `ORDER_START_DT_TM` | DATETIME |  |  | Order start date and time. |
| 188 | `ORDER_START_TZ` | DOUBLE |  |  | Time zone associated with the corresponding DT_TM column. |
| 189 | `ORDER_STATUS_DT_TM` | DATETIME |  |  | Order status date/time |
| 190 | `ORDER_STATUS_ENUM` | DOUBLE |  |  | Order status enumerated type |
| 191 | `ORDER_STATUS_S` | CHAR(40) |  |  | Order status |
| 192 | `ORDER_STATUS_TZ` | DOUBLE |  |  | Time zone associated with the corresponding DT_TM column. |
| 193 | `ORDER_STOP_DT_TM` | DATETIME |  |  | Order stop date and time. |
| 194 | `ORDER_STOP_TZ` | DOUBLE |  |  | Time zone associated with the corresponding DT_TM column. |
| 195 | `ORDER_TYPE_FLAG` | DOUBLE |  |  | Type of this order |
| 196 | `ORD_COST` | DOUBLE |  |  | Cost of the order |
| 197 | `ORD_DESC` | VARCHAR(100) |  |  | Order description. |
| 198 | `ORD_PEND_STATUS` | CHAR(20) |  |  | pending order status |
| 199 | `ORD_PHYS_ID` | DOUBLE | NOT NULL |  | Identifier for ordering physician |
| 200 | `ORD_PHYS_NAME` | VARCHAR(50) |  |  | Name of ordering physician |
| 201 | `ORD_PRICE` | DOUBLE |  |  | Price of the order |
| 202 | `ORD_TYPE` | DOUBLE |  |  | Type of order (med, IV) |
| 203 | `OTHER_COVERAGE_CD` | DOUBLE | NOT NULL |  | other coverage code |
| 204 | `OUTPUT_FORMAT_CD` | DOUBLE | NOT NULL |  | Code for desired output format |
| 205 | `OVERFILL_AMT` | DOUBLE |  |  | Overfill Amount |
| 206 | `PATIENT_MED_IND` | DOUBLE | NOT NULL |  | Indicates whether the order is a patient's own medication. |
| 207 | `PATIENT_TEXT_ID` | DOUBLE | NOT NULL | FK→ | Long text id of patient note. |
| 208 | `PAT_TEXT_ID` | DOUBLE | NOT NULL | FK→ | Not in use. |
| 209 | `PAYMENT_METHOD_CD` | DOUBLE | NOT NULL |  | Payment Method |
| 210 | `PA_BEG_DT_TM` | DATETIME |  |  | PA Beginning Date and time |
| 211 | `PA_BEG_TZ` | DOUBLE |  |  | Time zone associated with the corresponding DT_TM column. |
| 212 | `PA_END_DT_TM` | DATETIME |  |  | PA End Date and Time |
| 213 | `PA_END_TZ` | DOUBLE |  |  | Time zone associated with the corresponding DT_TM column. |
| 214 | `PA_NUMBER` | VARCHAR(25) |  |  | Prior Authorization Number |
| 215 | `PCA_DOSE_UNIT_CD` | DOUBLE |  |  | Code value from code set 54 representing the PCA Dose Unit. |
| 216 | `PCA_DOSE_UNIT_S` | VARCHAR(40) |  |  | Display value for the PCA Dose Unit. |
| 217 | `PCA_DOSE_VALUE` | DOUBLE |  |  | On-demand dose delivered by pump upon patient pressing dose delivery button |
| 218 | `PERSON_ID` | DOUBLE | NOT NULL | FK→ | This is the value of the unique primary identifier of the person table. It is an internal system assigned number. |
| 219 | `PERSON_NAME_S` | VARCHAR(50) |  |  | Patients name. |
| 220 | `PERSON_OWE_QTY` | DOUBLE |  |  | Amount of quantity owed to the patient on this dispense. |
| 221 | `PHARM_COMMENT_TEXT_ID` | DOUBLE |  | FK→ | Long text id of the pharmacy comment. Originally from order_comment table with comment_type_cd of "PHARM COMMEN". |
| 222 | `PHARM_TYPE_CD` | DOUBLE | NOT NULL |  | Pharm type cd |
| 223 | `PHYSICIAN_DEA_TXT` | VARCHAR(50) |  |  | The doctor's Drug Enforcement Administration number |
| 224 | `PKG_COUNT` | DOUBLE |  |  | Indicates the number of packages involved in the dispense event. |
| 225 | `PKG_NBR` | DOUBLE |  |  | Indicates the relative package within the dispense if multiple packages are dispensed. (i.e., 1 of 2, 2 of 2) |
| 226 | `PKG_QUANTITY` | DOUBLE |  |  | Indicates the quantity in each package |
| 227 | `PRICE_CODE_CD` | DOUBLE | NOT NULL |  | Price code code |
| 228 | `PRN_IND` | DOUBLE |  |  | Indicates whether this is a prn order |
| 229 | `PRN_REASON_CD` | DOUBLE | NOT NULL |  | Code Value representing PRN reason. |
| 230 | `PRN_REASON_S` | VARCHAR(60) |  |  | String representation of the PRN reason for the order. |
| 231 | `PRODUCT_NOTE_ID` | DOUBLE | NOT NULL | FK→ | Identifier representing the product note. |
| 232 | `PRODUCT_STRENGTH_UNIT_CD` | DOUBLE |  |  | Strength unit code value of an individual product within an order. |
| 233 | `PRODUCT_STRENGTH_VALUE` | DOUBLE |  |  | Strength value of an individual product within an order. |
| 234 | `PRODUCT_VOLUME_UNIT_CD` | DOUBLE |  |  | Volume unit code value of an individual product within an order. |
| 235 | `PRODUCT_VOLUME_VALUE` | DOUBLE |  |  | Volume value of an individual product within an order. |
| 236 | `PROD_CNT` | DOUBLE |  |  | Total number of products in the ingredient |
| 237 | `PROD_DESC` | VARCHAR(200) |  |  | Description of product. |
| 238 | `PROXY_PRESCRIBER_ID` | DOUBLE | NOT NULL |  | The proxy prescriber identifier of the prescription. |
| 239 | `PROXY_PRESCRIBER_NAME` | VARCHAR(50) |  |  | The proxy prescriber name of the prescription. |
| 240 | `QTY_REMAINING` | DOUBLE |  |  | Quantity remaining |
| 241 | `RACE_CD` | DOUBLE | NOT NULL |  | code value for race |
| 242 | `RACE_S` | CHAR(40) |  |  | race |
| 243 | `RATE` | DOUBLE |  |  | IV rate |
| 244 | `REASON_FOR_USE` | VARCHAR(100) |  |  | reason for use |
| 245 | `REFILLS_REMAINING` | DOUBLE |  |  | refills remaining |
| 246 | `REFILL_QTY` | DOUBLE |  |  | refill quantity |
| 247 | `REIMBURSEMENT` | DOUBLE |  |  | Amount reimbursed by the health plan |
| 248 | `REPLACE_EVERY` | DOUBLE |  |  | Length of time after which an IV bag should be replaced |
| 249 | `REPLACE_EVERY_UNIT_CD` | DOUBLE | NOT NULL |  | Unit of Measure for replace_every interval |
| 250 | `REPLACE_EVERY_UNIT_S` | VARCHAR(40) |  |  | Denormalized display value for replace_every_unit_cd |
| 251 | `REPORT_ID` | DOUBLE | NOT NULL |  | Column Not Used |
| 252 | `ROOM_CD` | DOUBLE | NOT NULL |  | Code value for room |
| 253 | `ROOM_S` | CHAR(40) |  |  | room description |
| 254 | `ROUTE_CD` | DOUBLE | NOT NULL |  | Route code. |
| 255 | `ROUTE_S` | CHAR(40) |  |  | Route description |
| 256 | `RPH_ID` | DOUBLE | NOT NULL |  | ID for pharmacist |
| 257 | `RPH_INITIALS` | CHAR(8) |  |  | Pharmacist initials |
| 258 | `RPH_NAME` | VARCHAR(50) |  |  | Pharmacist name |
| 259 | `RUN_ID` | DOUBLE | NOT NULL | FK→ | Print run identifier |
| 260 | `RX_EXPIRE_DT_TM` | DATETIME |  |  | rx expire date and time |
| 261 | `RX_EXPIRE_TZ` | DOUBLE |  |  | Time zone associated with the corresponding DT_TM column. |
| 262 | `RX_NBR` | DOUBLE |  |  | Retail number |
| 263 | `RX_NBR_CD` | DOUBLE | NOT NULL |  | Prescription number |
| 264 | `RX_NBR_IN_SET` | DOUBLE |  |  | retail number in set |
| 265 | `RX_NBR_S` | VARCHAR(40) |  |  | Formatted Prescription Number |
| 266 | `RX_PERSON_OWE_DOSES_CNT` | DOUBLE |  |  | This field will populate with person owe doses associated to the order. |
| 267 | `RX_QTY` | DOUBLE |  |  | rx quantity |
| 268 | `RX_SET_SIZE` | DOUBLE |  |  | rx_set_size |
| 269 | `RX_WORKSTATION_CD` | DOUBLE | NOT NULL |  | Service Resource Level 5 code (Code Set 221, CDF Meaning 'LEVEL5'). Identifies the pharmacy workstation that administered the order; entered, dispensed, etc. |
| 270 | `SAFETY_CAP_CD` | DOUBLE | NOT NULL |  | Indicates whether or not the patient has requested a Safety Cap for their prescription |
| 271 | `SAFETY_CAP_S` | VARCHAR(1) |  |  | safety_cap_s |
| 272 | `SCH_PRN_IND` | DOUBLE |  |  | Indicator for prn order with scheduled times |
| 273 | `SCRIPT_CLARIFY_CD` | DOUBLE | NOT NULL |  | Script (prescription) clarification code |
| 274 | `SCRIPT_ORIGIN_CD` | DOUBLE | NOT NULL |  | Code indicating the origin of the prescription. |
| 275 | `SEX_CD` | DOUBLE | NOT NULL |  | Sex code |
| 276 | `SEX_S` | CHAR(40) |  |  | Sex description |
| 277 | `SIDE_EFFECT_CODE` | VARCHAR(10) |  |  | Not in use at present time. |
| 278 | `SIG_ALT_LANG_TEXT_ID` | DOUBLE | NOT NULL | FK→ | Long Text ID for the alternate language signature instructions. |
| 279 | `SIG_CODES` | VARCHAR(100) |  |  | Pharmacy signature codes (such as PO BID) |
| 280 | `SIG_TEXT_ID` | DOUBLE | NOT NULL | FK→ | Long Text ID for the primary or default language signature instructions. |
| 281 | `SKIP_DISPENSE_FLAG` | DOUBLE | NOT NULL |  | A flag that indicates if the product was dispensed or skipped |
| 282 | `SORT_CLASS` | VARCHAR(20) |  |  | Not in use. |
| 283 | `SPLIT_CONTAINER_FLAG` | DOUBLE |  |  | Indicates whether the dispense event was associated to a split container dispense. |
| 284 | `STATUS_DT_TM` | DATETIME |  |  | Status date and time |
| 285 | `STRENGTH` | DOUBLE |  |  | Strength value |
| 286 | `STRENGTH_UNIT_CD` | DOUBLE | NOT NULL |  | Code value for strength unit |
| 287 | `STRENGTH_UNIT_S` | CHAR(40) |  |  | Strength unit description |
| 288 | `STRENGTH_WITH_OVERFILL_UNIT_CD` | DOUBLE | NOT NULL |  | The strength dose unit on the product's ingredient including the overfill added during TPN balancing. |
| 289 | `STRENGTH_WITH_OVERFILL_UNIT_S` | VARCHAR(40) |  |  | Display value of the strength_with_overfill unit of measure. |
| 290 | `STRENGTH_WITH_OVERFILL_VALUE` | DOUBLE | NOT NULL |  | The strength dose on the product's ingredient including the overfill added during TPN balancing. |
| 291 | `SUSPEND_ROUTING_TYPE_CD` | DOUBLE |  |  | Routing type for a suspended order. |
| 292 | `TECH_ID` | DOUBLE | NOT NULL |  | Pharmacy tech prsnl_id that was responsible for this print. |
| 293 | `TECH_INITIALS` | VARCHAR(8) |  |  | Pharmacy Tech username that was responsible for this print. |
| 294 | `TECH_NAME` | VARCHAR(50) |  |  | Pharmacy tech name (full formatted) that was responsible for this print. |
| 295 | `TEMP_STOCK_IND` | DOUBLE | NOT NULL |  | If set to 1, this was a temporary stock event. |
| 296 | `THER_CLASS_CODE` | VARCHAR(20) |  |  | AHFS Code Number (e.g. 080000) |
| 297 | `THER_CLASS_DESC` | VARCHAR(100) |  |  | AHFS class description (e.g. Anti-Infectives) |
| 298 | `THER_CLASS_ID` | DOUBLE | NOT NULL | FK→ | Key to alt_sel_cat table |
| 299 | `THER_CLASS_SORT_CODE` | VARCHAR(20) |  |  | Therapeutic class of first ingredient, used for sorting. |
| 300 | `TITRATE_IND` | DOUBLE |  |  | Titrate indicator; 1 = titrate, 0 = not titrate. |
| 301 | `TNF_ID` | DOUBLE | NOT NULL |  | Key to template_non-formulary table |
| 302 | `TOTAL_REFILLS` | DOUBLE |  |  | Number of times a prescription can be re-filled (does NOT include the initial fill) |
| 303 | `TOTAL_RX_QTY` | DOUBLE |  |  | total rx quantity |
| 304 | `TOT_VOLUME` | DOUBLE |  |  | Total volume |
| 305 | `TRACK_NBR` | DOUBLE |  |  | A number to track the prescription |
| 306 | `TRACK_NBR_CD` | DOUBLE | NOT NULL |  | TRACK nbr cd |
| 307 | `TRACK_NBR_S` | VARCHAR(40) |  |  | track number s |
| 308 | `TRANSFER_TO_LOC_CD` | DOUBLE | NOT NULL |  | Location code where stock is transferred to. |
| 309 | `TRANSFER_TO_LOC_S` | VARCHAR(40) |  |  | Display value for location code where stock is transferred to. |
| 310 | `UC_PRICE` | DOUBLE |  |  | Usual and Customary Price |
| 311 | `UNIQUE_BAG_ID` | DOUBLE | NOT NULL |  | Column Not Used |
| 312 | `UNROUNDED_DOSE_QTY` | DOUBLE |  |  | Product's quantity per dose prior to rounding for the product dispense. |
| 313 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 314 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 315 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 316 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 317 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 318 | `VERIFY_PRSNL_ID` | DOUBLE |  | FK→ | Personnel who created or verified the order. |
| 319 | `VOLUME` | DOUBLE |  |  | Volume |
| 320 | `VOLUME_UNIT_CD` | DOUBLE | NOT NULL |  | Volume unit of measure code. |
| 321 | `VOLUME_UNIT_S` | CHAR(40) |  |  | Volume unit of measure. |
| 322 | `VOLUME_WITH_OVERFILL_UNIT_CD` | DOUBLE | NOT NULL |  | The volume dose unit on the product's ingredient including the overfill added during TPN balancing. |
| 323 | `VOLUME_WITH_OVERFILL_UNIT_S` | VARCHAR(40) |  |  | Display value of the volume_with_overfill unit of measure. |
| 324 | `VOLUME_WITH_OVERFILL_VALUE` | DOUBLE | NOT NULL |  | The volume dose on the product's ingredient including the overfill added during TPN balancing. |
| 325 | `WASTE_FLAG` | DOUBLE |  |  | Indicates this dispense event can have waste applied. |
| 326 | `WEIGHT` | DOUBLE |  |  | Patient"s weight. |
| 327 | `WEIGHT_UNIT_CD` | DOUBLE | NOT NULL |  | Unit of measure patients weight is measured in. |
| 328 | `WEIGHT_UNIT_S` | CHAR(40) |  |  | Unit of measure patients weight is measured in. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `COMPOUND_TEXT_ID` | [LONG_TEXT](LONG_TEXT.md) | `LONG_TEXT_ID` |
| `DISPENSE_COMMENT_TEXT_ID` | [LONG_TEXT](LONG_TEXT.md) | `LONG_TEXT_ID` |
| `DISPENSE_ID` | [DISPENSE_HX](DISPENSE_HX.md) | `DISPENSE_HX_ID` |
| `DISPENSE_STATUS_HX_ID` | [DISPENSE_STATUS_HX](DISPENSE_STATUS_HX.md) | `DISPENSE_STATUS_HX_ID` |
| `ENCNTR_ID` | [ENCOUNTER](ENCOUNTER.md) | `ENCNTR_ID` |
| `FILL_NOTE_ID` | [LONG_TEXT](LONG_TEXT.md) | `LONG_TEXT_ID` |
| `FINNBR_ID` | [ENCNTR_ALIAS](ENCNTR_ALIAS.md) | `ENCNTR_ALIAS_ID` |
| `HEALTH_PLAN_ID` | [HEALTH_PLAN](HEALTH_PLAN.md) | `HEALTH_PLAN_ID` |
| `ICD9_ID` | [NOMENCLATURE](NOMENCLATURE.md) | `NOMENCLATURE_ID` |
| `ITEM_ID` | [ITEM_DEFINITION](ITEM_DEFINITION.md) | `ITEM_ID` |
| `LABEL1_ID` | [LONG_TEXT](LONG_TEXT.md) | `LONG_TEXT_ID` |
| `LABEL2_ID` | [LONG_TEXT](LONG_TEXT.md) | `LONG_TEXT_ID` |
| `MEDREC_NBR_ID` | [ENCNTR_ALIAS](ENCNTR_ALIAS.md) | `ENCNTR_ALIAS_ID` |
| `MED_PRODUCT_ID` | [MED_PRODUCT](MED_PRODUCT.md) | `MED_PRODUCT_ID` |
| `ORDER_COMMENT_ID` | [LONG_TEXT](LONG_TEXT.md) | `LONG_TEXT_ID` |
| `ORDER_ID` | [ORDERS](ORDERS.md) | `ORDER_ID` |
| `PATIENT_TEXT_ID` | [LONG_TEXT](LONG_TEXT.md) | `LONG_TEXT_ID` |
| `PAT_TEXT_ID` | [LONG_TEXT](LONG_TEXT.md) | `LONG_TEXT_ID` |
| `PERSON_ID` | [PERSON](PERSON.md) | `PERSON_ID` |
| `PHARM_COMMENT_TEXT_ID` | [LONG_TEXT](LONG_TEXT.md) | `LONG_TEXT_ID` |
| `PRODUCT_NOTE_ID` | [LONG_TEXT](LONG_TEXT.md) | `LONG_TEXT_ID` |
| `RUN_ID` | [FILL_PRINT_HX](FILL_PRINT_HX.md) | `RUN_ID` |
| `SIG_ALT_LANG_TEXT_ID` | [LONG_TEXT](LONG_TEXT.md) | `LONG_TEXT_ID` |
| `SIG_TEXT_ID` | [LONG_TEXT](LONG_TEXT.md) | `LONG_TEXT_ID` |
| `THER_CLASS_ID` | [ALT_SEL_CAT](ALT_SEL_CAT.md) | `ALT_SEL_CATEGORY_ID` |
| `VERIFY_PRSNL_ID` | [PRSNL](PRSNL.md) | `PERSON_ID` |

