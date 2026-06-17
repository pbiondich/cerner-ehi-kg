# OMF_POSTED_CHARGE_ST

> Stores charge data that has already been posted either by a foreign system or by ProFit.

**Description:** Stores charge data that has already been posted.  
**Table type:** ACTIVITY  
**Primary key:** _(not published — see note)_  
**Columns:** 79

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ACCESSION` | VARCHAR(20) |  |  | An accession uniquely identifies a specimen. |
| 2 | `ACTIVITY_TYPE_CD` | DOUBLE | NOT NULL |  | Department to which the activity belongs |
| 3 | `ACT_DIRECT_FIX_COST` | DOUBLE |  |  | The actual direct fixed cost. |
| 4 | `ACT_DIRECT_VAR_COST` | DOUBLE |  |  | The actual direct variable cost. |
| 5 | `ACT_INDIRECT_FIX_COST` | DOUBLE |  |  | The actual indirect fixed cost |
| 6 | `ACT_INDIRECT_VAR_COST` | DOUBLE |  |  | The actual indirect variable cost. |
| 7 | `ACT_SERVICE_TO_CHARGE` | DOUBLE |  |  | The actual turnaround time from the service date/time to the charge date/time (in minutes). |
| 8 | `ADMIT_TYPE_CD` | DOUBLE | NOT NULL |  | Stores the unique admission type for each patient |
| 9 | `BILL_CODE_ID` | DOUBLE | NOT NULL |  | Depending on the value in charge_mod_type_cd, this is either the value from 13030 that represents the suspense reason, or it is the value from 14002 that represents the bill code schedule. |
| 10 | `BILL_ITEM_ID` | DOUBLE | NOT NULL |  | The unique identifier for a bill item. |
| 11 | `CATALOG_CD` | DOUBLE | NOT NULL |  | The coded value for the order catalog for this order. |
| 12 | `CDM_DESC` | VARCHAR(200) |  |  | The charge description master description. |
| 13 | `CDM_NBR` | VARCHAR(200) |  |  | The charge description master number. |
| 14 | `CHARGE_DESCRIPTION` | VARCHAR(200) |  |  | The free text description for the charge. |
| 15 | `CHARGE_DT_NBR` | DOUBLE |  |  | The Julian date on which the charge occurred. |
| 16 | `CHARGE_DT_TM` | DATETIME |  |  | The date/time on which the charge occurred. |
| 17 | `CHARGE_ITEM_ID` | DOUBLE | NOT NULL |  | Charge Item ID uniquely identifies the charge. It is a foreign key to the Charge Table |
| 18 | `CHARGE_MIN_NBR` | DOUBLE |  |  | The minute of the day on which the charge occurred. |
| 19 | `CHARGE_TYPE_CD` | DOUBLE | NOT NULL |  | Represents the charge event: debit, credit, collection, no charge, etc. |
| 20 | `CHARGE_TZ` | DOUBLE |  |  | Time zone associated with the corresponding DT_TM column. |
| 21 | `COST_CENTER_CD` | DOUBLE | NOT NULL |  | The cost center within which the charge occurred. |
| 22 | `COST_CENTER_GRP_CD` | DOUBLE | NOT NULL |  | Grouping of cost centers (14058) |
| 23 | `CPT4_DESC` | VARCHAR(200) |  |  | The CPT4 description as it applies to the charge. |
| 24 | `CPT4_ID` | DOUBLE | NOT NULL |  | The nomenclature id for the CPT4 code |
| 25 | `CPT4_NBR` | VARCHAR(200) |  |  | The CPT4 number as it applies to the charge |
| 26 | `DEPARTMENT_CD` | DOUBLE | NOT NULL |  | The code value for the performing department. |
| 27 | `DISCOUNT_AMOUNT` | DOUBLE |  |  | The discount amount applied to the charge. |
| 28 | `ENCNTR_ID` | DOUBLE | NOT NULL | FK→ | This is the value of the unique primary identifier of the encounter table. It is an internal system assigned number. |
| 29 | `ICD9_DESC` | VARCHAR(200) |  |  | The ICD9 description as it applies to the charge. |
| 30 | `ICD9_ID` | DOUBLE | NOT NULL |  | The nomenclature id for the icd9 code. |
| 31 | `ICD9_NBR` | VARCHAR(200) |  |  | The ICD9 number as it applies to the charge. |
| 32 | `INSTITUTION_CD` | DOUBLE | NOT NULL |  | The code value for the performing institution. |
| 33 | `INTERFACED_DT_NBR` | DOUBLE |  |  | The Julian date for the interfaced date/time. |
| 34 | `INTERFACED_DT_TM` | DATETIME |  |  | The interfaced date/time. |
| 35 | `INTERFACED_MIN_NBR` | DOUBLE |  |  | The minute of day at which the charge was interfaced. |
| 36 | `INTERFACE_TZ` | DOUBLE |  |  | Time zone associated with the corresponding DT_TM column. |
| 37 | `ITEM_EXTENDED_PRICE` | DOUBLE |  |  | The extended price for the charge item. |
| 38 | `ITEM_PRICE` | DOUBLE |  |  | The price for the charge item. |
| 39 | `ITEM_QUANTITY` | DOUBLE |  |  | The charge quantity. |
| 40 | `LOC_FACILITY_CD` | DOUBLE | NOT NULL |  | The code value for the patient facility. |
| 41 | `LOC_NURSE_UNIT_CD` | DOUBLE | NOT NULL |  | The code value for the patient nurse unit. |
| 42 | `MANUAL_IND` | DOUBLE |  |  | Indicates if this charge is currently on hold as a manual charge or if it has ever been on hold as a manual charge. |
| 43 | `NOMENCLATURE_ID` | DOUBLE | NOT NULL |  | The unique identifier for the charge nomenclature. |
| 44 | `ORDER_DT_NBR` | DOUBLE |  |  | The Julian date number for the date on which the order occurred. |
| 45 | `ORDER_DT_TM` | DATETIME |  |  | The date/time on which the order occurred. |
| 46 | `ORDER_ID` | DOUBLE | NOT NULL |  | The unique identifier for the order. |
| 47 | `ORDER_MIN_NBR` | DOUBLE |  |  | The minute of day on which the order occurred. |
| 48 | `ORDER_PHYS_GRP_CD` | DOUBLE | NOT NULL |  | The code value representing the order physician group. |
| 49 | `ORDER_PHYS_ID` | DOUBLE | NOT NULL |  | The unique identifier for the ordering physician. |
| 50 | `ORDER_TZ` | DOUBLE |  |  | Time zone associated with the corresponding DT_TM column. |
| 51 | `PAYOR_ID` | DOUBLE | NOT NULL |  | The unique identifier for the organization that is the payor. |
| 52 | `PERF_PHYS_GRP_CD` | DOUBLE | NOT NULL |  | The code value representing the performing physician group. |
| 53 | `PERF_PHYS_ID` | DOUBLE | NOT NULL |  | The unique identifier for the performing physician |
| 54 | `PERSON_ID` | DOUBLE | NOT NULL | FK→ | This is the value of the unique primary identifier of the person table. It is an internal system assigned number. |
| 55 | `PROCESS_FLAG` | DOUBLE |  |  | Indicates how to process data in batch mode. |
| 56 | `PROCESS_FLG` | DOUBLE |  |  | Indicates if the charge is pending, suspended/held, skipped, interfaced, combined or bundled. |
| 57 | `REV_CAT_CD` | DOUBLE | NOT NULL |  | The grouping of revenue codes (20769) |
| 58 | `REV_CAT_GRP_CD` | DOUBLE | NOT NULL |  | Grouping of revenue categories (25993) |
| 59 | `REV_CODE_CD` | DOUBLE | NOT NULL |  | Revenue code assigned to the CDM |
| 60 | `SECTION_CD` | DOUBLE | NOT NULL |  | The code value representing the performing section. |
| 61 | `SERVICE_DT_NBR` | DOUBLE |  |  | The Julian date on which the service for the charge was performed. |
| 62 | `SERVICE_DT_TM` | DATETIME |  |  | The date/time on which the service for the charge was performed. |
| 63 | `SERVICE_MIN_NBR` | DOUBLE |  |  | The minute of day on which the service for the charge was performed. |
| 64 | `SERVICE_TZ` | DOUBLE |  |  | Time zone associated with the corresponding DT_TM column. |
| 65 | `STD_DIRECT_FIX_COST` | DOUBLE |  |  | The standard direct fixed cost. |
| 66 | `STD_DIRECT_VAR_COST` | DOUBLE |  |  | The standard direct variable cost. |
| 67 | `STD_INDIRECT_FIX_COST` | DOUBLE |  |  | The standard indirect fixed cost. |
| 68 | `STD_INDIRECT_VAR_COST` | DOUBLE |  |  | The standard indirect variable cost. |
| 69 | `SUBSECTION_CD` | DOUBLE | NOT NULL |  | The code value representing the subsection at which the service was performed. |
| 70 | `TASK_ASSAY_CD` | DOUBLE | NOT NULL |  | The code value representing the task assay that was performed. |
| 71 | `TIER_GROUP_CD` | DOUBLE | NOT NULL |  | The charge tier group code used to identity charges |
| 72 | `TOTAL_ACT_COST` | DOUBLE |  |  | The total actual cost. |
| 73 | `TOTAL_STD_COST` | DOUBLE |  |  | The total standard cost |
| 74 | `TRANSACTION_IND` | DOUBLE |  |  | The number of transactions. |
| 75 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 76 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 77 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 78 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 79 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `ENCNTR_ID` | [ENCOUNTER](ENCOUNTER.md) | `ENCNTR_ID` |
| `PERSON_ID` | [PERSON](PERSON.md) | `PERSON_ID` |

