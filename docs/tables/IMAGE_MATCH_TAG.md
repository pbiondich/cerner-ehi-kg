# IMAGE_MATCH_TAG

> Image Match Tag

**Description:** This table contains all DICOM tags that relate to Image Management  
**Table type:** REFERENCE  
**Primary key:** `TAG`  
**Columns:** 13  
**Referenced by:** 4 columns

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `AUTO_MATCH_IND` | DOUBLE |  |  | This column indicates if a specific DICOM tag is to be considered for Auto Matching. |
| 2 | `AUTO_MATCH_REQ_IND` | DOUBLE |  |  | This column indicates if the DICOM tag is required for Auto Matching. |
| 3 | `DATA_TYPE` | VARCHAR(2) |  |  | This column specifies the data type of the DICOM tag. |
| 4 | `DESCRIPTION` | VARCHAR(64) | NOT NULL |  | This column contains the description of the DICOM tag. |
| 5 | `TAG` | VARCHAR(11) | NOT NULL | PK | This column contains the actual DICOM tag. |
| 6 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 7 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 8 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 9 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 10 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |
| 11 | `UPD_IMAGE_HDR_IND` | DOUBLE |  |  | This column indicates if the DICOM tag is to be considered for update of the image header. |
| 12 | `UPD_IMAGE_HDR_REQ_IND` | DOUBLE |  |  | This column indicates if the DICOM tag is required for update of the image header. |
| 13 | `VALUE_MULTIPLICITY` | DOUBLE |  |  | This column specifies if and how many occurrences of a specific DICOM tag is possible. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Referenced by (4)

| From table | Column |
|------------|--------|
| [AUTO_MATCH_DEFINITION](AUTO_MATCH_DEFINITION.md) | `IMAGE_TAG` |
| [AUTO_MATCH_DEFINITION](AUTO_MATCH_DEFINITION.md) | `RIS_TAG` |
| [IM_IGNORE_DEFINITION](IM_IGNORE_DEFINITION.md) | `IGNORE_TAG_TXT` |
| [UPD_IMAGE_HDR_DEF](UPD_IMAGE_HDR_DEF.md) | `TAG` |

