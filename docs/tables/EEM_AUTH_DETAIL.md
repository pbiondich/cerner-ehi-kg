# EEM_AUTH_DETAIL

> The EEM_AUTH_DETAIL table stores detailed information pertaining to a single X12 278 Service Review transaction submitted as it was submitted for a given patient.

**Description:** EEM Authorization Detail  
**Table type:** ACTIVITY  
**Primary key:** _(not published — see note)_  
**Columns:** 20

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `DEP_NAME_FIRST` | VARCHAR(35) |  |  | This is the first name of the dependent as submitted on the outbound 278 transaction if the patient is not the subscriber. If the patient is the subscriber, this attribute will not be populated. |
| 2 | `DEP_NAME_LAST` | VARCHAR(60) |  |  | This is the last name of the dependent as submitted on the outbound 278 transaction if the patient is not the subscriber. If the patient is the subscriber, this attribute will not be populated. |
| 3 | `DEP_PERSON_ID` | DOUBLE | NOT NULL | FK→ | This is the person identifier of the dependent used for submitting the outbound 278 transaction if the patient is not the subscriber. If the patient is the subscriber, this attribute will not be populated. |
| 4 | `ENCOUNTER_ID` | DOUBLE | NOT NULL | FK→ | The ID of the encounter associated with this transaction. |
| 5 | `HEALTH_PLAN_ID` | DOUBLE | NOT NULL | FK→ | The ID of the health plan associated with the payer for the transaction. |
| 6 | `INTERCHANGE_ID` | DOUBLE | NOT NULL |  | A unique transaction identifier. |
| 7 | `PAYER_ID` | DOUBLE | NOT NULL | FK→ | UNIQUE identifier OF the organization that IS the payer/UMO FOR the TRANSACTION |
| 8 | `PROFILE_ID` | DOUBLE | NOT NULL | FK→ | UNIQUE identifier FOR the TRANSACTION PROFILE |
| 9 | `REPLY_DT_TM` | DATETIME |  |  | This IS the DATE AND TIME the TRANSACTION was last received |
| 10 | `SENDER_PRSNL_ID` | DOUBLE | NOT NULL | FK→ | UNIQUE identifier OF the person who IS the sender OF the TRANSACTION |
| 11 | `SENT_DT_TM` | DATETIME | NOT NULL |  | This IS the DATE AND TIME the TRANSACTION was originally sent |
| 12 | `SUB_MEMBER_IDEN` | VARCHAR(80) |  |  | This is the subscriber's member identifier for their health plan as submitted on the outbound 278 transaction. |
| 13 | `SUB_NAME_FIRST` | VARCHAR(35) |  |  | The subscriber?s first name |
| 14 | `SUB_NAME_LAST` | VARCHAR(60) |  |  | The subscriber?s last name |
| 15 | `SUB_PERSON_ID` | DOUBLE | NOT NULL | FK→ | UNIQUE identifier OF the person who IS the subscriber |
| 16 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 17 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 18 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 19 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 20 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `DEP_PERSON_ID` | [PERSON](PERSON.md) | `PERSON_ID` |
| `ENCOUNTER_ID` | [ENCOUNTER](ENCOUNTER.md) | `ENCNTR_ID` |
| `HEALTH_PLAN_ID` | [HEALTH_PLAN](HEALTH_PLAN.md) | `HEALTH_PLAN_ID` |
| `PAYER_ID` | [ORGANIZATION](ORGANIZATION.md) | `ORGANIZATION_ID` |
| `PROFILE_ID` | [EEM_PROFILE](EEM_PROFILE.md) | `PROFILE_ID` |
| `SENDER_PRSNL_ID` | [PRSNL](PRSNL.md) | `PERSON_ID` |
| `SUB_PERSON_ID` | [PERSON](PERSON.md) | `PERSON_ID` |

