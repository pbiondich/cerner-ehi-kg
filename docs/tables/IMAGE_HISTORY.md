# IMAGE_HISTORY

> The Image_History table contains all historical movement for a specific media or exam.

**Description:** Image History  
**Table type:** ACTIVITY  
**Primary key:** _(not published — see note)_  
**Columns:** 21

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ACTION_CD` | DOUBLE | NOT NULL |  | The Action_Cd identifies which action is being recorded for historical purposes. (ex. loaned, transferred, purged, created, etc.) |
| 2 | `ACTION_COMMENTS` | VARCHAR(255) |  |  | The Action_Comments contains general comments about the transaction that is being logged. |
| 3 | `ACTION_DT_TM` | DATETIME | NOT NULL |  | the Action_Dt_Tm field captures the date and time that the action took place. (ex. the date and time that the folder was loaned.) |
| 4 | `ACTION_METHOD_CD` | DOUBLE | NOT NULL |  | The Action_Method_Cd indicates the method of transport for those actions that require the folder/media item to be moved. |
| 5 | `AGENT` | VARCHAR(50) |  |  | The Agent field identifies the person who picked up the folder for a specific borrower. |
| 6 | `FROM_DT_TM` | DATETIME |  |  | The From_Dt_Tm field captures the beginning date and time of a date range. For a loan transaction this would be the date and time that the folder was loaned. |
| 7 | `LOGGED_DT_TM` | DATETIME |  |  | The Logged_Dt_Tm field captures the time that the transaction was entered into the system. |
| 8 | `NBR_COPIES` | DOUBLE |  |  | The Nbr_Copies field is used for the copy action. It indicates how many copies were made of a certain film exam. |
| 9 | `REQUEST_DT_TM` | DATETIME |  |  | The Request_Dt_Tm captures the date and time that a folder/media item was requested. |
| 10 | `REQUEST_PARENT_ID` | DOUBLE | NOT NULL |  | The request_parent_id, along with the request_parent_name, uniquely identify the requestor for the action that was logged in image history. |
| 11 | `REQUEST_PARENT_NAME` | VARCHAR(32) |  |  | The request_parent_name, along with the request_parent_id, uniquely identify the requestor for the action that was logged in image history. |
| 12 | `REQUEST_RETURN_DT_TM` | DATETIME |  |  | The Request_Return_Dt_Tm captures the date and time that a folder/media item was requested to be returned. |
| 13 | `SEQ_OBJECT_ID` | DOUBLE | NOT NULL | FK→ | The Seq_Object_Id is a foreign key to the Trackable_Object table. It uniquely identifies the folder/media item involved with this transaction. |
| 14 | `TRANSACTION_ID` | DOUBLE | NOT NULL | FK→ | The Transaction_Id identifies the person who executed the transaction. This is a foreign key to the Prsnl table. |
| 15 | `TRK_PT_PARENT_ID` | DOUBLE | NOT NULL |  | The trk_pt_parent_id along with the trk_pt_parent_name uniquely identify the tracking point/person/location that last had the folder. |
| 16 | `TRK_PT_PARENT_NAME` | VARCHAR(32) |  |  | The trk_pt_parent_name along with the trk_pt_parent_id uniquely identify the tracking point/person/location that last had the folder. |
| 17 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 18 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 19 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 20 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 21 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `SEQ_OBJECT_ID` | [TRACKABLE_OBJECT](TRACKABLE_OBJECT.md) | `SEQ_OBJECT_ID` |
| `TRANSACTION_ID` | [PRSNL](PRSNL.md) | `PERSON_ID` |

