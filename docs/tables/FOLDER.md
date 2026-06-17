# FOLDER

> The Folder table contains info about a patients image management folder.

**Description:** Folder  
**Table type:** ACTIVITY  
**Primary key:** `SEQ_OBJECT_ID`  
**Columns:** 9  
**Referenced by:** 2 columns

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `OLD_CERNER_NUMBER` | VARCHAR(50) |  |  | The Old_Cerner_Number contains the folders unique identifier from a previous Cerner system. |
| 2 | `PARENT_OBJECT_ID` | DOUBLE | NOT NULL | FK→ | The Parent_Object_Id identifies the folder that the current folder resides in. This allows for a hierarchical structure among folders. |
| 3 | `PERSON_ID` | DOUBLE | NOT NULL | FK→ | This is the value of the unique primary identifier of the person table. It is an internal system assigned number. |
| 4 | `SEQ_OBJECT_ID` | DOUBLE | NOT NULL | PK FK→ | The Seq_Object_Id is a foreign key to the Image_Class table. This uniquely identifies a folder within the image management area. |
| 5 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 6 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 7 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 8 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 9 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `PARENT_OBJECT_ID` | [FOLDER](FOLDER.md) | `SEQ_OBJECT_ID` |
| `PERSON_ID` | [PERSON](PERSON.md) | `PERSON_ID` |
| `SEQ_OBJECT_ID` | [IMAGE_CLASS](IMAGE_CLASS.md) | `SEQ_OBJECT_ID` |

## Referenced by (2)

| From table | Column |
|------------|--------|
| [FILM_EXAM](FILM_EXAM.md) | `FOLDER_ID` |
| [FOLDER](FOLDER.md) | `PARENT_OBJECT_ID` |

