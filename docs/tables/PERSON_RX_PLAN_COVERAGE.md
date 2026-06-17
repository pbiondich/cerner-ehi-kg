# PERSON_RX_PLAN_COVERAGE

> This table contains information pertaining to a specific prescription plan coverage for a person.

**Description:** Person Prescription Plan Coverage  
**Table type:** ACTIVITY  
**Primary key:** _(not published — see note)_  
**Columns:** 16

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ACTIVE_IND` | DOUBLE | NOT NULL |  | The table row is active or inactive. A row is generally active unless it is in an inactive state such as logically deleted, combined away, pending purge, etc. |
| 2 | `ACTIVE_STATUS_CD` | DOUBLE | NOT NULL |  | Indicates the status of the row itself (not the data in the row) such as active, inactive, combined away, pending purge, etc. |
| 3 | `ACTIVE_STATUS_DT_TM` | DATETIME | NOT NULL |  | The date and time that the active_status_cd was set. |
| 4 | `ACTIVE_STATUS_PRSNL_ID` | DOUBLE | NOT NULL |  | The person who caused the active_status_cd to be set or change. |
| 5 | `BEG_SERVICE_DT_TM` | DATETIME |  |  | The date the service coverage begins. |
| 6 | `COVERAGE_STATUS_CD` | DOUBLE | NOT NULL |  | Describes the eligibility of the coverage. For example, eligible or not eligible. |
| 7 | `END_SERVICE_DT_TM` | DATETIME |  |  | The date when service coverage ends. |
| 8 | `PERSON_RX_PLAN_COVERAGE_ID` | DOUBLE | NOT NULL |  | The primary identifier of this table. |
| 9 | `PERSON_RX_PLAN_RELTN_ID` | DOUBLE | NOT NULL | FK→ | The ID of the person prescription plan relation that this coverage is related to.. |
| 10 | `SERVICE_TYPE_CD` | DOUBLE | NOT NULL |  | The codified service type for the coverage. Populated when the service type for the coverage is defined by the X12 specification and can therefore be codified. No coverage will have both a service_type_cd and a service_type_txt. |
| 11 | `SERVICE_TYPE_TXT` | VARCHAR(255) |  |  | The free text service type for the coverage. Populated when the service type is not defined by the X12 specification and therefore cannot be codified. No coverage will have both a service_type_cd and a service_type_txt. |
| 12 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 13 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 14 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 15 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 16 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `PERSON_RX_PLAN_RELTN_ID` | [PERSON_RX_PLAN_RELTN](PERSON_RX_PLAN_RELTN.md) | `PERSON_RX_PLAN_RELTN_ID` |

