# SA_REF_DOC_TYPE

> SA REFERENCE DOCUMENT TYPE

**Description:** SA REFERENCE DOC TYPE  
**Table type:** REFERENCE  
**Primary key:** `SA_REF_DOC_TYPE_ID`  
**Columns:** 16  
**Referenced by:** 22 columns

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ACTIVE_IND` | DOUBLE | NOT NULL |  | The table row is active or inactive. A row is generally active unless it is in an inactive state such as logically deleted, combined away, pending purge, etc. |
| 2 | `ACTIVE_STATUS_CD` | DOUBLE | NOT NULL |  | Indicates the status of the row itself (not the data in the row) such as active, inactive, combined away, pending purge, etc. |
| 3 | `ACTIVE_STATUS_DT_TM` | DATETIME | NOT NULL |  | The date and time that the active_status_cd was set. |
| 4 | `ACTIVE_STATUS_PRSNL_ID` | DOUBLE | NOT NULL |  | The person who caused the active_status_cd to be set or change. |
| 5 | `BLOB_EVENT_CD` | DOUBLE | NOT NULL |  | Event Cd used for the finalized printed record |
| 6 | `CV_REPORT_EVENT_CD` | DOUBLE | NOT NULL |  | Event cd used for the cv report |
| 7 | `GEN_ACTION_EVENT_CD` | DOUBLE | NOT NULL |  | Event Cd used for generic actions |
| 8 | `RECORD_EVENT_CD` | DOUBLE | NOT NULL |  | Event Cd used for finalized record |
| 9 | `SA_DOC_TYPE_CD` | DOUBLE | NOT NULL |  | Doc Type Cd defining the type of document |
| 10 | `SA_REF_DOC_TYPE_ID` | DOUBLE | NOT NULL | PK | Unique identifier for row |
| 11 | `SA_REF_DOC_TYPE_NAME` | VARCHAR(255) | NOT NULL |  | Name of Document type |
| 12 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 13 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 14 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 15 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 16 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Referenced by (22)

| From table | Column |
|------------|--------|
| [SA_ANESTHESIA_RECORD](SA_ANESTHESIA_RECORD.md) | `SA_REF_DOC_TYPE_ID` |
| [SA_PREFERENCE](SA_PREFERENCE.md) | `SA_REF_DOC_TYPE_ID` |
| [SA_REF_DOC_TYPE_AREA](SA_REF_DOC_TYPE_AREA.md) | `SA_REF_DOC_TYPE_ID` |
| [SA_REF_EXCLUDE_ACTION](SA_REF_EXCLUDE_ACTION.md) | `SA_REF_DOC_TYPE_ID` |
| [SA_REF_EXCLUDE_DEVICE](SA_REF_EXCLUDE_DEVICE.md) | `SA_REF_DOC_TYPE_ID` |
| [SA_REF_EXCLUDE_DILUENT](SA_REF_EXCLUDE_DILUENT.md) | `SA_REF_DOC_TYPE_ID` |
| [SA_REF_EXCLUDE_FLUID](SA_REF_EXCLUDE_FLUID.md) | `SA_REF_DOC_TYPE_ID` |
| [SA_REF_EXCLUDE_ITEM](SA_REF_EXCLUDE_ITEM.md) | `SA_REF_DOC_TYPE_ID` |
| [SA_REF_EXCLUDE_MEDICATION](SA_REF_EXCLUDE_MEDICATION.md) | `SA_REF_DOC_TYPE_ID` |
| [SA_REF_EXCLUDE_PARAMETER](SA_REF_EXCLUDE_PARAMETER.md) | `SA_REF_DOC_TYPE_ID` |
| [SA_REF_EXCLUDE_POSITION](SA_REF_EXCLUDE_POSITION.md) | `SA_REF_DOC_TYPE_ID` |
| [SA_REF_EXCLUDE_PROVIDER](SA_REF_EXCLUDE_PROVIDER.md) | `SA_REF_DOC_TYPE_ID` |
| [SA_REF_FLUID_PREFERENCE](SA_REF_FLUID_PREFERENCE.md) | `SA_REF_DOC_TYPE_ID` |
| [SA_REF_MACRO](SA_REF_MACRO.md) | `SA_REF_DOC_TYPE_ID` |
| [SA_REF_MED_PREFERENCE](SA_REF_MED_PREFERENCE.md) | `SA_REF_DOC_TYPE_ID` |
| [SA_REF_REQUIRED_ACTION](SA_REF_REQUIRED_ACTION.md) | `SA_REF_DOC_TYPE_ID` |
| [SA_REF_REQUIRED_CATEGORY](SA_REF_REQUIRED_CATEGORY.md) | `SA_REF_DOC_TYPE_ID` |
| [SA_REF_REQUIRED_FLUID](SA_REF_REQUIRED_FLUID.md) | `SA_REF_DOC_TYPE_ID` |
| [SA_REF_REQUIRED_ITEM](SA_REF_REQUIRED_ITEM.md) | `SA_REF_DOC_TYPE_ID` |
| [SA_REF_REQUIRED_MEDICATION](SA_REF_REQUIRED_MEDICATION.md) | `SA_REF_DOC_TYPE_ID` |
| [SA_REF_REQUIRED_PARAMETER](SA_REF_REQUIRED_PARAMETER.md) | `SA_REF_DOC_TYPE_ID` |
| [SA_REF_REQUIRED_PRSNL_ACTIVITY](SA_REF_REQUIRED_PRSNL_ACTIVITY.md) | `SA_REF_DOC_TYPE_ID` |

