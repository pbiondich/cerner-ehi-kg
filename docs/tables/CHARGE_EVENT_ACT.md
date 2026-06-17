# CHARGE_EVENT_ACT

> Information regarding who triggered a charge, where the charge was created, and when a charge event took place.

**Description:** Charge Event Activity  
**Table type:** ACTIVITY  
**Primary key:** `CHARGE_EVENT_ACT_ID`  
**Columns:** 52  
**Referenced by:** 2 columns

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ACCESSION_ID` | DOUBLE | NOT NULL | FK→ | The unique identifier to the accession table. |
| 2 | `ACTIVE_IND` | DOUBLE |  |  | The table row is active or inactive. A row is generally active unless it is in an inactive state such as logically deleted, combined away, pending purge, etc. |
| 3 | `ACTIVITY_DT_TM` | DATETIME |  |  | The date and time that the actual event occurred. For example, the activity date and time on the ordered event would be the date and time that the item was actually ordered. |
| 4 | `ALPHA_NOMEN_ID` | DOUBLE | NOT NULL | FK→ | This is the value of the unique primary identifier of the nomenclature table. This is used in alpha response pricing logic. |
| 5 | `CEA_MISC1` | VARCHAR(200) |  |  | String field that holds miscellaneous information about the charge event. |
| 6 | `CEA_MISC1_ID` | DOUBLE | NOT NULL |  | Numeric field to hold miscellaneous information about the charge event. |
| 7 | `CEA_MISC2` | VARCHAR(200) |  |  | String field that holds miscellaneous information about the charge event. |
| 8 | `CEA_MISC2_ID` | DOUBLE | NOT NULL |  | Numeric field to hold miscellaneous information about the charge event. |
| 9 | `CEA_MISC3` | VARCHAR(200) |  |  | String field that holds miscellaneous information about the charge event. |
| 10 | `CEA_MISC3_ID` | DOUBLE | NOT NULL |  | Numeric field to hold miscellaneous information about the charge event. |
| 11 | `CEA_MISC4_ID` | DOUBLE | NOT NULL |  | Numeric field to hold miscellaneous information about the charge event. |
| 12 | `CEA_MISC5_ID` | DOUBLE | NOT NULL |  | Numeric value that holds the item_copay passed in from pharmacy and will be written to the item_copay field on the charge table. For pharmacy charges only. |
| 13 | `CEA_MISC6_ID` | DOUBLE | NOT NULL |  | Numeric value that holds the item_reimbursement passed in from pharmacy and will be written to the item_reimbursement field on the charge table. For pharmacy charges only. |
| 14 | `CEA_MISC7_ID` | DOUBLE | NOT NULL |  | Numeric value that holds the discount_amount passed in from pharmacy and will be written to the discount_amount field on the charge table. For pharmacy charges only. |
| 15 | `CEA_PRSNL_ID` | DOUBLE | NOT NULL | FK→ | ID from the prsnl table of the person associated with the event activity. |
| 16 | `CEA_TYPE_CD` | DOUBLE | NOT NULL |  | Value from 13039 that represents the event such as performed, verified, complete. |
| 17 | `CHARGE_DT_TM` | DATETIME |  |  | The date and time the charge was created. |
| 18 | `CHARGE_EVENT_ACT_ID` | DOUBLE | NOT NULL | PK | This is the value of the unique primary identifier of the charge_event_act table. It is an internal system assigned number. |
| 19 | `CHARGE_EVENT_ID` | DOUBLE | NOT NULL | FK→ | ID of the charge event to which this activity is associated. This is the unique primary identifier of the charge_event table. |
| 20 | `CHARGE_TYPE_CD` | DOUBLE | NOT NULL |  | Value from 13028 that represents whether the charge event is a debit, credit, collection, no charge, etc. |
| 21 | `DISCOUNT_AMOUNT` | DOUBLE | NOT NULL |  | Stores the discount amount |
| 22 | `INSERT_DT_TM` | DATETIME |  |  | The date and time the row was originally inserted. |
| 23 | `IN_LAB_DT_TM` | DATETIME |  |  | The date and time the specimen reached the "INLAB" status. This is derived by comparing the receiving location to the login location; when they are the same the specimen is considered "INLAB". |
| 24 | `ITEM_COPAY` | DOUBLE | NOT NULL |  | Stores the copay amount |
| 25 | `ITEM_DEDUCTIBLE_AMT` | DOUBLE |  |  | Contains the deductible amount for the item. |
| 26 | `ITEM_EXT_PRICE` | DOUBLE | NOT NULL |  | Stores the price multiplied by the quantity for a charge when the price is sent in the request (i.e. miscellaneous bill items) |
| 27 | `ITEM_PRICE` | DOUBLE | NOT NULL |  | Stores the price for a charge when the price is sent in the request (i.e. miscellaneous bill items) |
| 28 | `ITEM_REIMBURSEMENT` | DOUBLE | NOT NULL |  | Store the item reimbursement |
| 29 | `MISC_IND` | DOUBLE |  |  | This field, when sent in the server request, indicates a miscellaneous item. For CSBatchChargeEntry, this means the user is prompted for the description, price and quantity. For Pharmacy, it means to use the description sent instead of the description on the bill item. |
| 30 | `PATIENT_LOC_CD` | DOUBLE | NOT NULL |  | Value from 220 that represents the location to which the patient presented. |
| 31 | `PATIENT_RESPONSIBILITY_FLAG` | DOUBLE | NOT NULL |  | Flag to determine the responsibility of the patient. 0 - Unknown; 1 - Patient Responsible; 2 - Patient Not Responsible |
| 32 | `PRIORITY_CD` | DOUBLE | NOT NULL |  | This is the priority code passed to the charge server and used to evaluate the tier. Code set 1304. |
| 33 | `QUANTITY` | DOUBLE | NOT NULL |  | The number of items that should be used to extend the price. |
| 34 | `REASON_CD` | DOUBLE | NOT NULL |  | not used. |
| 35 | `REFERENCE_RANGE_FACTOR_ID` | DOUBLE | NOT NULL | FK→ | This is the value of the unique primary identifier of the reference_range_factor table. This is used in alpha response pricing logic. |
| 36 | `REPEAT_IND` | DOUBLE |  |  | Indicates if this event is a repeat workload event activity. This occurs when a test is performed more than once. |
| 37 | `RESULT` | VARCHAR(200) |  |  | Stores the numeric result for result is quantity charge calculation. |
| 38 | `SERVICE_DT_TM` | DATETIME |  |  | The date and time the service was provided. |
| 39 | `SERVICE_LOC_CD` | DOUBLE | NOT NULL |  | Value from 221 that represents the service resource where the activity/event occurred. |
| 40 | `SERVICE_RESOURCE_CD` | DOUBLE | NOT NULL |  | Value from 221 that represents the service resource where the activity/event occurred. |
| 41 | `SRV_DIAG1_ID` | DOUBLE | NOT NULL |  | This stores a code value that helps to diagnose why charges did not get created. |
| 42 | `SRV_DIAG2_ID` | DOUBLE | NOT NULL |  | This stores a code value that helps to diagnose why charges did not get created. |
| 43 | `SRV_DIAG3_ID` | DOUBLE | NOT NULL |  | This stores a value such as a code set that helps to diagnose why charges did not get created. |
| 44 | `SRV_DIAG4_ID` | DOUBLE | NOT NULL |  | This value helps to diagnose why charges were not created. Stores id fields such as organization id or price_sched_id. |
| 45 | `SRV_DIAG_CD` | DOUBLE | NOT NULL |  | This is the value from code set 18269 that defines the type of diagnosis code that the server has processed. |
| 46 | `UNITS` | DOUBLE | NOT NULL |  | The number of units that should be used in interval calculations. |
| 47 | `UNIT_TYPE_CD` | DOUBLE | NOT NULL |  | Value from 14276 that represents the type of unit such as miles, minutes, or hours. |
| 48 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 49 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 50 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 51 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 52 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `ACCESSION_ID` | [ACCESSION](ACCESSION.md) | `ACCESSION_ID` |
| `ALPHA_NOMEN_ID` | [NOMENCLATURE](NOMENCLATURE.md) | `NOMENCLATURE_ID` |
| `CEA_PRSNL_ID` | [PRSNL](PRSNL.md) | `PERSON_ID` |
| `CHARGE_EVENT_ID` | [CHARGE_EVENT](CHARGE_EVENT.md) | `CHARGE_EVENT_ID` |
| `REFERENCE_RANGE_FACTOR_ID` | [REFERENCE_RANGE_FACTOR](REFERENCE_RANGE_FACTOR.md) | `REFERENCE_RANGE_FACTOR_ID` |

## Referenced by (2)

| From table | Column |
|------------|--------|
| [CHARGE](CHARGE.md) | `CHARGE_EVENT_ACT_ID` |
| [CHARGE_EVENT_ACT_PRSNL](CHARGE_EVENT_ACT_PRSNL.md) | `CHARGE_EVENT_ACT_ID` |

