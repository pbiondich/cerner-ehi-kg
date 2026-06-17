# AP_IMAGE_MIGRATED

> This table contains records of image blobs migrated from DICOM to MMF.

**Description:** AP Image Migrated  
**Table type:** ACTIVITY  
**Primary key:** _(not published — see note)_  
**Columns:** 10

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `AP_IMAGE_MIGRATED_ID` | DOUBLE | NOT NULL |  | Uniquely identifies a given migrated image. |
| 2 | `CASE_ID` | DOUBLE | NOT NULL | FK→ | Uniquely identifies the Pathology Case related to this migrated image. |
| 3 | `DICOM_BLOB_HANDLE_IDENT` | VARCHAR(255) | NOT NULL |  | This stores the identifier with which the image was stored in DICOM. |
| 4 | `ENTITY_ID` | DOUBLE | NOT NULL | FK→ | Uniquely stores the identifier of the ap discrete entity related to this migrated image. |
| 5 | `MMF_BLOB_HANDLE_IDENT` | VARCHAR(255) | NOT NULL |  | Stores the identifier of the image stored in MMF. |
| 6 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 7 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 8 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 9 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 10 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `CASE_ID` | [PATHOLOGY_CASE](PATHOLOGY_CASE.md) | `CASE_ID` |
| `ENTITY_ID` | [AP_DISCRETE_ENTITY](AP_DISCRETE_ENTITY.md) | `ENTITY_ID` |

