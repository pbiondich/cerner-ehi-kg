# INVTN_INVITATION_ACTION

> Stores actions taken on an instance of an invitation. These actions can be composed of either changes in the tracking status, the generation of new communications, or the sending of communications.

**Description:** Invitation Action History  
**Table type:** ACTIVITY  
**Primary key:** _(not published — see note)_  
**Columns:** 17

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ACTION_DT_TM` | DATETIME |  |  | The point in time when this action was taken on the invitation. |
| 2 | `ACTION_FLAG` | DOUBLE | NOT NULL |  | Represents the type of action performed on the invitation. 1 = Tracking Status Change, 2 = Communication Generated, 3 = Communication Sent. |
| 3 | `ACTION_PRSNL_ID` | DOUBLE | NOT NULL |  | The person who performed thee action. Actions performed by the system will be zero. Foreign key to the PRSNL table. |
| 4 | `ACTIVE_IND` | DOUBLE | NOT NULL |  | The table row is active or inactive. A row is generally active unless it is in an inactive state such as logically deleted, combined away, pending purge, etc. |
| 5 | `COMMUNICATION_ID` | DOUBLE | NOT NULL | FK→ | This is the foreign key to the INVTN_COMMUNICATION table for the latest communication regarding this invitation. |
| 6 | `INVITATION_ACTION_ID` | DOUBLE | NOT NULL |  | The unique primary key that identifies the invitation action. |
| 7 | `PERSON_ID` | DOUBLE | NOT NULL | FK→ | The person this communication is associated with. |
| 8 | `PROGRAM_ID` | DOUBLE | NOT NULL | FK→ | Represents the program that contains the invitation associated with this action. This is a foreign key into the INV_PROGRAM table. |
| 9 | `TRACKING_STATUS_CD` | DOUBLE | NOT NULL |  | Represents the current tracking status of the invitation. |
| 10 | `TRACKING_STATUS_DT_TM` | DATETIME |  |  | Status Date and Time for the TRACKING item |
| 11 | `TRIGGER_ENTITY_ID` | DOUBLE | NOT NULL |  | The identifier of the item (identified in TRIGGER_ENTITY_NAME) that triggered this Invitation Action. |
| 12 | `TRIGGER_ENTITY_NAME` | VARCHAR(30) |  |  | The type of the item that triggered this Invitation Action |
| 13 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 14 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 15 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 16 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 17 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `COMMUNICATION_ID` | [INVTN_COMMUNICATION](INVTN_COMMUNICATION.md) | `COMMUNICATION_ID` |
| `PERSON_ID` | [PERSON](PERSON.md) | `PERSON_ID` |
| `PROGRAM_ID` | [INVTN_PROGRAM](INVTN_PROGRAM.md) | `PROGRAM_ID` |

