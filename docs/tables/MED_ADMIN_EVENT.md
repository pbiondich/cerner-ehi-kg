# MED_ADMIN_EVENT

> Medication Administration Event Table

**Description:** Medication Administration Event  
**Table type:** ACTIVITY  
**Primary key:** `MED_ADMIN_EVENT_ID`  
**Columns:** 30  
**Referenced by:** 1 columns

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `BEG_DT_TM` | DATETIME |  |  | The beginning date/time of the range of medication admin events. |
| 2 | `CAREAWARE_USED_IND` | DOUBLE | NOT NULL |  | Maintains whether CareAware was used to obtain drug related information. |
| 3 | `CLINICAL_WARNING_CNT` | DOUBLE | NOT NULL |  | The number of clinical warnings presented for this medication admin event. |
| 4 | `CRITICAL_DRUG_IND` | DOUBLE | NOT NULL |  | Indicates that the alert occurred upon a medication that was critically defined. |
| 5 | `DOCUMENTATION_ACTION_SEQUENCE` | DOUBLE | NOT NULL |  | The action sequence of the order that the medication admin event is associated to. |
| 6 | `END_DT_TM` | DATETIME |  |  | The end date/time of the range of medication admin events. |
| 7 | `EVENT_CNT` | DOUBLE | NOT NULL |  | The number of medication admin events in the range of beginning and end date/time. |
| 8 | `EVENT_ID` | DOUBLE | NOT NULL |  | The ID of the clinical event associated to this medication admin event. |
| 9 | `EVENT_TYPE_CD` | DOUBLE | NOT NULL |  | Identifies what type of event was audited. Values can be code_value for TASKPURGED, TASKCOMPLETE, NOTDONE, or NOTGIVEN from code_set 4000040. |
| 10 | `MED_ADMIN_EVENT_ID` | DOUBLE | NOT NULL | PK | The ID of the medication administration event. |
| 11 | `NEEDS_VERIFY_FLAG` | DOUBLE | NOT NULL |  | Indicator on whether this order is verified. 0 No Verify Needed 1 Verify 40 Needed 2 Superseded 3 Verified 4 Rejected 5 Reviewed |
| 12 | `NURSE_UNIT_CD` | DOUBLE | NOT NULL |  | The nurse unit of the device the user is using to enter the medication admin event. |
| 13 | `ORDER_ID` | DOUBLE | NOT NULL | FK→ | The ID of the order associated to this med admin event. |
| 14 | `ORDER_RESULT_VARIANCE_IND` | DOUBLE | NOT NULL |  | Indicates if the documented result details do not match the order details. |
| 15 | `POSITION_CD` | DOUBLE | NOT NULL |  | The position of the user documenting the medication admin event. |
| 16 | `POSITIVE_MED_IDENT_IND` | DOUBLE | NOT NULL |  | Indicates if the medication was positively identified for this medication admin event. |
| 17 | `POSITIVE_PATIENT_IDENT_IND` | DOUBLE | NOT NULL |  | Indicates if the patient was positively identified for this medication admin event. |
| 18 | `PRSNL_ID` | DOUBLE | NOT NULL | FK→ | The ID of the user documenting the medication admin event. |
| 19 | `SCHEDULED_DT_TM` | DATETIME |  |  | The date and time the task was scheduled to be given. |
| 20 | `SCHEDULED_TZ` | DOUBLE |  |  | Time zone associated with the corresponding DT_TM column. |
| 21 | `SOURCE_APPLICATION_FLAG` | DOUBLE |  |  | Identification for source application used to chart med event.0 |
| 22 | `TEMPLATE_ORDER_ID` | DOUBLE | NOT NULL |  | Order id for the template order. |
| 23 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 24 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 25 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 26 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 27 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |
| 28 | `VERIFICATION_DT_TM` | DATETIME |  |  | The date and time verification of the order took place. |
| 29 | `VERIFICATION_TZ` | DOUBLE |  |  | Time zone associated with the corresponding DT_TM column. |
| 30 | `VERIFIED_PRSNL_ID` | DOUBLE | NOT NULL |  | The personnel that verified the order. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `ORDER_ID` | [ORDERS](ORDERS.md) | `ORDER_ID` |
| `PRSNL_ID` | [PRSNL](PRSNL.md) | `PERSON_ID` |

## Referenced by (1)

| From table | Column |
|------------|--------|
| [MED_ADMIN_ALERT](MED_ADMIN_ALERT.md) | `MED_ADMIN_EVENT_ID` |

