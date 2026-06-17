# TRACKING_CHECKIN

> Tracking table used to log when a tracking item is checked into a tracking group. Any tracking group specific fields are also strored in this table.

**Description:** Tracking Checkin Table  
**Table type:** ACTIVITY  
**Primary key:** _(not published — see note)_  
**Columns:** 34

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ACTIVE_IND` | DOUBLE |  |  | The table row is active or inactive. A row is generally active unless it is in an inactive state such as logically deleted, combined away, pending purge, etc. |
| 2 | `ACUITY_LEVEL_ID` | DOUBLE | NOT NULL | FK→ | Patient Acuity Level used to identify how serious the injuries and how soon treatment must be provided. |
| 3 | `CHECKIN_DT_TM` | DATETIME |  |  | Date and time the tracking item was checked into the tracking group. |
| 4 | `CHECKIN_ID` | DOUBLE | NOT NULL | FK→ | ID of the person who checked the tracking item into the tracking group. |
| 5 | `CHECKOUT_DISPOSITION_CD` | DOUBLE | NOT NULL |  | Disposition at checkout time |
| 6 | `CHECKOUT_DT_TM` | DATETIME |  |  | Date and time the tracking item was checked out of the tracking group. |
| 7 | `CHECKOUT_ID` | DOUBLE | NOT NULL | FK→ | ID of the person who checked the tracking item out of the tracking group. |
| 8 | `DEPART_ACUITY_LEVEL_ID` | DOUBLE | NOT NULL | FK→ | Final acuity level assigned at time of departure. |
| 9 | `DOCUMENT_STATUS_CD` | DOUBLE | NOT NULL |  | Tracking Document StatusColumn |
| 10 | `FAMILY_PRESENT_CD` | DOUBLE | NOT NULL | FK→ | Family Present Code used to identify if the family of the patient is here or on their way to see the patient. |
| 11 | `PARENT_ENTITY_ID` | DOUBLE | NOT NULL |  | Table identifier for the Parent Entity Name table.Column |
| 12 | `PARENT_ENTITY_NAME` | VARCHAR(20) |  |  | Table name identifier for the Parent Entity Id.Column |
| 13 | `PAT_ED_ACKNOWLEDGED_IND` | DOUBLE |  |  | Indicator that the patient acknowledged understanding the instructions during th |
| 14 | `PAT_ED_ACKNOWLEDGED_USER_ID` | DOUBLE | NOT NULL | FK→ | This is the user_id of the PRSNL who last logged the Patient Acknowledged Indicator User IND. |
| 15 | `PRIMARY_DOC_ID` | DOUBLE | NOT NULL | FK→ | ID of the Primary Physician who is to see the Patient. |
| 16 | `PRIMARY_NURSE_ID` | DOUBLE | NOT NULL | FK→ | ID of the Primary Nurse who is to see the Patient. |
| 17 | `RANK_SEQUENCE` | DOUBLE |  |  | Rank sequence used to identify which patient is to be seen next. |
| 18 | `REACTIVATE_USER_ID` | DOUBLE | NOT NULL |  | The person id of the user that reactivated a patientColumn |
| 19 | `REACTIVATION_DT_TM` | DATETIME |  |  | Date and time when a patient was reactivatedColumn |
| 20 | `REGISTRATION_STATUS_ID` | DOUBLE | NOT NULL | FK→ | Registration status code used to identify the status of the patient registration. |
| 21 | `SECONDARY_DOC_ID` | DOUBLE | NOT NULL | FK→ | ID of the Secondary Physician who is to see the Patient. |
| 22 | `SECONDARY_NURSE_ID` | DOUBLE | NOT NULL | FK→ | ID of the Secondary Nurse who is to see the Patient. |
| 23 | `SPECIALTY_ID` | DOUBLE | NOT NULL | FK→ | Specialty code used to identify and categorize patient problems. |
| 24 | `TEAM_ID` | DOUBLE | NOT NULL | FK→ | Team code of which team is assigned to attend to the patient. |
| 25 | `TRACKING_CHECKIN_ID` | DOUBLE | NOT NULL |  | Tracking Checkin Identifier |
| 26 | `TRACKING_EVENT_TYPE_CD` | DOUBLE | NOT NULL | FK→ | Tracking Event Type Code |
| 27 | `TRACKING_GROUP_CD` | DOUBLE | NOT NULL | FK→ | Tracking Group Code used to identify which tracking group this patient is currently checked into. |
| 28 | `TRACKING_ID` | DOUBLE | NOT NULL | FK→ | Tracking ItemColumn |
| 29 | `TRAUMA_IND` | DOUBLE |  |  | Defines the patient is trauma or notColumn |
| 30 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 31 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 32 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 33 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 34 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `ACUITY_LEVEL_ID` | [TRACK_REFERENCE](TRACK_REFERENCE.md) | `TRACKING_REF_ID` |
| `CHECKIN_ID` | [PRSNL](PRSNL.md) | `PERSON_ID` |
| `CHECKOUT_ID` | [PRSNL](PRSNL.md) | `PERSON_ID` |
| `DEPART_ACUITY_LEVEL_ID` | [TRACK_REFERENCE](TRACK_REFERENCE.md) | `TRACKING_REF_ID` |
| `FAMILY_PRESENT_CD` | [CODE_VALUE](CODE_VALUE.md) | `CODE_VALUE` |
| `PAT_ED_ACKNOWLEDGED_USER_ID` | [PRSNL](PRSNL.md) | `PERSON_ID` |
| `PRIMARY_DOC_ID` | [PRSNL](PRSNL.md) | `PERSON_ID` |
| `PRIMARY_NURSE_ID` | [PRSNL](PRSNL.md) | `PERSON_ID` |
| `REGISTRATION_STATUS_ID` | [TRACK_REFERENCE](TRACK_REFERENCE.md) | `TRACKING_REF_ID` |
| `SECONDARY_DOC_ID` | [PRSNL](PRSNL.md) | `PERSON_ID` |
| `SECONDARY_NURSE_ID` | [PRSNL](PRSNL.md) | `PERSON_ID` |
| `SPECIALTY_ID` | [TRACK_REFERENCE](TRACK_REFERENCE.md) | `TRACKING_REF_ID` |
| `TEAM_ID` | [TRACK_REFERENCE](TRACK_REFERENCE.md) | `TRACKING_REF_ID` |
| `TRACKING_EVENT_TYPE_CD` | [CODE_VALUE](CODE_VALUE.md) | `CODE_VALUE` |
| `TRACKING_GROUP_CD` | [CODE_VALUE](CODE_VALUE.md) | `CODE_VALUE` |
| `TRACKING_ID` | [TRACKING_ITEM](TRACKING_ITEM.md) | `TRACKING_ID` |

