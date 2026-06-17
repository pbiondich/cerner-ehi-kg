# LIBRARY_GROUP

> The Library_Group table is a child of the service_resource table and contains information specific to the library groups which are a part of the image management area.

**Description:** Library Group  
**Table type:** REFERENCE  
**Primary key:** `SERVICE_RESOURCE_CD`  
**Columns:** 11  
**Referenced by:** 3 columns

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `CHK_DIFF_BORR_IND` | DOUBLE |  |  | The Chk_Diff_Borr_Ind indicates whether or not the system should look to see if any subordinate folders are checked out to a different borrower when a folder is being returned from a loan. |
| 2 | `DAILY_FOLDER_IND` | DOUBLE |  |  | The Daily_Folder_Ind indicates if a new folder should be generated each day that a patient has an exam performed. |
| 3 | `FOLDER_NBR_FORMAT_CD` | DOUBLE | NOT NULL |  | The Folder_Nbr_Format_Cd identifies the folder number format that is used within this library group. (ex. med rec, soc sec, etc.) |
| 4 | `RETURN_LOC_FLAG` | DOUBLE |  |  | The Return_Loc_Flag indicates which of the default locations to use when a folder is being returned. |
| 5 | `SERVICE_RESOURCE_CD` | DOUBLE | NOT NULL | PK FK→ | The Service_Resource_Cd is a foreign key to the Service_Resource table. This serves as a unique identifier for the library group. |
| 6 | `UNREAD_FILMS_IND` | DOUBLE |  |  | The Unread_Films_Ind indicates whether or not an unread film should be able to be loaned. This is controlled at the library group level. |
| 7 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 8 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 9 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 10 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 11 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `SERVICE_RESOURCE_CD` | [SERVICE_RESOURCE](SERVICE_RESOURCE.md) | `SERVICE_RESOURCE_CD` |

## Referenced by (3)

| From table | Column |
|------------|--------|
| [EXAM_ROOM_LIB_GRP_RELTN](EXAM_ROOM_LIB_GRP_RELTN.md) | `LIB_GROUP_CD` |
| [LIB_GRP_RELTN](LIB_GRP_RELTN.md) | `LIB_GROUP_CD` |
| [LIB_GRP_RELTN](LIB_GRP_RELTN.md) | `SERVICE_RESOURCE_CD` |

