# WORKLOAD

> Holds workload information at the discrete level. This is not statistical data.

**Description:** Workload  
**Table type:** ACTIVITY  
**Primary key:** _(not published — see note)_  
**Columns:** 51

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ACCESSION` | VARCHAR(20) |  |  | The accession number associated with the service or activity. It represents a specimen or case. This will not be associated with every workload row. |
| 2 | `ACCRUED_DT_TM` | DATETIME |  |  | The date and time the charge was created. |
| 3 | `ACTIVE_IND` | DOUBLE |  |  | The table row is active or inactive. A row is generally active unless it is in an inactive state such as logically deleted, combined away, pending purge, etc. |
| 4 | `ACTIVITY_TYPE_CD` | DOUBLE | NOT NULL |  | This value identifies what "net" (PathNet, RadNet) and/or what department (General Lab, Micro) a bill item belongs to. |
| 5 | `BEG_EFFECTIVE_DT_TM` | DATETIME |  |  | The date and time for which this table row becomes effective. Normally, this will be the date and time the row is added, but could be a past or future date and time. |
| 6 | `BILL_ITEM_ID` | DOUBLE | NOT NULL | FK→ | This is the value of the unique primary identifier of the bill_item table. |
| 7 | `CHARGE_EVENT_ACT_ID` | DOUBLE | NOT NULL |  | This is the value of the unique primary identifier of the charge_event_act table. It is an internal system assigned number. |
| 8 | `CHARGE_EVENT_ID` | DOUBLE | NOT NULL | FK→ | This is the value of the unique primary identifier of the charge_event table. |
| 9 | `DEF_BILL_ITEM_ID` | DOUBLE | NOT NULL |  | This is the value of the unique primary identifier of the bill_item table. It represents the bill item id of the default child bill item when a unique or default bill item have been used in accruing workload. |
| 10 | `DEPT_CD` | DOUBLE | NOT NULL |  | The code value from code_set 220 that represents the department where the service or activity was performed. The service resource on the charge event is used to determine the department. If the charge event is associated with a clinical event that occur |
| 11 | `ENCNTR_ID` | DOUBLE | NOT NULL |  | This is the value of the unique primary identifier of the encounter table. It is an internal system assigned number. |
| 12 | `ENCNTR_TYPE_CD` | DOUBLE | NOT NULL |  | This field is the value from codeset 71 that represents visit type. |
| 13 | `EXTENDED_UNITS` | DOUBLE |  |  | The number of units that were calculated by the server using the multiplier and interval logic if necessary. |
| 14 | `INSTITUTION_CD` | DOUBLE | NOT NULL |  | This is the value from code set 221 that represents the institution in the service resource heirarchy. |
| 15 | `ITEM_FOR_COUNT_CD` | DOUBLE | NOT NULL |  | This code value indicates accrual frequency for the item. An example might be per specimen. |
| 16 | `MANUAL_ENTRY_IND` | DOUBLE |  |  | Indicates that this workload row was added using Workload Entry, it was not automatically accrued based on clinical activity. |
| 17 | `MED_SERVICE_CD` | DOUBLE | NOT NULL |  | This is the value from codeset 34 that represents the category of treatment, surgery, or general resources. |
| 18 | `MULTIPLIER` | DOUBLE |  |  | The raw number of units that were assigned based on the standard or the number of units entered in the Pricing Tool. |
| 19 | `ORD_PHYS_ID` | DOUBLE | NOT NULL |  | This is the value of the unique primary identifier of the person table. It is an internal system assigned number. It represents the physician who ordered the service or activity. |
| 20 | `ORG_ID` | DOUBLE | NOT NULL |  | This is the value of the unique primary identifier of the organization table. . |
| 21 | `PARENT_WORKLOAD_ID` | DOUBLE | NOT NULL |  | This is the value of the unique primary identifier of the workload table. . It represents the identifier of the workload row that resulted from the parent bill item. |
| 22 | `PAT_LOC_CD` | DOUBLE | NOT NULL |  | The code value of the patient location from codeset 221. This is at the nurse unit/amulatory location level. |
| 23 | `PERSON_ID` | DOUBLE | NOT NULL |  | This is the value of the unique primary identifier of the person table. It is an internal system assigned number. |
| 24 | `POSITION_CD` | DOUBLE | NOT NULL |  | This value represents the position of the person in the prsn_id field. For example, RN, LPN etc. |
| 25 | `PROJECTED_DT_TM` | DATETIME |  |  | Not used |
| 26 | `PROJECTED_IND` | DOUBLE |  |  | Not used |
| 27 | `PRSNL_ID` | DOUBLE | NOT NULL |  | This is the value of the unique primary identifier of the workload_standard table. It is an internal system assigned number. It represents the person who completed the event that resulted in this workload row. |
| 28 | `QTY` | DOUBLE |  |  | This field contains the quantity for the number of units that will be multiplied to the workload multiplier in order to figure the volume of workload. |
| 29 | `RAW_COUNT` | DOUBLE |  |  | Raw procedure count. |
| 30 | `REASON_CD` | DOUBLE | NOT NULL |  | This is the field for the reason code |
| 31 | `REASON_COMMENT` | VARCHAR(200) |  |  | This field has the description for the reason code |
| 32 | `REPEAT_IND` | DOUBLE |  |  | Indicates whether this row is a result of repeated tests, used only for PathNet. |
| 33 | `SECTION_CD` | DOUBLE | NOT NULL |  | The code value from code_set 220 that represents the section where the service or activity was performed. The service resource on the charge event is used to determine the section if the charge event is associated with a clinical event that occurs before. |
| 34 | `SERVICE_DT_TM` | DATETIME |  |  | The date and time that the service was complete for the event that resulted in this workload row. |
| 35 | `SERVICE_RESOURCE_CD` | DOUBLE | NOT NULL |  | The code value from code_set 220 that represents the performing location of the service or activity. This could be an instrument, bench, exam room, or a role for tasks. |
| 36 | `SUBSECTION_CD` | DOUBLE | NOT NULL |  | The code value from code_set 220 that represents the subsection where the service or activity was performed. The service resource on the charge event is used to determine the subsection If the charge event is associated with a clinical event that occurs |
| 37 | `UNITS` | DOUBLE |  |  | The number of units that were calculated by the server using the multiplier and interval logic if necessary. |
| 38 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 39 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 40 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 41 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 42 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |
| 43 | `WL_BOOK_CD` | DOUBLE | NOT NULL |  | This value represents the book that this particular item's code was within. |
| 44 | `WL_CHAPTER_CD` | DOUBLE | NOT NULL |  | This value represents the chapter that the item's code was within. |
| 45 | `WL_CODE` | VARCHAR(50) |  |  | The code associated with this service or activity as assigned by the server using either the workload standard or the code entered in the Pricing Tool. |
| 46 | `WL_CODE_DESC` | VARCHAR(200) |  |  | The description associated with the workload code. This is either from the standard, or is entered in the Pricing Tool. |
| 47 | `WL_CODE_SCHED_CD` | DOUBLE | NOT NULL |  | This value represents the workload schedule from code set 14002 that the workload code belongs to. |
| 48 | `WL_SECTION_CD` | DOUBLE | NOT NULL |  | This value represents the section that the item's code was within. |
| 49 | `WORKLOAD_ID` | DOUBLE | NOT NULL |  | This is the value of the unique primary identifier of the workload table. It is an internal system assigned number. |
| 50 | `WORKLOAD_STANDARD_ID` | DOUBLE | NOT NULL | FK→ | This is the value of the unique primary identifier of the workload_standard table. |
| 51 | `WORKLOAD_TYPE_CD` | DOUBLE | NOT NULL |  | Indicates if the workload is accrued, modified, or credited. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `BILL_ITEM_ID` | [BILL_ITEM](BILL_ITEM.md) | `BILL_ITEM_ID` |
| `CHARGE_EVENT_ID` | [CHARGE_EVENT](CHARGE_EVENT.md) | `CHARGE_EVENT_ID` |
| `WORKLOAD_STANDARD_ID` | [WORKLOAD_STANDARD](WORKLOAD_STANDARD.md) | `WORKLOAD_STANDARD_ID` |

