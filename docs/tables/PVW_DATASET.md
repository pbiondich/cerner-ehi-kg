# PVW_DATASET

> DATESET FOR DICOM STANDARD. UIDS are stored. Indicates archiving solution/location.

**Description:** Contains DICOM SOP UIDS including archiving information.  
**Table type:** ACTIVITY  
**Primary key:** _(not published — see note)_  
**Columns:** 15

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ARCHIVE_CD` | DOUBLE | NOT NULL |  | Identifies the archive soulution available |
| 2 | `ARCHIVE_LOC_CD` | DOUBLE | NOT NULL |  | Multiple Storage/ archive can be supported. |
| 3 | `BLOB_HANDLE` | VARCHAR(255) |  |  | Indicating the actual location of the image. |
| 4 | `DATASET_REF_ID` | DOUBLE | NOT NULL |  | Unique identifier for each row of data in the Proview SOP table. |
| 5 | `DATASET_UID` | VARCHAR(512) | NOT NULL |  | Unique identifier that identifies the image (SOP Instance UID) or a study UID or Series UID. This would conform to DICOM standard |
| 6 | `LEVEL_CD` | DOUBLE | NOT NULL |  | Study Level, Series Level, Image Level Identifier |
| 7 | `PARENT_DATASET_REF_ID` | DOUBLE | NOT NULL |  | Parent dataset_ref_id to maintain parent child relationship. |
| 8 | `PARENT_ENTITY_ID` | DOUBLE | NOT NULL |  | Unique identifier of the row in the table defined by Parent Entity Name. |
| 9 | `PARENT_ENTITY_NAME` | VARCHAR(32) |  |  | Identifies a table where additional information about this row could be found |
| 10 | `PERSON_ID` | DOUBLE | NOT NULL | FK→ | This is the value of the unique primary identifier of the person table. It is an internal system assigned number. |
| 11 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 12 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 13 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 14 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 15 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `PERSON_ID` | [PERSON](PERSON.md) | `PERSON_ID` |

