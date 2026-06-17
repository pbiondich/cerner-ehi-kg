# PATIENT_EVENT_DETAIL

> Captures event details for a given Patient_Event row.

**Description:** Patient Event Detail  
**Table type:** ACTIVITY  
**Primary key:** `PATIENT_EVENT_DETAIL_ID`  
**Columns:** 18  
**Referenced by:** 1 columns

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ACTIVE_IND` | DOUBLE | NOT NULL |  | The table row is active or inactive. A row is generally active unless it is in an inactive state such as logically deleted, combined away, pending purge, etc. |
| 2 | `ACTIVE_STATUS_CD` | DOUBLE | NOT NULL |  | Indicates the status of the row itself (not the data in the row) such as active, inactive, combined away, pending purge, etc. |
| 3 | `ACTIVE_STATUS_DT_TM` | DATETIME | NOT NULL |  | The date and time that the active_status_cd was set. |
| 4 | `ACTIVE_STATUS_PRSNL_ID` | DOUBLE | NOT NULL |  | The person who caused the active_status_cd to be set or change. |
| 5 | `PATIENT_EVENT_DETAIL_ID` | DOUBLE | NOT NULL | PK | Uniquely identifies details about a patient event. |
| 6 | `PATIENT_EVENT_ID` | DOUBLE | NOT NULL | FK→ | Uniquely identifies a related patient event. |
| 7 | `PE_VALUE_CD` | DOUBLE | NOT NULL |  | Coded value for the given patient event detail. |
| 8 | `PE_VALUE_DT_TM` | DATETIME |  |  | Date and time value for the given patient event detail. |
| 9 | `PE_VALUE_ID` | DOUBLE | NOT NULL |  | Uniquely identifies the related row on the table identified in the PE_VALUE_NAME column. |
| 10 | `PE_VALUE_MEANING` | VARCHAR(25) |  |  | This meaning will define what value is being saved. This value can be created by whomever is writing the row. When reading from the table, every meaning should only have 1 of the corresponding pe_value columns actually valued. |
| 11 | `PE_VALUE_NAME` | VARCHAR(30) | NOT NULL |  | Identifies the table to which this event is related. |
| 12 | `PE_VALUE_NUMERIC` | DOUBLE |  |  | Numeric value for the given patient event detail. |
| 13 | `PE_VALUE_STRING` | VARCHAR(4000) |  |  | The string value for the given patient event detail. |
| 14 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 15 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 16 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 17 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 18 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `PATIENT_EVENT_ID` | [PATIENT_EVENT](PATIENT_EVENT.md) | `PATIENT_EVENT_ID` |

## Referenced by (1)

| From table | Column |
|------------|--------|
| [PATIENT_EVENT_DETAIL_HIST](PATIENT_EVENT_DETAIL_HIST.md) | `PATIENT_EVENT_DETAIL_ID` |

