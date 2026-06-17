# RX_PENDING_CREDIT

> This table will queue up order information for orders that have been end-stated and need to be processed for potential system crediting. Once a row has been processed successfully, it will get deleted from the table.

**Description:** Pharmacy Pending Credit  
**Table type:** ACTIVITY  
**Primary key:** _(not published — see note)_  
**Columns:** 15

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ACTION_EFFECTIVE_DT_TM` | DATETIME |  |  | Identifies the effective date and time associated with the end stated action. From ORDER_ACTION |
| 2 | `ACTION_EFFECTIVE_DT_TM_TZ` | DOUBLE | NOT NULL |  | Identifies the time zone associated with the action_effective_dt_tm. From ORDER_ACTION |
| 3 | `ACTION_SEQUENCE` | DOUBLE | NOT NULL | FK→ | Identifies the action sequence associated with an end-stated action. |
| 4 | `DISPENSE_CATEGORY_CD` | DOUBLE | NOT NULL |  | Identifies the dispense category code associated with the end stated action. From ORDER_DETAIL |
| 5 | `ORDER_ID` | DOUBLE | NOT NULL | FK→ | Identifies the order associated with an end-stated action. |
| 6 | `PATIENT_FACILITY_CD` | DOUBLE | NOT NULL | FK→ | Identifies the facility code associated with the patient.From ENCOUNTER |
| 7 | `PATIENT_NURSE_UNIT_CD` | DOUBLE | NOT NULL | FK→ | Identifies the nurse unit code associated with the patientFrom ENCOUNTER |
| 8 | `RX_PENDING_CREDIT_ID` | DOUBLE | NOT NULL |  | Unique, generated number that identifies a single row on the RX_PENDING_CREDIT table. |
| 9 | `STATUS_FLAG` | DOUBLE | NOT NULL |  | Indicates the status of each pending credit. |
| 10 | `STATUS_REASON_TXT` | VARCHAR(100) |  |  | Free text description of the reason for the current status. |
| 11 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 12 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 13 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 14 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 15 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `ACTION_SEQUENCE` | [ORDER_ACTION](ORDER_ACTION.md) | `ACTION_SEQUENCE` |
| `ORDER_ID` | [ORDER_ACTION](ORDER_ACTION.md) | `ORDER_ID` |
| `PATIENT_FACILITY_CD` | [LOCATION](LOCATION.md) | `LOCATION_CD` |
| `PATIENT_NURSE_UNIT_CD` | [LOCATION](LOCATION.md) | `LOCATION_CD` |

