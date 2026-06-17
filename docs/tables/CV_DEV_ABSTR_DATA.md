# CV_DEV_ABSTR_DATA

> OMF Summary Table for the CVNet Device Abstract Data

**Description:** CVNet Device Abstract Data  
**Table type:** ACTIVITY  
**Primary key:** _(not published — see note)_  
**Columns:** 23

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ACTIVE_IND` | DOUBLE |  |  | The table row is active or inactive. A row is generally active unless it is in an inactive state such as logically deleted, combined away, pending purge, etc. |
| 2 | `ACTIVE_STATUS_CD` | DOUBLE | NOT NULL |  | Indicates the status of the row itself (not the data in the row) such as active, inactive, combined away, pending purge, etc. |
| 3 | `ACTIVE_STATUS_DT_TM` | DATETIME |  |  | The date and time that the active_status_cd was set. |
| 4 | `ACTIVE_STATUS_PRSNL_ID` | DOUBLE | NOT NULL |  | The person who caused the active_status_cd to be set or change. |
| 5 | `BEG_EFFECTIVE_DT_TM` | DATETIME |  |  | The date and time for which this table row becomes effective. Normally, this will be the date and time the row is added, but could be a past or future date and time. |
| 6 | `DEVICE_ID` | DOUBLE | NOT NULL | FK→ | This is the primary key identifier to the CV_DEVICE table and serves as a foreign key to the CV_DEV_ABSTR_DATA table. |
| 7 | `DEV_ABSTR_DATA_ID` | DOUBLE | NOT NULL |  | This is the primary key identifier to the CV_DEV_ABSTR_DATA table. |
| 8 | `END_EFFECTIVE_DT_TM` | DATETIME |  |  | The date/time after which the row is no longer valid as active current data. This may be valued with the date that the row became inactive. |
| 9 | `EVENT_CD` | DOUBLE | NOT NULL |  | Event code that represents the clinical event for the OMF Clinical Report |
| 10 | `EVENT_ID` | DOUBLE | NOT NULL |  | Uniquely identifies a logical clinical event row. There may be more than one row with the same event_id, but only one of those rows will be current as indicated by the valid_until_dt_tm field. This is an EVENT_ID value from the CLINICAL_EVENT table. |
| 11 | `EVENT_TYPE_CD` | DOUBLE | NOT NULL |  | Event type code defines the group of data this particular event belongs for example Lesion, PTCA, Case, etc. |
| 12 | `GROUP_TYPE_CD` | DOUBLE | NOT NULL |  | Related events are grouped based on their nature or location |
| 13 | `NOMENCLATURE_ID` | DOUBLE | NOT NULL | FK→ | Stores the identifier (from the nomenclature table) that stores the text for the result. |
| 14 | `RESULT_CD` | DOUBLE | NOT NULL |  | This is the coded result. It is used to identify a particular patient response to a clinical event (instead of nomenclature id). |
| 15 | `RESULT_DT_TM` | DATETIME |  |  | The date and time that the result_value was set. |
| 16 | `RESULT_ID` | DOUBLE | NOT NULL |  | This is the identifier for the result. It depends on the field type, but at the moment we only use it for PERSON_ID when the result_val is a person name. (The usage in the other CV_*_ABSTR_DATA tables). |
| 17 | `RESULT_SOURCE` | VARCHAR(32) |  |  | This is the source table for the result. |
| 18 | `RESULT_VAL` | VARCHAR(255) |  |  | The value associated with the abstract event |
| 19 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 20 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 21 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 22 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 23 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `DEVICE_ID` | [CV_DEVICE](CV_DEVICE.md) | `DEVICE_ID` |
| `NOMENCLATURE_ID` | [NOMENCLATURE](NOMENCLATURE.md) | `NOMENCLATURE_ID` |

