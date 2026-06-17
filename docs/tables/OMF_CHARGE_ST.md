# OMF_CHARGE_ST

> OMF_CHARGE_ST

**Description:** Stores charge information related to a particular encounter  
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
| 5 | `ACT_INDIRECT_FIX_COST` | DOUBLE |  |  | The actual indirect fixed cost. |
| 6 | `ACT_INDIRECT_VAR_COST` | DOUBLE |  |  | The actual indirect variable cost |
| 7 | `ACT_SERVICE_TO_CHARGE` | DOUBLE |  |  | act_service_to_charge. Used to calculate Service to Charge turnaround times |
| 8 | `ADMIT_TYPE_CD` | DOUBLE | NOT NULL |  | Stores the unique admission type for each patient |
| 9 | `BILL_CODE_ID` | DOUBLE | NOT NULL |  | Depending on the value in charge_mod_type_cd, this is either the value from 13030 that represents the suspense reason, or it is the value from 14002 that represents the bill code schedule. |
| 10 | `BILL_ITEM_ID` | DOUBLE | NOT NULL |  | The unique identifier for a bill item |
| 11 | `CATALOG_CD` | DOUBLE | NOT NULL |  | The coded value for the order catalog for this order. |
| 12 | `CDM_DESC` | VARCHAR(200) |  |  | The charge description master description. |
| 13 | `CDM_NBR` | VARCHAR(200) |  |  | The charge description master number. |
| 14 | `CHARGE_DESCRIPTION` | VARCHAR(200) |  |  | The free text description for the charge. |
| 15 | `CHARGE_DT_NBR` | DOUBLE |  |  | The Cerner internal system date representation of the day the person was charged |
| 16 | `CHARGE_DT_TM` | DATETIME |  |  | The date/time charge occurred |
| 17 | `CHARGE_ITEM_ID` | DOUBLE | NOT NULL |  | Charge Item ID uniquely identifies the charge. It is a foreign key to the Charge Table |
| 18 | `CHARGE_MIN_NBR` | DOUBLE |  |  | The minute of day the charge occurred (1..1440). |
| 19 | `CHARGE_TYPE_CD` | DOUBLE | NOT NULL |  | Represents the charge event: debit, credit, collection, no charge, etc. |
| 20 | `CHARGE_TZ` | DOUBLE |  |  | Time zone associated with the corresponding DT_TM column. |
| 21 | `COST_CENTER_CD` | DOUBLE | NOT NULL |  | Cost center code value |
| 22 | `COST_CENTER_GRP_CD` | DOUBLE | NOT NULL |  | The grouping of cost center cds (14058) |
| 23 | `CPT4_DESC` | VARCHAR(200) |  |  | The CPT4 description as it applies to the charge. |
| 24 | `CPT4_ID` | DOUBLE | NOT NULL |  | cpt4_id |
| 25 | `CPT4_NBR` | VARCHAR(200) |  |  | The CPT4 number as it applies to the charge |
| 26 | `DEPARTMENT_CD` | DOUBLE | NOT NULL |  | Performing Department Code |
| 27 | `DISCOUNT_AMOUNT` | DOUBLE |  |  | Discount Amount |
| 28 | `ENCNTR_ID` | DOUBLE | NOT NULL | FK→ | This is the value of the unique primary identifier of the encounter table. It is an internal system assigned number. |
| 29 | `ICD9_DESC` | VARCHAR(200) |  |  | The ICD9 description as it applies to the charge. |
| 30 | `ICD9_ID` | DOUBLE | NOT NULL |  | icd9_id |
| 31 | `ICD9_NBR` | VARCHAR(200) |  |  | The ICD9 number as it applies to the charge. |
| 32 | `INSTITUTION_CD` | DOUBLE | NOT NULL |  | Performing Institution |
| 33 | `INTERFACED_DT_NBR` | DOUBLE |  |  | The Cerner internal system date representation of the day the charge interfaced |
| 34 | `INTERFACED_DT_TM` | DATETIME |  |  | The date/time that the charge was interfaced |
| 35 | `INTERFACED_MIN_NBR` | DOUBLE |  |  | The minute of day (1..1440). |
| 36 | `INTERFACED_TZ` | DOUBLE |  |  | Time zone associated with the corresponding DT_TM column. |
| 37 | `ITEM_EXTENDED_PRICE` | DOUBLE |  |  | item_extended_price |
| 38 | `ITEM_PRICE` | DOUBLE |  |  | The charge item price |
| 39 | `ITEM_QUANTITY` | DOUBLE |  |  | The number of charges |
| 40 | `LOC_FACILITY_CD` | DOUBLE | NOT NULL |  | Ordering institution |
| 41 | `LOC_NURSE_UNIT_CD` | DOUBLE | NOT NULL |  | The code_value that refers to the patient's nurse unit. |
| 42 | `MANUAL_IND` | DOUBLE |  |  | Indicates if this charge is currently on hold as a manual charge or if it has ever been on hold as a manual charge. |
| 43 | `NOMENCLATURE_ID` | DOUBLE | NOT NULL |  | Bill Code corresponding to the nomenclature Id |
| 44 | `ORDER_DT_NBR` | DOUBLE |  |  | The Cerner internal system date representation of the day the charge was ordered |
| 45 | `ORDER_DT_TM` | DATETIME |  |  | The date/time that the charge was ordered |
| 46 | `ORDER_ID` | DOUBLE | NOT NULL |  | Id of the order |
| 47 | `ORDER_MIN_NBR` | DOUBLE |  |  | The minute of day (1..1440). |
| 48 | `ORDER_PHYS_GRP_CD` | DOUBLE | NOT NULL |  | Grouping of ordering physicians |
| 49 | `ORDER_PHYS_ID` | DOUBLE | NOT NULL |  | The id of the ordering provider |
| 50 | `ORDER_TZ` | DOUBLE |  |  | Time zone associated with the corresponding DT_TM column. |
| 51 | `PAYOR_ID` | DOUBLE | NOT NULL |  | ID from the organization table that represents the client organization associated with this charge. |
| 52 | `PERF_PHYS_GRP_CD` | DOUBLE | NOT NULL |  | Grouping of performing physicians |
| 53 | `PERF_PHYS_ID` | DOUBLE | NOT NULL |  | The performing physician person ID |
| 54 | `PERSON_ID` | DOUBLE | NOT NULL | FK→ | This is the value of the unique primary identifier of the person table. It is an internal system assigned number. |
| 55 | `PROCESS_FLAG` | DOUBLE |  |  | Indicates how to process data in batch mode. |
| 56 | `PROCESS_FLG` | DOUBLE |  |  | Indicates if the charge is pending, suspended/held, skipped, interfaced, combined or bundled. |
| 57 | `REV_CAT_CD` | DOUBLE | NOT NULL |  | The grouping of revenue codes (20769) |
| 58 | `REV_CAT_GRP_CD` | DOUBLE | NOT NULL |  | The grouping of revenue categories (25993) |
| 59 | `REV_CODE_CD` | DOUBLE | NOT NULL |  | The revenue codes assigned to the CDM |
| 60 | `SECTION_CD` | DOUBLE | NOT NULL |  | The performing section code |
| 61 | `SERVICE_DT_NBR` | DOUBLE |  |  | The date number when the service took place. Used to gather date information from the omf_date table |
| 62 | `SERVICE_DT_TM` | DATETIME |  |  | The date and time when the service took place |
| 63 | `SERVICE_MIN_NBR` | DOUBLE |  |  | The minute number when the service took place. Used to get time information from the omf_time table. |
| 64 | `SERVICE_TZ` | DOUBLE |  |  | Time zone associated with the corresponding DT_TM column. |
| 65 | `STD_DIRECT_FIX_COST` | DOUBLE |  |  | The standard direct fixed cost. |
| 66 | `STD_DIRECT_VAR_COST` | DOUBLE |  |  | The standard direct variable cost. |
| 67 | `STD_INDIRECT_FIX_COST` | DOUBLE |  |  | The standard indirect fixed cost |
| 68 | `STD_INDIRECT_VAR_COST` | DOUBLE |  |  | The standard indirect variable cost. |
| 69 | `SUBSECTION_CD` | DOUBLE | NOT NULL |  | The performing subsection code |
| 70 | `TASK_ASSAY_CD` | DOUBLE | NOT NULL |  | Foreign key to discrete_task_assay |
| 71 | `TIER_GROUP_CD` | DOUBLE | NOT NULL |  | The charge tier group code used to identity charges |
| 72 | `TOTAL_ACT_COST` | DOUBLE |  |  | The total actual cost. |
| 73 | `TOTAL_STD_COST` | DOUBLE |  |  | The total standard cost |
| 74 | `TRANSACTION_IND` | DOUBLE |  |  | Number of transactions |
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

