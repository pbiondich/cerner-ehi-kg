# SURG_CASE_PROCEDURE

> Surgical Case Procedure Table

**Description:** Surgical Case Procedure  
**Table type:** ACTIVITY  
**Primary key:** `SURG_CASE_PROC_ID`  
**Columns:** 70  
**Referenced by:** 10 columns

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ACTIVE_IND` | DOUBLE |  |  | The table row is active or inactive. A row is generally active unless it is in an inactive state such as logically deleted, combined away, pending purge, etc. |
| 2 | `ACTIVE_STATUS_CD` | DOUBLE | NOT NULL |  | Indicates the status of the row itself (not the data in the row) such as active, inactive, combined away, pending purge, etc. |
| 3 | `ACTIVE_STATUS_DT_TM` | DATETIME |  |  | The date and time that the active_status_cd was set. |
| 4 | `ACTIVE_STATUS_PRSNL_ID` | DOUBLE | NOT NULL |  | The person who caused the active_status_cd to be set or change. |
| 5 | `ANESTH_TYPE_CD` | DOUBLE | NOT NULL |  | Used for Surgery Mgmt Reporting -- indicates the anesthesia type assoc. w/ this case |
| 6 | `BEG_EFFECTIVE_DT_TM` | DATETIME |  |  | The date and time for which this table row becomes effective. Normally, this will be the date and time the row is added, but could be a past or future date and time. |
| 7 | `CONCURRENT_IND` | DOUBLE |  |  | Concurrent Indicator - Specifies that the procedure is concurrent with the previous procedure in the sequence. |
| 8 | `CREATE_APPLCTX` | DOUBLE |  |  | Create Application ContextColumn |
| 9 | `CREATE_DT_TM` | DATETIME |  |  | Create Date and TimeColumn |
| 10 | `CREATE_PRSNL_ID` | DOUBLE | NOT NULL |  | Create Personnel IdColumn |
| 11 | `CREATE_TASK` | DOUBLE |  |  | Create TaskColumn |
| 12 | `DEPT_CD` | DOUBLE | NOT NULL |  | Used for Surgery Mgmt Reporting -- indicates the department assoc. w/ this procedure |
| 13 | `END_EFFECTIVE_DT_TM` | DATETIME |  |  | The date/time after which the row is no longer valid as active current data. This may be valued with the date that the row became inactive. |
| 14 | `EVENT_ID` | DOUBLE | NOT NULL |  | Event IdColumn |
| 15 | `INST_CD` | DOUBLE | NOT NULL |  | Used for Surgery Mgmt Reporting -- indicates the institution assoc. w/ this procedure |
| 16 | `MODIFIER` | VARCHAR(500) |  |  | Used for Surgery Mgmt Reporting -- the modifiers documented for this procedure |
| 17 | `ORDER_ID` | DOUBLE | NOT NULL | FK→ | Order IdColumn |
| 18 | `PICK_LIST_CHG_FLAG` | DOUBLE |  |  | Pick List Change FlagColumn |
| 19 | `PREF_CARD_ID` | DOUBLE | NOT NULL |  | Preference Card Id for the procedure |
| 20 | `PRIMARY_PROC_IND` | DOUBLE |  |  | Primary Procedure IndicatorColumn |
| 21 | `PRIMARY_SURGEON_ID` | DOUBLE | NOT NULL | FK→ | Primary Surgeon Id for the CaseColumn |
| 22 | `PROC_COMPLETE_QTY` | DOUBLE |  |  | Used for Surgery Mgmt Reporting -- indicates the completion of this procedure |
| 23 | `PROC_DUR_MIN` | DOUBLE |  |  | Used for Surgery Mgmt Reporting -- indicates the duration of this procedure |
| 24 | `PROC_END_DT_TM` | DATETIME |  |  | Procedure End Date and TimeColumn |
| 25 | `PROC_END_TZ` | DOUBLE |  |  | Time zone associated with the corresponding DT_TM column. |
| 26 | `PROC_START_DAY` | DOUBLE |  |  | Used for Surgery Mgmt Reporting -- indicates the day of the week this Procedure started |
| 27 | `PROC_START_DT_TM` | DATETIME |  |  | Procedure Start Date and TimeColumn |
| 28 | `PROC_START_HOUR` | DOUBLE |  |  | Used for Surgery Mgmt Reporting -- indicates the hour of the day this procaedure started at |
| 29 | `PROC_START_MONTH` | DOUBLE |  |  | Used for Surgery Mgmt Reporting -- indicates the month this case is Procedure started at |
| 30 | `PROC_START_TZ` | DOUBLE |  |  | Time zone associated with the corresponding DT_TM column. |
| 31 | `PROC_TEXT` | VARCHAR(255) |  |  | Procedure TextColumn |
| 32 | `REPORTING_PROC_IND` | DOUBLE |  |  | Reporting Procedure IndicatorColumn |
| 33 | `SCHED_ANESTH_TYPE_CD` | DOUBLE | NOT NULL |  | Scheduled Anesthesia Type CodeColumn |
| 34 | `SCHED_BLOOD_PRODUCT_REQ_IND` | DOUBLE | NOT NULL |  | A scheduled indicator of whether blood products are required for this surgical procedure. |
| 35 | `SCHED_CASE_LEVEL_CD` | DOUBLE | NOT NULL |  | The scheduled case level (such as Routine 1 Circ 1 Scrub) for this procedure. |
| 36 | `SCHED_DUR` | DOUBLE |  |  | Scheduled Duration of the procedure |
| 37 | `SCHED_FROZEN_SECTION_REQ_IND` | DOUBLE | NOT NULL |  | A scheduled indicator of whether a frozen section is required for this surgical procedure. |
| 38 | `SCHED_IMPLANT_IND` | DOUBLE | NOT NULL |  | A scheduled indicator of whether an implant is required for this surgical procedure. |
| 39 | `SCHED_MODIFIER` | VARCHAR(100) |  |  | Used for Surgery Mgmt Reporting -- the modifiers scheduled for this procedure |
| 40 | `SCHED_PRIMARY_IND` | DOUBLE |  |  | Used for Surgery Mgmt Reporting -- indicates whether this procedure was scheduled as the primary |
| 41 | `SCHED_PRIMARY_SURGEON_ID` | DOUBLE | NOT NULL | FK→ | Scheduled Primary Surgeon IdColumn |
| 42 | `SCHED_PROC_CNT` | DOUBLE | NOT NULL |  | The scheduled number of procedures that are actually represented by this surgical procedure. If this is a combination of procedures, this will be greater than one. |
| 43 | `SCHED_QTY` | DOUBLE |  |  | Used for Surgery Mgmt Reporting -- indicates that this procedure has been scheduled |
| 44 | `SCHED_SEQ_NUM` | DOUBLE |  |  | Scheduled Sequnce number of the procedure |
| 45 | `SCHED_SPEC_REQ_IND` | DOUBLE | NOT NULL |  | An scheduled indicator of whether a specimen is required for this surgical procedure. |
| 46 | `SCHED_SURG_AREA_CD` | DOUBLE | NOT NULL |  | Scheduled Surgical Area |
| 47 | `SCHED_SURG_PROC_CD` | DOUBLE | NOT NULL |  | Scheduled Surgical Procedure CodeColumn |
| 48 | `SCHED_SURG_SPECIALTY_ID` | DOUBLE | NOT NULL | FK→ | Used for Surgery Mgmt Reporting -- the surgical specialty scheduled for this procedure |
| 49 | `SCHED_UD1_CD` | DOUBLE | NOT NULL |  | The scheduled value of the first user-defined field for this surgical procedure. |
| 50 | `SCHED_UD2_CD` | DOUBLE | NOT NULL |  | The scheduled value of the second user-defined field for this surgical procedure. |
| 51 | `SCHED_UD3_CD` | DOUBLE | NOT NULL |  | The scheduled value of the third user-defined field for this surgical procedure. |
| 52 | `SCHED_UD4_CD` | DOUBLE | NOT NULL |  | The scheduled value of the fourth user-defined field for this surgical procedure. |
| 53 | `SCHED_UD5_CD` | DOUBLE | NOT NULL |  | The scheduled value of the fifth user-defined field for this surgical procedure. |
| 54 | `SCHED_WOUND_CLASS_CD` | DOUBLE | NOT NULL |  | The scheduled wound class for this procedure. |
| 55 | `SCHED_XRAY_IND` | DOUBLE | NOT NULL |  | A scheduled indicator of whether an Xray is required for this surgical procedure. |
| 56 | `SCHED_XRAY_TECH_IND` | DOUBLE | NOT NULL |  | A scheduled indicator of whether an Xray technician is required for this surgical procedure. |
| 57 | `SEGMENT_HEADER_ID` | DOUBLE | NOT NULL | FK→ | Segment Header IDColumn |
| 58 | `SPEC_NOT_COLLECTED_REASON_CD` | DOUBLE | NOT NULL |  | Specimen Not collected Reason Code |
| 59 | `SURG_AREA_CD` | DOUBLE | NOT NULL |  | Surgical Area CodeColumn |
| 60 | `SURG_CASE_ID` | DOUBLE | NOT NULL | FK→ | Surgical Case IDColumn |
| 61 | `SURG_CASE_PROC_ID` | DOUBLE | NOT NULL | PK | Surgical Case Procedure ID - the unique number on this table to identity the row |
| 62 | `SURG_PROC_CD` | DOUBLE | NOT NULL |  | Surgical Procedure CodeColumn |
| 63 | `SURG_SPECIALTY_ID` | DOUBLE | NOT NULL | FK→ | Surgical Specialty IDColumn |
| 64 | `SYNONYM_ID` | DOUBLE | NOT NULL | FK→ | Synonym IDColumn |
| 65 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 66 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 67 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 68 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 69 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |
| 70 | `WOUND_CLASS_CD` | DOUBLE | NOT NULL |  | Wound Class CodeColumn |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `ORDER_ID` | [ORDERS](ORDERS.md) | `ORDER_ID` |
| `PRIMARY_SURGEON_ID` | [PRSNL](PRSNL.md) | `PERSON_ID` |
| `SCHED_PRIMARY_SURGEON_ID` | [PRSNL](PRSNL.md) | `PERSON_ID` |
| `SCHED_SURG_SPECIALTY_ID` | [PRSNL_GROUP](PRSNL_GROUP.md) | `PRSNL_GROUP_ID` |
| `SEGMENT_HEADER_ID` | [SEGMENT_HEADER](SEGMENT_HEADER.md) | `SEGMENT_HEADER_ID` |
| `SURG_CASE_ID` | [SURGICAL_CASE](SURGICAL_CASE.md) | `SURG_CASE_ID` |
| `SURG_SPECIALTY_ID` | [PRSNL_GROUP](PRSNL_GROUP.md) | `PRSNL_GROUP_ID` |
| `SYNONYM_ID` | [ORDER_CATALOG_SYNONYM](ORDER_CATALOG_SYNONYM.md) | `SYNONYM_ID` |

## Referenced by (10)

| From table | Column |
|------------|--------|
| [CASE_CART_PICK_LIST](CASE_CART_PICK_LIST.md) | `SURG_CASE_PROC_ID` |
| [IMPLANT_HISTORY](IMPLANT_HISTORY.md) | `SURG_CASE_PROC_ID` |
| [LH_CNT_IC_PATIENT_READ_SRG](LH_CNT_IC_PATIENT_READ_SRG.md) | `SURG_CASE_PROC_ID` |
| [SCHED_CASE_PICK_LIST](SCHED_CASE_PICK_LIST.md) | `SURG_CASE_PROC_ID` |
| [SN_PICKLIST_REQUEST](SN_PICKLIST_REQUEST.md) | `SURG_CASE_PROC_ID` |
| [SN_PICKLIST_REQUEST_PC](SN_PICKLIST_REQUEST_PC.md) | `SURG_CASE_PROC_ID` |
| [SN_PICKLIST_USE](SN_PICKLIST_USE.md) | `SURG_CASE_PROC_ID` |
| [SN_SURG_CASE_PROC_CPT](SN_SURG_CASE_PROC_CPT.md) | `SURG_CASE_PROC_ID` |
| [SN_SURG_CASE_PROC_DOC](SN_SURG_CASE_PROC_DOC.md) | `SURG_CASE_PROC_ID` |
| [SURG_CASE_PROC_MODIFIER](SURG_CASE_PROC_MODIFIER.md) | `SURG_CASE_PROC_ID` |

