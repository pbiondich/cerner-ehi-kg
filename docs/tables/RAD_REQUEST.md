# RAD_REQUEST

> The Rad_Request table contains information about requests that have been made for films/folders within the image management area.

**Description:** Rad Request  
**Table type:** ACTIVITY  
**Primary key:** `RAD_REQUEST_ID`  
**Columns:** 17  
**Referenced by:** 1 columns

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `CONTACTED_DT_TM` | DATETIME |  |  | The Contacted_Dt_Tm captures the date and time that the lender was contacted concerning the request. |
| 2 | `LENDER_ID` | DOUBLE | NOT NULL | FK→ | The Lender_Id is a foreign key to the Borrower_Lender table. It identifies the Lender that has received the request. |
| 3 | `LOGGED_DT_TM` | DATETIME |  |  | The Logged_Dt_Tm captures the date and time that the request was logged into the system. |
| 4 | `PARENT_ENTITY_ID` | DOUBLE | NOT NULL |  | The Parent_Entity_Id along with the Parent_Entity_Name identifies the person or place that has entered the request. |
| 5 | `PARENT_ENTITY_NAME` | VARCHAR(32) |  |  | The Parent_Entity_Name along with the Parent_Entity_Id identifies the person or place that has entered the request. |
| 6 | `PERSON_ID` | DOUBLE | NOT NULL | FK→ | This is the value of the unique primary identifier of the person table. It is an internal system assigned number. |
| 7 | `RAD_REQUEST_ID` | DOUBLE | NOT NULL | PK | the Rad_Request_Id uniquely identifies a row in the Rad_Request table. It serves no other purpose other than to uniquely identify a row. |
| 8 | `REQUEST_COMMENT` | VARCHAR(255) |  |  | the Request_Comment field contains any general comments about the request. |
| 9 | `REQUEST_DT_TM` | DATETIME |  |  | The Request_Dt_Tm contains the date and time that the films/folders have been requested for. |
| 10 | `REQUEST_PRIORITY_CD` | DOUBLE | NOT NULL |  | The Request_Priority_Cd identifies the priority of the request. |
| 11 | `REQUEST_REASON` | VARCHAR(255) |  |  | The Request_Reason contains the reason that the film/folders are needed. |
| 12 | `SEQ_OBJECT_ID` | DOUBLE | NOT NULL | FK→ | The Seq_Object_Id is a foreign key to the Trackable_Object table. It identifies the folder that has been requested. |
| 13 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 14 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 15 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 16 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 17 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `LENDER_ID` | [BORROWER_LENDER](BORROWER_LENDER.md) | `BORROWER_LENDER_ID` |
| `PERSON_ID` | [PERSON](PERSON.md) | `PERSON_ID` |
| `SEQ_OBJECT_ID` | [TRACKABLE_OBJECT](TRACKABLE_OBJECT.md) | `SEQ_OBJECT_ID` |

## Referenced by (1)

| From table | Column |
|------------|--------|
| [RAD_FOREIGN_REQ_ITEMS](RAD_FOREIGN_REQ_ITEMS.md) | `RAD_REQUEST_ID` |

