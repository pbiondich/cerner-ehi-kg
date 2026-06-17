# EEM_ABN_LINK

> Denormailization of EEM_ABN_CHECK table for reporting and quick access to price information for signed forms

**Description:** Enterprise Eligibility Management Advance Beneficiary Notice Link  
**Table type:** ACTIVITY  
**Primary key:** _(not published — see note)_  
**Columns:** 21

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `BEG_EFFECTIVE_DT_TM` | DATETIME | NOT NULL |  | The date and time for which this table row becomes effective. Normally, this will be the date and time the row is added, but could be a past or future date and time. |
| 2 | `CANDIDATE_ID` | DOUBLE | NOT NULL |  | A sequence-generated number to uniquely identify the specific row in the database. |
| 3 | `EEM_ABN_LINK_ID` | DOUBLE | NOT NULL |  | Unique generated number that identifies a single row on the EEM_ABN_LINK table. |
| 4 | `ENCNTR_ID` | DOUBLE | NOT NULL | FK→ | ID of the encounter the ABN check is attached to |
| 5 | `END_EFFECTIVE_DT_TM` | DATETIME | NOT NULL |  | The date/time after which the row is no longer valid as active current data. This may be valued with the date that the row became inactive. |
| 6 | `HEALTH_PLAN_ID` | DOUBLE | NOT NULL | FK→ | The health plan id of the health plan that generated the price |
| 7 | `HIGH_STATUS_CD` | DOUBLE | NOT NULL |  | The high status code. Examples are form required or form not required. |
| 8 | `HIGH_STATUS_MEANING` | VARCHAR(12) |  |  | A textual representation of the high status. |
| 9 | `LOCATION_CD` | DOUBLE | NOT NULL | FK→ | The location that the procedure was checked against. |
| 10 | `MED_STATUS_CD` | DOUBLE | NOT NULL |  | The medium status code for the abn check. For example, meets medical necessity, does not meet medical necessity, policy not defined, ambiguous, etc. |
| 11 | `MED_STATUS_MEANING` | VARCHAR(12) |  |  | A text representation of the meaning for med_status_cd. |
| 12 | `ORDER_ID` | DOUBLE | NOT NULL | FK→ | ID of the order the ABN check is attached to |
| 13 | `ORDER_PRICE` | DOUBLE |  |  | A text representation of the price of the procedures not covered by Medicare |
| 14 | `PERSON_ID` | DOUBLE | NOT NULL | FK→ | ID of the person the ABN check is attached to |
| 15 | `PROCEDURE_STRING` | VARCHAR(255) |  |  | A text representation of the price of the procedures on the check |
| 16 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 17 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 18 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 19 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 20 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 21 | `VERSION_DT_TM` | DATETIME | NOT NULL |  | The version date and time marks the date the record became historical. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `ENCNTR_ID` | [ENCOUNTER](ENCOUNTER.md) | `ENCNTR_ID` |
| `HEALTH_PLAN_ID` | [HEALTH_PLAN](HEALTH_PLAN.md) | `HEALTH_PLAN_ID` |
| `LOCATION_CD` | [LOCATION](LOCATION.md) | `LOCATION_CD` |
| `ORDER_ID` | [ORDERS](ORDERS.md) | `ORDER_ID` |
| `PERSON_ID` | [PERSON](PERSON.md) | `PERSON_ID` |

