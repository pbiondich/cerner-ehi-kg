# EXAM_FOLDER

> The Exam_Folder table establishes relationships between orders and image management. It indicates which folders/media an ordered procedure can load to.

**Description:** Exam Folder  
**Table type:** REFERENCE  
**Primary key:** _(not published — see note)_  
**Columns:** 9

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `CATALOG_CD` | DOUBLE | NOT NULL | FK→ | The Catalog_Cd is a foreign key to the Order_Catalog table. This identifies a certain orderable procedure. |
| 2 | `IMAGE_CLASS_TYPE_CD` | DOUBLE | NOT NULL |  | The Image_Class_Type_Cd is a foreign key to the Image_Class_Type table. This identifies a folder type that the exam should load to. |
| 3 | `LIB_GROUP_CD` | DOUBLE | NOT NULL | FK→ | The Lib_Group_Cd is a foreign key to the Library Group table. This identifies the library group related to the image class type. |
| 4 | `REQUIRED_IND` | DOUBLE |  |  | The Required_Ind field indicates which folder types are required and which folder types are alternate folder types or media. |
| 5 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 6 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 7 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 8 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 9 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `CATALOG_CD` | [SERVICE_DIRECTORY](SERVICE_DIRECTORY.md) | `CATALOG_CD` |
| `LIB_GROUP_CD` | [SERVICE_RESOURCE](SERVICE_RESOURCE.md) | `SERVICE_RESOURCE_CD` |

