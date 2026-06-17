# CE_BLOB_RESULT

> The ce_blob_result table contains information about documents. Each ce_blob_result record corresponds to a single physical document. Blob results having a common {event_id, contributor_system_cd, series_ref_nbr} constitute a logical document

**Description:** ce blob result  
**Table type:** ACTIVITY  
**Primary key:** _(not published — see note)_  
**Columns:** 18

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `BLOB_ATTRIBUTES` | VARCHAR(255) |  |  | Attributes of remote blob: display rotation angle; display enhancement options (anti-aliasing, color enhancement, etc.) |
| 2 | `BLOB_HANDLE` | VARCHAR(2000) |  |  | Handle to remote blob |
| 3 | `CHECKSUM` | DOUBLE | NOT NULL |  | A unique value, created by parsing the contents of the blob, used as a comparison to identify changes to the blob. |
| 4 | `DEVICE_CD` | DOUBLE |  |  | Describes device which captured image |
| 5 | `EVENT_ID` | DOUBLE | NOT NULL |  | This value comes from an EVENT_ID in the CINICAL_EVENT Table. It may not equate to a primary key in CLIICAL_EVENT |
| 6 | `FORMAT_CD` | DOUBLE | NOT NULL |  | Identifies the type of blob |
| 7 | `MAX_SEQUENCE_NBR` | DOUBLE | NOT NULL |  | Number of blobs and/or remote blobs associated with the blob result. |
| 8 | `STORAGE_CD` | DOUBLE | NOT NULL |  | Identifies location/device where blob is stored. For example, Blob Table, Dictation System, Image Server, HSM, etc. |
| 9 | `SUB_SERIES_REF_NBR` | VARCHAR(60) |  |  | Used to qualify sub-groups of blobs within a Series. |
| 10 | `SUCCESSION_TYPE_CD` | DOUBLE | NOT NULL |  | Indicates how blobs replace/succeed other blobs. |
| 11 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 12 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 13 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 14 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 15 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 16 | `VALID_FROM_DT_TM` | DATETIME | NOT NULL |  | Contains the Beginning Point of when a row in the table is valid. |
| 17 | `VALID_UNTIL_DT_TM` | DATETIME | NOT NULL |  | Contains the "End Point" of when a row in the table is valid. Current version of the result has an open "Until Dt Tm" value. We need to determine what that value is. |
| 18 | `VERSION_NBR` | DOUBLE |  |  | Allows an external system to specify the version which it is attempting to update. If zero, no version checking is done. If non-zero, ensure must match version_nbr on update. version_nbr+1 is written to db. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

