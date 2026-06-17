# PERSON_PORTAL_INVITE

> Stores information relating to a person's portal enrollment invitation.

**Description:** Person Portal Invite  
**Table type:** ACTIVITY  
**Primary key:** `PERSON_PORTAL_INVITE_ID`  
**Columns:** 16  
**Referenced by:** 1 columns

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ACTIVE_IND` | DOUBLE | NOT NULL |  | The table row is active or inactive. A row is generally active unless it is in an inactive state such as logically deleted, combined away, pending purge, etc. |
| 2 | `ACTIVE_STATUS_CD` | DOUBLE | NOT NULL |  | Indicates the status of the row itself (not the data in the row) such as active, inactive, combined away, pending purge, etc. |
| 3 | `ACTIVE_STATUS_DT_TM` | DATETIME | NOT NULL |  | The date and time that the active_status_cd was set. |
| 4 | `ACTIVE_STATUS_PRSNL_ID` | DOUBLE | NOT NULL |  | The person who caused the active_status_cd to be set or change. |
| 5 | `CHALLENGE_ANSWER_TXT` | VARCHAR(50) |  |  | The answer to the challenge question selected by the patient or (authorized-patient representative). The challenge question paired with the answer is used for authenticating their identify when the invitation is claimed. |
| 6 | `CHALLENGE_QUESTION_CD` | DOUBLE | NOT NULL |  | The question selected by the patient or (authorized-patient representative) paired with the challenge answer for authenticating their identity when the invitation is claimed. |
| 7 | `ERROR_REASON_CD` | DOUBLE | NOT NULL |  | Information describing the reason that the attempt to send an invitation to the person was not successful. |
| 8 | `INVITE_STATUS_CD` | DOUBLE | NOT NULL |  | The status of the person's portal invitation (i.e., sent, sending, error, self-enrolled) |
| 9 | `PATIENT_PERSON_ID` | DOUBLE | NOT NULL | FK→ | This is the value of the unique primary identifier of the person table. It is an internal system assigned number. |
| 10 | `PERSON_ID` | DOUBLE | NOT NULL | FK→ | This is the value of the unique primary identifier of the person table. It is an internal system assigned number. |
| 11 | `PERSON_PORTAL_INVITE_ID` | DOUBLE | NOT NULL | PK | This is the value of the unique primary identifier of the person_portal_invite table. It is an internal system assigned number. |
| 12 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 13 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 14 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 15 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 16 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `PATIENT_PERSON_ID` | [PERSON](PERSON.md) | `PERSON_ID` |
| `PERSON_ID` | [PERSON](PERSON.md) | `PERSON_ID` |

## Referenced by (1)

| From table | Column |
|------------|--------|
| [PERSON_PORTAL_INVITE_HIST](PERSON_PORTAL_INVITE_HIST.md) | `PERSON_PORTAL_INVITE_ID` |

