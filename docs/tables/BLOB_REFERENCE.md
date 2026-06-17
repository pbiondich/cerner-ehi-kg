# BLOB_REFERENCE

> This table is used to store a row for each image. In the future it may contain other blob types such as video, sound, or presentation files.

**Description:** blob_reference  
**Table type:** ACTIVITY  
**Primary key:** `BLOB_REF_ID`  
**Columns:** 25  
**Referenced by:** 7 columns

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `BLOB_DT_TM` | DATETIME |  |  | The date and time the blob was created. |
| 2 | `BLOB_FOREIGN_IDENT` | VARCHAR(255) |  |  | The field stores information regarding blob originating from a foreign system. For ex: For PathNet Anatomic Pathology Images that are imported from foreign systems, this column would be used to store information that can be used to get back to the original\source image in the foreign system. |
| 3 | `BLOB_HANDLE` | VARCHAR(255) |  |  | This field contains the unique identifier for the blob data. For AP Images it contains the DICOM UID string for the image. |
| 4 | `BLOB_REF_ID` | DOUBLE | NOT NULL | PK | This field is the unique identifier for each blob_reference row. |
| 5 | `BLOB_TITLE` | VARCHAR(255) |  |  | This field contains the display name for the blob_reference row. |
| 6 | `BLOB_TYPE_CD` | DOUBLE | NOT NULL |  | This field contains a reference to code set 26820 which provides more information about the type of blob stored. For example, drivers license, consent form, requisition, etc. |
| 7 | `CHARTABLE_NOTE_ID` | DOUBLE | NOT NULL |  | This field contains the id of the long_text table row that contains the chartable note for the specific blob_reference row. |
| 8 | `CREATE_PRSNL_ID` | DOUBLE | NOT NULL | FK→ | This field contains the personnel id for the person who added this blob_reference row. |
| 9 | `DOCUMENT_ID` | DOUBLE | NOT NULL | FK→ | Uniquely identifies a logical document. There may be more than one row with the same document_id, but only one of those rows will be current as indicated by the valid_until_dt_tm field. |
| 10 | `FORMAT_CD` | DOUBLE | NOT NULL |  | This field contains the storage format identifier for a specific blob_reference row. |
| 11 | `NON_CHARTABLE_NOTE_ID` | DOUBLE | NOT NULL |  | This field contains the id of the long_text table row that contains the non-chartable note for the specific blob_reference ro |
| 12 | `OWNER_CD` | DOUBLE | NOT NULL |  | This is field is currently not used. In the future it may hold an identifier of the team that owns the blob_reference row. |
| 13 | `PARENT_ENTITY_ID` | DOUBLE | NOT NULL |  | This field contains an identifier for the parent table row. |
| 14 | `PARENT_ENTITY_NAME` | VARCHAR(32) |  |  | This field contains the name of table that this blob_reference row is associated to. |
| 15 | `PUBLISH_FLAG` | DOUBLE | NOT NULL |  | This field indicates whether or not this blob data should be published. |
| 16 | `SEQUENCE_NBR` | DOUBLE | NOT NULL |  | This field contains the display ordering for this blob_reference row. |
| 17 | `SOURCE_DEVICE_CD` | DOUBLE | NOT NULL |  | This field contains the unique identifier of the device that was used to capture the corresponding blob data. |
| 18 | `STORAGE_CD` | DOUBLE | NOT NULL |  | This field contains the unique identifier to indicate where the blob data is stored. |
| 19 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 20 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 21 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 22 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 23 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |
| 24 | `VALID_FROM_DT_TM` | DATETIME | NOT NULL |  | This field contains the "Beginning Point" of when a row in the table is valid. |
| 25 | `VALID_UNTIL_DT_TM` | DATETIME | NOT NULL |  | This field contains the "End Point" of when a row in the table is valid. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `CREATE_PRSNL_ID` | [PRSNL](PRSNL.md) | `PERSON_ID` |
| `DOCUMENT_ID` | [BLOB_REFERENCE](BLOB_REFERENCE.md) | `BLOB_REF_ID` |

## Referenced by (7)

| From table | Column |
|------------|--------|
| [BLOB_REFERENCE](BLOB_REFERENCE.md) | `DOCUMENT_ID` |
| [CDI_FORM_ACTIVITY](CDI_FORM_ACTIVITY.md) | `BLOB_REF_ID` |
| [CDI_TRANS_LOG](CDI_TRANS_LOG.md) | `BLOB_REF_ID` |
| [PFT_QUEUE_ITEM](PFT_QUEUE_ITEM.md) | `BLOB_REF_ID` |
| [PFT_QUEUE_ITEM_HIST](PFT_QUEUE_ITEM_HIST.md) | `BLOB_REF_ID` |
| [PPR_CONSENT_POLICY](PPR_CONSENT_POLICY.md) | `BLOB_REF_SCAN_ID` |
| [PPR_CONSENT_STATUS](PPR_CONSENT_STATUS.md) | `BLOB_REF_SCAN_ID` |

