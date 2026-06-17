# OMF_ORDER_ST

> omf_order_st

**Description:** Stores order information related to a particular encounter  
**Table type:** ACTIVITY  
**Primary key:** _(not published — see note)_  
**Columns:** 64

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ACTION_PERSONNEL_ID` | DOUBLE | NOT NULL |  | The unique identifier for the person that placed the order.. |
| 2 | `ACTION_PRSNL_POSITION_CD` | DOUBLE | NOT NULL |  | The Cerner-defined position for the prsnl placing the order. |
| 3 | `ACTIVITY_TYPE_CD` | DOUBLE | NOT NULL |  | A grouping mechanism within catalog type code. |
| 4 | `CANCEL_DT_NBR` | DOUBLE |  |  | The Julian date on which the order was cancelled. |
| 5 | `CANCEL_DT_TM` | DATETIME |  |  | The date/time on which the order was cancelled. |
| 6 | `CANCEL_IND` | DOUBLE |  |  | Indicates whether or not the order has been cancelled. |
| 7 | `CANCEL_MIN_NBR` | DOUBLE |  |  | The minute of the day on which the order was cancelled. |
| 8 | `CANCEL_REASON_CD` | DOUBLE | NOT NULL |  | The reason that an order was cancelled. |
| 9 | `CANCEL_TZ` | DOUBLE |  |  | Time zone associated with the corresponding DT_TM column. |
| 10 | `CATALOG_CD` | DOUBLE | NOT NULL |  | The coded value for the order catalog for this order. |
| 11 | `CATALOG_TYPE_CD` | DOUBLE | NOT NULL |  | A grouping mechanism to bring order catalogs together. |
| 12 | `CKI` | VARCHAR(255) |  |  | For Meds processes |
| 13 | `COMPLETE_DT_NBR` | DOUBLE |  |  | The Julian date on which the order was completed. |
| 14 | `COMPLETE_DT_TM` | DATETIME |  |  | The date/time on which the order was completed. |
| 15 | `COMPLETE_IND` | DOUBLE |  |  | Indicates whether or not the order has been completed. |
| 16 | `COMPLETE_MIN_NBR` | DOUBLE |  |  | The minute of the day on which the order was completed. |
| 17 | `COMPLETE_TZ` | DOUBLE |  |  | Time zone associated with the corresponding DT_TM column. |
| 18 | `CPT4_PROC_NOMENCLATURE_ID` | DOUBLE | NOT NULL |  | The nomenclature id for the CPT4 procedure attached to the order. |
| 19 | `CURRENT_START_DT_NBR` | DOUBLE |  |  | The Julian date on which the order was started. |
| 20 | `CURRENT_START_DT_TM` | DATETIME |  |  | The date/time on which the order was started. |
| 21 | `CURRENT_START_MIN_NBR` | DOUBLE |  |  | The minute of the day on which the order was started. |
| 22 | `CURRENT_START_TZ` | DOUBLE |  |  | Time zone associated with the corresponding DT_TM column. |
| 23 | `DISCONTINUE_DT_NBR` | DOUBLE |  |  | The Julian date on which the order was discontinued. |
| 24 | `DISCONTINUE_DT_TM` | DATETIME |  |  | The date/time on which the order was discontinued. |
| 25 | `DISCONTINUE_MIN_NBR` | DOUBLE |  |  | The minute of the day on which the order was discontinued. |
| 26 | `DISCONTINUE_REASON_CD` | DOUBLE | NOT NULL |  | The reason that an order was discontinued. |
| 27 | `DISCONTINUE_TZ` | DOUBLE |  |  | Time zone associated with the corresponding DT_TM column. |
| 28 | `ENCNTR_ID` | DOUBLE | NOT NULL | FK→ | This is the value of the unique primary identifier of the encounter table. It is an internal system assigned number. |
| 29 | `ICD9_DIAG_NOMENCLATURE_ID` | DOUBLE | NOT NULL |  | The nomenclature id for the diagnosis code attached to the order. |
| 30 | `ICD9_PRIN_PROC_DT_NBR` | DOUBLE |  |  | The Julian date for the principle procedure |
| 31 | `ICD9_PRIN_PROC_DT_TM` | DATETIME |  |  | The date/time on which the ICD9 Principal Procedure was performed. |
| 32 | `ICD9_PRIN_PROC_MIN_NBR` | DOUBLE |  |  | The minute number for the icd9 principal procedure |
| 33 | `ICD9_PRIN_PROC_TZ` | DOUBLE |  |  | Time zone associated with the corresponding DT_TM column. |
| 34 | `ICD9_PROC_NOMENCLATURE_ID` | DOUBLE | NOT NULL |  | The nomenclature id for the procedure attached to the orderable. |
| 35 | `NEED_DOCTOR_COSIGN_IND` | DOUBLE |  |  | Indicates whether or not the order requires a doctor cosign. |
| 36 | `ORDER_FACILITY_CD` | DOUBLE | NOT NULL |  | The coded value for the facility in which the patient was located at order time. |
| 37 | `ORDER_FACILITY_GRP_CD` | DOUBLE | NOT NULL |  | The grouping code for the order_facility |
| 38 | `ORDER_ID` | DOUBLE | NOT NULL |  | The unique identifier for the order. |
| 39 | `ORDER_IND` | DOUBLE |  |  | Indicates whether or not the order has been placed. |
| 40 | `ORDER_NURSE_UNIT_CD` | DOUBLE | NOT NULL |  | The nurse unit code at which the patient was located at order time. |
| 41 | `ORDER_NURSE_UNIT_GRP_CD` | DOUBLE | NOT NULL |  | The grouping code for the nurse unit. |
| 42 | `ORDER_PROVIDER_ID` | DOUBLE | NOT NULL |  | The unique identifier for the ordering physician |
| 43 | `ORDER_PROVIDER_POSITION_CD` | DOUBLE | NOT NULL |  | The Cerner-defined position for the ordering physician. |
| 44 | `ORIG_ORDER_DT_NBR` | DOUBLE |  |  | The Julian date on which the order took place. |
| 45 | `ORIG_ORDER_DT_TM` | DATETIME |  |  | The date/time on which the order took place. |
| 46 | `ORIG_ORDER_MIN_NBR` | DOUBLE |  |  | The minute of the day on which the order took place. |
| 47 | `ORIG_ORDER_TZ` | DOUBLE |  |  | Time zone associated with the corresponding DT_TM column. |
| 48 | `PERSON_ID` | DOUBLE | NOT NULL | FK→ | This is the value of the unique primary identifier of the person table. It is an internal system assigned number. |
| 49 | `PRIORITY_CD` | DOUBLE | NOT NULL |  | The priority of the order. |
| 50 | `REVIEW_COMPLETE_IND` | DOUBLE |  |  | Indicates whether or not the review has been completed. |
| 51 | `REVIEW_REQUIRED_IND` | DOUBLE |  |  | Indicates whether or not a review is required. |
| 52 | `STATUS_DT_NBR` | DOUBLE |  |  | The Julian date for the last time the order was modified. |
| 53 | `STATUS_DT_TM` | DATETIME |  |  | The date/time on which the order was last modified. |
| 54 | `STATUS_MIN_NBR` | DOUBLE |  |  | The minute of the day on which the order was last modified. |
| 55 | `STATUS_TZ` | DOUBLE |  |  | Time zone associated with the corresponding DT_TM column. |
| 56 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 57 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 58 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 59 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 60 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |
| 61 | `VISIT_DT_NBR` | DOUBLE |  |  | The Julian date for the admit date/time. |
| 62 | `VISIT_DT_TM` | DATETIME |  |  | The date/time on which the encounter visit occurred. |
| 63 | `VISIT_MIN_NBR` | DOUBLE |  |  | The minute number for the admit date/time. |
| 64 | `VISIT_TZ` | DOUBLE |  |  | Time zone associated with the corresponding DT_TM column. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `ENCNTR_ID` | [ENCOUNTER](ENCOUNTER.md) | `ENCNTR_ID` |
| `PERSON_ID` | [PERSON](PERSON.md) | `PERSON_ID` |

