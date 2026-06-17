# INTERFACE_CHARGE

> A batch process populates this file from the charge and charge mod tables with charge information to be used by the ESO server.

**Description:** Interface Charge  
**Table type:** ACTIVITY  
**Primary key:** _(not published — see note)_  
**Columns:** 96

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ABN_STATUS_CD` | DOUBLE | NOT NULL |  | This field displays the status of the charge regarding whether it was required, present, present & required, required and not present, or not present. |
| 2 | `ACTIVE_IND` | DOUBLE |  |  | The table row is active or inactive. A row is generally active unless it is in an inactive state such as logically deleted, combined away, pending purge, etc. |
| 3 | `ACTIVE_STATUS_CD` | DOUBLE | NOT NULL |  | Indicates the status of the row itself (not the data in the row) such as active, inactive, combined away, pending purge, etc. |
| 4 | `ACTIVE_STATUS_DT_TM` | DATETIME |  |  | The date and time that the active_status_cd was set. |
| 5 | `ACTIVE_STATUS_PRSNL_ID` | DOUBLE | NOT NULL |  | The person who caused the active_status_cd to be set or change. |
| 6 | `ACTIVITY_TYPE_CD` | DOUBLE | NOT NULL |  | A code value that uniquely identifies to which "net" (PathNet, RadNet) and/or what department (General Lab, Microbiology) an order belongs. |
| 7 | `ADDITIONAL_ENCNTR_PHYS1_ID` | DOUBLE | NOT NULL |  | This field holds the ID from the person table of an additional physician that was involved in the encounter. This is the value of the unique primary identifier of the person table. |
| 8 | `ADDITIONAL_ENCNTR_PHYS2_ID` | DOUBLE | NOT NULL |  | This field holds the ID from the person table of an additional physician that was involved in the encounter. This is the value of the unique primary identifier of the person table. |
| 9 | `ADDITIONAL_ENCNTR_PHYS3_ID` | DOUBLE | NOT NULL |  | This field holds the ID from the person table of an additional physician that was involved in the encounter. This is the value of the unique primary identifier of the person table. |
| 10 | `ADMIT_TYPE_CD` | DOUBLE | NOT NULL |  | This is the value from codeset 71 that represents the visit/encounter type from this encounter, if available. |
| 11 | `ADM_PHYS_ID` | DOUBLE | NOT NULL |  | This field holds the ID from the person table of the admitting physician. This is the value of the unique primary identifier of the person table. |
| 12 | `ATTENDING_PHYS_ID` | DOUBLE | NOT NULL |  | This field holds the ID from the person table of the attending physician. This is the value of the unique primary identifier of the person table. |
| 13 | `BATCH_NUM` | DOUBLE |  |  | Uniquely identifies a batch of charges based on when they were written to the interface_charge table. |
| 14 | `BED_CD` | DOUBLE | NOT NULL |  | Value from 220 that represents the bed in the patient location hierarchy. |
| 15 | `BEG_EFFECTIVE_DT_TM` | DATETIME | NOT NULL |  | The date and time for which this table row becomes effective. Normally, this will be the date and time the row is added, but could be a past or future date and time. |
| 16 | `BILL_CODE1` | VARCHAR(50) |  |  | Bill code from charge_mod table with priority 2. |
| 17 | `BILL_CODE1_DESC` | VARCHAR(200) |  |  | Description from bill code from charge_mod table with priority 2. |
| 18 | `BILL_CODE2` | VARCHAR(50) |  |  | Bill code from charge_mod table with priority 3. |
| 19 | `BILL_CODE2_DESC` | VARCHAR(200) |  |  | Description from bill code from charge_mod table with priority 3. |
| 20 | `BILL_CODE3` | VARCHAR(50) |  |  | Bill code from charge_mod table with priority 4. |
| 21 | `BILL_CODE3_DESC` | VARCHAR(200) |  |  | Description from bill code from charge_mod table with priority 4. |
| 22 | `BILL_CODE_MORE_IND` | DOUBLE |  |  | This field indicates that there are more bill codes than are listed on interface_charge. |
| 23 | `BILL_CODE_TYPE_CDF` | VARCHAR(12) |  |  | This field contains the cdf meaning for additional bill codes that were defined on the interface file |
| 24 | `BUILDING_CD` | DOUBLE | NOT NULL |  | Value from 220 that represents the building in the patient location hierarchy. |
| 25 | `CHARGE_DESCRIPTION` | VARCHAR(200) |  |  | This is the charge description from the charge table. |
| 26 | `CHARGE_ITEM_ID` | DOUBLE | NOT NULL | FK→ | This is the value of the unique primary identifier of the charge table. |
| 27 | `CHARGE_TYPE_CD` | DOUBLE | NOT NULL |  | Value from 13028 that represents whether the charge event is a debit, credit, collection, no charge, etc. |
| 28 | `CODE_MODIFIER1_CD` | DOUBLE | NOT NULL |  | This field contains the code modifier from the charge mod table with priority of 1. |
| 29 | `CODE_MODIFIER2_CD` | DOUBLE | NOT NULL |  | This field contains the code modifier on the charge mod table with a priority of 2. |
| 30 | `CODE_MODIFIER3_CD` | DOUBLE | NOT NULL |  | This is the field that contains the code modifier on the charge mod table with priority of 3. |
| 31 | `CODE_MODIFIER_MORE_IND` | DOUBLE |  |  | This field indicates that there are more code modifiers than are listed on the table. |
| 32 | `CODE_REVENUE_CD` | DOUBLE | NOT NULL |  | Stores the revenue code value |
| 33 | `CODE_REVENUE_MORE_IND` | DOUBLE |  |  | indicates that there are additional revenue codes on the charge_mod table |
| 34 | `COST_CENTER_CD` | DOUBLE | NOT NULL |  | This field is the cost center that a charge is associated with |
| 35 | `DEPARTMENT_CD` | DOUBLE | NOT NULL |  | Value from 221 that represents the department in the service resource hierarchy. |
| 36 | `DIAG_CODE1` | VARCHAR(50) |  |  | Diagnosis code from charge_mod with priority 1 with ICD-9 meaning. |
| 37 | `DIAG_CODE2` | VARCHAR(50) |  |  | Diagnosis code from charge_mod with priority 2 with ICD-9 meaning. |
| 38 | `DIAG_CODE3` | VARCHAR(50) |  |  | Diagnosis code from charge_mod with priority 3 with ICD-9 meaning. |
| 39 | `DIAG_DESC1` | VARCHAR(200) |  |  | The description associated with the primary diagnosis code. |
| 40 | `DIAG_DESC2` | VARCHAR(200) |  |  | The description associated with the secondary diagnosis. |
| 41 | `DIAG_DESC3` | VARCHAR(200) |  |  | The description associated with the tertiary diagnosis. |
| 42 | `DIAG_MORE_IND` | DOUBLE |  |  | This field indicates that there are more icd9 diagnosis codes on the charge mod table than there are listed on interface charge. |
| 43 | `DISCOUNT_AMOUNT` | DOUBLE |  |  | The amount of the discount that was applied to the gross price. |
| 44 | `ENCNTR_ID` | DOUBLE | NOT NULL |  | This is the value of the unique primary identifier of the encounter table. It is an internal system assigned number. |
| 45 | `ENCNTR_TYPE_CD` | DOUBLE | NOT NULL |  | Value from 71 that represents the visit type. |
| 46 | `END_EFFECTIVE_DT_TM` | DATETIME |  |  | The date/time after which the row is no longer valid as active current data. This may be valued with the date that the row became inactive. |
| 47 | `EXT_BILL_QTY` | DOUBLE |  |  | Stores the product of multiplying the item_quantity by the QCF value that gets associated to a JCode for Pharmacy charges. |
| 48 | `FACILITY_CD` | DOUBLE | NOT NULL |  | Value from 220 that represents the facility in the patient location hierarchy. |
| 49 | `FIN_NBR` | VARCHAR(50) |  |  | Either the research account ID, institutional financial number or the financial number from encounter table. |
| 50 | `FIN_NBR_TYPE_FLG` | DOUBLE |  |  | Identifies from where the fin nbr came. |
| 51 | `GROSS_PRICE` | DOUBLE |  |  | The price of the procedure before any discounts have been applied. |
| 52 | `ICD9_PROC_MORE_IND` | DOUBLE |  |  | This field indicates that there are more ICD9 procedure codes on the charge mod table that are not listed on the interface charge table. |
| 53 | `INSTITUTION_CD` | DOUBLE | NOT NULL |  | Value from 221 that represents the institution in the service resource hierarchy. |
| 54 | `INTERFACE_CHARGE_ID` | DOUBLE | NOT NULL |  | This is the value of the unique primary identifier of the interface_charge table. It is an internal system assigned number. |
| 55 | `INTERFACE_FILE_ID` | DOUBLE | NOT NULL |  | This is the value of the unique primary identifier of the interface_file table. |
| 56 | `LEVEL5_CD` | DOUBLE | NOT NULL |  | Value from 221 that represents level 5 (exam room, bench, instrument) in the service resource hierarchy. |
| 57 | `MANUAL_IND` | DOUBLE |  |  | Indicates if the charge was once on hold as a manual charge. |
| 58 | `MED_NBR` | VARCHAR(50) |  |  | Medical record number from encounter table. |
| 59 | `MED_SERVICE_CD` | DOUBLE | NOT NULL |  | This is the value from codeset 34 that represents the category of treatment, surgery or general resources. |
| 60 | `NDC_IDENT` | VARCHAR(40) | NOT NULL |  | A value used to uniquely identify drug products. |
| 61 | `NET_EXT_PRICE` | DOUBLE |  |  | Quantity X Price. |
| 62 | `NURSE_UNIT_CD` | DOUBLE | NOT NULL |  | Value from 220 that represents the nurse unit or ambulatory in the patient location hierarchy. |
| 63 | `ORDER_DEPT` | DOUBLE |  |  | not used. |
| 64 | `ORDER_NBR` | VARCHAR(200) |  |  | The order number based on the contributor_system_cd on the interface_file table. |
| 65 | `ORD_DOC_NBR` | VARCHAR(20) |  |  | This contains the doctor number from prsnl_alias table with alias_pool_cd of XXXXX. |
| 66 | `ORD_PHYS_ID` | DOUBLE | NOT NULL |  | This field holds the ID from the person table of the ordering physician. This is the value of the unique primary identifier of the person table. |
| 67 | `ORGANIZATION_ID` | DOUBLE | NOT NULL |  | This is the value of the unique primary identifier of the organization table. |
| 68 | `OVERRIDE_DESC` | VARCHAR(200) |  |  | This field will contain the description of the charge if the manual_ind is 1 on the charge that is being interfaced. |
| 69 | `PAYOR_ID` | DOUBLE | NOT NULL |  | This is the value of the unique primary identifier of the bill_org_payor table. |
| 70 | `PERF_LOC_CD` | DOUBLE | NOT NULL |  | Value from codeset 220 that represents the location at which the services were provided |
| 71 | `PERF_PHYS_ID` | DOUBLE | NOT NULL |  | Unique identifier to the person table of the performing physician. |
| 72 | `PERSON_ID` | DOUBLE | NOT NULL |  | This is the value of the unique primary identifier of the person table. It is an internal system assigned number. |
| 73 | `PERSON_NAME` | VARCHAR(100) |  |  | Person name from person table. |
| 74 | `POSTED_DT_TM` | DATETIME |  |  | The date and time that a custom program pulled the interface charge onto an interface file. |
| 75 | `PRICE` | DOUBLE |  |  | The gross price that was used in calculating the net_ext_price. |
| 76 | `PRIM_CDM` | VARCHAR(50) |  |  | Bill code from charge_mod table with priority 1 with CDM_SCHED as the meaning. |
| 77 | `PRIM_CDM_DESC` | VARCHAR(200) |  |  | Bill code description for the charge description master with priority of 1. |
| 78 | `PRIM_CPT` | VARCHAR(50) |  |  | Bill code from charge_mod table with priority 1 with CPT-4 meaning. |
| 79 | `PRIM_CPT_DESC` | VARCHAR(200) |  |  | Description of the CPT code that has a priority of 1. |
| 80 | `PRIM_ICD9_PROC` | VARCHAR(50) |  |  | Bill code from charge_mod table with priority 1 with PROCCODE meaning. |
| 81 | `PRIM_ICD9_PROC_DESC` | VARCHAR(200) |  |  | Description of the Primary ICD9 Procedure Code |
| 82 | `PROCESS_FLG` | DOUBLE |  |  | Shows the status of the interface charge. This flag will be used to determine if the interface charge qualifies for the interface file. |
| 83 | `QTY_CONV_FACTOR` | DOUBLE |  |  | Stores the multiplier value that gets associated with a JCode used for Pharmacy charges. |
| 84 | `QUANTITY` | DOUBLE |  |  | The number by which the price has been extended, which indicates a quantity of products or services. |
| 85 | `REFERRING_PHYS_ID` | DOUBLE | NOT NULL |  | This field holds the ID from the person table of the referring physician. This is the value of the unique primary identifier of the person table. |
| 86 | `ROOM_CD` | DOUBLE | NOT NULL |  | Value from 220 that represents the room in the patient location hierarchy. |
| 87 | `SECTION_CD` | DOUBLE | NOT NULL |  | Value from 221 that represents the section in the service resource hierarchy. |
| 88 | `SERVICE_DT_TM` | DATETIME |  |  | Service date and time. |
| 89 | `SUBSECTION_CD` | DOUBLE | NOT NULL |  | Value from 221 that represents the subsection in the service resource hierarchy. |
| 90 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 91 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 92 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 93 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 94 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |
| 95 | `USER_DEF_IND` | DOUBLE |  |  | This field stores an indicator that tells whether there are user-defined charge mods. |
| 96 | `VERIFY_PHYS_ID` | DOUBLE | NOT NULL |  | This field holds the prsnl_id for the physician on the verified or complete event. This is the value of the unique primary identifier of the person table |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `CHARGE_ITEM_ID` | [CHARGE](CHARGE.md) | `CHARGE_ITEM_ID` |

