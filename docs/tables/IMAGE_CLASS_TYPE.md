# IMAGE_CLASS_TYPE

> The Image_Class_Type table contains information about all of the different folder/media types within the image management system.

**Description:** Image Class Type  
**Table type:** REFERENCE  
**Primary key:** `IMAGE_CLASS_TYPE_CD`  
**Columns:** 19  
**Referenced by:** 3 columns

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ACTIVE_IND` | DOUBLE |  |  | The table row is active or inactive. A row is generally active unless it is in an inactive state such as logically deleted, combined away, pending purge, etc. |
| 2 | `BEG_EFFECTIVE_DT_TM` | DATETIME | NOT NULL |  | The date and time for which this table row becomes effective. Normally, this will be the date and time the row is added, but could be a past or future date and time. |
| 3 | `CONTENT_LABEL_CNT` | DOUBLE |  |  | Identifies the number of Content Labels to be created. |
| 4 | `CREATE_BY_ACC_IND` | DOUBLE |  |  | This column indicates if a certain folder type should be created by accession. |
| 5 | `DEFAULT_RETURN_LOCN_CD` | DOUBLE | NOT NULL | FK→ | The Default_Return_Locn_Cd is a foreign key to the Track_Pt_Library table. This uniquely identifies the library that should be used as a home location when creating a new folder/media item of this certain type. |
| 6 | `DEFAULT_TRACKING_POINT_CD` | DOUBLE | NOT NULL | FK→ | The Default_Tracking_Point_Cd is a foreign key to the Track_Pt_Library table. This uniquely identifies the library/tracking point that should be used as a current location when creating a new folder/media item of this certain type. |
| 7 | `END_EFFECTIVE_DT_TM` | DATETIME | NOT NULL |  | The date/time after which the row is no longer valid as active current data. This may be valued with the date that the row became inactive. |
| 8 | `IMAGE_CLASS_TYPE_CD` | DOUBLE | NOT NULL | PK FK→ | The Image_Class_Type_Cd uniquely identifies a row within the Image_Class_Type table. It has no other meaning or purpose other than to serve as a unique id. |
| 9 | `LABEL_CNT` | DOUBLE |  |  | The Label_Cnt specifies the number of labels that should print when a folder/media item of this type is created. |
| 10 | `LIB_GROUP_CD` | DOUBLE | NOT NULL | FK→ | The Lib_Group_Cd is a foreign key to the Library_Group table. It identifies which library group the folder/media type belongs to. |
| 11 | `LOANABLE_IND` | DOUBLE |  |  | The Loanable_Ind indicates if the folders and or media items of this certain type can be loaned. |
| 12 | `MAX_EXAMS` | DOUBLE |  |  | The Max_Exams indicates the maximum number of exams that can be stored within a folder/media item of this type. |
| 13 | `PARENT_IMAGE_CLASS_TYPE_CD` | DOUBLE | NOT NULL | FK→ | The Parent_Image_Class_Type_Cd allows for a hierarchical structure among folder types. It contains the parent folder type for a specified folder. |
| 14 | `STORE_EXAMS_IND` | DOUBLE |  |  | The Stores_Exams_Ind indicates whether or not a folder should store exams. |
| 15 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 16 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 17 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 18 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 19 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `DEFAULT_RETURN_LOCN_CD` | [SERVICE_RESOURCE](SERVICE_RESOURCE.md) | `SERVICE_RESOURCE_CD` |
| `DEFAULT_TRACKING_POINT_CD` | [SERVICE_RESOURCE](SERVICE_RESOURCE.md) | `SERVICE_RESOURCE_CD` |
| `IMAGE_CLASS_TYPE_CD` | [CODE_VALUE](CODE_VALUE.md) | `CODE_VALUE` |
| `LIB_GROUP_CD` | [SERVICE_RESOURCE](SERVICE_RESOURCE.md) | `SERVICE_RESOURCE_CD` |
| `PARENT_IMAGE_CLASS_TYPE_CD` | [IMAGE_CLASS_TYPE](IMAGE_CLASS_TYPE.md) | `IMAGE_CLASS_TYPE_CD` |

## Referenced by (3)

| From table | Column |
|------------|--------|
| [IMAGE_CLASS](IMAGE_CLASS.md) | `IMAGE_CLASS_TYPE_CD` |
| [IMAGE_CLASS_TYPE](IMAGE_CLASS_TYPE.md) | `PARENT_IMAGE_CLASS_TYPE_CD` |
| [TRANS_FOLD_EXCLUSIONS](TRANS_FOLD_EXCLUSIONS.md) | `IMAGE_CLASS_TYPE_CD` |

