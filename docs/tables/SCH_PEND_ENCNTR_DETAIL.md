# SCH_PEND_ENCNTR_DETAIL

> This table stores data that is captured at the time of booking the appointment and will be used to generate an encounter for the appointment closer to the appointment date and time.

**Description:** Scheduling Pending Encounter Details  
**Table type:** ACTIVITY  
**Primary key:** `SCH_PEND_ENCNTR_DETAIL_ID`  
**Columns:** 20  
**Referenced by:** 2 columns

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ASSIGNMENT_OF_BENEFITS_CD` | DOUBLE | NOT NULL |  | The patient's assignment of benefits code. |
| 2 | `ATTENDING_PRSNL_ID` | DOUBLE | NOT NULL | FK→ | The identifier of the attending physician. |
| 3 | `CLIENT_ORG_ID` | DOUBLE | NOT NULL | FK→ | The identifier of the client organization for the encounter. |
| 4 | `ENCNTR_TYPE_CD` | DOUBLE | NOT NULL |  | The type of encounter. |
| 5 | `EST_ARRIVE_DT_TM` | DATETIME |  |  | The estimated arrival date and time for the encounter. |
| 6 | `FACILITY_ORG_ID` | DOUBLE | NOT NULL | FK→ | The identifier of the facility organization for the encounter. |
| 7 | `LOCATION_CD` | DOUBLE | NOT NULL | FK→ | The location of the encounter. |
| 8 | `PATIENT_CASE_ID` | DOUBLE | NOT NULL | FK→ | The identifier of the patient case row for this appointment. |
| 9 | `PATIENT_SIGNATURE_SOURCE_CD` | DOUBLE | NOT NULL |  | The patient's signature source code. |
| 10 | `PROVIDER_ACCEPT_ASSIGNMENT_CD` | DOUBLE | NOT NULL |  | The provider accept assignment code. |
| 11 | `REASON_FOR_VISIT` | VARCHAR(255) |  |  | The free text description of reason for visit. otherwise known as admitting symptom, presenting symptom, etc. it is a brief description of why the person has presented for examination or treatment and may be the patient described symptom. |
| 12 | `REFERRING_PRSNL_ID` | DOUBLE | NOT NULL | FK→ | The identifier of the referring physician. |
| 13 | `REG_DT_TM` | DATETIME |  |  | The registration date and time of the encounter. |
| 14 | `RELEASE_OF_INFORMATION_CD` | DOUBLE | NOT NULL |  | The patient's release of information code. |
| 15 | `SCH_PEND_ENCNTR_DETAIL_ID` | DOUBLE | NOT NULL | PK | Unique generated number that identifies a single row on the SCH_PEND_ENCNTR_DETAIL table. |
| 16 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 17 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 18 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 19 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 20 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `ATTENDING_PRSNL_ID` | [PRSNL](PRSNL.md) | `PERSON_ID` |
| `CLIENT_ORG_ID` | [ORGANIZATION](ORGANIZATION.md) | `ORGANIZATION_ID` |
| `FACILITY_ORG_ID` | [ORGANIZATION](ORGANIZATION.md) | `ORGANIZATION_ID` |
| `LOCATION_CD` | [LOCATION](LOCATION.md) | `LOCATION_CD` |
| `PATIENT_CASE_ID` | [PATIENT_CASE](PATIENT_CASE.md) | `PATIENT_CASE_ID` |
| `REFERRING_PRSNL_ID` | [PRSNL](PRSNL.md) | `PERSON_ID` |

## Referenced by (2)

| From table | Column |
|------------|--------|
| [SCH_EVENT_PATIENT](SCH_EVENT_PATIENT.md) | `SCH_PEND_ENCNTR_DETAIL_ID` |
| [SCH_PEND_ENCNTR_AUTH_RELTN](SCH_PEND_ENCNTR_AUTH_RELTN.md) | `SCH_PEND_ENCNTR_DETAIL_ID` |

