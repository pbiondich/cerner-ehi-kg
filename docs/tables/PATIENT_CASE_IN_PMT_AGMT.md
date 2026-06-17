# PATIENT_CASE_IN_PMT_AGMT

> An inbound payment agreement patient case tracks a patient and their details when the patient is coming from another healthcare entity for care where a payment agreement exists between the two healthcare entities.

**Description:** Patient Inbound Case Payment Agreement  
**Table type:** ACTIVITY  
**Primary key:** _(not published — see note)_  
**Columns:** 16

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `CARE_TYPE_CD` | DOUBLE | NOT NULL |  | The type of care the patient will be receiving. |
| 2 | `PATIENT_CASE_ID` | DOUBLE | NOT NULL | FK→ | Uniquely identifies a patient's medical problem within a specific period of time across a continuum of care. |
| 3 | `PATIENT_CASE_IN_PMT_AGMT_ID` | DOUBLE | NOT NULL |  | Unique generated number that identifies a single row on the PATIENT_CASE_IN_PMT_AGMT table. |
| 4 | `PAYMENT_CONNECTION_IDENT` | VARCHAR(50) |  |  | The unique identifier of the payment agreement referral from the referring facility to communicate with the receiving facility. |
| 5 | `RECEIVING_CARE_UNIT_ORG_ID` | DOUBLE | NOT NULL | FK→ | This is the value of the unique primary identifier of the ORGANIZATION table. It is an internal system assigned number for the care unit organization that received the referral. |
| 6 | `RECEIVING_FACILITY_ORG_ID` | DOUBLE | NOT NULL | FK→ | This is the value of the unique primary identifier of the ORGANIZATION table. It is an internal system assigned number for the facility organization that received the referral. |
| 7 | `REFERRAL_REASON_CD` | DOUBLE | NOT NULL |  | The reason for the patient referral to a different care provider. |
| 8 | `REFERRING_FACILITY_CD` | DOUBLE | NOT NULL |  | A code that represents the external facility that referred the patient to the receiving facility. |
| 9 | `REFERRING_PROVIDER_NAME` | VARCHAR(100) |  |  | The name of the referring provider. |
| 10 | `SPECIALTY_CD` | DOUBLE | NOT NULL |  | The medical specialty for which the patient is to be seen. |
| 11 | `TYPE_CD` | DOUBLE | NOT NULL |  | The patient Case payment agreement type. |
| 12 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 13 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 14 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 15 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 16 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `PATIENT_CASE_ID` | [PATIENT_CASE](PATIENT_CASE.md) | `PATIENT_CASE_ID` |
| `RECEIVING_CARE_UNIT_ORG_ID` | [ORGANIZATION](ORGANIZATION.md) | `ORGANIZATION_ID` |
| `RECEIVING_FACILITY_ORG_ID` | [ORGANIZATION](ORGANIZATION.md) | `ORGANIZATION_ID` |

