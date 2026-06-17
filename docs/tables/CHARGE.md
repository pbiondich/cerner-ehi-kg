# CHARGE

> Processed charge events.

**Description:** Charge  
**Table type:** ACTIVITY  
**Primary key:** `CHARGE_ITEM_ID`  
**Columns:** 88  
**Referenced by:** 10 columns

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ABN_STATUS_CD` | DOUBLE | NOT NULL |  | This field displays the status of the charge regarding whether it was required, required & missing, or present. |
| 2 | `ACTIVE_IND` | DOUBLE |  |  | The table row is active or inactive. A row is generally active unless it is in an inactive state such as logically deleted, combined away, pending purge, etc. |
| 3 | `ACTIVE_STATUS_CD` | DOUBLE | NOT NULL |  | Indicates the status of the row itself (not the data in the row) such as active, inactive, combined away, pending purge, etc. |
| 4 | `ACTIVE_STATUS_DT_TM` | DATETIME |  |  | The date and time that the active_status_cd was set. |
| 5 | `ACTIVE_STATUS_PRSNL_ID` | DOUBLE | NOT NULL |  | The person who caused the active_status_cd to be set or change. |
| 6 | `ACTIVITY_DT_TM` | DATETIME |  |  | not used |
| 7 | `ACTIVITY_SUB_TYPE_CD` | DOUBLE | NOT NULL |  | The Activity_Sub_Type_Cd field identifies the Activity Sub Type or modality that the radiologist wants to restrict proxy for. |
| 8 | `ACTIVITY_TYPE_CD` | DOUBLE | NOT NULL |  | A code value that uniquely identifies to which "net" (PathNet, RadNet) and/or what department (General Lab, Microbiology) an order belongs. |
| 9 | `ADJUSTED_DT_TM` | DATETIME |  |  | The date and time associated with an adjustment. |
| 10 | `ADMIT_TYPE_CD` | DOUBLE | NOT NULL |  | This is the value from codeset 71 that represents the visit/encounter type from this encounter, if available. |
| 11 | `ALPHA_NOMEN_ID` | DOUBLE | NOT NULL | FK→ | alpha_nomen_id, which will hold the alpha nomen id for alpha response charges, will help the charging server when creating offsets so it will match up a debit with a credit correctly if the offset already exists. |
| 12 | `BEG_EFFECTIVE_DT_TM` | DATETIME |  |  | The date and time for which this table row becomes effective. Normally, this will be the date and time the row is added, but could be a past or future date and time. |
| 13 | `BILL_ITEM_ID` | DOUBLE | NOT NULL | FK→ | The ID of the bill item from the bill_item table. |
| 14 | `BUNDLE_ID` | DOUBLE | NOT NULL |  | Identifies charges that were bundled by the charge transformation tool. |
| 15 | `CHARGE_DESCRIPTION` | VARCHAR(200) |  |  | Description from the bill item table. |
| 16 | `CHARGE_EVENT_ACT_ID` | DOUBLE | NOT NULL | FK→ | This is the unique primary identifier from the charge_event_act table. |
| 17 | `CHARGE_EVENT_ID` | DOUBLE | NOT NULL | FK→ | The is the unique primary identifier from the charge_event table. |
| 18 | `CHARGE_ITEM_ID` | DOUBLE | NOT NULL | PK | This is the value of the unique primary identifier of the charge table. It is an internal system assigned number. |
| 19 | `CHARGE_TYPE_CD` | DOUBLE | NOT NULL |  | Value from 13028 that represents whether the charge event is a debit, credit, collection, no charge, etc. |
| 20 | `COMBINE_IND` | DOUBLE |  |  | Indicates if this charge has been combined "away". This is set on the "from" charges in the combine scripts so that the batch process that runs in operations to find the "stragglers" knows which charges on an encounter or person have already been processed. |
| 21 | `COST_CENTER_CD` | DOUBLE | NOT NULL |  | This field is the cost center that a charge is associated with. |
| 22 | `CREDITED_DT_TM` | DATETIME |  |  | The date and time associated with a credit. |
| 23 | `CS_CPP_UNDO_ID` | DOUBLE | NOT NULL | FK→ | Uniquely identifies a specific undo record related to this charge record. |
| 24 | `CS_CPP_UNDO_QUAL_ID` | DOUBLE | NOT NULL |  | Uniquely identifies a specific undo record id from the CS_CPP_UNDO table_ related to the new charge record created from this as an action from this charge qualifying rule. |
| 25 | `DEF_BILL_ITEM_ID` | DOUBLE | NOT NULL | FK→ | This is the unique id of the default parent or child bill item. |
| 26 | `DEPARTMENT_CD` | DOUBLE | NOT NULL |  | This is the value from codeset 221 that represents the department in the service resource hierarchy. |
| 27 | `DISCOUNT_AMOUNT` | DOUBLE |  |  | The amount of discount applied to the gross_price to arrive at the item_price (before extending by the quantity). |
| 28 | `ENCNTR_ID` | DOUBLE | NOT NULL | FK→ | This is the value of the unique primary identifier of the encounter table. It is an internal system assigned number. |
| 29 | `END_EFFECTIVE_DT_TM` | DATETIME |  |  | The date/time after which the row is no longer valid as active current data. This may be valued with the date that the row became inactive. |
| 30 | `EPSDT_IND` | DOUBLE |  |  | This field indicates whether or not the patient participates in an EPSDT. EPSDT is an entitlement provided by Medicaid. It is a service available to all individuals age 20 and younger that are eligible for medical assistance through their participating state Medicaid programs. The program includes early detection of illness or defects through regular and periodic screening examinations, follow up care, and promotion of healthy lifestyles. |
| 31 | `FIN_CLASS_CD` | DOUBLE | NOT NULL |  | Patient's financial class |
| 32 | `GROSS_PRICE` | DOUBLE |  |  | The price of an item before applying any discount. |
| 33 | `HEALTH_PLAN_ID` | DOUBLE | NOT NULL | FK→ | Identifies the person's health plan. It is the unique primary identifier from the health_plan table. |
| 34 | `INSTITUTION_CD` | DOUBLE | NOT NULL |  | This is the value from codeset 221 that represents the institution in the service resource hierarchy. |
| 35 | `INST_FIN_NBR` | VARCHAR(50) |  |  | This field will contain the financial number of the bill performing org |
| 36 | `INTERFACE_FILE_ID` | DOUBLE | NOT NULL | FK→ | This is the value of the unique primary identifier of the interface_file table. |
| 37 | `ITEM_ALLOWABLE` | DOUBLE |  |  | not used |
| 38 | `ITEM_COPAY` | DOUBLE |  |  | This field is passed from Pharmacy. Original data source is from one of two places. Either the Health Plan Benefit indicates a Copay amount or percent, or through the Online Claims process the Copay amount will be calculated and electronically received via real time interface. |
| 39 | `ITEM_DEDUCTIBLE_AMT` | DOUBLE |  |  | The deductible amount for a given item. |
| 40 | `ITEM_EXTENDED_PRICE` | DOUBLE |  |  | The final price as calculated by multiplying the item_price by the item_quantity. |
| 41 | `ITEM_INTERVAL_ID` | DOUBLE | NOT NULL | FK→ | If this charge was written as a result of qualifying in an interval for which multiple charges are created, this is the unique identifier of the item interval on which the charge was created. |
| 42 | `ITEM_LIST_PRICE` | DOUBLE |  |  | The price associated with the List Price schedule that was identified in the tier. |
| 43 | `ITEM_PRICE` | DOUBLE |  |  | The price as determined through tier logic, after discounting has been applied. |
| 44 | `ITEM_PRICE_ADJ_AMT` | DOUBLE |  |  | Indicates the offset that the item price was adjusted by using the Price Adjustment Factor |
| 45 | `ITEM_QUANTITY` | DOUBLE |  |  | The quantity the price should be multiplied by to arrive at the item_extended_price. |
| 46 | `ITEM_REIMBURSEMENT` | DOUBLE |  |  | Indicates the portion of Item_Extended_Price that is the patient's Health Plan's responsibility. This field will be sent outbound to Billing Systems, Accounts Receivable systems, or used for reporting purposes. If the Health Plan does not cover the Retail prescription, then this field will be zero. The difference between the Item_price_extended, copay_amt and Reimbursement_amt will be the contract write off. |
| 47 | `LEVEL5_CD` | DOUBLE | NOT NULL |  | This is the value from codeset 221 that represents the level 5 (exam room, bench, instrument) in the service resource hierarchy. |
| 48 | `LIST_PRICE_SCHED_ID` | DOUBLE | NOT NULL | FK→ | The price schedule identifier associated with the list price schedule identified in the tier. |
| 49 | `MANUAL_IND` | DOUBLE |  |  | Indicates if this charge is currently on hold as a manual charge or if it has ever been on hold as a manual charge. |
| 50 | `MED_SERVICE_CD` | DOUBLE | NOT NULL |  | This is the value from codeset 34 that represents the category of treatment, surgery, or general resources. |
| 51 | `OFFSET_CHARGE_ITEM_ID` | DOUBLE | NOT NULL | FK→ | The charge item identifier of the offsetting charge. The charge that was generated to completely offset this charge item. |
| 52 | `ORDER_ID` | DOUBLE | NOT NULL | FK→ | This is the unique primary identifier from the order table. |
| 53 | `ORD_LOC_CD` | DOUBLE | NOT NULL |  | Value from 220 that represents the location to which the person was registered. |
| 54 | `ORD_PHYS_ID` | DOUBLE | NOT NULL |  | ID from prsnl table of the ordering physician. |
| 55 | `ORIGINAL_ENCNTR_ID` | DOUBLE |  | FK→ | Contains the original clinical encounter ID for every charge that is posted. |
| 56 | `ORIGINAL_ORG_ID` | DOUBLE |  | FK→ | This field Is used to store the Original Organization Id from where the charges are posted |
| 57 | `PARENT_CHARGE_ITEM_ID` | DOUBLE | NOT NULL |  | The charge_item_id of the parent charge associated with this charge item. |
| 58 | `PATIENT_RESPONSIBILITY_FLAG` | DOUBLE | NOT NULL |  | Flag to determine whether the patient is responsible or not. 0 - unknown; 1 - patient responsible; 2 - patient not responsible |
| 59 | `PAYOR_ID` | DOUBLE | NOT NULL | FK→ | ID from the organization table that represents the client organization associated with this charge. |
| 60 | `PAYOR_TYPE_CD` | DOUBLE | NOT NULL |  | The code value in this field, from code set 25089, describes where the payor_id (or organization_id) was derived from. |
| 61 | `PERF_LOC_CD` | DOUBLE | NOT NULL |  | Value from 220 that represents the location at which the services were provided. |
| 62 | `PERF_PHYS_ID` | DOUBLE | NOT NULL |  | ID from prsnl table of the performing physician. |
| 63 | `PERSON_ID` | DOUBLE | NOT NULL | FK→ | This is the value of the unique primary identifier of the person table. It is an internal system assigned number. |
| 64 | `POSTED_CD` | DOUBLE | NOT NULL |  | Indicates if the charge has been billed or interfaced. |
| 65 | `POSTED_DT_TM` | DATETIME |  |  | Indicates the date and time the charge was billed or interfaced. |
| 66 | `POSTED_ID` | DOUBLE | NOT NULL | FK→ | Stores the person id who actually created this charge. |
| 67 | `PRICE_SCHED_ID` | DOUBLE | NOT NULL | FK→ | The id from the price_sched table that identifies the price schedule used to price this charge item. Tier logic determines this value. This is also the unique primary identifier from the price_sched table. |
| 68 | `PRICING_STATUS_CD` | DOUBLE | NOT NULL |  | Describes the status of the charge |
| 69 | `PROCESS_FLG` | DOUBLE |  |  | Indicates if the charge is pending, suspended/held, skipped, interfaced, combined or bundled. 0 - Pending; 1 - Suspended; 2 - Review; 3 - On Hold; 4 - Manual; 5 - Skipped; 6 - Combined; 7 - Absorbed; 8 - ABN Required; 10 - Offset; 11 - Adjusted; 12 - Grouped; 100 - Posted; 177 - Bundled - Profit; 222 - Temporary Near Time In-Process Flag; 777 - Bundled; 977 - Bundled - Interfaced; 996 - OMF Stats ONly; 997 - Statistics Only; 998 - Pharmacy No Charge; 999 - Interfaced |
| 70 | `PROVIDER_SPECIALTY_CD` | DOUBLE |  |  | Stores the rendering physicians specialty if one applies to the charge so that pricing may be driven by specialty. |
| 71 | `REASON_COMMENT` | VARCHAR(200) |  |  | obsolete - not currently being used |
| 72 | `REF_PHYS_ID` | DOUBLE | NOT NULL |  | ID from prsnl table of the referring physician. |
| 73 | `RESEARCH_ACCT_ID` | DOUBLE | NOT NULL |  | not used |
| 74 | `SECTION_CD` | DOUBLE | NOT NULL |  | This is the value from codeset 221 that represents the section in the service resource hierarchy. |
| 75 | `SERVER_PROCESS_FLAG` | DOUBLE |  |  | Flag used to determine if the server has finished processing: 0 - unknown; 1 - server has not finished processing; 2 - server has finished processing; 3 - Reporcessing of interval charges |
| 76 | `SERVICE_DT_TM` | DATETIME |  |  | The service date and time (from the cea_dt_tm on Charge Event Activity table). |
| 77 | `SERVICE_INTERFACE_FLAG` | DOUBLE |  |  | Flag to determine whether the charge is interfaced through service based approach or not. |
| 78 | `START_DT_TM` | DATETIME |  |  | The date and time the service was started. |
| 79 | `STOP_DT_TM` | DATETIME |  |  | The date and time the service ended. |
| 80 | `SUBSECTION_CD` | DOUBLE | NOT NULL |  | This is the value from codeset 221 that represents the subsection in the service resource hierarchy. |
| 81 | `SUSPENSE_RSN_CD` | DOUBLE | NOT NULL |  | not used |
| 82 | `TIER_GROUP_CD` | DOUBLE | NOT NULL |  | This is the tier that was responsible for creating the charge. |
| 83 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 84 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 85 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 86 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 87 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 88 | `VERIFY_PHYS_ID` | DOUBLE | NOT NULL |  | ID of the physician who verified the result. This is used mostly for the "read" in Radiology. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `ALPHA_NOMEN_ID` | [NOMENCLATURE](NOMENCLATURE.md) | `NOMENCLATURE_ID` |
| `BILL_ITEM_ID` | [BILL_ITEM](BILL_ITEM.md) | `BILL_ITEM_ID` |
| `CHARGE_EVENT_ACT_ID` | [CHARGE_EVENT_ACT](CHARGE_EVENT_ACT.md) | `CHARGE_EVENT_ACT_ID` |
| `CHARGE_EVENT_ID` | [CHARGE_EVENT](CHARGE_EVENT.md) | `CHARGE_EVENT_ID` |
| `CS_CPP_UNDO_ID` | [CS_CPP_UNDO](CS_CPP_UNDO.md) | `CS_CPP_UNDO_ID` |
| `DEF_BILL_ITEM_ID` | [BILL_ITEM](BILL_ITEM.md) | `BILL_ITEM_ID` |
| `ENCNTR_ID` | [ENCOUNTER](ENCOUNTER.md) | `ENCNTR_ID` |
| `HEALTH_PLAN_ID` | [HEALTH_PLAN](HEALTH_PLAN.md) | `HEALTH_PLAN_ID` |
| `INTERFACE_FILE_ID` | [INTERFACE_FILE](INTERFACE_FILE.md) | `INTERFACE_FILE_ID` |
| `ITEM_INTERVAL_ID` | [ITEM_INTERVAL_TABLE](ITEM_INTERVAL_TABLE.md) | `ITEM_INTERVAL_ID` |
| `LIST_PRICE_SCHED_ID` | [PRICE_SCHED](PRICE_SCHED.md) | `PRICE_SCHED_ID` |
| `OFFSET_CHARGE_ITEM_ID` | [CHARGE](CHARGE.md) | `CHARGE_ITEM_ID` |
| `ORDER_ID` | [ORDERS](ORDERS.md) | `ORDER_ID` |
| `ORIGINAL_ENCNTR_ID` | [ENCOUNTER](ENCOUNTER.md) | `ENCNTR_ID` |
| `ORIGINAL_ORG_ID` | [ORGANIZATION](ORGANIZATION.md) | `ORGANIZATION_ID` |
| `PAYOR_ID` | [ORGANIZATION](ORGANIZATION.md) | `ORGANIZATION_ID` |
| `PERSON_ID` | [PERSON](PERSON.md) | `PERSON_ID` |
| `POSTED_ID` | [PRSNL](PRSNL.md) | `PERSON_ID` |
| `PRICE_SCHED_ID` | [PRICE_SCHED](PRICE_SCHED.md) | `PRICE_SCHED_ID` |

## Referenced by (10)

| From table | Column |
|------------|--------|
| [CHARGE](CHARGE.md) | `OFFSET_CHARGE_ITEM_ID` |
| [CHARGE_MOD](CHARGE_MOD.md) | `CHARGE_ITEM_ID` |
| [CHARGE_TRANS_LOG](CHARGE_TRANS_LOG.md) | `RELATED_CHARGE_ITEM_ID` |
| [CS_CPP_UNDO_DETAIL](CS_CPP_UNDO_DETAIL.md) | `CHARGE_ITEM_ID` |
| [INTERFACE_CHARGE](INTERFACE_CHARGE.md) | `CHARGE_ITEM_ID` |
| [PCS_CHARGE_MOD_ABN](PCS_CHARGE_MOD_ABN.md) | `CHARGE_ITEM_ID` |
| [PFT_CHARGE](PFT_CHARGE.md) | `CHARGE_ITEM_ID` |
| [PFT_CHARGE](PFT_CHARGE.md) | `MV_ORIG_CHRG_ITEM_ID` |
| [PFT_COMBINE_LOG](PFT_COMBINE_LOG.md) | `CHARGE_ITEM_ID` |
| [RCR_TRANS_DIST](RCR_TRANS_DIST.md) | `CHARGE_ITEM_ID` |

