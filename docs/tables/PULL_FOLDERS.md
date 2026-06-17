# PULL_FOLDERS

> The Pull_Folders table contains a list of folders that qualified to be transferred as a part of a transfer pull list.

**Description:** Pull Folders  
**Table type:** ACTIVITY  
**Primary key:** _(not published — see note)_  
**Columns:** 9

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `PERSON_ID` | DOUBLE | NOT NULL | FK→ | This is the value of the unique primary identifier of the person table. It is an internal system assigned number. |
| 2 | `PULL_FOLDER_ID` | DOUBLE | NOT NULL |  | The Pull_Folder_Id uniquely identifies a row within the Pull_Folders table. This field serves no purpose other than to uniquely identify the row. |
| 3 | `PULL_LIST_ID` | DOUBLE | NOT NULL | FK→ | The Pull_List_Id is a foreign key to the Pull_List table. It identifies which pull list this specific folder is a part of. |
| 4 | `SEQ_OBJECT_ID` | DOUBLE | NOT NULL | FK→ | The Seq_Object_Id is a foreign key to the Trackable_Object table. This is used to identify the folder that is to be pulled as a part of this pull list. |
| 5 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 6 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 7 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 8 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 9 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `PERSON_ID` | [PERSON](PERSON.md) | `PERSON_ID` |
| `PULL_LIST_ID` | [PULL_TRANS_REQ](PULL_TRANS_REQ.md) | `PULL_LIST_ID` |
| `SEQ_OBJECT_ID` | [TRACKABLE_OBJECT](TRACKABLE_OBJECT.md) | `SEQ_OBJECT_ID` |

