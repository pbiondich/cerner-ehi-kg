# SELECTED_RX_FORMULARY

> This table stores a reference to the last manually selected prescription formulary to be used for a patient. A patient can have either a prescription plan or prescription system formulary but not both.

**Description:** Selected RX Formulary  
**Table type:** ACTIVITY  
**Primary key:** _(not published — see note)_  
**Columns:** 15

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ACTIVE_IND` | DOUBLE | NOT NULL |  | The table row is active or inactive. A row is generally active unless it is in an inactive state such as logically deleted, combined away, pending purge, etc. |
| 2 | `ACTIVE_STATUS_CD` | DOUBLE | NOT NULL |  | Indicates the status of the row itself (not the data in the row) such as active, inactive, combined away, pending purge, etc. |
| 3 | `ACTIVE_STATUS_DT_TM` | DATETIME | NOT NULL |  | The date and time that the active_status_cd was set. |
| 4 | `ACTIVE_STATUS_PRSNL_ID` | DOUBLE | NOT NULL |  | The person who caused the active_status_cd to be set or change. |
| 5 | `BEG_EFFECTIVE_DT_TM` | DATETIME |  |  | The date and time for which this table row becomes effective. Normally, this will be the date and time the row is added, but could be a past or future date and time. |
| 6 | `END_EFFECTIVE_DT_TM` | DATETIME |  |  | The date/time after which the row is no longer valid as active current data. This may be valued with the date that the row became inactive. |
| 7 | `PERSON_ID` | DOUBLE | NOT NULL | FK→ | The unique identifier of the patient for the selected formulary or plan. |
| 8 | `PERSON_RX_PLAN_RELTN_ID` | DOUBLE | NOT NULL | FK→ | The unique identifier of the last manually selected prescription plan. This attribute will be 0 if the patient has a selected system formulary instead of a prescription plan. |
| 9 | `SELECTED_RX_FORMULARY_ID` | DOUBLE | NOT NULL |  | This is the value of the unique primary identifier of the Selected_RX_Formulary table. It is an internal system assigned number. |
| 10 | `SYSTEM_RX_FORMULARY_ID` | DOUBLE | NOT NULL | FK→ | The unique identifier of the last manually selected system formulary. This attribute will be 0 if the patient has a prescription plan instead of a selected system formulary. |
| 11 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 12 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 13 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 14 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 15 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `PERSON_ID` | [PERSON](PERSON.md) | `PERSON_ID` |
| `PERSON_RX_PLAN_RELTN_ID` | [PERSON_RX_PLAN_RELTN](PERSON_RX_PLAN_RELTN.md) | `PERSON_RX_PLAN_RELTN_ID` |
| `SYSTEM_RX_FORMULARY_ID` | [SYSTEM_RX_FORMULARY](SYSTEM_RX_FORMULARY.md) | `SYSTEM_RX_FORMULARY_ID` |

