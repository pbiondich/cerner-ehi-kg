# CE_MED_RESULT

> There are two types of medication administration, continuous (IV, IVP) and intermittent. Each intermittent administration occupies one row in the ce_med_result table. For continuous administration, each action will be represented by a ce_med_result row,

**Description:** ce med result  
**Table type:** ACTIVITY  
**Primary key:** _(not published — see note)_  
**Columns:** 49

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ADMIN_DOSAGE` | DOUBLE | NOT NULL |  | Actual volume or quantity of administration. |
| 2 | `ADMIN_END_DT_TM` | DATETIME |  |  | For continuous administrations, this field is the end of the time period in which this administration was active. If the administration is currently active, this field will be NULL. For intermittent administrations, this field does not apply. |
| 3 | `ADMIN_END_TZ` | DOUBLE |  |  | Time zone associated with the corresponding DT_TM column. |
| 4 | `ADMIN_METHOD_CD` | DOUBLE | NOT NULL |  | The method of the administration. i.e. chew, shampoo. |
| 5 | `ADMIN_NOTE` | VARCHAR(120) |  |  | Short note associated with this medication administration |
| 6 | `ADMIN_PROV_ID` | DOUBLE | NOT NULL | FK→ | Personnel ID of provider administering medication. |
| 7 | `ADMIN_PT_LOC_CD` | DOUBLE | NOT NULL |  | The patient location when the medication was administered. |
| 8 | `ADMIN_ROUTE_CD` | DOUBLE | NOT NULL |  | Route of administration. i.e. PO, TOP, IM. |
| 9 | `ADMIN_SITE_CD` | DOUBLE | NOT NULL |  | For certain administration routes a body site might be needed to fully describe the method of administration. i.e. IM-Right Arm. |
| 10 | `ADMIN_START_DT_TM` | DATETIME | NOT NULL |  | The time at which this medication administration became active for continuous administrations. For intermittent, it is the time the administration happened. |
| 11 | `ADMIN_START_TZ` | DOUBLE |  |  | Time zone associated with the corresponding DT_TM column. |
| 12 | `ADMIN_STRENGTH` | DOUBLE |  |  | Use when medication_product_cd does not specify the strength. |
| 13 | `ADMIN_STRENGTH_UNIT_CD` | DOUBLE | NOT NULL |  | Units for admin_strength. This may be a compound unit (i.e. ml/hr). |
| 14 | `BOLUS_TYPE_CD` | DOUBLE |  |  | Bolus (an amount of IV medication administered rapidly to decrease the response time or to be used as a loading dose prior to an infusion) type. i.e. PCA, Loading. |
| 15 | `DILUENT_TYPE_CD` | DOUBLE | NOT NULL |  | The diluent if one was used. The diluent is an event code. |
| 16 | `DOSAGE_UNIT_CD` | DOUBLE | NOT NULL |  | Unit of measurement for dosage. i.e. tablet, ml. |
| 17 | `EVENT_ID` | DOUBLE | NOT NULL |  | Foreign key to the Event Table. |
| 18 | `IMMUNIZATION_TYPE_CD` | DOUBLE | NOT NULL |  | This field classifies the type of Immunization given. Some examples are Pediatric, Travel and Adult. |
| 19 | `INFUSED_VOLUME` | DOUBLE |  |  | The volume at any one point in time that remains in the IV Bag. |
| 20 | `INFUSED_VOLUME_UNIT_CD` | DOUBLE | NOT NULL |  | Unit of measure for infused volume |
| 21 | `INFUSION_RATE` | DOUBLE |  |  | For continuously administered medications, IV or IVP, the infusion rate and unit is used to capture the flow rate of the medication into the patient. |
| 22 | `INFUSION_TIME_CD` | DOUBLE | NOT NULL |  | The unit of measure for the duration of the administration. |
| 23 | `INFUSION_UNIT_CD` | DOUBLE | NOT NULL |  | The unit of measure for volume or quantity of the medication. i.e. ml, drip, tablet. |
| 24 | `INITIAL_DOSAGE` | DOUBLE | NOT NULL |  | Initial volume or quantity of the administered dose. |
| 25 | `INITIAL_VOLUME` | DOUBLE |  |  | Total volume medication and diluent at the beginning of the administration. |
| 26 | `IV_EVENT_CD` | DOUBLE | NOT NULL |  | Code to describe any change or activity on the iv for the patient. |
| 27 | `MEDICATION_FORM_CD` | DOUBLE | NOT NULL |  | Form of the medication (e.g., Caplet, Liquid, Ointment, etc.). Depending on how we going to allow clinicians to specify the actual product administered, this info might be moved to the product admin sub table. . |
| 28 | `PH_DISPENSE_ID` | DOUBLE | NOT NULL |  | *** OBSOLETE |
| 29 | `REASON_REQUIRED_FLAG` | DOUBLE |  |  | Whether the clinician is required to enter a reason for giving this medication. |
| 30 | `REFUSAL_CD` | DOUBLE | NOT NULL |  | Indicates the reason the patient refused the medical substance. Any entry in this field indicates that the patient did not take the substance. |
| 31 | `REMAINING_VOLUME` | DOUBLE |  |  | The remaining volume is the portion of the medication that is wasted after administering it to the patient. Used for reimbursement of the wasted amount. |
| 32 | `REMAINING_VOLUME_UNIT_CD` | DOUBLE | NOT NULL |  | The remaining volume unit code is the unit of measure for the portion of medication that was wasted after administering it to the patient. Used for reimbursement of the wasted amount. |
| 33 | `RESPONSE_REQUIRED_FLAG` | DOUBLE |  |  | Whether the clinician is required to document patient¿s response to the medication. |
| 34 | `SUBSTANCE_EXP_DT_TM` | DATETIME |  |  | Expiration date of the medical substance administered |
| 35 | `SUBSTANCE_EXP_DT_TXT` | VARCHAR(8) |  |  | Textual expiration date of the medical substance administered in the format of YYYYMMDD, YYYYMM, or YYYY; Captures the expiration date of a substance (medication) as it was entered by the user. |
| 36 | `SUBSTANCE_LOT_NUMBER` | VARCHAR(20) |  |  | Lot number of the medical substance administered |
| 37 | `SUBSTANCE_MANUFACTURER_CD` | DOUBLE | NOT NULL |  | The manufacturer of the medical substance administered. |
| 38 | `SYNONYM_ID` | DOUBLE | NOT NULL |  | The synonym of the order ingredient for this medication result. |
| 39 | `SYSTEM_ENTRY_DT_TM` | DATETIME |  |  | Timestamp of when the administration information was entered into the source system. |
| 40 | `TOTAL_INTAKE_VOLUME` | DOUBLE |  |  | The amount that impacted the patient¿s intake volume. |
| 41 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 42 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 43 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 44 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 45 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 46 | `VALID_FROM_DT_TM` | DATETIME | NOT NULL |  | Contains the "Beginning Point" of when a row in the table is valid. |
| 47 | `VALID_UNTIL_DT_TM` | DATETIME | NOT NULL |  | Contains the "End Point" of when a row in the table is valid. Current version of the result has an open "Until Dt Tm" value. We need to determine what that value is. |
| 48 | `WEIGHT_UNIT_CD` | DOUBLE | NOT NULL |  | The unit of measurement for the weight value. |
| 49 | `WEIGHT_VALUE` | DOUBLE | NOT NULL |  | The value of the documented weight used in charting the medication result. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `ADMIN_PROV_ID` | [PERSON](PERSON.md) | `PERSON_ID` |

