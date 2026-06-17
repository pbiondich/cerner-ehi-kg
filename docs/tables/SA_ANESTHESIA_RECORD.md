# SA_ANESTHESIA_RECORD

> Top-Level Anesthesia Record containing surgical case and when the record was initially created 1 record per case that is documented. 26,100

**Description:** SA Anethesia Record  
**Table type:** ACTIVITY  
**Primary key:** `SA_ANESTHESIA_RECORD_ID`  
**Columns:** 22  
**Referenced by:** 17 columns

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ACTIVE_IND` | DOUBLE | NOT NULL |  | The table row is active or inactive. A row is generally active unless it is in an inactive state such as logically deleted, combined away, pending purge, etc. |
| 2 | `ACTIVE_STATUS_CD` | DOUBLE | NOT NULL |  | Indicates the status of the row itself (not the data in the row) such as active, inactive, combined away, pending purge, etc. |
| 3 | `ACTIVE_STATUS_DT_TM` | DATETIME | NOT NULL |  | The date and time that the active_status_cd was set. |
| 4 | `ACTIVE_STATUS_PRSNL_ID` | DOUBLE | NOT NULL |  | The person who caused the active_status_cd to be set or change. |
| 5 | `CLINICAL_EVENT_ID` | DOUBLE | NOT NULL | FK→ | This column is now obsolete. It has been replace by column EVENT_ID. The FK constraint to clinical_event.clinical_event_id has been disabled. 7/31/03 |
| 6 | `CREATED_BY_PRSNL_ID` | DOUBLE | NOT NULL | FK→ | User who originally created the anesthesia record |
| 7 | `CREATE_DT_TM` | DATETIME |  |  | Date/Time the anesthesia record was originally created |
| 8 | `CREATE_LOCATION_CD` | DOUBLE | NOT NULL |  | Location where the PC that created the anesthesia record is located |
| 9 | `EVENT_ID` | DOUBLE | NOT NULL |  | Event ID. Logical Event ID from Clinical Event. This is not the CE primary key field. |
| 10 | `FINALIZATION_TYPE_FLAG` | DOUBLE | NOT NULL |  | Determines which method was used to finalize the anesthesia record. 0 = finalized using original finalization method; 1 = finalized using new finalization method |
| 11 | `LAST_DOC_DT_TM` | DATETIME |  |  | The last time the record was opened for documentation. |
| 12 | `LAST_DOC_PRSNL_ID` | DOUBLE | NOT NULL |  | Contains the id of the user who last had the record opened for documentation. |
| 13 | `RECORD_DESCRIPTION` | VARCHAR(50) |  |  | Anesthesia record description |
| 14 | `SA_ANESTHESIA_RECORD_ID` | DOUBLE | NOT NULL | PK | Unique value to identify the anesthesia record |
| 15 | `SA_REF_DOC_TYPE_ID` | DOUBLE | NOT NULL | FK→ | The SA Ref Doc Type for this record |
| 16 | `SUPERVISOR_REQ_IND` | DOUBLE | NOT NULL |  | The supervisor_req_ind is set to 1 if Supervision is not required, set to 0 if Supervision is required or if SaDBBuild setting is off. |
| 17 | `SURGICAL_CASE_ID` | DOUBLE | NOT NULL | FK→ | Surgical Case this Anesthesia Record is documenting |
| 18 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 19 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 20 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 21 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 22 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `CLINICAL_EVENT_ID` | [CLINICAL_EVENT](CLINICAL_EVENT.md) | `CLINICAL_EVENT_ID` |
| `CREATED_BY_PRSNL_ID` | [PRSNL](PRSNL.md) | `PERSON_ID` |
| `SA_REF_DOC_TYPE_ID` | [SA_REF_DOC_TYPE](SA_REF_DOC_TYPE.md) | `SA_REF_DOC_TYPE_ID` |
| `SURGICAL_CASE_ID` | [SURGICAL_CASE](SURGICAL_CASE.md) | `SURG_CASE_ID` |

## Referenced by (17)

| From table | Column |
|------------|--------|
| [SA_ACTION](SA_ACTION.md) | `SA_ANESTHESIA_RECORD_ID` |
| [SA_ANESTHESIA_CHARGE](SA_ANESTHESIA_CHARGE.md) | `SA_ANESTHESIA_RECORD_ID` |
| [SA_ANESTHESIA_REC_FIELD_VALUES](SA_ANESTHESIA_REC_FIELD_VALUES.md) | `SA_ANESTHESIA_RECORD_ID` |
| [SA_ANESTHESIA_REC_LOCK](SA_ANESTHESIA_REC_LOCK.md) | `SA_ANESTHESIA_RECORD_ID` |
| [SA_ANESTHESIA_REC_STATUS](SA_ANESTHESIA_REC_STATUS.md) | `SA_ANESTHESIA_RECORD_ID` |
| [SA_CASE_ATTRIBUTE](SA_CASE_ATTRIBUTE.md) | `SA_ANESTHESIA_RECORD_ID` |
| [SA_CHARGE_POSTPONE](SA_CHARGE_POSTPONE.md) | `SA_ANESTHESIA_RECORD_ID` |
| [SA_DISPLAY_RESULT](SA_DISPLAY_RESULT.md) | `SA_ANESTHESIA_RECORD_ID` |
| [SA_FLUID](SA_FLUID.md) | `SA_ANESTHESIA_RECORD_ID` |
| [SA_ITEM](SA_ITEM.md) | `SA_ANESTHESIA_RECORD_ID` |
| [SA_LINKED_RESULT](SA_LINKED_RESULT.md) | `SA_ANESTHESIA_RECORD_ID` |
| [SA_MACRO](SA_MACRO.md) | `SA_ANESTHESIA_RECORD_ID` |
| [SA_MEDICATION](SA_MEDICATION.md) | `SA_ANESTHESIA_RECORD_ID` |
| [SA_PARAMETER](SA_PARAMETER.md) | `SA_ANESTHESIA_RECORD_ID` |
| [SA_PRSNL_ACTIVITY](SA_PRSNL_ACTIVITY.md) | `SA_ANESTHESIA_RECORD_ID` |
| [SA_REMINDER](SA_REMINDER.md) | `SA_ANESTHESIA_RECORD_ID` |
| [SA_TODO_LIST](SA_TODO_LIST.md) | `SA_ANESTHESIA_RECORD_ID` |

