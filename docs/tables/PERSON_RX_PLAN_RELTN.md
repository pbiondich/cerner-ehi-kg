# PERSON_RX_PLAN_RELTN

> This relation table associates a person to a free text prescription plan or to a prescription plan on the health plan table.

**Description:** Person Prescription Plan Relation  
**Table type:** ACTIVITY  
**Primary key:** `PERSON_RX_PLAN_RELTN_ID`  
**Columns:** 28  
**Referenced by:** 2 columns

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ACTIVE_IND` | DOUBLE | NOT NULL |  | The table row is active or inactive. A row is generally active unless it is in an inactive state such as logically deleted, combined away, pending purge, etc. |
| 2 | `ACTIVE_STATUS_CD` | DOUBLE | NOT NULL |  | Indicates the status of the row itself (not the data in the row) such as active, inactive, combined away, pending purge, etc. |
| 3 | `ACTIVE_STATUS_DT_TM` | DATETIME | NOT NULL |  | The date and time that the active_status_cd was set. |
| 4 | `ACTIVE_STATUS_PRSNL_ID` | DOUBLE | NOT NULL |  | The person who caused the active_status_cd to be set or change. |
| 5 | `BEG_EFFECTIVE_DT_TM` | DATETIME |  |  | The date and time for which this table row becomes effective. Normally, this will be the date and time the row is added, but could be a past or future date and time. |
| 6 | `CARDHOLDER_FIRST_NAME` | VARCHAR(80) |  |  | The first name of the card holder for the prescription plan. |
| 7 | `CARDHOLDER_IDENT` | VARCHAR(50) |  |  | The prescription plan ID that is on the prescription plan card. |
| 8 | `CARDHOLDER_LAST_NAME` | VARCHAR(80) |  |  | The last name of the card holder for the prescription plan. |
| 9 | `CONTRIBUTOR_SYSTEM_CD` | DOUBLE | NOT NULL |  | Contributor system identifies the source feed of data from which a row was populated. This is mainly used to determine how to update a set of data that may have originated from more than one source feed. |
| 10 | `DATA_BUILD_FLAG` | DOUBLE | NOT NULL |  | Indicates how the data for this plan was loaded into this table. 0 - No Plan, 1 - Upload, 2 - RX Hub, 3 - Manual, 4 - System |
| 11 | `END_EFFECTIVE_DT_TM` | DATETIME |  |  | The date/time after which the row is no longer valid as active current data. This may be valued with the date that the row became inactive. |
| 12 | `HEALTH_PLAN_ID` | DOUBLE | NOT NULL | FK→ | The identifier of the health plan this person's prescription plan is related to. |
| 13 | `INTERCHANGE_ID` | DOUBLE | NOT NULL |  | This is the ID of the interchange message that this person's prescription plan is associated with. |
| 14 | `INTERCHANGE_SEQ` | DOUBLE | NOT NULL |  | This is used to uniquely identify the prescription plan inside the interchange message since multiple plans can come back in one message. |
| 15 | `PATIENT_UNIT_NUMBER` | VARCHAR(30) |  |  | A subset of the cardholder_identifier which is appended to the end of the cardholder_identifier for non-unique dependants of the card holder. |
| 16 | `PERSON_ID` | DOUBLE | NOT NULL | FK→ | The identifier of the person related to the prescription plan. |
| 17 | `PERSON_RX_PLAN_RELTN_ID` | DOUBLE | NOT NULL | PK | The unique identifier of the Person_RX_Plan_Reltn table. |
| 18 | `PRIORITY_SEQ` | DOUBLE | NOT NULL |  | Used to order the prescription plans by priority. |
| 19 | `RX_PLAN_BEG_DT_TM` | DATETIME |  |  | The date when the presecription plan becomes effective. |
| 20 | `RX_PLAN_END_DT_TM` | DATETIME |  |  | The date when the presecription plan becomes ineffective. |
| 21 | `TRANS_DT_TM` | DATETIME |  |  | The date/time the eligibility information was obtained. |
| 22 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 23 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 24 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 25 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 26 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |
| 27 | `VERIFIED_BY_ID` | DOUBLE | NOT NULL | FK→ | The personnel ID of the last person who verified the prescription plan coverage (note: this can be different than the updt_user_id which would be the last person who updated this row) |
| 28 | `VERIFIED_DT_TM` | DATETIME |  |  | The date/time the prescription plan was verified. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `HEALTH_PLAN_ID` | [HEALTH_PLAN](HEALTH_PLAN.md) | `HEALTH_PLAN_ID` |
| `PERSON_ID` | [PERSON](PERSON.md) | `PERSON_ID` |
| `VERIFIED_BY_ID` | [PRSNL](PRSNL.md) | `PERSON_ID` |

## Referenced by (2)

| From table | Column |
|------------|--------|
| [PERSON_RX_PLAN_COVERAGE](PERSON_RX_PLAN_COVERAGE.md) | `PERSON_RX_PLAN_RELTN_ID` |
| [SELECTED_RX_FORMULARY](SELECTED_RX_FORMULARY.md) | `PERSON_RX_PLAN_RELTN_ID` |

