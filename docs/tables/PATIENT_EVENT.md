# PATIENT_EVENT

> Table to capture event details for a patient_event row

**Description:** Patient Event  
**Table type:** ACTIVITY  
**Primary key:** `PATIENT_EVENT_ID`  
**Columns:** 15  
**Referenced by:** 3 columns

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ACTIVE_IND` | DOUBLE | NOT NULL |  | The table row is active or inactive. A row is generally active unless it is in an inactive state such as logically deleted, combined away, pending purge, etc. |
| 2 | `ACTIVE_STATUS_CD` | DOUBLE | NOT NULL |  | Indicates the status of the row itself (not the data in the row) such as active, inactive, combined away, pending purge, etc. |
| 3 | `ACTIVE_STATUS_DT_TM` | DATETIME | NOT NULL |  | The date and time that the active_status_cd was set. |
| 4 | `ACTIVE_STATUS_PRSNL_ID` | DOUBLE | NOT NULL |  | The person who caused the active_status_cd to be set or change. |
| 5 | `ENCNTR_ID` | DOUBLE | NOT NULL | FK→ | Uniquely identifies the related Encounter |
| 6 | `EVENT_DT_TM` | DATETIME |  |  | The date and time the event took place. |
| 7 | `EVENT_TYPE_CD` | DOUBLE | NOT NULL |  | Type of event being written. |
| 8 | `PATIENT_EVENT_ID` | DOUBLE | NOT NULL | PK | Uniquely identifies a captured event for a patient. |
| 9 | `PERSON_ID` | DOUBLE | NOT NULL | FK→ | Uniquely identifies a related person. |
| 10 | `TRANSACTION_DT_TM` | DATETIME |  |  | The date and time the event was written to the database. |
| 11 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 12 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 13 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 14 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 15 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `ENCNTR_ID` | [ENCOUNTER](ENCOUNTER.md) | `ENCNTR_ID` |
| `PERSON_ID` | [PERSON](PERSON.md) | `PERSON_ID` |

## Referenced by (3)

| From table | Column |
|------------|--------|
| [PATIENT_EVENT_DETAIL](PATIENT_EVENT_DETAIL.md) | `PATIENT_EVENT_ID` |
| [PATIENT_EVENT_DETAIL_HIST](PATIENT_EVENT_DETAIL_HIST.md) | `PATIENT_EVENT_ID` |
| [PATIENT_EVENT_HIST](PATIENT_EVENT_HIST.md) | `PATIENT_EVENT_ID` |

