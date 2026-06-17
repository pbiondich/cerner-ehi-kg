# INVTN_INVITATION

> Activity data for the current state of invitations for the new Invitations component

**Description:** INVITATION  
**Table type:** ACTIVITY  
**Primary key:** _(not published — see note)_  
**Columns:** 22

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ACTIVE_IND` | DOUBLE | NOT NULL |  | The table row is active or inactive. A row is generally active unless it is in an inactive state such as logically deleted, combined away, pending purge, etc. |
| 2 | `ASSIGN_DT_TM` | DATETIME |  |  | The date that the invitation was assigned. |
| 3 | `COMMUNICATION_ID` | DOUBLE | NOT NULL | FK→ | This is the foreign key to the invtn_communication table for the latest GENERATED communication for the invitation |
| 4 | `GENERATED_COMM_DT_TM` | DATETIME |  |  | The date/time that the latest GENERATED communication for this invitation was generated. |
| 5 | `INVITATION_ID` | DOUBLE | NOT NULL |  | The unique identifier of the invitation. Primary Key. |
| 6 | `LAST_UPDATED_BY_ID` | DOUBLE | NOT NULL |  | The prsnl id of the last person to update the invitation. |
| 7 | `LAST_UPDATED_DT_TM` | DATETIME |  |  | The date that the invitation was last updated. |
| 8 | `LIST_NAME` | VARCHAR(50) | NOT NULL |  | The list that this invitation applies to for the program. |
| 9 | `PARENT_ENTITY_ID` | DOUBLE | NOT NULL |  | The identifier of the item that the invitation references. |
| 10 | `PARENT_ENTITY_NAME` | VARCHAR(30) | NOT NULL |  | The type of the invitation. This is the table that the invitation references. |
| 11 | `PERSON_ID` | DOUBLE | NOT NULL | FK→ | The ID of the person this invitation is for. Foreign key to the person table. |
| 12 | `PROGRAM_ID` | DOUBLE | NOT NULL | FK→ | The ID of the program this invitation is for. This is the foreign key to the invtn_program table. |
| 13 | `SCHEDULED_COMMUNICATION_ID` | DOUBLE | NOT NULL | FK→ | The foreign key to the invtn_communication table for the latest SCHEDULED communication for the invitation. |
| 14 | `SCHEDULED_COMM_DT_TM` | DATETIME |  |  | The date/time that the latest SCHEDULED communication for this invitation was scheduled. |
| 15 | `SEQ_DT_TM` | DATETIME |  |  | The date that is used for sequencing this invitation in the list it belongs to. |
| 16 | `TRACKING_STATUS_CD` | DOUBLE | NOT NULL |  | The tracking status of the invitation from the choices in code set 66500. |
| 17 | `TRACKING_STATUS_DT_TM` | DATETIME |  |  | The date/time that the Invitation entered the current tracking status. |
| 18 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 19 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 20 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 21 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 22 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `COMMUNICATION_ID` | [INVTN_COMMUNICATION](INVTN_COMMUNICATION.md) | `COMMUNICATION_ID` |
| `PERSON_ID` | [PERSON](PERSON.md) | `PERSON_ID` |
| `PROGRAM_ID` | [INVTN_PROGRAM](INVTN_PROGRAM.md) | `PROGRAM_ID` |
| `SCHEDULED_COMMUNICATION_ID` | [INVTN_COMMUNICATION](INVTN_COMMUNICATION.md) | `COMMUNICATION_ID` |

