# INVTN_COMMUNICATION

> Includes all communications related to a specific invitation. Stores status and date time information related to the generation and sending or printing of a communication item that is associated with an invitation program for a specific person.

**Description:** INVITATION COMMUNICATION  
**Table type:** ACTIVITY  
**Primary key:** `COMMUNICATION_ID`  
**Columns:** 27  
**Referenced by:** 3 columns

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ACTIVE_IND` | DOUBLE | NOT NULL |  | The table row is active or inactive. A row is generally active unless it is in an inactive state such as logically deleted, combined away, pending purge, etc. |
| 2 | `ACTIVE_STATUS_CD` | DOUBLE | NOT NULL |  | Indicates the status of the row itself (not the data in the row) such as active, inactive, combined away, pending purge, etc. |
| 3 | `ACTIVE_STATUS_DT_TM` | DATETIME | NOT NULL |  | The date and time that the active_status_cd was set. |
| 4 | `ACTIVE_STATUS_PRSNL_ID` | DOUBLE | NOT NULL |  | The person who caused the active_status_cd to be set or change. |
| 5 | `COMMUNICATION_ID` | DOUBLE | NOT NULL | PK | The unique primary key that identifies the communication. |
| 6 | `CONTENT_BLOB_ID` | DOUBLE | NOT NULL | FK→ | The foreign key into the BLOB table. This blob is used to store the content of this communication. |
| 7 | `CONTENT_TYPE_FLAG` | DOUBLE | NOT NULL |  | The type of the blob content. 1=ASCII, 2=Postscript, 3=RTF, 4=PDF |
| 8 | `FAILED_DT_TM` | DATETIME |  |  | The date and time when the communication failed to move to the next status. |
| 9 | `FINAL_TRACKING_STATUS_CD` | DOUBLE | NOT NULL |  | Represents the final tracking status of the invitation. |
| 10 | `GENERATED_DT_TM` | DATETIME |  |  | The point in time when this communication was sent or printed. |
| 11 | `GENERATED_PRSNL_ID` | DOUBLE | NOT NULL |  | The person that generated the communication. This may or may not be the same as the person that sent the communication. |
| 12 | `METHOD_FLAG` | DOUBLE | NOT NULL |  | Determines which method will be used to communicate. Examples: printed letter, IQHealth. |
| 13 | `PERSON_ID` | DOUBLE | NOT NULL | FK→ | The person this communication is associated with. Foreign key into the PERSON table. |
| 14 | `PROGRAM_ID` | DOUBLE | NOT NULL | FK→ | The program this communication is associated with. Foreign key into the INVTN_PROGRAM table. |
| 15 | `REQUESTED_DT_TM` | DATETIME |  |  | The point in time when this communication was requested. |
| 16 | `REQUESTED_PRSNL_ID` | DOUBLE | NOT NULL |  | The person who requested the communication. Communications requested by the system will be zero. Foreign key to the PRSNL table. |
| 17 | `RESENT_DT_TM` | DATETIME |  |  | The point in time when this communication was resent or reprinted. |
| 18 | `RESENT_PRSNL_ID` | DOUBLE | NOT NULL |  | The person who resent or reprinted the communication. Foreign key to the PRSNL table. |
| 19 | `SCHEDULED_DT_TM` | DATETIME |  |  | The point in time when this communication was is scheduled to be generated. |
| 20 | `SENT_DT_TM` | DATETIME |  |  | The point in time when this communication was sent or printed. |
| 21 | `SENT_PRSNL_ID` | DOUBLE | NOT NULL |  | The person who sent or printed the communication. Foreign key to the PRSNL table. |
| 22 | `STATUS_FLAG` | DOUBLE | NOT NULL |  | The current status o the communication item. 1 = Requested, 2 = Scheduled, 3 = Generated, 4 = Sent, 5 = Resent, 6 = Cancelled |
| 23 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 24 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 25 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 26 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 27 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `CONTENT_BLOB_ID` | [LONG_BLOB](LONG_BLOB.md) | `LONG_BLOB_ID` |
| `PERSON_ID` | [PERSON](PERSON.md) | `PERSON_ID` |
| `PROGRAM_ID` | [INVTN_PROGRAM](INVTN_PROGRAM.md) | `PROGRAM_ID` |

## Referenced by (3)

| From table | Column |
|------------|--------|
| [INVTN_INVITATION](INVTN_INVITATION.md) | `COMMUNICATION_ID` |
| [INVTN_INVITATION](INVTN_INVITATION.md) | `SCHEDULED_COMMUNICATION_ID` |
| [INVTN_INVITATION_ACTION](INVTN_INVITATION_ACTION.md) | `COMMUNICATION_ID` |

