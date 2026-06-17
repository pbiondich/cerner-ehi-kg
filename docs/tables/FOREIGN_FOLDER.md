# FOREIGN_FOLDER

> The Foreign_Folder table contains information about folders that have been received from outside our system.

**Description:** Foreign Folder  
**Table type:** ACTIVITY  
**Primary key:** `SEQ_OBJECT_ID`  
**Columns:** 12  
**Referenced by:** 1 columns

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `CONTENT_COMMENT` | VARCHAR(255) |  |  | The Content_Comment field contains any general comments about the contents of a foreign folder. |
| 2 | `CUSTODIAN` | VARCHAR(50) |  |  | The Custodian contains a free text entry identifying the person(s) responsible for the foreign folder. |
| 3 | `DUE_DT_TM` | DATETIME |  |  | The Due_Dt_Tm field contains the date and time that the foreign folder should be returned to its origin. |
| 4 | `LENDER_ID` | DOUBLE | NOT NULL |  | The Lender_id is a foreign key to the Borrower_Lender table. It uniquely identifies the lender from which the foreign folder was received. |
| 5 | `PERSON_ID` | DOUBLE | NOT NULL | FK→ | This is the value of the unique primary identifier of the person table. It is an internal system assigned number. |
| 6 | `RECEIVED_DT_TM` | DATETIME |  |  | The Received_Dt_Tm captures the date and time that the foreign folder was received. |
| 7 | `SEQ_OBJECT_ID` | DOUBLE | NOT NULL | PK FK→ | The Seq_Object_Id is a foreign key to the Image_Class table. It serves as a unique identifier for the foreign folder. |
| 8 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 9 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 10 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 11 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 12 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `PERSON_ID` | [PERSON](PERSON.md) | `PERSON_ID` |
| `SEQ_OBJECT_ID` | [IMAGE_CLASS](IMAGE_CLASS.md) | `SEQ_OBJECT_ID` |

## Referenced by (1)

| From table | Column |
|------------|--------|
| [FOREIGN_CONTENT](FOREIGN_CONTENT.md) | `SEQ_OBJECT_ID` |

